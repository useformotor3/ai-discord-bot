from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import json
import os
import re
import unicodedata
import subprocess
import time
from google import genai
import requests
import uuid

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
recent_snippets = [item.get("snippet", "") for item in history_data[-15:]]
context_memory = (
    "\n".join([f"- {s}" for s in recent_snippets])
    if recent_snippets
    else "아직 초기 조사 단계입니다."
)

# 3. Gemini 클라이언트 초기화 및 프롬프트
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = f"""
    당신은 유럽연합(EU) CRA(Cyber Resilience Act) 규격 및 산업용 자동화 보안 최고 전문가입니다.
    산업용 서보 드라이브(Servo Drive) 제조사가 반드시 준수해야 하는 CRA 핵심 요건을 조사하고 있습니다.

    [지금까지 깃허브 외부 메모리에 누적된 이전 조사 내용 (참고용 - 중복 조사 방지)]
    {context_memory}

    위의 이전 내용들과 중복되지 않으면서, 아직 다루지 않은 더 발전되거나 세부적인 CRA 핵심 주제(예: 취약점 무상 패치, Secure by default, 기술 문서, SBOM, 생명주기 관리 등)를 깊이 있게 선정하여 아래 4가지 양식에 맞추어 엄격하게 조사하고 작성해 주세요.
    추측성 내용은 절대 배제하고, 실제 EU 규정 조항이나 공식 가이드라인을 기반으로 높은 품질의 전문적인 내용을 작성하세요.

    [필수 출처·정확성 규칙]
    - CRA 법적 주장에는 Regulation (EU) 2024/2847의 최종 Official Journal 원문을 우선 사용하세요.
    - 출처 자료에 다음 공식 원문 링크를 반드시 포함하세요: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
    - 조항 번호와 제목을 확인하고, 원문에 없는 구현 방식을 법적 의무로 표현하지 마세요.
    - 원문을 직접 확인하지 못한 문장은 직접 인용으로 꾸미지 말고 '요약/해석'으로 구분하세요.
    - 최근 조사 주제와 겹치면 억지로 새 주제를 만들지 말고 '추가로 검증할 신규 주제 없음'을 반환하세요.
    [작성 양식]
    1. 주제 요약: (핵심 내용 2줄)
    2. 규격 근거 및 상세 내용: (CRA 조항 또는 산업 표준 기준의 구체적 설명)
    3. 출처 자료(Source): (참고한 공식 EU 규정 문서명, 웹사이트 이름 또는 표준 규격 명칭과 URL)
    4. 출처 원문 텍스트(Raw Text Quote): (해당 출처에서 직접 확인한 실제 원문 문장. 직접 확인하지 못한 경우 인용문을 만들지 말 것)
    """

def validate_research_report(text):
  """프롬프트가 요구한 최소 보고서 구조를 확인한다. 정확성 검증과는 별개다."""
  if not isinstance(text, str):
    return False, "응답이 문자열이 아닙니다."

  report = text.strip()
  if len(report) < 250:
    return False, "응답 길이가 최소 기준(250자)에 미달합니다."

  lowered = report.lower()
  required_sections = [
      ("주제 요약",),
      ("규격 근거", "상세 내용"),
      ("출처 자료", "source:"),
      ("출처 원문", "raw text quote"),
  ]
  for alternatives in required_sections:
    if not any(marker in lowered for marker in alternatives):
      return False, f"필수 보고서 항목 누락: {' / '.join(alternatives)}"

  error_markers = [
      "시스템 긴급 경고",
      "모든 ai 모델",
      "temporarily unavailable",
      "quota exceeded",
      "rate limit exceeded",
      "internal server error",
      "resource_exhausted",
      "permission_denied",
      "service unavailable",
      "요청 처리에 실패",
      "응답 생성에 실패",
      "조사를 완료하지 못했습니다",
  ]
  if any(marker.lower() in lowered for marker in error_markers):
    return False, "오류 또는 서비스 장애 문구가 보고서에 포함되어 있습니다."

  # CRA 관련 법적 주장은 공식 EUR-Lex 법령 링크를 포함해야 한다.
  has_official_cra_source = (
      "eur-lex.europa.eu" in lowered
      and ("2024/2847" in lowered or "32024r2847" in lowered)
  )
  if not has_official_cra_source:
    return False, "CRA 공식 EUR-Lex 원문 링크가 누락되었습니다."

  return True, ""


