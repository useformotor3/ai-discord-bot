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


## 2026-11-16 — P1-B1 Discord 전송 신뢰성 구현 및 CI

### 승인 및 변경
- 사용자가 P1-B1만 구현하도록 승인했다. P1-B2~B4, 운영 workflow/data, 실제 Discord/Gemini 호출은 범위 밖이다.
- main.py에 connect/read timeout (3.05, 10), wait=true, HTTP status/message ID 확인, 429 Retry-After 제한 재시도, ConnectTimeout 제한 재시도, 영구 오류 및 delivery_unknown 분류, chunk별 ID와 partial 상태를 구현했다.
- Discord 실패가 archive/state/history 저장 흐름을 중단시키지 않도록 했다. 저장 원자성·transaction은 구현하지 않았다.
- mock fixture와 P1-B1 테스트를 확장했다. P1-B3 Git sync 상태화 xfail 1건은 남겼다.

### CI 및 정정
- Run #17: [failure](https://github.com/useformotor3/ai-discord-bot/actions/runs/43808247888), commit 715af78b42eacaeb3ca30c03c838132c2a51e707. main.py SHA pin 기대값 900391...와 실제 4b631c04e34b2b3bbade0aa9301e7d48578a1e03가 달라 source integrity에서 중단했다. compileall/pytest는 실행되지 않았다.
- workflow pin을 실제 main.py blob SHA로 수정했다.
- Run #18: [success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43808285335), commit dc341d9e89a837df878257fd3740633f8688507f.
- 6개 핵심 SHA 일치, compileall 통과, pytest 43 passed / 1 xfailed in 0.34s.
- xfail 1건은 P1-B3 Git push 실패 상태화이며 승인 범위 밖이다.
- 실제 Discord/Gemini, 운영 workflow, 운영 Git push 미실행.


## 2026-11-16 — 작업 브랜치와 main divergence 재확인
- 작업 브랜치 HEAD 비교 기준: 37148b596760a03c40164ed6b5a3316310697ba0.
- 기준 docs commit 대비 36 ahead / 0 behind.
- main 대비 diverged 147 ahead / 610 behind. main HEAD 8357da3abe3b87ca0e7a2fa50f862b693c0a226c, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- main.py blob SHA: 작업 브랜치 4b631c04e34b2b3bbade0aa9301e7d48578a1e03, main 86a7731aad5de8d75581fc953bcea2c44adf2f2b. 작업 브랜치에는 P0/P1-A 및 승인된 P1-B1 변경이 있고 main은 다른 시점의 코드다.
- 610 commits behind 상태이므로 PR/merge 전에 자동 생성 보고서, 코드, 데이터와 충돌을 별도 통합 감사해야 한다. 이번에는 merge/rebase/PR merge/운영 배포를 하지 않았다.


## 2026-11-16 — 최종 원격 스냅샷 갱신
- 비교 대상 작업 브랜치 HEAD: d99d897aaea5261e43e30eb0c8240b7fb8ee73c8.
- 기준 docs commit 대비 39 ahead / 0 behind (이 로그 갱신 전).
- main 대비 diverged 150 ahead / 610 behind; main HEAD 8357da3abe3b87ca0e7a2fa50f862b693c0a226c, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- main.py 작업 브랜치 SHA 4b631c04e34b2b3bbade0aa9301e7d48578a1e03, main SHA 86a7731aad5de8d75581fc953bcea2c44adf2f2b.
- 운영 main으로 직접 PR/merge하지 않는다. 610 behind를 포함한 차이를 별도 통합 감사해야 한다.


## 2026-11-16 — 읽기 전용 branch/main 통합 감사
- 작업 브랜치 HEAD a7f2cd285ad89df2d0c67f14acb036e8e42a73d9; main HEAD a7f2cd285ad89df2d0c67f14acb036e8e42a73d9; merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- 작업 브랜치 base 대비 41 ahead / 0 behind, main 대비 152 ahead / 657 behind.
- recursive Git tree 비교: merge-base 1,600 entries, main 2,257 entries, 양쪽 truncated=false. main에 research_archive 신규 657개, 삭제 0개, 변경 경로 history.json/state.json/research_archive 디렉터리.
- history.json 1,592 → 2,249개 객체. state.json count 29 → 110, 날짜 2026-11-14 → 2026-11-16.
- main.py는 merge-base와 동일 SHA 86a7731aad5de8d75581fc953bcea2c44adf2f2b이며 작업 브랜치 SHA 4b631c04e34b2b3bbade0aa9301e7d48578a1e03. 운영 run.yml은 merge-base와 동일 SHA 65a8cadc8eac593f551e390698e367b1d161ecf1.
- 운영 데이터/코드/workflow 변경, 운영 실행, merge/rebase/PR merge 없음. compare API 300개 경로 제한을 recursive tree 비교로 우회 확인.
- 보고서: reports/BRANCH_INTEGRATION_AUDIT_2026-11-16.md. 결론: 통합 보류, 데이터 보존형 별도 change-control 필요.


## 2026-11-16 — main 자동 아카이브로 통합 감사 스냅샷 갱신
- main이 Auto-archive #111로 c6262ddb96d608216e16b0860d2d02b6aedde940에서 31e0f8137630630ee30ea55add039b571f2c6801로 전진한 것을 확인했다.
- 최신 작업 브랜치 HEAD c43abc3315d8d7c8a3d5f4fc209465428a7e8aff; 42 ahead / 0 behind base, main 대비 153 ahead / 658 behind.
- recursive tree 재검증: main 2,258 entries, base 1,600; archive 658개 추가, 삭제 0, history/state 2개 파일 변경. main history 2,250개, state count 111.
- 기존 이벤트의 main_head 필드 오기를 최초 조회 시점의 main SHA로 정정하고 최신 스냅샷 이벤트를 추가한다.
- 운영 파일 변경 및 merge/rebase/PR merge 없음.


## 2026-11-16 — 통합 감사 보고서 메타데이터 정정
- 감사 보고서의 main HEAD를 실제 main ref `31e0f8137630630ee30ea55add039b571f2c6801`로 정정했다.
- 최신 main tree 기준 archive 추가 수 658개, history 항목 수 2,250개로 정합화했다.
- 보고서의 153 ahead / 658 behind는 감사 당시 작업 브랜치 HEAD c43abc3... 기준 스냅샷이며, 후속 문서 커밋은 작업 브랜치 ahead만 증가시킨다.


## 2026-11-16 — P1-B2 원자적 저장 설계 및 통합 감사 갱신
- 작업 브랜치 HEAD 227e3298066af4bda83fb0713fc1d57c749ee8c6, main HEAD 036334dd2665752c2e6ddb024001771cff4064c5, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- 최신 비교 155 ahead / 660 behind. recursive tree 2,260 vs 1,600; archive 660개 추가, history/state 변경, 삭제 0. main history 2,252개, state count 113.
- main의 자동 아카이브가 계속 실행되는 흔적을 확인했으나 신뢰성 개선 코드는 작업 브랜치에만 존재하며 운영 반영되지 않았다.
- P1-B2 durable journal + staged roll-forward + old/new SHA 검증 + idempotent recovery 설계서를 작성했다.
- P1-B2 구현은 미승인. main.py, tests, workflow, 운영 state/history/archive 변경 없음.
- 상세: reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md 및 reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md.


