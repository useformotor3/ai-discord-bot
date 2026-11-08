from datetime import datetime
import json
import os
from google import genai
import requests

# 0. 날짜 및 사용량 관리용 설정 파일 경로
STATE_FILE = "state.json"
TODAY = datetime.now().strftime("%Y-%m-%d")

# 1. state.json 읽기 및 쿼터(사용량) 체크
try:
  if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
      state_data = json.load(f)
  else:
    state_data = {"date": TODAY, "count": 0}
except Exception:
  state_data = {"date": TODAY, "count": 0}

# 날짜가 바뀌었으면 카운트 초기화
if state_data.get("date") != TODAY:
  state_data["date"] = TODAY
  state_data["count"] = 0

# 일일 안전 제한 설정 (무료 티어 1,500회 중 안전하게 1,000회까지만 허용)
MAX_DAILY_QUOTA = 1000

if state_data["count"] >= MAX_DAILY_QUOTA:
  print(
      "⚠️ [쿼터 초과 방어] 오늘 일일 최대 실행 횟수에 도달하여 스크립트를"
      " 종료합니다."
  )
  exit(0)

try:
  # 2. Gemini API 클라이언트 초기화
  client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

  # 3. 엄격한 규격 조사 프롬프트 (근거, 출처, 원문 필수)
  prompt = """
    당신은 유럽연합(EU) CRA(Cyber Resilience Act) 규격 및 산업용 자동화 보안 전문가입니다.
    산업용 서보 드라이브(Servo Drive) 제조사가 반드시 준수해야 하는 
    CRA 핵심 요건(취약점 무상 패치, Secure by default, 기술 문서 등) 중 
    하나를 선정하여 아래 4가지 양식에 맞추어 엄격하게 조사하고 작성해 주세요.
    추측성 내용은 배제하고 실제 EU 규격 기준이나 공식 가이드라인을 기반으로 작성하세요.

    [작성 양식]
    1. 주제 요약: (핵심 내용 2줄)
    2. 규격 근거 및 상세 내용: (CRA 조항 또는 산업 표준 기준의 구체적 설명)
    3. 출처 자료(Source): (참고한 공식 EU 규정 문서명, 웹사이트 이름 또는 표준 규격 명칭)
    4. 출처 원문 텍스트(Raw Text Quote): (해당 출처에서 인용하거나 근거로 삼은 실제 원문 문장 또는 규정 조항의 텍스트)
    """

  # 4. Gemini 모델 호출 (최신 Flash 모델 사용)
  response = client.models.generate_content(
      model="gemini-flash-latest", contents=prompt
  )

  if not response or not response.text:
    ai_message = (
        "⚠️ [시스템 경고] AI가 응답을 생성하지 못했거나 안전 필터에"
        " 걸렸습니다."
    )
  else:
    ai_message = response.text

except Exception as e:
  ai_message = f"❌ [에러 발생] 코드 실행 중 오류가 발생했습니다: {str(e)}"

# 5. 디스코드 전송 (2000자 제한 방어)
webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
if len(ai_message) > 1900:
  ai_message = ai_message[:1900] + "\n...(내용이 길어 일부 생략됨)"

payload = {
    "content": (
        f"🛡️ **[CRA 규격 심층 조사 및 근거 리포트]** (오늘 실행 횟수:"
        f" {state_data['count'] + 1})\n\n{ai_message}"
    )
}
requests.post(webhook_url, json=payload)

# 6. 사용량 카운트 증가 및 state.json 파일 업데이트 (로컬 저장 후 Git Push 자동화 준비)
state_data["count"] += 1
with open(STATE_FILE, "w", encoding="utf-8") as f:
  json.dump(state_data, f, indent=2, ensure_ascii=False)
