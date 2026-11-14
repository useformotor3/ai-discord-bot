# 자동화 테스트 가이드

## 목적
- 운영 `main.py`의 핵심 흐름을 격리된 mock 환경에서 검증한다.
- Gemini SDK, Discord HTTP, Git subprocess, sleep을 mock 처리한다.
- 상태파일과 아카이브는 pytest 임시 디렉터리에서만 생성한다.
- 실제 Gemini API, Discord Webhook, Git commit/push는 호출하지 않는다.

## 실행

```bash
python -m pip install pytest
python -m compileall -q main.py tests
python -m pytest -q
```

## 검증 범위
- 정상 보고서 생성 및 Gemini 모델 폴백
- 전체 모델 실패, 짧은 응답, 필수 섹션 누락, 오류 문구 차단
- 실패 시 기존 state/history 보존 및 외부 후속 작업 차단
- `state.json`의 JSON 파싱·필수 필드·자료형·날짜 형식 검증
- `history.json`의 JSON 파싱·최상위 배열·항목 객체 구조 검증
- 손상된 파일의 원본 보존 및 안전 종료
- naive/ timezone-aware `last_health_check` 처리
- mock 경계가 외부 호출을 실제로 가로채는지 검증

## 테스트 결과 해석
- pytest 통과는 mock 환경에서 코드 경로가 기대대로 동작한다는 뜻이다.
- 실제 Gemini·Discord 연동, GitHub Actions 운영 실행, CRA 법령 해석의 정확성을 보증하지 않는다.
- Discord timeout/HTTP status, Git push 실패 상태화, 아카이브 원자적 저장은 P1-B 후속 범위다.
