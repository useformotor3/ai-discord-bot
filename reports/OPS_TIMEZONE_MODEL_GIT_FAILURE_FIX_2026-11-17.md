# 운영 시간대·Gemini 모델·Git 저장 실패 처리 개선 — 2026-11-17

## 요약
2026-11-17 운영 점검에서 GitHub-hosted runner의 기본 시간대(UTC)가 CRA 일일 카운트 기준에 사용되고 있음을 확인했다. 한국 시간 기준 일일 카운트가 UTC 자정에 초기화되어 KST 09:00에 하루 경계가 바뀌는 문제가 있다. 또한 Gemini 모델 404 오류도 일시 오류와 동일하게 3회 재시도하고 있었으며, Git push 실패를 경고로만 출력하고 main.py가 성공 종료할 수 있는 구조였다.

## 근거
- GitHub Actions ubuntu-latest runner의 기본 시간대는 UTC이며 workflow에 TZ 설정이 없었다.
- main.py의 TODAY/NOW가 datetime.now()를 사용하고 있어 실행 환경 시간대에 종속됐다.
- 운영 state.json의 date가 2026-11-16인 시점에 KST는 이미 2026-11-17이었다.
- main.py의 모델 목록은 gemini-flash-latest, gemini-3.5-flash-lite였고, 첫 모델의 404에도 고정 3회 재시도했다.
- Git 저장 예외는 warning 출력 후 계속 종료하는 구조였다. 이 경우 Discord 전달은 되었지만 Git 원격 저장이 실패해도 main.py 단독 결과만으로는 성공처럼 보일 수 있다.

## 수정 내용
1. 기준 시간대를 ZoneInfo("Asia/Seoul")로 명시하고 TODAY/NOW 및 신규 기록 시간을 KST로 생성한다.
2. 기존 naive timestamp는 GitHub runner에서 작성된 legacy UTC로 간주해 KST aware datetime으로 변환한다. 신규 health-check timestamp는 timezone-aware ISO 문자열로 저장한다.
3. Gemini 모델 우선순위를 현재 Google Gemini API 공식 모델 카탈로그에 등재된 gemini-3.8-flash → gemini-3.5-flash-lite로 변경한다. 404/NOT_FOUND는 모델을 사용할 수 없는 응답으로 분류해 같은 모델을 재시도하지 않고 다음 모델로 전환한다. 기타 일시 오류는 기존 재시도 정책을 유지한다.
4. Git add/commit/push 중 오류가 발생하면 main.py가 비정상 종료하도록 변경한다. 강제 push, 자동 rebase, 원격 덮어쓰기는 하지 않는다. 원격 저장 실패 시 workflow 실패 및 baseline 보존으로 처리한다.
5. 회귀 테스트: KST 날짜 기준, aware/legacy naive timestamp, 404 즉시 fallback, Git push 실패 시 비정상 종료를 추가/수정한다.

## 검증 경계
- 변경은 GitHub test workflow의 source SHA 검증, compileall, 전체 pytest를 통과해야 한다.
- 실제 Gemini API나 Discord webhook을 호출하지 않는다.
- 첫 운영 실행에서 KST 날짜·count 경계와 정상 push를 관찰하기 전까지 운영 동작 검증 완료로 간주하지 않는다.
- Git push 실패 시 Discord 메시지는 이미 전달되었을 수 있으며 회수할 수 없다. 이 경우 report delivery와 archive persistence가 분리되므로 재전송 전 중복 확인이 필요하다.

## 참고 공식 자료
- Google Gemini API 모델 및 가격: https://ai.google.dev/gemini-api/docs/pricing
- Google Gemini API 모델 가이드: https://ai.google.dev/gemini-api/docs/models
- IANA time zone database key: Asia/Seoul (Python zoneinfo)


## CI 결과 및 후속 확인
- Run #58 (commit 4a11c5c7f15605d4e9e14e788281b51aefae7571): source SHA 검사 및 compileall 통과, pytest 95 passed / 2 failed / 1 xfailed. 실패는 테스트 두 곳이 이전 primary model ID `gemini-flash-latest`를 기대한 테스트 fixture 문제였다.
- 수정 commit fc77d6da07684936a27a60eb1a4cb920ceb37c14에서 기대값을 `gemini-3.8-flash`로 바꾸고 404 fallback 및 Git push failure 회귀 테스트를 추가.
- Run #59 (43975765823): 성공, 99 passed / 1 xfailed. Source SHA, compileall, 전체 pytest 통과.
- 운영 실행 전이므로 실제 Gemini 모델 접근성, KST 기준 첫 daily reset, Git push failover 동작은 아직 운영 환경에서 검증되지 않았다.
