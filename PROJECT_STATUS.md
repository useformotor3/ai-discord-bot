# CRA 서보 드라이브 프로젝트 상황판 — 역사 기록

> **현재 상태는 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 기준으로 확인한다.** 이 파일은 2026-11-17 이전 스냅샷 및 당시 작업 기록을 보존하는 역사 문서이며, 현재 main/CI/재개 지점의 기준 문서가 아니다.


> **활성 범위 통제(2026-11-17): CRA만 진행한다.** SIL 3 산출물은 과거 자료로 보존하되 비활성·별도 범위로 분리한다. 사용자 명시 재개 요청 전에는 SIL 3 후속 조사·설계·문서 작업을 하지 않는다. 과거 로그의 SIL 3 '다음 단계' 문구는 본 결정으로 대체한다.

- 최종 갱신: 2026-11-17 (KST)
- 기준 저장소: `useformotor3/ai-discord-bot`
- 운영 기준 브랜치: `main` (운영 자동화 및 데이터 보존)
- 현재 구현 작업 브랜치: `cra/guidance-claim-mapping-2026-11-17` (Guidance claim mapping 및 PDF binary acquisition 검증)
- 최신 CRA source 기준점: PR #29 merge commit `9c16724b8b72bd09d3492b19ff714602b235c66b`; PR #28 recovery checkpoint `942e1e6b5f2887001279a96c21f94138d283a689`; 관리 문서 PR #27 `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; source provenance 코드 PR #26 `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`
- 최신 source gate PR #26 병합 완료: CELLAR 공식 법령 7건 + Commission 공식 페이지 2건, SHA manifest, claim-level validator, fail-closed source gate
- CRA-only 범위 통제 병합 기준점: PR #18, merge commit `b7813ddd311bc51bfb0eb26458eace9ff82b621f` (2026-11-17)
- 마지막 CRA 코드/출처 검증 병합: PR #26 merge `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`. PR head Run #573 success: 138 passed / 1 xfailed, 9개 live official source 및 Article 13(8) locator/quote 확인. merge commit 자체의 별도 run은 미확인.
- 마지막 관리 문서 동기화: PR #27 merge `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`. Run #575 success: 138 passed / 1 xfailed 및 live source canary 재통과.
- 정오표 우선순위 보강: PR #29 merge `9c16724b8b72bd09d3492b19ff714602b235c66b`. 최종 PR head Run #596: 141 passed / 1 xfailed, 9개 source, Article 64(10)/67 corrigenda 및 Article 13(8) live canary 통과.
- 현재 기준선: GitHub `main` 브랜치 (정확한 HEAD는 세션 시작 시 실시간 조회; 과거 SHA를 현재 HEAD로 고정 표기하지 않음). PR #31 병합 완료.
- 프로젝트 상태: CRA 통합 보고서 v0.2 병합, 요구사항 추적표 35항목, 인터페이스 적용성 매트릭스 15항목 병합. 보안 통제·시험 매트릭스 36항목 초안 작업 중.
- 주 문서 언어: 한국어
- 안전 원칙: 법적 적합성·제품 분류·안전 관련 설계 판단은 근거와 인간 검토 없이 확정하지 않음

## 0. 2026-11-17 현재 브랜치 정합성 및 통합 판단

- canonical 운영 브랜치: main, PR #24 merge commit 153033aa535775a0df568ad83876bff487d33404. 브랜치 비교 수치는 merge 직전 addfa63d1a7d2d1c77ec61444aaadf2b1f327389 기준 snapshot.
- 병렬 브랜치 비교는 reports/BRANCH_RECONCILIATION_2026-11-17.md를 기준으로 한다. 이 보고서가 기존의 오래된 ahead/behind 스냅샷보다 우선한다.
- cra-project-foundation: 1,159 ahead / 1,906 behind. 고유 보고서/249-item archive audit queue를 보존하되 전체 병합하지 않는다.
- integration/cra-source-grounding-2026-11-17: 과거 참조 브랜치로 보존한다. 필요한 source/claim 기능은 최신 main 기반 PR #26에서 CELLAR retrieval, redirect allowlist, exact locator 및 tests와 함께 선택 통합 완료. branch 전체는 병합하지 않았다.
- feature/cra-source-grounding-atomic-2026-11-17: 165 ahead / 218 behind, PR #3 closed/unmerged. 원본 참고 브랜치로 보존한다.
- PR #26에서 Formex/HTML 줄바꿈을 정규화하고 Article 13(8) paragraph scope의 quote 일치를 실시간 확인했다. Article 13(8) 외 Annex I 및 주요 Article의 live locator canary는 후속 확장 대상이다.
- main.py의 최근 15개 history context, 2회 retry, 429/503/quota no-op, duplicate-topic suppression, transactional persistence/rollback을 보존한다.
- divergent branches, safety checkpoint, archive/state/history를 삭제·force-push·전체 merge하지 않는다.

## 1. 한눈에 보는 현재 상태

| 영역 | 상태 | 확인된 사실 / 다음 조치 |
|---|---|---|
| 프로젝트 관리 체계 | 반영 | README, 행동강령, 상황판, 마스터 계획, 세션 로그를 GitHub에서 유지 |
| CRA 조사 품질 감사 | 표본 감사 및 정정본 작성 | #27~#29 표본에서 인용·분류·시한 표현의 위험 식별 |
| P0 모델 실패 처리 | 작업 브랜치 구현 | 응답 구조 검사, 모든 모델 실패 시 비정상 종료 |
| P1-A 상태·이력 안전성 | 작업 브랜치 구현 | 손상 JSON/스키마 fail-closed, 날짜·시간 호환 |
| helper 독립 테스트 | 이전 독립 실행 7 passed | 실제 저장소 전체 suite 아님 |
| 임시 재구성 사본 테스트 | 예비 결과 | SHA 불일치로 원본 검증으로 인정하지 않음; 현재는 별도 Actions 원본 테스트로 대체 |
| 실제 저장소 전체 pytest | **통과** | Run #3 최신 검증 commit에서 21 passed, 5개 SHA 일치 |
| 테스트 전용 GitHub Actions CI | **통과** | Run #1~#3 success; 최신 Run #3에서 SHA·compileall·pytest 재검증 |
| P1-B1 Discord 전송 신뢰성 | **구현 및 CI 검증 완료** | Run #18: 43 passed / 1 xfailed; timeout/status/429/partial 검증 |
| P1-B2 저장 원자성 | 구현·보강 및 CI 검증 완료 | durable journal, SHA 보호, roll-forward, target allowlist; Actions 43851438733: 70 passed / 1 xfailed |
| P1-B3 Git sync 상태화 | 미구현 | 유일한 strict xfail; 별도 승인 필요 |
| P1-B4 구조 개선 | 미구현 | import-time 실행 제거 등 후속 단계 |
| CRA 통합 보고서 | 병합된 초안 v0.2 | 2026-07 Commission Guidance 및 2026-11 M/606 개정 반영; 모델별 적용성 검증 전 |
| CRA 요구사항 추적 | 병합된 초안 v0.2 | CSV 35항목 작성; 제품 증거·설계 통제·시험 결과 연결 필요 |
| CRA 인터페이스 적용성 | 병합된 초안 15항목 | 필드버스/serial/analog/discrete/encoder/STO/PC tool/RDPS 구분; 모델별 증거 필요 |
| CRA 보안 통제·시험 | 병합된 초안 36항목 | 35개 요구사항 ID와 교차 연결; Annex I/Articles 13-14/31-32/69 기반 통제·시험 후보; 구현/시험 미실시 |
| CRA 참조 보안 아키텍처 | 병합된 초안 v0.1 | 논리 블록·신뢰 경계·데이터 흐름; 특정 MCU/보드/프로토콜 미확인 |
| CRA 공식 source provenance | **PR #26 병합·CI 통과** | CELLAR 7개 법령 + Commission 2개 페이지, full/excerpt SHA-256, claim/locator validator, 9-source live canary |
| 과거 SIL 3 기능안전 자료 | 보존·비활성 | 기존 파일/PR 이력은 유지. CRA 활성 작업·다음 단계에 포함하지 않음 |

## 2. P1-B1 이전 기준선에서 확인한 원본 코드 사실

> 아래 Discord timeout/status 부재 등의 내용은 P1-B1 구현 전 기준선이다. 현재 변경 후 상태는 §26 및 P1-B1 상세 보고서를 따른다.

검토 기준 파일:
- `main.py`: blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43`
- `tests/conftest.py`: blob SHA `d55069fa82b4eb9d555033db8f8c2867ff774dd6`
- `tests/test_main_characterization.py`: blob SHA `8019b18696bc9f1eb729feed633ecf2e32f36c04`
- `tests/test_p1_reliability.py`: blob SHA `cff881cb0da2724f8810b88ae621909a9e23a6f9`
- `.github/workflows/run.yml`: blob SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`

### 테스트 fixture 검토
1. Git mock은 모든 subprocess 명령에 대해 항상 returncode=0을 반환하므로 Git commit/push 실패를 검증하지 못한다.
2. Discord mock은 항상 HTTP 204를 반환하므로 timeout, 네트워크 오류, 429, 4xx, 5xx 및 부분 전송을 검증하지 못한다.
3. 정상 테스트는 Git 명령 횟수만 확인하며 각 명령의 실패 결과를 확인하지 않는다.
4. 따라서 현재 테스트가 Git/Discord 실패 경로까지 검증했다고 표현하면 안 된다.

### 운영 코드 정적 검토
- Discord 요청에 timeout 및 HTTP status 검증이 없다.
- Discord 전송이 아카이브/상태 저장보다 먼저 수행된다.
- state/history를 직접 write하여 중간 중단 시 파일 손상 가능성이 있다.
- Git commit/push 예외를 출력만 하고 삼켜 프로세스가 성공 종료할 수 있다.
- webhook 미설정 시 전송 생략이 명시적 상태로 기록되지 않는다.
- history 항목의 snippet 자료형을 검증하지 않고 문자열 join에 사용한다.
- 아카이브 파일명이 초 단위라 같은 초의 실행에서 충돌할 가능성이 있다.
- 보고서 검증은 길이/섹션/일부 오류 문구 검사이며 출처 원문·조항 적합성 검증이 아니다.
- 모듈 import 시점에 전체 파이프라인이 실행되어 테스트/재사용성이 제한된다.

위 항목 중 snippet 자료형 분포와 실제 파일명 충돌 발생 여부는 추가 데이터 확인 전까지 잠재 위험으로 취급한다.

## 3. 테스트 실행 상태 — 반드시 구분

