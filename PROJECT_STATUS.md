# CRA 서보 드라이브 프로젝트 상황판

- 최종 갱신: 2026-11-14 (KST)
- 기준 저장소: `useformotor3/ai-discord-bot`
- 운영 기준 브랜치: `main` (운영 자동화 및 데이터 보존)
- 현재 작업 브랜치: `docs/cra-audit-and-project-control-2026-11-14`
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
| P1-B 전송·동기화 신뢰성 | 설계 및 정적 감사 | Discord/Git 실패 경로, 원자적 저장 개선은 별도 승인 필요 |
| CRA 요구사항 추적 | 후속 | 공식 조항-제품 적용성-통제-시험 증거 연결 |
| SIL 기능안전 자료 | 별도 추적 | CRA 사이버보안 결론과 혼합 금지 |

## 2. 이번 단계에서 원본 코드로 확인한 사실

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
