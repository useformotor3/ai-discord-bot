# 세션 로그

## 2026-11-14 — 최신 상태 확인 및 CRA 조사 품질 감사

### 수행
- `useformotor3/ai-discord-bot` 저장소와 `main` 브랜치 확인
- 최신 GitHub Actions 실행 #1608 확인: 2026-11-14 02:20 UTC, conclusion=success
- workflow job의 단계가 모두 success인 것 확인
- `state.json`의 당일 count=29 확인
- `history.json` 1,592개 항목 확인
- 최근 아카이브 #27, #28, #29 표본 확인
- main.py 및 run.yml 확인
- EUR-Lex Regulation (EU) 2024/2847 원문 검색으로 Article 13(8), Annex I Part I 2(g), Article 14의 역할 대조
- 보고서 #28·#29의 법령 조항 혼동 및 자동화 코드의 실패 성공처리 결함 기록
- 작업 브랜치 `docs/cra-audit-and-project-control-2026-11-14` 생성

### 핵심 판단
- Actions 성공은 코드 실행 성공이며 보고서의 법적 정확성 검증 완료를 뜻하지 않는다.
- #28의 지원기간 근거는 Article 13(8)과 Annex I Part I point 2(g)를 중심으로 다시 써야 한다. Article 14는 제조자 보고 의무다.
- #29의 취약점 보고는 Article 14(1)~(2)에 따라 적극 악용 취약점 보고를 분리해야 한다. 조기 경보는 인지 후 24시간 이내, 취약점 통지는 72시간 이내, 최종 보고는 시정/완화 조치가 가능해진 뒤 14일 이내라는 조건을 정확히 구분한다.
- main.py의 전체 모델 실패 경로가 success=True로 바뀌므로 성공 상태의 신뢰성이 깨진다.
- main.py 및 운영 workflow는 이번 작업에서 수정하지 않았다.

### 다음 단계
1. 보고서 #28·#29 정정본 작성(원본 보존, 정정 근거 링크 포함)
2. 최근 아카이브의 중복 주제와 잘못된 법령 인용을 추가 표본 감사
3. main.py 개선 제안서 작성: 실패 상태, URL/조항 근거 메타데이터, 중복 주제 인덱싱, HTTP 처리, 테스트
4. 사용자 승인 후 별도 작업 브랜치에서 코드 수정 및 mock 테스트
5. 테스트와 CI 결과를 상황판·세션 로그에 반영

### 변경 범위
- 이번 브랜치: 운영 문서와 감사 기록만 추가
- 금지/미수정: `main.py`, `.github/workflows/run.yml`, `state.json`, `history.json`

### 추가 수행 — 보고서 정정본
- #28 지원기간 근거를 Article 13(8), 무상 업데이트를 Annex I Part I 2(g), 업데이트 지속 제공을 Article 13(9)로 정정
- #29 적극 악용 취약점 보고와 심각한 사고 보고를 분리하고 24h/72h/14일 및 1개월 시한을 구분
- 정정본: `reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md`
- 원본 #28·#29는 변경/삭제하지 않음

## 2026-11-14 — main.py 상세 개선 설계
- main.py와 운영 workflow의 main 기준 원문을 다시 확인
- P0~P2 위험 12개를 정리
- 단계별 실행 상태 모델, 모듈 분리, 실패/재시도 정책, 출처 메타데이터, 중복 추적, 상태파일 호환, 테스트 24개, CI 순서 설계
- 상세 설계: `reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md`
- 구현 순서는 Phase A(테스트 기반)부터 시작하도록 제안
- 아직 main.py, workflow, state.json, history.json 변경 없음
- Phase A 구현은 사용자 승인 대기
## 2026-11-14 — Phase A 테스트 기반 구축

### 승인 범위
- 사용자 승인에 따라 작업 브랜치 `docs/cra-audit-and-project-control-2026-11-14`에서 Phase A만 수행
- 운영 `main.py`, `.github/workflows/run.yml`, `state.json`, `history.json`은 수정하지 않음
- 실제 Gemini API, Discord Webhook, Git commit/push 호출 금지

### 변경
- `tests/conftest.py`: Gemini, requests, subprocess, sleep mock fixture
- `tests/test_main_characterization.py`: 정상 생성, 모델 폴백, 전체 모델 실패의 현행 동작 기록
- `tests/test_mock_infrastructure.py`: 외부 경계 mock 차단 검증
- `tests/README.md`: 테스트 실행법과 테스트 해석 기준

### 검증
- Python compileall: 통과
- mock infrastructure test: 2 passed
- 브랜치에서 조회한 `main.py` 원문을 격리 작업공간에 반영해 전체 suite 실행: 5 passed.
- 실제 Gemini/Discord/Git 외부 호출: 없음
- 파일 재조회로 GitHub 저장 내용 확인

### 관찰 및 다음 단계
- 전체 모델 실패 시 오류 경고를 정상 보고서로 저장하는 BUG-01 경로를 characterization test로 고정했다. 이는 정상 요구사항이 아니며 Phase B에서 실패 상태와 아카이브/전송 차단을 기대하도록 테스트를 전환해야 한다.
- 작업 브랜치는 main보다 4 commits 뒤처진 diverged 상태다. 자동 생성된 main 아카이브를 보존하기 위해 merge/rebase하지 않았다.
- 다음은 실제 저장소 checkout이 가능한 환경에서 characterization 전체 테스트 실행 및 결과 보완이다.
- Phase B(P0 코드 수정)는 별도 사용자 승인 전까지 시작하지 않는다.