| 검증 | 결과 | 해석 |
|---|---|---|
| P1-A helper 독립 pytest | 7 passed | 분리된 helper 로직 검증 |
| 임시 재구성 사본 compileall | 종료 코드 0 | 임시 사본 문법 검증 |
| 임시 재구성 사본 pytest | 21 passed | 임시 사본 예비 검증 |
| 임시 사본 blob SHA 비교 | 5개 모두 불일치 | 원본 동일성 실패 |
| 작업 브랜치 원본 전체 pytest | **21 passed** | Run #3 commit `dddba44a41851e9d0319ce9a91535a9d26145d92`; 5개 SHA 일치 |
| 테스트 전용 GitHub Actions CI | **success** | [Run #3](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938) |
| 운영 workflow/API/Discord/Git push | 실행 안 함 | 운영 영향 없음 |

이전 ChatGPT 실행환경의 Git clone은 DNS 단계에서 실패했으나, 별도 승인된 테스트 전용 GitHub Actions로 대체 경로를 확보했다. Actions checkout 원본에서 다섯 개 Git blob SHA 일치, compileall, pytest 21 passed를 확인했다. 따라서 원본 테스트 실행 경로 문제는 해결된 것으로 갱신한다.

기존 workflow는 `repository_dispatch: run-bot` 및 `workflow_dispatch`에서 운영 `main.py`를 실행한다. 따라서 테스트를 위해 이 workflow를 실행하지 않는다. 테스트 전용 workflow `.github/workflows/tests.yml`은 별도 승인을 받아 추가했으며, 운영 workflow와 분리해 사용한다.

## 4. 위험 우선순위 및 조치

| 우선순위 | 항목 | 조치 |
|---|---|---|
| P0 | 원본 소스 동일성 보장 테스트 환경 | **해결** — 전용 GitHub Actions에서 SHA 일치 후 compileall/pytest 수행 |
| P1 | Git push 실패 미검증 | subprocess mock이 non-zero/CalledProcessError를 재현하도록 개선 |
| P1 | Discord timeout/status 미검증 | timeout, 429/4xx/5xx, 네트워크 오류 테스트 및 코드 개선 |
| P1 | 전송-아카이브-상태의 부분 성공 | 단계별 상태와 재실행/idempotency 정책 설계 |
| P1 | state/history 비원자적 저장 | 임시 파일 및 atomic replace, 복구 정책 |
| P2 | snippet 자료형/legacy history | 기존 1,592개 자료형 분포 확인 후 호환 규칙 |
| P2 | 초 단위 아카이브 이름 | run_id/충돌 방지 |
| P2 | 출처 검증 부족 | 공식 URL·조항·원문·적용성 증거 구조화 |
| P2 | import 시점 파이프라인 실행 | main guard 및 순수 함수 분리 설계 |

## 5. 브랜치 보호 및 운영 영향

- 2026-11-14의 61/49 및 72/50 ahead/behind 값은 과거 스냅샷이다. 현재 분기 상태는 Section 0 및 reports/BRANCH_RECONCILIATION_2026-11-17.md를 기준으로 한다.
- 병렬 branch의 전체 merge/rebase는 하지 않는다. 필요한 source-gate 기능만 최신 main에서 별도 branch로 선택 이식한다.
- 위 문장은 2026-11-14 당시 작업 범위의 역사 기록이다. 이후 PR #19–#23은 문서/CSV만 변경했고 운영 코드/workflow/state/history는 변경하지 않았다.
- 실제 Gemini/Discord/Git push 및 운영 workflow를 실행하지 않았다.

## 6. 다음 재개 지점 — 2026-11-17

1. PR #26에서 통합한 CELLAR source gate의 운영 로그/다음 정기 실행 결과를 관찰하되, Gemini/Discord 운영 실행을 임의로 테스트하지 않는다.
2. Commission Guidance C(2026) 5252 PDF 원문/Annex 및 M/606 결정 C(2026) 7861 Annex를 별도 수집·파싱하고, 페이지 locator와 SHA-256을 기록한다. 현재는 관련 URL만 기록하며 PDF/결정 Annex 본문은 미수집이다.
3. Article 13(8) 외 Annex I Part I/Part II 및 핵심 Article의 실시간 locator/quote canary를 확대한다.
4. CRA 35개 요구사항, 15개 인터페이스, 36개 SEC 통제/시험 항목을 source claim ID, 설계 통제, 시험 케이스 및 증거 링크와 교차 연결한다.
5. 실제 제품 모델·회로·펌웨어·프로토콜·EU 공급 구조 자료가 확보되면 제품별 적용성, Annex III/IV 분류 및 Article 32 경로를 검증한다. 자료가 없으면 일반 참조 설계/잠정 판단으로 유지한다.
6. main merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`의 post-merge CI 여부를 확인하고, 관리 문서·기계 로그를 동기화한다.

## 7. 문서 진입점

- [프로젝트 메인 페이지](README.md)
- [브랜치 정합성 및 소스 검증 통합 감사](reports/BRANCH_RECONCILIATION_2026-11-17.md)
- [CRA 공식 출처 수집·주장 추적 파이프라인](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md)
- [CRA 통합 보고서 v0.2](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)
- [CRA 보안 통제·시험 매트릭스](reports/CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv)
- [CRA 참조 보안 아키텍처](reports/CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md)
- [AI 행동강령](AI_RULEBOOK.md)
- [마스터 계획](MASTER_PLAN.md)
- [작업 이력](SESSION_LOG.md)
- [조사 품질 감사](reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md)
- [CRA 보고서 #28·#29 정정](reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md)
- [자동화 코드 개선 설계 및 정적 검토](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- [테스트 실행 환경 감사](reports/TEST_EXECUTION_ENVIRONMENT_AUDIT_2026-11-14.md)
- [테스트 가이드](tests/README.md)


## 8. 2026-11-14 15:31 KST — 원격 상태 재확인

- 작업 브랜치 HEAD: `8813eb53b186b25e72ac157d664d636be6d68fd8`
- 운영 main HEAD: `c9b5bff8ee851b6baa86bbe4073353c9303bb432`
- GitHub compare 결과: diverged, Historical snapshot 2026-11-14: 72 commits ahead / 50 behind; superseded by Section 0
- GitHub Actions runs API 조회 결과: 해당 작업 브랜치의 workflow run 0건
- 해석: 이 브랜치에서 확인 가능한 CI 성공 증거가 없다. CI 통과 또는 테스트 완료로 표시하지 않는다.
- 이번 조회는 GitHub API GET만 수행했다. workflow dispatch, 운영 자동화, 코드 실행은 하지 않았다.
- 병합/리베이스는 계속 보류한다.

## 9. 2026-11-14 — 테스트 전용 GitHub Actions 구현 및 원본 테스트 성공

### 구현
- 신규 workflow: `.github/workflows/tests.yml`
- 테스트 가이드: `tests/README.md` 갱신
- 실행 범위는 작업 브랜치 `docs/cra-audit-and-project-control-2026-11-14`로 제한
- `push` 경로 필터와 수동 `workflow_dispatch` 지원
- `permissions: contents: read`, checkout credential persistence 비활성화
- Gemini API 키, Discord webhook, 운영 Git push 권한을 사용하지 않음
- 기존 운영 `.github/workflows/run.yml` 및 운영 데이터는 변경하지 않음

### 실제 실행 증거
- Workflow: Isolated Python Tests
- Run: [#1 — 성공](https://github.com/useformotor3/ai-discord-bot/actions/runs/43567990149)
- 실행 commit: `d31c604c6067685e33f6888cbc488c0e45d80be7`
- 실행 이벤트: push
- Source integrity: 5개 핵심 파일 Git blob SHA 전부 일치
  - `main.py`: `470ac101d5cc4fdb2c5077d5468ef00327af3d43`
  - `tests/conftest.py`: `d55069fa82b4eb9d555033db8f8c2867ff774dd6`
  - `tests/test_main_characterization.py`: `8019b18696bc9f1eb729feed633ecf2e32f36c04`
  - `tests/test_mock_infrastructure.py`: `863a77c5ec3dc50c0a21b246b22cb862a8baeaa2`
  - `tests/test_p1_reliability.py`: `cff881cb0da2724f8810b88ae621909a9e23a6f9`
- `python -m compileall -q main.py tests`: 통과
- `python -m pytest -q`: **21 passed in 0.16s**
- Job conclusion: success

### 해석과 제한
- 이전 임시 재구성 사본의 21 passed와 달리, 이번 결과는 GitHub 원본 checkout과 SHA 일치가 확인된 commit에서 직접 실행한 결과다.
- 현재 저장소의 pytest 자동 탐색 범위에서 21개 테스트가 통과했다.
- 이 테스트는 mock 기반이다. 실제 Gemini/Discord 연동, 실제 Git push 성공, CRA 법률 해석 정확성, 미작성된 Discord/Git 실패 시나리오까지 보증하지 않는다.
- Workflow의 SHA 고정값은 기준 소스가 바뀌면 의도적으로 실패한다. 소스 변경 시 검토 후 SHA 기준값을 함께 갱신해야 한다.
- 운영 `main`, `main.py`, `.github/workflows/run.yml`, `state.json`, `history.json` 변경 없음.
- 운영 workflow dispatch, Gemini API, Discord webhook, Git push 실행 없음.

### 다음 단계
1. 현재 테스트의 Git/Discord 실패 경로 검증 공백을 유지보수 항목으로 추적한다.
2. P1-B 구현은 별도 승인 전까지 보류한다.
3. 이후 코드 변경은 동일한 SHA 검증 → compileall → pytest CI 게이트를 통과시킨다.


## 10. 최신 브랜치 HEAD 재검증 — 2026-11-14

- 최신 브랜치 HEAD: `dddba44a41851e9d0319ce9a91535a9d26145d92`
- [GitHub Actions Run #3 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938)
- 다섯 개 원본 Git blob SHA: 모두 일치
- compileall: 통과
- pytest: **21 passed in 0.19s**
- Run #1(21 passed in 0.16s), Run #2(success)에 이어 문서 기록 반영 후 최신 HEAD에서 다시 성공했다.
- Run #3의 source integrity, compile, pytest 단계와 최종 conclusion을 모두 확인했다.
- 현재까지 확인된 테스트는 mock 기반이다. Discord/Git 실패 경로 검증 공백과 P1-B 미구현 상태는 유지한다.


## 11. 최신 원격 상태 스냅샷 — 2026-11-14

- 작업 브랜치 HEAD 확인 시점: `a413eee5faa8844d42224987aef98f2b99704b72`
- main 대비 compare: diverged, 93 ahead / 53 behind
- 이 수치는 해당 조회 시점의 스냅샷이며 이후 커밋에 따라 변동한다.
- 테스트 전용 CI 최신 검증: [Run #3 success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938), 검증 commit `dddba44a41851e9d0319ce9a91535a9d26145d92`
- Run #3 이후의 추가 변경은 README/상황판/계획 등 문서만이며 `main.py`, 테스트 소스, 테스트 workflow의 SHA 기준값은 변경하지 않았다.
- merge/rebase는 여전히 보류한다.


## 12. 2026-11-14 최신 compare 재확인

- 조회 당시 작업 브랜치 HEAD: `fcb365ededdad0d2adf48289688dfa3cca98d43b`
- main 대비: diverged, 95 ahead / 53 behind
- 이 수치는 조회 당시 스냅샷이며, 이 상황판 갱신 커밋 이후 ahead 수가 증가할 수 있다.
- CI 최신 성공 검증 commit은 `dddba44a41851e9d0319ce9a91535a9d26145d92`이며, 이후 변경은 문서만 포함한다.
- 통합 전에는 compare를 다시 조회하고 충돌 검토 후에만 병합/리베이스를 판단한다.
 
## 11. 프로젝트 기록 형식 보완 — 2026-11-14

- 한국어 사람이 읽는 기록: `SESSION_LOG.md` 유지.
- AI/도구가 파싱할 작업 이벤트: `PROJECT_LOG.jsonl` 신규 추가. JSONL 한 줄당 이벤트 1건이며 이벤트 ID, 날짜, 유형, 상태, 요약, 브랜치, 파일, 검증, 한계, 승인 범위를 기록한다.
- 런타임 `state.json`·`history.json`은 프로젝트 작업 로그가 아니며 별도 승인 없이 수정하지 않는다.
- 최근 원격 compare 재조회: `main` 대비 diverged, 96 commits ahead / 54 commits behind (2026-11-14 조회 시점). 이후 문서 커밋으로 ahead 값은 증가할 수 있으므로 통합 직전 재조회한다.
- 병합/리베이스는 계속 보류한다.

## 12. 프로젝트 로그 구축 후 원격 상태 재확인 — 2026-11-14

- `PROJECT_LOG.jsonl` 및 관리 문서 갱신 후 GitHub compare 재조회: `main` 대비 diverged, **102 ahead / 54 behind**.
- compare 기준 main HEAD: `6ba398b5aebb136b1026b94cf361670b1f7f60bd`; merge base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 이 값은 이번 조회 시점의 스냅샷이다. 자동화 커밋으로 변동 가능하며 병합/리베이스는 보류한다.
- CI 최신 성공 근거는 Run #3, 검증 commit `dddba44a41851e9d0319ce9a91535a9d26145d92`; 이후 이번 작업은 문서만 변경했다.

## 13. 실패 경로 fixture 설계 완료 — 구현 승인 대기

- 원본 tests/conftest.py, tests/test_main_characterization.py, tests/test_p1_reliability.py 및 main.py를 재조회해 mock 동작과 미검증 경로를 확인했다.
- 상세 설계: [main.py 개선 설계 보고서 §16](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md).
- Discord timeout/network/429/4xx/5xx/chunk 부분 전송, Git add/commit/push 실패, atomic save 실패, secret 비노출 테스트 시나리오를 정의했다.
- 현재 fixture는 Discord 204와 Git returncode 0만 반환하므로 해당 실패 경로는 미검증이다.
- 이번 작업은 설계 문서만 갱신했다. 테스트 코드와 main.py는 변경/실행하지 않았다.
- P1-B 운영 코드 및 fixture/test 변경은 각각 승인 경계를 확인한 뒤 진행한다.
- 설계 작성 전 마지막 compare 스냅샷: 106 ahead / 55 behind, diverged. 이후 문서 커밋으로 수치는 증가할 수 있다.


## 14. 실패 경로 fixture 구현 및 CI 검증 — 2026-11-14

### 브랜치 및 기준점
- 전용 작업 브랜치: `test/failure-path-fixtures-2026-11-14`
- 기준 브랜치: `docs/cra-audit-and-project-control-2026-11-14`
- 기준 commit SHA: `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 작업 시작 시 `main` 비교: diverged, 111 ahead / 56 behind (이후 main 자동 커밋으로 변동 가능)

### 실제 변경 범위 — 기준점 대비
- 수정: `tests/conftest.py` — Discord 응답 큐/status/headers/예외/timeout 관찰, Git 명령별 return code 및 check=True 예외, sleep 기록
- 수정: `tests/test_mock_infrastructure.py` — Discord 429/Retry-After 응답과 Git CalledProcessError 주입 확인
- 추가: `tests/test_external_failure_paths.py` — timeout, 429 retry, 503 retry, 400 실패 차단, Git sync failed 기대 동작 5건(strict xfail)
- 수정: `.github/workflows/tests.yml` — 전용 feature branch 트리거와 6개 소스·테스트 blob SHA 검사
- 수정: `tests/README.md` — fixture 사용법, strict xfail 해석 규칙
- 기준 commit 대비 diff는 위 5개 경로만 변경되었으며 `main.py`는 변경하지 않았다.

### CI 실행 및 교정 이력
- Run #5: 테스트 2건 실패(경계 probe가 main.py를 실행하도록 잘못 연결, status capture 미반영). fixture/test 설계 결함으로 판정하고 수정.
- Run #6: workflow SHA 기준과 직전 fixture commit 불일치로 취소/검증 중단.
- Run #7: 테스트 1건 실패(경계 probe에 script_path 미지정). 수정.
- Run #8: 변경된 test_mock_infrastructure.py blob SHA와 workflow 기준값 불일치. workflow SHA 갱신.
- Run #9: 테스트 1건 실패(동일 probe 실행 대상 오류). 수정.
- Run #10: 같은 브랜치 후속 push에 따른 concurrency 취소.
- Run #11: [성공](https://github.com/useformotor3/ai-discord-bot/actions/runs/43569359083), 실행 commit `821d64bea0bc96710f083a773eabede80ba4a45c`; 6개 blob SHA 모두 일치, compileall 통과, pytest **23 passed, 5 xfailed**.
- 실패 시도는 모두 로그에서 원인을 확인했으며 최종 성공 결과와 혼동하지 않는다.

### 해석 및 미해결 사항
- 5 xfailed는 현행 main.py가 아직 지원하지 않는 P1-B 기대 동작을 엄격히 표시한다. 운영 코드 결함이 수정되어 테스트가 통과하면 XPASS(strict)로 CI가 실패하므로 xfail 해제 및 정상 테스트 전환이 필요하다.
- 이번 승인 범위는 테스트 fixture/test 및 테스트 전용 workflow다. P1-B 운영 코드 수정은 수행하지 않았다.
- Gemini API, 실 Discord webhook, 실제 Git push, 운영 workflow는 호출하지 않았다.
- merge/rebase/PR merge는 수행하지 않았다.


## 15. 전용 테스트 브랜치 최종 추적 스냅샷 — 2026-11-14

- 현재 확인 대상 HEAD(상황판 갱신 직전): `b652cbe264d0f99db27f5b0aacaa81a011abfac1`.
- 기준 브랜치 `docs/cra-audit-and-project-control-2026-11-14`의 기준 commit `c6dfc5cee2485922b2313030dd9a5843e347afe7` 대비 18 commits ahead / 0 behind.
- `main` 대비 diverged: 129 ahead / 57 behind (조회 시점). main 자동화 커밋으로 변동할 수 있다.
- 기준 commit 대비 실제 변경 경로는 11개이며 `main.py`는 변경 파일 목록에 없다. `main`과의 전체 비교에 보이는 `main.py` 변경은 상위 문서/개선 브랜치에서 상속된 기존 변경이며 이번 전용 테스트 브랜치의 신규 변경이 아니다.
- 18개 commit은 GitHub Contents API의 파일 단위 업데이트 및 CI SHA 정정 커밋이 누적된 결과다. 추적성은 유지되지만 논리 작업 단위보다 세분화된 점은 비효율이다. 다음 작업부터는 변경 묶음을 확정한 뒤 Git tree/commit API 등으로 논리적 커밋 수를 줄인다.
- Run #11은 commit `821d64bea0bc96710f083a773eabede80ba4a45c`에서 실행됐으며, 그 뒤 변경은 관리 문서와 로그만이다. 테스트 소스/fixture/workflow는 Run #11 이후 변경하지 않았다.
- 병합/리베이스/PR merge 및 운영 실행은 하지 않았다.


## 16. 최신 원격 비교값 — 2026-11-14

- 비교 기준 HEAD: `d31ccee8cb884c7eef93232d342a43dee0e1caff`.
- 기준 브랜치 commit `c6dfc5cee2485922b2313030dd9a5843e347afe7` 대비 20 ahead / 0 behind.
- 운영 `main` 대비 diverged, 131 ahead / 57 behind.
- 이 섹션을 반영하는 문서 커밋 1건이 추가되므로 이후 실제 ahead 값은 최소 1 증가한다. 다음 통합 판단 전에는 반드시 다시 조회한다.


## 17. 최신 재개 스냅샷 및 추가 실패 주입 테스트 — 2026-11-14

### 작업 시작 시 원격 기준점
- 작업 브랜치: `test/failure-path-fixtures-2026-11-14`
- 시작 HEAD: `4f599f14e92dcbe5ead14d4886feda34cfd874da`
- 기준 브랜치/commit: `docs/cra-audit-and-project-control-2026-11-14` @ `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 기준 브랜치 대비: 21 ahead / 0 behind
- `main` HEAD: `3b2dafd098b51eb60998ce3be032efc4a42760fb`
- `main` 대비: diverged, 132 ahead / 58 behind
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`
- 위 수치는 작업 시작 시점의 스냅샷이며 다음 커밋 후 ahead 수가 증가한다.

### 이번 승인 범위에서 추가한 fixture 검증
- Discord 전송 경계에서 연결/timeout 예외를 주입하고 캡처하는지 검증(2개 parameter case).
- HTTP 401/403 응답을 주입하고 status 및 raise_for_status 동작을 확인(2개 parameter case).
- Git add/commit/push 각 단계에 개별 실패를 주입하고 check=True의 CalledProcessError 및 이후 명령 미실행을 확인(3개 parameter case).
- 이는 **fixture의 실패 주입 능력**을 확인하는 테스트이며, 현행 main.py가 해당 장애를 올바르게 복구/재시도하거나 상태화한다는 의미가 아니다.
- P1-B 운영 코드와 `main.py`는 수정하지 않는다.

### CI 및 후속 확인
- 새 테스트 수: 기존 23 passed / 5 xfailed에서 7개 fixture case 추가. Run #13에서 30 passed / 5 xfailed로 확인했다.
- 테스트 workflow의 source pin은 변경된 `tests/test_mock_infrastructure.py` blob SHA로 갱신했다.
- Run #13에서 source integrity, compileall, pytest 전체가 통과했다.
- Run #11은 변경 전 소스만 검증하며, 이번 추가 7개 case는 Run #13에서 검증했다.


## 18. 실패 주입 2차 확장 CI 완료 및 정정 이력 — 2026-11-14

- 검증 대상 commit: `27d2c69287631b041672b9989fdeeb3066f5ebb9`
- [GitHub Actions Run #13 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208)
- 6개 source blob SHA: 모두 일치
- `python -m compileall -q main.py tests`: 통과
- `python -m pytest -q`: **30 passed, 5 xfailed in 0.26s**
- 기존 23 passed / 5 xfailed에서 fixture capability 테스트 7건을 추가한 결과다.
- Run #12는 실패했다. 로그에서 `tests/test_mock_infrastructure.py`의 실제 blob SHA가 workflow pin과 불일치한 것을 확인했다. 운영 코드/테스트 로직 실패가 아니라 SHA 고정값 갱신 누락이었다. 이후 테스트 파일과 workflow pin을 같은 논리 작업으로 수정하고 Run #13에서 SHA 6개 일치 및 전체 테스트 통과를 확인했다.
- Run #12 실패를 삭제하거나 성공으로 바꾸지 않는다. 이력은 Run #12 및 Run #13 링크로 보존한다.
- 기준 docs commit 대비 현재 23 ahead / 0 behind. `main` 대비 diverged 134 ahead / 58 behind (조회 당시 main HEAD `3b2dafd098b51eb60998ce3be032efc4a42760fb`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`). 문서 commit 추가 후 ahead 수는 증가한다.
- 이번 테스트는 fixture injection과 경계 관찰을 검증한다. 운영 main.py의 retry/부분 전송/상태화/atomic persistence를 검증하지 않는다.

## 19. 관리 문서 갱신 후 원격 상태 재조회 — 2026-11-14
- 직전 HEAD: `11c89c2bf513c0562aa0451caf38effae2041e26`.
- 기준 docs commit 대비 24 ahead / 0 behind.
- main 대비 diverged 135 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- Run #13에서 검증된 테스트 소스 commit `27d2c69287631b041672b9989fdeeb3066f5ebb9` 이후 변경은 문서·로그뿐이다.
- main.py blob SHA는 `470ac101d5cc4fdb2c5077d5468ef00327af3d43`이며 이번 테스트 브랜치 기준 commit 대비 미변경이다.


## 20. P1-B 정책 재검토 — 구현 전 설계만 수행
- 공식 Discord Rate Limits/Webhook Execute 및 Python Requests timeout/예외 문서를 교차 확인해 §17에 설계 정책을 추가했다.
- 핵심 수정 판단: Discord POST의 ReadTimeout/5xx는 서버 반영 여부가 불명확하므로, 중복 방지 수단 없이 무조건 재시도하는 기존 가정은 위험하다. 429는 서버가 제공한 Retry-After/retry_after를 따르고, 401/403/404는 재시도하지 않는다.
- `wait=true`로 서버 확인 및 message ID를 받을 수 있으나, 응답이 유실된 경우 중복 가능성을 완전히 없애지는 못한다.
- state/history 파일별 atomic replace는 두 파일 간 transaction 보장이 아니다. journal/recovery 정책이 필요하다.
- 현행 503 retry strict xfail는 정책과 충돌할 수 있어 구현 전에 재검토한다.
- 이번 단계는 문서 설계만이다. main.py/운영 workflow/state/history 변경 및 운영 실행은 없다.


## 21. Discord 오류 테스트 계약 정합화 및 최신 CI — 2026-11-14
- 초기 503 retry xfail은 Discord POST 중복 가능성과 충돌하여 `delivery_unknown`으로 변경했다.
- 401/403/404는 영구 실패(permanent_failure), 자동 재시도 금지 기대 테스트 3 case를 추가했다.
- [Run #15](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842), tested commit `b2e108768be08f06e85af154835424682337ebf5`: 6개 blob SHA 일치, compileall 통과, **30 passed, 8 xfailed in 0.23s**.
- 8 xfailed는 아직 구현되지 않은 P1-B 동작 계약이다. 이는 CI 실패가 아니라 의도적으로 표시한 미구현 기대 동작이다.
- 기준 docs commit 대비 27 ahead / 0 behind; main 대비 diverged 138 ahead / 59 behind. main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- main.py blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 유지. 이번 변경은 테스트/문서이며 운영 구현은 없다.

## 22. P1-B 정책 문서 갱신 후 원격 상태
- 직전 HEAD `5b3cd6ca70dcff7a50f4ad4c20f834592c9e8ca9`; 기준 docs commit 대비 28 ahead / 0 behind.
- main 대비 diverged 139 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- Run #15 검증 commit `b2e108768be08f06e85af154835424682337ebf5` 이후는 문서/로그만 변경.
- main.py blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 유지.


## 23. 다음 작업의 승인 경계 — P1-B1 제안
- P1-B 구현을 B1 Discord 전송, B2 atomic persistence, B3 Git sync, B4 구조 개선으로 분리했다.
- 우선 승인 요청 대상은 B1만: timeout/wait=true/status, 429 Retry-After, permanent failure, delivery_unknown, chunk partial.
- 변경 예정 파일과 테스트/롤백/제외 범위는 개선 설계 보고서 §18에 명시했다.
- P1-B1은 main.py 수정이 포함되므로 현재 미승인·미구현 상태다. 사용자 별도 승인 전에는 운영 코드를 변경하지 않는다.

## 24. P1-B1 제안서 저장 후 원격 상태
- 현재 HEAD `f5a83e3c8e04a43b6e38a593c7b01bd360583b3f`; 기준 docs commit 대비 30 ahead / 0 behind.
- main 대비 diverged 141 ahead / 60 behind; main HEAD `1dff09ffa9722119f6fb0847a51b6c87c322d114`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- Run #15 검증 commit `b2e108768be08f06e85af154835424682337ebf5` 이후 테스트 소스는 변경하지 않았다.
- 다음 단계는 P1-B1 승인 여부 확인이다. 승인 전 main.py 수정 금지.


## 26. P1-B1 구현 CI 검증 완료 — 2026-11-16
- 구현 commit: 715af78b42eacaeb3ca30c03c838132c2a51e707. CI pin 정정 commit: dc341d9e89a837df878257fd3740633f8688507f.
- [Run #18 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43808285335), tested HEAD dc341d9e89a837df878257fd3740633f8688507f.
- source integrity: 핵심 파일 6개 Git blob SHA 모두 일치.
- compileall: 통과.
- pytest: **43 passed, 1 xfailed in 0.34s**.
- Run #17은 잘못된 main.py SHA 기대값(900391...)과 실제 blob(4b631...) 불일치로 source integrity 단계에서 실패했다. workflow pin을 실제 SHA로 수정한 Run #18에서 성공했다.
- 유일한 xfail은 Git push 실패 상태화(P1-B3)이며 이번 승인 범위 밖이다.
- Discord 실패에도 archive/state/history 저장 흐름이 계속되는 점을 테스트했다. 단, 이들 파일의 atomicity/transaction 보장은 하지 않는다.
- 실제 Discord/Gemini, 운영 workflow, 운영 Git push 미실행.


## 최신 원격 브랜치 비교 — 2026-11-16
- 작업 브랜치 HEAD(비교 시점): bc0d05d45b63e9039a87abf6847c9daccc0124f3.
- 기준 docs commit c6dfc5cee2485922b2313030dd9a5843e347afe7 대비 36 ahead / 0 behind.
- 운영 main 대비 diverged: 147 ahead / 610 behind. main HEAD 8357da3abe3b87ca0e7a2fa50f862b693c0a226c, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- main.py SHA: 작업 브랜치 4b631c04e34b2b3bbade0aa9301e7d48578a1e03, main 86a7731aad5de8d75581fc953bcea2c44adf2f2b. 브랜치에는 P0/P1-A 및 P1-B1 변경이 있으나 main은 다른 시점의 코드다.
- 610 behind의 큰 차이가 있으므로 main으로 직접 PR/merge하지 않는다. 먼저 두 브랜치의 commit/file 차이, 자동 생성 보고서와 데이터 영향, 충돌을 별도 통합 감사해야 한다.
- merge/rebase/PR merge/운영 배포는 수행하지 않았다. 비교 수치는 조회 시점 기준이다.


## 최신 원격 비교 스냅샷 — 2026-11-16
- 비교 대상 작업 브랜치 HEAD: 934319884561ac772e7cc805a3ae58415742ab07.
- 기준 docs commit 대비 38 ahead / 0 behind.
- main 대비 diverged 149 ahead / 610 behind; main HEAD 8357da3abe3b87ca0e7a2fa50f862b693c0a226c, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- 문서 갱신 커밋 이후 ahead 수가 증가하므로 이 수치는 조회 시점 스냅샷이다.
- 610 behind로 직접 병합하지 않고 통합 감사 전까지 병합·리베이스를 보류한다.


## 27. 관리 문서 상단 현황 정합화 — 2026-11-16
- README와 상황판의 상단 요약을 최신 P1-B1 구현/CI 결과에 맞춰 갱신했다.
- 최신 테스트는 Run #18의 43 passed / 1 xfailed다.
- P1-B2/B3/B4는 미구현이며 승인 범위 밖이다.
- main 대비 151 ahead / 610 behind이므로 통합 감사 전 병합하지 않는다.


## 2026-11-16 통합 감사 최신 결과
- 현재 작업 브랜치 HEAD: `a7f2cd285ad89df2d0c67f14acb036e8e42a73d9`; main HEAD: `a7f2cd285ad89df2d0c67f14acb036e8e42a73d9`; merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 작업 브랜치 기준 base 대비 41 ahead / 0 behind, main 대비 152 ahead / 657 behind.
- recursive Git tree 비교(양쪽 truncated=false): merge-base 1,600 entries, main 2,257 entries. main 고유 추가 657개는 전부 `research_archive/` 아래 자동 생성 보고서이며, 삭제 0개, 변경 경로는 `history.json`, `state.json`, `research_archive/` 3개.
- main history.json 2,249개 객체, merge-base 1,592개 객체. main state.json count=110/date=2026-11-16, merge-base count=29/date=2026-11-14.
- main.py는 merge-base와 동일 SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; 작업 브랜치는 `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`. 운영 run.yml은 merge-base와 동일 SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- 운영 state/history/archive, main.py, run.yml을 변경하지 않았다. merge/rebase/PR merge/운영 실행 없음.
- 상세 근거: `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16.md`. 결론: 데이터 보존·코드 분리 통합안과 별도 승인이 있기 전까지 통합 보류.


## 2026-11-16 최신 main 자동 아카이브 반영 스냅샷
- 감사 도중 main 자동 실행 Auto-archive #111로 main HEAD가 `31e0f8137630630ee30ea55add039b571f2c6801`로 이동했다. 작업 브랜치 HEAD는 `c43abc3315d8d7c8a3d5f4fc209465428a7e8aff`.
- 최신 비교: 작업 브랜치 base 대비 42 ahead / 0 behind, main 대비 153 ahead / 658 behind.
- 최신 recursive tree 비교(양쪽 truncated=false): base 1,600 entries, main 2,258 entries. 추가 658개(모두 research_archive), 삭제 0개, 변경 파일 history.json/state.json.
- 최신 main history.json 2,250개 객체, state.json count=111. main.py 및 운영 run.yml은 merge-base와 동일 SHA.
- 앞선 수치는 조회 시점 스냅샷이며 본 최신 수치로 대체한다. 상세 보고서와 PROJECT_LOG의 정정 이벤트 참조.


## 최신 통합 감사 스냅샷 — 2026-11-16 (KST)
- 작업 브랜치 HEAD `227e3298066af4bda83fb0713fc1d57c749ee8c6`; 운영 main HEAD `036334dd2665752c2e6ddb024001771cff4064c5`; merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 작업 브랜치 기준 base 대비 44 ahead / 0 behind, main 대비 155 ahead / 660 behind.
- recursive tree 비교(양쪽 truncated=false): merge-base 1,600 entries, main 2,260 entries. archive 660개 추가, 삭제 0개, history/state 변경 2개.
- main history.json 2,252개 객체, state.json count=113. main.py SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`, 작업 브랜치 main.py SHA `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- 자동 조사/아카이브 운영은 main에서 계속된 흔적이 있으나 P0/P1-A/P1-B1 신뢰성 개선은 작업 브랜치에만 존재한다. 운영 배포로 간주하지 않는다.
- 상세: `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md`.

## P1-B2 상태 — 최신
- [완료] 사용자 승인 후 durable journal 기반 atomic persistence 구현.
- [완료] recovery target allowlist 적용: `state.json`, `history.json`, `research_archive/*.md`.
- [완료] 장애 주입 테스트 및 Actions 43851438733: 70 passed / 1 xfailed.
- [보류] PR 생성/merge와 운영 배포는 별도 승인 대상.


## 2026-11-16 운영 모니터링 설정
- ChatGPT 예약 작업 `매일 Git 브랜치 통합 상태 점검` 생성 완료. ID `6afacb7561d8819182728a42ffd4e867`, 매일 09:00 Asia/Seoul, 첫 실행 2026-11-17 09:00.
- refs/ahead-behind/recursive tree/state-history-archive 변경을 재조회한다. 안전할 때만 작업 브랜치의 상황판·로그 문서를 갱신한다.
- 운영 main/data/workflow 수정, merge/rebase/PR merge, 실제 Gemini/Discord 호출은 금지한다.
- 이 예약 작업은 ChatGPT의 모니터링이며 GitHub Actions 운영 workflow와 별개다.


## 2026-11-16 재개 시점 원격 상태 재확인
- 작업 브랜치 HEAD: `7383385e7dd8b7abcdba5c72e70ce5cf78dfb2a7` (조회 기준).
- 운영 main HEAD: `c2936e9484a44d76dc60ff811e4b904c89cf742f` (Auto-archive: Research report #124).
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; compare 기준 작업 브랜치 157 ahead / 671 behind, status diverged.
- 운영 main의 `state.json`: date `2026-11-16`, count `124`, blob SHA `e8b5d8a0797f985de437e62bdce4e399bb68de4a`.
- 운영 main의 `history.json`: top-level object 2,263개, blob SHA `c127452fadb3d9aff9074b8ac3ac2bbdd42943fc`.
- 운영 main의 `main.py` SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; 작업 브랜치 SHA `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- 운영 `.github/workflows/run.yml` SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- recursive tree 전체 비교는 이번 조회에서 수행하지 못했으므로 archive 추가/삭제 수는 미확정이다. compare API의 파일 목록을 전체 경로 목록으로 간주하지 않는다.
- 운영 main, 운영 workflow, state/history/archive 변경 없음. merge/rebase/PR merge/운영 실행/Gemini·Discord 외부 호출 없음.
- 당시 스냅샷에서는 P1-B2 구현 승인을 기다리고 있었다. 이후 사용자 승인으로 구현·CI 검증을 완료했으며 현재 상태는 아래 P1-B2 완료 섹션과 통합 전략 보고서를 따른다.


## P1-B2 구현 및 검증 완료 — 2026-11-16 (KST)
- 사용자 승인: P1-B2 원자적 로컬 저장 구현 승인.
- 전용 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16`; 구현 기준 HEAD는 기존 관리 브랜치 `7ae3b251861b9a3de9981bd7202e346d05ca9430`.
- 구현 파일: `main.py`, 신규 `persistence.py`, 신규 `tests/test_p1_b2_atomic_persistence.py`, 테스트 전용 `.github/workflows/tests.yml`.
- 동작: 시작 시 미완료 저널 복구 후 state/history 원본 bytes snapshot을 읽는다. Discord 호출 후 로컬 저장 시 snapshot SHA를 다시 확인하고 archive → history → state 순서로 transaction을 적용한다.
- 트랜잭션은 PREPARED/APPLYING/COMMITTED journal, staged payload, 기존 파일 backup, SHA 검증, 동일 파일시스템의 fsync + os.replace, 반복 가능한 roll-forward recovery를 사용한다.
- 장애 주입: 각 replace 이후 중단, PREPARED 이후 중단, stage/fsync 실패, journal/stage/backup 손상, 외부 target 변경, archive 충돌, snapshot stale, 중복 target, 잘못된 경로, 시작 시 recovery 실패 차단을 검증한다.
- 동시 실행은 POSIX advisory lock을 recovery/commit 구간에 적용하고, 장시간 외부 API 구간은 잠그지 않는다. 대신 처음 읽은 원본 bytes와 저장 직전 SHA를 비교해 stale update를 거부한다. 동시 실행에서 Discord 중복 전송을 막는 기능은 outbox 범위이므로 보장하지 않는다.
- CI Run #21은 테스트 파일 SHA pin 불일치로 source-integrity 단계에서 실패(테스트 미실행). pin을 정정한 Run #22에서 62 passed / 1 xfailed, directory fsync 및 중복 target 검증 추가 후 Run #23에서 63 passed / 1 xfailed로 최종 통과.
- Run #23: https://github.com/useformotor3/ai-discord-bot/actions/runs/43848498440
- 검증된 commit: `045b8dbeb54d8d280ab91d6219d968bfdefed107`; main.py SHA `fa8679b758916ba8a446bae41b9ec1b40328da09`, persistence.py SHA `0250152c005f4ef842119e6ddd3b305fb57d0e31`, 신규 테스트 SHA `ab832e4267e7204538af128b4759c943cc0da212`.
- 운영 main, 운영 run.yml, 운영 state/history/archive는 변경하지 않았다. 실제 Gemini/Discord 호출, 운영 Git push, merge/rebase/PR merge 없음.
- 제한: 파일시스템 durability는 POSIX fsync/flock 지원 환경을 전제로 하며, Windows 네이티브 실행은 별도 lock backend 없이는 지원하지 않는다. CI runner는 Ubuntu.
- 이전 P1-B2 구현 직후 snapshot 수치는 이후 main 자동 아카이브로 superseded 됐다. 현재 merge-base 감사 결과는 `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`와 아래 최신 통합 전략 감사 섹션을 따른다.
- 다음 단계: 최신 main ref 재조회, PR Files changed 사전 검사, PR CI/conflict check. PR 생성·merge와 운영 배포는 별도 승인 대상이며 P1-B3/B4는 보류.


## 2026-11-16 통합 전략 감사 갱신 — merge-base 기준
- 감사 스냅샷: main `267d97478b785e6bb268e224a70dbad6631cf43e` (#131), 작업 브랜치 `0fe9912b5dbba29eeb3ebd9e9f2c16a42544f925`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare: 221 ahead / 678 behind. 이 수치는 커밋 그래프 차이이며 파일 삭제 수가 아니다.
- recursive tree: merge-base 1,597 blobs(archive 1,592); main 2,275 blobs(archive 2,268); 작업 브랜치 1,620 blobs(archive 1,592).
- merge-base→main: archive 678개 추가, 삭제 0, history/state 2개 수정. main history 2,270건과 archive 2,270개가 일치하고 file 참조 누락 0.
- merge-base→작업 브랜치: 23개 경로 추가, 삭제 0, main.py 1개 수정. state/history는 merge-base와 동일한 blob.
- 결론: 3-way PR은 데이터 보존 측면에서 통합 후보가 양호하다. 실제 PR conflict check 전까지 merge 가능을 확정하지 않는다.
- P1-B2 code review에서 recovery target이 저장소 내 임의 경로를 가리킬 수 있는 점을 발견해 `state.json`, `history.json`, `research_archive/*.md` allowlist로 제한했다.
- 테스트 전용 workflow는 pull_request→main 및 main push 트리거를 갖도록 보강했다. Actions 43851438733: source SHA 일치, compileall 통과, 70 passed / 1 xfailed.
- 운영 `run.yml`, state/history/archive, main 브랜치, 실제 서비스 호출은 변경하지 않았다. PR 생성·merge·운영 배포도 하지 않았다.
- 권장 다음 단계: 최신 main 재조회 후 PR diff가 24개 예상 경로인지 확인하고, PR CI와 GitHub conflict check를 검증한다. PR/merge/운영 rollout은 별도 승인 대상.


## 2026-11-16 — 최신 원격 branch/main 비교
- 작업 브랜치 HEAD(이 스냅샷 기준): `02fde2489323f9f553405e014fac20d75d13a7fa`.
- 운영 main HEAD: `267d97478b785e6bb268e224a70dbad6631cf43e` (Auto-archive #131).
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare: 221 ahead / 678 behind, diverged; PR compare 변경 파일 24개.
- main state count=131, history=2,270, archive=2,270, 참조 누락 0.
- 이 ahead 수치는 이 스냅샷 commit 기준이며, 로그/문서 추가 commit 이후 증가한다. main 자동 아카이브도 계속 변하므로 PR 직전 재조회한다.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지. PR/merge/운영 실행은 수행하지 않았다.



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


## 2026-11-16 — Draft PR #1 생성 및 PR CI 결과
- [Draft PR #1](https://github.com/useformotor3/ai-discord-bot/pull/1) 생성 완료. base `main`, head `feature/p1-b2-atomic-persistence-2026-11-16`.
- PR head SHA: `01e7cf50436f35d9eddb931ae4e1d177af805387`; PR 생성 시 base SHA: `38abb075ebe0f7180abaebc4da52e2f18ea28915`.
- PR 생성 직전 compare: 230 ahead / 700 behind; merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- PR 변경 24개(추가 23, 수정 main.py 1, 삭제 0); 보호 운영 경로 변경 없음.
- GitHub PR 상태 재조회: open=true, draft=true, merged=false, mergeable=true.
- PR-triggered Actions Run #32 (`43869220252`) success. source integrity, compile, complete pytest job 모두 성공.
- 사전 코드 검증 Run #43851438733은 70 passed / 1 xfailed. PR-triggered Run #32는 job-level success만 확인했으며 개별 passed/xfail 수치는 확인되지 않아 혼동하지 않는다.
- PR은 검토 대기 상태다. 병합·리베이스·운영 workflow/data 변경·실제 Gemini/Discord 호출은 수행하지 않았다.
- 다음 단계: PR 리뷰/Files changed 재검토 및 main 최신화에 따른 compare/conflict 재검증. 병합과 운영 반영은 별도 승인 필요.


## 2026-11-16 — 상시 진행 승인 / 롤백 준비 현황
- 사용자 지시: 매 단계별 승인 질문 없이 필요한 작업을 계속 진행. main 및 운영 관련 파일 수정도 허용하되, 실행 후 이상 발생 시 정상 코드/데이터로 복구할 수 있어야 함.
- 행동강령 AI_RULEBOOK.md §18에 상시 진행 권한, 체크포인트, 백업, 통합 게이트, 실행 후 데이터 검증 및 실패 시 복구를 기록했다.
- 백업 브랜치 생성: safety/pre-merge-main-2622e332 → 2622e332d6a3defd2079ccad3af36970001de5c1; safety/pre-merge-feature-eba3aeb → eba3aeb5710dcc6507623d56d586a619e9a4fc46.
- main HEAD 2622e332d6a3defd2079ccad3af36970001de5c1; feature HEAD eba3aeb5710dcc6507623d56d586a619e9a4fc46; compare 231 ahead / 703 behind; merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- PR mergeable 응답은 false→true로 변동했고 PR base SHA가 main 최신 HEAD와 불일치하는 값을 반환했다. PR head 기준 CI는 성공이나 최신 main을 포함한 통합 결과 CI로 간주하지 않는다.
- 복구 준비 평가: (1) 코드 이력/백업 브랜치 생성 완료, (2) 운영 데이터 snapshot/restore 검증 미완료, (3) main 통합 및 첫 운영 실행 미실행. 따라서 현재 코드 롤백 기준점은 있으나 운영 데이터까지 복구 준비 완료라고 말할 수 없다.
- 다음 우선순위: backup refs readback → main 최신 base 기준 통합/CI 확인 → state/history/archive 사전 백업 및 복원 리허설 → PR merge commit 통합 → post-merge 검증 → 제한된 첫 실행 및 데이터 무결성 확인.

## 2026-11-16 — 운영 데이터 기준선 #158 및 복구 상태
- 고정 main SHA 4cf0e708b28a343898af00d01521044dfb9a1987.
- 동일 SHA에서 state count=158, history=2,297, archive=2,297, 참조 누락 0. tree 2,305 entries, truncated=false.
- safety/pre-merge-main-4cf0e70 readback SHA exact match.
- U+200B가 앞에 붙은 별도 state 파일(date=2026-06-07,count=0, blob=de8505bdcb7709a96a4fe89edf124f9ad1917ce8)을 삭제하지 않고 보존.
- 이전 moving-ref 불일치는 immutable SHA 재검사에서 재현되지 않아 snapshot race로 정정.
- per-run 자동 snapshot/restore는 아직 미구현/미검증. 상세 reports/ROLLBACK_AND_DATA_BASELINE_AUDIT_2026-11-16.md.

## 2026-11-16 — 운영 rollback guard 및 최신 통합 검증
- feature HEAD 8ad2364992cfd0e4f60108d4bfcdf36e99d9131e; main HEAD f5b5a112ec72b01f8b3f91f734b8d755dde416c6.
- compare 239 ahead / 708 behind; merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7; changed paths 28.
- PR #1 latest base/head exact match, mergeable clean at last check. Run #43874801395 success: 86 passed, 1 xfailed, compileall passed.
- production workflow pre-run checkpoint and post-run guarded data-only restore implemented. No actual Gemini/Discord/production execution yet.
- code/data backups: safety/pre-merge-main-f5b5a11 and safety/pre-merge-feature-8ad2364; both readback exact.


## 2026-11-16 — final integration readiness snapshot
- feature code/test/workflow head abee2a88f7e0bbfad0ad483c6b50cea63e26b871; documentation/log commits may advance head thereafter.
- main #162 adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890.
- PR compare at snapshot 241 ahead / 709 behind, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7, 28 changed paths. No state.json/history.json/research_archive paths in PR diff.
- PR mergeable clean at last refresh; Run #43875746973 on exact main #162 base passed 87 tests with 1 expected xfail.
- Merge method: merge commit. Never squash/rebase/force-push. Keep safety refs and run first production execution only after merge verification.

## 2026-11-16 — PR #1 merge 이후 상황
- PR #1 merge commit 6fd03efaf8623cb3ec2ab938aa7161b41ffed82e; parent main #162 adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890; parent feature d48ae1c9b655d7384aff497c9d17168a5d0b25c5.
- post-merge backup safety/post-merge-main-6fd03ef exact SHA readback.
- push CI Run #43876347620 success (87 passed, 1 xfailed, compileall passed).
- same commit data integrity: state=162, history=2,301, archive=2,301, missing refs=0; state/history blobs unchanged from pre-merge baseline.
- PR #1 closed/merged. production run.yml changed, but merge push triggered only isolated test workflow. No real Gemini/Discord call or production run.
- Next: observe first explicitly triggered production run and verify pre-run checkpoint plus post-run guard.


## 2026-11-17 — GitHub 자동화 점검 및 체크포인트 누적 개선
- 원격 Actions 최근 20건은 조회 당시 completed/success였으나, #2412는 현재 작업 중 main 커밋이 추가된 경합으로 실패했다.
- #2412: 로컬 보고서 #235 commit 생성, Discord 2/2 chunks 전송, Git push는 non-fast-forward(fetch first) 거부. operational_guard는 remote main 불일치로 자동 복구를 거부했다. 보고서 #235는 원격 history/archive/state에 반영되지 않았다.
- 실행별 safety/data-pre-run 브랜치 94개 확인. 성공 실행 이후에도 무제한 누적되는 구조를 결함으로 분류.
- main 변경 전 백업: safety/pre-checkpoint-prune-1abfcfb → 1abfcfb26a8b414dc75eb584082ed35cab0d6412.
- main commit b89f2bf58752045361fa088a6fc4311ba8798fcb에 성공 실행에서만 최근 30개 체크포인트를 남기고 현재 baseline ref를 보호하는 pruning step 및 스크립트를 추가했다.
- 첫 CI Run 43959203356: compileall 통과, pytest 96 passed / 1 failed / 1 xfailed. 실패는 보호된 오래된 ref 테스트의 기대값 오류이며 수정 후 재검증한다.
- 아직 실제 checkpoint pruning은 실행되지 않았다. CI 통과 후 다음 정상 운영 실행에서만 실행되도록 구성했다.
- 이후 main 변경은 활성 production run 종료 확인 후 수행한다. #2412 Discord 전송은 회수할 수 없으므로 후속 보고서 count 중복 가능성을 추적한다.


## 2026-11-17 최신 운영 점검
- 최신 main 확인 시점 SHA: 514eebd9a7e96cafa16fe59107b1b840d51667f1 이후 자동 아카이브 커밋 1건 추가.
- 운영 run #2431(43974577082): success, guard 성공, checkpoint pruning 성공.
- pre-run checkpoint refs: 30개 유지, 현재 실행 baseline 포함.
- 데이터: state count=253(당시 일일 카운트), history=2,392, archive=2,392, 참조 누락 0.
- 발견: GitHub runner UTC 기준으로 TODAY/NOW 생성. KST 날짜 경계가 9시간 어긋날 수 있음. main.py를 Asia/Seoul 기준으로 수정.
- Gemini model catalog 확인: gemini-3.8-flash 및 gemini-3.5-flash-lite 사용. 404/NOT_FOUND 즉시 fallback.
- Git add/commit/push 오류는 warning 후 계속하지 않고 main.py exit 1로 처리. 강제 push/rebase 금지.
- 변경 후 CI 대기/검증 예정. 실제 Gemini/Discord 운영 호출은 수행하지 않음.

- KST/모델/Git 저장 실패 개선 commit: fc77d6da07684936a27a60eb1a4cb920ceb37c14.
- CI Run #59: 성공, 99 passed / 1 xfailed; source SHA 검사·compileall·전체 pytest 통과. Run #58은 모델명 기대값이 구형이라 2건 실패했고, 테스트 수정 후 Run #59에서 재검증 통과.
- 변경 후 실제 Gemini/Discord API 운영 실행은 아직 없음. 다음 production run에서 KST date/count, 신규 model id, 정상 Git push를 관찰해야 함.
- 현재 데이터 readback: state count=254(기존 UTC 기준 값, 새 KST 로직 미적용 실행 기준), history=2,393, archive=2,393, 참조 누락 0. checkpoint refs=30.


## 2026-11-17 — KST 적용 후 운영 데이터 readback
- main 관찰 HEAD: `655bde43483f4c2e793954e4206590d768e6ab74`.
- `state.json`: date=2026-11-17, count=4.
- `history.json`: 전체 JSON 파싱 성공, 2,397개 항목.
- 당일 마지막 4개 history: 08:05:32 / 08:10:37 / 08:15:40 / 08:20:40 KST, count 1~4.
- 해당 4개 archive 파일을 각각 원격에서 재조회했고 모두 존재한다.
- 보고서 #1~#4 자동 아카이브 커밋을 확인. #4 commit diff에서 history append, archive 생성, state count 3→4를 확인했다.
- 따라서 KST 날짜·일일 카운트·원격 archive 저장은 운영 데이터로 확인됨.
- 운영 Job 상세 로그는 현재 조회하지 못했다. 실제 Gemini 모델 ID, operational_guard, checkpoint pruning, Discord 응답 상태는 미확인으로 유지한다.
- 상세 증거 및 제한: `reports/PRODUCTION_RUN_OBSERVATION_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #4 표본 감사 결과
- 원본 `research_archive/2026-11-17_082040817286_b5f20b1f.md`는 보존했다.
- 중대 정정: CRA 삭제 요건은 Annex I Part I (2)(m), 원본 (2)(i) 인용은 오기. (2)(i)는 서비스 가용성 영향 최소화 항목.
- IEC 62443-4-2 CR 4.1은 정보 기밀성, CR 4.2는 정보 잔존/삭제, CR 4.3은 암호기술 사용으로 구분.
- NIST SP 800-88 Rev.1은 2025-09-26 철회되어 Rev.2로 대체. Flash multi-pass overwrite 권고는 삭제/재작성 필요.
- 하드웨어·펌웨어 강제, CE 필수 등 법령에 명시되지 않은 구현 단정은 권고 수준으로 재분류.
- 정정 상세: `reports/CRA_CORRECTION_REPORT_4_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #3 표본 감사 결과
- 원본 `research_archive/2026-11-17_081540588844_6957403e.md` 보존.
- 중대 정정: Article 13(8)은 취약점 처리 지원 기간 및 최소 5년 원칙(제품 예상 사용 기간이 더 짧으면 그 기간)이며, 보안 업데이트의 분리 제공은 Annex I Part II (2), 무상 제공은 Part II (8).
- Article 13(9)의 업데이트 장기 이용 가능성(최소 10년 또는 지원 기간 잔여기간 중 더 긴 기간) 누락 확인.
- Annex I Part II (4)의 취약점 정보 공개 요건과 CVE/CSAF의 비의무적 권고 지위를 구분.
- 자동 rollback/Safe State는 CRA가 모든 제품에 직접 지정한 요구가 아니며, 서보 드라이브 위험분석 기반 엔지니어링 검증 항목으로 분류.
- IEC 62443-4-1 Practice 7은 주제상 연결되나, 정식 라이선스 표준 전문 대조 전 세부 적합성 판단 보류.
- 상세: `reports/CRA_CORRECTION_REPORT_3_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #2 표본 감사 결과
- 원본 `research_archive/2026-11-17_081037059553_f43b5252.md` 보존.
- Article 11은 General product safety. CVD 정책/접수 연락처는 Article 13(8)/(17), Annex I Part II (5)/(6), Annex II (2).
- Article 14 공식 제목은 Reporting obligations of manufacturers. 원본 Article 11 인용문은 공식 원문과 일치하지 않음.
- actively exploited vulnerability: 24h early warning, 72h notification, 시정·완화 조치 가용 후 14일 final report.
- severe incident: 24h early warning, 72h incident notification, incident notification 제출 후 1개월 final report.
- 단일 신고 플랫폼, coordinating CSIRT/ENISA 동시 통지, 사용자 통지, Article 14 적용일 2026-09-11 및 Article 69(3) 경과규정 확인.
- Annex II는 사용자 지침, Annex VII가 기술문서.
- 상세: `reports/CRA_CORRECTION_REPORT_2_2026-11-17.md`.


## 2026-11-17 — CRA 보고서 #1 표본 감사 결과
- 원본 `research_archive/2026-11-17_080532833611_7d315e0a.md` 보존.
- Article 11은 General product safety이며 제조사 의무 조항이 아님. Article 13(8)은 support period, Annex I Part II (8)은 보안 업데이트 무상 제공(맞춤형 제품 business-user 합의 예외).
- CVD 정책/접수 연락처/안전한 업데이트 배포는 Annex I Part II (5)–(7), Article 13(17), Annex II (2).
- 디지털 서명은 무결성·안전 배포 구현 수단이지 CRA가 모든 제품에 직접 지정한 단일 암호방식은 아님.
- 실시간 제어 중단 없는 설치 또는 STO 상태 설치도 법령의 보편적 설치 절차가 아니라 제품 위험분석·기능안전 영향평가 항목.
- Annex I Part I(제품 속성)와 Part II(취약점 처리) 구조를 구분.
- 상세: `reports/CRA_CORRECTION_REPORT_1_2026-11-17.md`.
## 2026-11-17 — 운영 5분 반복 실행 및 조사 품질 게이트 개선

- main 최신 기준 archive #38, state count=38, history/archive=2,431개. 최근 #33–#38의 원본을 직접 재조회하고 #33–#38 정정 보고서 작성.
- #33/#35/#37/#38은 취약점 처리·무상 업데이트·지원기간 주제가 중복됐고, #34는 Annex II/Annex VII 및 제품 분류 혼합, #36은 Article 14의 final-report 시계 혼합을 확인.
- PR #10 merge commit `2e583f5c7b24743fbb1bd7d375643e314cf3115d`: EUR-Lex 공식 링크 누락 거부, 최근 30개 archive 주제 중복 차단, 최근 15개 이력 프롬프트 제공.
- PR #10 CI Run #455: **101 passed, 1 xfailed**; exact blob SHA/compileall/full pytest success.
- 다음 cadence PR branch `fix/production-cadence-2026-11-17`: 외부 repository_dispatch trigger 제거, 매시간 정각 UTC schedule 및 manual dispatch 유지. PR CI 후 병합 대기.
- 원본 archive/state/history는 변경하지 않았다. cadence 변경 후 첫 3회 hourly run을 별도 관찰한다.
- 상세: `reports/PRODUCTION_AUTOMATION_QUALITY_AND_CADENCE_AUDIT_2026-11-17.md`.

## 2026-11-17 — Gemini 무료 quota 장애 원인 및 cadence 재조정
- 운영 Run ID `44016487535`의 실패 로그를 직접 확인했다. `gemini-3.8-flash`는 Free Tier `generate_content_free_tier_requests` 일일 한도 20회 초과(HTTP 429 RESOURCE_EXHAUSTED), fallback `gemini-3.5-flash-lite`는 HTTP 503 UNAVAILABLE 및 EUR-Lex 링크 누락 응답을 반환했다.
- 기존 main.py는 quota/503을 동일 모델에서 3회 반복하고, 품질 거부 후에도 workflow 실패로 종료하는 문제가 있었다.
- cadence PR에서 모델별 최대 2회 시도, 429/503은 즉시 같은 모델 재시도 중단 후 fallback, 품질 거부/할당량/일시 과부하는 부작용 없는 정상 no-op으로 처리하도록 보강했다. 인증/설정 등 미분류 치명 오류는 계속 exit 1.
- 실행 주기는 매 3시간(UTC 정각)으로 조정했다. 8회/일 × 모델당 최대 2회 = 최대 16회/일/모델의 이론상 상한으로 20회 Free Tier 제한 아래에 여유를 둔다.
- CI 재검증 대기 중이며 PR #11은 아직 main에 병합하지 않았다.
## 2026-11-17 — 운영 cadence·quota·복구 체계 최종 반영

- 운영 main 최신 기준: merge commit `bef260a29481320de3eae9cafe4a6f907e38ead0`.
- PR #10: 공식 EUR-Lex 링크 누락 거부 + 최근 30개 원문 기반 중복 주제 차단. CI #455 **101 passed, 1 xfailed**.
- PR #11: 외부 `repository_dispatch` 제거, 내부 schedule `0 */3 * * *`(3시간 간격, 8회/일), Gemini 모델별 최대 2회, 429/503/품질 거부 clean no-op. CI #467 **103 passed, 1 xfailed**. merge `21c6add0c58de39fbc2755882885bffe2cd44394`.
- PR #12: 실패 후에도 pre-run checkpoint 기반 operational guard 실행, uncommitted/unpublished 데이터 복원, guard 성공 시에만 checkpoint prune, GitHub 저장 후 Discord 전송. CI #470 **105 passed, 1 xfailed**. merge `bef260a29481320de3eae9cafe4a6f907e38ead0`.
- 마지막 확인된 production state: count=38, history=2,431, state SHA `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, history SHA `b9ea42fa437b2b3a5728db5d125d287fb746b46b`. Quota 장애 run #44016487535 이후에도 state/history/archive 변경 없음.
- CRA archive #33–#38 정정 보고서가 main에 보존되어 있다. 원본 archive는 수정하지 않았다.
- 다음 단계: 첫 3회 3-hourly production run의 실제 결과, quota handling, guard, pruning, archive 참조 무결성을 관찰한다. 이후 CRA 통합 한국어 보고서와 CRA 요구사항 추적표를 작성·검증한다. SIL 3는 활성 다음 단계에서 제외.
- 상세: `reports/PRODUCTION_AUTOMATION_QUALITY_AND_CADENCE_AUDIT_2026-11-17.md`.

## 2026-11-17 — CRA archive #1–#38 정정 감사 통합
- 기존 main의 정정 #1–#4와 #33–#38에 더해, 이전 integration branch의 정정 #5–#21을 main 통합 후보로 복사하고 #22–#32를 EUR-Lex 최종 OJ와 대조해 신규 작성했다.
- 정정 보고서 #1–#38 전체를 한 인덱스로 정리: `reports/CRA_CORRECTION_INDEX_2026-11-17.md`.
- 주요 발견: Article 10/11을 제조사 의무로 오인, Article 24를 사용자 지침 조항으로 오인, Annex VI/VII 혼동, 기본 credential 문구의 비원문 인용, CVD와 mandatory reporting 혼합, Article13(8)/(9) 지원기간·업데이트 보존 혼합, Annex III 제품 등급 과장, logging/CVD 파트 혼합.
- 모든 원본 archive는 수정하지 않았으며 정정 문서만 추가했다. PR #14에서 main 병합 전 검증한다.

## 2026-11-17 — CRA 정정 #1–#38 main 통합 완료

- PR #14 merge: `6994e4828a03482713f7990c7f82036bacfe4772`; CI #474 **105 passed, 1 xfailed**.
- main에서 `CRA_CORRECTION_REPORT_1`부터 `CRA_CORRECTION_REPORT_38`까지 38개 파일의 존재를 개별 확인했다.
- #22–#32 원본 archive 11개 blob SHA를 재조회해 감사 시점과 동일함을 확인했다. #33–#38도 기존 SHA 보존.
- state.json SHA `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, history.json SHA `b9ea42fa437b2b3a5728db5d125d287fb746b46b` 유지. state count=38, history entries=2,431.
- [CRA 정정 인덱스](reports/CRA_CORRECTION_INDEX_2026-11-17.md) main 반영 완료.
- 대체된 Draft PR #3/#6은 정정 문서와 기능이 PR #10–#14로 main에 통합되어 close 처리했다. 소스 작업은 버리지 않았으며 correction #5–#21도 main에 존재한다.
- 남은 운영 검증: 3시간 주기 첫 3회 production run의 Gemini quota, clean no-op, recovery guard, checkpoint pruning 및 archive/state/history 무결성 확인.

## 2026-11-17 — SIL 3 서보 드라이브 벤치마킹/하드웨어 설계 v0.1 작성
- [벤치마킹 보고서](reports/SIL3_SERVO_DRIVE_BENCHMARK_REPORT_2026-11-17.md): Mitsubishi MELSERVO-J5, Yaskawa Sigma-7 ASM7, Rockwell Kinetix 5700, Siemens SINAMICS S210을 공식 제조사 자료로 비교.
- [하드웨어 블록 설계](design/SIL3_SERVO_DRIVE_HARDWARE_BLOCK_DESIGN_2026-11-17.md): 전력 스테이지, 독립 safety CPU/FPGA, 이중 STO, 안전 피드백, SBC/기계 브레이크, 안전 통신, 보안 경계, 시험 계획.
- [요구사항 추적성 매트릭스](reports/SIL3_SERVO_DRIVE_REQUIREMENTS_TRACEABILITY_2026-11-17.md): 기능안전 FS와 CRA 사이버보안 CYB 요구사항을 분리.
- 표준 업데이트: IEC 61800-5-2 AMD1:2026(2026-10-30), IEC 62061 AMD2:2026(2026-03-20), ISO 13849-1:2023 확인. IEC 61508-1 Ed.3 PRV는 최종 발행 전.
- 제품 PFH 값은 범위가 서로 달라 직접 순위화하지 않았다. 드라이브/모듈 PFH와 전체 안전 기능 PFH를 구분했다.
- 현재 문서는 v0.1 reference architecture다. 전압, 출력, 축 수, 모터/엔코더, 안전 기능 및 F-PLC/네트워크가 확정되기 전 최종 회로도/BOM/PFH를 단정하지 않는다.

- 추가 발견: Rockwell PSA 2017-01-001은 특정 Kinetix 5700 ERS3 firmware의 hardwired STO에서 SIL PFH 미달 가능성을 공지한다. 영향 모델/firmware와 수정 버전 V7.003 이상을 보고서에 반영했으며 ERS4에 일반화하지 않는다.

## 2026-11-17 — SIL 3 서보 드라이브 산출물 v0.1 main 병합
- PR #16 merge commit: `34449753857c6ab004271f69aac19867a7aed1fa`.
- CI Run #488: **105 passed, 1 xfailed**.
- Main에 벤치마킹 보고서, 하드웨어 reference block design, FS/CYB traceability matrix 및 spreadsheet-ready CSV 비교표 반영.
- CSV: `reports/SIL3_SERVO_DRIVE_BENCHMARK_MATRIX_2026-11-17.csv`.
- 범위는 1축 reference architecture. 정격/부하/축 수/encoder/네트워크/안전 기능 확정 전 최종 회로도/BOM/PFH 계산은 보류.
- 제조사별 2026-10-30 IEC 61800-5-2 AMD1 적용 인증서 및 실제 installed firmware/옵션은 공급사 확인 필요.


## 범위 정정 기록 — 2026-11-17

- README, 마스터 계획 및 세션 로그에 SIL 3를 CRA의 후속 작업으로 기재한 문구는 활성 프로젝트 범위와 불일치했다.
- 현재 사용자 지시를 반영해 CRA만 활성 범위로 확정했다. SIL 3 산출물은 과거 자료로 링크와 커밋 이력을 보존하되 비활성 상태로 분리했다.
- PR #16의 과거 병합 사실은 삭제·부정하지 않는다. 해당 병합은 CRA 범위 승인이나 CRA deliverable의 일부를 의미하지 않는다.
- 재개 시 우선순위: (1) 이 범위 통제 확인, (2) GitHub 최신 상태/CI/미완료 작업 재검증, (3) CRA 통합 보고서 및 요구사항 추적 작업.

## 2026-11-17 — CRA 공식 source provenance 파이프라인 PR #26 병합

- PR #26 [CRA: integrate CELLAR official-source retrieval and claim-level traceability](https://github.com/useformotor3/ai-discord-bot/pull/26) merge 완료.
- Merge commit: `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`; 구현 브랜치 `experiment/cellar-source-retrieval-2026-11-17`는 감사/복구를 위해 유지.
- 기존 PR #25는 PR #26에 동일 변경과 후속 검증이 포함되어 중복 정리했다. 코드 변경은 PR #26에 모두 포함된다.
- 변경 파일 9개: `.github/workflows/tests.yml`, `cra_source.py`, `cra_claims.py`, `main.py`, `tests/conftest.py`, `tests/test_main_characterization.py`, `tests/test_cra_source.py`, `tests/test_cra_claims.py`, `tests/test_external_failure_paths.py`.
- EUR-Lex 직접 HTTP 202/자동화 접근 응답을 정상 원문으로 처리하지 않고, Publications Office 공식 CELLAR REST API로 법령·정오표·위임규정 7건 수집 경로를 전환했다. Commission 공식 안내/표준화 페이지 2건을 추가해 총 9개 source를 검증했다.
- source별 요청/최종 URL, 수집 시각, visible text 길이, 전체 visible text SHA-256, prompt excerpt SHA-256을 manifest에 기록한다.
- CELLAR redirect는 같은 allowlist host만 허용하고 HTTP redirect는 HTTPS로 승격한 뒤 재요청한다. source timeout/202/빈 응답은 외부 부작용 없는 safe no-op, TLS/host/content validation 오류는 fail-closed 처리한다.
- claim validator는 claim ID/본문 statement/source ID/직접 quote/Article paragraph/Annex Part-point locator를 검증한다. 동일 Article의 다른 paragraph quote는 거부한다.
- [Actions Run #573](https://github.com/useformotor3/ai-discord-bot/actions/runs/44039961078): **138 passed, 1 xfailed**. 9개 공식 source 실시간 수집 및 Article 13(8) paragraph locator/quote 일치 확인.
- 테스트 실행 대상 PR head: `d1bda523c1b593bbd48bf4916dd7bbd741001894`. merge commit 자체의 별도 Actions run은 확인되지 않아 post-merge CI success로 확대 주장하지 않는다.
- Commission Guidance PDF/Annex 및 M/606 결정 C(2026) 7861 Annex는 관련 URL만 manifest에 기록했다. PDF/결정문 원문 파싱은 미완료이며 source page summary로 Annex 내용을 입증했다고 주장하지 않는다.
- 제품 모델/회로/펌웨어/프로토콜/시장 공급 구조가 없으므로 모델별 CRA 적용성·분류·적합성 결론은 여전히 잠정이다.
- 상세 설계·source IDs·SHA-256·검증·한계: [CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md).
- 다음 재개: (1) PDF/decision Annex 수집·검증, (2) Article/Annex locator canary 확대, (3) 35 requirements/15 interfaces/36 SEC controls를 source claims 및 제품별 증거와 연결, (4) main merge commit CI 및 관리 문서 재확인.


## 2026-11-17 — CRA 프로젝트 기록 동기화 PR #27 병합

- PR #27 [docs: synchronize CRA source provenance status, rules and resume point](https://github.com/useformotor3/ai-discord-bot/pull/27) merge 완료.
- Merge commit: `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`.
- [Actions Run #575](https://github.com/useformotor3/ai-discord-bot/actions/runs/44040949610): 138 passed / 1 xfailed, 9개 live official source 및 Article 13(8) locator/quote canary 재통과.
- README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG.jsonl과 source provenance 상세 보고서를 동기화했다.
- JSONL 76개 레코드 parse success, 신규 event ID 확인, source excerpt SHA-256 9개가 각각 64 hex임을 readback했다.
- PR #27 pre-merge ref `safety/pre-merge-main-pr27-2026-11-17` → `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`; post-merge ref `safety/post-merge-main-pr27-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`. 두 ref 모두 SHA readback 검증 완료.
- merge commit 자체의 별도 Actions run은 아직 확인되지 않았다. PR head Run #575 성공으로만 기록한다.
- 다음 재개는 PDF/decision Annex 수집, Annex/Article locator canary 확대, 요구사항·통제·제품 증거 연결이다.


## 2026-11-17 — PR #28 최종 복구 체크포인트 및 main 상태 readback

- PR #28 [docs: finalize PR27 rollback checkpoints and project readback](https://github.com/useformotor3/ai-discord-bot/pull/28) merge 완료.
- Merge commit: `942e1e6b5f2887001279a96c21f94138d283a689`.
- [Actions Run #577](https://github.com/useformotor3/ai-discord-bot/actions/runs/44041626911): 138 passed / 1 xfailed, 9개 official source live fetch 및 Article 13(8) locator/quote canary 통과.
- PR #28 pre-merge ref `safety/pre-merge-main-pr28-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; post-merge ref `safety/post-merge-main-pr28-2026-11-17` → `942e1e6b5f2887001279a96c21f94138d283a689`. 두 ref 모두 SHA readback 검증 완료.
- merge commit 자체의 별도 Actions run은 확인되지 않았다. PR head Run #577 결과만 기록한다.
- 변경은 문서/로그/복구 기준점에 한정되며 운영 코드, workflow, state/history/archive, Gemini/Discord 외부 동작은 변경하지 않았다.


## 2026-11-17 — CRA 정오표 우선순위 검증 PR #29 병합

- PR #29 [fix: verify consolidated CRA text reflects operative corrigenda](https://github.com/useformotor3/ai-discord-bot/pull/29) merge 완료.
- Merge commit: `9c16724b8b72bd09d3492b19ff714602b235c66b`.
- Article 64(10): 2025-07-02 R(02)의 정정 후 문구 `paragraphs 2 to 9`를 prompt excerpt에서 확인하고, 정정 전 `paragraphs 3 to 9`가 남아 있으면 해당 Article block 안에서만 교체한다.
- Article 67: 2025-10-17 R(04)의 정정 후 참조 `72. Regulation (EU) 2024/2847`를 확인하고, 정정 전 `69.`가 남아 있으면 해당 Article block 안에서만 교체한다.
- 정오표 source ID의 전/후 문구, 대상 Article, 중복 여부를 확인한다. source 또는 문구가 누락·모호하면 fail-closed.
- raw visible-text SHA-256은 수집 원문 그대로 유지하고, 적용/확인된 prompt excerpt SHA-256을 재계산한다. manifest에 적용/확인 정오표 ID와 변경 설명을 기록한다.
- [Actions Run #596](https://github.com/useformotor3/ai-discord-bot/actions/runs/44043479661): **141 passed, 1 xfailed**; 9개 공식 source fetch, Article 64(10)/67 corrigenda precedence, Article 13(8) locator/quote canary 통과.
- PR #29 pre-merge ref `safety/pre-merge-main-pr29-2026-11-17` → `9ad730c42de6451ce6942298e9b17e3e82a3ef62`; post-merge ref `safety/post-merge-main-pr29-2026-11-17` → `9c16724b8b72bd09d3492b19ff714602b235c66b`. 두 ref SHA readback 검증 완료.
- PR head Run #596은 확인했으나 merge commit 자체의 별도 Actions run은 확인되지 않았다.
- 운영 Gemini/Discord workflow, state/history/archive 및 SIL 3 과거 산출물은 변경하지 않았다.
- 다음: Commission Guidance PDF/Annex 및 M/606 C(2026) 7861 decision Annex 원문 수집, Annex I live locator 확대, 35 requirements/15 interfaces/36 SEC controls의 source claim·제품 증거 연결.


## 2026-11-17 — Commission Guidance 및 M/606 Annex 1차 감사

- 작업 브랜치: `cra/official-annex-audit-2026-11-17`; 생성 기준 main SHA `80245d9e132380a10581612c031f87869993b98d`.
- 신규 보고서: `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md`.
- Commission Guidance C(2026) 5252 Annex의 PDF text layer를 확인하고 §2.4–2.7, §4, §5, §6, §7, §8, §9.3.2의 서보 드라이브 관련 locator/해석을 정리했다.
- Guidance §2.5 paras. 26–28은 encoded digital information을 데이터 연결 기준으로 설명한다. 단순 전기 신호/trigger와 디지털 정보 교환을 구분하도록 인터페이스 매트릭스 보강 근거를 확보했다.
- Guidance §6은 Annex III/IV 분류가 제품명/내장 구성요소가 아니라 제품 전체 core functionality에 달렸음을 확인했다. §8은 RDPS 3개 누적 조건과 industrial robot 예시를 제공한다.
- C(2026) 7861 Annex I에서 41개 표준 주제와 ESO adoption deadline을 추출했다. 항목 18의 날짜 셀은 text extraction에서 판독 불가로 미확인 유지.
- **검증 한계:** Commission-hosted C(2026) 5252 PDF와 C(2026) 7861 Annex PDF의 원본 바이너리 다운로드 및 SHA-256은 실행환경에서 실패했다. PDF text layer 내용 감사는 완료했으나 원본 byte identity/해시는 미검증이다. Guidance PDF는 ANFR mirror를 통한 text layer를 확인했으며 Commission download와 byte-for-byte 동일성은 확인하지 않았다.
- 법적 구속력, ESO adoption deadline, harmonised standard OJ citation, CRA application date를 구분한다. 표준화 기한을 제품 적합성 완료 기한으로 해석하지 않는다.
- 운영 코드/workflow/state/history/archive, 운영 Gemini/Discord는 변경·실행하지 않았다. SIL 3 과거 자료도 변경하지 않았다.
- 다음: M/606 item 18 PDF 시각 확인, 원본 PDF 바이너리/해시 취득 경로 확보, Guidance §2.5/§6/§8을 15개 interface/35개 requirement/36개 SEC control에 claim-level 연결, Annex I locator canary 확대.


## 2026-11-17 — PR #30 격리 CI 트리거 준비

- PR #30 `https://github.com/useformotor3/ai-discord-bot/pull/30`을 생성하고 ready-for-review 상태로 전환했다.
- PR branch의 `.github/workflows/tests.yml` push branch allowlist에 `cra/official-annex-audit-2026-11-17`만 추가했다. 이 workflow는 `permissions: contents: read`의 격리 테스트 전용이며 운영 `run.yml`은 변경하지 않았다.
- 변경 후 main 대비 9 commits ahead / 0 behind, 8개 변경 경로이며 변경 범위는 보고서·관리 문서·JSONL 및 테스트 workflow 1줄이다.
- GitHub workflow run/status 조회에서는 현재 head의 CI 결과가 아직 보이지 않는다. 따라서 CI 통과나 merge 완료를 주장하지 않으며 PR #30은 미병합 상태로 유지한다.


## 2026-11-17 — PR #30 병합 완료

- PR #30 [CRA Guidance/M/606 Annex 1차 감사](https://github.com/useformotor3/ai-discord-bot/pull/30) 병합 완료.
- Merge commit: `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`.
- [GitHub Actions Run #610](https://github.com/useformotor3/ai-discord-bot/actions/runs/44050954456): success — **141 passed, 1 xfailed**, compileall, exact source blob identity, 9개 공식 출처 live fetch, Article 64(10)/67 corrigenda 및 Article 13(8) locator/quote canary 통과.
- Pre-merge ref `safety/pre-merge-main-pr30-2026-11-17` → `80245d9e132380a10581612c031f87869993b98d`; post-merge ref `safety/post-merge-main-pr30-2026-11-17` → `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`; readback compare에서 main과 post-merge ref 동일 확인.
- PR #30 범위: 한국어 CRA 감사 보고서, 관리 문서·로그 동기화, 격리 테스트 workflow push branch allowlist 1줄. 운영 애플리케이션 코드, 운영 `run.yml`, state/history/archive, Gemini/Discord 외부 실행 및 SIL 3 과거 산출물은 변경하지 않았다.
- M/606 Commission PDF 및 Guidance ANFR mirror raw-byte SHA-256 검증 완료. M/606 item 18 deadline 31/01/2027 시각 확인 완료. Guidance Commission primary byte identity는 미확인.
- 현재 구현 작업 브랜치: `cra/requirements-legal-locator-audit-2026-11-17` (CRA-001~CRA-035 법령 Article/Annex locator 전수 대조).


## 2026-11-17 — PR #31 사후 동기화 완료

- PR #31 merge commit: `24312166b892127e845721793b1abfee4d91f9c2`.
- [Actions Run #618](https://github.com/useformotor3/ai-discord-bot/actions/runs/44051283237): success, 141 passed / 1 xfailed; compileall, source blob identity, 9-source live canary 및 Article 13(8) locator/quote 통과.
- Pre-merge ref `safety/pre-merge-main-pr31-2026-11-17` → `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`; post-merge ref `safety/post-merge-main-pr31-2026-11-17` → `24312166b892127e845721793b1abfee4d91f9c2`. post ref와 main compare identical 확인.
- 현재 구현 작업 브랜치: 없음. 다음 구현은 PR #34 사후 동기화 후 최신 main을 조회하고 새 작업 브랜치에서 시작한다.


## 2026-11-17 — Guidance claim mapping 및 PDF source acquisition 구현 중

- 작업 브랜치 `cra/guidance-claim-mapping-2026-11-17`는 최신 main에서 생성했다.
- 신규 [Guidance claim register](reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv): G-001~G-013, 모두 `official_explanation`이며 법적 요구사항으로 취급하지 않는다.
- 기존 매트릭스에 Guidance claim ID와 M/606 Annex I 조건부 후보 항목 열을 추가했다: 인터페이스 15행, CRA 요구사항 35행, SEC 통제·시험 36행.
- G-002 (§2.5 paras. 26–28)는 인코딩된 디지털 데이터 연결과 단순 electrical trigger를 구분한다. G-007 (§6/6.1) core functionality, G-010/011 (§8) RDPS, G-006 support period, G-012 Machinery Regulation interplay 등을 연결했다.
- `cra_pdf_sources.py`와 `tests/test_cra_pdf_sources.py`를 추가했다. Commission PDF URL에서 원본 bytes를 취득하고 PDF header/redirect host/document markers를 확인한 뒤 raw-byte SHA-256, page count, extracted-text SHA-256을 산출한다. Guidance primary source가 비-PDF/일시 unavailable이면 allowlist된 ANFR mirror만 fallback한다.
- `.github/workflows/tests.yml`에 pypdf, source blob pins, PDF live canary 및 7일 artifact 업로드를 추가했다. CI가 성공하고 artifact hash를 readback하기 전에는 원본 PDF 취득·해시 완료라고 기록하지 않는다.
- 상태: 구현·mock 테스트 완료; Run #669에서 CI 148 passed / 1 xfailed 및 PDF binary fetch/hash/artifact readback 통과.
- 제품별 적용성/Annex III·IV 분류는 실제 모델·회로·펌웨어·통신·시장 공급 사실이 확보되기 전까지 잠정 상태를 유지한다.


## 2026-11-17 — CRA PDF binary provenance readback

- GitHub Actions Run #642 (`44052336199`)의 PDF source canary에서 Guidance 및 M/606 Annex PDF 2개를 실제 취득하고 pypdf parse, document markers, page count, raw-byte SHA-256, extracted-text SHA-256을 계산했다.
- Guidance: ANFR mirror fallback 사용, 1,190,726 bytes, 84 pages, SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; Commission-hosted original byte identity는 미확인.
- M/606 Annex: Commission document-register direct fetch, 151,267 bytes, 6 pages, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- Artifact ID `14313359693`, ZIP SHA-256 `150a687e4d4b13fdd20a432e99fc8ea9ec5bc847b8551dd3f157258dc41cd869`; artifact ZIP를 다운로드하고 SHA-256 재계산하여 GitHub digest와 일치 확인.
- M/606 Annex I item 18 password manager deadline은 PDF printed page 3의 원본 표 우측 셀에서 `31/01/2027`로 시각 확인. 텍스트 추출에서 행 설명이 페이지 경계를 넘어가며 날짜 셀을 놓쳤던 문제를 해결했다.
- 상세 manifest: `reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json`.
- Run #642에서 발견된 summary page marker 오류를 수정했고, Run #669에서 PDF·HTML source canary 모두 통과했다.


## 2026-11-17 — PR #33 source validator correction 및 Run #669 성공

- 기존 Run #642에서 발견된 오류: Commission guidance publication summary page에 PDF 문서번호 `C(2026) 5252`가 반드시 존재해야 한다고 잘못 요구했다. 해당 페이지는 PDF Annex 자체가 아니므로 문서번호 marker를 페이지 검증에 사용하지 않도록 분리했다. PDF Annex identity marker는 `cra_pdf_sources.py`에서 별도로 검증한다.
- Regression test 추가 및 source blob pins 갱신 후 [Run #669](https://github.com/useformotor3/ai-discord-bot/actions/runs/44052967754) 성공: **148 passed / 1 xfailed**.
- Compileall 및 exact source blob identity 통과.
- PDF canary: C(2026)5252 ANFR mirror 84 pages / 1,190,726 bytes / SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; C(2026)7861 Annex Commission PDF 6 pages / 151,267 bytes / SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- PDF artifact ID `14315096266` 다운로드 및 readback 완료; ZIP SHA-256 `82e86c3347413bc6f210a7403939141679c34e5ad738822043af87fc5c2290c`가 GitHub metadata와 일치하고 내부 PDF hashes도 재계산 결과와 일치.
- 기존 HTML source canary도 9개 allowlisted official sources, Article 64(10)/67 corrigenda, Article 13(8) locator/quote 통과.
- M/606 item18 deadline `31/01/2027` 시각 검증 완료. Guidance Commission primary byte identity만 미확인.


## 2026-11-17 — 최종 branch-head Run #690 재검증

- 최신 문서/로그 변경이 반영된 branch HEAD `535300d60e1e943a867e3348c3c152832238b665`에서 Run #690 성공: **148 passed / 1 xfailed**.
- Exact source blob identity, compileall, PDF source canary 2종, artifact upload, 9개 official HTML source, consolidated corrigenda, Article 13(8) locator/quote 통과.
- 최신 artifact ID `14315106623` 다운로드 후 ZIP SHA-256 `da2f0e5fbfb5f5fa66360a2faa5af3d85821d3b7269885e34e1a3115f37cd3e2` 재계산 일치. 내부 PDF SHA-256도 manifest와 재계산 결과 일치.
- PR #33은 Run #690 검증 완료 상태로 병합 전 최종 diff 및 safety checkpoint 대기.


## 2026-11-17 — Latest branch-head Run #702

- Latest tested branch HEAD `3b895cb1411ada883b8df04972f929c1381f4053` Run #702 success: **148 passed / 1 xfailed**.
- PDF canary (2 docs), HTML source canary (9 docs), compileall, exact source blob pins, Article 64(10)/67 corrigenda and Article 13(8) locator/quote all passed.
- Artifact #14314174227 downloaded and rehashed; ZIP SHA-256 `8fddbba46ccf9b0901b36d88ce27d79817ac620f9fabf37a8b6beefe5dfcaa82` matches GitHub metadata; internal PDF hashes match manifest.
- PR #33 remains open pending final diff review and pre-merge recovery checkpoint.


## 2026-11-17 — PR #33 병합 완료

- PR #33 squash merge: `50e4784de60430bb2b8c70ca06b41627d75379ae`.
- [Run #713](https://github.com/useformotor3/ai-discord-bot/actions/runs/44054006627): success, **148 passed / 1 xfailed**, compileall, exact source pins, 2 PDF canaries, artifact upload, 9 official HTML sources, Article 64(10)/67 corrigenda, Article 13(8) locator/quote 통과.
- Pre-merge `safety/pre-merge-main-pr33-2026-11-17` → `16b5d2e732e9f5f158d2b79aa9c0c62f0488fc92`; post-merge `safety/post-merge-main-pr33-2026-11-17` → `50e4784de60430bb2b8c70ca06b41627d75379ae`. Post ref와 main compare identical.
- Guidance claim register G-001~G-013 및 15/35/36개 매트릭스 연결, PDF fetch/hash automation, provenance manifest가 main에 병합됨.
- M/606 item 18 deadline `31/01/2027` 시각 확인. Guidance Commission-hosted primary byte identity만 미확인.
- 현재 구현 작업 브랜치 없음. PR #34는 문서 전용 사후 동기화이며 다음 구현은 최신 main에서 새 branch로 시작한다.


## 2026-11-17 — CRA matrix traceability integrity automation

- 최신 main에서 `cra/traceability-integrity-2026-11-17` 작업 브랜치 생성.
- 신규 `cra_traceability.py`: claim register 13개, interface 15개, requirements 35개, SEC controls 36개 count/ID uniqueness를 확인한다.
- 모든 matrix의 Guidance claim IDs가 register에 존재하고 orphan claim이 없는지 검사한다.
- M/606 Annex I candidate refs가 1–41 범위인지, Guidance claims가 비구속적 explanation으로 분류됐는지, PDF provenance raw/text SHA-256·artifact readback·item18 confirmation이 기록됐는지 확인한다.
- README/통합 보고서의 claim/provenance 링크 및 PROJECT_LOG.jsonl 전체 JSON/unique event_id를 검증한다.
- `tests/test_cra_traceability.py`에 정상 저장소, unknown claim ID, M/606 item 42 오기재 fail-closed 회귀 테스트를 추가했다.
- `.github/workflows/tests.yml`에서 compileall 후 `python cra_traceability.py`를 실행하고 전체 pytest에 포함한다.
- 상태: PR #35 병합 완료; Run #738에서 추적성 gate 및 전체 CI 통과.


## 2026-11-17 — PR #35 병합 완료

- PR #35 squash merge: `2a347a60f2632bbe87044484187765adab45aee2`.
- [Run #738](https://github.com/useformotor3/ai-discord-bot/actions/runs/44055249482): success, **151 passed / 1 xfailed**.
- Traceability gate: 13 claims, 15 interfaces, 35 requirements, 36 SEC controls, 13 linked claims, 89 project log events(84 modern IDs + 5 legacy rows), 41 M/606 items, PDF provenance 및 item18 verification 통과.
- PDF canary 2건, HTML official sources 9건, Article 13(8) locator/quote 통과.
- Pre-merge `safety/pre-merge-main-pr35-2026-11-17` → `cad8452b64f274ceeaa203c1b0de6ecea5e2baac`; post-merge `safety/post-merge-main-pr35-2026-11-17` → `2a347a60f2632bbe87044484187765adab45aee2`. post ref와 main compare identical.
- 현재 구현 작업 브랜치 없음. PR #36은 문서 전용 사후 동기화이며 다음 구현은 최신 main에서 새 브랜치로 시작한다.


## 2026-11-17 — M/606 Annex I 41-item relevance map

- 신규 `reports/CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv`: Annex I 41개 전체 항목을 paraphrase하고 ESO adoption deadline, PDF printed page locator, candidate CRA requirement/SEC control/interface refs, servo-drive relevance class 및 판단 근거를 기록했다.
- Horizontal items 1–15, vertical product-type items 16–27/31–36/40, component-dependent items 28–30/37–39/41로 구분했다.
- 제품 자체의 intended purpose/core functionality가 확인되지 않으면 vertical category로 분류하지 않는다. 내장 MCU/FPGA/network interface/secure element는 supplier due diligence 후보이지 자동 완제품 분류가 아니다.
- M/606 dates는 ESO adoption deadlines이며 manufacturer compliance dates가 아니다. OJ citation 전에는 harmonised standard/presumption of conformity로 취급하지 않는다.
- Item18 deadline `31/01/2027` locator는 PDF viewer page 3 / printed `EN 3` 우측 셀로 정정했다.
- `cra_traceability.py`에 41개 mapping row, unique item, deadline, candidate ID cross-reference 및 page locator 검증을 추가하는 중.


## 2026-11-17 — PR #37 M/606 Annex I 41-item mapping 병합

- PR #37 squash merge: `25e1c36cc61a3001b5045cb8a6e90473fe830459`.
- [Run #757](https://github.com/useformotor3/ai-discord-bot/actions/runs/44056704831): success, **154 passed / 1 xfailed**.
- Traceability gate: 13 claims, 15 interfaces, 35 requirements, 36 SEC controls, 41 M/606 map rows, 93 project log events, item18 EN3 locator 통과.
- PDF 2-source canary, HTML 9-source canary, Article 13(8) locator/quote 통과.
- Pre-merge `safety/pre-merge-main-pr37-2026-11-17` → `360b93a1b9fbf554607e8f258edbaa303c1fcb6f`; post-merge `safety/post-merge-main-pr37-2026-11-17` → `25e1c36cc61a3001b5045cb8a6e90473fe830459`. post ref와 main compare identical.
- 현재 구현 작업 브랜치 없음. PR #38은 문서 전용 사후 동기화이며 다음 구현은 최신 main에서 새 branch로 시작한다.


## 2026-11-17 — 제품 경계 및 증거 수집 기준서

- 신규 `reports/CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md` 작성: 제품 식별, intended purpose, product boundary, interfaces, RDPS, 보안 기능, BOM/SBOM, vulnerability handling, support period, 안전·규제 중첩 및 evidence inventory를 포함한다.
- 현재 제품별 제조사/모델/데이터시트/사용설명서/BOM/SBOM/네트워크 구조는 저장소에 확인되지 않으므로 제품별 법적 분류·적합성 판정은 보류한다.
- 다음은 정확한 제품 모델 데이터시트와 사용설명서를 확보해 product boundary를 먼저 확정하는 것이다. 확인되지 않은 사실을 추정하지 않는다.


## 2026-11-17 — PR #39 제품 경계·증거 수집 기준서 CI 검증

- [PR #39](https://github.com/useformotor3/ai-discord-bot/pull/39) Run #776 성공: **154 passed / 1 xfailed**.
- Traceability: 13 claims, 15 interfaces, 35 requirements, 36 SEC controls, 41 M/606 rows, 95 project-log records(90 modern IDs + 5 legacy).
- 공식 CRA Guidance PDF(84 pages) 및 M/606 Annex PDF(6 pages) canary와 HTML canary 통과. PDF artifact upload 성공.
- 초기 Run #770은 integrated report 내 intake 링크의 상대경로 검사 오류를 정확히 검출했다. validator를 report-relative basename 검사로 수정하고 source blob pin을 갱신했으며, Run #776 전체 검증에서 통과했다.
- 현재 PR #39는 CI 성공, merge 전 검토 상태다. 제품별 제조사/모델 자료가 없어 특정 제품 분류·적합성은 여전히 미확정.


## 2026-11-17 — PR #39 병합 완료

- PR #39 squash merge: `aec679142bf8c12b1ce18b233956f9695d70ca21`.
- Run #781 성공: **154 passed / 1 xfailed**. Traceability: 13 claims, 15 interfaces, 35 requirements, 36 SEC controls, 41 M/606 rows, 96 project-log records(91 modern IDs + 5 legacy).
- 공식 CRA Guidance PDF(84 pages), M/606 Annex PDF(6 pages), HTML canary 및 PDF evidence artifact upload 통과.
- Pre-merge `safety/pre-merge-main-pr39-2026-11-17` → `d212081d0f105fc2b293606d71f9b156f0c45c89`; post-merge `safety/post-merge-main-pr39-2026-11-17` → `aec679142bf8c12b1ce18b233956f9695d70ca21`. post ref와 merge SHA/main compare identical.
- 제품별 모델 자료는 아직 미제공이므로 제품별 CRA 분류·적합성 결론은 미확정. 다음 실질 작업은 통합 CRA 보고서의 법령·요구사항·증거 연결을 독립 검토하고, 제품 자료가 들어오면 intake 기준서로 적용성 매핑을 수행하는 것이다.
- 현재 구현 작업 브랜치 없음. PR #40은 이 상태판 동기화만 수행한다.


## 2026-11-17 — 통합 CRA 보고서 2차 검토 착수

- PR #39 제품 증거 intake 기준서 및 PR #40 사후 상태 동기화가 main에 병합되고 post-merge safety ref 검증을 완료했다.
- 통합 보고서에서 추가된 §11–§13과 기존 §11–§13 번호 중복을 발견해 추가 섹션을 §14–§16으로 수정했다. Annex III Important products와 Annex IV Critical products 용어도 구분했다.
- 독립 검토 기록 `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md` 작성. Guidance mirror byte identity의 한계와 제품별 증거 미확보 상태를 명시했다.
- `cra_traceability.py`에 top-level section number 중복 검증을 추가하고 negative test를 작성 중이다.


## 2026-11-17 — 독립 검토 1차 수정 및 CI

- 보고서 최상위 섹션 번호 중복을 §14–§16으로 정정하고 분류 용어를 정리했다.
- traceability gate에 top-level section number uniqueness 검사를 추가하고 duplicate heading negative test를 추가했다.
- [Run #797](https://github.com/useformotor3/ai-discord-bot/actions/runs/44059539968): **155 passed / 1 xfailed**; CRA traceability, official Guidance/M/606 PDF canaries, HTML canary 및 artifact upload 통과.
- EUR-Lex 원문으로 Article 6, 7(1), 10, 11, 14, 32, 69(2)–(3), 71(2)와 Regulation (EU) 2025/327 Article 104의 적용 예정일을 표본 대조했다. 전체 35개 requirement 전수 대조는 계속 진행한다.
- Guidance PDF의 Commission-hosted primary byte identity는 여전히 미확인으로 유지한다.


## 2026-11-17 — Commission Guidance PDF locator 재대조

- CI artifact Run #702의 Guidance PDF를 다운로드하고 SHA-256 manifest와 대조한 뒤 G-001~G-013의 paragraph/page locator를 PDF 추출 텍스트와 재대조했다.
- G-002, G-005, G-006, G-008, G-009, G-010, G-012, G-013의 printed-page locator를 정정했다. G-001, G-003, G-004, G-007, G-011은 유지했다.
- 정정 내역은 `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md` §7에 기록했다. Commission-hosted primary PDF byte identity는 아직 미확인이다.


## 2026-11-17 — PR #41 독립 검토 병합

- PR #41 merge commit `acfa2f583157ac541c4c60d71090197322bc8efb`.
- Run #806 success: **155 passed / 1 xfailed**; 13 claims, 15 interfaces, 35 requirements, 36 SEC controls, 41 M/606 rows, 100 project-log records.
- G-001~G-013 Guidance PDF paragraph/page locator를 재대조하고 8개 printed-page range를 정정했다. 보고서 섹션 번호 중복 검증도 CI에 추가했다.
- Pre-merge `safety/pre-merge-main-pr41-2026-11-17` → `576b3918e7f3e6013c59e49bf7e55d49d387217a`; post-merge `safety/post-merge-main-pr41-2026-11-17` → `acfa2f583157ac541c4c60d71090197322bc8efb`; post ref와 main compare identical.
- 다음 단계는 CRA-001~CRA-035 법령 Article/Annex locator를 공식 EUR-Lex 원문과 대조하고, 근거 불일치가 있으면 매트릭스와 보고서를 함께 수정하는 것이다.


## 2026-11-17 — SBOM 조항 교차 확인

- EUR-Lex Annex I Part II(1)에서 최소 최상위 의존성을 포함한 기계 판독형 SBOM 작성이 제조자 기본 의무임을 확인했다.
- Annex VII(2)(b)는 SBOM을 기술문서의 취약점 처리 프로세스 내용에 포함하며, Annex VII(8)은 시장감시당국의 합리적 요청 및 필요 시 추가 제출 규정이다. Annex VII(8)을 Annex I Part II(1)의 작성 의무 예외로 오독하지 않도록 보고서 문구를 명확히 했다.
- Annex II(9)의 사용자 제공은 제조자가 SBOM을 사용자에게 공개하기로 결정한 경우의 접근 위치 안내와 구분했다.


## 2026-11-17 — CRA 법령 locator 1차 인벤토리 검토

- CRA-001~CRA-035의 Article/Annex locator를 1차로 검토했고, 명백한 잘못된 조항 번호는 현재까지 발견하지 못했다. 세부 문언·조건·예외의 전수 확정은 계속 진행한다.
- Annex I Part II(1) SBOM 기본 작성 의무, Annex VII(2)(b) 기술문서 포함, Annex VII(8) 요청 제출, Annex II(9) 사용자 공개 조건을 구분해 보고서를 명확화했다.
- Run #819 성공: **155 passed / 1 xfailed**; 13 claims, 15 interfaces, 35 requirements, 36 SEC controls, 41 M/606 rows, 102 project-log records; official PDF/HTML canaries 및 artifact upload 통과.
- 제품별 제조사/모델 증거가 없으므로 제품별 분류 및 적합성은 여전히 미확정이다.
> **최신 재개 상태(2026-11-18):** 현재 기준 스냅샷은 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 우선 참조한다. PR #42 merge `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`, exact head Run #824 success (155 passed / 1 xfailed). pre/post safety refs 및 main 동등성 검증 완료. 다음은 CRA-001–CRA-035 법령 문언·조건·예외 심층 감사다.

