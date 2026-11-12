from datetime import datetime, timedelta
import json
import os
import subprocess
import time
from google import genai
from google.genai import types
import requests

from cra_report_contract import ReportGenerationError, generate_validated_report

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

# 3. Gemini 클라이언트 초기화 및 버전 관리 프롬프트 로드
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
PROMPT_FILE = "prompts/CRA_RESEARCH_PROMPT_V2.txt"
with open(PROMPT_FILE, "r", encoding="utf-8") as f:
  prompt = f.read()

# 4. JSON 계약 검증을 포함한 모델 폴백. 유효한 결과가 없으면 저장/게시 전에 중단.
models_to_try = ["gemini-flash-latest", "gemini-3.5-flash-lite"]
try:
  report_payload, ai_message, selected_model = generate_validated_report(
      client=client,
      models=models_to_try,
      prompt=prompt,
      config_factory=types.GenerateContentConfig,
      max_retries=3,
      retry_delay=5,
      sleeper=time.sleep,
      logger=print,
  )
  print(f"Validated CRA draft generated with model: {selected_model}")
except ReportGenerationError as e:
  # Fail closed: do not enter Discord/archive/state/history success path.
  print(f"FAIL-CLOSED: {e}")
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
