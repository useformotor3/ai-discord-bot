## 2026-11-23 — LS메카피온 제품군 증거 등록 및 PR #203 검증 동기화

- PR #203 병합 완료: merge SHA `584a7c092ea434d52f7794452ca85b0cbe981210`.
- PR exact-head Run #1343 / ID `45133630273`: success. Main push Run #1344 / ID `45133730871`: success. 전체 테스트·CRA traceability·공식 PDF/HTML canary·provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- 복구 기준점: `safety/post-merge-pr203-2026-11-23`.
- LS메카피온 공식 드라이브 페이지에서 iX700M, iX7M, iX7NH, L7NHA/B, L7NHF, L7PA/B, PHOX, L7C, L7SA/B, GEM 제품군을 확인. 제품군별 전압·용량·통신 유형이 달라 단일 SKU처럼 다루지 않음.
- iX700M 공개 모델코드 예시 `iX700MD1-B-150B`의 코드 구성은 제조사 인증서 페이지에서 확인. 실제 대상 모델이라고 단정하지 않음.
- 통합 보고서 작업 브랜치 v0.15 → v0.16, §46 추가. 상세 증거 등록부 `reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md` 작성.
- iX700M Ver1.4 매뉴얼 및 PEGA2 Ver1.3 매뉴얼의 제조사 목록 메타데이터는 확인했으나, iX700M Ver1.4 본문 PDF는 확보하지 못함. 미열람 내용을 검증된 사실처럼 쓰지 않음.
- 제품별 Annex III/IV 분류는 정확한 실제 SKU, HW/FW, ST MCU order code 미확보로 Unknown 유지.
- 범위: CRA only. SIL 3 제외. 운영 코드, workflow, secrets, API cadence 변경 없음.

## 2026-11-23 — PR #202 병합 및 main 검증 완료

- PR #202 병합 완료: https://github.com/useformotor3/ai-discord-bot/pull/202
- squash merge SHA: `794d2d69c6a46e85d5cc64c7c0c337a7493ebcc4`
- 보고서 main read-back: v0.15, §45 및 §45.7 확인.
- 최신 매트릭스 Markdown/CSV main read-back 확인: 18개 데이터 행, CSV 21개 열, 모든 행의 열 수 일치.
- PR exact-head Run #1341 / ID `45133314471`: success. 전체 테스트·CRA traceability·공식 PDF/HTML canary·provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- main push Run #1342 / ID `45133462189`: success. 전체 테스트·CRA traceability·공식 PDF/HTML canary·provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- post-merge 복구 기준점: `safety/post-merge-pr202-2026-11-23`.
- PROJECT_LOG에는 이번 상태 갱신 이벤트를 추가한다. 제품별 분류는 LS메카피온 정확한 모델 및 ST MCU 주문 코드가 확보되기 전까지 Unknown.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, API cadence 변경 없음.

## 2026-11-23 — ETSI M/606 18개 Work Item live status 재점검

- 공식 ETSI active list 재조회: 2026-11-23 / Work Programme v2.3.3 / 18 active items.
- 통합 CRA 보고서 작업 브랜치에서 v0.14 → v0.15, §45 추가. 11월 20일 스냅샷과 구분해 11월 23일 최신 상태를 별도 기록.
- 새 매트릭스: `reports/CRA_ETSI_M606_18_ACTIVE_WORK_ITEM_MASTER_MATRIX_2026-11-23.md` 및 `.csv`. CSV는 18개 데이터 행, 20개 열, 모든 행 열 수 일치 확인.
- 중요 버전 변경: EN 304 619 V1.0.3, EN 304 635 V1.0.9. EN 304 635 상태는 EC assessment before WNV requested (2026-11-19), 다음 단계 2026-11-28로 표시.
- EN 304 617/618/620/621/622/623/625/626/627/631/632/633/634/636의 최신 active-list status 및 next-stage dates를 snapshot에 반영. EN 304 624는 11월 23일 최신 목록의 상세 행을 재확인하지 못해 이전 monitoring snapshot으로 구분.
- ETSI status milestone는 계획 단계다. 표준 채택·발행·OJ citation 또는 CRA Article 27 presumption으로 해석하지 않는다.
- 2026-11-23 GoSRSReq006-M/606 AMD 1 회의는 ETSI calendar의 일정 게시만 확인. 개최 결과·회의록·ESO 수령일/비수락 통지는 Unknown.
- PR #201 병합: merge SHA `0643c656b7801fcaf4453042e97623f2e57d73cd`. PR exact-head Run #1337 / ID `45123857980` success. Main push Run #1338 / ID `45132883785`는 마지막 확인 시점에 진행 중(공식 PDF canary 이후 단계 확인 필요).
- 복구 기준점: `safety/post-merge-pr201-2026-11-23`.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, API cadence 변경 없음.

## 2026-11-23 — PR #200 병합 및 CRA Annex III MCU 분류 정밀화

- PR #200: https://github.com/useformotor3/ai-discord-bot/pull/200 — squash merge 완료.
- merge SHA: `53d91ee5beb16f703bbaddc3ec64dd238989d55a`; exact PR head: `bced199d83a1f6ee9a9948951851d2dafb2f5740`.
- 보고서 `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` main read-back: **v0.14**, §44 확인. Annex III Class I point 14 / Class II point 4와 M/606 item 29 / 38 번호 체계, Reg. (EU) 2025/2392 MCU technical descriptions, Article 7 core-functionality/component-integration 경계를 추가.
- PR exact-head Actions Run #1331 / ID `45114851876`: success. Source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries, PDF evidence upload 및 provenance manifest upload 성공.
- post-merge safety ref: `safety/post-merge-pr200-2026-11-23` (merge SHA 기준).
- main push Actions Run #1332 / ID `45123598545`: **success**. Source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries, provenance manifest upload 모두 성공. PDF evidence upload은 변경 없음 조건으로 skipped(실패 아님).
- 제품 판정 경계: ST MCU 정확한 order code·보안 구성 및 LS메카피온 정확한 SKU/HW/FW/BOM이 확보되지 않아 MCU/완제품 Annex III 분류는 Unknown. 부품 내장만으로 완제품 분류가 자동 승계되지 않지만 완제품 CRA 기본 의무는 유지.
- ETSI GoSRSReq006-M/606 AMD 1 examination meeting은 공식 ETSI calendar에서 2026-11-23 온라인 일정으로 재확인. 일정 게시만 확인되며 회의 결과·회의록·ESO 수령일/비수락 통지는 여전히 Unknown.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, API 호출 주기 변경 없음.

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
## 2026-11-17 — 5분 간격 반복 실행 원인 및 조사 품질 개선

### 발견
- 운영 `.github/workflows/run.yml`은 `repository_dispatch: run-bot` 및 `workflow_dispatch`만 구독하고 내부 schedule이 없었다. main의 #33–#38 archive commit은 약 5분 간격으로 반복됐다. 따라서 외부 dispatcher가 반복 호출한 정황이 확인되며, 외부 서비스 설정 자체는 이 저장소에서 직접 수정할 수 없다.
- main의 기존 보고서 검사는 형식 중심이었다. 최근 6건에서 주제 중복, CRA 조항 오인용, Annex II/Annex VII 혼합, 신고 시한 혼합, EUR-Lex 링크 누락을 확인했다.

### 코드/운영 변경
- PR #10 `2e583f5c7b24743fbb1bd7d375643e314cf3115d`를 merge했다.
- main.py는 EUR-Lex Regulation (EU) 2024/2847 공식 링크가 없는 CRA 보고서를 거부한다.
- 최근 30개 archive 원문과 주제어를 비교해 중복 주제는 Discord/archive/state/history/Git 부작용 전에 no-op 처리한다.
- 프롬프트 참고 이력을 최근 5개에서 15개로 늘리고, 공식 OJ URL·직접 확인한 원문만 인용·새 주제가 없으면 억지 생성 금지를 명시했다.
- CI Run #455: 101 passed, 1 xfailed; exact blob SHA, compileall, 전체 pytest 통과.

### 법령 감사
- #33–#38 원본은 그대로 보존하고 정정 보고서 6건을 별도 작성했다.
- Article 13(8) 최소 5년/예상 사용기간이 더 짧으면 예외, Article 13(9) 업데이트 10년 또는 지원기간 잔여기간 중 더 긴 이용 가능성, Annex I Part II (2)/(7)/(8)의 취약점 처리·안전 배포·무상 업데이트를 분리했다.
- Article 14(2)(c) vulnerability final report는 조치 가용 후 14일, Article 14(4)(c) severe incident final report는 incident notification 제출 후 1개월로 정정했다.
- Annex III Class I/II에 일반 산업용 서보 드라이브가 자동 포함된다고 단정하지 않도록 정정했다.

### 다음 cadence PR
- `fix/production-cadence-2026-11-17`에서 외부 repository_dispatch trigger를 제거하고 매시간 정각 UTC schedule과 workflow_dispatch를 유지한다.
- 테스트 workflow가 run.yml PR 변경에도 실행되도록 경로 필터를 수정하고 cadence 회귀 테스트를 추가했다.
- PR CI 통과 후 main 병합. 첫 3회 hourly run에서 guard/pruning 및 데이터 참조 무결성 확인.
- 원본 state/history/archive는 이번 정정/코드 작업에서 수정하지 않았다.

## 2026-11-17 — 운영 Run #44016487535 quota 장애 분석 및 재발 방지

### 실제 실패 원인
- production Run ID `44016487535`, job `133815553121` 로그를 확인했다.
- `gemini-3.8-flash`: HTTP 429 `RESOURCE_EXHAUSTED`, Free Tier `generate_content_free_tier_requests` 일일 limit 20 초과. 응답은 약 3시간 39분 후 재시도를 제시했다.
- `gemini-3.5-flash-lite`: HTTP 503 `UNAVAILABLE`, 이후 보고서도 EUR-Lex 공식 링크 검사를 통과하지 못했다.
- 기존 main.py는 429/503을 모델별 3회 반복하고 모든 모델이 실패하면 workflow exit 1로 종료했다. 따라서 5분 외부 dispatch와 결합해 quota를 더 빨리 소진하고 실패를 반복시킬 수 있었다.

### cadence PR 보강
- 모델별 최대 시도를 2회로 낮췄다.
- 429/503은 동일 모델 재시도를 중단하고 fallback으로 이동한다.
- EUR-Lex 링크 누락 등 품질 거부는 같은 모델에 반복 요청하지 않는다.
- quota/일시 장애/품질 거부 후 유효 보고서가 없으면 경고 로그와 함께 exit 0 no-op. Discord, archive, state/history, Git 저장 부작용은 발생하지 않는다.
- 인증/설정 등 미분류 치명 오류는 exit 1을 유지한다.
- schedule을 3시간마다 UTC 정각(8회/일)으로 변경했다. 모델별 2회 시도 시 이론상 16회/일로 Free Tier 20/day 한도에 여유를 둔다.

### 검증
- PR #11 CI를 변경된 main.py/test blob SHA로 다시 실행해야 한다.
- 기존 운영 state/history/archive는 quota 실패 실행에서 변경되지 않았음을 재조회한다.
- 첫 3회 3-hourly production run을 관찰한다.
## 2026-11-17 — 운영 안정화 PR #10–#12 main 병합 완료

### PR #10 — 조사 품질 게이트
- Merge: `2e583f5c7b24743fbb1bd7d375643e314cf3115d`
- CI #455: 101 passed, 1 xfailed.
- CRA 보고서에 EUR-Lex Regulation (EU) 2024/2847 공식 링크를 필수화하고, 최근 30개 archive 원문과 주제어를 비교해 중복 주제를 전송/저장 전에 차단.

### PR #11 — quota 및 5분 반복 실행 원인 차단
- Merge: `21c6add0c58de39fbc2755882885bffe2cd44394`
- CI #467: 103 passed, 1 xfailed.
- Production run #44016487535/job #133815553121 로그에서 Gemini Free Tier 20 requests/day 초과(429), fallback 503, EUR-Lex 링크 누락을 확인.
- 외부 repository_dispatch 구독 제거, 내부 schedule을 3시간 간격(`0 */3 * * *`)으로 변경. 모델별 최대 2회, 429/503 즉시 fallback, quota/품질 거부 시 no-op.

### PR #12 — 실패 경로 복구 및 외부 전송 순서
- Merge: `bef260a29481320de3eae9cafe4a6f907e38ead0`
- CI #470: 105 passed, 1 xfailed.
- workflow는 pre-run checkpoint가 생성된 뒤 main.py가 실패해도 operational guard를 실행한다.
- uncommitted operational data는 checkpoint에서 복원하고, remote main이 baseline이면 unpublished local data commit을 local reset으로 복구한다. remote가 전진한 경우 force-push/덮어쓰기를 거부한다.
- checkpoint pruning은 guard 성공 후에만 실행한다.
- main.py는 archive/state/history를 GitHub에 commit/push한 뒤 Discord 전송한다. Git 저장 실패 시 Discord 메시지를 보내지 않는다.

### 데이터 무결성
- quota 실패 run #44016487535 이후 state.json SHA `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, history.json SHA `b9ea42fa437b2b3a5728db5d125d287fb746b46b` 및 count=38/2,431 entries가 유지됨.
- 원본 archive #33–#38은 그대로 보존하고 correction reports #33–#38을 별도 추가.
- 운영 실제 runtime 검증은 첫 3회 3-hourly run에서 진행한다. 현재까지 PR CI는 mock 기반이므로 실제 Gemini/Discord 전송 성공을 보장한다고 표현하지 않는다.

## 2026-11-17 — CRA archive #22–#32 감사 및 #1–#38 정정 인덱스

- main의 2026-11-17 archive #22–#32 원문 11건을 직접 fetch해 전체 내용과 blob SHA를 확인했다.
- #22: secure-by-default broad requirement는 존재하지만 default credential을 특정 방식으로 바꾸라는 원문 인용은 final OJ에서 확인되지 않음.
- #23: 기술문서는 Article 31/Annex VII, 보존은 Article 13(13); Annex VI 오인용 및 서보 드라이브 Class I/II 자동 분류를 정정.
- #24: 사용자 정보/지침은 Article 13(18)/Annex II이며 Article 24는 open-source software stewards 조항.
- #25–#28: Article 10 제조사 의무 오인용, CVD 정책(Annex I Part II (5)), contact address ((6)), Article 13(17) single point of contact, Article14/15 mandatory/voluntary reporting 혼합, PGP/security.txt/CVE/SLA의 직접 의무 과장을 정정.
- #29: security logging은 Annex I Part I (2)(l), integrity는 (2)(f), CVD는 Part II (5)/(6)으로 분리. Immutable log retention/WORM/SIEM은 구현 선택.
- #30–#32: Article 13(8) support period, Article13(9) update availability, Annex I Part II (2)/(7)/(8) vulnerability remediation/secure distribution/free updates 및 tailor-made product/business user 예외를 정정.
- 정정 #22–#32 11건 작성. 기존 integration branch의 정정 #5–#21도 main 통합 후보 branch로 복사.
- CRA 정정 #1–#38 master index 작성. 원본 archive는 수정/삭제하지 않았다.
- 공식 기준: EUR-Lex Regulation (EU) 2024/2847 OJ https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

## 2026-11-17 — PR #14 병합 및 CRA 정정 #1–#38 main 검증

