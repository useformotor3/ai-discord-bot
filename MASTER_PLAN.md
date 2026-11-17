# CRA 서보 드라이브 마스터 계획서

## 목표

산업용 서보 드라이브 제조사가 EU CRA에 대응할 수 있도록 적용성 분석, 보안 요구사항 추적, 하드웨어·펌웨어·개발 프로세스 설계, 검증 증거, 한국어 보고서와 매뉴얼을 하나의 추적 가능한 체계로 만든다.

## 운영 원칙

- 기존 `main.py`와 운영 workflow는 변경 승인 전까지 보존한다.
- 조사 결과를 바로 최종 보고서로 승격하지 않는다.
- 모든 법령 주장은 공식 원문 조항·URL·원문 발췌·해석·제품 적용성을 함께 관리한다.
- 법적 의무, 표준의 요구사항, 엔지니어링 권고, 미확인 가설을 명확히 분리한다.
- 같은 주제를 반복 수집하는 것보다 기존 내용을 검증·정정·통합하는 일을 우선한다.
- 보고서 수를 늘리는 것보다 정확성, 추적성, 검증 가능성을 우선한다.
- 한국어를 기본 언어로 하고 영문 원문은 근거로 보존한다.
- 프로젝트의 공식 진행 기록은 GitHub 문서에 유지한다. 대화창은 의사소통 수단이지 단일 기록 저장소가 아니다.

## 관리 문서 구조

| 문서 | 책임 |
|---|---|
| `README.md` | 메인 페이지, 현황 요약, 주요 자료 링크 |
| `PROJECT_STATUS.md` | 현재 사실·상태·위험·다음 재개 지점 |
| `MASTER_PLAN.md` | 목표·우선순위·단계·완료 기준 |
| `AI_RULEBOOK.md` | 조사·검증·코드·기록 행동강령 |
| `SESSION_LOG.md` | 작업별 변경·검증·미완료 기록 |
| `reports/` | 상세 감사·설계·정정·통합 보고서 |
| `tests/` | mock/unit test와 테스트 실행 지침 |

## 단계 및 완료 기준

### Phase 0 — 운영 현황과 보안 기준선
- 저장소 트리, 공개 범위, Actions, workflow, state/history, 최근 아카이브를 점검
- 비밀정보·개인정보·고객사 기밀이 공개 저장소에 들어가지 않도록 점검
- 특수문자 파일명과 중복 상태파일 조사
- 완료 기준: 현재 구조와 위험이 상황판에 기록되고 미확인 사항이 분리됨

### Phase 1 — 조사 품질 개선
- 최근 보고서 표본을 공식 EUR-Lex 원문과 대조
- 조항 번호, 적용 시점, 보고 시한, 용어, 원문 인용 검증
- 출처 URL·접근일·원문 발췌·해석·신뢰 상태 기록
- 완료 기준: 정정 전/후가 추적되고 근거가 재검증 가능함

### Phase 2 — 자동화 코드 신뢰성
- 모델 전부 실패 시 실패 종료 및 실패 상태 저장
- 응답이 비어 있거나 오류 문구인 경우 보고서 성공 처리 금지
- state/history 입력 검증 및 시간 처리
- HTTP timeout/status/retry/backoff 처리
- 조사 결과의 URL·법령 조항·인용 검증 메타데이터 보존
- 중복 주제 인덱싱 및 정정 이력
- 실행 성공, 조사 생성 성공, 근거 검증 성공을 별도 상태로 분리
- 변경은 사전 제안 및 승인 후 작업 브랜치에서 수행

### Phase 3 — 테스트 및 CI
- 모델 호출·Discord 전송·Git push를 mock 처리한 단위 테스트
- 모델 전부 실패, 빈 응답, Discord 오류, Git push 실패, quota 경계 테스트
- workflow에 lint/test 단계를 별도 구성
- 완료 기준: 저장소 전체 테스트 로그와 CI 링크가 남고 실패 경로가 실제 검증됨

### Phase 4 — CRA 요구사항 추적표
- CRA 조항 / Annex I 요구사항 / 적용성 / 설계 통제 / 검증 방법 / 증거 / 담당을 연결
- 제품 범위·용도·시장 출시 형태·구성요소·연결 기능을 확인해 적용성을 판단
- ST MCU를 기본 설계 비교 기준으로 삼고 TI MCU/솔루션은 비교 항목으로 유지
- 완료 기준: 각 요구사항에 상태와 객관적 근거가 연결됨

### Phase 5 — 하드웨어·펌웨어·운영 설계
- 보안 부팅, 펌웨어 무결성, 디버그 포트, 인증·권한, 통신 인터페이스, 업데이트/복구, 키 관리, 로그, SBOM 등 검토
- CRA 요구사항과 기능안전(SIL) 요구사항을 혼합하지 않고 별도 추적
- 안전 관련 변경은 영향분석 및 전문 검토 없이 확정하지 않음

### Phase 6 — 통합 문서화
- 단일 통합 보고서 + 필요한 부속서(요구사항 추적표, 시험 증거, 설계 상세, 용어집)
- 문서마다 동일한 사실을 중복 기재하지 않고 기준 문서와 상호 링크
- 변경 이력과 검토 상태 유지
- 한국어 최종 보고서, 매뉴얼, 발표자료, 표/데이터 파일 생성

## 현재 진행 상태 — 2026-11-14

- Phase 1 표본 감사 및 #28/#29 정정본 작성: 수행
- Phase 2 P0 모델 응답 검증/실패 차단: 작업 브랜치 구현 및 격리 mock 테스트 9 passed 기록
- Phase 2 P1-A state/history 검증 및 datetime 호환: 작업 브랜치 구현, helper 독립 pytest 7 passed
- Phase 3 기본 원본 테스트 실행 기반: 확보. 테스트 전용 GitHub Actions Run #1~#3 success, 최신 Run #3에서 SHA 5개 일치, compileall 통과, pytest 21 passed
- Phase 2 P1-B1 Discord 전송 및 P1-B2 atomic persistence: 작업 브랜치 구현·CI 검증 완료; P1-B3 Git sync/P1-B4 구조 개선은 미구현
- Phase 4~6: 후속 단계

