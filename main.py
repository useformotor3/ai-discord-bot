from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import json
import os
import subprocess
import time
from google import genai
import requests
import uuid

from cra_source import fetch_official_cra_source, validate_research_report

from persistence import (
    commit_persistence_transaction,
    read_optional_bytes,
    recover_pending_transactions,
)

# 0. 파일 경로 설정
STATE_FILE = "state.json"
HISTORY_FILE = "history.json"
SEOUL = ZoneInfo("Asia/Seoul")
NOW = datetime.now(SEOUL)
TODAY = NOW.strftime("%Y-%m-%d")
_UNSET = object()

def load_state(path, today, raw_bytes=_UNSET):
  """상태파일을 검증해 읽는다. 손상된 파일은 초기화하지 않고 안전 실패한다."""
  if raw_bytes is _UNSET:
    if not os.path.exists(path):
      return {
          "date": today,
          "count": 0,
          "last_health_check": NOW.isoformat(),
      }
    try:
      with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
      raise SystemExit(
          f"❌ [상태파일 오류] {path}를 읽을 수 없습니다. 원본을 보존하고 종료합니다."
      ) from exc
  elif raw_bytes is None:
    return {
        "date": today,
        "count": 0,
        "last_health_check": NOW.isoformat(),
    }
  else:
    try:
      data = json.loads(raw_bytes.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
      raise SystemExit(
        f"❌ [상태파일 오류] {path}를 읽을 수 없습니다. 원본을 보존하고 종료합니다."
    ) from exc

  if not isinstance(data, dict):
    raise SystemExit(
        f"❌ [상태파일 오류] {path}의 최상위 구조가 객체가 아닙니다. 원본을 보존하고 종료합니다."
    )

  stored_date = data.get("date")
  if not isinstance(stored_date, str):
    raise SystemExit(
        f"❌ [상태파일 오류] {path}의 date 필드가 없거나 문자열이 아닙니다."
    )
  try:
    datetime.strptime(stored_date, "%Y-%m-%d")
  except ValueError as exc:
    raise SystemExit(
        f"❌ [상태파일 오류] {path}의 date 형식이 올바르지 않습니다."
    ) from exc

  count = data.get("count")
  if isinstance(count, bool) or not isinstance(count, int) or count < 0:
    raise SystemExit(
        f"❌ [상태파일 오류] {path}의 count는 0 이상의 정수여야 합니다."
    )

  last_check = data.get("last_health_check")
  if last_check is not None:
    if not isinstance(last_check, str):
      raise SystemExit(
          f"❌ [상태파일 오류] {path}의 last_health_check는 ISO 날짜 문자열이어야 합니다."
      )
    try:
      datetime.fromisoformat(last_check)
    except ValueError as exc:
      raise SystemExit(
          f"❌ [상태파일 오류] {path}의 last_health_check 날짜 형식이 올바르지 않습니다."
      ) from exc

  if stored_date != today:
    data["date"] = today
    data["count"] = 0
  return data


def load_history(path, raw_bytes=_UNSET):
  """이력파일의 JSON과 항목 구조를 검증한다. 손상된 이력은 빈 목록으로 대체하지 않는다."""
  if raw_bytes is _UNSET:
    if not os.path.exists(path):
      return []
    try:
      with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
      raise SystemExit(
          f"❌ [이력파일 오류] {path}를 읽을 수 없습니다. 원본을 보존하고 종료합니다."
      ) from exc
  elif raw_bytes is None:
    return []
  else:
    try:
      data = json.loads(raw_bytes.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
      raise SystemExit(
        f"❌ [이력파일 오류] {path}를 읽을 수 없습니다. 원본을 보존하고 종료합니다."
    ) from exc

  if not isinstance(data, list):
    raise SystemExit(
        f"❌ [이력파일 오류] {path}의 최상위 구조가 배열이 아닙니다. 원본을 보존하고 종료합니다."
    )
  if any(not isinstance(item, dict) for item in data):
    raise SystemExit(
        f"❌ [이력파일 오류] {path}에 객체가 아닌 이력 항목이 있습니다. 원본을 보존하고 종료합니다."
    )
  return data


def parse_health_check(value):
  """ISO datetime을 파싱하고 aware/naive 혼용을 현재 로컬 시간 기준으로 정규화한다."""
  if not value:
    return None
  parsed = datetime.fromisoformat(value)
  # Legacy timestamps were naive UTC values written by GitHub-hosted runners.
  # New values are timezone-aware Asia/Seoul timestamps.
  if parsed.tzinfo is None:
    parsed = parsed.replace(tzinfo=timezone.utc)
  return parsed.astimezone(SEOUL)


# 1. 미완료 로컬 트랜잭션을 먼저 복구하고, 읽은 원본 bytes를 저장 시점까지 추적한다.
recover_pending_transactions(".")
state_snapshot = read_optional_bytes(STATE_FILE)
history_snapshot = read_optional_bytes(HISTORY_FILE)
state_data = load_state(STATE_FILE, TODAY, raw_bytes=state_snapshot)
history_data = load_history(HISTORY_FILE, raw_bytes=history_snapshot)

current_count = state_data["count"]
MAX_DAILY_QUOTA = 1200  # 운영 한도는 별도 공식 정책 확인 필요

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

# 일일 쿼터 초과 시 안전 종료
if current_count >= MAX_DAILY_QUOTA:
  print("⚠️ [쿼터 방어] 일일 허용 횟수 도달. 이번 실행을 건너뜁니다.")
  exit(0)

# 12시간마다 강제 생존신고(Health-Check) 체크
last_check_str = state_data.get("last_health_check")
is_health_check = False
try:
  last_check_time = parse_health_check(last_check_str)
except (TypeError, ValueError) as exc:
  raise SystemExit(
      "❌ [상태파일 오류] last_health_check를 해석할 수 없어 안전 종료합니다."
  ) from exc

if last_check_time is None:
  is_health_check = True
elif (NOW - last_check_time) >= timedelta(hours=12):
  is_health_check = True

# 2. 🧠 [외부 메모리] 검증된 이력의 최근 요약을 조사 프롬프트에 반영
recent_snippets = [item.get("snippet", "") for item in history_data[-5:]]
context_memory = (
    "\n".join([f"- {s}" for s in recent_snippets])
    if recent_snippets
    else "아직 초기 조사 단계입니다."
)

# 3. 공식 CRA 원문을 직접 수집한다. 원문 확보 실패 시 보고서 생성·전송·저장을 중단한다.
try:
  cra_source = fetch_official_cra_source()
except Exception as exc:
  print(f"❌ [공식 원문 수집 실패] CRA 원문을 확인할 수 없어 안전 종료합니다: {exc}")
  raise SystemExit(1) from exc

# 4. Gemini 클라이언트 초기화 및 프롬프트
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = f"""
    당신은 유럽연합(EU) CRA(Cyber Resilience Act) 규격 및 산업용 자동화 보안 최고 전문가입니다.
    산업용 서보 드라이브(Servo Drive) 제조사가 반드시 준수해야 하는 CRA 핵심 요건을 조사하고 있습니다.

    [지금까지 깃허브 외부 메모리에 누적된 이전 조사 내용 (참고용 - 중복 조사 방지)]
    {context_memory}

    아래에 제공된 EUR-Lex 공식 CRA 원문만을 법적 근거의 기준으로 사용하세요. 원문에 없는 표준·가이드·제조사 관행을 법적 의무로 추가하지 마세요.
    원문에서 확인 가능한 조항을 주제로 선정하고, 원문에 근거가 부족하면 억지로 주제를 만들지 말고 조사 공백으로 명시하세요.
    각 법적 주장은 정확한 Article/Annex/point를 표시하고, 원문 인용은 아래 원문에서 연속된 문장을 50자 이상 그대로 복사해 큰따옴표로 감싸세요. 인용을 번역·요약·재구성하지 마세요.
    법적 의무, 공식 설명, 엔지니어링 권고를 명확히 구분하고 제품 적용성은 별도 확인이 필요하다고 표시하세요.

    [EUR-Lex 공식 원문 URL]
    {cra_source['url']}
    [공식 원문 텍스트]
    {cra_source['text']}

    [작성 양식]
    1. 주제 요약: (핵심 내용 2줄)
    2. 규격 근거 및 상세 내용: (CRA 조항 또는 산업 표준 기준의 구체적 설명)
    3. 출처 자료(Source): Regulation (EU) 2024/2847, EUR-Lex 공식 URL을 정확히 기재
    4. 출처 원문 텍스트(Raw Text Quote): 위 공식 원문에서 50자 이상 연속된 실제 문장을 큰따옴표로 직접 인용
    """

# 4. 모델 폴백 & 재시도 픽서 로직 (Latest ➔ Lite)
models_to_try = ["gemini-3.8-flash", "gemini-3.5-flash-lite"]
ai_message = ""
success = False

for model_name in models_to_try:
  max_retries = 3
  retry_delay = 5
  print(f"🔍 모델 [{model_name}]으로 조사를 시도합니다.")

  for attempt in range(1, max_retries + 1):
    try:
      response = client.models.generate_content(
          model=model_name, contents=prompt
      )
      candidate = response.text if response and response.text else ""
      is_valid, validation_reason = validate_research_report(candidate, cra_source)
      if is_valid:
        ai_message = candidate.strip()
        success = True
        break
      print(
          f"모델 {model_name} 시도 {attempt} 무효 응답: "
          f"{validation_reason}"
      )
      if attempt < max_retries:
        time.sleep(retry_delay)
    except Exception as e:
      status_code = getattr(e, "status_code", None)
      if status_code is None:
        status_code = getattr(e, "code", None)
      if status_code is None:
        status_code = getattr(getattr(e, "response", None), "status_code", None)
      if status_code == 404 or str(status_code).upper() in ("404", "NOT_FOUND"):
        print(f"모델 {model_name}을 사용할 수 없습니다(404). 재시도 없이 다음 모델로 전환합니다.")
        break
      print(f"모델 {model_name} 시도 {attempt} 실패: {str(e)}")
      if attempt < max_retries:
        time.sleep(retry_delay)

  if success:
    break

if not success:
  print(
      "❌ [조사 실패] 모든 모델 호출이 실패했거나 응답 검증을 통과하지 "
      "못했습니다. 이번 실행은 전송·아카이브·카운트 증가 없이 종료합니다."
  )
  raise SystemExit(1)

# 5. 디스코드 분할 전송 (2000자 제한 방어)
title_prefix = (
    "🟢 **[12시간 시스템 생존신고 & 정기 헬스체크]**"
    if is_health_check
    else "🛡️ **[CRA 조사 초안: EUR-Lex 원문 인용 대조 통과 / 법률 해석 미검증]**"
)

full_text = (
    f"{title_prefix} (오늘 누적 횟수: {current_count + 1})\n\n{ai_message}"
)


DISCORD_CONNECT_TIMEOUT_SECONDS = 3.05
DISCORD_READ_TIMEOUT_SECONDS = 10
MAX_DISCORD_RETRIES = 2
MAX_DISCORD_RETRY_WAIT_SECONDS = 30


def _discord_retry_after_seconds(response):
  """Discord 429의 Retry-After 또는 JSON retry_after 값을 초 단위로 읽는다."""
  header_value = None
  for key, value in getattr(response, "headers", {}).items():
    if key.lower() == "retry-after":
      header_value = value
      break
  candidates = [header_value]
  try:
    body = response.json()
  except Exception:
    body = {}
  if isinstance(body, dict):
    candidates.append(body.get("retry_after"))
  for candidate in candidates:
    if candidate is None:
      continue
    try:
      delay = float(candidate)
    except (TypeError, ValueError):
      continue
    if delay >= 0:
      return delay
  return None


def send_discord_chunked(text, webhook_url):
  """Discord 전송을 chunk별로 확인하고 모호한 POST 결과는 재전송하지 않는다."""
  if not webhook_url:
    return {"status": "skipped", "chunks": [], "sent_chunks": 0, "total_chunks": 0}
  max_len = 1900
  chunks = [text[i : i + max_len] for i in range(0, len(text), max_len)]
  chunk_results = []
  sent_chunks = 0

  def finish(failure_status, chunk_index, status_code=None):
    chunk_result = {"index": chunk_index + 1, "status": failure_status}
    if status_code is not None:
      chunk_result["http_status"] = status_code
    chunk_results.append(chunk_result)
    overall = "partial" if sent_chunks else failure_status
    return {
        "status": overall,
        "chunks": chunk_results,
        "sent_chunks": sent_chunks,
        "total_chunks": len(chunks),
    }

  for idx, chunk in enumerate(chunks):
    msg = chunk
    if len(chunks) > 1:
      msg = f"(파트 {idx+1}/{len(chunks)})\n" + msg
    payload = {"content": msg}
    chunk_sent = False
    for attempt in range(MAX_DISCORD_RETRIES + 1):
      try:
        response = requests.post(
            webhook_url,
            json=payload,
            params={"wait": "true"},
            timeout=(DISCORD_CONNECT_TIMEOUT_SECONDS, DISCORD_READ_TIMEOUT_SECONDS),
        )
      except requests.exceptions.ConnectTimeout:
        if attempt < MAX_DISCORD_RETRIES:
          continue
        return finish("failed", idx)
      except (
          requests.exceptions.ReadTimeout,
          requests.exceptions.ConnectionError,
          requests.exceptions.Timeout,
          requests.exceptions.RequestException,
      ):
        return finish("delivery_unknown", idx)

      status_code = response.status_code
      if status_code == 429:
        retry_after = _discord_retry_after_seconds(response)
        if (
            attempt >= MAX_DISCORD_RETRIES
            or retry_after is None
            or retry_after > MAX_DISCORD_RETRY_WAIT_SECONDS
        ):
          return finish("deferred", idx, status_code)
        time.sleep(retry_after)
        continue
      if status_code in (400, 401, 403, 404):
        return finish("permanent_failure", idx, status_code)
      if 500 <= status_code <= 599:
        return finish("delivery_unknown", idx, status_code)
      if not 200 <= status_code <= 299:
        return finish("permanent_failure", idx, status_code)
      try:
        response_body = response.json()
      except Exception:
        response_body = None
      message_id = response_body.get("id") if isinstance(response_body, dict) else None
      if not message_id:
        return finish("delivery_unknown", idx, status_code)
      chunk_results.append({
          "index": idx + 1,
          "status": "sent",
          "message_id": str(message_id),
          "http_status": status_code,
      })
      sent_chunks += 1
      chunk_sent = True
      break
    if not chunk_sent:
      return finish("deferred", idx)
    if idx < len(chunks) - 1:
      time.sleep(1)
  return {
      "status": "sent",
      "chunks": chunk_results,
      "sent_chunks": sent_chunks,
      "total_chunks": len(chunks),
  }


discord_result = send_discord_chunked(full_text, webhook_url)
print(f"Discord 전송 결과: {discord_result['status']} ({discord_result['sent_chunks']}/{discord_result['total_chunks']} chunks 확인)")

# 6. GitHub 백서버 저장 (폴더별 마크다운 아카이브 & 상태 업데이트)
archive_filename = (
    f"research_archive/{TODAY}_{NOW.strftime('%H%M%S%f')}_{uuid.uuid4().hex[:8]}.md"
)
archive_payload = (
    f"# CRA Research Draft\n- **Evidence gate:** EUR-Lex official source fetched; Article/Annex locator and at least one verbatim quote matched. Legal interpretation and product applicability remain unverified.\n- **Source URL:** {cra_source['url']}\n- **Source checked at:** {NOW.isoformat()}\n- **Date:** {TODAY} {NOW.strftime('%H:%M:%S')}\n-"
    f" **Count:** {current_count + 1}\n\n{ai_message}"
).encode("utf-8")

state_data["count"] = current_count + 1
if is_health_check:
  state_data["last_health_check"] = NOW.isoformat()

history_data.append({
    "date": TODAY,
    "time": NOW.strftime("%H:%M:%S"),
    "count": state_data["count"],
    "snippet": ai_message[:150],
    "file": archive_filename,
})

state_payload = json.dumps(state_data, indent=2, ensure_ascii=False).encode("utf-8")
history_payload = json.dumps(history_data, indent=2, ensure_ascii=False).encode("utf-8")
transaction_id = commit_persistence_transaction(
    ".",
    [
        {
            "target": archive_filename,
            "payload": archive_payload,
            "expected_old": None,
        },
        {
            "target": HISTORY_FILE,
            "payload": history_payload,
            "expected_old": history_snapshot,
        },
        {
            "target": STATE_FILE,
            "payload": state_payload,
            "expected_old": state_snapshot,
        },
    ],
)
print(f"로컬 저장 트랜잭션 완료: {transaction_id}")

# 7. 🚀 [엔터프라이즈 기능] 변경된 아카이브 파일들을 깃허브에 자동 커밋 & 푸시
try:
  subprocess.run(["git", "config", "--global", "user.name", "CRA-Research-Bot"], check=True)
  subprocess.run(["git", "config", "--global", "user.email", "bot@users.noreply.github.com"], check=True)
  subprocess.run(["git", "add", "state.json", "history.json", "research_archive/"], check=True)
  subprocess.run(["git", "commit", "-m", f"Auto-archive: Research report #{current_count + 1}"], check=True)
  subprocess.run(["git", "push"], check=True)
  print("🚀 깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다.")
except Exception as e:
  print(f"❌ GitHub 운영 데이터 저장 실패: {str(e)}. 원격 저장 성공으로 처리하지 않고 실행을 실패시킵니다.")
  raise SystemExit(1) from e