## 2026-11-14 — Phase B P0 수정

### 승인 범위
- 사용자 승인에 따라 작업 브랜치에서 P0 모델 실패/응답 검증 문제 수정
- 운영 workflow, state.json, history.json은 변경하지 않음
- 실제 Gemini API, Discord Webhook, Git push 호출 금지

### 코드 변경
- `main.py`에 보고서 최소 구조 검증 함수 추가
- 응답 길이 250자 미만, 필수 4개 항목 누락, 대표 오류/쿼터/서비스 장애 문구가 있으면 무효 처리
- 무효 응답은 동일 모델에서 최대 3회 시도 후 다음 모델로 폴백
- 모든 모델이 실패하면 비정상 종료하고 전송·아카이브·상태 변경·Git 동기화 이전에 중단

### 테스트 변경 및 결과
- 기존 P0 결함 재현 테스트를 기대 동작 검증으로 교체
- 정상 보고서, 모델 폴백, 전체 모델 실패, 짧은/형식 불량 응답, 오류 문구가 섞인 응답, 기존 상태파일 보존을 검증
- mock 인프라 경계 테스트 포함
- 격리 Python 실행환경에서 compileall 통과 및 pytest 9 passed
- 실제 외부 API/Discord/Git 호출 없음. GitHub Actions CI/운영 실행은 수행하지 않음.

### 남은 범위
- P1: state.json/history.json 손상 시 fail-closed 처리
- P1: last_health_check datetime parsing 오류 처리
- P1: Discord timeout 및 HTTP status 확인
- P1: Git commit/push 실패를 실행 상태에 반영
- 이 항목들은 이번 승인 범위의 P0 수정에 포함하지 않았으며 다음 단계에서 우선순위를 재검토한다.



## 2026-11-14 — P1-A 상태·이력 데이터 보호

### 승인 범위
- 사용자 승인에 따라 작업 브랜치에서 상태·이력 파일 검증과 날짜 호환성만 수정
- workflow, state.json, history.json, 운영 main 브랜치는 변경하지 않음
- Gemini API, Discord Webhook, Git commit/push 실호출 금지

### 구현
- `main.py`에 `load_state()`, `load_history()`, `parse_health_check()` 추가
- 상태파일 JSON 파싱 실패, 최상위 자료형 오류, date/count 필드 오류, 잘못된 last_health_check는 원본을 보존하고 안전 종료
- 이력파일 JSON 파싱 실패, 배열이 아닌 최상위 구조, 객체가 아닌 이력 항목은 원본을 보존하고 안전 종료
- 기존 이력 항목의 추가 필드는 요구하지 않아 하위 호환성을 유지
- timezone-aware datetime은 로컬 naive datetime으로 정규화한 뒤 기존 비교 로직에 전달
- `tests/test_p1_reliability.py`에 손상 파일, 스키마 오류, datetime 호환성 테스트 추가
- `tests/README.md`를 현재 테스트 범위에 맞게 정리

### 검증 결과 및 한계
- GitHub에 저장한 `main.py`, 신규 테스트, README, 상황판, 세션 로그를 다시 fetch해 저장 확인
- 기존 `state.json`은 객체/date 문자열/count 정수/last_health_check 문자열 구조로 확인
- 기존 `history.json`은 1,592개 항목의 배열이며 비객체 항목 0개임을 JSON 파싱으로 확인
- 신규 helper와 P1 테스트 모듈의 Python 문법 파싱(ast.parse)은 통과
- 이 환경에서 GitHub 저장소 checkout 기반 pytest 실행은 수행하지 못했으므로 pytest 통과로 보고하지 않음
- GitHub Actions CI와 운영 workflow는 실행하지 않음
- 현재 브랜치는 main 대비 41 commits ahead / 6 commits behind이며 자동화가 계속 추가되므로 merge/rebase 보류
- P1-B(Discord timeout/status, Git 동기화 실패 상태화)는 별도 승인 대상


### 추가 코드 수행 검증
- GitHub에서 재조회한 P1-A helper 구현을 분리해 임시 pytest 환경에서 7개 동작 검증을 실행했고 7 passed
- 손상 파일 원본 보존, 잘못된 state/history 구조 거부, datetime 시간대 정규화, 날짜 변경 시 quota count reset을 확인
- 이 검증은 helper 로직의 독립 실행이며 저장소 전체 테스트 suite 또는 main.py end-to-end 실행이 아니다.
- 전체 저장소 pytest, GitHub Actions CI, 운영 workflow는 미실행 상태로 유지한다.
- 코드 리뷰상 Discord 응답 상태/timeout, Git push 실패 상태, state/history 원자적 저장은 아직 미해결이며 P1-B 또는 후속 안정성 작업 대상이다.


## 2026-11-14 — 프로젝트 기록 체계 정합성 점검 및 갱신

