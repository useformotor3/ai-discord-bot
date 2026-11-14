from datetime import datetime, timedelta
import json
import os
import subprocess
import time
from google import genai
import requests

# 0. 파일 경로 설정
STATE_FILE = "state.json"
HISTORY_FILE = "history.json"
TODAY = datetime.now().strftime("%Y-%m-%d")
NOW = datetime.now()

# 1. state.json 읽기 및 일일 쿼터 체크
try:
  if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
      state_data = json.load(f)
  else:
    state_data = {
        "date": TODAY,
        "count": 0,
        "last_health_check": datetime.now().isoformat(),
    }
except Exception:
  state_data = {"date": TODAY, "count": 0}

if state_data.get("date") != TODAY:
  state_data["date"] = TODAY
  state_data["count"] = 0

current_count = state_data["count"]
MAX_DAILY_QUOTA = 1200  # 무료 티어 안전 마진

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

# 일일 쿼터 초과 시 안전 종료
if current_count >= MAX_DAILY_QUOTA:
  print("⚠️ [쿼터 방어] 일일 허용 횟수 도달. 이번 실행을 건너뜁니다.")
  exit(0)

# 12시간마다 강제 생존신고(Health-Check) 체크
last_check_str = state_data.get("last_health_check")
is_health_check = False
if last_check_str:
  last_check_time = datetime.fromisoformat(last_check_str)
  if (NOW - last_check_time) >= timedelta(hours=12):
    is_health_check = True
else:
  is_health_check = True

# 2. 🧠 [외부 메모리 읽기] 깃허브에 쌓인 이전 히스토리 불러오기
history_data = []
try:
  if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
      history_data = json.load(f)
except Exception:
  history_data = []

recent_snippets = [item.get("snippet", "") for item in history_data[-5:]]
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

    [작성 양식]
    1. 주제 요약: (핵심 내용 2줄)
    2. 규격 근거 및 상세 내용: (CRA 조항 또는 산업 표준 기준의 구체적 설명)
    3. 출처 자료(Source): (참고한 공식 EU 규정 문서명, 웹사이트 이름 또는 표준 규격 명칭)
    4. 출처 원문 텍스트(Raw Text Quote): (해당 출처에서 인용하거나 근거로 삼은 실제 원문 문장 또는 규정 조항의 텍스트)
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

  return True, ""


# 4. 모델 폴백 & 재시도 픽서 로직 (Latest ➔ Lite)
models_to_try = ["gemini-flash-latest", "gemini-3.5-flash-lite"]
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
      is_valid, validation_reason = validate_research_report(candidate)
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
    else "🛡️ **[CRA 규격 심층 조사 및 근거 리포트]**"
)

full_text = (
    f"{title_prefix} (오늘 누적 횟수: {current_count + 1})\n\n{ai_message}"
)


def send_discord_chunked(text, webhook_url):
  if not webhook_url:
    return
  max_len = 1900
  chunks = [text[i : i + max_len] for i in range(0, len(text), max_len)]
  for idx, chunk in enumerate(chunks):
    msg = chunk
    if len(chunks) > 1:
      msg = f"(파트 {idx+1}/{len(chunks)})\n" + msg
    payload = {"content": msg}
    requests.post(webhook_url, json=payload)
    time.sleep(1)


send_discord_chunked(full_text, webhook_url)

# 6. GitHub 백서버 저장 (폴더별 마크다운 아카이브 & 상태 업데이트)
os.makedirs("research_archive", exist_ok=True)
archive_filename = f"research_archive/{TODAY}_{NOW.strftime('%H%M%S')}.md"
with open(archive_filename, "w", encoding="utf-8") as f:
  f.write(
      f"# CRA Research Report\n- **Date:** {TODAY} {NOW.strftime('%H:%M:%S')}\n-"
      f" **Count:** {current_count + 1}\n\n{ai_message}"
  )

state_data["count"] = current_count + 1
if is_health_check:
  state_data["last_health_check"] = NOW.isoformat()

with open(STATE_FILE, "w", encoding="utf-8") as f:
  json.dump(state_data, f, indent=2, ensure_ascii=False)

history_data.append({
    "date": TODAY,
    "time": NOW.strftime("%H:%M:%S"),
    "count": state_data["count"],
    "snippet": ai_message[:150],
    "file": archive_filename,
})
with open(HISTORY_FILE, "w", encoding="utf-8") as f:
  json.dump(history_data, f, indent=2, ensure_ascii=False)

# 7. 🚀 [엔터프라이즈 기능] 변경된 아카이브 파일들을 깃허브에 자동 커밋 & 푸시
try:
  subprocess.run(["git", "config", "--global", "user.name", "CRA-Research-Bot"], check=True)
  subprocess.run(["git", "config", "--global", "user.email", "bot@users.noreply.github.com"], check=True)
  subprocess.run(["git", "add", "state.json", "history.json", "research_archive/"], check=True)
  subprocess.run(["git", "commit", "-m", f"Auto-archive: Research report #{current_count + 1}"], check=True)
  subprocess.run(["git", "push"], check=True)
  print("🚀 깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다.")
except Exception as e:
  print(f"⚠️ Git Push 생략 또는 변경사항 없음: {str(e)}")