- PR #14 merge commit `6994e4828a03482713f7990c7f82036bacfe4772`; CI Run #474: 105 passed, 1 xfailed.
- main에서 correction report #1–#38을 개별 fetch해 모두 존재함을 확인.
- #22–#32 original archive blob SHA 11개를 다시 조회해 기존과 일치함을 확인. #33–#38 원본도 보존.
- state.json SHA `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, history.json SHA `b9ea42fa437b2b3a5728db5d125d287fb746b46b` 유지; count=38, entries=2,431.
- master index `reports/CRA_CORRECTION_INDEX_2026-11-17.md` main 반영.
- 이전 Draft PR #3/#6은 후속 PR #10–#14가 해당 기능/자료를 main에 통합했으므로 close. correction #5–#21은 main에 보존.
- 다음 실무 우선순위: 정정된 법적 근거를 한국어 CRA 통합 보고서/traceability matrix에 반영하고, 이후 SIL 3 servo-drive benchmarking report와 hardware block design을 작성.

## 2026-11-17 — SIL 3 서보 드라이브 벤치마킹 및 하드웨어 설계 초안

### 조사 표준
- IEC 61800-5-2:2016+AMD1:2026 CSV Ed.2.1(2026-10-30 발행)을 현재 제품 안전 서브기능 기준으로 반영.
- IEC 62061:2021+AMD1:2024+AMD2:2026 CSV Ed.2.2(2026-03-20), ISO 13849-1:2023 반영.
- IEC 61508-1:2010 Ed.2는 현재 유효. IEC 61508-1:2026 Ed.3 PRV는 FDIS 투표가 2026-11-13 종료됐지만 최종 발행 전(예정 2027-01-22)이므로 규범 기준으로 사용하지 않는다.
- IEC 61800-5-2 AMD1:2026은 시험/파라미터/EMC/열/기계 내성/피드백 관련 내용을 갱신하고 PDS(SR) proof-test 용어/개념을 삭제했다. 2016판 제조사 매뉴얼의 proof-test interval을 최신 규격 요구로 자동 적용하지 않도록 주의사항 추가.

### 제조사 벤치마킹
- Mitsubishi MELSERVO-J5: 모델별 STO/SS1/SS2/SOS/SBC/SLS/SSM/SDI/SLI/SLT, PFH 및 encoder/test-pulse 조건 차이 확인. 일부 기능은 SIL2/PLd.
- Yaskawa Sigma-7 ASM7: OSB01A/OSB02A, FSoE/physical I/O, 최대 16개 기능, module PFH와 전체 drive PFH 범위 차이, encoder configuration dependency 확인.
- Rockwell Kinetix 5700 ERS4: drive-based Monitored/Timed SS1, 일부 motion monitoring SIL3/PLe, position-based functions 일부 SIL2/PLd, dual feedback 필요성 및 PFH 범위 확인.
- Siemens S210: 2025 Safety Manufacturer Declaration 기준 SIL3/PLe, Basic/Extended 및 Cat3/Cat4 구분, runtime license 조건 및 2026 amendment 재확인 필요.
- PFH 수치는 component scope가 달라 단순 제조사 순위로 사용하지 않음.

### 생성 문서
- `reports/SIL3_SERVO_DRIVE_BENCHMARK_REPORT_2026-11-17.md`
- `design/SIL3_SERVO_DRIVE_HARDWARE_BLOCK_DESIGN_2026-11-17.md`
- `reports/SIL3_SERVO_DRIVE_REQUIREMENTS_TRACEABILITY_2026-11-17.md`

### 제한
- 1축 기준 reference architecture이며 전압/출력/부하/엔코더/네트워크/안전 기능 범위가 미확정.
- 제조사별 2026-10-30 IEC 61800-5-2 amendment 적용 인증서와 최신 firmware 범위를 직접 확인하지 않았다.
- 최종 회로도/BOM/PFH 계산은 정격/부하/위험평가가 확정된 후 수행한다.

- Rockwell Product Safety Advisory PSA 2017-01-001 추가 대조: 2198-S* ERS3 V7.001 이하 및 2198-D* ERS3 V7.002 이하의 hardwired STO 구성은 공표 SIL PFH 미달 가능. 수정 firmware V7.003 이상. Integrated network STO는 해당 공지의 영향 범위 밖. 설치 firmware 확인이 필요하며 ERS4에 일반화하지 않는다.

## 2026-11-17 — SIL 3 servo-drive report PR #16 merged

- Merge commit `34449753857c6ab004271f69aac19867a7aed1fa`; CI #488: 105 passed, 1 xfailed.
- Main files:
  - `reports/SIL3_SERVO_DRIVE_BENCHMARK_REPORT_2026-11-17.md`
  - `design/SIL3_SERVO_DRIVE_HARDWARE_BLOCK_DESIGN_2026-11-17.md`
  - `reports/SIL3_SERVO_DRIVE_REQUIREMENTS_TRACEABILITY_2026-11-17.md`
  - `reports/SIL3_SERVO_DRIVE_BENCHMARK_MATRIX_2026-11-17.csv`
- Benchmark includes Mitsubishi J5, Yaskawa Sigma-7 ASM7, Rockwell Kinetix 5700 ERS4 and Siemens S210. Rockwell ERS3 hardwired STO PSA 2017-01-001 is called out separately.
- Standard revisions current as of 2026-11-17, including IEC 61800-5-2 AMD1:2026 and IEC 62061 AMD2:2026.
- Deliverable is a reference architecture, not a final certified design. Exact ratings, load, encoder, network, safety functions and manufacturer 2026 amendment certificates remain open.


## 2026-11-17 — 프로젝트 범위 정정 및 CRA-only 재개 기준 확정

- 저장소의 README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG를 main에서 다시 읽어 상호 대조했다.
- 확인 결과 CRA가 프로젝트의 저장소 목적이지만, README 하단·상황판·마스터 계획·세션 로그·기계 로그에 SIL 3를 CRA 후속 작업처럼 적은 충돌이 존재했다.
- PR #16과 SIL 3 산출물은 main에 실제 반영된 과거 작업이다. 이를 삭제하거나 사용자 입력 실수로 단정하지 않는다. 현재 활성 범위는 CRA만이며, SIL 3는 명시적 별도 재개 지시 전 비활성으로 취급한다.
- 범위 정정은 작업 브랜치 `docs/cra-scope-governance-2026-11-17`에서 수행한다. 운영 코드, workflow, state/history, 원본 archive 및 기존 SIL 3 산출물은 변경하지 않는다.
- README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK 및 PROJECT_LOG의 범위 문구를 동기화한다. 본 기록은 범위 정정 사실과 이후 재개 순서를 보존한다.
- 검증 한계: 이 변경은 문서 거버넌스 정정이다. CRA 법적 적합성 평가나 제품 적합성 결론을 새로 내리지 않는다.


## 2026-11-17 — CRA-only 범위 통제 PR #18 병합

- PR #18 `Set CRA as the sole active project scope`를 main에 병합했다.
- Merge commit: `b7813ddd311bc51bfb0eb26458eace9ff82b621f`.
- 변경 파일: README.md, PROJECT_STATUS.md, MASTER_PLAN.md, AI_RULEBOOK.md, SESSION_LOG.md, PROJECT_LOG.jsonl (문서 6개만).
- PR merge 시 충돌 없음(`mergeable=true`). 운영 코드/workflow/state/history/original archive 및 SIL 3 산출물은 변경하지 않았다.
- SIL 3 산출물 4개 파일을 main에서 재조회해 모두 존재함을 확인했다. PR #16 및 기존 merge commit 이력도 유지.
- PROJECT_LOG.jsonl은 58개 record 모두 JSON 파싱 성공.
- CI 상태: merge commit의 combined status에 등록된 status check가 없고, PR-triggered workflow 조회도 비어 있었다. 따라서 이번 문서 PR의 CI 통과를 주장하지 않는다. 문서 범위 diff와 JSONL 구문 검증만 확인했다.
- 다음 재개: CRA만 활성 범위로 유지한다. 운영 3시간 주기 첫 3회 관찰 상태를 최신 Actions에서 확인한 뒤 CRA 통합 한국어 보고서와 CRA 요구사항 추적표를 진행한다.


## 2026-11-17 — CRA 통합 보고서/요구사항 추적표 v0.1 작성

- 활성 범위 CRA-only 통제(PR #18 merge commit `b7813ddd311bc51bfb0eb26458eace9ff82b621f`) 이후, 최신 `main`에서 `cra/integrated-report-and-traceability-2026-11-17` 작업 브랜치를 생성했다.
- `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` 초안과 `reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv` 28항목을 작성했다.
- 기존 CRA 정정 인덱스 #1–#38과 운영 실행 관찰 보고서를 읽고, 기존 정정 내용과 중복/충돌을 줄이는 방향으로 통합했다.
- 최신 공식 자료 교차 확인: CRA OJ Regulation (EU) 2024/2847; Commission Guidance C(2026) 5252 final (2026-07-27); Commission Implementing Decision C(2026) 7861 final Annex (2026-11-10); Regulation (EU) 2025/327 Article 104/105; Commission CRA implementation/FAQ/standardisation/reporting pages; ENISA SRP FAQ (updated 2026-10-15).
- 중요 확인: 일반 서보 드라이브 카테고리는 Annex III/IV에 직접 열거되지 않는다. 디지털 데이터 연결과 제품 핵심 기능을 기준으로 제품별 판단이 필요하며, 통신 포트/일반 MCU 존재만으로 Class I/II를 단정하지 않는다.
- CRA Article 14 신고 의무는 2026-09-11부터 이미 적용 중이며, 2027-12-11 이전 출시 제품도 포함된다. 지원기간 종료 후에도 신고 의무는 지속될 수 있다는 Commission Guidance 해석을 보고서에 반영했다.
- M/606 개정 기한을 공식 C(2026) 7861 Annex와 Commission standardisation page에서 확인했다: 항목 1/15 2026-11-30, 항목 16–41 2027-01-31, 항목 2–14 2027-10-30. 표준 납품 일정과 CRA 적용일을 구분했다.
- Regulation (EU) 2025/327의 CRA 개정은 Article 12 고위험 AI 제품 및 Article 32(5a) EHR 시스템에 한정된 특례이며 2027-03-26 적용이다. 일반 서보 드라이브에 자동 확장하지 않는다.
- ENISA SRP FAQ(2026-10-15)를 확인해 초기 플랫폼의 영어 UI 및 API 미제공 상태를 운영 참고사항으로 기록했다.
- 제품 모델, 통신 프로토콜, 공급 구조, cloud/RDPS 및 제품별 설계 증거가 제공되지 않아 적용성/분류 결론은 잠정 상태로 유지한다.
- 운영 코드, workflow, state/history, 원본 archive 및 SIL 3 산출물은 변경하지 않았다.
- 다음: 제품별 사실 자료 확보, Annex III/IV 분류, 28항목의 설계·시험 증거 연결, CSV/JSONL/링크/diff 검증 후 PR 생성. CI 결과가 확인되지 않으면 통과로 기록하지 않는다.


## 2026-11-17 — CRA 통합 보고서 PR #19 및 CI 시작

- PR #19 생성: https://github.com/useformotor3/ai-discord-bot/pull/19
- 작업 브랜치 `cra/integrated-report-and-traceability-2026-11-17` → `main`; 변경 경로 9개, 16 commits ahead / 0 behind, merge-base 동일.
- GitHub Actions isolated test workflow Run #500 (`44028473103`)이 PR 생성 후 시작됨. 첫 job의 source blob identity 검사는 성공했으며 dependency 설치 단계 진행 중; 전체 compile/pytest 결과는 미확정.
- PR 생성 시 GitHub가 `mergeable=false`를 반환했으므로 아직 병합하지 않는다. CI 완료와 mergeability 재조회 후 진행한다.


## 2026-11-17 — PR #19 병합 및 CI 재검증 완료

- PR #19를 squash merge 완료. Merge commit: `5776ca609130033bfff17ca62c9fabc3b9570b3b`.
- PR-triggered isolated test workflow Run #500 (`44028473103`) success: source blob identity, dependency installation, compileall, 전체 repository pytest 단계 모두 success.
- main push workflow Run #502 (`44028536971`)도 success: 동일한 source integrity/compile/pytest 단계 완료.
- 병합 후 main에서 README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG, 통합 보고서, CSV 추적표, correction index를 재조회했다.
- PROJECT_LOG.jsonl 61개 record 모두 JSON 파싱 성공. CSV 추적표 28개 요구사항 행 존재 확인.
- SIL 3 벤치마킹 보고서와 하드웨어 설계 파일이 main에 계속 존재함을 재확인. 과거 산출물/PR #16 이력은 수정하지 않았다.
- PR #19 변경은 문서 9개 경로에 한정되며 운영 코드, workflow, state/history, archive 변경 없음.
- 다음 작업은 제품별 통신/데이터 흐름·시장 공급·원격 처리 사실을 확인하고 28항목을 설계/시험 증거에 연결하는 것이다.


## 2026-11-17 — PR #19 이후 다음 재개 지점 정리

- PR #19 및 두 CI run 성공 이후, 다음 작업을 제품별 적용성 및 28개 요구사항의 설계/시험 증거 연결로 고정했다.
- 순서: (1) 제품군 통신/데이터 흐름/필수 소프트웨어/RDPS/시장 공급 구조, (2) Annex III/IV 핵심 기능 분류와 Article 32 경로, (3) 28항목 통제·시험 증거 연결, (4) CRA 보안 아키텍처 및 구현·검증 매뉴얼, (5) 통합 보고서 v0.2.
- 특정 모델 정보가 없으므로 제품별 법적 결론은 계속 잠정으로 둔다. 이 제한을 해소하기 전에도 일반 서보 드라이브 공통 요구사항·검증 설계는 계속 진행할 수 있다.


## 2026-11-17 — 서보 드라이브 인터페이스 CRA 적용성 매트릭스 작성

- `reports/CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv` 신규 작성: 15개 인터페이스/기능 유형을 데이터 연결 기준으로 분류했다.
- EtherCAT/PROFINET/EtherNet-IP/Modbus TCP/CANopen/RS-485+Modbus/USB/serial/무선은 디지털 데이터 교환 가능성이 높다고 구분했다.
- 아날로그 ±10V/4–20mA, 단순 24V DI/DO, STO 하드와이어드 신호는 단순 전기 신호/trigger인지, 정의된 디지털 정보가 인코딩되어 수신 측에서 해독되는지 구분하도록 했다.
- Encoder feedback, vendor PC tool, cloud/RDPS는 제품 경계·기능·데이터 인코딩·필수성에 따라 조건부로 분류했다.
- 근거는 Commission Guidance C(2026) 5252 §2.2, §2.4, §2.5, §2.6, §8 및 CRA Article 2/3에 연결했다. 공식 URL을 CSV 각 행에 포함했다.
- 실제 모델 회로/프로토콜/설명서가 없으므로 15개 행 모두 제품별 미확인으로 표시했다. 이 매트릭스는 일반적 분류 도구이지 모델별 판정이 아니다.


## 2026-11-17 — 인터페이스 적용성 매트릭스 PR #20 병합

- PR #20 `Add servo drive interface-level CRA applicability matrix` squash merge 완료.
- Merge commit: `951fc5ee0122b847b5e8f77bd5e0706db65efb76`.
- 변경 경로 8개: 인터페이스 매트릭스 CSV 신규, 통합 보고서/인덱스/README/상황판/마스터 계획/세션 로그/기계 로그 갱신.
- 병합 전 compare: 9 commits ahead / 0 behind, merge-base 동일. CSV 15행·9열·ID unique·모든 행에 EUR-Lex 및 Commission Guidance URL 확인.
- 병합 후 main에서 매트릭스 CSV 15행, 통합 보고서, 추적표 28행, README/상황판/마스터 계획/세션 로그/PROJECT_LOG 및 SIL 3 역사적 산출물 존재 확인.
- PROJECT_LOG.jsonl 64개 record는 병합 전 JSON 파싱 성공.
- PR #20에 대한 PR-triggered 또는 merge commit Actions run은 조회 시점에 확인되지 않았다. 따라서 CI 통과를 주장하지 않는다. CSV 구조/ID/공식 URL 및 JSONL 구문 수동 검증만 확인했다.
- 운영 코드, workflow, state/history, archive, SIL 3 파일은 변경하지 않았다.
- 다음: 실제 서보 드라이브 제품군의 데이터시트/통신 매뉴얼/회로도에 따라 15개 인터페이스 잠정 분류를 확정하고, 28개 CRA 요구사항과 설계·시험 증거를 연결한다.


## 2026-11-17 — CRA 정정 보고서 #1–#38 통합 검토 및 보고서 v0.2 보강

- 인덱스에 연결된 CRA correction reports #1–#38 개별 파일 38개 모두 fetch/read 가능함을 확인하고, 각 보고서의 주요 오류 유형·법적 locator·핵심 정정 사항을 추출해 상호 대조했다.
- 통합 보고서 §11에 반복 오류와 정확한 최종 OJ locator를 통합했다: Article 10/11/13/14/15/16 역할, Annex I Part I vs Part II, Part I (2)(a)–(m), Part II (1)–(8), Article 13(8)/(9), SBOM 최소 범위, Annex II vs Annex VII, 신고 시한, 제품 core functionality 분류.
- 엔지니어링 권고와 CRA 직접 의무를 분리했다. least privilege/RBAC/MFA/unique credentials/digital signatures/immutable logs/resource isolation/automatic rollback/STO/SS1 등을 CRA의 보편적 직접 의무로 표현하지 않는다.
- #4 정정 내용에 따라 NIST SP 800-88 Rev.1은 2025-09-26 철회, Rev.2가 현행임을 NIST 공식 페이지에서 재확인하고, CRA 법령이 아닌 기술 참고자료로 구분했다.
- 보고서 v0.2에 Article 2(2)–(7) 명시적 제외, Article 13(14)–(23) 추가 제조사 의무, Article 15 자발적 신고, Article 18–23 EU 경제운영자 책임을 보강했다.
- 요구사항 추적표를 28개에서 35개로 확장하고 각 행에 공식 근거 URL을 유지했다.
- 다음: CSV 35행 파싱/ID 중복/URL 검증, 보고서와 38개 정정 보고서 간 locators 교차 점검, PR/CI 검증.


## 2026-11-17 — CRA 보고서 v0.2 및 35항목 추적표 PR #21 병합

- PR #21을 squash merge 완료. Merge commit `e11d376bab43ccc99bdf70549ad47eec57a01760`.
- PR #21 Actions Run #517 (`44029412739`) success. 단, Run #517은 최종 2개 문서 수정(Article 32 절차 상세화 및 CRA-020 추적행 보강) 이전 커밋 `24984c447387cfad52d01d3b829b293ff2ecf8e5`에서 실행되었다.
- 최종 head `f90bf728a0261aae9446c660676402b040d1812f` 및 merge commit에 대한 추가 workflow run/status는 조회 시점에 확인되지 않았다. 따라서 최종 변경 전체에 대한 CI success로 확대 주장하지 않는다.
- 최종 CSV는 35 data rows, 8 columns, unique IDs, uniform columns, 각 행에 EUR-Lex URL 포함을 재검증했다. PROJECT_LOG.jsonl 66 records parse success.
- 보고서 v0.2에 Article 2(2)-(7) exclusions, Article 13(14)-(23), Article 15 voluntary reporting, Articles 18-23 economic operator duties, Annex I Part I (2)(a)-(m), Article 32(1)-(4) conformity routes, #1–#38 correction synthesis를 반영했다.
- PR #21은 문서만 변경했으며 운영 코드/workflow/state/history/archive/SIL3 파일 변경 없음.
- 다음 단계는 제품별 인터페이스 사실을 확인하고, 35개 요구사항 및 15개 인터페이스 항목을 보안 통제·시험 케이스·증거에 연결하는 것이다.


## 2026-11-17 — CRA 보안 통제·시험 매트릭스 36항목 작성

- `reports/CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv` 신규 작성: CRA 법적 근거, 공식 URL, 통제 목표, 위험 시나리오, 구현 후보, 시험 방법, 증거, 적용성, 상태를 포함한 36항목.
- Annex I Part I (1), (2)(a)-(m)와 Part II (1)-(8), Articles 13-15, 18-23, 31-32, 69 및 RDPS/인터페이스 적용성에 연결했다.
- MFA/RBAC/고유 비밀번호/디지털 서명/immutable logs/resource isolation/STO/SS1 등은 CRA의 일률적 직접 구현 명령이 아니라 위험기반 구현 후보로 구분했다.
- 각 행에 EUR-Lex CRA 원문과 Commission Guidance 공식 URL을 포함했다.
- 상태는 모두 미작성/증거 미확인으로 유지했다. 제품 모델·회로·펌웨어·프로토콜이 없는 상태에서 구현 또는 시험 완료를 주장하지 않는다.
- 다음: CSV 36행/10열 파싱, ID unique, 공식 URL 확인 후 PR; 이후 모델별 설계/시험 증거로 갱신.


## 2026-11-17 — 보안 통제·시험 매트릭스와 요구사항 추적 ID 연결

- 36개 SEC 통제/시험 행에 CRA-001~CRA-035 요구사항 ID를 직접 연결했다.
- CSV 최종 구조: 36 data rows × 11 columns, 법적 근거 URL, 관련 CRA requirement IDs, 통제 목표, 위험 시나리오, 구현 후보, 검증/시험, 증거, 잠정 적용성, 상태.
- 구현 후보는 CRA가 특정 기술을 보편적으로 강제한다는 의미가 아니라 위험기반 설계 선택지임을 명시했다.


## 2026-11-17 — CRA 보안 통제·시험 매트릭스 PR #22 병합

- PR #22 squash merge 완료. Merge commit `20e503c1da2fe2f053630263a8c4942680ec1515`.
- Actions Run #525 (`44029944407`) success: source blob identity, dependency install, compileall, complete repository pytest all success on PR head `697157b52023cc96d47e6d6b60b8551863597221`.
- Merge commit 자체에 대한 추가 workflow/status는 조회 시점에 확인되지 않았으므로 PR Run #525 결과만 기록한다.
- 36개 SEC control/test row × 11 columns, unique SEC IDs, each row has official EUR-Lex + Commission Guidance URLs, each row maps to one or more CRA-001..CRA-035 requirement IDs (unmapped=0).
- 모든 행의 상태는 미작성/증거 미확인이다. 실제 제품 구현/시험이 수행되었다고 주장하지 않는다.
- PR #22는 문서/CSV 8개 경로만 변경. 운영 코드/workflow/state/history/archive/SIL3 산출물 변경 없음.
- 다음: 일반 reference security architecture를 작성하되 제품별 MCU/네트워크/저장장치/원격 처리 구성은 미확인으로 분리하고, 각 SEC 항목을 실제 회로/펌웨어/시험 결과에 연결한다.


## 2026-11-17 — CRA 참조 보안 아키텍처 v0.1 작성

- `reports/CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md` 신규 작성: 논리 블록, trust boundary, data flow, HW/boot, firmware, communication, NVM/key store, optional RDPS, manufacturer operations 구조를 정리했다.
- Mermaid block diagram source 포함. 실제 회로/MCU/fieldbus/flash/cloud 구성은 미제공이므로 모든 블록은 reference option이며 제품별 구현 완료로 간주하지 않는다.
- 36개 SEC control/test matrix, 35개 CRA requirements matrix, 15개 interface applicability matrix와 링크했다.
- secure boot, secure element, signed update, debug lock, rate limiting, RBAC/MFA 등은 위험기반 구현 후보로 분류. CRA가 특정 기술을 일률 의무화한다고 표현하지 않았다.
- STO/SS1 등 기능안전 동작은 CRA 자동 요구사항에서 제외하고 별도 hazard/safety analysis 대상으로 유지했다.


## 2026-11-17 — CRA 참조 보안 아키텍처 PR #23 병합

- PR #23 squash merge 완료. Merge commit `b90a0ac07865c18d846323d843fef38b1123077a`.
- Actions Run #531 (`44030343837`) success: source blob identity, dependency install, compileall, complete repository pytest all success on PR head `9886b12aa140f0853487df3d5aa2f00af0fc5578`.
- Merge commit 자체의 추가 workflow/status는 조회 시점에 확인되지 않았다. PR Run #531 결과만 기록한다.
- `reports/CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md` main readback 완료; Mermaid block diagram, 6개 trust boundary, 10개 주요 block, 35 requirement/15 interface/36 SEC matrix 연결 확인.
- PR #23은 문서 8개 경로만 변경; 운영 코드/workflow/state/history/archive/SIL3 산출물 변경 없음.
- 다음: 실제 제품 모델/회로/MCU/프로토콜/업데이트 경로를 확인하고 참조 아키텍처를 제품별 설계로 구체화한다. 정보가 없으면 generic design/test cases를 계속 축적하되 모델별 결론으로 표현하지 않는다.


## 2026-11-17 — branch reconciliation report 및 통합 규칙 보강

- `reports/BRANCH_RECONCILIATION_2026-11-17.md` 작성. main canonical, divergent branch ahead/behind, merge-base, unique content, PR #3/#10-#14 상태를 기록했다.
- PROJECT_STATUS Section 0에 현재 branch authority를 추가하고 2026-11-14의 72/50 스냅샷은 historical로 격하했다.
- AI_RULEBOOK Section 48에 selective integration, main.py 보호 동작, exact paragraph/point quote scope, source host allowlist, no live Gemini/Discord canary 원칙을 추가했다.
- MASTER_PLAN에 source provenance gate 통합을 P0로 지정했다.
- 기능안전/SIL 관련 AI_RULEBOOK Sections 46-47은 historical reference only로 표시. 현재 활성 범위는 CRA-only이며 사용자 명시 재개 전에는 SIL 작업을 시작하지 않는다.


## 2026-11-17 — 브랜치 정합성 감사 PR #24 병합

- PR #24 squash merge 완료. Merge commit `153033aa535775a0df568ad83876bff487d33404`.
- Actions Run #540 (`44031831729`) success: source blob identity, dependency installation, compileall, complete repository pytest all success on PR head `a661fe4604f3127b88ab20a48e04fd7f20779737`.
- merge commit 자체의 별도 workflow run은 확인되지 않았다. PR Run #540 결과만 기록한다.
- PROJECT_STATUS/AI_RULEBOOK/MASTER_PLAN/README/SESSION_LOG/PROJECT_LOG에 branch authority와 source-gate 통합 순서를 반영했다.
- main을 canonical로 유지하고, diverged branches 전체 병합 금지. 다음 작업은 최신 main에서 source provenance gate를 선택 이식하는 것.


## 2026-11-17 — CRA 공식 source provenance / claim validator 통합 및 PR #26 병합

### 작업 시작 기준
- canonical base: `main` @ `f4bb159e164b00e4586868f335519cea3c4802ae`.
- 작업 목적: PR #24에서 남긴 source/claim gate 통합 계획을 최신 main의 보호 동작을 유지하면서 구현·검증한다.
- 활성 범위는 CRA만이다. SIL 3 과거 파일/PR/커밋은 수정하거나 삭제하지 않는다.

### 구현 및 검증 과정
1. `cra_source.py` / `cra_claims.py`와 main.py source gate를 선택 통합하고 source/claim regression tests를 추가했다.
2. 첫 CI에서 107 passed / 27 failed가 발생했다. 주요 원인은 typed source exception과 테스트 fixture의 claim ID/JSON 계약 불일치, manifest 추가 후 Discord 메시지 chunk 수 변화였다. 테스트를 느슨하게 하지 않고 운영 코드/fixture를 정합화했다.
3. 다음 검증에서 134 passed / 1 xfailed까지 개선했으나 live EUR-Lex canary가 HTTP 202/빈 응답/자동화 접근 차단을 발견했다. 202 응답을 정상 원문으로 취급하지 않고 temporary unavailable로 분류했다.
4. EUR-Lex HTML 직접 호출 대신 Publications Office의 공식 CELLAR REST API를 실험 브랜치에서 검증했다. CELLAR는 일부 CELEX URL을 HTTP로 redirect했으므로 동일 allowlist host 확인 후 HTTPS로 승격하는 redirect handler를 추가했다.
5. Corrigendum CELEX suffix의 URL encoding 문제를 수정하고, Formex 원문에서 번호와 문장이 서로 다른 줄/블록으로 나뉘는 문제를 whitespace-normalized marker matching으로 해결했다.
6. 실시간 canary에서 CRA 법령·정오표·위임규정 7건과 Commission 공식 페이지 2건, 총 9개 source fetch를 확인했다. Article 13(8) paragraph locator 안에서 기대 원문 quote가 일치하는지도 live 확인했다.
7. 최종 PR head `d1bda523c1b593bbd48bf4916dd7bbd741001894`의 [Actions Run #573](https://github.com/useformotor3/ai-discord-bot/actions/runs/44039961078)은 **138 passed, 1 xfailed**. source blob identity, compileall, 전체 pytest, 9-source canary, Article 13(8) locator/quote canary 모두 통과했다.

### 변경 및 병합
- PR #26 [CRA: integrate CELLAR official-source retrieval and claim-level traceability](https://github.com/useformotor3/ai-discord-bot/pull/26) merge 완료.
- Merge commit: `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`.
- 변경 파일: `.github/workflows/tests.yml`, `cra_source.py`, `cra_claims.py`, `main.py`, `tests/conftest.py`, `tests/test_main_characterization.py`, `tests/test_cra_source.py`, `tests/test_cra_claims.py`, `tests/test_external_failure_paths.py`.
- PR #25는 PR #26에 전체 변경이 포함되어 중복 정리했다. 원래 branch는 감사/복구를 위해 유지했다.
- pre-merge safety ref: `safety/pre-merge-main-pr26-2026-11-17` → `f4bb159e164b00e4586868f335519cea3c4802ae`.
- post-merge safety ref: `safety/post-merge-main-pr26-2026-11-17` → `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`. 두 ref 모두 GitHub에서 재조회해 SHA 일치 확인했다.

### 결과 해석 및 제한
- source manifest에는 요청/최종 URL, retrieval timestamp, visible text length, full-text SHA-256, prompt-excerpt SHA-256을 기록한다.
- claim validator는 본문 claim ID/statement, source ID, exact quote, Article paragraph/Annex Part-point locator의 일치 여부를 검증한다. 법률 해석이나 제품별 적합성 자체를 자동 확정하지 않는다.
- Commission Guidance C(2026) 5252 PDF/Annex와 M/606 C(2026) 7861 decision Annex는 관련 URL만 manifest에 기록했다. 실제 PDF/decision Annex 원문 다운로드·파싱은 미완료다.
- 제품 모델/회로/펌웨어/프로토콜/EU 공급 구조가 없어 모델별 CRA 적용성·Annex III/IV 분류·Article 32 경로는 잠정이다.
- PR head CI는 성공했으나 merge commit 자체의 별도 Actions run은 아직 확인되지 않았다.
- 운영 Gemini/Discord workflow는 실행하지 않았으며 state.json/history.json/research_archive 데이터는 변경하지 않았다.

### 관련 보고서와 다음 재개
- [CRA source provenance pipeline 설계·검증 보고서](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md)
- 다음: (1) Guidance PDF/Annex 및 M/606 decision Annex 수집·해시·페이지 locator, (2) Article 13(8) 외 Annex I/핵심 Article live canary 확대, (3) 35 requirements/15 interfaces/36 SEC controls를 claim IDs·설계 통제·시험·제품 증거와 연결, (4) merge commit CI 확인.


## 2026-11-17 — 프로젝트 상황판·행동강령·재개 기록 PR #27 병합

- PR #27 [docs: synchronize CRA source provenance status, rules and resume point](https://github.com/useformotor3/ai-discord-bot/pull/27) merge 완료.
- Merge commit: `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`.
- [Actions Run #575](https://github.com/useformotor3/ai-discord-bot/actions/runs/44040949610): 138 passed / 1 xfailed, 9개 official source live fetch 및 Article 13(8) locator/quote canary 성공.
- README/PROJECT_STATUS/MASTER_PLAN의 현재 상태와 다음 재개 순서를 갱신하고, AI_RULEBOOK에 CELLAR source/claim validation 규칙과 반복 승인 없는 가역 작업 권한을 반영했다.
- SESSION_LOG와 PROJECT_LOG.jsonl에 PR #26 구현·검증·실패 수정 과정과 PR #27 병합 결과를 추가했다.
- JSONL 76개 record 전체 parse 성공, source excerpt SHA-256 9개 각각 64 hex 확인.
- PR #27 pre-merge checkpoint: `safety/pre-merge-main-pr27-2026-11-17` → `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`.
- PR #27 post-merge checkpoint: `safety/post-merge-main-pr27-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`. 두 ref readback SHA 검증 완료.
- merge commit 자체의 별도 Actions run은 확인되지 않았다. PR head Run #575 결과만 검증 증거로 기록한다.
- 운영 Gemini/Discord workflow와 외부 전송은 실행하지 않았다. state/history/archive 및 SIL 3 과거 산출물도 변경하지 않았다.
- 다음 작업: Guidance PDF/Annex 및 M/606 decision Annex 원문 수집, Article/Annex live locator canary 확대, 요구사항/인터페이스/SEC 통제의 source claim·제품 증거 연결.


## 2026-11-17 — PR #28 복구 체크포인트 동기화 및 최종 main 상태 반영

- PR #28 [docs: finalize PR27 rollback checkpoints and project readback](https://github.com/useformotor3/ai-discord-bot/pull/28) merge 완료.
- Merge commit: `942e1e6b5f2887001279a96c21f94138d283a689`.
- [Actions Run #577](https://github.com/useformotor3/ai-discord-bot/actions/runs/44041626911): 138 passed / 1 xfailed, 9개 official source live fetch 및 Article 13(8) locator/quote canary 통과.
- PR #28 pre-merge ref `safety/pre-merge-main-pr28-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; post-merge ref `safety/post-merge-main-pr28-2026-11-17` → `942e1e6b5f2887001279a96c21f94138d283a689`. 두 ref를 재조회해 SHA 일치 확인.
- README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK에 PR #28 merge SHA와 복구 refs를 반영했다.
- merge commit 자체의 별도 Actions run은 확인되지 않아 PR head Run #577만 검증 증거로 기록한다.
- 운영 코드/workflow/state/history/archive 변경, 운영 Gemini/Discord 실행 및 외부 전송은 없었다.


## 2026-11-17 — Commission Guidance C(2026) 5252 및 M/606 C(2026) 7861 Annex 1차 감사

- main 최신 HEAD `80245d9e132380a10581612c031f87869993b98d`를 확인했다. PR #29 post-merge safety checkpoint `9c16724b8b72bd09d3492b19ff714602b235c66b` 대비 main은 README/PROJECT_STATUS/source provenance report 문서 전용 3개 커밋 ahead, 0 behind였다.
- `cra/official-annex-audit-2026-11-17`를 main HEAD에서 생성하고 생성 직후 compare 결과 0 ahead / 0 behind를 확인했다.
- Commission C(2026) 5252 publication page 및 PDF text layer를 확인했다. PDF 표제/날짜, 비구속적 지위(para. 8), 데이터 연결(§2.5 paras. 26–28), 복합 시스템/위험평가(§2.6), substantial modification(§4), support period(§5), core functionality(§6), risk assessment/due diligence(§7), RDPS(§8), Machinery Regulation 관계(§9.3.2)를 서보 드라이브 관점으로 정리했다.
- §2.5는 단순 electrical trigger와 인코딩된 디지털 정보를 구분한다. 단순 0/1 상태만으로 data connection이 자동 성립하지 않으며 송신 측 encoding과 수신 측 decoding을 확인해야 한다.
- §6은 제품의 실제 core functionality로 Annex III/IV 분류를 판단하고, 내장 부품 또는 ancillary function만으로 전체 제품 분류가 자동 결정되지 않는다고 설명한다.
- §8 RDPS는 원격 처리 여부, 기능 수행에 대한 필수성, 제조자 개발/책임 여부를 누적 확인한다. Industrial robot example은 원격 처리에서 명령을 반환하고 해당 처리가 기능에 필수인 사례다.
- Commission C(2026) 7861 Annex I에서 41개 표준 주제/ESO adoption deadline을 추출했다. 항목 1/15는 30.11.2026, 수평 항목 2–14는 30.10.2027, 수직 항목은 대부분 31.01.2027로 표시된다. 항목 18의 날짜는 text extraction에서 보이지 않아 미확인으로 남겼다.
- 신규 보고서 `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` 생성.
- **취득/무결성 제한:** PDF text layer는 확인했으나 직접 다운로드 도구가 Commission PDF 원본 bytes를 반환하지 않아 바이너리 SHA-256을 산출하지 못했다. Guidance PDF는 ANFR mirror의 text layer로 확인했으며 Commission 원본과 byte identity는 미검증. M/606 Annex도 Commission register PDF text layer로 확인했으나 원본 바이너리 해시 미검증.
- 보고서/관리 문서 변경은 CRA 문서화 작업이다. 운영 main.py/workflow/state/history/archive, Gemini/Discord 호출, SIL 3 자료는 변경하지 않았다.
- 다음: item 18 원본 PDF 이미지 확인, 원본 bytes/hash 취득, §2.5/§6/§8 내용을 기존 interface/requirements/SEC matrix에 claim-level로 연결, Annex I canary 확장.


## 2026-11-17 — PR #30 및 격리 CI 트리거 준비

- PR #30을 생성하고 draft에서 ready-for-review로 전환했다: https://github.com/useformotor3/ai-discord-bot/pull/30.
- PR event 기반 CI가 connector readback에 나타나지 않아, 테스트 전용 `.github/workflows/tests.yml`의 push branch allowlist에 현재 감사 브랜치만 추가했다. 운영 `.github/workflows/run.yml`은 수정하지 않았다.
- 최신 branch head `7311e569053d6816c0685b740a782881c56dfc2a` 이후 PROJECT_LOG 검증 메모를 추가했다. 현재 CI status 조회는 비어 있으므로 테스트 성공으로 기록하지 않는다.
- PR #30은 9 commits ahead / 0 behind, 8 changed files. 문서/로그/격리 테스트 workflow만 변경했다.
- 다음: GitHub Actions run/status 결과를 확인하고, 성공 시 PR merge 전후 readback 및 safety refs를 수행한다. 실패 시 로그를 분석하고 수정 후 재검증한다.