### 사용자 요청 및 판단
- 사용자는 행동강령, 진행사항, 상황판, 프로젝트 메인 페이지를 대화창이 아니라 GitHub에 지속적으로 축적할 것을 명시했다.
- 기존 작업 브랜치에 행동강령·상황판·마스터 계획·세션 로그는 있었으나 루트 `README.md`는 해당 브랜치에서 조회되지 않았다.
- 따라서 관리 문서의 책임을 명확히 하고 README 메인 페이지를 추가하는 것이 가장 직접적이고 유지보수 비용이 낮은 조치라고 판단했다.

### 이번 실제 변경 범위
- `AI_RULEBOOK.md`: GitHub 우선 기록, 의미 있는 작업 후 문서 갱신, 저장 후 재조회, 테스트 범위의 정직한 표기, 승인 경계, 객관적 우선순위 규칙 추가
- `PROJECT_STATUS.md`: 최신 브랜치 비교(45 ahead / 7 behind), P0/P1-A 구현 상태, helper 테스트 7 passed의 한계, 전체 pytest 미완료, 다음 재개 지점으로 정리
- `MASTER_PLAN.md`: 관리 문서 역할표, 현재 단계별 완료 상태, 전체 테스트 확보를 P1-B보다 앞선 선행 작업으로 재정렬
- `README.md`: 프로젝트 메인 페이지 신규 생성 및 주요 문서/보고서/테스트 진입 링크 제공
- `SESSION_LOG.md`: 이번 기록 체계 갱신 작업을 추가

### 사실 검증 및 제한
- 작업 브랜치의 기존 관리 문서를 GitHub에서 직접 재조회한 뒤 갱신안을 작성했다.
- `README.md`는 해당 브랜치에서 fetch 결과 404로 확인되어 신규 파일로 생성한다.
- `main`과 작업 브랜치 비교를 다시 수행: diverged, 45 commits ahead / 7 commits behind.
- 이번 작업은 관리 문서 갱신이며 코드 테스트를 실행한 작업이 아니다.
- 전체 저장소 pytest, GitHub Actions CI, 운영 workflow는 실행하지 않았다.
- 운영 `main`, `main.py`, `.github/workflows/run.yml`, `state.json`, `history.json`은 이번 변경 대상이 아니다.
- 문서 파일 각각의 GitHub 반영 후 동일 브랜치에서 재조회해 저장 내용과 SHA를 확인한다.

### 다음 재개 지점
1. 작업 브랜치의 실제 소스를 안전한 격리 환경에 확보해 전체 pytest 및 compileall 실행
2. P1-A 통합 회귀 검증 결과를 상황판/세션 로그에 기록
3. P1-B 최소 변경안 제시 및 사용자 승인 요청
4. 승인된 변경만 구현하고 mock 테스트 후 저장소 전체 회귀 검증


## 2026-11-14 — 격리 테스트 환경 확보 및 예비 실행

### 수행
- GitHub 저장소 메타데이터에서 저장소 공개 상태(public)와 작업 브랜치 접근 권한 확인
- 작업 브랜치의 main.py 및 테스트 4개 파일을 GitHub에서 조회
- 컨테이너에서 branch clone 시도: DNS 해석 실패(`Could not resolve host: github.com`)
- 별도 임시 디렉터리에 조회한 내용을 바탕으로 테스트 사본을 구성하고 compileall 및 pytest 실행

### 예비 실행 결과
- compileall 종료 코드 0
- pytest 21 passed (0.14s)
- Gemini/Discord/Git/sleep 경계는 mock 처리
- 실제 외부 API, Discord webhook, Git commit/push, GitHub Actions workflow 실행 없음

### 중요 제한 및 교차검증
- 임시 사본 5개 파일의 Git blob SHA-1을 GitHub 조회 당시 SHA와 비교한 결과 5개 모두 불일치
- 따라서 실행한 사본이 GitHub 원본과 byte-for-byte 동일하지 않음
- 21 passed는 임시 재구성 사본의 예비 검증일 뿐, 작업 브랜치 전체 저장소 pytest 통과로 보고하지 않음
- 전체 저장소 pytest와 GitHub Actions CI는 미실행 상태 유지
- 상세 기록: `reports/TEST_EXECUTION_ENVIRONMENT_AUDIT_2026-11-14.md`

### 변경/운영 영향
- 이번 작업에서 저장소 코드나 workflow를 변경하지 않음
- 운영 main, state.json, history.json, main.py, run.yml 미변경
- 다음 단계는 원본 파일의 blob SHA를 일치시킬 수 있는 실행 경로 확보


## 2026-11-14 — P1-A 코드 정적 재검토 및 잔여 위험 우선순위화

### 검토
- GitHub 작업 브랜치의 `main.py` 원문을 직접 조회해 P1-A 구현과 후속 부작용 경로를 재검토
- state/history fail-closed, count 검증, datetime 정규화, 전체 모델 실패 시 외부 부작용 차단 경로를 확인
- Discord timeout/status 미검증, Discord 전송과 파일 저장 순서, state/history 비원자적 write, Git push 실패 삼킴, webhook 미설정의 무표시, 출처 내용 미검증, import 시점 파이프라인 실행 구조를 잔여 위험으로 분류