## 2026-11-16 운영 모니터링 설정
- ChatGPT 예약 작업 `매일 Git 브랜치 통합 상태 점검` 생성 완료. ID `6afacb7561d8819182728a42ffd4e867`, 매일 09:00 Asia/Seoul, 첫 실행 2026-11-17 09:00.
- refs/ahead-behind/recursive tree/state-history-archive 변경을 재조회한다. 안전할 때만 작업 브랜치의 상황판·로그 문서를 갱신한다.
- 운영 main/data/workflow 수정, merge/rebase/PR merge, 실제 Gemini/Discord 호출은 금지한다.
- 이 예약 작업은 ChatGPT의 모니터링이며 GitHub Actions 운영 workflow와 별개다.


## 2026-11-16 — 재개 시점 원격 상태 재확인
- 작업 브랜치 HEAD `7383385e7dd8b7abcdba5c72e70ce5cf78dfb2a7`, main HEAD `c2936e9484a44d76dc60ff811e4b904c89cf742f`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare 결과 157 ahead / 671 behind, diverged. main은 Auto-archive #124.
- main state count=124, history top-level object=2,263. main.py/workflow SHA 및 작업 브랜치 main.py SHA를 재확인했다.
- recursive tree 전체 비교는 수행하지 못했으므로 archive delta를 미확정으로 남긴다.
- 운영 파일·workflow·데이터, merge/rebase/PR merge, 운영 실행, Gemini/Discord 호출은 하지 않았다.
- P1-B2 구현은 별도 승인 대기. P1-B3/B4 보류.


## 2026-11-16 — P1-B2 원자적 로컬 저장 구현 및 검증

### 승인 및 기준
- 사용자 명시 승인에 따라 P1-B2 구현을 진행했다.
- 구현 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16`.
- 브랜치 생성 기준: `7ae3b251861b9a3de9981bd7202e346d05ca9430`.
- 기존 작업 브랜치와 운영 main은 분기되어 있으므로 기존 브랜치에 직접 구현하거나 운영 main에 반영하지 않았다.

### 변경 파일
- `persistence.py`: durable journal, staged/backup payload, SHA 검사, POSIX advisory lock, idempotent roll-forward recovery.
- `main.py`: 시작 시 recovery, 단일 원본 bytes snapshot으로 state/history 읽기, 저장 직전 old SHA 확인, archive → history → state transaction 적용.
- `tests/test_p1_b2_atomic_persistence.py`: crash/failure injection 및 main integration 테스트.
- `.github/workflows/tests.yml`: 전용 브랜치 트리거와 핵심 소스 blob SHA pin 갱신. 운영 `run.yml`은 변경하지 않았다.
- `reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md`, 관리 문서와 테스트 가이드를 구현 결과에 맞춰 갱신했다.

### 구현 판단
- 개별 `os.replace`만으로 다중 파일 transaction이 되지 않으므로 PREPARED/APPLYING/COMMITTED journal을 사용한다.
- stage/backup/manifest/journal은 파일 fsync와 디렉터리 fsync를 수행한다. target 적용은 target과 같은 디렉터리에서 임시 파일을 fsync한 뒤 replace한다.
- 복구는 이미 new SHA인 target을 건너뛰고 old SHA인 target만 roll-forward한다. 예상 밖 SHA, journal/stage/backup 손상, 경로 위반은 자동 덮어쓰기 없이 fail-closed 한다.
- 장시간 Gemini/Discord 호출 동안 lock을 잡아두지 않도록 POSIX advisory lock은 recovery와 commit 구간에 한정했다. 대신 읽은 bytes snapshot과 저장 직전 SHA를 비교해 stale write를 차단한다. 이 방식은 로컬 lost-update를 방지하지만, 동시 실행의 Discord 중복 전송은 막지 않는다(P1-B2 범위 밖).
- POSIX `fcntl.flock` 및 directory fsync를 사용하므로 현재 Ubuntu CI 실행 환경을 전제로 한다. Windows 네이티브 호환성은 별도 작업이다.

### 검증
- Run #21: 테스트 파일 SHA pin 불일치로 source-integrity 단계 실패; compileall/pytest는 실행되지 않았다.
- Run #22: pin 정정 후 62 passed / 1 xfailed.
- directory fsync 및 duplicate target 검증을 보강하고 SHA pin을 갱신한 Run #23: **63 passed / 1 xfailed**, source SHA·compileall·전체 pytest 모두 통과.
- CI 증거: https://github.com/useformotor3/ai-discord-bot/actions/runs/43848498440
- P1-B3 Git sync 상태화의 기존 xfail 1건은 범위 밖으로 유지했다.

### 운영 영향 및 잔여 위험
- 운영 `main.py`, `.github/workflows/run.yml`, 운영 `state.json`, `history.json`, `research_archive/` 변경 없음.
- 실제 Gemini/Discord 호출, 운영 Git push, merge/rebase/PR merge 없음.
- Discord 전송과 로컬 저장은 원자적이지 않으며 exactly-once/outbox는 보장하지 않는다.
- compare snapshot commit `0236dbda2793d6dc2ba4dfc245905a73f8783136` 기준 main HEAD `6eec802125c1bcf3cf0b2dd1401a9c6430792920`, branch compare 181 ahead / 673 behind, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; main state count=126, history=2,265; 통합 보류.
- 다음 재개 지점: 구현 diff 및 POSIX 실행환경 제약을 검토하고, 운영 archive/state/history를 보존하는 별도 통합 전략을 설계한다. P1-B3/B4는 별도 승인 전 착수하지 않는다.


## 2026-11-16 — merge-base 통합 전략 감사 및 P1-B2 보강

### 기준 스냅샷
- repo: `useformotor3/ai-discord-bot`
- main HEAD: `260c0c2d38dd658714e58db5e7a4cdb2b34bc5b3` (Auto-archive #129)
- feature HEAD: `2b2645b23876378a6c384c8da819de84104ac49a`
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`
- compare: 189 ahead / 676 behind; diverged.

### 전체 tree 및 데이터 검증
- recursive tree 응답은 base/main/feature 모두 truncated=false.
- base: 1,597 blob / archive 1,592.
- main: 2,273 blob / archive 2,268.
- feature: 1,619 blob / archive 1,592.
- base→main: 676개 archive 추가, 삭제 0, history/state 수정 2.
- base→feature: 22개 경로 추가, 삭제 0, main.py 수정 1.
- feature state/history blob은 base와 동일하다.
- main state count=129, history 2,268건, archive 2,268개. history file 참조 누락 0.
- 따라서 main의 archive 676개는 main에서 분기 후 추가된 자료이며 feature에서 삭제한 것이 아니다. 정상 3-way merge는 이 main 변경을 보존할 수 있는 구조다.