## 2026-11-17 — PR #30 병합 및 복구 체크포인트

- PR #30 `https://github.com/useformotor3/ai-discord-bot/pull/30` 병합 완료.
- Merge commit: `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`.
- Run #610 (`44050954456`) success: **141 passed, 1 xfailed**; source blob identity, compileall, live 9 official sources, corrigenda precedence, Article 13(8) locator/quote canary 통과.
- Pre-merge ref `safety/pre-merge-main-pr30-2026-11-17` → `80245d9e132380a10581612c031f87869993b98d`; post-merge ref `safety/post-merge-main-pr30-2026-11-17` → `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`. post-merge ref와 main compare identical 확인.
- PR #30에서 수정한 파일은 `.github/workflows/tests.yml`, AI_RULEBOOK, MASTER_PLAN, PROJECT_LOG, PROJECT_STATUS, README, SESSION_LOG 및 신규 감사 보고서다. 운영 `run.yml`/런타임 코드/state/history/archive는 변경하지 않았다.
- 원본 PDF 바이너리 SHA-256과 item 18 날짜는 미완료/미확인으로 남긴다.


## 2026-11-17 — PR #30 사후 상황판 동기화

- PR #30 merge `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd` 및 Run #610 success를 README/PROJECT_STATUS/MASTER_PLAN/AI_RULEBOOK/SESSION_LOG/PROJECT_LOG에 반영했다.
- `docs/pr30-postmerge-status-sync-2026-11-17`은 문서 전용 브랜치이며 구현 작업 브랜치로 취급하지 않는다.
- 격리 tests workflow의 push allowlist에 이 문서 브랜치를 추가해 변경분도 CI 검증한다. 운영 workflow는 변경하지 않는다.
- PR #30의 원본 PDF binary hash와 item 18 날짜 미확인 제한을 계속 유지한다.


## 2026-11-17 — PR #31 최종 사후 확인

- PR #31 merge commit `24312166b892127e845721793b1abfee4d91f9c2`.
- Run #618 (`44051283237`) success: 141 passed / 1 xfailed, compileall, source identity, 9 official source canary 통과.
- Pre-merge `safety/pre-merge-main-pr31-2026-11-17` → `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`; post-merge `safety/post-merge-main-pr31-2026-11-17` → `24312166b892127e845721793b1abfee4d91f9c2`. post-merge ref and main compare identical.
- README/PROJECT_STATUS에서 특정 시점의 main SHA를 현재 HEAD처럼 고정 표기하지 않도록 수정했다. 이후 세션 시작 시 main HEAD를 실시간 조회한다.


## 2026-11-17 — Guidance claim mapping 및 PDF 원문 취득 자동화

- 작업 브랜치 `cra/guidance-claim-mapping-2026-11-17` 생성.
- 신규 `reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv`: G-001~G-013 비구속적 Commission explanation, 문단/페이지 locator, 연결된 CRA requirements/interfaces/SEC controls.
- 인터페이스 매트릭스 15행, 요구사항 추적표 35행, SEC control/test matrix 36행에 Guidance claim ID 및 M/606 Annex I candidate item columns를 추가했다. 후보 관련성은 제품 분류나 harmonised status를 의미하지 않는다.
- `cra_pdf_sources.py` 및 `tests/test_cra_pdf_sources.py` 추가: Commission-hosted PDF fetch, host allowlist, PDF magic/identity marker/page count, raw byte SHA-256, extracted text SHA-256, optional ANFR mirror fallback, manifest/artifact output.
- 테스트 workflow에 pypdf dependency, exact blob pins, live PDF canary, 7-day artifact upload를 추가했다. 운영 workflow는 변경하지 않았다.
- CI와 실제 PDF binary 취득은 아직 확인 전이다. 성공·해시·artifact 보관을 선제 주장하지 않는다.
- 다음: PR CI에서 mock test 및 live PDF canary 실행, artifact download/readback, PDF bytes/hash 검증, M/606 item18 시각 확인, matrix/report readback.


## 2026-11-17 — CRA PDF 원문 바이너리 취득 및 표 이미지 검증

- Run #642 (`44052336199`)에서 `cra_pdf_sources.py` PDF canary 성공, PDF 2개 다운로드·파싱·해시 산출.
- Guidance C(2026)5252 ANFR mirror: 1,190,726 bytes, 84 pages, raw SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; fallback used=true. Commission-hosted original byte identity는 미확인.
- M/606 C(2026)7861 Annex: Commission document-register PDF, 151,267 bytes, 6 pages, raw SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`; fallback used=false.
- Extracted-text SHA-256 및 page count는 `reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json`에 기록.
- Artifact ID `14313359693` ZIP를 다운로드했고, ZIP SHA-256 `150a687e4d4b13fdd20a432e99fc8ea9ec5bc847b8551dd3f157258dc41cd869`가 GitHub metadata와 일치함을 확인.
- M/606 item18 password manager deadline은 원본 PDF printed page 3, PDF page index 2의 표 우측 셀에서 `31/01/2027`로 시각 확인.
- Run #642의 기존 CRA HTML source canary는 Commission summary page에 PDF document number `C(2026) 5252`를 요구해 실패했다. Summary page와 PDF Annex의 검증을 분리하도록 `cra_source.py`와 regression test를 수정했으며 재실행 대기.


## 2026-11-17 — Run #669 최종 source canary 성공

- Run #642가 발견한 Commission summary page marker 오류를 수정했다. `cra_source.py`는 page summary metadata만 검증하고, PDF document number는 `cra_pdf_sources.py`에서 raw PDF identity marker로 검증한다.
- Regression test 추가, workflow blob pin 갱신 후 Run #669 성공: 148 passed / 1 xfailed.
- PDF 2개 fetch/parse/hash/artifact upload 통과. Artifact ID 14315096266 다운로드 후 ZIP SHA-256 및 PDF별 SHA-256 재계산 일치.
- 9개 공식 HTML sources, consolidated CRA corrigenda, Article 13(8) locator/quote live canary 통과.
- M/606 item18 deadline 31/01/2027 시각 확인 완료. Guidance Commission primary binary identity는 미확인으로 남긴다.


## 2026-11-17 — 최종 branch-head Run #690

- 최신 branch HEAD `535300d60e1e943a867e3348c3c152832238b665`에서 Run #690 성공: 148 passed / 1 xfailed.
- PDF 2종 fetch/parse/hash, artifact #14315106623 upload/download/re-hash, 9개 HTML sources, Article 13(8) live locator/quote 통과.
- ZIP digest `da2f0e5fbfb5f5fa66360a2faa5af3d85821d3b7269885e34e1a3115f37cd3e2` GitHub metadata와 일치; 내부 PDF hashes도 manifest와 일치.
- PR #33 최종 diff/safety checkpoint 검토 후 병합한다.


## 2026-11-17 — Latest branch-head Run #702

- Run #702 on HEAD `3b895cb1411ada883b8df04972f929c1381f4053`: success, 148 passed / 1 xfailed.
- 2 PDF sources, 9 HTML sources, Article 13(8) locator/quote, corrigenda, compileall and blob pins passed.
- Artifact #14314174227 downloaded and SHA-256 reverified: ZIP `8fddbba46ccf9b0901b36d88ce27d79817ac620f9fabf37a8b6beefe5dfcaa82`; internal PDF hashes match provenance manifest.
- PR #33 is ready for final diff/safety check.


## 2026-11-17 — PR #33 merge 및 복구 확인

- PR #33 squash merge 완료: `50e4784de60430bb2b8c70ca06b41627d75379ae`.
- Run #713 success: 148 passed / 1 xfailed; 2 PDF sources and 9 HTML sources live canary passed.
- Pre/post safety refs `safety/pre-merge-main-pr33-2026-11-17` / `safety/post-merge-main-pr33-2026-11-17`; post ref and main compare identical.
- PR #33 diff는 18개 파일, isolated tests workflow + CRA source verifier/PDF fetcher/tests + 보고서/매트릭스/관리문서. main.py, production run.yml, state/history/archive, Gemini/Discord production execution, SIL 3 files unchanged.
- Next implementation starts from latest main in a new branch after PR #34 documentation-only sync.


## 2026-11-17 — CRA traceability integrity gate

- `cra_traceability.py`와 `tests/test_cra_traceability.py`를 추가했다.
- 13 Guidance claims / 15 interfaces / 35 CRA requirements / 36 SEC controls의 row count, unique IDs, claim foreign keys, orphan claim, M/606 item 1–41, provenance hashes, item18 confirmation, README/report links, PROJECT_LOG JSONL integrity를 검증한다.
- Negative tests: unknown G-999 reference와 invalid M/606 item 42가 CI fail-closed하도록 검증.
- tests workflow에 source blob pins, compileall 및 `python cra_traceability.py` step을 추가했다. CI 결과 대기.


## 2026-11-17 — PR #35 traceability gate merge

- PR #35 squash merge 완료: `2a347a60f2632bbe87044484187765adab45aee2`.
- Run #738 success: 151 passed / 1 xfailed; traceability gate, PDF/HTML source canaries passed.
- Traceability gate: 13/15/35/36 records, all Guidance claims linked, 89 project log events including legacy rows, M/606 1–41, PDF hashes and item18 confirmation passed.
- Pre/post safety refs `safety/pre-merge-main-pr35-2026-11-17` / `safety/post-merge-main-pr35-2026-11-17`; post ref and main compare identical.
- Next implementation starts from latest main after PR #36 documentation-only status sync.


## 2026-11-17 — M/606 Annex I 41-item mapping

- `reports/CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv` 신규 작성: 41개 Annex I 항목의 paraphrased topic, ESO deadline, page locator, servo-drive relevance class, candidate CRA/SEC/interface IDs.
- Horizontal items 1–15, vertical product types, component-dependent items를 구분하고 intended purpose/core functionality에 따른 조건부 판단을 기록.
- ESO adoption deadlines를 제조자 compliance deadline과 구분하고, OJ citation 전 harmonised standard/presumption으로 주장하지 않도록 명시.
- Item18 deadline locator를 PDF viewer page3 / printed EN3로 정정.
- Next: extend traceability validator and tests to check all 41 mapping rows and foreign keys.


## 2026-11-17 — PR #37 M/606 41-item map merge

- PR #37 squash merge: `25e1c36cc61a3001b5045cb8a6e90473fe830459`.
- Run #757 success: 154 passed / 1 xfailed; 41-item mapping traceability, PDF/HTML source canaries passed.
- Pre/post safety refs `safety/pre-merge-main-pr37-2026-11-17` / `safety/post-merge-main-pr37-2026-11-17`; post ref and main compare identical.
- M/606 item18 printed page EN3 locator and 31/01/2027 deadline validated.
- Next implementation starts from latest main after PR #38 documentation-only status sync.


## 2026-11-17 — CRA 제품 경계 및 증거 수집 기준서

- `reports/CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md` 작성.
- 제품 식별·intended purpose·product boundary·network interfaces·RDPS·security functions·BOM/SBOM·vulnerability handling·support period·evidence inventory를 한국어 템플릿으로 정리.
- 실제 제조사/모델 자료가 없어 제품별 CRA 분류·적합성은 확정하지 않는다. 첫 자료는 정확한 모델 데이터시트와 사용설명서.


## 2026-11-17 — PR #39 CI 통과

- Run #776 성공: 154 passed / 1 xfailed. Traceability 13/15/35/36/41 및 PROJECT_LOG 95 records 통과.
- CRA Guidance PDF 84 pages, M/606 Annex PDF 6 pages 및 HTML live canary 통과; PDF evidence artifact 업로드 성공.
- Run #770의 validator 상대경로 오류를 수정하고 전체 CI를 재실행해 통과. 실패를 무시하거나 테스트를 생략하지 않음.
- PR #39 merge 전 안전 체크포인트 생성 및 merge 예정.


## 2026-11-17 — PR #39 merge 및 사후 검증

- PR #39 squash merge `aec679142bf8c12b1ce18b233956f9695d70ca21`.
- Run #781 success: 154 passed / 1 xfailed; CRA traceability, official PDF/HTML canaries and PDF artifact upload passed.
- Pre/post safety refs 생성. Post ref와 merge SHA/main 비교 `identical` 확인.
- 제품별 데이터시트/사용설명서가 없으므로 제품별 적용성/분류는 미확정으로 유지.


## 2026-11-17 — 통합 CRA 보고서 독립 검토 시작

- 보고서 추가 섹션의 중복 번호(§11–§13)를 확인하고 §14–§16으로 정정.
- Annex III Important products와 Annex IV Critical products 용어를 구분.
- 독립 검토 기록 추가, unique top-level section numbering validator와 negative test 추가.
- 다음은 법령 locator와 Guidance PDF claim locator를 표본 대조한다.


## 2026-11-17 — 독립 보고서 검토 1차 수정

- §11–§13 중복을 §14–§16으로 정정, Annex III Important / Annex IV Critical 용어 구분.
- CRA traceability에 중복 top-level section number 검증 및 negative test 추가.
- Run #797: 155 passed / 1 xfailed, PDF/HTML canaries 통과.
- EUR-Lex Article 6, 7(1), 10, 11, 14, 32, 69, 71 및 EHDS Regulation 2025/327 Article 104 적용일을 표본 대조.
- 다음 단계: CRA-001~CRA-035 법령 locator 전수 대조 및 G-001~G-013 Guidance PDF locator 표본 대조.


## 2026-11-17 — Guidance PDF locator 재대조

- Run #702 artifact PDF를 내려받아 SHA-256 manifest와 대조하고, G-001~G-013 paragraph locator와 printed page number를 재확인.
- G-002, G-005, G-006, G-008, G-009, G-010, G-012, G-013의 페이지 범위를 정정. 나머지 5개는 유지.
- physical PDF page index와 printed page number를 분리해 기록.
- Commission-hosted primary byte identity 미확인 한계는 그대로 공개.


## 2026-11-17 — PR #41 merge / CRA locator audit 다음 단계

- PR #41 merge `acfa2f583157ac541c4c60d71090197322bc8efb`; Run #806 155 passed / 1 xfailed.
- Guidance claim G-001~G-013 PDF paragraph/page locator 8건 정정 및 독립 audit record 추가.
- Pre/post safety refs 생성, post ref와 main compare identical.
- 다음은 CRA-001~CRA-035 법령 locator와 각 row의 법적 설명·적용 주체·조건·예외를 공식 EUR-Lex 원문과 행 단위로 교차 검토한다.


## 2026-11-17 — SBOM 의무 원문 대조

- EUR-Lex Annex I Part II(1), Annex II(9), Annex VII(2)(b), (8)을 대조.
- 기계 판독형 SBOM(최소 top-level dependencies) 작성은 기본 의무, 기술문서 포함은 Annex VII(2)(b), 시장감시당국 요청에 따른 제출은 Annex VII(8), 사용자 제공은 Annex II(9) 조건부로 각각 분리.
- 통합 보고서의 법적 해석 문구를 이 구분에 맞춰 보강.


## 2026-11-17 — CRA 법령 locator 1차 인벤토리

- CRA-001~CRA-035 조항 참조를 1차 검토. 잘못된 Article/Annex 번호는 발견되지 않았으나 문장·조건·예외의 전수 검토는 계속.
- SBOM 의무의 Annex I Part II(1), Annex VII(2)(b)/(8), Annex II(9) 구분을 명확화.
- Run #819: 155 passed / 1 xfailed; official PDF/HTML canaries 통과.


## 2026-11-18 — CRA PR #42 병합 및 프로젝트 재개 상태 동기화

- 상세 재개 기록: [SESSION_LOG_2026-11-18.md](SESSION_LOG_2026-11-18.md).
- PR #42 exact head CI Run #824 success: 155 passed / 1 xfailed; source integrity, compile, traceability, PDF/HTML canaries 통과.
- Merge commit `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`; pre/post safety refs 생성 및 post ref == main 확인.
- Guidance PDF는 ANFR mirror fallback=True이며 Commission primary byte identity는 미확인.
- 최신 재개 스냅샷 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)에 활성 범위, 기준점, 검증, 한계 및 다음 작업을 정리했다.


## 2026-11-19 — PR #97 기준점 확인 및 프로젝트 관리 문서 정합성 점검
- 최신 main commit `9ebab690b6cbbf0f3588bfeab16c622dca4d65e9`의 commit message와 GitHub ref를 재확인했다.
- PR #97 exact-head Run #983 success, 172 passed / 0 failed; exact-main Run #984 (ID 44450311535) success, 172 passed / 0 failed을 확인했다.
- Exact-main workflow의 source blob integrity, compile, CRA traceability, full pytest, official CRA PDF live canary, artifact upload, live EUR-Lex canary가 모두 통과한 기록을 대조했다.
- 관리 문서 간 최신성 차이를 확인했다: README와 MASTER_PLAN은 PR #95/#96 수준, PROJECT_STATUS_CURRENT는 PR #96 수준, PROJECT_STATUS.md는 2026-11-17 역사 스냅샷이었다. 이번 PR에서 현재 진입점과 최신 기준점을 명확히 동기화한다.
- 기존 분기 브랜치 `cra/applicability-core-functionality-audit-2026-11-19`는 main 대비 9 ahead / 9 behind이며 merge-base가 오래되어 통합하지 않았다. 필요한 작업은 최신 main 기반 새 브랜치에서 진행한다.
- CRA 제품별 실제 자료는 여전히 미제공. E-001~E-015는 not_provided 상태를 유지하며 제품별 적합성/분류/시험 Pass를 주장하지 않는다.
- 운영 `main.py`, `.github/workflows/run.yml`, secrets, `state.json`, `history.json`은 변경하지 않았다.


## 2026-11-19 — PR #98 상태 문서 정합성 병합
- PR #98 merge fa97e00b4f6ba1c31d175efcd0a48e68fe926347; README/PROJECT_STATUS_CURRENT/MASTER_PLAN/SESSION_LOG/PROJECT_LOG를 PR #97 기준으로 동기화하고 PROJECT_STATUS.md를 역사 스냅샷으로 명시.
- Exact-head Run #986 / ID 44454415836: success, 172 passed / 0 failed. Official HTML live canary 9개 출처 및 Article 13(8) 확인.
- PDF source canary는 EUR-Lex PDF endpoint empty body로 SKIPPED; artifact upload도 skip. 이를 통과로 기록하지 않았다.
- Post-merge safety ref safety/post-merge-pr98-2026-11-19와 main identical.

## 2026-11-19 — PR #99 2025/2392 공식 source pack 및 locator parser 개선
- 공식 source catalog에 Commission Implementing Regulation (EU) 2025/2392 추가; source pack v4 / 10 official sources.
- cra_claims.py에 명시적 Annex category locator를 추가해 footnote (1)와 category 1.의 혼동을 방지.
- tests/test_cra_claims.py, tests/test_cra_source.py에 Annex/Article locator 및 source catalog 회귀 검증을 추가하고 tests workflow blob pins 갱신.
- PR #99 exact-head Run #993 / ID 44454970377: success, **173 passed / 0 failed**. Live source pack 10개, 2025/2392 33,865 chars, Annex I category 10 / Annex II category 1 locator canary 통과.
- Commission PDF 3개 수집/해시 성공; artifact #14496564799 SHA-256 c19aaf7465041fd21def6d634daaea08f897ec32ca1892452e6d18bce71d44c2. Guidance PDF는 fallback=True, 나머지 2개는 fallback=False.
- PR #99 merge b5e6982270a4b3b913e5ae584786340ce58755f3; post-merge safety ref safety/post-merge-pr99-2026-11-19와 main identical.
- Exact-main push CI는 아직 독립 확인하지 않았으며 성공으로 기록하지 않는다. 운영 main.py 및 .github/workflows/run.yml 미변경.


## 2026-11-19 — PR #100 상태 동기화
- PR #100 merge `6342ba3238c32b88d5c33e6cd0b60ad2178c7738`; PR #99 source pack v4와 live locator 결과를 README/현재 상황판/마스터 계획/로그에 동기화.
- Exact-head Run #995 / ID 44455231426: success, 173 passed / 0 failed; CRA traceability, 10 official sources, 3 PDF sources 및 Annex locator canary 통과.
- PROJECT_LOG.jsonl 188행 JSON parse, 183 unique event IDs 확인.
- Post-merge safety ref `safety/post-merge-pr100-2026-11-19`와 main identical.

## 2026-11-19 — PR #101 공식 source provenance artifact
- PR #101 merge `a47c1d4e8a85803778f87318535583fa83e1d5cf`; source provenance manifest builder, validation tests, CI artifact upload 추가.
- Exact-head Run #998 / ID 44455595307: success, 174 passed / 0 failed; 10 source records manifest artifact #14497541325 생성.
- Post-merge review에서 JSON newline escape가 실제 newline인지 확실하지 않고 CI가 parse를 검증하지 않는 점을 발견. PR #101 artifact는 superseded 처리하고 후속 PR #102에서 수정·검증.

## 2026-11-19 — PR #102 JSON serialization fail-closed fix
- PR #102 merge `84101bcc8871e41f8a25de3edf892666b1650b8c`; tests workflow에 실제 newline 및 json.loads + object equality round-trip 검증 추가.
- Exact-head Run #1000 / ID 44455799462: success, **174 passed / 0 failed**.
- Live official source pack 10개 및 Article 13(8), 2025/2392 core-functionality, Annex I category 10 / Annex II category 1 canary 통과.
- Manifest 10 records 생성·JSON parse·round-trip 성공. Artifact #14496534452 SHA-256 `7f2836072bdfa38b7857c47bdac4c6fdb2b71c38bd29b987889aad0646e78cc7`.
- PDF artifact #14497431708 SHA-256 `b4090a51f855b1d6f391b82942e6301d91119e651fe528848eaa77e66b5ac4ee`.
- Post-merge safety ref `safety/post-merge-pr102-2026-11-19`와 main identical. Exact-main push CI는 별도 확인 전.


## 2026-11-19 — LS메카피온 서보드라이브 제품군 예비 분석 착수
- 최신 main 기준점 `1baea7b034a0b49eb42c433f2edc9d5d2d1d7d73`에서 safety ref `safety/pre-lsmecapion-family-assessment-2026-11-19` 및 작업 브랜치 `cra/lsmecapion-family-assessment-2026-11-19`를 생성했다.
- LS메카피온 공식 제품 목록에서 13개 드라이브 계열, 입력전압/용량/통신형·펄스형 구분을 확인했다.
- 공식 매뉴얼 목록에서 iX700M Ver1.4(2026-05-26), iX7M Ver1.3, iX7NH Ver1.7 및 L7C/PHOX/L7NHF/L7P 등의 자료 목록을 확인했다.
- 제조사 DriveCM 페이지에서 지원 계열과 L7S/L7N 구형 제품의 LIVE i.C.E 사용 안내를 확인했다. 제품 목록·매뉴얼 목록·설정 도구 안내는 개별 제품의 HW/FW revision, 현재 판매 상태, 지원기간을 입증하지 않으므로 이를 추정하지 않는다.
- 보고서 초안 `reports/CRA_LS_MECAPION_SERVO_DRIVE_FAMILY_PRELIMINARY_ASSESSMENT_2026-11-19.md` 작성. CRA 입문 설명, 13개 제품군 표, Article 2 데이터 연결, 제품 경계, Annex III/IV 핵심 기능, Article 13/14 의무, 위협 시나리오, 참조 보안 아키텍처, 시험 계획, E-001~E-015 증거 게이트, 용어집 포함.
- EtherCAT 제품은 데이터 연결 가능성이 높다는 제품군 스크리닝을 기록하되, 인터페이스 존재만으로 Annex III Class I/IV 분류를 자동 확정하지 않는다. 펄스/아날로그 제품은 신호 의미와 서비스/설정 데이터 통신을 모델별로 확인해야 한다.
- 현재 HTML source pack 10개 + PDF source pipeline 3개는 CRA 주요 법령·공식자료의 수집 체계이지 모든 관련 제품법령·표준·FAQ의 전수 완료를 의미하지 않는다.
- 모델별 적용성·분류·적합성 Unknown, 보안 시험 Not Run 유지. 개별 매뉴얼 PDF 원본 확보·SHA-256·페이지 검토, 정확한 SKU/HW/FW 확인이 다음 단계다.


## 2026-11-19 — PR #104 LS메카피온 제품군 예비 분석 병합 및 CI 검증
- PR #104 merge `c3d234240d342d82cf9402ef0b07b82531ddee03`; 신규 LS메카피온 제품군 예비 분석 보고서 및 README/상황판/마스터 계획/세션 로그/기계 로그를 main에 반영.
- Exact-head Run #1004 / ID 44485297107: success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, M/606 41 통과.
- Live official CRA HTML source pack 10개 fetch 성공. JSON provenance manifest 10 records 생성·parse·object round-trip 성공.
- Manifest artifact #14509668548, SHA-256 `1d3ac8ea2e049780161766ef158fecfa3ab2a7d795b477424b339e5004772bf6`, 2,566 bytes; expires 2026-11-26 08:10:28 UTC.
- PDF canary는 EUR-Lex C/2026/6013 endpoint empty body로 temporary source outage / SKIPPED. PDF artifact는 생성되지 않았고 성공으로 기록하지 않음.
- Pre-merge ref `safety/pre-lsmecapion-family-assessment-2026-11-19`, post-merge ref `safety/post-merge-pr104-2026-11-19`; post ref와 main identical.
- No production main.py, .github/workflows/run.yml, secrets, state/history, legacy SIL 3 assets changed.
- 제품별 scope/classification/conformity Unknown, 모든 보안 시험 Not Run. 법령 전수 수집 및 모델별 원본 매뉴얼 분석은 후속 작업.


## 2026-11-19 — 최신 CRA 지침 및 M/606 개정 확인
- Commission CRA guidance C(2026) 6013 공식 페이지와 Commission CRA standardisation 페이지를 재확인했다. guidance는 비구속적이며 적용 범위/RDPS/FOSS/substantial modification/support period/reporting/risk assessment를 설명한다. M/606은 2026-11-10 개정되어 일부 수평 및 모든 수직 표준 제출 일정이 3개월 연장됐다.
- 이 일정 변경을 CRA 적용일 변경이나 Article 27 적합성 추정 발생으로 오해하지 않도록 LS메카피온 보고서에 별도 설명을 추가했다.
- iX700M Ver1.4, iX7M Ver1.3, iX7NH Ver1.7의 공식 매뉴얼 첨부 메타데이터를 재확인했다. 첨부파일 다운로드 링크는 제조사 사이트에서 “잘못된 접근”을 반환했다. PDF 원본 확보·해시·페이지 검토는 완료되지 않았으며 증거 accepted로 승격하지 않는다.
- 다음 작업은 모델별 매뉴얼 원본 확보 및 41개 표준/OJ 인용 상태·ENISA/Commission 최신 자료의 출처별 감사다.


## 2026-11-19 — PR #106 병합 및 ENISA/위임규정 추가 조사
- PR #106 squash merge 2c24b16ede905009f2a2f07edb4072bb9c244316; post-merge safety ref safety/post-merge-pr106-2026-11-19.
- Exact-head Run #1008 / ID 44489742051 success: 174 passed / 0 failed. Source integrity, compile, CRA traceability, full pytest, live 10-source HTML canary, JSON manifest round-trip 통과. PDF canary는 C(2026) 6013 PDF endpoint empty body로 SKIPPED, artifact 없음.
- 공식 source manifest artifact #14511852597, SHA-256 a34bd69a01bfe18f4967c1982e7ade0e959d0e9ae6f7740cfc9e94b5c566304a, 2,565 bytes.
- 보고서 v0.3에 Delegated Regulations (EU) 2025/1535 및 2026/881의 범위·효과와 ENISA의 SME maturity, secure-by-design, SBOM, secure update, SRP 자료를 추가했다.
- 2025/1535의 L-category 차량 제외를 일반 서보드라이브 면제로 확대하지 않는다. 2026/881은 CSIRT 전파 지연 규정이지 제조자 신고기한 연장 규정이 아니다.
- ENISA 기술자료는 법적 의무나 Article 27 적합성 추정을 부여하지 않는 실무 참고자료다.
- Exact-main push CI는 독립 확인 전이므로 미확인. 제품별 판정 Unknown, 시험 Not Run 유지.


## 2026-11-19 — PR #107 병합 및 기계류 규정 상호작용 검토
- PR #107 squash merge 0682d83f891a20438d6d37eb231c3b20ca72c67e; post-merge safety ref safety/post-merge-pr107-2026-11-19.
- Exact-head Run #1010 / ID 44490148586 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON provenance manifest round-trip 통과.
- Manifest artifact #14511858034 SHA-256 dd4305ae872aec9cf208228f8924ed06a2cf2a2c3b9cabd7b063babbe3c2c69e. PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED.
- Official Commission CRA FAQ 2026-09-04 및 Machinery Regulation (EU) 2023/1230을 검토했다. 양 규정 동시 적용 제품은 양쪽 요구와 적합성 평가 절차를 각각 확인해야 한다.
- 보고서 v0.4에 Machinery Regulation Annex III 1.1.9/1.2.1, 적용일 2027-01-20, EMC/LVD/RED/RoHS/WEEE/PLD 1차 스크리닝 및 제품 경계 질문을 추가했다.
- Exact-main push CI는 별도 확인 전. 제품별 적용성·책임분담 Unknown, 시험 Not Run 유지.


## 2026-11-19 — PR #108 병합 및 추가 CRA 표준화 경로 조사
- PR #108 squash merge 4a1b44501dec629ae2f42106d6b8d200f177765a; post-merge safety ref safety/post-merge-pr108-2026-11-19.
- Exact-head Run #1012 / ID 44490507909 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON manifest round-trip 통과.
- Manifest artifact #14512183573 SHA-256 8e3b3883bc2b3b3f0c9c0d002efb2d794e1610883f186ccab16ebb0eb8f51c05. PDF canary는 C(2026) 6013 empty body로 SKIPPED.
- Commission Notice C/2026/1695의 CRA standardisation Action 5가 M/606을 보완하며 Annex III/IV 밖의 machinery, rail, lifts, agricultural machinery, AI, solar inverters에 대한 추가 표준화 요청을 계획함을 확인했다.
- Action 5는 계획이며, 실제 표준 발행·OJ 인용·Article 27 적합성 추정으로 확대 해석하지 않는다.
- 보고서 v0.5에 M/606과 Action 5의 차이, OJ 인용 확인 게이트를 추가한다. Exact-main push CI는 별도 확인 전.


## 2026-11-19 — PR #109 병합 및 M/606 개정 Annex 원문 대조
- PR #109 squash merge 172caa7427dd7af412d555bf2a82660537c0e16f; post-merge safety ref safety/post-merge-pr109-2026-11-19.
- Exact-head Run #1014 / ID 44490815716 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON manifest round-trip 통과.
- Artifact #14511964662 SHA-256 16f516e1bb84f2267327318d70994b1e77f7eb1029c5a40685763e67cc882dfe. PDF canary는 C(2026) 6013 empty body로 SKIPPED.
- C(2026) 7861 final Annex I 원문을 직접 확인했다. M/606 41개 제출기한: 1·15번 2026-11-30, 2–14번 2027-10-30, 16–41번 2027-01-31.
- 기존 41행 매핑 CSV와 validator 일정 값이 원문과 일치하여 날짜 수정 없이 보고서 v0.6에 상세 설명을 추가한다.
- OJ citation 상태는 별도 전수 감사가 필요하며, M/606 Annex는 그 자체로 Article 27 presumption을 주지 않는다.
- Exact-main push CI는 별도 확인 전.


## 2026-11-19 — PR #110 병합 및 SRP v1.3 신고 운영 상세화
- PR #110 squash merge 57c7734d59b5046598e67aefd5d74a2ea29d3e2b; post-merge safety ref safety/post-merge-pr110-2026-11-19.
- Exact-head Run #1016 / ID 44491245339 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON manifest round-trip 통과.
- Artifact #14512063867 SHA-256 b2630ffa5f6d6cd71026faf31422e2365a836c51c50225c6ccdd51f2b1f55b09. PDF canary는 C(2026) 6013 empty body로 SKIPPED.
- ENISA SRP FAQ 2026-10-15 및 platform/User Manual v1.3(2026-11-04)을 확인하고 보고서 v0.7에 신고 시계, AR 역할, EU Login/MFA, no API, English-only UI, outage workflow, CDaC 선택, 과거 출시 제품·통합 부품 신고 범위를 상세화했다.
- SRP v1.3 72h counter 표시가 인지 시각 기준과 다를 수 있고 AEV Final Report counter가 미구현임을 확인. 내부 deadline tracker를 별도 운영해야 한다.
- Exact-main push CI는 별도 확인 전.


## 2026-11-19 — PR #111 병합 및 SRP v1.3 신고 운영자료 반영
- PR #111 squash merge 26e6cc348f0e4207fe04a4d789ace38b7434b8ea; post-merge safety ref safety/post-merge-pr111-2026-11-19.
- Exact-head Run #1018 / ID 44491554033 success: 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41, 10 official HTML sources, JSON manifest round-trip 통과.
- Manifest artifact #14512443373 SHA-256 6354a013d1753e4b67dae2fb87071b330f6b591097b8946ce7ec95f050e29dea. PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED.
- LS메카피온 report v0.7에 SRP v1.3 FAQ/User Manual, reporting timelines, Primary/Secondary AR, MFA, no API, outage process, counter caveats 반영.
- 다음은 모델별 매뉴얼 PDF 원본 확보·해시·페이지 검토, M/606 41개 표준 개별 진행상태 및 OJ citation 감사, C/2026/1695 Action 5 후속 요청 추적.
- Exact-main push CI는 독립 확인 전이므로 미확인.


## 2026-11-19 — PR #112 병합 및 제품/도구/ESI 공개목록 매핑
- PR #112 squash merge 4507bc5dc2a8c189073ab0728a2b271063c4bf5c; post-merge safety ref safety/post-merge-pr112-2026-11-19.
- Exact-head Run #1020 / ID 44491849633 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON manifest round-trip 통과.
- Artifact #14513316478 SHA-256 a57834f4e1cf07fb42be120cb50090badb86acb3e4a8626503d2ed7747afd5c4. PDF canary는 C(2026) 6013 empty body로 SKIPPED.
- 제품표 13개군, DriveCM v1.03.2 지원 목록, ESI v0.98 11개 적용 모델을 대조해 보고서 v0.8에 제품별 인터페이스/도구 매핑을 추가했다.
- iX700M은 ESI v0.98 공개 적용 모델에 명시되지 않으며, iX700M/L7NHA/B/L7SA/B/GEM의 DriveCM 지원 여부도 공개 게시물만으로 확정하지 않는다.
- 도구의 펌웨어 다운로드 프로그램 언급은 확인했지만 서명·무결성·인증·롤백 등 보안 통제는 검증하지 않았다.
- 원본 PDF/설치 파일/ESI XML의 다운로드·SHA-256·내용 검토는 미완료. Exact-main push CI는 독립 확인 전.


## 2026-11-19 — PR #113 병합 및 M/606 ESO 진행상태·OT/IACS 표준 조사
- PR #113 squash merge 5273e6da25862a8ad1e92b2473a11a63b0d8015f; post-merge safety ref safety/post-merge-pr113-2026-11-19.
- Exact-head Run #1022 / ID 44492219721 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON manifest round-trip 통과.
- Artifact #14513586428 SHA-256 bc438c098ff591da5690070adcc417d3f440adcf4a6635df87b00b05ed9b7d95. PDF canary는 C(2026) 6013 empty body로 SKIPPED.
- STAN4CR/CEN-CENELEC/ETSI joint M/606 report V2.0 (2026-06-03) 4페이지를 검토하고 개별 표준 단계 및 OT/IACS supporting deliverables를 보고서 v0.9에 반영했다.
- EN IEC 62443-4-1/-4-2/-3-3은 M/606 41개 Annex I 표준 및 CRA OJ citation과 구분되는 supporting deliverables다.
- 2026-06-03 publication forecast는 과거 snapshot이며 C(2026)7861 개정 이후의 현재 제출기한으로 사용하지 않는다.
- Exact-main push CI는 독립 확인 전.


## 2026-11-19 — PR #114 병합 및 M/606/OT 진행현황 반영
- PR #114 squash merge 88a3c3b29ecf7af2884e6df288075a0ce48f73f2; post-merge safety ref safety/post-merge-pr114-2026-11-19.
- Exact-head Run #1024 / ID 44492644455 success: 174 passed / 0 failed. CRA traceability, 10 official HTML sources, JSON manifest round-trip 통과.
- Artifact #14514585121 SHA-256 bd7e0fe6244c8d9ad0bd312ec3e4016836bfc1c738a0a685a8d5c3696bc6a198. PDF canary는 C(2026) 6013 empty body로 SKIPPED.
- 보고서 v0.9에 2026-06-03 ESO M/606 progress snapshot과 산업용 IEC 62443-4-1/-4-2/-3-3 supporting deliverables를 추가했다.
- 다음 작업은 2026-11-19 현재의 개별 M/606 진행상태·최종 발행·OJ citation 확인, LS메카피온 공식 매뉴얼·ESI·DriveCM 원본 파일 확보 및 해시·페이지 검토다.
- Exact-main push CI는 독립 확인 전.


---

## 2026-11-20 — M/606 ETSI 공개 진행상태 부분 최신화

- 시작 기준 main: `82e9bbf31124b840fa560f7a9e45b1fe84c53ce7`.
- 작업 브랜치: `cra/m606-live-etsi-status-audit-2026-11-20`.
- 복구 기준: `safety/pre-m606-live-status-audit-2026-11-20`.
- 공식 유럽위원회 CRA 표준화 페이지, C(2026) 7861 Annex I, ETSI M/606 Work Programme v2.3.3 및 개별 작업 페이지를 확인했다.
- ETSI 활성 M/606 작업 18개 확인(2026-11-17). EN 304 625 승인 절차 종료(11-02), EN 304 626 종료(11-05), EN 304 636 의견 분류 평가 완료(10-06)를 기록했다.
- 채택/발행/OJ 일정은 계획값으로 구분. Article 27 적합성 추정은 OJ 실제 게재 전에는 주장하지 않는다.
- 보고서 §23 addendum, 상황판, 마스터 계획 및 README를 갱신했다.
- 법령/표준 전수감사 완료로 표시하지 않음. 41개 전체 개별 상태/OJ, CEN/CENELEC 상세, 제조사 파일 원본·해시·페이지 검토는 미완료.
- 제품별 scope/classification/conformity = Unknown; security tests = Not Run.
- 이 세션에서 운영 코드, 운영 workflow, secrets, state/history, legacy SIL 3 자료는 변경하지 않았다.
- 검증 결과는 PR exact-head CI 실행 후 기록한다.


### 추가 공식 상태 확인 — CEN-CENELEC EN 40000 발행 (2026-11-20)
- CEN-CENELEC 공식 뉴스룸의 2026-11-19 발표에서 EN 40000-1-1(용어) 및 EN 40000-1-2(원칙·제품 위험관리·생애주기 활동) 발행 사실을 확인했다.
- EN 40000-1-2를 LS메카피온 제품 위험평가·개발·생산·유지보수·지원종료 프로세스 검토의 우선 참고표준으로 기록했다.
- 표준 발행과 CRA Article 27 OJ 인용은 별개다. OJ 참조 게재가 확인되기 전에는 적합성 추정을 주장하지 않는다.
- 통합 보고서 §23 및 상황판/마스터 계획/README에 반영했다.


---

## 2026-11-20 — PR #116 병합 및 사후 안전 기준점

- PR #116 `docs(cra): refresh M/606 status and EN 40000 publication` squash merge 완료.
- Merge SHA / main: `6092ca1c61c696a716583e6bc0f7d5150cbee269`.
- Pre-work safety: `safety/pre-m606-live-status-audit-2026-11-20`; post-merge safety: `safety/post-merge-pr116-2026-11-20` (merge SHA에서 생성).
- Exact-head Run #1032 / ID `44638812806`: success. Source blob identity, compile, CRA traceability, full pytest, live official CRA HTML source canary and manifest upload succeeded.
- Provenance artifact #14584442966, 2,566 bytes, SHA-256 `408714c0be46f9238250aaff678191a86ac0ff35112370132d679f59ba591836`, expires 2026-11-26 23:35:10 UTC.
- PDF artifact upload skipped; PDF 원문 확보 성공으로 기록하지 않는다.
- Exact-main push CI는 연결된 조회로 독립 확인되지 않아 미확인으로 유지한다.
- PR #116은 문서/로그 6개만 변경. runtime/workflow/secrets/state/history/legacy SIL 3 자산 미변경.


---

## 2026-11-20 — ETSI 상태표 정정: 11-19 최신 요약 스냅샷 우선

- ETSI Work Programme Version 2.3.3 전체 M/606 요약 목록의 기준일이 2026-11-19이며 18개 작업을 표시함을 확인했다.
- 이전 PR #116의 EN 304 625/626 상태는 각각 11-11/11-09 상세 페이지의 상태였고, 11-19 요약 목록보다 오래된 스냅샷이었다.
- 최신 요약 목록 기준으로 EN 304 625 = Comments categorisation assessed (2026-11-05), 다음 상태 목표 2027-01-15 / 예정 절차 2027-02-08 VA.
- EN 304 626 = Comments categorisation assessed (2026-11-06), 다음 상태 목표 2027-01-21 / 예정 절차 2027-02-17 VA.
- EN 304 636 = Comments categorisation assessed (2026-10-06), 다음 상태 목표 2026-12-22 / 예정 절차 2027-01-11 VA.
- 이전 계획표의 승인 종료·2027-03 OJ 목표 일정은 현재값으로 유지하지 않고, 최신 요약 목록에 표시된 다음 상태/절차로 교체했다. 예정일은 실적이 아니며 OJ 인용 여부는 별도 확인 대상이다.
- 통합 보고서 §23.3, 상황판, 마스터 계획, README에 정정사항을 반영한다.


---

## 2026-11-20 — CRA 공식 관보 해설 C/2026/6013 확보·분석

- OJ C/2026/6013 (17.11.2026) 최종본 61페이지 PDF를 EUR-Lex에서 확보했다.
- PDF 2,709,282 bytes; SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`.
- C(2026)7861 Annex I 6페이지 PDF도 확보: SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- CI artifact #14584269836, 3,070,504 bytes, SHA-256 `0c77f3ae2546927fd2ae37da024b1b398e0d58a0be08fde50581a984f685c94f`. Artifact expiry 2026-11-26 23:39:21 UTC.
- C(2026)5252 draft PDF는 원래 EC redirect에서 fallback으로 ANFR mirror를 사용한 사실을 manifest에 기록하고, 최종 해석의 주 근거로 사용하지 않는다.
- OJ guidance §2.4–2.6, §4.3, §5, §6.1, §7.1–7.4, §8, §9.1을 검토해 제품 경계, 디지털 데이터 연결, core functionality, 업데이트 substantial modification, 지원기간, 구성요소 due diligence, 제품군 재사용, RDPS 및 Article 14 보고 의무를 LS메카피온 적용표로 정리했다.
- Article 14 reporting: 2026-09-11부터 CRA 적용범위 제품에 적용되며, 제품 지원기간 종료 후에도 보고 의무가 지속된다는 공식 해설을 확인했다.
- 통합 보고서 §24 및 상황판/마스터 계획/README/로그를 갱신한다.
- 제품별 판정은 SKU·설계·판매경계·지원정책 증거 확보 전까지 Unknown; security tests Not Run.