### 판단
- 가장 먼저 해결할 것은 원본 소스 동일성이 보장된 전체 테스트 환경 확보
- 이후 전송/저장/동기화의 부분 성공과 데이터 손상 위험을 우선 개선
- P1-B 코드 변경 및 workflow 변경은 별도 승인 전 수행하지 않음

### 검증 한계 및 운영 영향
- 이번 단계는 GitHub에서 읽은 코드에 대한 정적 검토이며 새 코드 테스트를 실행한 것이 아님
- 임시 재구성 사본 pytest 21 passed는 blob SHA 불일치로 예비 결과에 한정
- 저장소 전체 pytest와 GitHub Actions CI 미실행
- `main.py`, workflow, `state.json`, `history.json`, 운영 `main` 미변경
- 실제 Gemini API, Discord webhook, Git commit/push, 운영 workflow 호출 없음
- 상세 설계 기록: `reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md` §14


## 2026-11-14 — 원본 테스트 fixture 및 main.py 부작용 경로 재검토

### 검토 대상
- 작업 브랜치의 `main.py`, `tests/conftest.py`, `tests/test_main_characterization.py`, `tests/test_p1_reliability.py`를 GitHub connector로 다시 조회
- 각 파일의 blob SHA를 기록하고 코드 내용을 직접 검토
- `.github/workflows/run.yml`의 트리거와 실행 단계를 재확인

### 실제 확인된 사항
- Git subprocess mock은 모든 명령에 대해 항상 returncode=0을 반환한다. 따라서 `check=True`에서 발생하는 Git 실패 예외를 재현하지 못한다.
- Discord mock은 항상 HTTP 204를 반환하며 timeout/429/4xx/5xx/네트워크 오류를 검증하지 않는다.
- 정상 테스트는 Git 명령 호출 횟수만 검사하며 명령별 실패 결과를 확인하지 않는다.
- main.py는 Discord timeout/status를 확인하지 않고, Discord 전송이 아카이브/상태 저장보다 먼저 실행된다.
- state/history는 목적 파일에 직접 write한다.
- Git push 예외는 출력만 하고 삼켜 프로세스 성공 종료 가능성이 남는다.
- history snippet 자료형과 초 단위 아카이브 파일명 충돌은 잠재 위험으로 분류했다. 실제 데이터 분포/충돌 여부는 미확인이다.

### 판단
- 기존 테스트는 정상 및 일부 모델 실패 경로에는 유용하지만 Git/Discord 실패 경로를 충분히 검증하지 못한다.
- 원본 소스 동일성이 보장된 전체 테스트 환경 확보를 계속 최우선으로 둔다.
- 이후 fixture 실패 경로 보강과 P1-B 구현은 범위·테스트·롤백을 제시하고 별도 승인을 받는다.

### 변경/운영 영향
- 이번 단계에서 GitHub 원본 코드와 테스트를 정적 검토했으며 코드/테스트/workflow/state/history는 변경하지 않았다.
- 실제 pytest 및 CI는 실행하지 않았다.
- 운영 Gemini/Discord/Git push 및 운영 workflow를 실행하지 않았다.
- 상세 기록: `reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md` §15 및 `PROJECT_STATUS.md`

### GitHub 관리 문서 갱신
- README, AI_RULEBOOK, PROJECT_STATUS, MASTER_PLAN, SESSION_LOG 및 개선 설계 보고서를 작업 브랜치에 갱신했다.
- 여섯 파일을 동일 브랜치에서 다시 fetch해 저장된 내용과 새 blob SHA를 확인했다.
- 갱신 후 main 대비 67 ahead / 49 behind를 재조회했다.


## 2026-11-14 15:31 KST — 원격 브랜치 및 CI 기록 재조회

### 조회 결과
- 작업 브랜치 HEAD: `8813eb53b186b25e72ac157d664d636be6d68fd8`
- main HEAD: `c9b5bff8ee851b6baa86bbe4073353c9303bb432`
- compare: diverged, 72 ahead / 50 behind
- 작업 브랜치 GitHub Actions runs: 0건

### 판단 및 제한
- 기존 문서의 61/49는 과거 스냅샷이므로 현재 상황판에는 최신 조회값을 별도 기록했다.
- Actions 실행기록 0건은 CI 성공이 아니다. 원본 전체 pytest와 CI는 여전히 미완료다.
- GitHub GET 조회만 수행했으며 workflow dispatch, 운영 자동화, 코드 변경은 하지 않았다.
- merge/rebase 및 P1-B 구현은 수행하지 않았다.

## 2026-11-14 — 테스트 전용 GitHub Actions 구현 및 원본 전체 테스트 실행

### 승인 범위
- 사용자가 테스트 전용 GitHub Actions workflow 신규 생성을 명시적으로 승인했다.
- 승인 범위: 작업 브랜치에 테스트 workflow 추가, 원본 SHA 검증, compileall, pytest 실행.
- 운영 workflow, 운영 main 브랜치, 운영 상태/이력 데이터는 변경 금지.