### 추가 코드 검토 및 보강
- P1-B2 `_safe_target()`이 저장소 root 안의 임의 경로를 허용하는 점을 발견했다. 복구 manifest가 변조되면 workflow/code/document를 target으로 지정할 수 있어 통합 전 보강이 필요했다.
- 허용 target을 `state.json`, `history.json`, `research_archive/*.md`로 제한했다.
- `.github/workflows/run.yml`, `.git/config`, README, 코드, archive 하위 폴더 및 비-md 경로 거부 테스트를 추가했다.
- 테스트 workflow를 pull_request→main 및 main push에서도 실행하도록 변경했다. 권한은 contents:read, checkout persist-credentials:false이며 외부 secrets/API 호출 없음.

### 검증
- Actions ID `43851438733`: exact source SHA 확인, compileall 통과, **70 passed / 1 xfailed**.
- source `persistence.py` SHA: `953e2a52b7e6d6e619a4f43766e52d6835df50c8`.
- test SHA: `f78d36164b5ac0d5d5eebe0c5eb5c1214c4e0671`.
- test workflow SHA: `6a5bee0785eccc1f1b8074b80761b1b2a772d3c0`.
- xfail 1건은 P1-B3 Git sync 상태화로 범위 밖.

### 권장 통합 전략 및 경계
- 최신 main을 기준으로 feature→main PR을 생성하고 PR CI 및 conflict check를 검증한 후 merge commit 방식으로 통합하는 안을 권장한다.
- PR Files changed에 state/history/archive/run.yml 삭제·변경이 없어야 한다. compare API는 23개 예상 경로를 보고한다.
- squash/rebase/force-push 및 state/history/archive migration은 피한다.
- PR 생성/merge, 운영 배포, run.yml 변경, 실제 Gemini/Discord 호출은 이번 작업에서 수행하지 않았다. 운영 반영은 별도 승인 대상이다.
- 잔여: POSIX-only flock/fsync, Discord POST와 local persistence 사이의 outbox 부재, non-blocking lock, P1-B3/B4 미구현.
- 상세 보고서: `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`.


## 2026-11-16 — 통합 감사 스냅샷 main #130 갱신
- main은 Auto-archive #130으로 HEAD `3ebf6b977b0127291957ffb415dbdbc83b5b6d97`까지 전진했다.
- 최신 데이터: state count=130, history=2,269건, archive=2,269개, history 참조 누락 0.
- main tree 2,274 blobs, feature tree 1,620 blobs, merge-base tree 1,597 blobs. base→main archive +677/삭제 0; base→feature +23 paths/삭제 0/main.py 수정.
- compare: feature 204 ahead / 677 behind. 수치는 스냅샷이며 main 자동 실행에 따라 계속 변한다.
- PR 변경 예상: 24 paths(23 added + main.py modified). state/history/archive/run.yml은 PR에서 수정·삭제 대상이 아니어야 한다.
- P1-B2 source/test/workflow SHA와 Actions 43851438733(70 passed / 1 xfailed)을 재확인했다.
- main `run.yml` SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지.
- PR 생성, merge, rebase, 운영 데이터/workflow 변경, 운영 실행 및 외부 서비스 호출 없음.


