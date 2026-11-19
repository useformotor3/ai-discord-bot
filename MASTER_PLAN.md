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
- Phase 2 P1-B Discord 전송/Git 동기화 신뢰성: 설계만 존재, 별도 승인 대기
- Phase 4~6: 후속 단계

## 다음 실행 순서 — 객관적 우선순위

1. **실패 경로 fixture 보강 설계**: Git add/commit/push 실패, Discord timeout/network/429/4xx/5xx, 부분 성공을 테스트하는 시나리오를 설계한다.
2. **P1-B 제안**: Discord timeout/status/retry와 Git push 상태화의 최소 변경 범위·위험·테스트·롤백을 제시하고 승인받는다.
3. **P1-B 구현 및 테스트**: 승인된 범위만 작업 브랜치에 반영하고 동일 CI 게이트에서 회귀 검증한다.
4. **조사 품질 구조화**: 출처 메타데이터와 topic/correction 인덱스 설계 및 검증.
5. **요구사항 추적**: CRA 조항에서 제품 요구사항, 설계 통제, 시험 증거까지 연결.
6. **통합 문서화**: 검증된 사실만 한국어 기준 보고서와 필요한 부속서에 반영.

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


## 다음 승인 게이트 — P1-B1
- P1-B 전체를 한 번에 구현하지 않고 B1 Discord 전송, B2 로컬 저장, B3 Git sync, B4 구조 개선으로 나눈다.
- 다음 승인 요청은 B1만으로 제한한다. 설계서 §18의 변경 파일·테스트·롤백·제외 범위를 따른다.
- 승인 전에는 main.py 및 운영 관련 코드를 수정하지 않는다.


## 2026-11-16 — P1-B1 Discord 전송 구현 및 CI 확인
- P1-B1을 구현하고 테스트 전용 Actions Run #18에서 43 passed / 1 xfailed를 확인했다.
- 1 xfailed는 P1-B3 Git sync 상태화 미구현 기대 동작이다.
- Run #17 SHA pin 오류는 기록 후 수정했다. Run #18에서 source SHA, compileall, 전체 pytest 통과를 확인했다.
- 다음 우선순위는 P1-B1 경계의 추가 검토 및 문서 정합성, 이후 P1-B2 atomic persistence 설계다. P1-B2는 별도 승인 전 구현하지 않는다.


## 통합 게이트 — 2026-11-16 감사 반영
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


## 다음 실행 단계 — P1-B2 설계 완료
- [완료] P1-B2 원자적 저장 설계서: `reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md`.
- [완료] 최신 통합 감사 스냅샷: `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md`.
- [승인 대기] P1-B2 코드 구현 및 crash/failure injection tests.
- [보류] P1-B3 Git sync status, P1-B4 import-time execution cleanup.
- 운영 main/data/workflow 변경과 merge/rebase/PR merge는 별도 승인 전 금지.


## 2026-11-16 운영 모니터링 설정
- ChatGPT 예약 작업 `매일 Git 브랜치 통합 상태 점검` 생성 완료. ID `6afacb7561d8819182728a42ffd4e867`, 매일 09:00 Asia/Seoul, 첫 실행 2026-11-17 09:00.
- refs/ahead-behind/recursive tree/state-history-archive 변경을 재조회한다. 안전할 때만 작업 브랜치의 상황판·로그 문서를 갱신한다.
- 운영 main/data/workflow 수정, merge/rebase/PR merge, 실제 Gemini/Discord 호출은 금지한다.
- 이 예약 작업은 ChatGPT의 모니터링이며 GitHub Actions 운영 workflow와 별개다.


## 최신 작업 브랜치 포인터
- P1-B2 설계/감사 문서 커밋 이후 작업 브랜치 HEAD는 `38bb00c815eee3e754bff14f67bcab2f23172a92`이며, main HEAD `036334dd2665752c2e6ddb024001771cff4064c5` 대비 156 ahead / 660 behind다. 앞선 155/660 수치는 설계 문서 커밋 직전의 감사 기준 HEAD `227e3298066af4bda83fb0713fc1d57c749ee8c6` 기준 스냅샷이다.


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

### 통합 판단
- 이 감사 기준에서 작업 브랜치는 main의 조상이며 ahead=0이다. 따라서 main에 없는 작업 브랜치 고유 커밋은 없다.
- 작업 브랜치를 main에 병합하는 것은 새로운 기능 반영 경로가 아니며, 현재 데이터 및 코드 차이를 해결하지 않는다. 이 브랜치를 기준으로 통합하지 않는다.
- 실패 경로 fixture가 필요한 경우 main에 존재하는 테스트 경로와 해당 이력을 별도로 확인한 뒤, 최신 main에서 새 작업 브랜치를 만드는 편이 안전하다. 이번 감사에서는 이를 구현하거나 변경하지 않았다.


## 2026-11-19 — 통합 판단 갱신
- test/failure-path-fixtures-2026-11-14는 감사 기준 main 대비 1 ahead / 1,357 behind이며 merge-base는 7ae3b251861b9a3de9981bd7202e346d05ca9430이다.
- 전체 recursive tree 비교(truncated=false): main 2,548 blobs, 작업 브랜치 1,617 blobs; main-only 931, branch-only 0, modified 19.
- 운영 데이터 차이: main archive/history 각 2,431, 작업 브랜치 각 1,592; main에 archive 839개와 history 항목 839개가 추가됐다. branch history는 main history의 정확한 prefix다. state.json도 별도 값으로 변경됐다.
- main.py, 운영 run.yml, 테스트 workflow/코드 및 관리 문서도 SHA 차이가 있다. 전체 코드 의미 검토나 테스트는 이번 감사 범위에서 수행하지 않았다.
- 결론: 해당 브랜치를 main에 직접 통합하지 않는다. 고유 1개 커밋의 내용과 필요한 fixture만 최신 main 기준 별도 작업으로 재검토한다. 운영 데이터는 main 원본을 보존한다.
- 감사 기준: 2026-11-19T09:34:27+09:00; main 732f5167ed1a272afc10bb66d4aceb68ccb96b79, 작업 브랜치(문서 갱신 전) ca3f6ee8c917da8e2485cf75cd9c90ee7fb03a85.
