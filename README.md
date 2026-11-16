# CRA Servo Drive Compliance & Engineering Project

산업용 서보 드라이브의 EU Cyber Resilience Act(CRA) 대응을 위한 조사·설계·검증·문서화 프로젝트입니다. 문서의 기본 언어는 한국어이며, 법령·표준·제조사 원문은 원어와 출처를 보존합니다.

> **기록 원칙:** 프로젝트의 공식 진행 상태와 재개 지점은 이 저장소에 기록합니다. 대화창의 기억에만 의존하지 않습니다.

## 현재 상태

- 현재 작업 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16` (P1-B2 전용 구현 브랜치)
- 운영 기준 브랜치: `main` — 별도 승인 없이 수정·병합하지 않습니다.
- P0 응답 검증/실패 차단, P1-A 상태·이력 검증, P1-B1 Discord 전송 신뢰성: 작업 브랜치 구현 완료
- **P1-B2 로컬 다중 파일 저장 일관성: 사용자 승인 후 구현 및 테스트 CI 검증 완료**
- **최신 테스트 전용 CI (Actions 43851438733): 70 passed, 1 xfailed; source SHA·compileall·전체 pytest 통과**
- P1-B2는 durable journal, staged payload, backup/SHA 검증, idempotent roll-forward recovery, snapshot 충돌 방지 및 허용 target allowlist 적용
- P1-B3 Git sync 상태화는 미구현(기존 strict xfail), P1-B4 import-time 구조 개선도 미구현
- Discord exactly-once/outbox는 P1-B2 범위 밖이며 보장하지 않음
- main 대비 작업 브랜치: diverged, 221 ahead / 678 behind (snapshot commit `02fde2489323f9f553405e014fac20d75d13a7fa`, 2026-11-16); merge-base 기준 통합 분석은 완료, PR/merge는 별도 승인 대기
- 운영 main 최신 조회: HEAD `267d97478b785e6bb268e224a70dbad6631cf43e` (#131), state count=131, history=2,270, archive=2,270
- 운영 main의 main.py와 run.yml은 각각 SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`, `65a8cadc8eac593f551e390698e367b1d161ecf1`; 작업 브랜치 main.py만 개선했고 run.yml은 변경하지 않음

Actions 성공은 자동화 실행 결과이지 CRA 법령 해석이나 출처의 사실 정확성을 보증하지 않습니다. 테스트 통과 숫자는 반드시 실행한 정확한 소스와 범위를 함께 표시합니다.

## 프로젝트 관리 문서

| 문서 | 목적 |
|---|---|
| [상황판](PROJECT_STATUS.md) | 현재 상태, 위험, 실제 검증 결과, 다음 재개 지점 |
| [마스터 계획](MASTER_PLAN.md) | 전체 단계, 우선순위, 완료 기준 |
| [AI 행동강령](AI_RULEBOOK.md) | 조사·근거·코드·테스트·기록 규칙 |
| [세션 로그](SESSION_LOG.md) | 날짜별 실제 작업, 변경 범위, 테스트 결과 |

## 주요 기술 자료