---

## 2026-11-20 — PR #119 병합 및 공식 관보 해설 분석 반영

- PR #119 `docs(cra): analyze OJ C/2026/6013 guidance for LS Mecapion` squash merge 완료.
- Merge SHA / main: `46feea8fab4924889be30f8ae5afb7a072673055`.
- Pre-work safety: `safety/post-merge-pr118-2026-11-20`; post-merge safety: `safety/post-merge-pr119-2026-11-20`.
- Exact-head Run #1038 / ID `44639933454`: success; source integrity, compile, CRA traceability, full pytest, official PDF source retrieval, HTML canary and manifest upload.
- PDF artifact #14584694804, 3,070,503 bytes, SHA-256 `a45396f7bc6d0d8abd29c1e0b3ee3655197e23f005fe5e3fbe6df16768a7f0c2`; individual PDF hashes matched the committed source manifest.
- OJ C/2026/6013 final guidance analysis and LS Mecapion product application map are in report §24.
- Exact-main push CI remains not independently confirmed; product scope/classification/RDPS remain Unknown; security tests Not Run.


---

## 2026-11-20 — CRA 지침 식별자 정정

- 기존 §15.1의 “C(2026) 6013” 표기는 문서 유형과 관보 인용번호를 혼동한 것이므로 정정한다.
- 최종 공식 지침의 관보 인용은 OJ C/2026/6013 (17.11.2026).
- C(2026) 5252 final은 Commission draft-guidance approval document이며 OJ citation이 아니다.
- 법적 해설은 EUR-Lex 최종 OJ PDF를 기준으로 하고, C(2026) 5252 ANFR fallback은 non-primary provenance로만 남긴다.
- 통합 보고서 §15.1 및 §24.1, 상황판, README, project log에 정정 기록을 추가한다.


---

## 2026-11-20 — LS메카피온 매뉴얼 원본 수집 재시도

- 공식 Servo 자료실에서 iX7M Ver1.3 및 iX7NH 200V Ver1.7 첨부파일명/용량/표시시각을 재확인: 각각 12.4 MB / 19.5 MB, 첨부 표시일 2026-06-05.
- iX700M 400V DRIVE 매뉴얼 Ver1.4가 공식 매뉴얼 목록에 2026-05-26 게시물로 표시됨. 첨부파일 상세는 아직 확인되지 않음.
- iX7M/iX7NH 첨부 다운로드는 브라우저/검색 경유 timeout 또는 HTTP 502. 원본 PDF bytes/해시/페이지 수/본문 분석은 미완료.
- 보고서 §25와 manufacturer intake JSON에 metadata-only 상태로 기록. 제품별 분류 Unknown, 보안시험 Not Run 유지.
- 다음 조치: 제조사 기술지원 채널을 통한 원본 파일 요청 또는 다운로드 경로 복구 후 SHA-256 및 페이지별 증거 검토.


---

## 2026-11-20 — iX700M 모델 코드 및 CE 문서 메타데이터

- LS메카피온 공식 인증서 게시물에서 iX700MD1-B-150B 모델 코드와 제조사 정의(D1=1축, B=480 Vac, 150=15 kW, encoder B=BiSS-C)를 확인.
- CE_DoC-LVDEMC 첨부 238.9 KB, 게시 2026-04-30. 첨부 원본은 HTTP 502로 미확보; DoC 본문은 검증하지 않음.
- CE/LVD/EMC 게시 메타데이터를 CRA 적합성 또는 사이버보안 증거로 오인하지 않도록 보고서 §26과 intake JSON에 한계를 기록.
- 제품별 CRA 판정 Unknown, 보안시험 Not Run 유지.


---

## 2026-11-20 — PR #123 병합 및 iX700M 식별 증거 동기화

- PR #123 squash merge: `2f09103fa5efe23374458ddf49de7c0fd4febddb`.
- Pre-merge safety: `safety/pre-ix700m-doc-metadata-2026-11-20`; post-merge safety: `safety/post-merge-pr123-2026-11-20`.
- Exact-head CI Run #1046 / ID `44644308627`: success. Source identity, compile, CRA traceability, full pytest, official CRA PDF source retrieval and manifest upload passed.
- PR #123 report §26 documents iX700MD1-B-150B manufacturer code definitions and CE/LVD/EMC listing metadata; PDF bytes were not acquired, and no CRA conformity inference is made.
- PR #122 merge `8a18856a677ccbab4117c0ea35524116ac5ad70a`, Run #1044 success; report §25 and 4-record manufacturer intake register document iX7M/iX7NH manual metadata, not original PDF content.
- Product scope/classification/RDPS Unknown; security tests Not Run; exact-main push CI not independently confirmed.


## 2026-11-20 — M/606 표준 발행 및 OJ 인용 게이트 부분 감사

- GitHub main 최근 커밋을 재조회해 현재 기준 SHA가 `3aebf09e6786fa9ee451b027ed83756f37bd89b3`임을 확인했다.
- CEN-CENELEC 2026-11-19 공식 발표에서 EN 40000-1-1 및 EN 40000-1-2 발행을 확인했다. European Commission 2026-11-19 뉴스는 첫 CRA 지원 유럽표준이 2026-11-18 발행됐다고 설명한다. 표준별 표지상 개별 발행일은 별도 확인 전까지 미확정으로 둔다.
- EUR-Lex CRA Regulation Article 27(1) 원문을 재확인했다. 조화표준 참조가 OJ에 게재된 범위에서 적합성 추정이 발생한다.
- EN 40000-1-1/-1-2 및 EN 304 625를 대상으로 한 초기 검색에서는 CRA OJ 참조를 직접 확인하지 못했다. 검색 결과 없음은 OJ 미게재 확정이 아니므로 미확인으로 기록한다.
- 통합 보고서 §27, PROJECT_STATUS_CURRENT.md, README.md, MASTER_PLAN.md를 갱신하고 PROJECT_LOG.jsonl에 사건을 append한다.
- M/606 41개 전수감사는 미완료. 제품별 scope/classification/RDPS Unknown, security tests Not Run 유지.
- main.py, 운영 workflow, secrets, state/history, legacy SIL 3 자산 미변경.


## 2026-11-20 — PR #125 병합 및 exact-head CI 사후 확인

- PR #125 `docs(cra): record EN 40000 publication and M/606 OJ gate`를 exact head SHA `e940663da113dedcd8071f5781f1bcf78f449ccf`로 확인 후 squash merge했다.
- Merge SHA: `0a5f5140e323303d6a960ca73edd8ec8c05f55f2`; GitHub는 merged=true를 반환했다.
- Exact-head CI Run #1050 (run ID `44647390136`) 성공. Source blob identity, compile, CRA cross-matrix traceability, full pytest, live official CRA PDF/source read-only canaries 및 provenance manifest 업로드 성공. PDF evidence upload 단계는 skipped로 보고되었으며, 원본 PDF bytes 확보로 오인하지 않는다.
- Post-merge safety ref: `safety/post-merge-pr125-2026-11-20`; pre-work safety ref `safety/pre-m606-oj-audit-2026-11-20`.
- CEN-CENELEC 발표에서 EN 40000-1-1/-1-2 발행 확인. 추가 2차 추적 사이트는 CEN catalogue가 두 표준의 OJ citation을 기대하지 않는다고 표시한다고 보고한다. 이번 세션에서는 CEN catalogue 개별 레코드를 직접 열람하지 못했으므로, 잠정 2차 자료로만 관리하고 최종 OJ 판정은 CEN catalogue 및 EUR-Lex/OJ 직접 확인이 필요하다.
- 상황판, README, SESSION_LOG, PROJECT_LOG.jsonl을 PR #125 및 현재 main SHA 기준으로 동기화한다.
- M/606 41개 전수감사는 미완료. 제품별 scope/classification/RDPS Unknown, security tests Not Run 유지. main push CI는 별도 확인되지 않았다.

- 2026-11-20: PR #126 merged; exact-head Actions Run #1052 success; main SHA 9b61f1d9b177454c3530fa5339883e6434d01df3. Post-merge main read-back and safety refs completed. Official CEN-CENELEC publication of EN 40000-1-1/-1-2 confirmed; CEN individual catalogue citation field remains unverified; secondary tracker indication remains provisional. M/606 41-item OJ audit still open.

- 후속 1차 출처 검증: CEN 공식 카탈로그 개별 레코드 두 건에서 EN 40000-1-1(JT013095), EN 40000-1-2(JT013089) 모두 Published, DAV 2026-11-18, OJEU citation field “No citation expected for Directive 2024/2847” 직접 확인. 기존 잠정/미확인 표기는 종료하고 보고서 §28.4에 1차 근거 반영.

- M/606 41개 항목 1차 출처 대조: C(2026) 7861 final replacement Annex I의 항목번호·주제·ESO 기한을 기존 매트릭스와 41/41 비교. 기한 분포 2/13/26건(2026-11-30 / 2027-10-30 / 2027-01-31). Annex I에 EN/ETSI 번호와 OJ reference는 없으므로 actual standard mapping/OJ status는 별도 미완료. Article 2의 ESO 1개월 비수락 조건도 후속 검증으로 등록.


## 2026-11-20 — PR #128 병합 및 사후 검증
- PR #128 exact-head `25ad1721045d489d8d0ce2b8689511c7b5776e9d`, Actions Run #1060 success (전체 테스트·추적성·컴파일·공식 출처 canary/manifest 업로드).
- 사전 복구 브랜치 `safety/pre-pr128-merge-2026-11-20`; squash merge SHA `6733f37201117cb5744215d9deb337b0810acc49`; 사후 복구 브랜치 `safety/post-merge-pr128-2026-11-20`.
- main read-back 및 PR 병합상태 확인. 41개 Annex I 항목 감사대장 반영. `PROJECT_LOG.jsonl` 218줄 JSON parse 218 success / 0 invalid.
- main push CI Run #1061 (`44657049974`) success. 전체 단계 완료.
- 후속: JT013090 공식 카탈로그/OJ 필드, C(2026) 7861 Article 2 비수락 통지 확인.