## 2026-11-16 — 최신 원격 branch/main 비교
- 작업 브랜치 HEAD(이 스냅샷 기준): `1aadc3fcd2b2e1b3bf2b45783da9fecb1a91afe7`.
- 운영 main HEAD: `3ebf6b977b0127291957ffb415dbdbc83b5b6d97` (Auto-archive #130).
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare: 216 ahead / 677 behind, diverged; PR compare 변경 파일 24개.
- main state count=130, history=2,269, archive=2,269, 참조 누락 0.
- 이 ahead 수치는 이 스냅샷 commit 기준이며, 로그/문서 추가 commit 이후 증가한다. main 자동 아카이브도 계속 변하므로 PR 직전 재조회한다.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지. PR/merge/운영 실행은 수행하지 않았다.


## 2026-11-16 — main 자동 아카이브 #131 반영
- 운영 main HEAD `267d97478b785e6bb268e224a70dbad6631cf43e` (#131).
- state count=131, history=2,270건, archive=2,270개, history 참조 누락 0.
- recursive tree main 2,275 blobs / archive 2,270; merge-base 1,597 blobs / archive 1,592; main은 merge-base 이후 archive 678개 추가, 삭제 0.
- 작업 브랜치 비교 스냅샷 `02fde2489323f9f553405e014fac20d75d13a7fa`: 221 ahead / 678 behind; PR changed files 24개.
- PR 생성/merge/운영 workflow 및 데이터 변경/실제 외부 호출 없음.



## 2026-11-16 — PR 사전 검사 결과 (원격 HEAD 고정)
- 운영 main HEAD: `267d97478b785e6bb268e224a70dbad6631cf43e` (Auto-archive #131).
- 작업 브랜치 HEAD(검사 기준): `be3e243a7cccaf8cf26b2ced453b733098debadd`.
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; compare 228 ahead / 678 behind.
- GitHub compare의 전체 변경 경로 24개: 신규 23개 + `main.py` 수정 1개, 삭제 0개.
- 변경 경로에 `state.json`, `history.json`, `research_archive/**`, 운영 `.github/workflows/run.yml` 없음.
- merge-base/main의 `main.py` blob SHA 모두 `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; main 쪽은 분기 이후 이 파일이 바뀌지 않았다. 작업 브랜치 main.py만 `fa8679b758916ba8a446bae41b9ec1b40328da09`로 변경됐다. 따라서 현재 확인 범위에서 main.py의 양쪽 동시 수정 충돌 요인은 없다.
- 테스트 workflow SHA `6a5bee0785eccc1f1b8074b80761b1b2a772d3c0`; `pull_request: branches: [main]`, `permissions: contents: read`, checkout `persist-credentials: false`.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지.
- Actions #43851438733은 성공(70 passed / 1 xfailed). 실행 HEAD는 `2b2645b23876378a6c384c8da819de84104ac49a`; 이후 변경은 문서/로그만이며 검증 대상 main.py, persistence.py, 테스트 파일, test workflow의 blob SHA가 동일함을 재확인했다.
- PR은 아직 생성하지 않았으므로 GitHub의 실제 `mergeable` 결과와 PR-triggered CI는 미확인. 현재는 merge-base/tree 및 파일 경로 사전 검사 결과이지 최종 충돌 판정이 아니다.
- PR 생성, merge/rebase/force-push, 운영 workflow/data 변경, 실제 Gemini/Discord 호출은 수행하지 않았다.



## 2026-11-16 — main 자동 아카이브 #132 이후 최신 재조회
- 운영 main HEAD `7296fcd9261a3171fc2cc8a5a51bde73dcf052cb` (Auto-archive #132); 작업 브랜치 감사 기준 HEAD `74b2c1281fe89a96b94ba13fbac74189350c4aa8`.
- merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; compare 229 ahead / 679 behind.
- 운영 state count=132, history=2,271, archive=2,271, history→archive 참조 누락 0.
- main recursive tree 2,276 blobs; tree 응답 truncated=false.
- PR 변경 경로 24개(23 added + main.py modified), 삭제 0. 보호 경로(state/history/archive/run.yml) 변경 없음.
- main.py merge-base/main blob SHA 동일 `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; 작업 브랜치 blob SHA `fa8679b758916ba8a446bae41b9ec1b40328da09`. 분기 이후 main.py의 양측 동시 수정은 확인되지 않음.
- PR 미생성 상태이므로 GitHub mergeable 및 PR-triggered CI는 아직 미확인. 실제 통합 가능 여부는 PR 생성 후 재검증한다.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지.


## 2026-11-16 — Draft PR #1 생성 및 PR-triggered CI
### 작업
- 사용자 승인에 따라 `feature/p1-b2-atomic-persistence-2026-11-16` → `main` Draft PR #1 생성.
- PR: https://github.com/useformotor3/ai-discord-bot/pull/1
- PR head `01e7cf50436f35d9eddb931ae4e1d177af805387`; 생성 시 base SHA `38abb075ebe0f7180abaebc4da52e2f18ea28915`.
- PR 생성 직전 compare 230 ahead / 700 behind, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; changed files 24 (23 added, main.py modified, 0 deleted).
- protected paths `state.json`, `history.json`, `research_archive/**`, production `.github/workflows/run.yml` absent from changed paths.

### 검증 결과
- PR 상태 재조회: open, draft, not merged, mergeable=true.
- PR-triggered Actions Run #32 / ID `43869220252`: success.
- Job `Source integrity, compile and pytest`: all steps completed successfully, including exact source blob integrity, compile, and complete repository pytest suite.
- Run #43851438733 (pre-PR code validation): 70 passed / 1 xfailed. PR-triggered Run #32 exact test counts not exposed in job summary; do not infer.
- Run URL: https://github.com/useformotor3/ai-discord-bot/actions/runs/43869220252

### 경계 및 다음 단계
- Draft PR 생성만 수행. merge/rebase/force-push/운영 배포/운영 workflow 또는 state-history-archive 변경/실제 Gemini·Discord 호출 없음.
- GitHub mergeable=true는 조회 시점 상태이며 main 자동 커밋에 따라 바뀔 수 있다.
- 다음은 PR 리뷰와 최신 main 기준 재검토. 병합 및 운영 반영은 별도 승인 대상.


## 2026-11-16 — 상시 진행 지시, PR 재조회 및 복구 체크포인트
### 사용자 운영 지시
- 사용자는 이후 매 단계별 승인을 묻지 말고 목표 달성에 필요한 작업을 계속 진행하라고 지시했다.
- main 및 관련 운영 파일 수정도 허용하되, 실행 후 이상 발생 시 정상 코드로 복귀하고 데이터도 복구할 수 있어야 한다는 요구를 명시했다.
- 이에 따라 AI_RULEBOOK.md §18을 추가해 상시 진행 권한과 복구 우선 게이트를 문서화했다.

### 현재 원격 상태 재확인
- main HEAD: 2622e332d6a3defd2079ccad3af36970001de5c1 (Auto-archive #156).
- feature HEAD: eba3aeb5710dcc6507623d56d586a619e9a4fc46.
- merge-base: f9a12a5778f5fa1d907201ab2931d20ca2656bb7; compare 231 ahead / 703 behind.
- PR #1은 open/draft/not merged. mergeable 값이 조회 중 false→true로 변동했고 PR base SHA는 main 최신 HEAD와 일치하지 않는 값을 반환했다. PR head 기준 CI Run #33 success는 확인했으나 최신 main base와 통합된 commit의 CI 결과는 별도로 검증해야 한다.

### 롤백 준비
- main backup branch: safety/pre-merge-main-2622e332 → 2622e332d6a3defd2079ccad3af36970001de5c1.
- feature backup branch: safety/pre-merge-feature-eba3aeb → eba3aeb5710dcc6507623d56d586a619e9a4fc46.
- 현재 Git 코드 기준점은 보존했으나 state/history/archive의 별도 snapshot/restore는 아직 검증되지 않았다. 따라서 운영 데이터까지 복구 준비 완료라고 표현하지 않는다.
- main merge, workflow 변경, 운영 실행은 아직 하지 않았다. 먼저 backup ref readback 및 데이터 복원 리허설을 진행한다.

## 2026-11-16 — main #158 immutable data baseline 감사
- main HEAD 4cf0e708b28a343898af00d01521044dfb9a1987 (Auto-archive #158).
- backup safety/pre-merge-main-4cf0e70 readback SHA exact match.
- tree entries 2,305, truncated=false; state count=158; history=2,297; archive=2,297; missing references=0.
- U+200B ZERO WIDTH SPACE가 앞에 붙은 별도 state file(date=2026-06-07,count=0)은 보존한다.
- 이전 moving-ref 조회에서 나타난 history/archive 차이는 동일 immutable SHA에서 재현되지 않아 snapshot race로 정정했다.
- per-run 자동 snapshot/restore는 미구현/미검증이므로 첫 운영 실행 전 복원 리허설을 진행한다.

## 2026-11-16 — production data checkpoint 및 rollback guard 구현
- .github/workflows/run.yml: 실행 전 safety snapshot, concurrency, Python 3.11, 15분 timeout, post-run guard.
- scripts/operational_guard.py: baseline/current snapshot, single-child/remote HEAD/changed path, append-only history, archive refs, state count, quota no-op, data-only restore commit.
- tests/test_operational_guard.py: 정상 전이, append-only 위반, archive 누락/삭제, count 오류, 날짜 변경, unsafe path, bare remote 복구/미push/quota no-op.
- .github/workflows/tests.yml: scripts compile 및 source blob pins, run.yml/scripts 변경 시 CI.
- Run #43873774430: 80 passed, 1 failed, 1 xfailed. Fixture baseline 오류 수정.
- 최종 Run #43874801395: 86 passed, 1 xfailed; compileall 및 source SHA 확인 성공. PR base f5b5a112ec72b01f8b3f91f734b8d755dde416c6.
- main #161 baseline: state 161, history 2,300, archive 2,300, missing 0. safety/pre-merge-main-f5b5a11 exact SHA.
- actual Gemini/Discord/production workflow not executed.


## 2026-11-16 — main #162 final pre-merge snapshot
- main SHA adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890 (Auto-archive #162), state count 162, history 2,301, archive 2,301, missing refs 0.
- safety/pre-merge-main-adf74ea readback exact SHA; feature backup safety/pre-merge-feature-abee2a8 readback exact SHA.
- PR #1 current code/test/workflow validation: Run #43875746973 success, 87 passed, 1 xfailed.
- Code rollback and data-only rollback are separate; production workflow now creates pre-run snapshot branch and only auto-restores when remote main is exactly the run's single child commit.
- actual production execution not yet performed.

## 2026-11-16 — PR #1 merge 및 post-merge 검증
### 통합
- PR #1: https://github.com/useformotor3/ai-discord-bot/pull/1
- merge commit: 6fd03efaf8623cb3ec2ab938aa7161b41ffed82e
- parent 1 main #162: adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890
- parent 2 feature: d48ae1c9b655d7384aff497c9d17168a5d0b25c5
- post-merge backup: safety/post-merge-main-6fd03ef, readback exact SHA.

### 검증
- push CI Run #43876347620 success; 87 passed, 1 xfailed; source blob identity, compileall, full pytest all passed.
- same merge commit tree: state count 162, history 2,301, archive 2,301, history reference missing 0.
- state/history blob SHA match pre-merge main #162; operational data was not changed by PR merge.
- production workflow trigger remains repository_dispatch/workflow_dispatch; merge push ran only isolated test workflow. No actual Gemini/Discord or production workflow invocation.

### 다음
- first production workflow run is not yet executed. Before it, ensure snapshot branch and concurrency are active; after it, verify the guard result and archive/history/state invariants.
- Discord messages, once sent, cannot be recalled by Git rollback.


## 2026-11-17 — 운영 실행 #2412 경합 장애 및 복구 조치
- #2411(43958205823)은 성공. #2412(43959068835)는 실행 중 main이 b89f2bf로 이동해 로컬 Auto-archive #235 commit ef4ca1fa의 push가 non-fast-forward로 거부됨.
- main.py는 push 실패를 출력하고 진행했으나 operational_guard가 remote main 불일치를 감지해 자동 복구를 거부하고 workflow를 실패 처리함. 로컬 report #235는 원격 archive/history/state에 저장되지 않았고 Discord 2/2 청크는 이미 전송됨.
- 동시 실행 중 main을 수정한 작업 순서 오류를 기록. 앞으로 운영 workflow 활성 여부를 먼저 확인하고 종료 뒤 main 변경.
- checkpoint refs 94개 누적 확인. 성공 검증 후 최근 30개+현재 baseline ref를 보존하는 pruning 스크립트/step 추가.
- CI #43959203356: 96 passed, 1 failed, 1 xfailed. 보호된 오래된 ref를 추가 보존하는 테스트의 기대값 오류로 판명, 수정 후 재검증 예정.
- Gemini gemini-flash-latest 404 3회 후 fallback 경로로 진행. 모델 사용 가능성 별도 확인 필요.
- 상세: reports/GITHUB_AUTOMATION_INCIDENT_2026-11-17.md.


## 2026-11-17 — KST·Gemini fallback·Git push fail-closed 개선
- 최신 운영 #2431 success. guard/pruning 모두 통과. checkpoint ref 수 30개, 최신 baseline 포함.
- state date가 runner UTC 날짜(2026-11-16)로 기록되는 문제 발견. KST는 2026-11-17이므로 daily count 경계가 9시간 늦게 바뀌는 결함으로 판정.
- main.py: Asia/Seoul aware datetime 사용, legacy naive UTC timestamp는 UTC로 간주해 KST로 변환.
- Gemini API 공식 모델 자료에서 gemini-3.8-flash, gemini-3.5-flash-lite 확인. 모델 404/NOT_FOUND는 즉시 fallback, 일시 오류 재시도는 유지.
- Git 저장 오류를 warning-only에서 SystemExit(1)로 변경해 저장 실패를 성공처럼 취급하지 않도록 함. 원격 덮어쓰기/강제 push 없음.
- 회귀 테스트: KST 기준 날짜, timezone-aware 및 legacy naive timestamp, 모델 404 fallback, Git push 실패 fail-closed.
- 상세: reports/OPS_TIMEZONE_MODEL_GIT_FAILURE_FIX_2026-11-17.md.
- CI 통과 전까지 변경 완료 선언 금지.

- CI Run #58은 테스트에 남아 있던 gemini-flash-latest 기대값 2건으로 실패(95 passed, 2 failed, 1 xfailed). 원인 확인 후 기대값을 gemini-3.8-flash로 수정하고 404 fallback/Git push 실패 테스트를 추가.
- CI Run #59 성공: 99 passed, 1 xfailed. SHA pin, compileall, 전체 pytest 통과.
- 최신 main fc77d6da07684936a27a60eb1a4cb920ceb37c14. production active run 없음 확인.
- 데이터 readback: state count=254, history/archive=2,393/2,393, 참조 누락 0, checkpoint refs 30. 신규 KST 코드는 실제 운영 실행 전이므로 다음 run 검증 대기.


## 2026-11-17 — KST 운영 적용 및 저장 무결성 readback
- main HEAD `655bde43483f4c2e793954e4206590d768e6ab74`에서 운영 코드와 데이터 재조회.
- state date=2026-11-17, count=4 확인.
- history.json 전체 JSON 파싱 성공, 2,397 entries.
- 마지막 4개 history의 KST 시간은 08:05:32, 08:10:37, 08:15:40, 08:20:40이며 count 1~4.
- history가 가리키는 최근 archive 4개 파일 모두 원격에서 존재 및 blob SHA 확인.
- 보고서 #1~#4 auto-archive commits 확인. #4 commit diff는 history append, archive 신규 생성, state count 3→4를 보여준다.
- 운영 Git 저장 및 KST date/count/archive 반영은 확인됨.
- 상세 Actions job log는 현재 도구에서 조회할 수 없어 실제 Gemini model ID, operational_guard, checkpoint pruning, Discord 응답 성공은 미확인으로 남긴다.
- 상세 보고서: `reports/PRODUCTION_RUN_OBSERVATION_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #4 근거 더블체크 및 정정
- 원본 보고서 #4를 EUR-Lex Regulation (EU) 2024/2847, NIST SP 800-88, IEC 62443-4-2 자료와 대조.
- Annex I Part I (2)(i) 인용이 잘못됐고, 사용자 데이터 영구 삭제는 (2)(m)에 해당함을 확인.
- IEC 62443-4-2 CR 4.1(정보 기밀성)과 CR 4.2(정보 잔존/삭제), CR 4.3(암호기술 사용)을 구분.
- NIST SP 800-88 Rev.1은 2025-09-26 철회·Rev.2 대체 확인. Flash multi-pass overwrite는 NIST Rev.2의 저장매체별 주의사항과 맞지 않아 제거.
- CRA가 특정 hardware/firmware/CE 구현을 직접 의무화한다고 단정한 문장을 법적 요구와 엔지니어링 권고로 분리.
- 원본 archive는 보존하고 정정 문서를 별도 작성.
- 상세: `reports/CRA_CORRECTION_REPORT_4_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #3 근거 더블체크 및 정정
- EUR-Lex 공식 원문 Article 13(8)/(9), Annex I Part I (2)(c), Part II (2)/(4)/(7)/(8) 대조.
- Article 13(8)은 support period(최소 5년 원칙, 제품 예상 사용 기간이 더 짧으면 그 기간)이며, 원본이 인용한 보안 업데이트 무상/분리 문구가 아님.
- 분리 제공: Annex I Part II (2), 단 “where technically feasible” 조건.
- 무상 제공: Annex I Part II (8), 단 맞춤형 제품에 대해 제조사와 business user가 달리 합의한 경우 예외.
- 업데이트 장기 이용 가능성: Article 13(9), 발행 후 최소 10년 또는 support period 잔여기간 중 더 긴 기간.
- 취약점 공개: Annex I Part II (4). CVE ID/CSAF는 법령이 지정한 형식이 아니라 운영 권고.
- 자동 rollback/Safe State/독립적 패치 선택은 법적 문언과 구분해 엔지니어링 권고로 분류.
- IEC 62443-4-1 Practice 7 연결은 주제상 타당하나, 공개 자료만으로 상세 조항 적합성을 선언하지 않음.
- 원본 archive는 보존하고 정정 문서를 별도 작성.
- 상세: `reports/CRA_CORRECTION_REPORT_3_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #2 근거 더블체크 및 정정
- EUR-Lex 공식 원문 Articles 11, 13–16, 69, 71 및 Annex I Part II, Annex II, Annex VII 대조.
- Article 11은 General product safety이며 CVD 근거가 아님. CVD는 Article 13(8)/(17), Annex I Part II (5)/(6), Annex II (2).
- Article 14는 Reporting obligations of manufacturers. 원본 Article 11 명의의 인용문은 공식 원문과 일치하지 않음.
- actively exploited vulnerability: 24h early warning, 72h vulnerability notification, 시정/완화 조치 가용 후 14일 final report.
- severe incident: 24h early warning, 72h incident notification, notification 제출 후 1개월 final report.
- 단일 신고 플랫폼 및 coordinating CSIRT/ENISA 동시 통지, Article 14(8) 사용자 통지 반영.
- Article 14는 2026-09-11부터 적용, Article 69(3)에 따라 이전 시장 출시된 CRA 범위 제품에도 적용.
- Annex II는 사용자 지침, Annex VII가 기술문서.
- 원본 archive 보존, 정정 문서 별도 작성.
- 상세: `reports/CRA_CORRECTION_REPORT_2_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #1 근거 더블체크 및 정정
- EUR-Lex Regulation (EU) 2024/2847 Article 11, Article 13(8)/(17), Annex I Part I (2)(c)/(f), Part II (5)–(8), Annex II/VII 대조.
- Article 11은 General product safety. 제조사 의무는 Article 13.
- 지원 기간은 Article 13(8), 무상 보안 업데이트는 Annex I Part II (8). 원본 Article 11(2)(c) 직접 인용문은 공식 원문과 불일치.
- CVD 정책·제보 연락처·안전 배포는 Annex I Part II (5)–(7), Article 13(17), Annex II (2).
- 디지털 서명은 보안 무결성 구현 수단, STO 연계 설치는 제품별 안전 검증 권고로 분리.
- 원본 archive는 보존하고 정정 문서를 별도 작성.
- 상세: `reports/CRA_CORRECTION_REPORT_1_2026-11-17.md`.


## 2026-11-17 — CRA 공식 원문 출처검증 gate 구현 및 재검증

### 배경 및 원인
- 2026-11-17 생성된 CRA 보고서 4건을 공식 EUR-Lex 원문과 대조한 결과, 법령 조항 오인, 원문 인용 불일치, 의무/권고 혼동이 확인됐다.
- 기존 생성기는 client.models.generate_content 일반 텍스트 생성만 사용했고, validator는 길이·필수 섹션·오류 문구만 검사했다. 출처 URL·조항·직접 인용의 사실 대조가 없었다.
- Gemini 3 계열 Google Search Grounding은 Free tier에서 제공되지 않는 현재 요금표 조건을 확인해 무료 운영 경로로 선택하지 않았다.

### 변경 및 안전 경계
- 기준 main SHA: 0dde26ebac80a789c7a9d9e26560abad54606d32.
- 복구 브랜치: safety/pre-cra-source-grounding-2026-11-17.
- 작업 브랜치: feature/cra-source-grounding-atomic-2026-11-17.
- Draft PR #3: https://github.com/useformotor3/ai-discord-bot/pull/3.
- cra_source.py: EUR-Lex 공식 HTTPS HTML endpoint 직접 조회, 최종 호스트 검사, 최소 본문 길이, 통합본/정오표 날짜 검사, whitespace 정규화.
- main.py: 공식 원문 수집 성공 후 Gemini 실행, URL/버전/Article/Annex/50자 이상 인용문 원문 대조, 실패 시 후속 처리 중단, 초안/미검증 상태 표시.
- 테스트 fixture: EUR-Lex HTTP, Gemini, Discord, Git을 mock. 원문 503, 비공식 redirect, corrigenda 누락, 직접 인용 불일치 차단 테스트 추가.
- 운영 main, .github/workflows/run.yml, 운영 state/history/archive 미변경. 실제 Gemini/Discord 호출 및 운영 workflow 실행 없음.

### 검증
- 최초 CI Run #79: 97 passed, 5 failed, 1 xfailed. 테스트 간 requests 모듈 캐시로 source mock이 현재 테스트 호출을 포착하지 못하는 문제를 확인.
- HTTP 의존성을 호출 시점 import로 변경하고 fixture 기대 키를 갱신.
- CI Run #83: 102 passed, 1 xfailed.
- corrigenda C1/C2/C3 인덱스 날짜 검사 및 source version 메타데이터를 추가.
- CI Run #89: 103 passed, 1 xfailed; blob SHA 확인·compileall·전체 pytest 모두 통과.
- Run #89 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43985975373.

### 제한 및 다음 단계
- 통합본은 문서화 도구이며 관보 정본/정오표의 법적 효력을 대체하지 않는다.
- provenance gate는 최소 출처 추적성 및 직접 인용 대조일 뿐, 모든 주장·해석·제품 분류·적합성 결론을 검증하지 않는다.
- 실제 EUR-Lex endpoint canary, 실제 Gemini/Discord, 운영 실행은 미수행.
- 다음은 비운영 canary로 endpoint와 응답 구조를 확인하고, 주장별 조항·인용 연결 검증을 강화한다.
- 상세: reports/CRA_SOURCE_PROVENANCE_GATE_2026-11-17.md.


## 2026-11-17 — 상황판·행동강령·테스트 문서 동기화
- README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG.jsonl, tests/README 및 CRA 출처검증 설계 보고서를 작업 브랜치에 기록했다.
- 테스트 workflow push branch/path 필터에 현재 source-gate 브랜치와 cra_source.py를 추가했다.
- 최신 CI Run #91: 103 passed, 1 xfailed; blob SHA, compileall, 전체 pytest 성공.
- CI 링크: https://github.com/useformotor3/ai-discord-bot/actions/runs/43986374463.
- 코드 검증은 Run #89와 #91 모두 성공. 문서 변경은 기존 코드 동작을 바꾸지 않는다.
- 운영 main 및 production workflow 미변경, Draft PR #3 유지.


## 2026-11-17 — 최종 PR 및 복구 상태 정리
- PR #2는 PR #3으로 대체되어 closed (not merged) 처리했다. 원 브랜치와 커밋은 감사 추적을 위해 유지한다.
- 최종 작업 PR #3은 Draft/open 상태이며 mergeable=true, 아직 main에 병합하지 않았다.
- 최종 작업 브랜치: feature/cra-source-grounding-atomic-2026-11-17.
- 기준 main SHA: 0dde26ebac80a789c7a9d9e26560abad54606d32. 안전 복구 브랜치 safety/pre-cra-source-grounding-2026-11-17도 동일 SHA를 보존한다.
- 최신 CI Run #93: 103 passed, 1 xfailed; source SHA, compileall, 전체 pytest 성공. 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43986520995.
- 운영 main은 자동 archive로 별도 전진할 수 있으므로 병합 시점에는 main 최신 SHA와 diff를 다시 확인해야 한다.
- 운영 main, production run.yml, state/history/archive는 이번 작업에서 수정하지 않았다.


## 2026-11-17 — EUR-Lex 실제 endpoint canary 성공 및 법적 효력 주의 강화
- Read-only canary workflow .github/workflows/cra-source-canary.yml 및 scripts/cra_source_canary.py 추가.
- 최초 canary #1은 스크립트 실행 시 repo root import 경로가 없어 실패. 스크립트에서 저장소 root를 sys.path에 추가해 해결.
- Canary Run #3 / #5 success: 공식 EUR-Lex HTTPS URL fetch, final host 확인, visible text 196,076 characters, corrigenda 날짜 5.12.2024 / 2.7.2025 / 17.10.2025 확인.
- Canary Run #5 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987091981.
- Validator 강화: EUR-Lex consolidated text는 documentation tool이며 Official Journal(관보) 정본 및 공식 corrigenda가 법적 효력의 기준이라는 문구가 보고서에 없으면 reject.
- Isolated CI Run #107: 103 passed, 1 xfailed; blob SHA, compileall, full pytest 성공. 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987116390.
- 실제 Gemini/Discord/production workflow는 실행하지 않았다. Canary는 EUR-Lex read-only GET만 수행했다.
- 다음 단계: 주장별 근거 매핑, 원문 hash/version change detection, 검증 실패 시 review queue.


## 2026-11-17 — 법적 효력 caveat 포함 최종 코드 및 canary 재검증
- Validator는 EUR-Lex 통합본이 documentation tool이며 Official Journal(관보) 정본과 공식 corrigenda가 법적 효력의 기준임을 보고서에 명시하도록 요구한다.
- Isolated CI Run #109: 103 passed, 1 xfailed; source blob SHA, compileall, 전체 pytest 성공. 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987545006.
- Read-only EUR-Lex canary Run #10: success; 196,076자 visible text와 정오표 날짜 3개 확인. 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987552717.
- Canary는 public EUR-Lex HTTPS GET만 수행한다. 실제 Gemini/Discord/production workflow 호출은 없다.
- 운영 main 및 run.yml 미변경, PR #3은 Draft/open 상태.


## 2026-11-17 — 최종 재실행 결과
- 최신 isolated CI Run #111: 103 passed, 1 xfailed. source SHA, compileall, full pytest 성공. 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987722348.
- 최신 EUR-Lex read-only canary Run #11: success. 공식 endpoint에서 196,076자 수집, 정오표 3개 날짜 확인. 로그: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987730194.
- EUR-Lex consolidated text의 법적 효력 caveat를 prompt/validator/archive에 반영했다.
- 운영 Gemini/Discord/production workflow는 호출하지 않았고, PR #3은 Draft/open 유지.


## 2026-11-17 — CRA 후속 법령 source pack 구현 및 검증
- cra_source.py에 EUR-Lex 공식 후속 법령 3건을 추가하고, main.py 프롬프트에서 적용 범위를 구분했다.
- tests/conftest.py 및 tests/test_main_characterization.py mock을 네 원문으로 확장하고, 전체 테스트 및 blob SHA pin을 갱신했다.
- CI Run #141: 103 passed, 1 xfailed; compileall 및 전체 pytest 성공. https://github.com/useformotor3/ai-discord-bot/actions/runs/43989211881
- EUR-Lex read-only canary Run #26: 성공. CRA 통합본과 후속 법령 3건 총 220,715자 visible text, 정오표 3개 날짜 확인. https://github.com/useformotor3/ai-discord-bot/actions/runs/43989211861
- 코드 변경은 Draft PR #3에 존재하며 main 미병합. 운영 main.py/run.yml, Gemini/Discord 호출 없음.
- 상세: reports/CRA_SOURCE_PROVENANCE_GATE_2026-11-17.md.


## 2026-11-17 — 최종 문서·SHA·CI 동기화
- 최신 작업 브랜치 SHA: d564e91faf616d95c0ab91c269fcfc3315413c50.
- CI Run #154: 103 passed, 1 xfailed; source SHA, compileall, full pytest success. https://github.com/useformotor3/ai-discord-bot/actions/runs/43995859144
- EUR-Lex canary Run #29: success; 4개 공식 법령 source pack 및 CRA 정오표 3개 날짜 확인. https://github.com/useformotor3/ai-discord-bot/actions/runs/43995859223
- 보고서·README·PROJECT_STATUS·MASTER_PLAN·SESSION_LOG·tests README·PROJECT_LOG를 같은 실행 결과로 동기화했다.
- Draft PR #3은 main에 미병합. 운영 main SHA ff599733d62a8926ee281a9958aa6e03f5ce75f4.


## 2026-11-17 — CRA 주장별 근거 추적성 구현
- 작업 브랜치: `feature/cra-source-grounding-atomic-2026-11-17`.
- 변경: `cra_claims.py` 신규, `main.py` prompt/validation 연결, `tests/test_cra_claims.py` 신규 및 기존 mock report fixture 보강, isolated tests workflow source pin/경로 보강.
- 복구 ref: `safety/pre-claim-evidence-2026-11-17-d8870e3` → `d8870e32e16ba5ebd3a7670d12816324de3b485a`.
- CI 첫 실행에서 85 passed / 27 failed / 1 xfailed. f-string JSON brace 충돌, fixture의 새 JSON contract 누락 및 assertion 우선순위 오류를 확인하고 수정했다.
- 수정 후 최종 정확한 head SHA CI 결과는 별도 확인 전까지 미확정이다. 운영 main 및 production workflow는 변경하지 않았으며 실제 Gemini/Discord 호출도 없다.


## 2026-11-17 — CRA claim-to-evidence gate 최종 격리 CI 통과
- 최종 작업 브랜치 SHA: `b11f0dcb9bc8f41a0e82ac8062c75c1ca2d08143`.
- Isolated CI Run #194: **112 passed, 1 xfailed**; source blob SHA pin, compileall, full pytest 모두 성공.
- EUR-Lex read-only canary Run #53: success.
- CI: https://github.com/useformotor3/ai-discord-bot/actions/runs/43998058880
- Canary: https://github.com/useformotor3/ai-discord-bot/actions/runs/43998058856
- CI 로그에서 85/27 실패 원인(f-string JSON brace 및 기존 mock contract)과 후속 blob pin mismatch를 확인하고 각각 수정했다. 최종 run에서 전체 검증 통과.
- PR #3 Draft/open 유지. 최신 main과 8 commits behind이므로 병합하지 않았다. 실제 Gemini/Discord 및 production workflow 미실행.


### 문서 동기화 후 정확한 head 재검증
- 문서/테스트 가이드/프로젝트 로그 동기화 head `7c9360ad6c4e833e0037e3fbc0756d736a15efd2`에서 Isolated CI Run #206 성공: **112 passed, 1 xfailed**.
- Source SHA pin, compileall, full pytest 통과. https://github.com/useformotor3/ai-discord-bot/actions/runs/43998309434


## 2026-11-17 — 수동 Free Tier 게이트 Gemini canary 구현
- 안전 복구 ref: `safety/pre-gemini-json-canary-2026-11-17-198dfcc` → `198dfcc84b872e5ade7a58c673df335c7c97dcf9`.
- 추가: `scripts/cra_gemini_canary.py`, `tests/test_cra_gemini_canary.py`, `.github/workflows/cra-gemini-canary.yml`.
- 고정 synthetic text 1건, 1회 REST 요청, 20초 timeout, JSON claim schema/quote matching, API key header-only. Search Grounding 없음.
- Manual workflow only, `confirm_free_tier=false` default. 실제 project billing tier를 확인할 수 없어 live API 호출은 하지 않는다.
- workflow는 현재 Draft PR branch에만 있으므로 default branch 반영 전 dispatch 불가. 운영 workflow에는 영향 없음.


## Gemini canary mock tests 통과
- head `e2f3dbbc9e6cfb5bbd414cf410b5e23e506ed135`, CI Run #247: **116 passed, 1 xfailed**.
- Source SHA pin / compileall / full pytest 성공. https://github.com/useformotor3/ai-discord-bot/actions/runs/43998889661
- Canary tests use mocked HTTP opener only; live Gemini API requests remain zero.


### Gemini canary 최종 head CI
- head `173181265a157bb0086358ea0479c93941149dc6`: Isolated CI Run #257 **116 passed, 1 xfailed**.
- EUR-Lex read-only Canary Run #85 success.
- CI: https://github.com/useformotor3/ai-discord-bot/actions/runs/43999017790
- Canary: https://github.com/useformotor3/ai-discord-bot/actions/runs/43999023906
- Live Gemini API 호출은 하지 않았으며 manual Free Tier gate는 유지.


### Gemini canary 문서/로그 최신 head 재검증
- head `d335612023398184c54b6b86e9c56e7668779a7c`: CI Run #266 **116 passed, 1 xfailed**.
- Exact source SHA pin, compileall, full pytest 성공.
- https://github.com/useformotor3/ai-discord-bot/actions/runs/43999131134

## 2026-11-17 — 최신 main 통합 사전 감사 및 claim quote 범위 수정
- 저장소 최신 상태를 재조회했다. main 9ad23da7136e3af7167048be51a0bf7f7c96d850, feature 감사 기준 3b1c2f3481e9b2e89288cbec80dfbff3d854c8b5, merge-base 0dde26ebac80a789c7a9d9e26560abad54606d32; compare는 116 ahead / 9 behind.
- main의 main.py는 CRA source/claim validator를 import하지 않고, main tests workflow의 exact SHA pins도 기존 P1-B2 기준이다. feature workflow는 CRA 모듈과 테스트까지 pin한다.
- 기존 claim validator는 quote가 source 전체에 존재하는지만 확인했다. Article locator가 존재하되 quote가 다른 Article에 있어도 통과할 수 있는 false-positive를 재현하는 테스트를 추가했다.
- _quote_is_in_locator_scope를 추가해 Article/Annex scope 내 quote 여부를 검사한다. paragraph/point 정확 경계는 아직 미검증이며 추가 작업 대상이다.
- validator commit 0706df175d23cef3f40eeccebb96a08a728bafec, regression test commit fee65c436a0a112f6415d01aca35a9ba7c72a83c, workflow pin commit 3b1c2f3481e9b2e89288cbec80dfbff3d854c8b5.
- 기존 head CI #274 success 및 EUR-Lex Canary #93 success. 신규 CI #279 / Canary #95는 pending 상태로 시작했으며 최종 결과 재확인 필요.
- EUR-Lex Official Journal에서 세 영어 corrigenda를 독립 확인: 2024-12-05 title의 “No” 삭제, 2025-07-02 Article 64(10) “paragraphs 3 to 9” → “paragraphs 2 to 9”, 2025-10-17 Article 67 “69” → “72”. 현재 source fetch는 날짜 인덱스만 확인하고 정정문 개별 fetch/대조는 하지 않는다.
- 상세: reports/INTEGRATION_AND_CLAIM_SCOPE_AUDIT_2026-11-17.md.
- main / 운영 run.yml / state / history / archive 변경 없음. merge/rebase/force-push/production 실행/Gemini live call 없음. PR #3 Draft 유지.

## 2026-11-17 — CRA claim scope helper 수정 및 CI 회복
- 최초 helper 구현에서 정규식 escape를 이중 처리해 CI #279가 실패했다: 25 failed, 92 passed, 1 xfailed. job log에서 주요 원인은 claim quote scope가 정상 fixture에서 false가 된 것이었고, 그 결과 main 통합 fixture들이 연쇄 실패했다.
- 정규식 escape를 바로잡고 workflow SHA pin을 새 blob으로 갱신했다.
- 수정 후 Isolated CI Run #294: **117 passed, 1 xfailed**. Exact blob SHA, compileall, 전체 pytest 성공.
- EUR-Lex read-only Canary Run #101: success.
- 실패 Run #279는 이력으로 유지하며, 수정 후 성공과 구분한다.
- PROJECT_LOG.jsonl은 UTF-8 원문 전체를 보존한 채 빈 줄을 제거하고 1행 1 JSON 객체 형식으로 정리했으며, 수정 후 검증 event를 추가했다.
- 마지막 compare 스냅샷: main 83bc2430842413080e73bc5b98a8a82c45d03909, feature 784c41a90bd77dd5776c1637f6abe646452e7175, 125 ahead / 10 behind. main 자동 archive가 계속 전진하므로 통합 직전 재조회한다.
- Official Journal corrigenda 개별 원문 fetch/문구 검증은 미완료. PR #3 Draft 유지, main/운영 workflow/state/history/archive 변경 없음, production/Gemini live 호출 없음.