def _topic_tokens(text):
  """보고서 서두에서 주제어를 추출하고 한국어 조사/일반 용어를 정규화한다."""
  normalized = unicodedata.normalize("NFKC", text[:1800]).lower()
  raw_tokens = re.findall(r"[가-힣]{2,}|[a-z][a-z0-9_-]{1,}", normalized)
  stopwords = {
      "서보", "드라이브", "산업용", "제조사", "제품", "디지털", "요구사항",
      "규정", "보안", "법적", "의무", "핵심", "관련", "기준", "통해",
      "경우", "대한", "위한", "있다", "한다", "해야", "있으며", "포함",
      "cra", "cyber", "resilience", "act", "european", "union", "digital",
      "elements", "the", "and", "for", "with", "from", "this", "that",
      "shall", "where", "such", "including", "section", "article",
      "주제", "요약", "규격", "근거", "상세", "내용", "출처", "자료",
      "원문", "텍스트", "문서", "제공", "사용자", "따라", "통해",
  }
  suffixes = (
      "으로부터", "으로서", "으로", "에서", "에게", "부터", "까지",
      "처럼", "에는", "에도", "이며", "이고", "은", "는", "이", "가",
      "을", "를", "의", "에", "와", "과", "도", "로", "만", "적",
  )
  synonyms = {
      "무료": "free", "무상": "free", "free-of-charge": "free",
      "취약점": "vulnerability", "취약성": "vulnerability",
      "처리": "handling", "관리": "handling", "핸들링": "handling",
      "업데이트": "update", "업데이트들": "update", "패치": "patch",
      "시정": "correction", "교정": "correction",
  }
  tokens = set()
  for token in raw_tokens:
    for suffix in suffixes:
      if token.endswith(suffix) and len(token) - len(suffix) >= 2:
        token = token[:-len(suffix)]
        break
    token = synonyms.get(token, token)
    if len(token) >= 2 and token not in stopwords:
      tokens.add(token)
  return tokens


def find_duplicate_topic(report, history, root="."):
  """최근 30개 원문과 주제어 중복을 비교해 유사 보고서 저장을 차단한다."""
  candidate = _topic_tokens(report)
  if len(candidate) < 5:
    return None
  for item in reversed(history[-30:]):
    relative = item.get("file") if isinstance(item, dict) else None
    if not isinstance(relative, str):
      continue
    if relative.startswith("/") or ".." in relative.split("/"):
      continue
    if not relative.startswith("research_archive/") or not relative.endswith(".md"):
      continue
    try:
      with open(relative, "r", encoding="utf-8") as stream:
        previous = _topic_tokens(stream.read())
    except (OSError, UnicodeError):
      continue
    if len(previous) < 5:
      continue
    overlap = candidate & previous
    union = candidate | previous
    similarity = len(overlap) / len(union) if union else 0.0
    containment = len(overlap) / min(len(candidate), len(previous))
    if len(overlap) >= 5 and (similarity >= 0.22 or containment >= 0.60):
      return {
          "file": relative,
          "overlap_terms": sorted(overlap),
          "jaccard": round(similarity, 3),
          "containment": round(containment, 3),
      }
  return None


# 4. 모델 폴백 & 재시도 픽서 로직 (Latest ➔ Lite)
models_to_try = ["gemini-3.8-flash", "gemini-3.5-flash-lite"]
ai_message = ""
success = False
quota_exhausted = False
transient_unavailable = False
quality_rejected = False
fatal_model_error = False