## 2026-11-20 — M/606 Work Item 1차 출처 연결 및 Article 2 법률검토
- PR #129 merge SHA `da3cbc4b68ba92b8512f08740c02eefc415a616e`; PR #129 Run #1062 success, main push Run #1063 (`44657325405`) success. Pre/post safety refs 생성 완료.
- CEN/CENELEC M/606 Work Programme V1 (2025-04-02) pp.1–2: item 1 → JT013089 (Principles for cyber resilience); items 2–14 → JT013091 (Generic Security Requirements); item 15 → JT013090 (Vulnerability Handling).
- CEN-CENELEC 2026-02-23 webinar p.36: JT013090 = prEN 40000-1-3 Vulnerability handling. 2026-11-19 CEN-CENELEC announcement: FprEN 40000-1-3 publication forthcoming.
- 공식 카탈로그 JT013090의 최신 단계 및 OJ citation 필드는 직접 미확인. Formal Vote 19 Nov / citation expected는 secondary-only lead.
- C(2026) 7861 Article 2: 1개월은 각 ESO가 결정을 수령한 날부터 계산. ESO별 수령일 및 비수락 통지 원본 미확보. Recital (2)의 기존 C(2025)618 수락을 amendment acceptance로 오인하지 않음.
- 감사대장 1·2–14·15 Work Item 매핑 갱신. 41개 Annex I 행의 topic/deadline 검증과 41개 실제 EN/ETSI/OJ 전수확인은 별개임.


## 2026-11-20 — PR #130 병합 및 main CI
- PR #130 exact-head `accf11726771374f632bb66783ce0fefaf400daa`, Run #1064 success.
- Pre-merge safety ref `safety/pre-pr130-merge-2026-11-20`; squash merge SHA `bfcc2e61fc07b2148fca7a162349af40aa84bc47`; post-merge safety ref `safety/post-merge-pr130-2026-11-20`.
- main push Run #1065 (`44658780153`) success; full test suite, traceability, source canary and provenance manifest upload all passed.
- main JSONL 221/221 valid; audit CSV 41 data rows.
- 후속: OT/IACS 관련 M/606 Work Items와 서보드라이브 제품기능의 적용 경계 분석.

## 2026-11-20 — M/606 OT/IACS 6개 수직 프로파일 1차 출처 대조 및 서보드라이브 경계 분석