### 실제 변경
- 신규 `.github/workflows/tests.yml` 생성
  - 작업 브랜치에만 push 트리거 제한
  - workflow_dispatch 지원
  - contents: read만 허용
  - checkout persist-credentials=false
  - Gemini/Discord 비밀키 및 운영 Git push 사용 없음
  - 5개 파일 Git blob SHA 선검증
  - Python 3.11 compileall 및 pytest 실행
- `tests/README.md`에 실행 방법, 보안 경계, SHA 갱신 규칙 추가

### 실행 및 교차검증
- GitHub Actions Run #1: [https://github.com/useformotor3/ai-discord-bot/actions/runs/43567990149]
- run ID: `43567990149`
- 실행 commit: `d31c604c6067685e33f6888cbc488c0e45d80be7`
- 5개 핵심 파일의 Git blob SHA: 모두 일치
- compileall: 통과
- pytest: **21 passed in 0.16s**
- job 및 workflow conclusion: success
- GitHub Actions 로그에서 SHA별 실제 계산값, compileall 단계, pytest 출력과 21 passed 결과를 확인

### 운영 영향
- `main`, `main.py`, `.github/workflows/run.yml`, `state.json`, `history.json`은 변경하지 않음
- 운영 workflow dispatch, Gemini API, Discord webhook, 실제 Git push 없음
- 테스트는 mock 환경이며 Discord/Git 실패 경로를 충분히 검증하지 않음

### 다음 재개 지점
1. 상황판과 README에 Run #1 및 21 passed를 반영하고 저장 후 재조회
2. fixture 실패 경로 보강 설계 및 P1-B 별도 승인 절차 진행


## 2026-11-14 — 최신 브랜치 HEAD에서 CI 재검증

