# CRA 서보 드라이브 프로젝트 상황판

- 최종 갱신: 2026-11-16 (KST)
- 기준 저장소: `useformotor3/ai-discord-bot`
- 운영 기준 브랜치: `main` (운영 자동화 및 데이터 보존)
- 현재 작업 브랜치: `test/failure-path-fixtures-2026-11-14` (최신 상태 절 참조)
- 이번 비교 기준: main과 diverged 상태. ahead/behind 수치는 main 자동화 커밋에 따라 변동하므로 통합 직전에 재조회
- 프로젝트 상태: 조사 품질 감사 및 자동화 신뢰성 개선 진행 중
- 주 문서 언어: 한국어
- 안전 원칙: 법적 적합성·제품 분류·안전 관련 설계 판단은 근거와 인간 검토 없이 확정하지 않음

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
| P1-B2 저장 원자성 | 미구현 | state/history transaction journal 및 crash recovery 설계·승인 필요 |
| P1-B3 Git sync 상태화 | 미구현 | 유일한 strict xfail; 별도 승인 필요 |
| P1-B4 구조 개선 | 미구현 | import-time 실행 제거 등 후속 단계 |
| CRA 요구사항 추적 | 후속 | 공식 조항-제품 적용성-통제-시험 증거 연결 |
| SIL 기능안전 자료 | 별도 추적 | CRA 사이버보안 결론과 혼합 금지 |

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

- 이전 비교 기록(61 ahead / 49 behind)은 과거 스냅샷이다. 2026-11-14 15:31 KST 재조회 결과는 72 ahead / 50 behind이며 diverged 상태다.
- main의 자동 생성 자료와 작업 변경의 충돌 여부를 확인하기 전까지 merge/rebase하지 않는다.
- 운영 `main`, `.github/workflows/run.yml`, `state.json`, `history.json`은 변경하지 않았다.
- 실제 Gemini/Discord/Git push 및 운영 workflow를 실행하지 않았다.

## 6. 다음 재개 지점

1. 기본 원본 실행 경로는 확보했고, 최신 Run #3에서 SHA·compileall·pytest 21 passed를 재확인했다.
2. fixture의 Git/Discord 실패 경로 검증 공백을 보강할 설계안을 작성한다.
3. P1-B 최소 변경안과 롤백 방안을 사용자에게 제시하고 별도 승인받는다.
4. 승인된 변경 후 동일 CI 게이트로 전체 회귀 검증한다.
5. 이후 CRA 요구사항 추적 및 검증된 통합 보고서로 진행한다.

## 7. 문서 진입점

- [프로젝트 메인 페이지](README.md)
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
- GitHub compare 결과: diverged, 72 commits ahead / 50 commits behind
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

## P1-B2 상태
- [완료] 원자적 로컬 저장 설계서 작성 및 자체 범위 검토.
- [승인 대기] P1-B2 구현. 이번 단계에서 main.py/tests/workflow/state/history/archive 변경 없음.


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
- P1-B2는 설계 완료·구현 별도 승인 대기. P1-B3/B4는 보류 상태 유지.