## 다음 실행 순서 — 2026-11-16 최신 우선순위

1. **통합 전 PR 사전 검사**: 최신 main/feature ref 재조회, PR 변경 경로와 merge-base 비교를 다시 확인한다.
2. **PR CI 및 conflict check**: PR 전용 mock CI, exact source SHA, compileall, 전체 pytest 및 GitHub conflict check를 검증한다.
3. **통합 승인 요청**: 코드 통합과 운영 실행/배포를 구분해 변경 범위·롤백·운영 영향과 함께 별도 승인받는다.
4. **P1-B3 설계**: Git push 결과의 durable status 및 재동기화 정책을 별도 승인 대상으로 제안한다.
5. **P1-B4 설계**: import-time execution 분리 및 테스트 가능한 구조를 별도 단계로 제안한다.
6. **조사 품질 구조화 및 CRA 요구사항 추적**: 기존 보고서 검증·정정 후 조항→제품 요구사항→통제→시험 증거로 연결한다.

## 완료 정의

작업이 완료됐다고 말하려면 다음을 모두 만족해야 한다.
1. 공식 원문과 조항 번호 확인
2. 적용성 및 전제조건 명시
3. 독립된 근거 또는 교차 검증
4. 설계·시험·문서 증거 연결
5. 코드 변경 시 관련 mock/unit test와 CI 통과(실행 범위 명시)
6. 미해결 사항·제약·사람의 승인 필요 지점 명시
7. GitHub 저장 파일 재조회 및 변경 내역 확인



## 2026-11-14 추가 실행 게이트 — 테스트 신뢰성

### P0 선행 조건
- 저장소 원본 파일의 Git blob SHA가 실행환경의 테스트 대상과 일치해야 한다.
- SHA 불일치 사본의 테스트 결과는 예비 검증이며 전체 저장소 테스트 완료로 인정하지 않는다.
- 기존 운영 workflow는 테스트에 사용하지 않는다. 별도 테스트 workflow 추가/수정은 별도 사용자 승인 대상이다.

### 테스트 fixture 보완 완료 기준
- subprocess mock에서 명령별 returncode 및 `check=True` 예외를 재현한다.
- Git add/commit/push 각각의 실패 경로를 검증한다.
- Discord mock에서 timeout, 네트워크 예외, HTTP 429, 4xx, 5xx를 재현한다.
- 부분 chunk 전송 후 실패와 재실행 정책을 검증한다.
- 테스트가 확인하지 않은 실패 경로는 문서에 미검증으로 남긴다.

### 현재 우선순위 갱신
1. 원본 SHA 일치 실행환경 확보
2. fixture의 실패 시나리오 보강 및 원본 전체 pytest
3. P1-B 코드 변경 범위·테스트·롤백 제안 및 사용자 승인
4. 승인 후 전송/저장/동기화 안정성 개선
5. CRA 출처 검증 메타데이터 및 요구사항 추적 체계 구축


## 2026-11-14 15:31 KST — CI 증거 게이트 갱신

- 작업 브랜치 HEAD `8813eb53b186b25e72ac157d664d636be6d68fd8`의 Actions runs 조회 결과 0건.
- 이는 CI 성공이 아니라 해당 브랜치에 연결된 workflow 실행 기록을 확인하지 못했다는 뜻이다.
- 기존 운영 workflow를 실행해 테스트를 만들지 않는다. 별도 테스트 전용 workflow 신설/수정은 사용자 승인 전 금지한다.
- 다음 선행 작업은 원본 blob SHA 일치 실행환경 확보이며, 실행 불가 시 정확한 장애 원인과 대체 가능한 검증 수준을 문서화한다.

## 2026-11-14 — 테스트 전용 CI 구축 완료

- 별도 `.github/workflows/tests.yml`을 작업 브랜치에 추가했다. 기존 운영 workflow와 분리되어 있으며, 읽기 전용 권한과 mock 테스트만 사용한다.
- GitHub Actions Run #1: [21 passed, success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43567990149)
- 테스트 대상 commit: `d31c604c6067685e33f6888cbc488c0e45d80be7`
- 다섯 개 핵심 소스/테스트 파일의 Git blob SHA가 모두 기대값과 일치한 뒤 compileall 및 pytest를 수행했다.
- 이로써 Phase 3의 **기본 원본 테스트 실행 기반 확보**는 완료로 변경한다. 단, 실패 경로 fixture 보강 및 P1-B 검증까지 완료된 것은 아니다.
- 테스트 가이드의 SHA 고정 기준을 유지하고, 소스 변경 시 승인된 검토와 함께 기준값을 갱신한다.

### 우선순위 재정렬
1. Git/Discord 실패 시나리오의 fixture 보강 설계 및 별도 승인
2. P1-B 전송·저장·동기화 안정성 변경안과 롤백 설계 제시
3. 승인 후 코드 구현 및 CI 회귀 검증
4. CRA 출처 검증 메타데이터와 요구사항 추적 체계 구축