- 앞선 Run #1 성공 결과를 README/상황판/계획/감사 기록에 반영한 후 최신 HEAD `dddba44a41851e9d0319ce9a91535a9d26145d92`에서 workflow 재실행을 확인했다.
- [Run #3](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938): success
- 원본 SHA 5개 일치, compileall 통과, pytest **21 passed in 0.19s**
- 테스트 전용 workflow가 코드 기준 SHA를 검사하고 있음을 반복 확인했다.
- 이 실행은 문서 변경을 포함한 최신 HEAD의 회귀 검증이다. P1-B의 실패 경로 테스트를 새로 추가한 것은 아니다.


## 2026-11-14 — 사람·AI 공용 이중 형식 프로젝트 로그 구축

### 사용자 확인 사항
- 사용자는 로그가 AI가 파악할 수 있는 형식과 사람이 읽을 수 있는 형식으로 함께 누적되는지 확인을 요청했다.
- 점검 결과 `SESSION_LOG.md` 등 한국어 관리 문서는 존재했으나, 프로젝트 변경 사건을 일정한 스키마로 파싱할 전용 JSONL 로그는 없었다.
- 기존 `state.json`·`history.json`은 자동화 런타임 데이터이므로 프로젝트 개발 로그로 간주하지 않기로 했다.

### 실제 변경
- `PROJECT_LOG.jsonl` 신규 생성: 프로젝트 관리, P1-A, 테스트 workflow 승인/구축, CI Run #1 및 Run #3의 검증 사실을 구조화 이벤트로 기록했다.
- `README.md`: 두 로그의 역할과 진입 링크 추가.
- `AI_RULEBOOK.md`: JSONL 필수 필드, 증거/한계/승인 기록 규칙 추가.
- `PROJECT_STATUS.md`: 이중 기록 체계와 브랜치 diverged 상태 기록.
- `MASTER_PLAN.md`: 새 대화 재개 시 JSONL과 한국어 세션 로그를 함께 확인하도록 추가.

### 검증 및 제한
- 기록된 CI 증거: Run #1 및 Run #3 링크, 원본 blob SHA 확인, compileall 및 pytest 21 passed.
- GitHub compare 재조회 당시 `main` 대비 diverged, 96 ahead / 54 behind. 이후 문서 커밋이 추가되므로 수치는 변동 가능하며 통합 직전 다시 조회해야 한다.
- 운영 `main`, `main.py`, 운영 workflow, `state.json`, `history.json`은 이번 작업에서 변경하지 않았다.
- P1-B 구현이나 실패 경로 테스트 추가는 수행하지 않았다. 별도 승인 경계를 유지한다.

### 추가 정합성 확인
- README의 Run #3 실행 commit 표기가 Run #1 commit으로 잘못 남아 있어 `dddba44a41851e9d0319ce9a91535a9d26145d92`로 정정했다.
- `PROJECT_LOG.jsonl`에 이중 형식 로그 구축 사건 자체를 추가했다.
- 전체 JSONL과 관리 문서 재조회 후 GitHub compare를 다시 확인: `main` 대비 diverged, 102 ahead / 54 behind. merge/rebase는 수행하지 않았다.


## 2026-11-14 — Git/Discord 실패 경로 fixture 설계

### 원본 검토
- tests/conftest.py의 Discord mock은 항상 204를 반환하며 timeout/status/header/예외를 지원하지 않는다.
- Git subprocess mock은 모든 명령에 returncode=0을 반환하고 check=True 실패를 재현하지 않는다.
- main.py는 Discord timeout/status 검사와 Git 실패 상태화를 수행하지 않는다.

### 설계 산출물
- reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md §16에 fixture 확장안과 D01~D06, G01~G04, S01~S03, L01 실패 시나리오를 기록했다.
- P1-B 최소 제안은 Discord timeout/status/retry, Git 단계별 실패 상태, state/history 원자적 저장, 부분 성공 분리, 비밀정보 비노출이다.

### 변경 및 검증 경계
- 이번 단계는 원본 파일 정적 검토 및 설계 문서 갱신이다. main.py, tests, workflow, 운영 데이터는 변경하지 않았고 테스트 실행도 하지 않았다.
- fixture/test 변경과 P1-B 운영 코드 변경은 승인 전 구현하지 않는다.


## 2026-11-14 — 전용 실패 경로 테스트 브랜치 구현 및 검증

### 사용자 승인
- 사용자가 테스트 전용 fixture 및 실패 경로 테스트 추가를 승인했다.
- 승인 경계: `main.py`, 운영 workflow, `state.json`, `history.json` 미변경. 실제 Gemini/Discord/Git push 및 운영 workflow 실행 금지.

### 브랜치 전략 및 기준점
- 기존 문서/설계 브랜치 `docs/cra-audit-and-project-control-2026-11-14`의 commit `c6dfc5cee2485922b2313030dd9a5843e347afe7`에서 새 작업 브랜치 `test/failure-path-fixtures-2026-11-14`를 생성했다.
- 이 방식으로 기존 문서 작업과 실패 경로 테스트 작업을 분리하고, 변경을 기준 commit 대비 비교할 수 있게 했다.
- 기준점 대비 변경 파일은 `.github/workflows/tests.yml`, `tests/README.md`, `tests/conftest.py`, `tests/test_mock_infrastructure.py`, `tests/test_external_failure_paths.py` 5개 경로다.
- `main.py` blob SHA는 기준과 동일하게 `470ac101d5cc4fdb2c5077d5468ef00327af3d43`이며 수정하지 않았다.

### 구현
- Discord mock은 response queue, HTTP status, headers/Retry-After, 예외, timeout 인자, payload 길이를 관찰할 수 있게 했다. webhook URL과 payload 본문은 캡처하지 않는다.
- Git mock은 명령별 return code/예외를 주입하고 `check=True`에서 `subprocess.CalledProcessError`를 발생시킨다.
- sleep mock은 실제 대기 없이 호출 시간을 기록한다.
- 경계 mock 자체의 동작을 검증하는 테스트 2건을 추가/보강했다.
- 현재 운영 코드가 아직 만족하지 못하는 P1-B 기대 동작 5건은 `xfail(strict=True)`로 표시했다. 이는 결함을 성공 처리하지 않으며 향후 구현 시 XPASS(strict)가 되면 테스트를 정상 통과로 전환하도록 하는 게이트다.
- 테스트 전용 workflow에 feature branch push 트리거를 추가하고 6개 파일 blob SHA를 검증하도록 했다.

### CI 시행착오 및 원인 교정
- Run #5 실패: probe 테스트가 실제 main.py로 실행되어 유효 보고서가 아닌 mock 응답을 사용했고, HTTP status capture도 미완성이었다.
- Run #6 취소: workflow의 기대 blob SHA와 새 fixture blob이 일시적으로 어긋났다.
- Run #7 실패: probe 스크립트 경로를 지정하지 않아 main.py가 실행됐다.
- Run #8 실패: test_mock_infrastructure.py 변경 후 workflow SHA 기준 갱신 전 실행됐다.
- Run #9 실패: 동일 probe script_path 연결 오류가 남아 있어 재수정했다.
- Run #10 취소: 같은 브랜치 후속 push로 concurrency 정책이 이전 실행을 취소했다.
- 위 오류는 모두 workflow/job 로그에서 확인하고 수정했다. 실패 실행을 성공으로 보고하지 않는다.

### 최종 CI 검증
- Run #11: https://github.com/useformotor3/ai-discord-bot/actions/runs/43569359083
- 검증 commit: `821d64bea0bc96710f083a773eabede80ba4a45c`
- 6개 파일 blob SHA 전부 일치, Python compileall 통과, pytest `23 passed, 5 xfailed in 0.20s`.
- 5 xfailed: Discord timeout 전달, 429 재시도, 503 재시도, 400 후속 저장 차단, Git push 실패 상태화.
- 실제 Gemini/Discord/Git push, 운영 workflow 실행 없음.

### Git 변경 추적 및 개선점
- 전용 브랜치에서만 변경했으며 기준 commit 대비 파일 목록을 compare로 확인했다. merge/rebase/PR merge는 하지 않았다.
- GitHub Contents API로 파일을 순차 갱신해 수정 파일마다 별도 commit이 생겼다. 이력은 추적 가능하지만 commit granularity가 세분화된 점은 개선 대상이다. 이후 여러 파일을 한 논리 작업으로 묶을 수 있는 Git tree/commit 경로를 사용하거나 변경 파일 묶음을 먼저 확정한 뒤 단일 logical commit으로 기록하는 방식을 우선한다.
- `AI_RULEBOOK.md`에 브랜치 기준점, 변경 전/후 SHA, CI commit SHA, rollback 및 commit grouping 규칙을 추가했다.

### 다음 단계
- P1-B의 retry, 4xx/5xx, 부분 chunk 전송, Git sync 상태 및 atomic state/history write 정책을 명세한다.
- 기존 동작/변경 동작, 영향 파일, 테스트, 롤백 계획을 포함한 구현안을 별도 제시하고 사용자 승인을 받는다.


## 2026-11-14 — 원격 상태 재조회 및 실패 주입 fixture 2차 확장

### 재개 전 확인
- 저장소 관리 문서, 테스트 fixture, 실패 경로 테스트, 테스트 workflow를 현재 작업 브랜치에서 다시 조회했다.
- 작업 시작 HEAD: `4f599f14e92dcbe5ead14d4886feda34cfd874da`.
- 기준 docs 브랜치 commit `c6dfc5cee2485922b2313030dd9a5843e347afe7` 대비 21 ahead / 0 behind.
- `main` HEAD `3b2dafd098b51eb60998ce3be032efc4a42760fb`; compare diverged 132 ahead / 58 behind.
- README 및 상황판 상단의 현재 브랜치 표기가 이전 docs 브랜치로 남아 있는 것을 확인했다. 이번 묶음에서 정정한다.

### 변경
- `tests/test_mock_infrastructure.py`: Discord transport exception 2 case, HTTP 401/403 2 case, Git add/commit/push 단계별 실패 3 case 추가.
- `.github/workflows/tests.yml`: 변경된 테스트 파일의 정확한 Git blob SHA로 source pin 갱신.
- README, 상황판, 마스터 계획, 테스트 가이드에 현재 브랜치/스냅샷/검증 범위를 갱신한다.
- 이번 변경은 테스트 경계의 오류 주입 capability 검증이다. main.py와 운영 workflow/data는 변경하지 않는다.

### 검증 계획 및 제한
- 이번 commit을 push한 후 전용 Actions에서 exact blob SHA → compileall → 전체 pytest 순으로 검증한다.
- 새 CI 결과 전에는 테스트 통과를 주장하지 않는다. 기존 Run #11은 변경 전 코드만 검증한다.
- merge/rebase/PR merge, 운영 workflow 실행, Gemini/Discord 실호출, 실제 Git push는 수행하지 않는다.


## 2026-11-14 — 실패 주입 fixture 2차 확장 CI 검증 및 정정

### CI 결과
- 첫 실행 Run #12: [failure](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570141381), commit `717175eed7bd29c0d8d9e86616b66fe5ebfc24da`.
- 로그를 확인한 결과 `tests/test_mock_infrastructure.py` 실제 SHA `0750cc274fe2490c30e1d508c721c86ed3d9ee1b`와 workflow 기대 SHA `706d0c1d7cfcd595129e6cd4c42947ab4bf00bb8`가 불일치했다. 이 단계에서 중단되어 compileall/pytest는 실행되지 않았다.
- 테스트 소스의 생성 문자열 개행 이스케이프도 함께 점검·수정했고, workflow SHA를 새 blob `05a92ff7ff3a6e4a0374d270770ecc6cf38e0a7f`로 갱신했다.
- 수정 commit: `27d2c69287631b041672b9989fdeeb3066f5ebb9`.
- Run #13: [success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208). 6개 blob SHA 모두 일치, compileall 통과, pytest **30 passed, 5 xfailed in 0.26s**.
- 이 결과는 현재 테스트 소스와 fixture를 대상으로 한 mock CI다. 실제 Gemini/Discord/Git push나 운영 workflow는 실행하지 않았다.

### 원격 추적
- Run #13 시점 기준 docs commit 대비 23 ahead / 0 behind.
- main 대비 diverged 134 ahead / 58 behind; main HEAD `3b2dafd098b51eb60998ce3be032efc4a42760fb`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 문서 갱신 commit 이후 수치는 다시 조회한다. merge/rebase/PR merge는 하지 않는다.

## 2026-11-14 — 관리 문서 재조회 후 최신 브랜치 수치 확정
- README, PROJECT_STATUS, MASTER_PLAN, SESSION_LOG, PROJECT_LOG, tests/README 및 workflow를 동일 브랜치에서 다시 fetch했다. JSONL 10행 모두 JSON 파싱 성공.
- 문서 갱신 직전 HEAD `11c89c2bf513c0562aa0451caf38effae2041e26`; 기준 docs commit 대비 24 ahead / 0 behind.
- main 대비 diverged 135 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- main.py blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 보존 확인. 기준 commit 대비 diff에도 main.py는 포함되지 않는다.
- Run #13 검증 commit `27d2c69287631b041672b9989fdeeb3066f5ebb9` 이후는 문서만 갱신했으므로 30 passed / 5 xfailed의 코드 검증 근거는 유효하다.


## 2026-11-14 — P1-B 전송·저장·동기화 정책 정밀 설계

### 공식 기술 문서 확인
- Discord 공식 Rate Limits 문서에서 429의 Retry-After 또는 JSON retry_after 준수, invalid request(401/403/429) 반복 위험, webhook 404 재요청 금지 안내를 확인했다.
- Discord Execute Webhook 문서에서 wait=true일 때 서버가 메시지 저장을 확인하고 message 객체를 반환하며, wait=false 기본 동작은 저장되지 않은 메시지에 오류를 돌려주지 않을 수 있음을 확인했다.
- Python Requests 문서에서 timeout 미지정 시 무기한 대기 가능, connect/read timeout 구분, ConnectTimeout은 재시도 안전하다고 명시된 점을 확인했다.

### 설계 판단
- Discord POST의 ReadTimeout/일반 ConnectionError/5xx는 서버 측 반영 여부가 불명확하므로, idempotency 수단 없이 무조건 재시도하면 중복 메시지를 만들 수 있다. 기본 상태를 delivery_unknown으로 두고 재시도는 보류한다.
- 429는 Retry-After/retry_after를 준수하며 실행 대기 예산을 초과하면 임의로 대기시간을 줄이지 않고 deferred로 처리한다.
- wait=true와 chunk별 message ID/상태를 사용해 확인 성공 파트를 추적한다. 부분 성공과 unknown 파트를 분리한다.
- archive를 먼저 원자적으로 저장하되 state/history 각각의 atomic replace만으로 두 파일 간 transaction이 보장되지 않으므로 journal/recovery 설계를 추가한다.
- Git push 실패 시 로컬 commit을 보존하고 다음 실행에서 원격 ref를 조회해 같은 commit의 반영 여부를 먼저 확인한다.
- 기존 503 retry strict xfail는 새 정책과 충돌할 수 있으므로 P1-B 구현 전 테스트 계약을 수정하거나 중복 방지 수단을 먼저 결정한다.

### 승인/운영 경계
- 상세 설계는 `reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md` §17에 기록했다.
- 공식 출처는 Discord Rate Limits, Discord Webhook Resource, Python Requests Quickstart/Advanced 문서다.
- 이번 변경은 문서만이며 main.py, 운영 workflow, state/history를 수정하지 않았다. 운영 Gemini/Discord/Git push도 실행하지 않았다.
- P1-B 코드는 별도 승인 전까지 구현하지 않는다.


## 2026-11-14 — Discord 실패 테스트 계약 수정 및 CI 검증

### 정책 정합성 수정
- 공식 Discord 문서와 Requests 문서에 근거해 503/ReadTimeout 등의 POST 결과는 서버 반영 여부가 불명확할 수 있으므로, idempotency/outbox 없이 자동 재전송하지 않는 정책을 채택했다.
- 기존 `test_discord_503_is_retried_then_succeeds` 기대를 `delivery_unknown` + no automatic retry로 변경했다.
- HTTP 401/403/404에 대해 `permanent_failure` + no retry 기대 테스트 3 case를 추가했다.
- 이 기대 동작은 현행 main.py에 구현되지 않아 strict xfail로 남긴다.

### CI
- [Run #15 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842)
- tested commit: `b2e108768be08f06e85af154835424682337ebf5`
- 6개 source blob SHA 일치, compileall 통과, pytest **30 passed, 8 xfailed in 0.23s**.
- 운영 main.py/운영 workflow/state/history 변경 없음.
- 이번 조치는 테스트 계약과 설계 문서 정합화이며 P1-B 운영 구현 승인이 아니다.

## 2026-11-14 — P1-B 정책 문서 저장 후 재조회
- README, 상황판, 세션 로그, JSONL을 재조회할 수 있도록 최신 원격 상태를 추가 기록한다.
- 직전 HEAD `5b3cd6ca70dcff7a50f4ad4c20f834592c9e8ca9`; 기준 docs commit 대비 28 ahead / 0 behind.
- main 대비 diverged 139 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- Run #15의 검증 대상은 `b2e108768be08f06e85af154835424682337ebf5`; 그 이후는 문서/로그 변경만이다.


## 2026-11-14 — P1-B 단계별 구현 제안서 작성

- P1-B 전체를 한 번에 구현하면 외부 부작용과 데이터 일관성 위험이 동시에 바뀌므로 B1 Discord 전송, B2 atomic persistence, B3 Git sync, B4 구조 개선으로 분리했다.
- 우선순위는 현재 가장 큰 즉시 위험인 Discord 무한 대기/HTTP 실패의 성공 오인/중복 전송 불명확 상태를 다루는 B1로 설정했다.
- B1의 변경 예정 파일, 함수 수준 동작, 테스트, CI SHA pin, rollback, 제외 범위를 개선 설계 보고서 §18에 기록했다.
- 이 제안은 main.py 변경 승인이 아니다. B1 별도 승인 전에는 구현하지 않는다. B2~B4, 운영 main/workflow/data는 이번 제안 범위 밖이다.

## 2026-11-14 — P1-B1 제안서 반영 후 원격 상태 확인
- 직전 HEAD `f5a83e3c8e04a43b6e38a593c7b01bd360583b3f`.
- 기준 docs commit 대비 30 ahead / 0 behind.
- main 대비 diverged 141 ahead / 60 behind; main HEAD `1dff09ffa9722119f6fb0847a51b6c87c322d114`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 마지막 테스트 CI Run #15 검증 commit은 `b2e108768be08f06e85af154835424682337ebf5`; 그 이후 테스트 소스는 미변경이다.