for model_name in models_to_try:
  max_retries = 2
  retry_delay = 5
  print(f"🔍 모델 [{model_name}]으로 조사를 시도합니다.")

  for attempt in range(1, max_retries + 1):
    try:
      response = client.models.generate_content(
          model=model_name, contents=prompt
      )
      candidate = response.text if response and response.text else ""
      is_valid, validation_reason = validate_research_report(candidate)
      if is_valid:
        duplicate = find_duplicate_topic(candidate, history_data)
        if duplicate:
          print(
              "⚠️ [중복 주제 차단] 최근 보고서와 주제 중복이 감지되어 "
              f"Discord 전송 및 아카이브를 생략합니다: {duplicate}"
          )
          raise SystemExit(0)
        ai_message = candidate.strip()
        success = True
        break
      quality_rejected = True
      print(
          f"모델 {model_name} 시도 {attempt} 무효 응답: "
          f"{validation_reason}"
      )
      # 공식 법령 링크 누락은 같은 모델에 반복 요청해도 보완되지 않는 경우가 많다.
      if "EUR-Lex" in validation_reason:
        break
      if attempt < max_retries:
        time.sleep(retry_delay)
    except Exception as e:
      status_code = getattr(e, "status_code", None)
      if status_code is None:
        status_code = getattr(e, "code", None)
      if status_code is None:
        status_code = getattr(getattr(e, "response", None), "status_code", None)
      error_text = str(e).lower()
      if status_code == 404 or str(status_code).upper() in ("404", "NOT_FOUND"):
        print(f"모델 {model_name}을 사용할 수 없습니다(404). 재시도 없이 다음 모델로 전환합니다.")
        break
      if status_code == 429 or "429 resource_exhausted" in error_text:
        quota_exhausted = True
        print(
            f"⚠️ 모델 {model_name} 할당량/요청 제한(429). "
            "동일 모델 재시도를 중단하고 대체 모델로 전환합니다."
        )
        break
      if status_code == 503 or "503 unavailable" in error_text:
        transient_unavailable = True
        print(
            f"⚠️ 모델 {model_name} 일시적 과부하(503). "
            "동일 모델 재시도를 중단하고 대체 모델로 전환합니다."
        )
        break
      fatal_model_error = True
      print(f"모델 {model_name} 시도 {attempt} 실패: {str(e)}")
      if attempt < max_retries:
        time.sleep(retry_delay)

  if success:
    break

if not success:
  if not fatal_model_error and (
      quota_exhausted or transient_unavailable or quality_rejected
  ):
    print(
        "⚠️ [조사 보류] Gemini 할당량/일시 장애 또는 보고서 품질 검증 "
        "실패로 이번 실행을 정상 건너뜁니다. 전송·아카이브·카운트는 변경하지 않습니다."
    )
    raise SystemExit(0)
  print(
      "❌ [조사 실패] 인증/설정 등 복구가 필요한 오류로 모든 모델 호출이 "
      "실패했습니다. 전송·아카이브·카운트 증가 없이 종료합니다."
  )
  raise SystemExit(1)

# 5. 디스코드 분할 전송 (2000자 제한 방어)
title_prefix = (
    "🟢 **[12시간 시스템 생존신고 & 정기 헬스체크]**"
    if is_health_check
    else "🛡️ **[CRA 규격 심층 조사 및 근거 리포트]**"
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


# 6. GitHub 백서버 저장 (폴더별 마크다운 아카이브 & 상태 업데이트)
archive_filename = (
    f"research_archive/{TODAY}_{NOW.strftime('%H%M%S%f')}_{uuid.uuid4().hex[:8]}.md"
)
archive_payload = (
    f"# CRA Research Report\n- **Date:** {TODAY} {NOW.strftime('%H:%M:%S')}\n-"
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

# Discord 전송은 원격 archive/state/history commit이 성공한 뒤 수행한다.
# 전송 실패 시에도 보고서 원본은 GitHub에 안전하게 보존된다.
discord_result = send_discord_chunked(full_text, webhook_url)
print(
    f"Discord 전송 결과: {discord_result['status']} "
    f"({discord_result['sent_chunks']}/{discord_result['total_chunks']} chunks 확인)"
)
