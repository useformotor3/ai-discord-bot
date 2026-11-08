from datetime import datetime, timedelta
import json
import os
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

# 2. 이전 조사 기록 불러오기
history_data = []
try:
  if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
      history_data = json.load(f)
except Exception:
  history_data = []

# 3. Gemini 클라이언트 초기화 및 프롬프트
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = """
    당신은 유럽연합(EU) CRA(Cyber Resilience Act) 규격 및 산업용 자동화 보안 최고 전문가입니다.
    산업용 서보 드라이브(Servo Drive) 제조사가 반드시 준수해야 하는 
    CRA 핵심 요건(예: 취약점 무상 패치, Secure by default, 기술 문서, SBOM 등) 중 
    아직 다루지 않았을 법한 핵심 주제를 깊이 있게 선정하여 아래 4가지 양식에 맞추어 엄격하게 조사하고 작성해 주세요.
    추측성 내용은 절대 배제하고, 실제 EU 규정 조항이나 공식 가이드라인을 기반으로 높은 품질의 전문적인 내용을 작성하세요.

    [작성 양식]
    1. 주제 요약: (핵심 내용 2줄)
    2. 규격 근거 및 상세 내용: (CRA 조항 또는 산업 표준 기준의 구체적 설명)
    3. 출처 자료(Source): (참고한 공식 EU 규정 문서명, 웹사이트 이름 또는 표준 규격 명칭)
    4. 출처 원문 텍스트(Raw Text Quote): (해당 출처에서 인용하거나 근거로 삼은 실제 원문 문장 또는 규정 조항의 텍스트)
    """

# 4. 모델 폴백 & 재시도 픽서 로직
# 1단계: 최신 모델 (gemini-flash-latest)로 3회 시도
# 2단계: 실패 시 하위 안정 모델 (gemini-3.5-flash-lite)로 3회 추가 시도
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
      if response and response.text:
        ai_message = response.text
        success = True
        break
    except Exception as e:
      print(f"모델 {model_name} 시도 {attempt} 실패: {str(e)}")
      if attempt < max_retries:
        time.sleep(retry_delay)

  if success:
    break  # 성공하면 하위 모델로 넘어가지 않고 탈출

# 모든 모델 실패 시 방어
if not success:
  ai_message = (
      "⚠️ [시스템 긴급 경고] 모든 AI 모델(Latest 및 Lite)의 일시적"
      " 과부하로 이번 회차 조사가 지연되었습니다. 시스템은 정상 대기"
      " 중입니다."
  )
  success = True

# 5. 디스코드 전송 (2000자 제한 방어)
if len(ai_message) > 1900:
  ai_message = ai_message[:1900] + "\n...(내용이 길어 일부 생략됨)"

title_prefix = (
    "🟢 **[12시간 시스템 생존신고 & 정기 헬스체크]**"
    if is_health_check
    else "🛡️ **[CRA 규격 심층 조사 및 근거 리포트]**"
)

payload = {
    "content": (
        f"{title_prefix} (오늘 누적 횟수: {current_count + 1})\n\n{ai_message}"
    )
}
if webhook_url:
  requests.post(webhook_url, json=payload)

# 6. 상태 업데이트 및 기록 저장
state_data["count"] = current_count + 1
if is_health_check:
  state_data["last_health_check"] = NOW.isoformat()

with open(STATE_FILE, "w", encoding="utf-8") as f:
  json.dump(state_data, f, indent=2, ensure_ascii=False)

# 히스토리 기록 추가
history_data.append({
    "date": TODAY,
    "time": NOW.strftime("%H:%M:%S"),
    "count": state_data["count"],
    "snippet": ai_message[:150],
})
with open(HISTORY_FILE, "w", encoding="utf-8") as f:
  json.dump(history_data, f, indent=2, ensure_ascii=False)