## 2026-11-17 09:09 KST — 매일 통합 상태 점검
- 조회 시각: 2026-11-17T09:09:39+09:00
- 감사 기준 main HEAD: `0dde26ebac80a789c7a9d9e26560abad54606d32`
- 감사 기준 작업 브랜치 HEAD: `7ae3b251861b9a3de9981bd7202e346d05ca9430`
- merge-base: `7ae3b251861b9a3de9981bd7202e346d05ca9430`; compare: **0 ahead / 919 behind** (branch is an ancestor of main; no branch-only commits).
- recursive tree: main `d606a8f03ba1db6cfb292e4087ae696234ea7ce0`, 2,438 blobs, truncated=false; branch `5d40aa70d81faf7602c077e1ba440c7a166fa1c2`, 1,617 blobs, truncated=false.
- 전체 blob 경로 차이: main-only 821, branch-only 0, same-path modified 16.
- 데이터: main archive 2,398 / branch archive 1,592; main-only archive 806, branch-only 0, modified archive 0. state.json 및 history.json은 각각 변경되어 데이터 차이 총 808 paths.
- history.json: main 2,398개 / branch 1,592개. branch의 1,592개 항목은 main history의 정확한 prefix이며 main에 806개가 추가됨.
- state.json: main date/count=`2026-11-17 / 5`; branch date/count=`2026-11-14 / 29`. count는 state의 실행 카운터 필드이며 history/archive 전체 개수와 같은 의미가 아님.
- blob SHA: main state `c94cc82a55ad64555fe1c946a4acc163c98da2d5`, branch state `172963125a28bcdc51f3bfc4504866505d7626c2`; main history `dbf719321a8fc27f7d910df5767734a1e2120964`, branch history `4dc2d720418944be1dea42841933199247417864`.
- 코드/운영 workflow 차이도 존재: main.py main `f28dbc540d56b313f0648d77c58734d27eb95d1a` vs branch `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`; run.yml main `743c2300d9d5fd51f86b3bee3effaeb7ec456f71` vs branch `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- JSONL 기존 25행은 모두 유효했고, 이번 감사 이벤트 1행을 추가함.
- 문서만 작업 브랜치에 갱신. main, main.py, 운영 run.yml, state/history/archive 원본은 수정하지 않음. merge/rebase/PR merge, workflow 실행, Gemini/Discord 외부 호출 없음.
- 테스트는 실행하지 않았으며 PASS로 기록하지 않음.



## 2026-11-19 09:34 KST — 최신 브랜치/main 감사 상태

## 2026-11-19 09:34 KST — 매일 통합 상태 점검 (읽기 전용 비교)

- 조회 기준 시각: 2026-11-19T09:34:27+09:00
- 운영 main HEAD: `732f5167ed1a272afc10bb66d4aceb68ccb96b79`
- 작업 브랜치 HEAD (문서 갱신 전): `ca3f6ee8c917da8e2485cf75cd9c90ee7fb03a85`
- merge-base: `7ae3b251861b9a3de9981bd7202e346d05ca9430`
- GitHub compare API: status=`diverged`, **ahead=1 / behind=1,357**. 작업 브랜치에는 main에 없는 고유 커밋 1개가 있다.
- compare API wrapper의 파일 통계는 6개만 반환했으므로 전체 파일 경로 판정에 사용하지 않았다. 양쪽 recursive Git tree 전체를 조회하고 `truncated=false`를 확인한 뒤 path/blob SHA를 비교했다.
- recursive tree: main tree `d1281ea188b7313ee4923c2e9df5ab88a1014561`, 2,548 blobs; branch tree `9bed5aa6d39e210ac564fcaea9d744d086d5ce21`, 1,617 blobs.
- 전체 blob 경로 차이: main-only 931, branch-only 0, 동일 경로 blob 변경 19. main-only 중 archive 839, 비-archive 92.
- 변경 경로 19개: `.github/workflows/run.yml`, `.github/workflows/tests.yml`, `AI_RULEBOOK.md`, `MASTER_PLAN.md`, `PROJECT_LOG.jsonl`, `PROJECT_STATUS.md`, `README.md`, `SESSION_LOG.md`, `history.json`, `main.py`, `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16.md`, `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md`, `reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md`, `state.json`, `tests/README.md`, `tests/conftest.py`, `tests/test_external_failure_paths.py`, `tests/test_main_characterization.py`, `tests/test_p1_reliability.py`.
- 데이터 경로: main archive 2,431 / branch archive 1,592; main-only archive 839, branch-only 0, modified archive 0. 즉 archive 원본은 추가분 외에 동일 경로 내용 변경이 없다.
- `history.json`: main 2,431개 / branch 1,592개. branch 배열 1,592개 항목은 main 배열의 정확한 prefix이며 main에 839개가 추가됐다. main SHA `b9ea42fa437b2b3a5728db5d125d287fb746b46b`, branch SHA `4dc2d720418944be1dea42841933199247417864`.
- `state.json`: main date/count=`2026-11-17 / 38`, branch date/count=`2026-11-14 / 29`. main SHA `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, branch SHA `172963125a28bcdc51f3bfc4504866505d7626c2`. count는 상태 파일 내부 실행 카운터이며 history/archive 누적 개수와 별개다.
- 주요 코드/워크플로 SHA도 다르다: `main.py`와 `.github/workflows/run.yml`은 양쪽 blob SHA가 각각 다르다. 이번 감사에서는 파일 내용을 변경하거나 실행하지 않았다.
- 작업 브랜치의 README, PROJECT_STATUS, MASTER_PLAN, SESSION_LOG, PROJECT_LOG, 본 감사 보고서를 읽었다. 기존 PROJECT_LOG.jsonl 26행 모두 유효 JSON이었다.
- 판단: 작업 브랜치는 main보다 1,357 commits 뒤처져 있고 main에 없는 커밋은 1개다. 운영 데이터 839건 누적 차이와 코드/workflow/test 변경이 공존하므로 이 브랜치를 main에 직접 통합하지 않는다. 고유 1개 커밋의 내용은 별도 검토 대상이다.
- 이번 실행은 문서 기록만 작업 브랜치에 추가한다. main, main.py, 운영 run.yml, state/history/archive 원본은 수정하지 않는다. merge/rebase/PR merge, 운영 workflow 실행, Gemini/Discord 외부 호출은 하지 않는다.
- 테스트는 실행하지 않았으므로 PASS 판정은 없다.