- [조사 품질 감사](reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md)
- [CRA 보고서 #28·#29 정정 기록](reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md)
- [자동화 코드 개선 설계 및 테스트 계획](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- [테스트 실행 환경 감사 및 예비 검증 한계](reports/TEST_EXECUTION_ENVIRONMENT_AUDIT_2026-11-14.md)
- [테스트 가이드](tests/README.md)

## 진행 원칙

1. 공식 법령·표준 원문을 우선하고 조항, URL, 확인일, 원문 인용을 기록합니다.
2. 법적 의무, 표준 요구사항, 공식 해석, 엔지니어링 권고, 미확인 가설을 분리합니다.
3. 조사 초안 생성과 출처/내용 검증을 구분합니다.
4. 중복 보고서를 양산하기보다 기존 자료를 검증·정정·통합합니다.
5. 코드 변경은 작업 브랜치에서 mock 테스트부터 수행하고, 운영 코드·workflow·데이터 변경은 별도 승인 없이 하지 않습니다.
6. 테스트 원본과 blob SHA가 일치하지 않으면 결과를 예비 검증으로만 기록합니다.
7. 운영 workflow를 테스트 목적으로 실행하지 않습니다.
8. 의미 있는 작업이 끝날 때 README, 상황판, 마스터 계획, 행동강령, 세션 로그와 관련 보고서를 동기화하고 GitHub에서 재조회합니다.

## 초기 테스트 실행 증거 — 2026-11-14 (과거 기준선)

- [GitHub Actions latest Run #3 — 21 passed](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938)
- 실행 commit: `dddba44a41851e9d0319ce9a91535a9d26145d92`
- 다섯 개 핵심 파일의 Git blob SHA 일치 확인 후 compileall 및 pytest 실행.
- 테스트 전용 workflow: [.github/workflows/tests.yml](.github/workflows/tests.yml)

## 다음 작업

- [완료] P1-B2 구현·보강 및 테스트 전용 CI 검증.
- [완료] merge-base 기준 전체 tree 및 운영 archive/history/state 보존 분석.
- [다음] 최신 main/feature ref를 재조회하고 PR Files changed에 예상 23개 경로 외의 데이터 변경·삭제가 없는지 확인한다.
- [다음] PR CI와 GitHub conflict check를 검증한다.
- PR 생성, merge, 운영 workflow 실행 및 배포는 별도 승인 전 수행하지 않는다. P1-B3/B4는 별도 범위다.

자세한 재개 지점과 검증 한계는 [PROJECT_STATUS.md](PROJECT_STATUS.md)를 기준으로 합니다.

## 프로젝트 작업 로그

- [기계 판독형 프로젝트 로그](PROJECT_LOG.jsonl): 작업 이벤트를 JSONL로 기록합니다. 각 줄은 독립 JSON 객체이며 이벤트 ID, 날짜, 상태, 변경 파일, 검증 결과, 근거 링크, 한계 및 승인 범위를 포함합니다.
- [한국어 세션 로그](SESSION_LOG.md): 작업 배경과 판단, 사용자 승인, 검증 해석을 사람이 읽기 쉽게 기록합니다.
- `state.json` 및 `history.json`은 기존 자동화 런타임 데이터로 유지하며 프로젝트 작업 로그로 대체하거나 임의 수정하지 않습니다.


## 과거 테스트 fixture 작업 기록 — 2026-11-14
- 작업 브랜치: `test/failure-path-fixtures-2026-11-14`
- 기준 브랜치/커밋: `docs/cra-audit-and-project-control-2026-11-14` @ `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 목적: Discord/Git 실패 응답을 주입할 수 있는 mock fixture 및 strict xfail 회귀 테스트 추가
- 최신 확인 CI: [Run #11 — success, 23 passed / 5 xfailed](https://github.com/useformotor3/ai-discord-bot/actions/runs/43569359083)
- 변경 파일: `.github/workflows/tests.yml`, `tests/README.md`, `tests/conftest.py`, `tests/test_mock_infrastructure.py`, `tests/test_external_failure_paths.py`
- 운영 `main.py`, 운영 workflow `run.yml`, `state.json`, `history.json`은 변경하지 않았다.
- 상세 현황은 작업 브랜치의 `PROJECT_STATUS.md` 및 `SESSION_LOG.md`를 확인한다.


## 최신 원격 상태 — 2026-11-14 확인
- CI 검증 대상 commit: `27d2c69287631b041672b9989fdeeb3066f5ebb9` (Run #13); 문서 정리 전 HEAD
- 기준 브랜치: `docs/cra-audit-and-project-control-2026-11-14` @ `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 기준 브랜치 대비: 23 ahead / 0 behind (Run #13 시점)
- `main` 대비: diverged, 134 ahead / 58 behind (Run #13 시점; 자동화 커밋으로 변동)
- 최신 확인 테스트 증거: [Run #13](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208), 30 passed / 5 xfailed. Run #13이 새 fixture 7개 case를 포함한 변경 소스 SHA와 compileall을 검증했다.
- 이 문서 앞부분의 과거 브랜치/Run #3 요약은 당시 기록이다. 현재 기준은 이 최신 상태 절과 `PROJECT_STATUS.md`를 따른다.

## 최신 상태 스냅샷 — 2026-11-14
- 문서 갱신 전 작업 브랜치 HEAD: `11c89c2bf513c0562aa0451caf38effae2041e26`
- 기준 docs commit `c6dfc5cee2485922b2313030dd9a5843e347afe7` 대비 24 ahead / 0 behind.
- `main` 대비 diverged 135 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- Run #13에서 검증된 테스트 commit은 `27d2c69287631b041672b9989fdeeb3066f5ebb9`이며, 그 이후 변경은 관리 문서와 로그다.
- `main.py` blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43`; 테스트 브랜치의 기준 commit 대비 변경 파일 목록에도 `main.py`는 없다.
- 문서 저장 후 ahead/behind는 다시 증가할 수 있으므로 다음 작업 시작 시 재조회한다.


## P1-B 정책 설계 최신화
- [P1-B 전송·저장·동기화 정책 명세](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- Discord 429/timeout/POST 중복 가능성, chunk 부분 성공, state/history transaction, Git 원격 동기화 확인 정책을 공식 기술 문서와 대조해 정리했다.
- 구현 승인이 아니다. 운영 코드 변경 전 별도 제안·승인이 필요하다.


## P1-B 테스트 정책 정합성 및 최신 CI
- 503 자동 재시도 xfail을 중복 방지 관점의 `delivery_unknown` 기대 동작으로 변경했다.
- Discord 401/403/404 영구 실패·재시도 금지 기대 테스트 3 case를 추가했다.
- [Run #15 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842), commit `b2e108768be08f06e85af154835424682337ebf5`: **30 passed / 8 xfailed**.

## 최신 상태 재조회 — 2026-11-14
- 직전 HEAD: `5b3cd6ca70dcff7a50f4ad4c20f834592c9e8ca9`.
- 기준 docs commit 대비 28 ahead / 0 behind.
- main 대비 diverged 139 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 마지막 테스트 코드 검증은 Run #15, commit `b2e108768be08f06e85af154835424682337ebf5`: 30 passed / 8 xfailed. 그 이후 변경은 문서/로그뿐이다.
- main.py SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 유지.


## 과거 승인 게이트 기록 — P1-B1 (이후 승인·구현 완료)
- P1-B는 단계별로 분리했다. 우선 제안은 **P1-B1 Discord 전송 결과 신뢰성**만이다.
- 변경 파일, 기대 동작, 테스트, 롤백 및 제외 범위는 [개선 설계 보고서](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)의 §18을 참조한다.
- P1-B1은 main.py 운영 코드 변경이므로 별도 승인 전까지 구현하지 않는다.

## 최신 브랜치 상태 — 2026-11-14
- 조회 HEAD: `f5a83e3c8e04a43b6e38a593c7b01bd360583b3f`
- 기준 docs commit 대비 30 ahead / 0 behind.
- main 대비 diverged 141 ahead / 60 behind; main HEAD `1dff09ffa9722119f6fb0847a51b6c87c322d114`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 마지막 테스트 검증 commit `b2e108768be08f06e85af154835424682337ebf5`, [Run #15](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842): 30 passed / 8 xfailed. 이후 테스트 코드 변경은 없고 문서만 갱신했다.
- main.py blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 유지.


## P1-B1 Discord 전송 신뢰성 구현 — 2026-11-16
- 사용자 승인 범위 P1-B1을 작업 브랜치에서 구현했다.
- Discord webhook POST에 connect/read timeout (3.05, 10), wait=true, HTTP 응답 및 message ID 확인을 추가했다.
- 429 Retry-After, ConnectTimeout 제한 재시도, 400/401/403/404 영구 실패, 5xx/ReadTimeout/ConnectionError 전달 불명확 상태, chunk partial 처리를 구현했다.
- [GitHub Actions Run #18](https://github.com/useformotor3/ai-discord-bot/actions/runs/43808285335): 43 passed, 1 xfailed; source SHA 6개 및 compileall 통과.
- Run #17은 main.py SHA pin 불일치로 실패했고 Run #18에서 정정 후 통과했다. 실패 이력은 보존한다.
- 이 P1-B1 작업 시점에는 P1-B2/B3/B4와 운영 main 병합이 미실행이었다. P1-B2는 이후 별도 승인으로 구현·검증됐으며, P1-B3/B4는 여전히 보류다.


## 이전 원격 브랜치 비교 스냅샷 — 2026-11-16 (이후 갱신됨)
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


## 이전 통합 감사 스냅샷 — 2026-11-16 (KST, 이후 갱신됨)
- 작업 브랜치 HEAD `227e3298066af4bda83fb0713fc1d57c749ee8c6`; 운영 main HEAD `036334dd2665752c2e6ddb024001771cff4064c5`; merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 작업 브랜치 기준 base 대비 44 ahead / 0 behind, main 대비 155 ahead / 660 behind.
- recursive tree 비교(양쪽 truncated=false): merge-base 1,600 entries, main 2,260 entries. archive 660개 추가, 삭제 0개, history/state 변경 2개.
- main history.json 2,252개 객체, state.json count=113. main.py SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`, 작업 브랜치 main.py SHA `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- 자동 조사/아카이브 운영은 main에서 계속된 흔적이 있으나 P0/P1-A/P1-B1 신뢰성 개선은 작업 브랜치에만 존재한다. 운영 배포로 간주하지 않는다.
- 상세 감사: `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md`.
- 통합 전략: `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`.


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


## 통합 전략 감사 — 2026-11-16
- merge-base 기준 main은 archive 678개만 추가하고 history/state를 갱신했으며 삭제는 0개다.
- 작업 브랜치는 main.py 수정 및 23개 경로 추가, 삭제 0개다. 따라서 3-way PR 통합 시 운영 archive/history/state 보존을 기대할 수 있다.
- P1-B2 recovery target allowlist 보강 후 CI Actions 43851438733에서 70 passed / 1 xfailed.
- PR 생성·merge·운영 배포는 별도 승인 전 수행하지 않는다.
- PR 비교 변경 경로: 24개(23개 추가 + main.py 수정). state/history/archive/run.yml 변경은 없어야 한다.
- 상세: [통합 전략 감사 보고서](reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md).


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


## 2026-11-16 — Draft PR #1 생성 및 PR CI 검증
- Draft PR: https://github.com/useformotor3/ai-discord-bot/pull/1
- 대상: `main` ← `feature/p1-b2-atomic-persistence-2026-11-16`; PR head `01e7cf50436f35d9eddb931ae4e1d177af805387`, PR 생성 시 base main `38abb075ebe0f7180abaebc4da52e2f18ea28915`.
- 생성 직전 compare: 230 ahead / 700 behind, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; 변경 24개(23 added + main.py modified), 삭제 0.
- 보호 경로 `state.json`, `history.json`, `research_archive/**`, 운영 `.github/workflows/run.yml`는 PR 변경 경로에서 제외됨.
- PR 생성 후 GitHub 재조회: open, draft=true, merged=false, mergeable=true.
- PR-triggered Actions Run #32 (`43869220252`) 성공: source integrity, compile, 전체 pytest 단계 완료. [Run #32](https://github.com/useformotor3/ai-discord-bot/actions/runs/43869220252).
- 이전 코드 검증 Run #43851438733은 70 passed / 1 xfailed였으며 PR-triggered run #32의 개별 테스트 수치는 job summary에서 확인되지 않아 별도 숫자로 단정하지 않는다.
- 현재 PR은 검토용 Draft이며 merge/rebase/운영 반영은 하지 않았다. main의 지속적인 자동 아카이브로 base가 움직일 수 있으므로 병합 직전 재비교가 필요하다.


## 2026-11-16 — 상시 진행 승인 및 복구 우선 운영 기준
- 사용자는 매 단계별 승인 질문 없이 목표 달성에 필요한 작업을 계속 진행하도록 상시 승인했다. 안전 통제·검증·복구 절차는 유지한다.
- AI_RULEBOOK.md §18에 변경 전 체크포인트, safety/ 백업 브랜치, merge commit, 운영 데이터 사전 백업/복원, 실패 시 revert/복구 절차를 명문화했다.
- 현재 main 백업 safety/pre-merge-main-2622e332 → 2622e332d6a3defd2079ccad3af36970001de5c1; feature 백업 safety/pre-merge-feature-eba3aeb → eba3aeb5710dcc6507623d56d586a619e9a4fc46.
- Draft PR #1: https://github.com/useformotor3/ai-discord-bot/pull/1. main은 2622e332d6a3defd2079ccad3af36970001de5c1까지 진행. 최신 compare는 231 ahead / 703 behind, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- PR mergeable 값은 조회 시점에 변동했고 PR base SHA 응답도 main HEAD와 일치하지 않는 스냅샷을 반환했다. 최신 base 기준 통합 검증이 완료된 것으로 보지 않는다.
- 코드 백업 ref는 만들었지만 운영 데이터 snapshot/restore 절차는 아직 검증되지 않았다. 이를 완료하고 복원 리허설하기 전에는 신규 코드의 첫 운영 실행을 하지 않는다.

## 2026-11-16 — 운영 데이터 immutable baseline #158
- 기준 commit 4cf0e708b28a343898af00d01521044dfb9a1987 (Auto-archive #158).
- 동일 SHA 검사: state count=158, history=2,297, archive=2,297, 참조 누락 0, tree 2,305 entries.
- backup safety/pre-merge-main-4cf0e70가 같은 SHA를 가리킨다.
- U+200B가 앞에 붙은 별도 state 파일(date 2026-06-07,count 0)은 조사 전까지 보존한다.
- moving-ref 조회에서 보인 불일치 1건은 immutable SHA 재검사에서 재현되지 않았다.
- 상세 감사: reports/ROLLBACK_AND_DATA_BASELINE_AUDIT_2026-11-16.md.

## 2026-11-16 — 운영 rollback guard 구현 및 검증
- production workflow에 실행 전 고유 safety/data-pre-run checkpoint, 실행 직렬화, 실행 후 무결성 검증/조건부 데이터 복구를 추가했다.
- operational_guard.py 및 테스트 추가. local bare Git remote로 정상 전이/복구 commit/미push 거부/quota no-op을 검증.
- 최종 PR CI Run #43874801395: 86 passed, 1 xfailed, compileall 성공. https://github.com/useformotor3/ai-discord-bot/actions/runs/43874801395
- 최신 main #161 baseline: f5b5a112ec72b01f8b3f91f734b8d755dde416c6; state count 161, history 2,300, archive 2,300, missing refs 0.
- main backup safety/pre-merge-main-f5b5a11, feature backup safety/pre-merge-feature-8ad2364. 상세 reports/ROLLBACK_AND_DATA_BASELINE_AUDIT_2026-11-16.md


## 2026-11-16 — rollback guard final CI and main #162 baseline
- [Draft PR #1](https://github.com/useformotor3/ai-discord-bot/pull/1) includes production run.yml pre-run checkpoint and guarded restore.
- Latest feature head at code verification: abee2a88f7e0bbfad0ad483c6b50cea63e26b871; main #162: adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890.
- CI Run #43875746973 success: 87 passed, 1 xfailed, compileall and source SHA checks passed. https://github.com/useformotor3/ai-discord-bot/actions/runs/43875746973
- main #162 immutable baseline: state count 162, history 2,301, archive 2,301, missing refs 0.
- main backup safety/pre-merge-main-adf74ea readback SHA exact. Feature backup safety/pre-merge-feature-abee2a8 readback exact.
- Production workflow has not yet been executed; first execution remains external-effect operation. The workflow now snapshots before run and verifies/restores data after run.

## 2026-11-16 — PR #1 통합 완료
- PR #1 merged: https://github.com/useformotor3/ai-discord-bot/pull/1
- merge commit 6fd03efaf8623cb3ec2ab938aa7161b41ffed82e (main #162 + feature d48ae1c9b655d7384aff497c9d17168a5d0b25c5).
- Post-merge safety branch safety/post-merge-main-6fd03ef, readback exact SHA.
- Push CI Run #43876347620 success: 87 passed, 1 xfailed, compileall success.
- Merge 직후 same-SHA data integrity: state count 162, history 2,301, archive 2,301, missing refs 0. state/history blob SHA는 pre-merge main #162와 동일.
- Merge 자체로 production workflow는 실행되지 않음(현재 trigger repository_dispatch/workflow_dispatch). 실제 Gemini/Discord 호출 없음.
- 다음: 첫 production run 전 snapshot branch 및 post-run guard 동작을 실제 workflow에서 관찰한다.


## 2026-11-17 — GitHub 자동화 점검 및 체크포인트 누적 개선
- 원격 Actions 최근 20건은 조회 당시 completed/success였으나, #2412는 현재 작업 중 main 커밋이 추가된 경합으로 실패했다.
- #2412: 로컬 보고서 #235 commit 생성, Discord 2/2 chunks 전송, Git push는 non-fast-forward(fetch first) 거부. operational_guard는 remote main 불일치로 자동 복구를 거부했다. 보고서 #235는 원격 history/archive/state에 반영되지 않았다.
- 실행별 safety/data-pre-run 브랜치 94개 확인. 성공 실행 이후에도 무제한 누적되는 구조를 결함으로 분류.
- main 변경 전 백업: safety/pre-checkpoint-prune-1abfcfb → 1abfcfb26a8b414dc75eb584082ed35cab0d6412.
- main commit b89f2bf58752045361fa088a6fc4311ba8798fcb에 성공 실행에서만 최근 30개 체크포인트를 남기고 현재 baseline ref를 보호하는 pruning step 및 스크립트를 추가했다.
- 첫 CI Run 43959203356: compileall 통과, pytest 96 passed / 1 failed / 1 xfailed. 실패는 보호된 오래된 ref 테스트의 기대값 오류이며 수정 후 재검증한다.
- 아직 실제 checkpoint pruning은 실행되지 않았다. CI 통과 후 다음 정상 운영 실행에서만 실행되도록 구성했다.
- 이후 main 변경은 활성 production run 종료 확인 후 수행한다. #2412 Discord 전송은 회수할 수 없으므로 후속 보고서 count 중복 가능성을 추적한다.


## 2026-11-17 운영 안정화 업데이트
- 체크포인트 보존 정책은 운영 run #2431에서 실제 정리 성공을 확인했다. 사전 실행 백업 브랜치는 30개 유지.
- 추가 개선: KST 기준 일일 카운트, Gemini 모델 404 즉시 fallback, Git push 실패 fail-closed.
- 상세 설계·근거·검증 한계: reports/OPS_TIMEZONE_MODEL_GIT_FAILURE_FIX_2026-11-17.md.

- KST/모델/Git 저장 실패 개선 CI: Run #59 성공(99 passed, 1 xfailed). Run #58은 테스트의 구형 모델명 기대값 2건으로 실패했으며 수정 후 #59에서 통과.