### 재개 기준
- main HEAD 36f170de199d2fc23e4e40969584e56c37dbebe7 (PR #131 이후).
- PR #130 merge bfcc2e61fc07b2148fca7a162349af40aa84bc47; main push Run #1065 (44658780153) success.
- 작업 브랜치 cra/ot-iacs-vertical-profile-boundary-2026-11-20; pre-work safety ref safety/pre-ot-iacs-vertical-audit-2026-11-20.

### 수행한 조사
- CEN-CENELEC CLC/TC 65X 공식 Work Programme의 여섯 프로젝트와 개별 CENELEC 프로젝트 레코드를 직접 확인했다.
- M/606 20b→prEN 50770-4 (81652, VPN), 21b→prEN 50770-2 (81650, network management), 22b→prEN 50770-6 (81654, SIEM), 25b→prEN 50770-3 (81651, physical/virtual interfaces), 27b→prEN 50770-5 (81653, routers/modems/switches), 36b→prEN 50770-1 (81649, firewalls/IDS/IPS).
- 6개 모두 Work Programme 상태 Under Drafting, 개별 프로젝트 상태 Committee stage. 각 레코드의 OJEU 필드는 Citation expected; 실제 OJ citation number/date와 DOR/DAV/DOA/DOP는 확인되지 않았다.
- CLC/TC 65X의 공식 scope는 산업 공정 계측·제어·자동화 장비·시스템 및 통합 구성요소/기능의 안전·보안 표준화다. 이것만으로 개별 서보드라이브가 여섯 수직 제품 유형에 속한다고 판단하지 않는다.
- 25b는 모델에 실제 OT 네트워크 인터페이스가 존재할 때 조건부 우선 검토 후보. VPN/NMS/SIEM/router-modem-switch/firewall-IDS-IPS 기능은 현재 확보된 LS메카피온 자료에서 확인되지 않았으나, 원본 매뉴얼 미확보 상태이므로 기능 없음으로 단정하지 않았다.

### 산출물 변경
- 통합 보고서 §31 및 버전 0.10 반영.
- M/606 41-item 감사 CSV의 행 20/21/22/25/27/36에 CENELEC project, 상태, OJ 필드, 제품 기능 경계 추가.
- 6개 수직 프로파일의 상세 6-row CSV 추가.
- PROJECT_STATUS_CURRENT, MASTER_PLAN, README, SESSION_LOG, PROJECT_LOG.jsonl 동기화.

### 검증 및 한계
- 공식 출처: CLC/TC 65X Work Programme, 여섯 개 개별 CENELEC 프로젝트 레코드, CEN-CENELEC Work Programme 2026 Digital Society 페이지.
- 작업 브랜치 변경사항은 아직 CI로 검증하지 않았다. PR 생성 전 diff/readback과 JSONL/CSV/추적성 검증을 수행하고 exact-head CI 결과를 별도 기록한다.
- 모델별 제품 기능, CRA scope/classification/Annex III·IV/RDPS는 Unknown; security tests Not Run.
- 운영 코드/workflow/secrets/state/history, legacy SIL 3 산출물은 변경하지 않았다.

## 2026-11-20 — PR #132 병합 및 exact-head CI 검증
- PR #132 exact head 15df2eae8b3a5eea809496e46a412f67f0f3576e; Run #1068 / ID 44660527456 success, 174 passed / 0 failed.
- Source blob integrity, compileall, CRA cross-matrix traceability, full pytest, official CRA PDF canary, 10-source HTML canary, provenance manifest JSON round-trip/upload 모두 성공.
- PDF artifact #14595995557 (3,070,503 bytes; ZIP SHA-256 2d3848ab2c7046b53154e3c304bee5dca5ad33bd23a00c4a5396b020922bb6ef), provenance artifact #14595062566 (2,567 bytes; ZIP SHA-256 657f92dd556ac2dc56ccb68278452a2e9f9422eeaec366098117c1ef52d47bc9). 둘 다 7일 보존.
- Pre-merge safety ref safety/pre-pr132-merge-2026-11-20; squash merge SHA f3a8fc06b2a0c5fdaa98d98ad8bc0f21abee22df; post-merge safety ref safety/post-merge-pr132-2026-11-20 생성 및 main과 identical 확인.
- main push CI는 연결된 도구 조회로 독립 확인하지 못했으므로 성공으로 기록하지 않는다.
- 보고서 §31 및 6-row matrix, 41-item audit CSV, PROJECT_STATUS_CURRENT, MASTER_PLAN, README, SESSION_LOG, PROJECT_LOG 동기화 완료.

## 2026-11-20 — PR #133 병합 및 사후 검증
- PR #133 exact head 466b3d93db6119c3a73c8cef6bc2e55cf698294d; Actions Run #1070 / ID 44660790965 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596185499 (3,070,503 bytes; SHA-256 5a84aeb59f8d960d80d611be7ee4b978d808e84b68255c489633fc94af84ca18); provenance artifact #14595641444 (2,567 bytes; SHA-256 81bcba6e53025759610218c9d66334710919510c1b8d623c7e880af72d9501d5).
- Pre-merge safety safety/pre-pr133-merge-2026-11-20; squash merge SHA a889b03855e3c7683aa140220352510ab4c4c116; post-merge safety safety/post-merge-pr133-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 별도 조회에서 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #134 병합 및 사후 검증
- PR #134 exact head 7a560c3d6db33f3d553f7fa9cd3596f9c7c6cd02; Actions Run #1072 / ID 44660976790 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14594883481 (3,070,503 bytes; SHA-256 b78ae81c852f64e47167ccccf05420d5480a086cb6a1888e0992c40d5a66e2d7); provenance artifact #14594828906 (2,567 bytes; SHA-256 73fca113ee234b576051b14454b8934c545742be616ecbef831cb020d15c849e).
- Pre-merge safety safety/pre-pr134-merge-2026-11-20; squash merge SHA 7162664b29554a01d2694cd027efb0191a6c3344; post-merge safety safety/post-merge-pr134-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 별도 조회에서 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — 제조사 공식 자료실 인벤토리 및 인터페이스 증거
- PR #135 exact-head Run #1074 / ID 44661159895 success, 174 passed / 0 failed; PDF/HTML canaries와 provenance artifact 업로드 성공.
- LS메카피온 공식 자료실에서 DriveCM 1.03.2, EtherCAT Drive ESI 0.98 및 0.96, PEGA2 Ver1.3, iX700M 400V Ver1.4, Step EtherCAT 기능 매뉴얼 등록정보를 확인.
- ESI 0.98은 L7NH/Pegasus/PHOX/L7NHF/L7N/GEM/SMT/L7MMT/iX7NH/iX7M/iX7MD 11개 모델을 열거. DriveCM 1.03.2 게시물은 L7P/L7NH/L7NHF/PEGA/PHOX/iX7NH/L7C/iX7M/PEGA2 지원과 PEGA2 EtherCAT/RS-485 신규 변형을 기재.
- 25b 기술 후보를 열거된 EtherCAT 모델 및 PEGA2 EtherCAT 변형에 대해 강화. ESI 목록과 DriveCM 지원목록은 동일하지 않으며, L7P 등은 ESI 0.98 목록만으로 EtherCAT 기능을 추정하지 않음.
- 공식 첨부 PDF/XML/MSI 원본 bytes 미확보, SHA-256 미계산, 본문 content review metadata-only. Step 카테고리 EtherCAT 매뉴얼은 Servo 제품군과 별도 유지.
- 통합 보고서 §32, 제조사 source inventory CSV, M/606 41-item audit row 25 및 6-profile matrix row 25b 갱신. Product classification Unknown, security tests Not Run.

## 2026-11-20 — PR #136 병합 및 사후 검증
- PR #136 exact head 25215700a415b094c6c187278183b8ca15e4e4ca; Run #1076 / ID 44661598986 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14595209202 (3,070,503 bytes; SHA-256 6356c21834522bcb9f90de5e903679d02b18ced0c49fe2287f7ae065a1b8e9ff); provenance artifact #14595972121 (2,567 bytes; SHA-256 752e408af313d26b37d184b22180aea597b57058fc65e6a4d9398b9019c6638e).
- Pre-merge safety safety/pre-pr136-merge-2026-11-20; squash merge SHA d7e921f5a6db04d20ce06778f6ea384dbd9c63fe; post-merge safety safety/post-merge-pr136-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — 모델별 통신 인터페이스 증거 대조
- PR #137 exact-head Run #1078 / ID 44661804214 success, 174 passed / 0 failed; official CRA source canaries/provenance upload success.
- LS메카피온 공식 드라이브 카탈로그에서 iX700M/iX7M/iX7NH/L7NHA/L7NHB/L7NHF EtherCAT 통신형, L7PA/L7PB/L7C/L7SA/L7SB pulse/analog 계열을 분리 확인.
- 공식 iX7NH Modbus TCP API 가이드 및 L7P Modbus RS-422 API 가이드 확인. iX7NH EtherCAT+Modbus TCP 동시지원/옵션은 미확정; L7P RS-422의 prEN 50770-3 범위 포함 여부도 Unknown.
- iX700MD1-B-150B CE DoC 등록정보와 모델코드 구조를 확인; CE DoC 본문은 미검토.
- 보고서 §33, 14행 model-interface matrix, manufacturer source inventory, M/606 item 25 및 25b 매트릭스 갱신. 원본 PDF/XML/MSI/API ZIP bytes 및 SHA-256 미확보, content review metadata-only.

## 2026-11-20 — PR #138 병합 및 사후 검증
- PR #138 exact head 0ca7cfb745884ba8c7a1f3f383974286d0e88fd8; Run #1080 / ID 44662266977 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14595309514 (3,070,503 bytes; SHA-256 bf73016cdd73cba8daab1c7108e5c469f4ac5bcfdd4648d43e9cc56d705f4f1e); provenance artifact #14595489037 (2,567 bytes; SHA-256 8175503c2935119183cd810fd287028b288d36e837af79608de56c64883b27c9).
- Pre-merge safety safety/pre-pr138-merge-2026-11-20; squash merge SHA 372860cfb1a149bc5d5a7bf993e11dbf68217478; post-merge safety safety/post-merge-pr138-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #139 병합 및 사후 검증
- PR #139 exact head 28086497e73f123aef28e695a56e455ed9cc092a; Run #1082 / ID 44662453390 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596455559 (3,070,502 bytes; SHA-256 c58dc3d7a47b43d323a626db8f390754dc7b4a6db8ee49b880510a15fd5f3327); provenance artifact #14596296397 (2,567 bytes; SHA-256 27132710326a210178372b9b0fb8ecc340b4b2c6e5b0f165eea705f574c4302c).
- Pre-merge safety safety/pre-pr139-merge-2026-11-20; squash merge SHA 7545a771ce16f362cf5b911cd8c850efc91c2e92; post-merge safety safety/post-merge-pr139-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #140 병합 및 사후 검증
- PR #140 exact head 1f859f5431917e8202ffdcaf7141376c8712eb8e; Run #1084 / ID 44662635778 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14595564027 (3,070,502 bytes; SHA-256 95dd3a2d6be26a27894175c4d73a94e26e883ff6a1253b2c99b8347cffbce4c6); provenance artifact #14595579119 (2,567 bytes; SHA-256 c52b41c5124c4593847c4136956b4863c7c0befc20726646517ab5caa689d935).
- Pre-merge safety safety/pre-pr140-merge-2026-11-20; squash merge SHA 2edae2463e04b5d4280aa9d04c48f7805b554707; post-merge safety safety/post-merge-pr140-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #141 병합 및 사후 검증
- PR #141 exact head 468eba3d10c9d76279dfa2f64c445b11db25d288; Run #1086 / ID 44662805428 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596955128 (3,070,501 bytes; SHA-256 257c1f95b42c6b4122386e2bc34bb1a2de6789ead07ac85e77b25c250c4311a0); provenance artifact #14595634151 (2,567 bytes; SHA-256 12ff89b7934e7fdf5d4cbc107d65e35acfe2bf755f65f29231922a5c872b0f78).
- Pre-merge safety safety/pre-pr141-merge-2026-11-20; squash merge SHA f798d9d16d74e399124c207c45ee6bdb6c1339a7; post-merge safety safety/post-merge-pr141-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #142 병합 및 사후 검증
- PR #142 exact head a7662c01f4c8f74790f4848a1d702ee22cb2d74a; Run #1088 / ID 44662991366 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14595914125 (3,070,503 bytes; SHA-256 91553fb5a43e6e30fdce54a04ccca0e2bf8198630d59417639a5a4a1e0b72197); provenance artifact #14597100049 (2,567 bytes; SHA-256 ae842c563c3bd0ba36f4f0a2fb2052a8556146486c2ea7cf18bb13f2f9666b6c).
- Pre-merge safety safety/pre-pr142-merge-2026-11-20; squash merge SHA 0c8144a59e0741eb9538af2e8493def6fe982f33; post-merge safety safety/post-merge-pr142-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #143 병합 및 사후 검증
- PR #143 exact head d0aef1b098d5b1f52e83f24b5d0eb9a37e98b34d; Run #1090 / ID 44663182762 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596188740 (3,070,503 bytes; SHA-256 2105504b4942f21db41a38eaca9b548e3a94a6696593238b3bf2cbf8e2b85c57); provenance artifact #14595554868 (2,567 bytes; SHA-256 c3f7cf7311772cfa4687cef25c13790d3e302a916c2c847badf0589fa0457c63).
- Pre-merge safety safety/pre-pr143-merge-2026-11-20; squash merge SHA f1157fb1b5581f55b1f192c15b1822386ce3ed1e; post-merge safety safety/post-merge-pr143-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #144 병합 및 사후 검증
- PR #144 exact head 09ac041dbb3df72e8c3cf3dd01e53bbc80d9ff7f; Run #1092 / ID 44663374900 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14597230119 (3,070,502 bytes; SHA-256 b8ff2c79732ee37e0bb625d84c66abf1026863bf229f85883ccc7b3d3036876b); provenance artifact #14596691436 (2,567 bytes; SHA-256 3640500172144d9754c6dffbf5fe46af153ee6928376ede0ce947291172e4a34).
- Pre-merge safety safety/pre-pr144-merge-2026-11-20; squash merge SHA c616169b4300521459cc3ae78d631fcd739103fb; post-merge safety safety/post-merge-pr144-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #145 병합 및 사후 검증
- PR #145 exact head dd536778451cb7629cf351480c41d9726b8e5365; Run #1094 / ID 44663593799 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596711210 (3,070,503 bytes; SHA-256 267ee572e7e36074114ffe259141268965cd79791f01f0b379d0ccc695a47741); provenance artifact #14596970810 (2,567 bytes; SHA-256 556d6304875a80d6ffe6da0dfe46f09b2011abb7f59545667b510f61b1f16ed9).
- Pre-merge safety safety/pre-pr145-merge-2026-11-20; squash merge SHA 482305a4d5334ef19105560d0b4a3bd012acc1d0; post-merge safety safety/post-merge-pr145-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #146 병합 및 사후 검증
- PR #146 exact head aed4a54883cdcacda59bad30f7b2a939b9b346b0; Run #1096 / ID 44663781793 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14597665057 (3,070,502 bytes; SHA-256 88940d8d171a9578b6475a52c1c967f737823dcef5b82c479556e82e856144bd); provenance artifact #14597380473 (2,567 bytes; SHA-256 35d45fee83dbf0c907a5ec980bb7ebc407c3a71a6f23063eb75527229f7228d7).
- Pre-merge safety safety/pre-pr146-merge-2026-11-20; squash merge SHA bd0938484b22b4d8c6d8ad94b440de2b479a0ea2; post-merge safety safety/post-merge-pr146-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #147 병합 및 사후 검증
- PR #147 exact head 789963424610a4369930bc1f841f30160378d50b; Run #1098 / ID 44663993153 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14597665320 (3,070,502 bytes; SHA-256 20974038626f21d9a54f888c0b4ddaf47eb6c0f76b42c1a006ab4689d1b5a3cd); provenance artifact #14596892018 (2,566 bytes; SHA-256 90c98687bcdc4eb8cdfb9692b1ed88fe6753d2d354be20ca364dfba554d387c4).
- Pre-merge safety safety/pre-pr147-merge-2026-11-20; squash merge SHA 51d75213e3e035dfc7a7858570844533644aedc5; post-merge safety safety/post-merge-pr147-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #148 병합 및 사후 검증
- PR #148 exact head 27a194485b7545a6c6e9c285b485822034e47815; Run #1100 / ID 44664187925 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14597670650 (3,070,504 bytes; SHA-256 cf2196ee53be64f58f1d2bc570a1ec7879fdfd13cd9e978bd1094d5b9b065e1b); provenance artifact #14597051830 (2,567 bytes; SHA-256 161343a0077a9057b01170a56e06f724b6a27842a28494d5ddfee64bdce64bf1).
- Pre-merge safety safety/pre-pr148-merge-2026-11-20; squash merge SHA 33d82ee31c151c4d2f19165f1c17882fc5dfe722; post-merge safety safety/post-merge-pr148-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #149 병합 및 사후 검증
- PR #149 exact head 0e872bcf989951a446bc8263e015d786a0e51ed0; Run #1102 / ID 44664418107 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596792806 (3,070,503 bytes; SHA-256 4f154be7978242c7ae1ae6e938fb3bc0190bb340fcf76aa2aa4560d31e50a958); provenance artifact #14596862640 (2,567 bytes; SHA-256 17bf9c8c04619deccf312406b9cc9ef005b72b4e6f668d78bd719d7540078f11).
- Pre-merge safety safety/pre-pr149-merge-2026-11-20; squash merge SHA 6e04cd691d637589af69437068befe623fd46312; post-merge safety safety/post-merge-pr149-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #150 병합 및 사후 검증
- PR #150 exact head 2c0dd8491a57d1cee9794fa6fb56e001f05bf193; Run #1104 / ID 44664625871 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF artifact #14596532979 (3,070,503 bytes; SHA-256 629255735141dd80f36c04b8fe0be97aa8b447966d558445051ed58156f7332c); provenance artifact #14597076911 (2,567 bytes; SHA-256 492975b4ac6d0c072e56b8c4d8a3b7a58a2ff7baec31af7fa73567cbe6fde92f).
- Pre-merge safety safety/pre-pr150-merge-2026-11-20; squash merge SHA 89659bc8dc718e8f090644b3aeb2de7c1ec363d1; post-merge safety safety/post-merge-pr150-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #151 병합 및 사후 검증
- PR #151 exact head 89aa425bc56fb7b3049ee10dc3effbb058b897d1; Run #1106 / ID 44664881039 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공. PDF artifact upload은 source content unchanged로 skipped.
- Provenance artifact #14597945822 (2,567 bytes; SHA-256 c50a3c3f3d459ea10de54a4a6682f0b55f35d3691da236610ac1743f7b84b37f).
- Pre-merge safety safety/pre-pr151-merge-2026-11-20; squash merge SHA 05d95d7760aacd1b608e85b583069507c0b4a369; post-merge safety safety/post-merge-pr151-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #152 병합 및 사후 검증
- PR #152 exact head 95e8b887d41b7e33aa988ad83166184bb523c28c; Run #1108 / ID 44665093443 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공. PDF artifact upload은 source content unchanged로 skipped.
- Provenance artifact #14597237413 (2,567 bytes; SHA-256 5c4d4e47614375696d429775da93bcbe8a0e130a1548a786650008e106ed212f).
- Pre-merge safety safety/pre-pr152-merge-2026-11-20; squash merge SHA 8f2fa6af11be627dc3926dc46a28eb70c1ec23a0; post-merge safety safety/post-merge-pr152-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #153 병합 및 사후 검증
- PR #153 exact head 84e73ec56fe375cfec52b584612d856475f5518d; Run #1110 / ID 44665312753 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공. PDF artifact upload은 source content unchanged로 skipped.
- Provenance artifact #14597622291 (2,567 bytes; SHA-256 c6446496947c8f1d615d19828b6e1a435b07f6774f26223234f444976261802b).
- Pre-merge safety safety/pre-pr153-merge-2026-11-20; squash merge SHA 61c432f7c310bb8bbbf2bd2c8143b5860926ee68; post-merge safety safety/post-merge-pr153-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #154 병합 및 사후 검증
- PR #154 exact head 0e60f078ab7bb91ec599f97b117315013a03f70c; Run #1112 / ID 44665540665 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공. PDF artifact upload은 source content unchanged로 skipped.
- Provenance artifact #14597173328 (2,567 bytes; SHA-256 2757b6776b78a089092c8af8997f7615fea68ea3c387b77564394ea64d18d6da).
- Pre-merge safety safety/pre-pr154-merge-2026-11-20; squash merge SHA 481d340050df4fd93689b992a374df3da2cfaa47; post-merge safety safety/post-merge-pr154-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.

## 2026-11-20 — PR #155 병합 및 사후 검증
- PR #155 exact head 19240925263c43c1f765463ad4e795f1767a2551; Run #1114 / ID 44665772110 success, 174 passed / 0 failed.
- Compile, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 성공. PDF artifact upload은 source content unchanged로 skipped.
- Provenance artifact #14597677644 (2,567 bytes; SHA-256 39c4c43327a6ecc2da82dd8adba0a2b99b4d7245e54ecfc410d56a017bacc9cd).
- Pre-merge safety safety/pre-pr155-merge-2026-11-20; squash merge SHA cd5976403f91c79beca845d8efd3f4e5f1930e23; post-merge safety safety/post-merge-pr155-2026-11-20 생성 및 main과 identical 확인.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.


## 2026-11-20 — 제조사 펌웨어·도구 자료 목록 추가 조사
- 공식 LS메카피온 소프트웨어 목록에서 DFU Downloader_Ver1.00.4 (2026-09-16), L7NH 특주 O/S (2026-08-31) 게시 항목을 확인했다.
- 공식 가이드북 목록에서 DriveCM V1.03.1 가이드 및 DriveCM 게인 튜닝 가이드(2026-09-08), iX7NH 교육자료(2026-09-14)를 확인했다.
- 상세 게시물/첨부파일의 원본 bytes와 SHA-256은 확보하지 못했다. 목록 메타데이터만 인벤토리에 기록했으며, 파일 내용·서명·보안 업데이트 기능을 검증한 것으로 취급하지 않는다.
- 보고서 §34에 CRA 업데이트 진위성·인증·권한·anti-rollback·복구·지원기간 검증 질문을 추가했다.
- 공식 소프트웨어/가이드북 목록: https://lsmecapion.com/bbs/board.php?bo_table=software&sca= / https://lsmecapion.com/bbs/board.php?bo_table=guidebook
- 다운로드 링크 열람 일부 실패. 후속 작업은 첨부파일 원본 확보와 SHA-256/서명/본문 검토를 우선한다.


## 2026-11-20 — PR #157 병합 및 사후 검증
- PR #157 exact head `5210f9f11f1898f3dc83173df7a1a352d889c696`; Run #1118 / ID `44678289573` success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance manifest upload 성공. PDF source artifact upload은 unchanged로 skipped.
- Provenance artifact #14602977168 (2,567 bytes; ZIP SHA-256 `aeb27bb37f157d6d3de8dcde48d4cfad56caae112ec4d5637a470eca325a4f17`).
- Pre-merge safety `safety/pre-pr157-merge-2026-11-20`; squash merge SHA `0ea0fba1fb37504f9d11b5c12d562c0d68f1d190`; post-merge safety `safety/post-merge-pr157-2026-11-20` 생성 및 main과 identical 확인.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run. Main push CI는 독립 확인되지 않아 미확인.


## 2026-11-20 — ESI·DriveCM·신형 모델 적용범위 교차검증
- 공식 ESI Ver0.98 게시물에서 게시일 2025-07-15, 3개 언어 XML 파일명/크기, 11개 적용 모델을 확인했다.
- DriveCM Ver1.03.2 게시물에서 지원 모델, .NET Framework 4.8 요구, 첨부 MSI/릴리스 노트, PEGA2 EtherCAT 및 RS-485 두 신규 변형, L7S/L7N 단종 제품의 LIVE i.C.E 사용 안내를 확인했다.
- PEGA2 Ver1.3 매뉴얼 첨부 메타데이터와 iX700M Ver1.4 매뉴얼 목록, iX700M 제품 카탈로그상 EtherCAT을 확인했다.
- ESI Ver0.98의 공개 적용목록에 PEGA2/iX700M이 없는 반면 DriveCM에는 PEGA2가 있어 적용범위 차이를 기록했다. 별도 ESI/컨트롤러 패키지 존재 가능성이 있어 비호환/부재를 단정하지 않는다.
- 첨부 원본 bytes·SHA-256은 다운로드 경로 오류/시간초과로 확보하지 못했다. 보고서 §35, 인벤토리 및 상황판에 반영.
- 출처: https://lsmecapion.com/bbs/board.php?bo_table=software&sca=Servo&wr_id=13005 ; https://lsmecapion.com/bbs/board.php?bo_table=software&wr_id=13110 ; https://lsmecapion.com/bbs/board.php?bo_table=manual&wr_id=12651 ; https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive


## 2026-11-20 — PR #159 병합 및 사후 검증
- PR #159 exact head `cc91056b674e54d80dfdd59f412b140caec4e6ed`; Actions Run #1122 / ID `44685551882` success.
- Source blob integrity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF and 10-source HTML canaries, provenance manifest upload success. PDF upload skipped as unchanged.
- CRA traceability summary: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, M/606 41, project log 250.
- Squash merge SHA `c43b35df267c30facbc8c8f62677e48189d24127`; pre safety `safety/pre-pr159-merge-2026-11-20`, post safety `safety/post-merge-pr159-2026-11-20` and post == main verified.
- Report §35/v0.14 and inventory 17 rows merged. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.


## 2026-11-20 — PR #160 병합 및 기준점 재확인
- PR #160 exact head `4f56e9b24354d25f03363127e8167a46049c5ded`; Actions Run #1124 / ID `44685715888` success, **174 passed / 0 failed**.
- Source blob identity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance manifest upload 통과. PDF 업로드 unchanged skipped.
- Provenance artifact #14606367087 (2,566 bytes; SHA-256 `57dba2ea061de40faec834b3794e102e414fa2f0e13a8fd72a0af2ede1447a80`).
- Squash merge SHA `8bc9762efbd20ca9c7aaaddc3832745d4e6dc53e`; pre/post safety refs 생성, post ref와 main identical 확인.
- PR #160은 PR #159 결과를 상황판·계획·README·세션/JSONL에 동기화한 문서 전용 PR이다.


## 2026-11-20 — PR #161 병합 및 사후 검증
- PR #161 exact head `66ed22f9ab16576b607fb70c898f71f82f860ea1`; Actions Run #1126 / ID `44690800297` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 252.
- Provenance artifact #14608053214, SHA-256 `758aded424447f0d6fb74729a699ac9f856fa403d128a1db04883d9afb48ff42`.
- Merge SHA `3e633d1b1b8312f5cb6665b44ee8a6fac43ee694`; pre/post safety refs 생성 및 post == main 확인.

## 2026-11-20 — iX7NH 펌웨어 업데이트 경로 및 인증정보 단서 조사
- LS ELECTRIC 공식 호스트의 iX7NH 매뉴얼 Ver1.1 텍스트를 검토하여 USB OTG, EtherCAT FoE, DriveCM USB, 내장 웹서버/Ethernet의 4개 업데이트 경로를 확인.
- 구판 매뉴얼에 FoE 업데이트 password '00000000', 웹서버 object 0x2420/0x2421의 기본 ID/PASSWORD 값과 RW 설정 가능성이 기재됨. 현행 Ver1.7에도 동일한지, 기본값 변경/기기별 고유성/암호화 여부는 미확인.
- 최신 공식 매뉴얼 Ver1.7 파일명·19.5MB·첨부일 2026-06-05 확인. 첨부 다운로드는 '잘못된 접근'으로 실패하여 최신 본문은 검토하지 못함.
- 보고서 §37 및 자료 인벤토리에 구판 본문 검토와 최신판 메타데이터를 분리해 기록. 기본 인증정보를 실제 취약점이나 현행 제품 상태로 단정하지 않음.


## 2026-11-20 — PR #162 병합 및 사후 검증
- PR #162 exact head `903fd90709636b37f2b4ebd1abec893555955a8e`; Actions Run #1128 / ID `44691140978` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 254.
- Provenance artifact #14609085450, SHA-256 `0407e5069a4f5d9698f6d9be994ffecbbc62c9dbae54b29b52cb96c39873cf4c`.
- Merge SHA `1d6110236984ee11387aaf2be99f239fa2f2ec1e`; pre/post safety refs 생성 및 post == main 확인.
- 보고서 v0.16 §37, 인벤토리 20개 데이터 행, JSONL 254건 반영.



## 2026-11-20 — PR #163 사후 상태 동기화
- PR #163 exact head `3d1f28acb57078c59bcb3d634674f8ac279358fd`; Actions Run #1130 / ID `44691317078` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 255.
- Provenance artifact #14609280243, SHA-256 `3bd36d529e45b20de019c783128a8f221bfd3debd895c65ddc640e11caf1f946`.
- Merge SHA `814cc6309e72461f0649b1b6d34109894cff4810`; pre/post safety refs 생성 및 post == main 확인.


## 2026-11-20 — PR #164 사후 상태 동기화
- PR #164 exact head `f0f7a51883bd66ad73f2252d8933067840c3d4c8`; Actions Run #1132 / ID `44691510530` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 256.
- Provenance artifact #14609395254, SHA-256 `da47c2cf1d99bca2b067fb4836e9a7b3320d435e05cd7cf1e7859ab6ee566e0b`.
- Merge SHA `77e3050558869cab2624880bb1d5bfe8a9d5685c`; pre/post safety refs 생성 및 post == main 확인.


## 2026-11-20 — iX7NH 통신·원격설정 공격면 조사
- LS ELECTRIC 공식 iX7NH Series PDF(문서 하단 2021.05) 본문을 확인: USB OTG 펌웨어 업데이트/파라미터 백업·복원/알람이력 백업, EtherCAT FoE, EoE/UDP 파라미터 설정·조정·복사, CoE/CiA402, Modbus TCP, 내장 웹서버 및 Ethernet 원격 시운전, STO1/STO2 입력 및 EDM 출력.
- 기능 존재와 보안 통제의 존재를 구분하여 USB OTG, FoE, EoE, Modbus TCP, 웹서버, 백업/복원, 로그별 검증 질문을 보고서 §38에 작성.
- STO 표기만으로 SIL/PL 인증·등급 또는 CRA 사이버보안 적합성을 확정하지 않는다. CE LVD/EMC 및 UL 목록 역시 CRA conformity evidence로 간주하지 않는다.
- 추가 listing-only 자료: iX7NH 표준 O/S 업데이트 가이드영상(2025-12-24), iX7NH 교육자료(2026-09-14), Modbus TCP API 가이드(2024-01-29; 일부 첨부 갱신 2026-01-20), CE LVD/EMC 및 UL certificate listings.
- iX7NH Ver1.7 첨부 다운로드는 제조사 페이지에서 '잘못된 접근'을 반환. 최신 본문, 업데이트 영상, API 코드 원본은 미검토 상태.
- 출처: https://sol.ls-electric.com/uploads/document/16389370233610/iX7NH%20Series_KR_202104.pdf ; https://lsmecapion.com/bbs/board.php?bo_table=software&page=2&sca=Servo ; https://lsmecapion.com/bbs/board.php?bo_table=guidebook ; https://lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE ; https://lsmecapion.com/bbs/board.php?bo_table=certificate&sca=UL



## 2026-11-20 — PR #166 병합 및 사후 검증
- PR #166 exact head `fa7120c73cbe6fe244319a8d1b1e7bc699b47259`; Actions Run #1136 / ID `44692817817` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 259.
- Provenance artifact #14609257372, SHA-256 `e23c851495214060b6749de728888f6b7ea662fa1bf0ced9b42eb1179427d851`.
- Merge SHA `761b3ccffc142f11cbfe0d0dfb0e905b5d368ecb`; pre/post safety refs 생성 및 post == main 확인.
- 보고서 v0.17 §38, 제조사 인벤토리 26행, JSONL 259건 반영.



## 2026-11-20 — PR #167 사후 상태 동기화
- PR #167 exact head `dace5c2b1c61e295e8aea6fef18d08fc4c09236d`; Actions Run #1138 / ID `44693025760` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 260.
- Provenance artifact #14609352656 SHA-256 `1c9f5f187223cb6d9b8b4780eedc04cb1739bc9433d153ed38abb309e7517c63`.
- Merge SHA `7f9c35c54f93505f541198f3ceef723540f4df72`; pre/post safety refs 생성 및 post == main 확인.
- GitHub branch API에서 main `protected=false` 확인. 서버 측 required checks 미강제 상태를 위험으로 기록; 현재 연결 도구는 보호 설정 변경 불가.


## 2026-11-20 — iX7NH Ver1.1 웹서버·Modbus TCP 원문 감사

### 수행
- LS ELECTRIC 공식 iX7NH Ver1.1 매뉴얼의 웹서버 제12장, Modbus TCP 제13장, 펌웨어 업데이트 제15장 추출 본문을 직접 검토.
- 웹서버 ID/PW Object 0x2420/0x2421, 로그인 및 웹 업데이트 흐름 확인.
- Modbus TCP Server의 EtherCAT IN 접속, 예시 TCP/502, Function Code 1/2/3/4/5/6/15/16 확인. 읽기/쓰기 기능을 구분하고 실제 위험 주소 범위는 추가 매핑 대상으로 남김.
- USB OTG/FoE/DriveCM/Webserver 업데이트 절차 및 구판 문서의 제한사항을 정리.
- 보고서 §39 추가, 제조사 인벤토리의 Ver1.1 매뉴얼 항목을 보강.

### 판단 및 제한
- Ver1.1은 역사적 매뉴얼이며 Ver1.7/현행 펌웨어 설정을 입증하지 않는다.
- 공개 저장소에는 구판 기본 인증정보의 정확한 문자열을 재게시하지 않는다.
- 문서상 HTTPS/TLS, 인증 강제, 서명/해시 검증, anti-rollback, 복구 기능을 확인하지 못했으나, 문서 미기재를 기능 부재로 해석하지 않는다.
- PDF 원본 bytes/SHA-256 미확보, 실기기·네트워크·자격증명 시험 미수행.
- 제품 CRA scope/classification/Annex III-IV/RDPS Unknown, security tests Not Run 유지.
- 운영 코드/workflow/secrets/state/history 및 SIL 3 보존 자료 미변경.

### 다음 단계
1. iX7NH Ver1.7 PDF 원본과 2025-12-24 업데이트 영상 확보.
2. Modbus TCP API PDF/ZIP 첨부 확보 및 코드·명령·쓰기 주소 검토.
3. 최신 SKU/펌웨어 기준 인증·권한·TLS·서명·anti-rollback·복구의 제조사 증거 확보.
4. PR exact-head CI 통과 후 main 병합, pre/post safety ref 및 main read-back 검증.


## 2026-11-20 — PR #170 병합 및 사후 검증

- PR #170 exact head `8af0834e56c8ec8cd4c13d900a5fe77c0b788424`; Actions Run #1142 / ID `44701241693` success.
- Full pytest **174 passed / 0 failed**; source integrity, compileall, CRA traceability, official CRA PDF/HTML canaries 및 provenance upload 통과.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional true, M/606 41, JSONL 262 events.
- Provenance artifact #14611894438, SHA-256 `0563c2493e7d19acf7e0cddee34c91e4c4b0339cfc696e52f8d27c79de373ad6`.
- Squash merge SHA `cad75135996c129bc576d83ce5b7ed968ca6a63b`.
- Pre-main ref `safety/pre-main-pr170-merge-2026-11-20`; post ref `safety/post-merge-pr170-2026-11-20`; post ref == main 확인.
- 보고서 v0.18 §39 및 제조사 인벤토리 26행 main 반영. 제품별 CRA scope/classification/Annex III-IV/RDPS Unknown, security tests Not Run 유지.
- 운영 코드/workflow/secrets/state/history 및 SIL 3 보존 자료 미변경.


## 2026-11-20 — PR #171 상태 동기화 병합 및 사후 검증

- PR #171 exact head `19d296c154115d47ef3b30be25c8700b53fa745f`; Run #1144 / ID `44701518420` success, **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional true, M/606 41, project log 263 events.
- Provenance artifact #14613405592, SHA-256 `f14e2ad608899ec53d999aa0dda87178fbf87494bdee4de9a7fb9f7477b74d27`.
- Squash merge SHA `a8db31bd2c7a1e0127ef226a432183633e66eb76`; pre-merge safety ref `safety/pre-pr171-merge-2026-11-20`; post ref `safety/post-merge-pr171-2026-11-20`; post ref == main 확인.
- PR #170 연구 산출물 v0.18 §39 및 인벤토리 26행 main 반영 상태 유지.
- 제품별 CRA scope/classification/Annex III-IV/RDPS Unknown, security tests Not Run 유지.


## 2026-11-20 — iX7NH Ver1.7·Modbus TCP API 공식 자료실 재감사

- 공식 Ver1.7 상세 게시물 확인: `iX7NH_KOR_Ver1.7_260605.pdf`, 19.5 MB, 게시물 작성 2021-05-14 / 첨부 표시 2026-06-05.
- 공식 API 가이드 게시물에서 테스트 가이드 PDF(1.3 MB), `iX7NH_TCP_API.zip`(69.8 MB), `x64.zip`(44.6 KB), `APIv1.02_20210505 1.pdf`(1.5 MB; 2026-01-20 표시) 확인.
- 공식 게시물 HTML은 확인했으나 첨부 다운로드 링크는 TimeoutError. 원본 바이트/SHA-256/본문/API 코드 미확보. metadata_only로 상태 유지.
- 보고서 v0.19 §40, 제조사 인벤토리 MANUAL-IX7NH-V1.7 및 GUIDE-IX7NH-MODBUS-TCP-API 레코드 업데이트.
- Ver1.1 기능을 Ver1.7에 전이하지 않으며 제품 CRA scope/classification/Annex III-IV/RDPS Unknown, security tests Not Run 유지.
- 다음 P0는 제조사 고객지원으로부터 원본/대체 다운로드 URL 확보 후 해시·개정·본문 비교.


## 2026-11-20 — iX7NH Modbus TCP 2026 보충 가이드 2차 자료 검토

- AutomationDirect `iX7NH Modbus TCP Communication Guide`, 1st Ed Rev B, 2026-05-05, 14 pages parsed text reviewed.
- 문서가 LS Electric User Manual을 대체하지 않는 보충 자료임을 명시하므로 제조사 1차 자료와 분리.
- Node 99는 Modbus TCP + built-in webserver, Node 98은 firmware >=1.15에서 Modbus TCP without webserver로 기술.
- 가이드는 내장 Modbus TCP communication timeout이 없다고 기술하며 PLC 측 상태 감시/통신 상실 시 SV_ON 제거를 권고. 500ms는 예시값이지 안전 반응시간이 아님.
- RW 제어 코일, Control Word 0x6040/Modbus 0x6001, Target Position 0x607A/0x6025, Procedure Command 0x2700/0x2701 및 JOG/Software Reset 등의 제어면을 확인.
- 제조사 Ver1.7/API 원본 다운로드는 TimeoutError로 미확보. 2차 가이드 내용의 현행 펌웨어/SKU 적용성은 미검증.
- 보고서 v0.20 §40–§41, 인벤토리 2차 자료 별도 행 추가. 실기기/네트워크/쓰기 시험 미수행.


## 2026-11-20 — PR #173 병합 및 사후 검증

- PR #173 exact head `2e536ed1cd893e433b0aab6b98185c40bff3ff8a`; Actions Run #1148 / ID `44702831239` success, **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional true, M/606 41, JSONL 266 events.
- Official source canary: 10 allowlisted sources fetched; one separate PDF empty-body response skipped as temporary outage; workflow success.
- Provenance artifact #14613259125, SHA-256 `22b402eeb9c351c65210a80c47d7f0deb6cc2526383138b12c2c96d892ca73c1`.
- Squash merge SHA `634c3178471ff20c99e97ba48fc4c5e187afb28d`; pre-work ref `safety/pre-ix7nh-v17-api-audit-2026-11-20`; post ref `safety/post-merge-pr173-2026-11-20`; post ref == main 확인.
- Report v0.20 §40–§41 and inventory 27 rows in main. Ver1.7/API official attachments still metadata_only; AutomationDirect guide is secondary evidence only.
- Product CRA scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run; no live device/network/write/motion tests.

## 2026-11-20 — PR #174 병합 및 사후 검증

- PR #174 exact head `779474728cb39501991dff7846b52a5bbae83ec4`; Actions Run #1150 / ID `44703086698` success.
- Full pytest **174 passed / 0 failed**; exact source integrity, compile, CRA cross-matrix traceability, live official HTML source canary and provenance manifest round-trip/upload passed.
- Official source canary fetched 10 allowlisted records; verified consolidated CRA Article 13(8) locator/quote and Implementing Regulation 2025/2392 Annex I category 10 / Annex II category 1 locators.
- CRA PDF source evidence upload step skipped; do not treat this as original PDF acquisition. Provenance artifact #14613952433, 2,567 bytes, SHA-256 `84a6cab72e1403f205d03151a9259a8ac101244d95fafdd3e87b5c5fca05b718`.
- Squash merge SHA `090c78bfa0edc759641a8dd30f9156038fa86a82`; main read-back and compare identical.
- Pre-merge safety ref `safety/pre-pr174-merge-2026-11-20`; post-merge safety ref `safety/post-merge-pr174-2026-11-20`.
- Ver1.7/API official attachment bytes/SHA-256 remain unavailable. AutomationDirect Modbus TCP guide remains secondary source only. Product CRA scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run.

## 2026-11-20 — PR #175 병합 및 최신 제조사 자료실 인덱스 조사

- PR #175 exact head `65f0a5f136e0a37797710f485dcdc478b9cf45b0`; Actions Run #1152 / ID `44707031513` success; full pytest **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC crosswalk 16, product evidence 15, bidirectional links true, M/606 41, JSONL 268 events.
- Official CRA HTML canary fetched 10 sources and verified Article 13(8), 2025/2392 Annex I(10)/Annex II(1); PDF evidence upload step skipped.
- Provenance artifact #14615596751, 2,567 bytes, SHA-256 `25c5c192aa96544b5e41c8cac6eeda0d629f3c95af6755e090be6d34ae506a70`.
- Squash merge SHA `850e2c851630239140e9a39d5f0978204b2ee025`; main read-back identical. Pre-merge safety ref `safety/pre-pr176-merge-2026-11-20`; post-merge ref `safety/post-merge-pr175-2026-11-20`.
- Official guidebook index: iX7NH training 2026-09-14; DriveCM V1.03.1 and gain-tuning guides 2026-09-08; PN8B+L7NH(iX7NH) CSV synchronous control and EtherCAT 0x211F external IO guides 2026-07-06. Metadata only; detailed attachments and bytes not acquired.
- Official drive catalogue lists iX7NH 100–120/200–240 V, 0.1–15 kW; product family range only, not an exact SKU.
- Report §42 and inventory snapshot row added. Product CRA scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run.


## 2026-11-20 — PR #176 병합 및 사후 검증

- PR #176 exact head `788d5aea88d12a7bdb1087d264173ac0f487caf8`; Actions Run #1154 / ID `44707491717` success, full pytest **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional true, M/606 41, JSONL 269 events.
- Official source canary fetched 10 sources; Article 13(8), Implementing Regulation 2025/2392 Annex I(10)/Annex II(1) locators verified. PDF evidence upload skipped.
- Provenance artifact #14614954168, 2,567 bytes, SHA-256 `067e43ccfc1c5b438f719489dc44f3e2ead4e152a2294d2c9b5031ca6bc192dd`.
- Squash merge SHA `8f19a8b9fcf8e4582a9470e5483ff08019d1711f`; main read-back identical. Pre/post safety refs retained.
- Report v0.21 §42 and inventory 28 rows in main. New guidebook index entries are metadata-only; detailed attachments and bytes not acquired.
- Product CRA scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run.

## 2026-11-20 — CRA 핵심 이행 최신정보 재검증 및 정확성 관리 강화

### 수행
- main SHA `07d6d3b1d8f91637da7b6a9a023b2f4ec64e7efd` 및 열린 PR 없음 확인.
- 기존 CRA 통합 보고서가 2026-11-17 기준 v0.2였고 README 상단 재개 문구가 PR #173에 머물러 있음을 확인. 이는 최신성/관리 문서 불일치로 기록.
- Commission reporting page (2026-09-11), implementation page (2026-07-27), Commission FAQ v1.4 (2026-09-04), ENISA SRP FAQ (2026-10-15), Glossary v1.6 (2026-10-21), AR User Manual v1.3 (2026-11-04) 공식 페이지/본문 재조회.
- ENISA SRP 운영상 API 미제공, 영어 UI, Article 15 미구현, 장애 복구 후 SRP 제출, 72h 카운터 불일치 가능성, AEV final counter 미구현, Primary/Secondary AR 및 EU Login MFA, EUVD/CVE 후속을 보고서 §25 및 운영 기준서에 기록.
- 보고서 v0.3 및 freshness register, AI_RULEBOOK §59 업데이트를 작업 브랜치에 반영.

### 검증 한계
- ENISA FAQ/Glossary는 HTML parsed text; raw bytes/SHA-256 미확보.
- AR User Manual은 v1.3/2026-11-04 page metadata만 확인; PDF 원본 본문/bytes/hash 미검토.
- ENISA SRP Status endpoint 열람 실패; live platform login/submit 테스트 미실시.
- CI 성공은 법률적 100% 정확성이나 제품 적합성 판정을 뜻하지 않음.

### 다음 단계
- Commission/ENISA 공식 동적 페이지와 OJ/CEN/CLC/ETSI 상태를 주기적으로 재확인.
- M/606 41개 actual standard mapping/OJ 상태 및 C(2026) 7861 Article 2 acceptance notice 조사 지속.
- 제품별 CRA scope/classification/RDPS Unknown, security tests Not Run 유지.

## 2026-11-20 — CRA 핵심 표준화 최신상태 확인
- CEN-CENELEC 2026-11-19 공지 및 CEN 개별 레코드 직접 확인: EN 40000-1-1:2026 (JT013095), EN 40000-1-2:2026 (JT013089) Published, DAV 2026-11-18. 두 레코드 모두 CRA Directive 2024/2847에 대해 “No citation expected”; Article 27 presumption 근거로 사용하지 않음.
- ETSI Work Programme Version 2.3.3은 M/606 active 18 items를 표시. 조회 목록은 10개만 노출하므로 18개 전수 상세 검토를 완료했다고 주장하지 않음.
- EN 304 625 개별 레코드 최신 상태는 Comments categorisation assessed (2026-11-05); 2026-11-19 remark에 EC second assessment received in batches dated 2026-09-28 and 2026-11-16. 이전 2026-09-28 “7 VR” 상태는 outdated.
- EN 304 620 VPN, EN 304 621 NMS, EN 304 622 SIEM, EN 304 627 router/modem/switch scope에 industrial OT domain exclusion 확인. CENELEC prEN 50770 OT work items와 별도 관리.
- 제품 적용성 경계: drive port/feature만으로 Annex III Class I product category를 자동 분류하지 않음. OJ actual citation은 개별 record에서 미확인.
- 신규 보고서 §26 및 ETSI/CEN 상태보고서 addendum 반영.
- 한계: CEN prEN50770-1~6 20 Nov 재열람 미완료, ETSI 18개 중 미검토 8개, 표준 본문 미취득.

## 2026-11-20 — ETSI EN 304 620 추가 최신상태 정정
- 2026-11-20 ETSI direct record for EN 304 620 shows Comments categorisation assessed (2026-11-06), v1.0.0; 2026-11-19 remark says EC second assessment received for comment batches dated 2026-09-28 and 2026-10-22.
- 기존 2026-09-28 “7 VR – EC assessment before EV received”는 현재 상태가 아니므로 보고서 §26 및 ETSI 상태 addendum에서 수정.
- ETSI EN 304 620/621/622/627 scope에 industrial OT domain exclusion을 개별 record에서 확인; 각 OJ field는 비어 있음.

## 2026-11-20 — EU 표준화 법체계 제안 및 M/606 개정 근거 확인
- Commission CRA standardisation page last update 2026-11-12 states M/606 amended on 2026-11-10, extending all vertical and some horizontal ESO delivery deadlines by 3 months.
- Commission Register C(2026)7861 final (Brussels 2026-11-10) and Annex source record checked. Conflicting 2026-11-11 secondary tracker statement was not adopted is superseded by later official Commission page/document evidence.
- COM(2026)780 proposal (2026-10-06) to repeal/replace Regulation 1025/2012 recorded as proposal only, not current law.
- Commission Harmonised Standards index accessed 2026-11-20; page explains OJ publication requirement and currently lists no CRA entry. Cross-check against OJ/Article 27 maintained.
- Integrated report v0.5 §27–§28 and source freshness register updated.

## 2026-11-20 — PR #178 CRA 핵심 이행·표준화 업데이트 병합

- PR #178 exact head `21b11774933e9b3a6c67922eddbb6bbb907439d4`; squash merge SHA `8abf70a68add7f0e7a38283da3dd3d78c160829c`.
- Actions Run #1158 / ID `44709421086`: success; full pytest **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC crosswalk 16, product evidence 15, bidirectional links true, M/606 mapping 41, JSONL 274 events (269 modern IDs + 5 legacy).
- Official source canary fetched 10 allowlisted sources; CRA Article 13(8) and 2025/2392 Annex I(10)/Annex II(1) locators passed. PDF evidence upload step skipped.
- Provenance artifact #14616666445, 2,567 bytes, SHA-256 `77061f3b46331afb3ce9c1f8b60ce116754f4f4bb6c817ccdc8af1f4fa58ab54`.
- Merge SHA readback identical to main; pre-work safety ref `safety/pre-cra-core-implementation-refresh-2026-11-20`; post-merge ref `safety/post-merge-pr178-2026-11-20`.
- CRA report v0.5 §§25–28, SRP readiness, 21-source freshness register, CEN/ETSI corrections, rulebook freshness requirements all main.
- Evidence limits retained: ENISA HTML parsed/no raw hash, AR Manual metadata only, ETSI 18 items list only shows 10 with 8 detailed records pending, CEN prEN50770-1..6 not fully re-read, standard full text not acquired.
- Product scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run.


## 2026-11-20 — AI 세션 연속성·자기검토·토큰 효율 기준 보강

### 수행
- 저장소/브랜치 상태를 재조회하고, 과거 기록의 `cra-project-foundation`이 현재 활성 기준이 아님을 확인.
- `PROJECT_STATUS.md`는 역사 기록이며 `PROJECT_STATUS_CURRENT.md`가 최신 재개 기준임을 확인.
- CRA 전체 프로젝트 우선순위를 재확인하고 LS메카피온/iX7NH는 사례연구로 유지.
- 신규 기준서 `reports/AI_SESSION_CONTINUITY_SELF_REVIEW_AND_TOKEN_EFFICIENCY_2026-11-20.md` 작성.
- `AI_RULEBOOK.md`에 실시간 브랜치 재확인, 오류/개선 기록, 독립 검증, 토큰 효율, read-back 규칙 추가.
- `MASTER_PLAN.md`에 운영 품질 개선 트랙 및 다음 CRA P0 게이트 추가.

### 자체 오류·교훈
- 이전 세션 요약의 오래된 브랜치명을 현재 브랜치처럼 취급하면 재개 기준을 잘못 잡을 수 있다. 앞으로 과거 branch/commit을 신뢰하지 않고 매 세션 GitHub에서 HEAD/branch/PR/CI를 재조회한다.
- 오래된 `PROJECT_STATUS.md`와 `PROJECT_STATUS_CURRENT.md`의 역할을 혼동하지 않는다.
- 사례연구의 세부 작업이 CRA 전체 법령·표준화·OJ 핵심 트랙을 가리지 않도록 우선순위를 명시한다.
- 모델 자체가 재귀 학습하는 것처럼 표현하지 않는다. GitHub 문서·검증·규칙·테스트를 통한 외부화된 개선 루프라고 정확히 설명한다.

### 검증 및 한계
- 문서 변경은 작업 브랜치에서 수행. 운영 코드, workflow, secrets, state/history 및 SIL 3 보존 자료는 변경하지 않음.
- 이번 세션에서는 CRA 최신 외부 원문을 새로 전수 검증하지 않았다. 관리 체계 보강을 CRA 법적 사실 최신화로 표현하지 않는다.
- 저장 후 동일 브랜치 read-back과 PR exact-head CI는 다음 단계에서 확인한다.


## 2026-11-20 — PR #180 병합 및 AI 운영 기준 사후 검증

- PR #180 squash merge SHA `3ded54116b3ecfa77645c50ada45575fbe656aea`; Exact-head Run #1162 success; source integrity/compile/traceability/full pytest **174 passed / 0 failed**.
- Official CRA HTML source canary 및 provenance manifest upload success. CRA Guidance PDF canary returned empty body; PDF upload skipped, no PDF evidence claimed.
- Pre/post safety refs: `safety/pre-merge-pr180-ai-self-review-2026-11-20`, `safety/post-merge-pr180-ai-self-review-2026-11-20`.
- Four documentation files and 140 insertions merged: AI_RULEBOOK, MASTER_PLAN, SESSION_LOG, new AI continuity/self-review/token-efficiency standard.
- Main merge post-ref and project status synchronization are being recorded in this documentation-only PR.
- CRA regulatory research remains separate; PR #180 does not mean current CRA law/standards or product conformity have been revalidated.


## 2026-11-20 — ETSI 8개 상세 감사 및 CLC/TC 65X OT 표준 정합성

- ETSI Work Programme v2.3.3 M/606 active list에서 기존 미검토 8개 EN 304 617–624 상세 레코드를 개별 열람. scope, version, status, next milestone, Harmonised Standard metadata, OJ field를 CSV로 기록.
- EN 304 620/621/622 scope에서 industrial OT exclusion 확인. 8개 record의 OJ field는 비어 있어 Article 27 presumption은 주장하지 않음.
- CLC/TC 65X OT profile에서 prEN 50770-1이 1-1 firewalls와 1-2 IDS/IPS로 분할된 사실을 DKE Oct-2026 national tracker에서 확인. 기존 6개 표기를 7개 deliverable로 정정.
- DKE Drafting prEN, BSI -2/-3 PWI/target dates unknown, LVS In development 간 status discrepancy 발견. Central CENELEC record는 이번 pass에서 재열람 실패; stage/forecast Unknown/Conflict 유지.
- C(2026)7861 Annex I deadline group 확인: 1/15 2026-11-30; 2–14 2027-10-30; 16–41 2027-01-31. Article 2 one-month non-acceptance condition은 ESO receipt date 기준. ESO별 receipt/notice evidence 미확보.
- ETSI calendar에 GoSRSReq006-M/606 AMD 1 examination meeting 2026-11-23 예정 확인; 11/20 현재 회의 결과 아님.
- 통합 보고서 v0.6, ETSI/CEN audit, 2 CSV 및 M/606 41-item row36 mapping 갱신.
- 한계: Commission Register 원본 PDF bytes/hash 미취득. Article2/Annex text는 Commission certified-copy stamp가 있는 제3자 호스팅 PDF copy에서 읽고 Commission official page와 대조. CENELEC central record 및 ESO receipt/acceptance 미검증.
- 제품별 CRA classification Unknown; physical/security testing Not Run.


## 2026-11-20 — CENELEC 81649 central record 추가 직접 확인

- CENELEC central project 81649를 다시 열어 parent prEN 50770-1, combined firewall+IDS/IPS scope, Committee stage, Citation expected, DOR/DAV 미기재 확인.
- DKE Oct-2026의 -1-1/-1-2 split과 central parent record가 일치하지 않음을 기록. split child project IDs는 확정하지 않음.
- 81650–81654 central records는 이번 pass에서 direct readback 실패. -2/-3 DKE/BSI conflict, -4/-5/-6 historical central snapshot status를 구분.
- CSV와 integrated report §32, CEN audit addendum, situation board, plan, README, session log, AI rulebook에 반영.


## 2026-11-20 — Annex III/IV core functionality 및 Article 32 route matrix

- EUR-Lex CRA consolidated text 및 Commission Implementing Regulation (EU) 2025/2392 공식 OJ PDF를 대조.
- Article 2(1) scope, Article 7(1) core functionality/integrated component boundary, Annex III/IV technical descriptions, Article 32(1)–(4) conformity routes를 정리.
- Fieldbus controllers/adapters가 Annex III Class I network-interface category 기술 설명에 포함됨을 확인. 내장 포트와 별도 판매 interface module을 분리 분석하도록 기준화.
- Security MCU, RTOS, NMS/VPN/SIEM, router/switch, firewall/IDS/IPS, Annex IV security box/secure element에 대한 product boundary 및 evidence checklist 작성.
- Article 13(5)/(6) third-party component due diligence 및 component vulnerability handling 연결.
- 제품별 Annex III/IV classification 및 conformity route는 exact SKU/BOM/FW/market configuration evidence 부족으로 Unknown 유지.


## 2026-11-20 — PR #182 병합 및 CRA 제품분류 분석 사후 검증

- PR #182 squash merge SHA 904b2ed0897331ced9dedfcbd25afd608f92f951; exact-head Run #1177 success; 174 passed / 0 failed.
- Source blob integrity, compile, CRA traceability, full pytest, official HTML source canary, provenance manifest upload passed. Traceability counts: 13 claims, 15 interfaces, 35 requirements, 36 SEC, 16 EVD-SEC, 41 M/606 mappings, 279 project log events; bidirectional links true.
- CRA Guidance PDF canary returned empty body; skipped explicitly. Main push CI was not separately verified through the available connector.
- PR #182 merged the ETSI 8-item audit, OT 7-deliverable reconciliation, C(2026)7861 Article2/Annex I deadline condition, and Annex III/IV + Article32 legal product-boundary matrix.
- Product-level Annex III/IV classification and Article32 route remain Unknown pending exact SKU/BOM/FW/marketed component evidence; security tests Not Run.
- Pre/post safety refs: safety/pre-merge-pr182-cra-standardization-classification-2026-11-20; safety/post-merge-pr182-cra-standardization-classification-2026-11-20.


## 2026-11-20 — ETSI M/606 18개 통합 및 Class I/II metadata mismatch

- ETSI Work Programme v2.3.3 active 18개 개별 record를 통합 matrix로 구성: 17개 Annex I vertical topics 17–27/31–36 및 추가 telecom support item EN304642.
- EN304635 hypervisors 및 EN304636 firewalls/IDS/IPS의 ETSI scope text가 Class I로 표시되지만 Regulation 2025/2392는 각각 Class II category1/2로 분류함을 발견. 법령이 우선하며 Article32(3) route 적용 대상임을 기록.
- Normative draft bytes는 미취득이므로 오류 범위는 ETSI Work Programme metadata/scope text로 한정. 실제 draft 본문 오류라고 단정하지 않음.
- EN304627 routers/modems/switches의 industrial OT exclusion도 확인. OT exclusions 4개로 통합.
- 18개 HEN metadata Yes / OJ field blank; actual OJ citation 미확인.
- 신규 18-item master report/CSV, integrated report v0.8, Annex III/IV legal report, status/plan/README/session/project log/AI rulebook 갱신.


## 2026-11-20 — ETSI 18개 matrix 저장 및 문서 인덱스 정합성

- ETSI 18개 active work item master report/CSV 생성 및 README index 추가.
- EN304635/636 Work Programme class label과 Regulation 2025/2392 legal class 간 mismatch를 status/plan/rulebook/integrated report에 기록.
- README project title와 조사 산출물 진입점 readback 확인.
- 후속: EN304635/636 normative draft 원문 취득, metadata-only 여부 확인, ETSI correction tracking.


## 2026-11-20 — EN304635/636 공개 interim draft 대조

- ETSI DocBox 공개 interim draft EN304636 V0.0.9 (2025-12-15) 확보. Introduction/Scope에서 Annex III Class II point 2를 명시해 법령과 일치함을 확인.
- EN304635 V0.0.8 (2025-11-10) 확보. 추출된 본문에서 Annex III/Class I/Class II label을 찾지 못함.
- 따라서 Work Item page metadata의 Class I 표기는 discrepancy로 유지하되, 실제 normative draft의 오류라고 단정하지 않도록 정정. 최신 v1.0.0/v1.0.1 draft는 아직 미취득.


## 2026-11-20 — 최신 EN304636 V1.0.0 draft 검증

- ETSI DocBox directory listing에서 최신 EN304636 V1.0.0 (2026-07-09) PDF 확인 및 열람.
- PDF page 9 Introduction이 firewalls/IDS/IPS를 Annex III Class II point 2로 명시. 최신 공개 draft는 법령과 일치하며 Work Item page의 Class I label이 stale metadata임을 확인.
- EN304635 V1.0.1 (2026-06-24)은 DocBox에 존재하지만 fetch timeout. 이전 V0.0.8은 class label 미포함; 최신 본문은 미확인.


## 2026-11-20 — CSV 무결성 자체검토 및 복구

- M/606 41-item CSV의 row 35/36 수정 과정에서 단일 행 parser를 전체 CSV parser처럼 사용해 두 행의 열 구조가 손상된 것을 readback/roundtrip 검사에서 발견.
- 손상본을 기준으로 덮어쓰지 않고, 손상 직전 커밋 85a03faefa87b024ebf378a629cca00d0f4d46d5의 정상 CSV를 복원 기준으로 사용한 뒤 Class II/draft 검증 메모를 재적용.
- 복구 후 전체 CSV를 RFC4180-style quote-aware parser로 재검증: header+41 data rows = 42 rows, 모든 row 10 columns. row35/36 원래 필드와 기존 CLC mapping 보존 확인.
- 재발 방지: CSV 수정 시 항상 전체 파일 parse → row/column count → serialize → reparse roundtrip을 수행하고, 단일-line parsing과 full-file parsing 함수를 구분한다.


## 2026-11-20 — PR #184 자체검토 및 상태 문서 동기화

- PR #184 head eba04e6d1b71c4024cb03ac4a909fd9734e0c121; PR-triggered Isolated Python Tests run #1197 completed success.
- 재검토에서 matrix/integrated report/Annex III legal report/status/plan/README 간 최신 EN304636 V1.0.0 사실과 이전 초안 상태가 일부 불일치한 점 발견. 최신 EN304636 V1.0.0 Class II 표기를 기준으로 통합하고, EN304635 V1.0.1은 DocBox 등록·fetch timeout·본문 미검증으로 통일.
- Integrated report version label duplicate text, README stale v0.7 link, status/plan stale “latest drafts not acquired” statements identified for correction.
- AI_RULEBOOK section 18 added: session resume, source-first self-review, persisted error/root-cause/recovery/prevention loop, structured-file validation, token/tool efficiency, branch/safety/CI discipline.
- Safety snapshot branch: safety/pre-pr184-doc-reconciliation-2026-11-20 (from PR head before cleanup).


## 2026-11-20 — EN304635 V1.0.1 latest draft sample resolves legal class

- ETSI DocBox latest EN304635 V1.0.1 PDF fetch timed out, but iTeh publicly indexed 15-page sample preview for the exact ETSI title/version.
- Sample PDF document p.15 Scope explicitly says the product is in CRA Annex III Class II point 1 and cites Commission Implementing Regulation (EU) 2025/2392. This resolves the latest-version class text question; it aligns with law.
- Limitation: preview is 15 pages of a 386-page draft; full original not obtained. EN304636 V1.0.0 full public draft had already been inspected at document p.9 for Class II point 2.
- Conclusion: both latest public drafts align with law; ETSI Work Item page Class I scope labels are stale/incorrect metadata. Corrected matrix, CSV, legal report and status accordingly.


## 2026-11-20 — PR #184 exact-head CI Run #1223 success / next ETSI meeting source

- Exact head `7d9d300a017bfc6d68b247b3a5de56c8a744e1c8` CI Run #1223 completed success: 174 passed / 0 failed.
- Source blob identity, compile, CRA traceability, live official CRA PDF canary, live official CRA HTML canary and provenance manifest upload all succeeded; PDF artifact upload step was skipped because the workflow's source artifact condition was empty, not because the tests failed.
- ETSI official portal calendar lists `GoSRSReq006-M/606 AMD 1 - examination meeting` on 2026-11-23. Calendar listing proves scheduled event only; agenda, decision, minutes and ESO acceptance remain pending.
- Next: monitor meeting output; do not infer an AMD1 amendment or acceptance before official decision/receipt evidence.


## 2026-11-20 — CENELEC official WG3 mapping cross-check

- CENELEC CLC/TC65X WG3 official presentation dated 2026-05-07 explicitly maps M/606 topics to WIIDs/prEN deliverables: 36b→81649/prEN 50770-1; 21b→81650/-2; 25b→81651/-3; 20b→81652/-4; 27b→81653/-5; 22b→81654/-6.
- DKE October 2026 national tracker corroborates all seven deliverables at Start NWI and Drafting prEN, with 81649 split into -1-1 firewall and -1-2 IDS/IPS.
- Mapping is now source-verified; individual central CENELEC stages/DOR/DAV for 81650–81654 and 81649 parent/child record synchronization remain open. No OJ citation inferred.
- Updated integrated report §38, OT reconciliation report §5, status, plan and project log.


## 2026-11-20 — PR #184 latest exact-head CI Run #1234

- Final documentation head before merge: `a391c039837a1219591dead58d962013dee788b1`.
- Run #1234 / 44718762561 completed success: 174 passed / 0 failed.
- Source blob identities, compile, CRA cross-matrix traceability, official CRA PDF and HTML read-only canaries, and provenance manifest upload all succeeded. CRA PDF evidence upload step was skipped by workflow condition; no test failure.
- Branch was advanced afterward only to persist this CI result in the status board/logs; a fresh exact-head CI run is required before merge.


## 2026-11-20 — PR #184 squash merge 및 post-merge readback

- PR #184 merged to main via squash: `9dbe6e92c358d0361f9640651152e4d1e8b1ec6b`.
- Final exact-head CI Run #1238 on `3dc3af115769ef2380a8895d41b0eced04b67fff`: success, 174 passed / 0 failed; official CRA PDF/HTML canaries and provenance upload succeeded.
- Created `safety/pre-merge-pr184-2026-11-20` from pre-merge main and `safety/post-merge-pr184-2026-11-20` from merge SHA. Post-merge safety ref compares identical to main (0 ahead/0 behind).
- Main readback verified README, status board, AI_RULEBOOK, 18-item matrix (18 rows), integrated report §38, OT mapping report, and PROJECT_LOG (290 valid JSONL events).
- Self-review found README's temporary “PR #184 open” banner had become stale after merge; this follow-up branch corrects README and updates status board with the merge SHA and safety refs.


## 2026-11-20 — README merge-banner no-op 발견 및 재발방지

- PR #185 post-merge readback에서 README 첫 배너가 여전히 “PR #184 is open”이라고 표시됨을 발견했다. 이전 수정은 실제 문자열이 아닌 다른 CI-run 문구를 대상으로 `replace()`하여 no-op이 발생했지만 commit 자체는 정상 생성되었다.
- 원인: 치환 대상 문자열을 최신 파일 readback으로 확인하지 않고 이전 대화 상태에서 추정했다. 저장 성공을 내용 수정 성공으로 오인했다.
- 복구: README 정확한 3번째 줄을 readback한 뒤 해당 줄 전체를 병합 완료 상태로 교체. AI_RULEBOOK에 no-op 치환 탐지, 기대 문구 횟수 확인, 저장 후 readback 규칙 추가.
- 교훈: update_file commit 성공은 파일 변경의 의미적 성공을 보증하지 않는다. 매 수정 후 정확한 파일 readback과 기대 문자열 검증을 수행한다.


## 2026-11-20 — PR185/186 follow-up merge chain and final situation-board sync

- PR #185 merged via squash as `ebc6fda0f2a89be0e5306a00fb12ac7b0d2802bf`; exact-head CI #1240 success, 174 passed / 0 failed.
- PR #186 merged via squash as `8adf72f3bbda24165479f7aa4d4246d48e4acd99`; exact-head CI #1242 success, 174 passed / 0 failed. It corrected README's stale PR #184 open banner and added the no-op replacement guard to AI_RULEBOOK.
- `safety/post-merge-pr185-2026-11-20` and `safety/post-merge-pr186-2026-11-20` each read back identical to main at their respective merge points; latest PR186 safety ref is identical to current main.
- Final main SHA updated to `8adf72f3bbda24165479f7aa4d4246d48e4acd99`; this branch synchronizes the situation board and logs the follow-up merge chain.

## 2026-11-20 — 운영 자동화 주기·실행 품질 감사 및 관측성 개선

### 수행
- `.github/workflows/run.yml` 확인: 실제 schedule은 `0 */3 * * *`(UTC 3시간 간격), 5분 주기가 아님.
- GitHub schedule event 최근 26건의 job conclusion은 모두 success. 과거 오래된 실패 이력은 최근 실행과 구분.
- 최근 3개 production job 로그를 직접 열어 실제 실행 결과를 분리 확인.
  - Run #2522: 공식 source 10개 확보, Gemini 3.8 Flash 503, 3.5 Flash Lite fallback, 신규 주제 없음, 아카이브/Discord 변경 없음.
  - Run #2521: 조사 보류, 원격 main 동시 변경으로 no-op.
  - Run #2520: 조사 보류, 운영 데이터 변경 없음.
- Actions success가 신규 CRA 보고서 생성 완료를 뜻하지 않는 관측성 문제 확인.
- 개선 브랜치 `fix/automation-outcome-visibility-2026-11-20` 생성. 3시간 간격은 유지하되 정각 부하 회피를 위해 cron minute를 :00에서 :17로 이동하는 변경을 PR에 포함. main.py·secrets·외부 호출 빈도는 변경하지 않고 결과 분류/요약 추가.
- 최근 26개 schedule run created_at을 예정 슬롯과 비교: 평균 59분, 중앙값 58분, 범위 49~71분 지연. Run #2523은 기존 12:00 UTC cron 슬롯보다 약 63분 늦은 13:03 UTC에 생성. GitHub 공식 문서는 정각 고부하 시 지연/누락 가능성을 안내하므로 :17 offset을 적용하되, 지연 제거를 보장하지 않음.

### 변경
- `scripts/automation_outcome_summary.py`: 실행 로그를 보수적으로 분류해 GitHub Step Summary 출력.
- `tests/test_automation_outcome_summary.py`: 8개 fixture case.
- `.github/workflows/run.yml`: main.py output tee, 원래 exit code 보존, always summary step 추가.
- `reports/CRA_AUTOMATION_CADENCE_AND_OUTCOME_OBSERVABILITY_AUDIT_2026-11-20.md`.

### 판단
- 5분마다 Gemini production workflow를 돌리면 일 최대 288회 호출 시도, quota/비용/중복/queue/동시성 위험이 커진다. 현 3시간 간격 유지.
- 5분 상태 확인이 실제 요구라면 Gemini/Discord/운영 데이터 쓰기 없는 별도 read-only heartbeat로 분리해야 한다.
- ChatGPT 예약 작업은 주간 CRA·MCU 공식자료 점검만 enabled; 일일 Git 통합 점검 및 보고서 대기열 점검은 disabled. 5분 task는 확인되지 않음.

### 검증 경계 및 다음 단계
- CI 실행 전. 테스트 통과·PR 병합·main 반영 주장 금지.
- PR exact-head CI → diff/safety 검토 → 다음 production schedule에서 summary가 실제 결과를 정확히 분류하는지 확인.
- workflow 변경은 summary/로그 수집만 추가하며 cron, secrets, Gemini/Discord 실행 빈도, checkpoint 및 operational guard를 바꾸지 않음.


### 후속 CI 결과 — PR #189
- Exact-head Run #1247 / ID `44741088582` success; pytest **182 passed / 0 failed**.
- Source blob identity, compileall, CRA cross-matrix traceability, official CRA PDF/HTML canaries, provenance manifest upload 성공.
- PDF source artifact upload은 unchanged 조건으로 skipped. 실제 production workflow dispatch/Gemini/Discord 호출은 하지 않음.
- CI는 테스트 브랜치에서 summary classifier를 검증한 결과이며 main 배포 또는 다음 production run에서의 실제 summary 검증은 아직 아님.


### 스케줄 조정 후 재검증 상태
- 운영 cadence는 3시간으로 유지하고 cron minute만 UTC :00 → :17로 변경. 호출 빈도·Gemini/Discord 요청 수는 늘리지 않음.
- 최초 PR HEAD Run #1247: 182 passed / 0 failed. 이후 workflow cron 및 관리 문서가 변경되었으므로 최신 HEAD에 대한 CI 재실행을 기다림. 최초 CI를 최신 HEAD 검증으로 오인하지 않음.


### 자동화 cadence 테스트 회귀 정정
- PR #189 중간 HEAD Run #1262 실패: **181 passed / 1 failed**.
- 유일한 실패는 기존 `tests/test_production_workflow_cadence.py`가 옛 cron 문자열 `0 */3 * * *`를 고정 assert한 테스트였다. 실제 3시간 cadence를 검증하는 테스트가 offset 변경과 동기화되지 않은 상태.
- 작업 브랜치에서 기대 cron을 `17 */3 * * *`로 수정. 실패를 숨기거나 xfail 처리하지 않았다. 최신 HEAD CI로 재검증 예정.


### PR #189 code HEAD CI 결과
- code HEAD `2b3522b1a95256901636afae8ee1af92e68bc35a`, Run #1271 / ID `44741902473`: success, 전체 pytest **182 passed / 0 failed**.
- Source blob identity, compileall, CRA traceability, official PDF/HTML canaries, provenance manifest upload 성공.
- 이후 문서 전용 갱신으로 HEAD가 바뀌어 최신 HEAD 확인은 별도 CI를 기준으로 함. main 미병합.


### Production Run #2523 사후 로그 검증 및 폴백 분류 보강
- Run #2523 / ID `44740952326` success; 약 7분 41초 실행.
- 공식 source gate 10개. Gemini 3.8 Flash 응답은 EUR-Lex 공식 링크 누락으로 quality validation reject, 3.5 Flash Lite 대체 모델로 전환.
- 대체 모델은 신규 주제 없음으로 종료. archive/Discord/state 변경 없음. operational guard 및 checkpoint pruning 성공.
- 기존 classifier는 503/429 로그가 없으면 quality rejection으로 인한 대체 모델 전환을 놓칠 수 있었음. 두 개 이상 모델 시도를 폴백으로 탐지하고 사유를 분류하도록 수정; 9번째 fixture test 추가.
- Run #1271의 182 passed는 새 fixture 추가 전 결과. 최신 HEAD CI 재실행 대기.


### PR #189 최신 CI 및 테스트 fixture 최종 정정
- Run #1282: 181 passed / 2 failed. 원인은 fallback fixture의 실제 대체 모델 로그 누락과 quality-fallback fixture의 newline 이중 escape.
- 실제 production log (#2523)의 두 모델 시도/품질 거절 문구를 재현하도록 테스트 fixture를 정정. xfail/skip 처리하지 않음.
- 최신 HEAD `0238f456d3c3087a91e5b94b8b649d0cd39c3634`, Run #1285 / ID `44742487474`: success, **183 passed / 0 failed**.
- Source blob identity, compileall, CRA traceability, official PDF/HTML canaries, provenance manifest upload 성공. PDF evidence upload은 unchanged/condition skipped.
- PR #189 main 미병합. merge 후 다음 :17 scheduled production run에서 Step Summary 실제 분류 확인 필요.


## 2026-11-20 — PR #189 자동화 관측성 개선 병합 및 사후 검증

### 병합
- PR #189 squash merge: `1683b5ec780c7396309d85b86cba100a021194e4`; main read-back 동일.
- Pre-merge safety ref `safety/pre-merge-pr189-automation-observability-2026-11-20`; post-merge safety ref `safety/post-merge-pr189-automation-observability-2026-11-20`. 두 ref 모두 merge point main SHA와 동일 확인.
- Exact PR HEAD Run #1289 success, 183 passed / 0 failed. Main push Run #1290 / ID `44742940672` success, 183 passed / 0 failed; source identity, compileall, CRA traceability, official PDF/HTML canaries, provenance manifest upload success. PDF evidence upload skipped by unchanged condition.

### 운영 변경
- 기존 `0 */3 * * *` → `17 */3 * * *`. 3시간 cadence와 API 호출량은 그대로이며 UTC 정각 부하를 회피하도록 minute offset만 변경.
- main.py output tee, 원래 exit code 보존, Actions Step Summary에 조사 결과 분류/모델 폴백 사유/source count/archive/Discord 상태 기록.
- main.py, secrets, Gemini/Discord 호출 횟수, checkpoint/guard/pruning 로직은 변경하지 않음.
- Production Run #2523 실제 결과: 공식 source 10개, Gemini 3.8 Flash는 EUR-Lex 링크 누락으로 품질 거절, 3.5 Flash Lite 대체 모델, 신규 주제 없음, archive/Discord 변경 없음; guard/pruning success.

### 남은 검증
- 최근 26회 schedule run은 job success이나 예정 슬롯 대비 평균 59분(중앙값 58분, 범위 49~71분) 지연. :17 offset은 위험 완화이지 정시 보장이 아님.
- 첫 post-merge scheduled run 예상 슬롯 2026-11-20 15:17 UTC / 2026-11-21 00:17 KST. 실제 실행에서 Actions Summary가 quality-based fallback 및 NO_NEW_TOPIC을 올바르게 분류하는지 확인해야 함.
- 5분 production Gemini run은 설정하지 않음. 필요 시 read-only heartbeat 별도 설계.


## 2026-11-21 — EN 304 635 live status correction and Run #2526 post-merge verification

### 수행 및 검증
- Production schedule Run #2526 / ID 44825006768, head main 5be75068b7413e39bd1b2509d65e715d96907ae5, job success. 10 official sources 확보.
- Gemini 3.8 Flash 503 후 Gemini 3.5 Flash Lite로 전환했으나, 대체 모델 응답에 CRA 공식 EUR-Lex 원문 링크가 없어 quality gate에서 거절. 조사 보류(DEFERRED), 보고서/원격 archive/Discord 변경 없음. operational guard no-op, checkpoint pruning success.
- run start 2026-11-20 21:58:47 UTC; expected :17 UTC slot 대비 약 41m47s 지연. cadence 3시간, no five-minute production loop.
- Summary step completed/success. Jobs API는 GITHUB_STEP_SUMMARY 본문을 반환하지 않으므로 원시 로그와 classifier logic로 DEFERRED 판정; 렌더링 summary text를 직접 read-back했다고 주장하지 않음.

### CRA 원문 조사 — EN 304 635
- ETSI live Work Programme query result 및 Work Item Monitoring은 DEN/CYBER-EUS-0016 / EN 304 635 V1.0.9, status EC assessment before WNV requested (2026-11-19), next EC assessment before WNV received (2026-11-28)로 표시.
- 2026-11-20 remark: V1.0.9 새 draft 업로드, Draft Review after PE, Enquiry 및 EC HAS2 comments 해결을 포함한 CYBER-EUSR 승인 버전.
- cached individual Work Item page는 V1.0.1 / 2026-09-17 상태를 유지. live query/Monitoring과 충돌하므로 stale cache issue로 기록.
- 공식 free download area는 V1.0.1 (2026-06), 2,700,830 bytes만 노출. V1.0.9 full draft bytes/hash/page count는 미확보.
- ETSI calendar의 GoSRSReq006-M/606 AMD 1 examination meeting은 2026-11-23 예정. 회의 전 단계이므로 minutes/decision을 추정하지 않는다.
- 법적 class: EN 304 635 범주의 hypervisors/container runtime systems는 Regulation 2024/2847 Annex III Class II point 1 및 Implementing Regulation 2025/2392 Annex I에 따라 Class II. ETSI Work Item scope의 Class I 표현은 법령을 대체하지 않는다.

### 다음 작업
1. V1.0.9 공식 PDF/원문 확보 가능성 확인 후 bytes, SHA-256, page count, version metadata 보존.
2. V1.0.1과 V1.0.9 차이점 및 Enquiry/EC HAS2 comment resolution 변경 분석.
3. 11/23 M/606 AMD 1 회의 후 공식 minutes/decision, ESO 수령·수락·비수락 증거 추적.
4. M/606 18개 Work Item live status와 41개 Annex I topic → EN/ETSI/OJ citation matrix 갱신.


## 2026-11-21 — AI 행동 자기검토 및 개선 선별 기준 정비

### 확인한 상태
- main SHA `c813b7d6b48890b87c099d5a3f7c322170c3baf3` 확인. PR #191 merge 후 main CI Run #1294 / ID `44838660060` success, 183 passed / 0 failed.
- AI_RULEBOOK에는 이미 세션 연속성/자기검토 기준이 있었으나, 후행 섹션 번호가 기존 1~59와 중복되어 11~19, 14 등이 재사용되고 있었음.
- EN 304 635 관련 후행 규칙이 V1.0.1 sample preview를 'latest publicly viewable draft'로 표현해 2026-11-21 live Work Programme의 V1.0.9와 혼동될 여지가 있었음. V1.0.9 full PDF는 미확보 상태.

### 반영 내용
- 후행 규칙 번호를 60~71로 재정렬.
- Section 69에서 V1.0.1 sample을 역사적 증거로 한정하고, V1.0.9 본문/페이지/hash는 미확보라고 명시.
- Section 71 및 세션 운영 문서 §8에 대화 단위 결과 검토, AI 행동 점검, 개선 선별(A~D 반영 수준), 효과 검증 원칙을 추가.
- 이번 반영은 문서 운영 기준 정비이며, 장기 효과는 아직 미검증으로 남김.

### 다음 확인
1. PR exact-head CI 및 main CI에서 전체 테스트/traceability/source canary 확인.
2. 다음 대화부터 결과 대비 요청, 근거·검증, AI의 오류·비효율을 선택적으로 점검하고 유효한 개선만 반영.
3. 다음 ETSI 조회에서 V1.0.9 full draft official route를 재탐색하되, 검색 목록과 실제 PDF 취득을 구분.


## 2026-11-21 — KST 일일 재귀개선 모방 알고리즘 정립

### 관찰/요구
- 사용자는 날짜가 바뀔 때 최신 검증된 재귀개선 구조를 GitHub에 적용하고, 재귀개선 모방 알고리즘도 갱신하도록 요청.
- 직전 세션의 자기검토 기준은 있었으나, KST 날짜 경계 트리거, 일일 검토 파이프라인, 효과 상태, NO_CHANGE 처리, 자동화 한계가 단일 프로토콜로 정리되어 있지 않았음.

### 조치
- `AI_RECURSIVE_IMPROVEMENT_PROTOCOL.md` 신규 작성: 날짜 경계 감지, 기준 상태 동기화, 결과/행동 감사, 후보 평가, A~D 반영, 검증/복구, 효과 상태, 토큰 효율 가드.
- AI_RULEBOOK §72, 세션 운영 문서 §9, MASTER_PLAN 및 PROJECT_STATUS_CURRENT에 기준선과 재개 절차 반영.
- 기준일은 2026-11-21 KST. 다음 날짜 경계에서 세션 시작/재개 시 실제 실행하도록 정의.
- 별도 자동 스케줄러/백그라운드 감시/모델 가중치 재학습은 구현하지 않았으며, 이를 구현했다고 주장하지 않도록 명시.

### 검증
- PR #192 main post-merge CI Run 44839652639: success. Source integrity, compile, CRA traceability, full pytest, official CRA PDF/HTML read-only canaries, provenance upload 통과.
- 이번 신규 알고리즘 자체의 테스트 및 read-back/PR CI는 이번 작업 브랜치에서 별도 검증 예정.
- 장기 운영 효과는 다음 KST 날짜 경계 이후 관찰 전까지 미검증.


## 2026-11-22 — CRA 보고서의 전문성과 비전문 독자 이해도 동시 보강

### 사용자 요구
- 보고서는 회사용 전문 문서로 작성하되, 사용자가 중학교 2학년 수준의 배경지식으로도 읽고 이해할 수 있어야 함.
- 읽는 순서와 원리·작동 메커니즘을 상세히 설명하고, 쉽게 설명한다는 이유로 전문 내용·법률 조건·예외를 생략하지 말 것.

### 현황 감사
- 기존 통합 보고서 v0.9에는 CRA 적용범위, 의무, 신고, 표준화, 제품 분류, 증거·추적 분석이 광범위하게 포함되어 있었음.
- 그러나 법률·기술 용어가 초반부터 밀집되어 있고, 독자별 읽는 순서, 일반 서보 드라이브 작동 원리, 초심자용 핵심 용어·상태 해설이 전면에 체계화되어 있지 않았음. 따라서 '내용의 전문성'은 높지만 사용자가 요구한 '이해 가능성'까지 충족했다고 볼 수 없음.

### 변경
- 통합 보고서 v0.10 서두에 보고서 목적/독자/읽는 순서, 일반 서보 드라이브 작동 원리(명령→비교→제어 계산→전력 변환→피드백→설정/진단/업데이트), CRA 적용 판단 흐름, 핵심 용어집, 상태 표시, 회사 부서별 활용 방법 추가.
- `REPORT_WRITING_STANDARD_CRA.md` 신규: 각 주제를 결론→쉬운 설명→정확한 전문 설명→작동/판단 원리→제품 적용→회사 조치→증거/검증→한계 순서로 작성하도록 규정.
- AI_RULEBOOK §73, README, PROJECT_STATUS_CURRENT, MASTER_PLAN 갱신.
- 일반적인 서보 작동 원리와 특정 LS메카피온 제품의 확인 사실을 구분하고, 정확한 모델 자료가 없는 판정은 Unknown 유지.

### 잔여 과제
- 이번 작업은 보고서 진입 안내와 작성 기준 정립이다. §1~§10 및 심층 부속서 전체의 상세 설명 보강은 계속 진행해야 함.
- 실제 중학생 수준의 비전문 독자 검토 및 전문가 법률·기술 검토를 별도로 수행해야 함.


## 2026-11-22 — 통합 CRA 보고서 §1~§4 설명 계층 확장
- 보고서 v0.11로 갱신. §1의 10개 결론을 항목별로 해설하고, §2의 법령·개정법령·Commission Guidance·표준·OJ·제품 증거의 효력/확인 순서를 설명.
- §3에 EtherCAT 디지털 데이터 교환, 아날로그 지령, USB 설정, MCU, 별도 보안 게이트웨이, 필수 클라우드에 대한 가상 사례를 추가. 각 사례에서 결론 가능한 범위와 추가 증거를 분리.
- §4에 발효일, 부분 적용일, Article 14 적용일, 일반 적용일, 전환 규정의 차이를 단계별로 설명.
- 실제 LS메카피온 제품 사실로 오인되지 않도록 가상 예시임을 명시. 기존 법적 결론과 Unknown 경계는 유지.


## 2026-11-23 — ST MCU 통합 제품의 CRA 분류 및 M/606 AMD 1 일정 재확인

### 조사
- EUR-Lex의 Regulation (EU) 2024/2847 및 Implementing Regulation (EU) 2025/2392를 대조해 Article 7(1), Annex III Class I category 14, 2025/2392 전문 (1)~(2)의 제품 전체 핵심 기능 원칙을 정리.
- ST MCU를 사용한다는 사실만으로 서보 드라이브 완제품이 category 14로 자동 분류되지 않는다는 판단 경계를 문서화. MCU 보안 기능은 부품 수준 사실과 완제품 위험평가/설계 증거로 별도 검토.
- ETSI 공식 캘린더에서 GoSRSReq006-M/606 AMD 1 examination meeting이 2026-11-23 Online 일정으로 게시된 사실을 재확인. 회의 결과·ESO 수락은 공개 일정으로 입증되지 않아 Unknown 유지.

### 산출물
- `reports/CRA_ST_MCU_INTEGRATION_AND_M606_FOLLOWUP_2026-11-23.md` 신규 작성.
- 제품 증거 요청 항목: ST 전체 order code, security feature/활성화 상태, secure boot·키관리·debug 정책, LS메카피온 정확한 SKU/HW/FW/BOM 및 통신 구조.

### 한계와 다음 작업
- ST MCU 정확한 부품번호, LS메카피온 모델별 BOM/FW/회로도는 미확보. 특정 MCU의 category 14 해당 여부 및 완제품 Annex III/IV·Article 32 경로는 확정하지 않음.
- 회의 후 공식 minutes/decision, M/606 AMD 1 최종 문서, ESO receipt/acceptance/non-acceptance evidence를 확인.
- 문서 변경은 CRA 조사 메모와 진행 기록에 한정. 운영 코드, workflow, secrets, Gemini/Discord 호출 빈도는 변경하지 않음.


### 검증 오류 및 복구 기록 — 2026-11-23
- PR #196 최초 CI Run #1303에서 CRA traceability가 PROJECT_LOG.jsonl line 309의 빈 행으로 실패했고, pytest 및 후속 canary는 실행되지 않음.
- 원인: JSONL 파일이 이미 개행으로 끝나는 상태에서 새 레코드 앞에 추가 개행을 한 번 더 넣음. 사전 검사는 빈 행을 필터링한 뒤 JSON 파싱하여 이 결함을 놓침.
- 복구: 기존 이벤트는 보존하고 이번 세션 이벤트만 1개 유지했으며, 파일 중간 빈 행/JSON 오류가 없는지 전 행 재검증. 현재 309 records, invalid JSON 0, interior blank line 0, 신규 event ID 1개.
- 재발 방지: JSONL append 전 마지막 문자의 개행 여부를 확인하고, 빈 행을 허용하지 않는 전체 파일 파서를 실행한 후 CI를 재실행한다.
- 상태: 최초 CI 실패는 숨기지 않고 기록. 수정된 HEAD의 재실행 결과 확인 전까지 CI 통과로 간주하지 않음.
 
## 2026-11-23 — 통합 보고서 v0.12 §5~§10 설명 보강 및 M/606 후속 확인

### 변경
- 사용자 요구에 따라 기업용 전문 문서의 기술·법률 깊이를 유지하면서 비전문 독자도 이해할 수 있도록 통합 보고서 v0.12를 작성.
- §5~§10에 실무 해설 추가: 제조사 의무를 제품 생애주기/부서별 역할로 연결, Article 14 신고 접수·최초 인지시각·triage 흐름, 표준 초안/Work Item/OJ citation 구분, CRA와 기계류 규정의 위험·증거 경계, SKU/HW/FW 단위 증거 추적, 단계별 완료 게이트.
- §39~§42에 §5~§10 통합 해설, M/606 회의 상태, ST MCU Category 14 증거 분리, PR #196 CI 결과 기록.
- 보고서 기준일 2026-11-23, 버전 v0.12.

### 새로 확인한 사실과 한계
- ETSI 공식 회의 캘린더는 GoSRSReq006-M/606 AMD 1 examination meeting을 2026-11-23 Online으로 표시. 일정 게시만 확인했으며 실제 개최/결과/표결/ESO 수락 여부는 공개 1차 증거를 확보하지 못함. Unknown 유지.
- PR #196 exact-head Run #1308 / 45094691796 success: source integrity, compile, CRA traceability, full pytest, official CRA PDF/HTML canaries, PDF evidence and provenance uploads 모두 성공.
- Run #1307은 JSONL 중간 빈 행으로 CRA traceability 단계 실패. 빈 행/중복 이벤트를 수정한 뒤 Run #1308 전체 성공. 최초 실패는 숨기지 않고 유지.
- ST MCU 전체 order code와 LS메카피온 정확한 SKU/HW/FW/BOM은 미확보. Category 14/Annex III·IV/Article 32 제품별 결론은 Unknown.

### 다음 작업
1. M/606 공식 minutes/contribution/decision 및 ESO receipt/acceptance/non-acceptance 확인.
2. ST 전체 주문 코드와 security feature/configuration 원문 확보.
3. LS메카피온 모델별 SKU/HW/FW/BOM/매뉴얼/통신 구조 확보.
4. §5~§10 비전문 독자 검토 및 CRA 법률·제품 기술 전문가 교차검토.
5. 문서 변경은 PR #196에 유지하고 exact-head/main CI와 merge read-back 전에는 병합 완료로 기록하지 않는다.


## 2026-11-23 — PR #196 병합 사후 기록
- PR #196을 exact-head CI Run #1312 success 확인 후 squash merge. Merge SHA e82683964413ca2c5922477e9755c62ae7b21064.
- PR CI는 source integrity, compile, CRA traceability, full pytest, PDF/HTML canary, provenance upload 성공. PDF evidence upload는 skipped로 기록.
- main read-back으로 보고서 v0.12, §39~§42, ST MCU/M/606 follow-up note 확인. JSONL 310개 유효 레코드, 내부 빈 행 0.
- pre/post merge safety refs 생성. main push CI는 현재 조회되지 않으므로 PR exact-head 성공과 혼동하지 않고 후속 확인.



## 2026-11-23 — PR #197 병합 및 M/606 개정 결정 원문 확인

### PR #197 사후 검증
- 이전 PR #197 exact-head Run ID 45095286445의 첫 attempt는 dependency install 도중 cancelled. 원인을 확인한 뒤 해당 job만 재실행했다.
- 재실행 결과 exact-head Run 45095286445 success: source integrity, compile, CRA traceability, 전체 pytest, official CRA PDF/HTML canary, provenance manifest 업로드 성공. PDF evidence upload 단계는 skipped.
- PR #197 squash merge SHA: b69710cf1eb3c17c1e99fc2ecd57e86c23053fde.
- main read-back에서 PROJECT_LOG.jsonl 311 records, invalid JSON 0, interior blank lines 0 확인. Post-merge safety ref 생성.
- PR exact-head CI success를 main push CI success로 간주하지 않는다. merge SHA의 main push workflow는 별도 확인 대상.

### M/606 법령 1차 출처 업데이트
- Commission Implementing Decision C(2026) 7861 final (2026-11-10) 본문 및 Annex I를 Commission document register에서 직접 확인.
- 변경 기한: 항목 1·15=2026-11-30, 16~41=2027-01-31, 2~14=2027-10-30.
- Article 2: CEN/CENELEC/ETSI가 해당 개정사항 수령 후 1개월 내 비수락을 통지하면 개정 결정은 적용 중단되고 C(2025)618의 2025-02-03 버전이 계속 적용된다. 각 ESO 수령일 및 비수락 통지 여부는 Unknown 유지.
- M/606 ESO 채택 기한과 OJ 인용/CRA Article 27 적합성 추정을 분리한다. CRA Regulation 자체의 적용일은 변경되지 않음.
- 보고서 v0.13 §43에 원문·기한표·조건·제품 영향·증거 한계를 추가.

### 다음 작업
1. ESO별 receipt/비수락 통지 및 11월 23일 ETSI 회의 결과 1차 증거 확보.
2. 개정 Annex I 기준 41개 항목의 마스터 매트릭스 기한을 재검증·동기화.
3. ST MCU 전체 order code/보안기능/활성화 증거와 LS메카피온 모델별 SKU/HW/FW/BOM 확보.
4. 보고서 §1~§10을 비전문 독자 관점에서 읽고 법률·기술 전문가 교차검토를 위한 쟁점 목록을 정리.


## 2026-11-23 — PR #196/#197 main push CI 사후 확인

- GitHub Actions를 merge SHA 기준으로 조회해 PR #196 main push Run #1313 / ID 45095198162 success 확인.
- PR #197 main push Run #1317 / ID 45104679354 success 확인.
- 두 실행 모두 source integrity, compile, CRA traceability, 전체 pytest, official CRA PDF/HTML canary, provenance manifest upload 성공.
- PDF evidence upload은 두 실행 모두 skipped. 따라서 PDF 원문 파일을 새로 확보한 것으로 기록하지 않는다.
- PR exact-head 검증과 main push 검증을 별도 항목으로 유지한다.


## 2026-11-23 — PR #198 병합 및 M/606 매트릭스 반영

- PR #198은 exact head d67423bde5c3cbc5dc6f9601e28a1cf494a46d4d에서 Run #1324 / ID 45105031988 전체 성공 확인 후 squash merge.
- Merge SHA: 447fd178fc0068c7616444485d75e639d9edc8f2.
- 동일 head의 Run #1325 / ID 45105052195는 cancelled. 별도 성공 실행 #1324와 혼동하지 않음.
- main read-back: 보고서 v0.13 §43, M/606 matrix Markdown/CSV, JSONL 314 records, invalid 0, interior blank 0.
- safety ref: safety/post-merge-pr198-2026-11-23.
- main push Run #1326 / ID 45114580241은 in_progress 시점 기록. 최종 결론은 후속 확인.

- PR #198 merge SHA의 main push Run #1326 / ID 45114580241 최종 success 확인. Source integrity, compile, CRA traceability, full pytest, PDF/HTML canary, PDF evidence upload, provenance manifest upload 모두 success. PR exact-head Run #1324의 PDF upload skipped와 구분한다.



## 2026-11-23 — PR #204 제품 증거 등록부 검토 및 M/606 회의 후속 재조회

### 기준 상태
- main 기준 commit: 584a7c092ea434d52f7794452ca85b0cbe981210.
- 열린 PR #204 브랜치: research/cra-lsmecapion-product-evidence-2026-11-23; main 대비 7 ahead / 0 behind.
- 변경 파일 7개: 보고서, 제품 증거 등록부, README, 상황판, 마스터 계획, 세션 로그, JSONL.

### 조사·검토
- PR #204의 보고서 v0.16 §46과 제품 증거 등록부를 읽고, 13개 제품군·예시 모델코드가 실제 사용자 대상 SKU로 오인되지 않도록 하는 경계와 미확인 증거 상태를 확인했다.
- LS메카피온 공식 Servo 카탈로그 목록과 iX700M 상세 게시물을 대조했다. 목록 제목은 2025년 7월을 표시하지만 상세 첨부파일의 파일 날짜는 2025-12-05다. 이 차이를 문서 개정일로 단정하지 않고 register §8에 별도 기록했다. PDF 원문은 아직 확보·검토하지 않았다.
- ETSI 공식 회의 캘린더를 재조회했다. GoSRSReq006-M/606 AMD 1은 2026-11-23 Online 일정으로 게시되어 있으나, 회의록/결정/공식 contribution 및 ESO receipt/acceptance/non-acceptance notice는 공개 근거로 확보하지 못했다.
- 따라서 회의가 열리지 않았다고 판단하지 않는다. 회의 개최 여부·결과·개정안 채택·ESO 수령일은 Unknown으로 유지하고 통합 보고서 §47에 기록했다.

### 개선 및 검증 원칙
- 목록 제목, 첨부파일 메타데이터, 원문 PDF 개정 이력을 별도 필드로 관리한다.
- 일정 게시와 회의 결과, ESO 수령과 수락, ESO 채택과 OJ citation/Article 27 presumption을 혼동하지 않는다.
- PR #204는 exact-head CI 확인 전 병합하지 않는다. 이번 점검은 운영 코드/workflow/secrets/API cadence를 변경하지 않았다.

### 다음 작업
1. PR #204 exact-head CI, 파일 read-back 및 diff 확인.
2. M/606 minutes/decision/contribution과 ESO별 수령·수락/비수락 통지 추적.
3. 실제 LS메카피온 SKU/HW/FW/BOM 및 ST MCU full order code 확보.
4. 원본 매뉴얼·카탈로그 PDF를 확보할 수 있으면 파일 해시·개정·모델 적용범위를 확인.

범위: CRA only. SIL 3 제외.



## 2026-11-23 — EU 관보 Commission CRA Guidance C/2026/6013 분석

### 원문 확인
- EUR-Lex ELI: https://eur-lex.europa.eu/eli/C/2026/6013/oj
- OJ C, 17.11.2026, 61 pages.
- 지침 §8은 문서가 경제운영자에게 구속력이 없으며 CRA의 권위 있는 해석은 CJEU에 있다고 명시한다. 보고서에서 법령과 공식 해석 지침을 구분했다.

### 핵심 분석
- §§141~145: 제품 전체 core functionality가 중요/핵심 제품 분류 및 conformity assessment route를 결정한다. 별도 판매 모듈은 독립 PDE로, 통합 제품에만 포함된 모듈은 통합 제품 수준으로 본다.
- §§147~151: 제품 전체 위험평가는 계속 필요하며, OJ 인용 표준의 범위 밖 추가 기능 위험은 별도 조치·문서화한다.
- §§156~163: 잔여 위험은 충분히 처리되어야 하며 제조자 내부 risk appetite·상업 전략·비용만으로 미처리 위험을 정당화할 수 없다.
- §§170~173: 외부 통합 부품은 risk-based due diligence 대상이며 제조사 기술/보안 문서 및 필요 시 시험 증거를 활용한다.
- §§125~127: support period는 예상 사용기간 기준. 최소 5년은 자동 기본값이 아니며 5년보다 긴 제품 사용기간은 더 긴 지원기간을 요구할 수 있다.
- §108 및 §§122~124: 보안 업데이트는 intended purpose 변경/새 위험 도입 여부에 따라 substantial modification 여부를 판단하고, 변경되지 않은 영역의 기존 증거 재사용 가능성을 구분한다.

### 서보드라이브 영향
- ST MCU의 기능 보유 여부와 완제품 내 실제 활성화·구성·검증을 분리한다.
- iX700M Converter Unit/Drive Unit의 별도 판매 여부와 통합 다축 제품의 경계를 확인한다.
- EtherCAT/RS-485 포트나 MCU 보안기능만으로 Annex III 카테고리를 확정하지 않는다.
- 산업 설비의 실제 예상 사용기간, 서비스 계약, 부품 지원기간을 수집한다.
- 잔여 위험을 폐쇄망/고객 책임/비용만으로 종결하지 않는다.

### 문서 변경
- 통합 보고서 v0.17 §48 추가.
- LS메카피온 제품 증거 등록부 §9 추가.
- PROJECT_STATUS_CURRENT, MASTER_PLAN, SESSION_LOG, README, PROJECT_LOG 갱신.
- 이전 PR #204 exact-head CI Run #1352는 success. 이번 문서 변경 후의 새 head는 별도 CI가 필요하다.
- 운영 코드, workflow, secrets, API cadence 변경 없음. CRA only; SIL 3 제외.

## 2026-11-23 — PR #204 최종 브랜치 스냅샷 및 새 CI 게이트

- 작업 브랜치: research/cra-lsmecapion-product-evidence-2026-11-23.
- 기준 main: 584a7c092ea434d52f7794452ca85b0cbe981210.
- C/2026/6013 guidance 분석 추가 후 브랜치 비교: 27 commits ahead / 0 behind; 변경 파일 8개.
- 최신 문서 커밋: 36a3dd41236ee03df0dacf407d9117c5ab317cf7.
- GitHub read-back: 통합 보고서 v0.17 및 §48, 제품 증거 등록부 §9 확인; PROJECT_LOG 323 records, JSONL parse invalid 0.
- PR #204 exact-head Run #1352 (commit dc9f6674f0a2e7cdeb3953776f3c573c7304272b) success. 이후 C/2026/6013 반영으로 문서 전용 커밋이 추가되어 현재 최신 head 36a3dd41236ee03df0dacf407d9117c5ab317cf7에 연결된 PR CI run은 확인되지 않음.
- 최신 문서 커밋은 소스 코드·workflow 변경 없이 Markdown/JSONL만 변경했다. JSONL 전체 파싱과 핵심 문서 read-back은 통과했지만, 최신 head CI가 확인되기 전에는 PR 병합하지 않는다.
- CRA only; SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.



## 2026-11-23 — PR #204 병합 후 검증 상태

- Merge SHA: 8254b6f97a8c6a82cf33bfa25ab6d01bcf408ff0; PR #204 squash merge 완료.
- Exact-head Run #1358 / ID 45136682197 success: source integrity, compile, CRA traceability, full pytest, official PDF/HTML canary, provenance manifest upload.
- PDF evidence upload은 unchanged 조건으로 skipped. PDF 원문을 새로 확보한 것으로 기록하지 않는다.
- Pre-merge safety ref: safety/pre-pr204-merge-2026-11-23. Post-merge safety ref: safety/post-merge-pr204-2026-11-23.
- main read-back: report v0.17 §48, LS Mecapion evidence register §9, JSONL 324 records/0 invalid.
- main push CI: commit status context 미확인. PR exact-head CI와 구분해 별도 확인.
- Next: actual LS Mecapion SKU/product boundary, ST MCU order code/configuration evidence, M/606 ESO receipt and meeting outcome.