### 최신 HEAD 반복 검증 결과
- 문서 기록 반영 후 최신 작업 브랜치 HEAD `dddba44a41851e9d0319ce9a91535a9d26145d92`에서 테스트 전용 workflow가 다시 실행되었다.
- [Run #3 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938), SHA 5개 일치, compileall 통과, pytest **21 passed in 0.19s**.
- 기본 원본 테스트 실행 기반 확보 완료를 유지한다. 실패 경로 보강과 P1-B는 별도 작업/승인이다.
 
## 프로젝트 로그 운영 방식

- 모든 의미 있는 작업 단위는 `PROJECT_LOG.jsonl`(기계 판독)과 `SESSION_LOG.md`(한국어 상세 기록)에 함께 남긴다.
- JSONL은 자동 집계·검색·재개를 위한 최소 사건 데이터이며, 기술 설명과 근거 해석을 대신하지 않는다.
- 새 대화에서 작업을 재개할 때 `AI_RULEBOOK.md`, `README.md`, `PROJECT_STATUS.md`, `MASTER_PLAN.md`, 최근 `SESSION_LOG.md`, `PROJECT_LOG.jsonl`을 먼저 확인한다.
- 운영 자동화 런타임 데이터(`state.json`, `history.json`)와 프로젝트 변경 로그를 혼합하지 않는다.

## 다음 작업 — 실패 경로 검증 설계 완료 후

1. [실패 경로 fixture 설계](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md) §16를 기준으로 테스트 전용 변경 범위를 사용자에게 제안한다.
2. 테스트 fixture/test 추가 승인을 별도로 받은 뒤 작업 브랜치에서 mock만 확장한다. main.py 및 workflow는 변경하지 않는다.
3. 테스트만으로 기존 코드의 실패 동작을 확인하고, 기대 동작과 실제 동작의 차이를 기록한다.
4. 그 결과를 근거로 P1-B 최소 코드 변경안·데이터 일관성 정책·롤백 계획을 제시하고 별도 승인을 받는다.
5. 승인된 P1-B만 구현하고 SHA 고정 CI 게이트를 통과시킨다.


## 실패 경로 fixture 단계 완료 후 우선순위
1. 현재 strict xfail 5건을 근거로 P1-B의 실패 정책과 부분 성공 모델을 확정한다.
2. Discord HTTP 429/5xx/network retry 정책, 4xx 영구 실패, chunk 단위 부분 전송 정책을 명세한다.
3. Git add/commit/push 실패를 실행 성공과 분리하고, state/history atomic write 및 archive ordering의 데이터 일관성 기준을 확정한다.
4. 구현 제안서에 기존 동작/변경 동작, 파일 diff, 승인 범위, 테스트, 롤백 및 운영 영향 분석을 포함해 사용자 승인을 받는다.
5. P1-B 승인 전에는 `main.py`를 변경하지 않는다.


## 2026-11-14 — 실패 주입 fixture 2차 확장
- 기존 승인 범위(테스트 fixture/test만) 안에서 Discord transport exception, 401/403, Git add/commit/push 단계별 실패 주입을 추가한다.
- 각 테스트는 mock 경계의 주입/관찰 능력만 검증한다. 실제 운영 코드의 재시도·상태화·부분 성공 정책은 증명하지 않는다.
- 새 CI에서 원본 blob SHA 일치, compileall, 전체 pytest 결과를 확인한 후에만 이 테스트 묶음을 완료 처리한다.
- 다음 P1-B 단계는 정책 명세 및 구현 제안서 작성이다. 운영 코드 변경은 사용자 별도 승인 전 금지한다.


## 2026-11-14 — 실패 주입 fixture 2차 확장 검증 완료
- Discord transport exception 2 case, HTTP 401/403 2 case, Git add/commit/push 단계별 실패 3 case를 추가했다.
- [Run #13](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208), 검증 commit `27d2c69287631b041672b9989fdeeb3066f5ebb9`: 6개 SHA 일치, compileall 통과, **30 passed / 5 xfailed**.
- Run #12의 SHA pin 누락 실패를 기록하고 Run #13에서 정정 완료했다.
- 다음 우선순위는 P1-B 동작 정책 명세(Discord retry/영구 실패/부분 chunk, Git 단계 상태, archive·state/history atomic write 및 복구)다. 운영 코드 변경은 별도 승인 전 금지한다.


## 2026-11-14 — P1-B 설계 정책 정밀화
- [정책 명세 §17](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md#17-p1-b-전송저장동기화-정책-명세--2026-11-14-구현-전-설계)를 P1-B 구현 전 기준으로 사용한다.
- Discord POST는 중복 가능성을 고려해 delivery unknown과 재시도 가능 상태를 구분한다. 429는 Retry-After/retry_after 준수, 400/401/403/404는 영구 실패로 중단한다.
- state/history의 다중 파일 일관성에는 transaction journal/recovery 검증이 필요하다.
- 다음 단계는 구현 전 변경 제안 및 승인이다. 운영 코드 변경은 별도 승인 전 금지한다.


## 2026-11-14 — Discord 실패 테스트 정책 정합화
- 503 응답의 무조건 재시도 기대를 제거하고 delivery_unknown으로 남기는 duplicate-safe 계약으로 수정했다.
- 401/403/404 영구 실패 및 자동 재시도 금지 xfail 3 case를 추가했다.
- [Run #15](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842): 30 passed / 8 xfailed.
- 다음 단계는 P1-B 최소 구현안과 복구/중복 방지 설계를 승인 요청하는 것이다. 운영 코드 변경은 별도 승인 전 금지한다.


## 과거 승인 게이트 기록 — P1-B1 (이후 승인·구현 완료)
- P1-B 전체를 한 번에 구현하지 않고 B1 Discord 전송, B2 로컬 저장, B3 Git sync, B4 구조 개선으로 나눈다.
- 다음 승인 요청은 B1만으로 제한한다. 설계서 §18의 변경 파일·테스트·롤백·제외 범위를 따른다.
- 승인 전에는 main.py 및 운영 관련 코드를 수정하지 않는다.


## 2026-11-16 — P1-B1 Discord 전송 구현 및 CI 확인
- P1-B1을 구현하고 테스트 전용 Actions Run #18에서 43 passed / 1 xfailed를 확인했다.
- 1 xfailed는 P1-B3 Git sync 상태화 미구현 기대 동작이다.
- Run #17 SHA pin 오류는 기록 후 수정했다. Run #18에서 source SHA, compileall, 전체 pytest 통과를 확인했다.
- 당시 다음 우선순위는 P1-B2 설계였다. P1-B2는 이후 별도 승인으로 구현·검증 완료했다.


## 이전 통합 게이트 스냅샷 — 2026-11-16 (이후 merge-base 재감사로 갱신)
1. [완료] main/작업 브랜치 ref, merge-base, ahead/behind 재조회.
2. [완료] merge-base와 main의 recursive Git tree 비교(양쪽 API truncated=false).
3. [완료] 운영 state/history/archive 및 main.py/workflow 원문·SHA 교차확인.
4. [진행 전 보류] 데이터 보존을 전제로 한 코드/문서 통합 후보 분리와 migration 설계.
5. [승인 대기] main 반영, 데이터 변경, workflow 실행, P1-B2/B3/B4 구현.

통합은 단순 branch merge가 아니라 운영 데이터와 자동 생성 보고서 보존을 포함한 별도 change-control 작업으로 취급한다. 현재 main 대비 152 ahead / 657 behind이며 통합을 진행하지 않는다.


## 2026-11-16 최신 통합 감사 스냅샷
- main HEAD `31e0f8137630630ee30ea55add039b571f2c6801`, 작업 브랜치 HEAD `c43abc3315d8d7c8a3d5f4fc209465428a7e8aff`.
- 작업 브랜치 153 ahead / 658 behind main. main 고유 archive 658개, history 2,250개, state count 111.
- 데이터 보존 및 별도 통합 설계 전까지 merge/rebase/PR merge 금지.


## 다음 실행 단계 — P1-B2 구현/검증 완료
- [완료] P1-B2 원자적 저장 설계·구현: `reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md`.
- [완료] crash/failure injection tests 및 테스트 전용 CI Run #23: 63 passed / 1 xfailed.
- [완료] 정확한 source blob SHA, compileall, 전체 pytest 확인.
- [완료] P1-B2 diff/운영 위험 검토 및 merge-base 기반 통합 전략 보고서 작성.
- [다음] PR 사전 검사, PR CI 및 conflict check. PR 생성/merge/운영 rollout은 별도 승인 대상.
- [보류/별도 승인] P1-B3 Git sync status, P1-B4 import-time execution cleanup.
- 운영 main/data/workflow 변경과 merge/rebase/PR merge는 별도 승인 전 금지.


## 2026-11-16 운영 모니터링 설정
- ChatGPT 예약 작업 `매일 Git 브랜치 통합 상태 점검` 생성 완료. ID `6afacb7561d8819182728a42ffd4e867`, 매일 09:00 Asia/Seoul, 첫 실행 2026-11-17 09:00.
- refs/ahead-behind/recursive tree/state-history-archive 변경을 재조회한다. 안전할 때만 작업 브랜치의 상황판·로그 문서를 갱신한다.
- 운영 main/data/workflow 수정, merge/rebase/PR merge, 실제 Gemini/Discord 호출은 금지한다.
- 이 예약 작업은 ChatGPT의 모니터링이며 GitHub Actions 운영 workflow와 별개다.


## 최신 작업 브랜치 및 통합 기준 — 2026-11-16
- 작업 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16`; 감사 스냅샷 HEAD `0fe9912b5dbba29eeb3ebd9e9f2c16a42544f925`.
- 운영 main HEAD `267d97478b785e6bb268e224a70dbad6631cf43e` (#131); merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare: 221 ahead / 678 behind. 이는 commit count이며 파일 삭제를 뜻하지 않는다.
- merge-base 기준 main은 archive 678개 추가·삭제 0·history/state 2개 수정; 작업 브랜치는 23개 경로 추가·삭제 0·main.py 1개 수정이다.
- 운영 데이터 보존을 위한 3-way PR 통합 후보가 양호하나, 실제 PR conflict check 및 별도 승인 전 merge 금지.


## 2026-11-16 — P1-B2 구현 완료
- 전용 브랜치 `feature/p1-b2-atomic-persistence-2026-11-16`에서 durable journal 기반 multi-file persistence를 구현했다.
- recovery는 state/history 읽기와 외부 서비스 호출보다 먼저 수행한다. commit 시 읽은 원본 snapshot SHA를 확인해 동시 변경을 fail-closed 한다.
- 장애 주입 및 통합 테스트 포함 Run #23에서 63 passed / 1 xfailed.
- POSIX flock/fsync 기반이므로 Ubuntu 등 POSIX 실행 환경을 전제로 한다. Windows lock backend는 미구현.
- P1-B3/B4, 운영 데이터, 운영 workflow, merge/rebase는 이번 승인 범위 밖이다.


## 2026-11-16 — 통합 전략 감사 완료
- merge-base 기준 전체 recursive tree 비교와 history→archive 참조 무결성 확인을 완료했다.
- main의 678개 archive는 merge-base 이후 추가된 자료이며 작업 브랜치가 삭제한 파일이 아니다. main history/state는 main에서만 변경됐고 작업 브랜치는 merge-base blob을 유지한다.
- 작업 브랜치의 코드·테스트·관리 문서 변경은 main의 운영 데이터 변경과 경로상 분리되어 3-way PR 통합 후보로 평가한다.
- P1-B2 recovery target allowlist 보강 후 Actions 43851438733: 70 passed / 1 xfailed.
- PR CI 트리거를 pull_request→main 및 main push로 준비했다.
- 실제 PR 생성, merge, rebase, 운영 workflow/data 변경은 수행하지 않았다. 통합 및 운영 배포는 별도 승인 후 진행한다.
- 상세: `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`.


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


## 2026-11-16 — 복구 우선 통합/운영 단계 추가
1. 체크포인트 고정: main/feature 백업 브랜치 SHA를 원격 재조회해 검증한다.
2. 최신 base 통합 검증: main 자동 아카이브가 진행된 상태에서 PR base/head SHA, merge-base, 전체 diff 및 PR mergeability를 다시 확인한다. 최신 base에 대한 CI 결과가 없으면 merge하지 않는다.
3. 운영 데이터 복구체계: state/history/archive snapshot, checksum, file count, history 참조 무결성 검증 및 별도 복원 리허설을 구축한다.
4. 통합: 안전 게이트 통과 시 merge commit으로 통합하고, main HEAD와 PR merge SHA를 기록한다.
5. 첫 실행 검증: 운영 데이터 백업 후 단일 실행, state/history/archive 변화량 및 참조 무결성을 확인한다. 이상 시 재실행을 막고 코드 revert/데이터 복구를 수행한다.
6. 지속 운영: 매 세션 시작 시 이전 정상 commit/백업 ref/최근 CI를 확인하고, 변경 단위별 테스트 및 복구 가능성을 검증한다.

완료 기준은 단순히 Git commit이 존재하는 것이 아니라, 코드와 운영 데이터 각각에 대해 정상 기준점으로 되돌리는 절차가 실제로 검증된 상태다.

## 2026-11-16 — 운영 데이터 baseline 및 rollback
- main HEAD를 immutable SHA로 고정한 뒤 state/history/archive를 같은 SHA에서 검사한다.
- Git safety branch는 tracked 운영 데이터 기준 snapshot으로 유지한다.
- 첫 운영 실행 전 per-run snapshot branch 생성과 실패 시 restore commit 경로를 mock으로 구현·리허설한다.
- U+200B legacy state 파일은 참조/생성 경위를 확인할 때까지 보존한다.
- 코드 rollback과 데이터 rollback을 분리하고, 외부 Discord 전송은 회수 불가 경계로 유지한다.

## 2026-11-16 — 운영 rollback guard 계획
- 운영 workflow 실행 전 baseline branch를 생성하고 실행 후 append-only 및 참조 무결성을 검증한다.
- 복구는 remote main이 실행의 단일 child commit일 때만 data-only restore commit으로 수행하며 force-push하지 않는다.
- local bare Git remote integration tests 및 최신 base PR CI 성공 후 통합한다.
- 첫 실제 운영 실행 결과를 별도 관찰하고 외부 Discord 메시지는 회수 불가 경계로 관리한다.


## 2026-11-16 — latest rollback guard verification
- Run #43875746973: 87 passed, 1 xfailed; compileall and source blob identity checks passed.
- Tested normal one-report append, archive/history mismatch, deleted archive, invalid state count, date rollover, unsafe archive paths, local bare remote data restore, no-push fail-closed, quota no-op, missing state restore, symlink/empty archive detection.
- main #162 baseline state=162, history=2,301, archive=2,301, missing refs=0. safety/pre-merge-main-adf74ea exact SHA.
- First production execution is not yet performed; Gemini/Discord calls not made in CI.

## 2026-11-16 — 통합 단계 완료 및 다음 운영 단계
- Phase 2 신뢰성 개선 및 Phase 3 테스트 기반/운영 data guard를 main에 통합 완료.
- PR #1 merge commit 방식, post-merge CI 통과.
- 다음은 production workflow 첫 실행 관찰이다. 실행 전 snapshot branch 생성, 실행 후 operational_guard 결과, state/history/archive 무결성을 확인한다.
- 실제 운영 실행 결과를 법적 CRA 근거 검증과 혼동하지 않는다.


## 2026-11-17 — 자동화 운영 안정화 후속 작업
1. checkpoint pruning 테스트 기대값을 수정하고 main CI 성공을 확인한다.
2. 다음 production run은 정상 종료 및 guard 통과 여부를 확인한다. 실제 pruning이 30개 기준으로 작동했는지 원격 ref 수를 재조회한다.
3. #2412의 Discord 전송/미저장 보고서 #235를 중복 없이 처리할 방법을 검토한다. 보고서 본문이 원격에 없으므로 추측해 복원하지 않는다.
4. Gemini 모델 설정의 404 fallback 원인을 공식 모델 목록 및 SDK API 지원 기준으로 확인한다.
5. Git push 실패 시 운영 workflow가 성공처럼 끝나지 않도록 하고, main 변경과 운영 데이터 쓰기의 동시성 정책을 별도 설계·테스트한다.
6. main 변경 전 활성 production workflow가 없는지 확인한다. 작업 중 운영 workflow가 시작되면 main 변경을 중단한다.


## 2026-11-17 운영 신뢰성 후속 우선순위
1. KST 날짜 경계 및 기존 UTC naive health-check timestamp 호환성 테스트를 통과시킨다.
2. Gemini API 404/NOT_FOUND 즉시 fallback 및 공식 모델 ID 사용을 테스트한다.
3. Git push 실패가 workflow 실패로 전파되는지 mock으로 검증한다. 실제 Discord/Gemini는 호출하지 않는다.
4. CI 통과 후 다음 운영 실행에서 state date가 KST 기준인지, history/archive가 한 건씩 append되는지 확인한다.
5. Git push race가 발생하면 강제 push하지 않고 fail-closed한다. Discord delivery와 Git archive가 분리되므로 중복 방지/outbox 설계는 별도 과제로 둔다.


## 2026-11-17 — KST/model/Git fail-closed 구현 검증
- [완료] Asia/Seoul 기준 날짜·시간 및 legacy naive UTC health-check 호환.
- [완료] gemini-3.8-flash → gemini-3.5-flash-lite, 404/NOT_FOUND 즉시 fallback.
- [완료] Git 저장 실패 시 비정상 종료, 강제 push 금지.
- [완료] CI Run #59: 99 passed, 1 xfailed.
- [대기] 다음 운영 실행에서 KST 날짜·일일 count, 실제 Gemini 모델 ID 성공, Git push와 operational_guard의 정상 완료 확인.
- [대기] Discord 전송 이후 Git 저장 실패 시 재전송 중복 방지/outbox 설계.


## 2026-11-17 — CRA 자동 출처검증 gate (Phase 1/2 연결 단계)
### 목적
- 형식 검사만으로 사실 정확성을 추정하지 않는다.
- 보고서 생성 전에 EUR-Lex 공식 CRA 통합본을 직접 확보하고, 원문·버전·조항·인용의 최소 추적성을 확보한다.

### 구현 완료 기준
- 공식 EUR-Lex HTTPS URL 직접 조회 및 최종 호스트 확인.
- 통합본 버전 및 알려진 정오표 C1/C2/C3 날짜 확인.
- 원문 확보 실패 또는 corrigenda index 누락 시 fail-closed.
- 보고서에 정확한 공식 URL/버전, Article/Annex locator, 50자 이상 원문 직접 인용을 요구하고 수집 원문과 대조.
- 모든 보고서를 법률 해석·제품 적용성 미검증 초안으로 명시.
- 실제 Gemini/Discord 없이 전체 mock suite와 blob SHA/compileall CI 통과.

### 완료 상태 및 경계
- 작업 브랜치: feature/cra-source-grounding-atomic-2026-11-17, Draft PR #3.
- CI Run #89: 103 passed, 1 xfailed.
- 이 gate는 하나 이상의 직접 인용이 원문에 존재하는지 확인하는 provenance gate다. 본문 모든 문장에 대한 논리적 함의 검증, 규정 해석, 제품 분류, 법적 적합성 결론은 제공하지 않는다.
- EUR-Lex consolidated text 자체는 documentation tool이며, 공식 관보 정본과 corrigenda가 법적 효력의 기준이다.
- Google Search Grounding은 Gemini 3 계열 Free tier에서 제공되지 않는 현재 요금 조건 때문에 선택하지 않았다. EUR-Lex 직접 조회는 Gemini 검색 Grounding 과금과 분리된다.

### 후속 우선순위
1. 운영과 분리된 canary에서 EUR-Lex HTML endpoint 접근성·응답 길이·정오표 날짜 확인.
2. Article/Annex/point별 claim-to-quote 매핑으로 검증 단위를 확대.
3. 원문 버전·해시 변화 및 corrigenda 추가 시 경보/차단.
4. 검증 실패·불확실 보고서는 게시하지 않고 검토 큐에 남기는 구조를 설계.


## 2026-11-17 — EUR-Lex 실제 endpoint canary 완료
- Read-only canary workflow 및 스크립트를 추가했다. 실제 Gemini/Discord/운영 workflow와 분리된다.
- Canary Run #11 성공: HTTPS EUR-Lex endpoint 응답, 최종 host, 196,076자 visible text, corrigenda 3개 날짜 확인.
- 법적 효력 주의: EUR-Lex consolidated text는 documentation tool이며 Official Journal 정본 및 corrigenda가 법적 효력의 기준이다.
- 다음 단계는 claim-to-evidence 매핑 및 원문 버전/hash 변경 감지다.


## 2026-11-17 — 후속 법령 원문 source pack 확장 완료
- CRA 통합본 외 EUR-Lex 공식 원문 3건(2025/327, 2025/1535, 2026/881)을 수집 대상으로 추가했다.
- CI Run #141: 103 passed, 1 xfailed; EUR-Lex canary Run #26: source pack 추출 텍스트 220,715자(2025/327은 Article 104 관련 발췌), 각 원문 HTML visible text 개별 길이는 196,076자 / 394,354자 / 6,246자 / 15,284자.
- 제품 적용성을 추정하지 않고 EHR 적용 시기, L-category 제한적 제외, Article 16 통지 전파 지연을 분리한다.
- 다음 우선순위: (1) claim-to-evidence 단위 검증 (2) Official Journal 정본/정오표 차이 대조 (3) 모델 출력 호환성 비운영 검증 (4) 게시 전 사람 검토 단계.
- 운영 main 병합은 위 항목과 별도 검토 후 결정한다.


## 2026-11-17 — 최종 문서·코드 일치 검증
- 최신 source blob SHA/compileall/전체 pytest: CI Run #154, 103 passed, 1 xfailed.
- 최신 EUR-Lex source pack read-only canary: Run #29 success.
- 보고서와 상황판은 위 최신 run ID와 작업 브랜치 SHA를 기준으로 동기화했다.
- Draft PR #3은 open/mergeable 상태이나, claim-to-evidence, 관보 정본 대조, Gemini 호환성 canary가 미완료이므로 main 병합 전 상태로 유지한다.


## CRA 보고서 신뢰성 개선 — claim-to-evidence 단계
1. 구조화 claim_id와 source_id/locator/직접 인용 연결을 생성 단계의 필수 산출물로 만든다.
2. 각 법적 주장마다 해당 원문 인용을 독립 검증하고, 실패 시 전송·아카이브·count 증가를 차단한다.
3. legal requirement, official explanation, interpretation, engineering recommendation을 별도 유형으로 분류한다.
4. mock CI 통과 후 격리된 실제 Gemini 모델 호환성 canary를 설계한다. 운영 Gemini/Discord workflow를 테스트에 사용하지 않는다.
5. claim mapping 통과와 별개로 Official Journal 정본 및 corrigenda 대조, 제품 범위·적용성 검토를 완료하기 전 CRA 적합성 결론으로 승격하지 않는다.


### 진행 결과 — 2026-11-17
- [완료] 구조화 claim-to-evidence validator 구현 및 main.py report acceptance gate 연결.
- [완료] legal requirement / official explanation / interpretation / engineering recommendation 분리.
- [완료] mock tests, 기존 main.py 통합 테스트, source SHA pin, compileall 및 전체 pytest 검증: 112 passed, 1 xfailed.
- [완료] EUR-Lex read-only canary: success.
- [미완료] 실제 Gemini 모델 JSON 출력 호환성 canary, Official Journal 정본/정오표 대조, 본문 claim 누락에 대한 사람 검토.
- [보류] main 통합. PR #3는 main 최신화 및 통합 CI/보호 경로 검토 전까지 Draft로 유지.


## Gemini model compatibility canary — 수동 비용 게이트
1. [완료] 공식 가격표에서 Gemini 3.8 Flash Free Tier의 token 가격, data-use 조건, Search Grounding 제한을 확인했다.
2. [완료] 공개 합성 문장 1건만 사용하는 opt-in JSON compatibility script와 manual workflow를 추가했다.
3. [완료] mock-only tests를 추가하고 실제 API 요청이 없는 CI로 검증한다.
4. [보류] 실제 API canary는 project billing tier 확인 전 dispatch하지 않는다. 실행 전 Free Tier/no paid billing을 명시 확인해야 한다.
5. [후속] generateContent가 legacy로 분류되어 Interactions API 권장 상태이므로, 현행 코드 호환성 확인 후 migration 비용/영향을 별도 검토한다.


### Gemini canary 구현 상태
- [완료] 합성 입력 전용 REST canary script 및 mock-only tests 추가.
- [완료] manual workflow에 Free Tier 확인 boolean 기본값 false 적용. 자동 호출 없음.
- [제약] workflow 파일은 Draft PR branch에만 있으므로 default branch 반영 전에는 workflow_dispatch 실행 불가.
- [보류] default branch 반영 여부는 main 최신화, PR 검토, Free Tier/billing 상태 확인 후 결정한다. 현재 실제 Gemini API 요청은 하지 않는다.

## 2026-11-17 — 통합 사전 감사 결과 및 다음 게이트
1. [완료] 최신 원격 상태 재조회: main 9ad23da7, feature 감사 기준 3b1c2f3, 116 ahead / 9 behind, diverged.
2. [완료] main과 feature의 main.py / tests workflow 차이 확인. main CI는 CRA gate를 포함하지 않으므로 통합 검증 대체 불가.
3. [완료] claim quote가 다른 Article에 위치해도 통과할 수 있는 false-positive를 확인하고 Article/Annex 범위 검사와 regression test 추가.
4. [진행] 신규 CI #279 및 EUR-Lex read-only Canary #95 결과/로그 확인.
5. [우선] Official Journal corrigenda 2024-12-05, 2025-07-02, 2025-10-17의 개별 원문을 source pack에 추가하고 각 정정 대상·정정 문구를 검증한다. 현재는 consolidated text 내 날짜 존재 확인만 수행한다.
6. [후속] claim locator의 paragraph/point 범위 검사 및 false-negative 테스트 추가. Article/Annex 범위 검사는 법률적 정확성 보증이 아니다.
7. [후속] main의 9개 후속 커밋과 운영 데이터 보존 상태를 immutable SHA로 감사하고, 별도 integration branch에서만 통합·회귀 테스트한다.
8. [보류] PR #3 Draft 유지. 최신 main 통합 CI/보호 경로/데이터 불변성 검증 전 merge 금지. Gemini live canary는 billing tier와 데이터 사용 조건 미확인으로 미실행.

## 2026-11-17 — claim scope 회귀검증 및 후속 우선순위
1. [완료] Article/Annex scope quote gate 추가 및 교차 조항 quote 거부 회귀 테스트.
2. [완료] 첫 CI #279 실패(25 failed, 92 passed, 1 xfailed)의 원인을 regex double-escape로 특정하고 수정.
3. [완료] 수정 head CI #294: 117 passed, 1 xfailed; exact SHA, compileall, full pytest 통과.
4. [완료] EUR-Lex read-only Canary #101 success.
5. [우선] 개별 Official Journal corrigenda 3건을 source pack에 추가하고 정정 대상·정정 문구를 기계 검증한다. 날짜 인덱스만 확인하는 현 상태를 개선한다.
6. [후속] paragraph/point 수준 locator 범위 검증과 false-negative fixture 추가.
7. [후속] 최신 main과 다시 비교(마지막 스냅샷 125 ahead / 10 behind)하고 운영 state/history/archive 불변성 확인 후 별도 integration branch에서 검증한다.
8. [보류] PR #3 Draft 유지. 최신 main 기준 통합 CI 및 보호 경로 검증 전 merge 금지. Gemini live canary는 billing tier 확인 전 미실행.

## 2026-11-17 — Official Journal corrigenda source gate 확장
1. [완료] CRA 영어 corrigenda 2024-12-05, 2025-07-02, 2025-10-17을 개별 공식 ELI URL로 source catalog에 추가.
2. [완료] 각 정오표의 Article/표제와 원문 for/read 문구를 필수 marker로 검사. 누락/비공식 redirect/짧은 응답은 fail-closed.
3. [완료] report manifest와 Gemini prompt에 3개 개별 정오표 source ID/URL/version 반영.
4. [완료] EUR-Lex live read-only Canary #115 success; 7개 source, 245,502 visible-text chars 수집.
5. [완료] 최종 격리 CI #323: 117 passed, 1 xfailed; source SHA, compileall, full pytest 통과.
6. [후속] paragraph/point 수준 claim locator 정확도와 false-negative 테스트.
7. [후속] 최신 main 및 운영 state/history/archive 보존 상태 immutable SHA 감사 후 별도 integration branch에서 검증.
8. [보류] PR #3 Draft 유지. 최신 main 통합 CI 완료 전 merge 금지. Gemini live canary는 billing/data-use 확인 전 미실행.

## 2026-11-17 — 자동 archive #14–#17 정정 감사
1. [완료] 원본 archive #14–#17의 immutable blob SHA를 확인하고 원본 파일은 수정하지 않음.
2. [완료] correction report #14: Article 11/13/14, Annex I Part II CVD·신고 요건 구분.
3. [완료] correction report #15: Annex I Part I (2)(f)의 법적 요구와 서보 구현 후보, real-time/PLC/STO 의무 주장을 분리.
4. [완료] correction report #16: 직접 인용 불일치, manufacturer/user 오기, cryptographic mechanisms 비원문 구절, 디지털 서명 의무 과장을 정정.
5. [완료] correction report #17: RBAC/least privilege/MFA/session timeout 직접 의무 및 원문 인용 오류 정정.
6. [진행] archive #13 이하를 원문/공식 OJ와 대조하고 정정 필요 항목을 누적한다.
7. [후속] 정정 보고서를 master CRA report에 통합하고 claim-level source evidence와 engineering recommendation을 분리한다.

## 2026-11-17 — archive #18 정정
1. [완료] 원본 archive #18 blob SHA f986f2f2db5f74ca8dd072deb2fe90e013b4a63c 확인, 원본 보존.
2. [완료] correction report #18 생성: Annex I Part I (2)(b)/(d)/(l) 분리, RBAC/least privilege 직접 인용 및 실패 인증 로그 의무 과장 정정.
3. [진행] archive #13 이하 역순 감사 및 correction index 누적.

## 2026-11-17 — latest-main integration 및 다음 보고서 우선순위
1. [완료] main의 13개 후속 자동 archive 커밋(#6–#18)이 state/history/archive만 변경함을 확인.
2. [완료] PR #5로 최신 main snapshot을 integration branch에 동기화.
3. [완료] PR #4로 CRA source/claim gate를 integration branch에 병합. main은 변경하지 않음.
4. [완료] state.json/history.json/archive #18 blob SHA가 main과 integration에서 동일함을 검증.
5. [완료] 통합 트리 CI #366: 117 passed, 1 xfailed; EUR-Lex Canary #134 success.
6. [완료] correction reports #14–#18 작성, 원본 archive SHA 보존.
7. [진행] archive #13 이하 역순 감사, 공식 OJ/정오표 대조 및 correction index 축적.
8. [후속] 검증된 claim을 통합 CRA 한국어 보고서로 정리하고, 서보 드라이브 설계 적용 항목/근거/권고를 분리.
9. [후속 별도 산출물] SIL 3 서보 드라이브 벤치마킹 보고서 및 하드웨어 블록 설계 작성. IEC 61508/IEC 61800-5-2 등 기능안전 근거를 CRA 사이버보안 근거와 분리해 추적.
10. [보류] PR #6 Draft 유지. main 병합은 통합 보고서/기능안전 산출물 검토 및 명시적 승인 전 수행하지 않는다.

## 2026-11-17 — archive #19 감사 및 다음 우선순위
1. [완료] main archive #19 snapshot을 PR #7로 integration에 동기화. main은 변경하지 않음.
2. [완료] state/history/archive #19 exact blob SHA가 main과 integration에서 동일함을 확인.
3. [완료] correction report #19 생성: Annex I Part I (2)(l) logging, (2)(c) update, (2)(h) availability locator/quote 오류 정정.
4. [완료] correction reports #14–#19 누적, 원본 archive 모두 보존.
5. [진행] archive #13 이하 역순 감사 및 correction index.
6. [후속] 검증된 claim을 통합 CRA 한국어 보고서와 서보 드라이브 보안 설계 추적표로 정리.
7. [후속 별도 산출물] SIL 3 서보 드라이브 벤치마킹 및 하드웨어 블록 설계 보고서. 기능안전 규격과 CRA 사이버보안 규격을 분리 추적.

## 2026-11-17 — archive #13 correction audit
1. [완료] 원본 archive #13 blob SHA 확인 및 보존.
2. [완료] Article 11/13/14와 Annex I Part II (1)–(8) 의무를 구분해 correction report #13 작성.
3. [완료] CVD 정책, 제보 연락 주소, 수정 취약점 공개, Article 14 mandatory reporting을 분리.
4. [진행] archive #12 이하 역순 감사. 기존 보고서의 proposal/draft 문구와 enacted OJ 문구를 구별.

## 2026-11-17 — archive #12 correction audit
1. [완료] Article 13(8)/(9)/(14)/(19) 및 Annex I Part II (2)/(8) 분리.
2. [완료] support period 5년 원칙, security update availability 10년/잔여기간 중 긴 기간, 무상 제공 예외를 correction report #12에 반영.
3. [진행] archive #11 이하 역순 감사.

## 2026-11-17 — archive #11 correction audit
1. [완료] Annex I Part I (2)(d)/(e) exact quote 대조.
2. [완료] attack-surface/secure-by-default 법적 요구와 포트 disable/opt-in/least-privilege 구현 권고를 분리.
3. [완료] factory reset의 안전 파라미터/보안 설정 영향 검토 항목을 correction report #11에 기록.
4. [진행] archive #10 이하 역순 감사.

## 2026-11-17 — archive #10 correction audit
1. [완료] Article 13(8)/(9), Annex I Part II (1)–(8) 구분.
2. [완료] non-verbatim quote 및 CVD/free update/support-period 혼합을 correction report #10에 반영.
3. [진행] archive #9 이하 역순 감사.

## 2026-11-17 — archive #9 correction audit
1. [완료] Annex I Part II (1) SBOM minimum top-level dependency 범위 검증.
2. [완료] SPDX/CycloneDX, transitive dependencies, hardware revision mapping을 법적 의무가 아닌 구현 선택/권고로 분리.
3. [완료] vulnerability remediation (2)와 fixed-vulnerability disclosure (4) 구분.
4. [진행] archive #8 이하 역순 감사.
