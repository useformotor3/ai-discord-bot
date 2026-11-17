# CRA 서보 드라이브 마스터 계획서

> **활성 범위 통제(2026-11-17): 본 계획은 CRA 대응만 다룬다.** SIL 3 기능안전 자료는 과거 산출물로 보존하지만 활성 단계·완료 기준·다음 작업에 포함하지 않는다. 별도 명시적 재개 지시가 있을 때만 독립 계획으로 다룬다.

## 목표

산업용 서보 드라이브 제조사가 EU CRA에 대응할 수 있도록 적용성 분석, 보안 요구사항 추적, 하드웨어·펌웨어·개발 프로세스 설계, 검증 증거, 한국어 보고서와 매뉴얼을 하나의 추적 가능한 체계로 만든다.

## 운영 원칙

- 운영 `main.py`와 workflow는 직접 수정하지 않고, CRA 목표에 필요한 변경만 작업 브랜치·mock/전체 테스트·CI·PR·rollback ref를 갖춰 통합한다. 사용자의 상시 진행 승인 범위에서는 반복 승인 질문을 하지 않는다. 운영 workflow 실행·비가역 외부 효과는 별도 안전 확인 대상으로 둔다.
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
- 통상적인 CRA 범위 변경은 사용자의 상시 진행 승인에 따라 작업 브랜치에서 수행하고, 영향분석·테스트·복구 경로·CI를 확인한 후 PR로 통합

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
- 활성 범위는 CRA 사이버보안 요구사항만 포함한다. 기능안전/SIL 설계·검증은 활성 범위에서 제외하며 별도 명시 지시 없이는 진행하지 않는다.
- 안전 관련 변경은 영향분석 및 전문 검토 없이 확정하지 않음

### Phase 6 — 통합 문서화
- 단일 통합 보고서 + 필요한 부속서(요구사항 추적표, 시험 증거, 설계 상세, 용어집)
- 문서마다 동일한 사실을 중복 기재하지 않고 기준 문서와 상호 링크
- 변경 이력과 검토 상태 유지
- 한국어 최종 보고서, 매뉴얼, 발표자료, 표/데이터 파일 생성

## 현재 진행 상태 — 2026-11-17

- Phase 1 표본 감사 및 #28/#29 정정본 작성: 수행
- Phase 2 P0 모델 응답 검증/실패 차단: 작업 브랜치 구현 및 격리 mock 테스트 9 passed 기록
- Phase 2 P1-A state/history 검증 및 datetime 호환: 작업 브랜치 구현, helper 독립 pytest 7 passed
- Phase 3 기본 원본 테스트 실행 기반: 확보. 테스트 전용 GitHub Actions Run #1~#3 success, 최신 Run #3에서 SHA 5개 일치, compileall 통과, pytest 21 passed
- Phase 2 P1-B1 Discord 전송 및 P1-B2 atomic persistence: 작업 브랜치 구현·CI 검증 완료; P1-B3 Git sync/P1-B4 구조 개선은 미구현
- Phase 4: CRA 요구사항 추적표 v0.2(35항목) 작성. 제품별 증거·설계 통제·시험 결과 연결은 진행 중.
- 서보 드라이브 인터페이스별 CRA 적용성 매트릭스 15항목 작성. 실제 모델 회로·프로토콜·의도된 사용 검증 전 잠정.
- CRA 보안 통제·시험 매트릭스 36항목 작성, 35개 요구사항 추적 ID와 연결. 각 구현 후보는 법정 단일 구현방식이 아닌 위험기반 선택지로 표시; 제품별 시험은 미실시.
- CRA 서보 드라이브 참조 보안 아키텍처 v0.1 PR #23 병합 및 main readback 완료: 논리 블록, trust boundary, data flow, HW/FW/network control candidates. 실제 부품/회로에 맞춘 설계는 제품 자료 확보 후 진행.
- Phase 6: CRA 통합 규제·기술 준수 보고서 v0.2 보강 및 PR #21 병합 완료. 2026-07 Commission Guidance 및 2026-11 M/606 개정 반영. 제품별 판정 전.
- Phase 2/3 CRA source provenance: PR #26 병합 완료. CELLAR official source 7건 + Commission page 2건, source SHA manifest, claim/paragraph/Annex locator validator, fail-closed source gate. Run #573: 138 passed / 1 xfailed; live 9-source canary와 Article 13(8) quote 확인.

## 2026-11-17 최신 재개 지점 — CRA source provenance 통합 완료

- canonical 운영 브랜치는 `main`이다. 최신 source provenance merge commit은 `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`.
- PR #26에서 source/claim gate 선택 이식과 CELLAR official source retrieval을 완료했다. [검증 보고서](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md)를 상세 근거로 사용한다.
- PR #26 Actions Run #573: 138 passed / 1 xfailed; official source 9개 live fetch 및 Article 13(8) locator/quote canary 성공. PR head SHA는 `d1bda523c1b593bbd48bf4916dd7bbd741001894`; merge commit 자체의 별도 CI는 아직 확인되지 않았다.
- 운영 main의 history 15, retry 2, quota/429/503 no-op, duplicate-topic suppression, transactional persistence/rollback은 유지했다.
- Commission Guidance PDF/Annex 및 M/606 C(2026) 7861 decision Annex는 관련 URL만 manifest에 기록했다. 원문 다운로드·파싱은 미완료로 남긴다.
- 다음 우선순위는 PDF/decision Annex 수집, Article/Annex live locator 확대, 35 requirements/15 interfaces/36 SEC controls와 source claim 및 제품별 증거 연결이다.
- divergent branches 전체 병합 금지, force-push/history rewrite 금지. 과거 SIL 3 산출물은 역사 기록으로 보존하고 CRA 계획에 포함하지 않는다.

## 다음 실행 순서 — 2026-11-17 CRA 우선순위

1. **공식 부속문서 수집**: Commission Guidance C(2026) 5252 PDF 원문/Annex 및 M/606 결정 C(2026) 7861 Annex를 별도 수집·파싱하고 페이지 locator, source URL, retrieval time, SHA-256을 기록한다. 현재 source pack은 관련 URL만 기록하며 PDF/decision Annex 본문은 미수집이다.
2. **locator 검증 범위 확대**: Article 13(8) 외 Article 주요 paragraph, Annex I Part I/Part II point를 live source text에서 검증하는 canary와 regression test를 추가한다.
3. **요구사항·통제 추적 통합**: 35개 CRA 요구사항, 15개 인터페이스, 36개 SEC 통제/시험 항목에 source claim ID, 설계 통제, 검증 방법, 시험 결과, 증거 링크를 연결한다.
4. **제품 적용성·분류**: 실제 모델·회로·펌웨어·프로토콜·디지털 데이터 흐름·원격 처리·EU 공급 주체 자료가 확보되면 Annex III/IV core functionality 및 Article 32 경로를 검증한다. 미제공 사항은 잠정으로 유지한다.
5. **통합 보고서·매뉴얼**: 기존 v0.2 보고서와 38개 정정 보고서를 기준으로 신규 근거를 통합하고, 법적 의무·공식 해석·엔지니어링 권고·미확인 가설을 구분한다.
6. **CI/운영 관찰**: main merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`의 post-merge CI를 확인한다. 운영 Gemini/Discord 실행은 운영 모니터링 범위에서만 관찰하며 테스트 목적으로 실행하지 않는다.
7. **문서 정합성**: README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG.jsonl을 같은 사건 ID/commit 기준으로 갱신하고 JSONL·CSV·문서 링크를 재검증한다.

기능 코드나 운영 workflow 변경은 CRA 산출물에 실제 필요성이 확인된 경우에만 별도 영향분석·테스트·롤백 계획을 수립한다. 과거 P1-B3/P1-B4 계획은 현재 CRA 보고서의 선행 조건으로 취급하지 않는다.

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
## 2026-11-17 — 반복 자동화 및 조사 품질 개선

1. [완료] main의 최근 #33–#38을 EUR-Lex OJ 원문과 대조하고 원본 보존 정정 보고서 6건 추가.
2. [완료] PR #10을 main에 merge. EUR-Lex CRA 공식 링크 누락 거부, 최근 30개 원문 기반 중복 주제 차단, 프롬프트 최근 15개 이력 확대.
3. [완료] PR #10 CI Run #455: 101 passed, 1 xfailed.
4. [진행] 외부 5분 repository_dispatch를 제거하고 hourly schedule로 전환하는 PR 검증 및 병합.
5. [후속] 첫 3회 hourly production run의 checkpoint/guard/prune 및 archive 참조 무결성을 관찰.
6. [후속] 중복탐지 false positive/negative를 로그로 검토하고 임계값을 근거 기반 조정.
7. [핵심 산출물] CRA 통합 한국어 보고서 및 CRA 요구사항 추적표를 작성·검증한다. SIL 3 기능안전 자료는 과거 산출물로 보존하며 본 프로젝트의 후속 작업으로 진행하지 않는다.

## 2026-11-17 — Gemini 무료 할당량 장애 반영
1. [완료] Production Run `44016487535` 로그에서 Gemini 429 daily quota 20/day와 fallback 503 UNAVAILABLE를 확인.
2. [완료] 같은 모델의 429/503 반복 호출을 즉시 중단하고 대체 모델로 전환.
3. [완료] quota/일시 장애/품질 검증 실패 시 외부 전송·아카이브·상태 변경 없이 no-op 종료. 인증/설정 오류는 실패 유지.
4. [완료] Free Tier 일일 한도와 재시도 여유를 고려해 운영 schedule을 3시간마다(8회/일)로 조정; 모델당 최대 2회 시도 기준 최대 16회/일.
5. [진행] PR #11 isolated CI 재검증 및 병합, 이후 첫 3회 production run 관찰.
## 2026-11-17 — 운영 안정화 PR #10–#12 병합 완료

1. [완료] PR #10: EUR-Lex official-link gate + recent-30 archive duplicate-topic suppression. CI #455: 101 passed, 1 xfailed.
2. [완료] PR #11: 외부 5분 repository_dispatch 제거, 3시간 schedule, Gemini 429/503 즉시 fallback, quota/quality clean no-op. CI #467: 103 passed, 1 xfailed.
3. [완료] PR #12: 실패 후 guard always, dirty/unpublished data restore, guard 성공 후에만 checkpoint pruning, persist-before-Discord. CI #470: 105 passed, 1 xfailed.
4. [진행] 첫 3회 3-hourly production run을 관찰하고 actual quota/Discord/guard/prune 결과 확인.
5. [다음] CRA 한국어 통합 보고서와 requirements traceability matrix 작성. 법령 직접 의무와 제조사 권고 구현을 구분.
6. [다음] CRA 통합 한국어 보고서와 CRA cybersecurity 요구사항 추적표 작성·검증. 기능안전(SIL 3)은 별도 재개 지시 전 비활성.

## 2026-11-17 — CRA 자동 보관 #1–#38 원문 정정
1. [완료] CRA 정정 보고서 #1–#4 및 #33–#38 main의 기존 정정 확인.
2. [완료] #5–#21 정정 보고서를 이전 source-audit branch에서 main 통합 후보로 복사.
3. [완료] #22–#32 원본을 EUR-Lex final OJ와 대조해 11개 정정 보고서 작성.
4. [완료] #1–#38 인덱스 생성.
5. [진행] PR #14 CI 및 병합 후 정정 보고서/원본 archive SHA 무결성 확인.
6. [다음] 정정된 근거를 CRA 한국어 통합 보고서 및 requirements traceability matrix에 반영.

## 2026-11-17 — CRA correction coverage 완료
1. [완료] 자동 생성 CRA archive #1–#38 각각에 correction report #1–#38을 main에 통합.
2. [완료] master index `reports/CRA_CORRECTION_INDEX_2026-11-17.md` 작성.
3. [완료] 원본 archive SHA 보존, state/history SHA 동일성 검증.
4. [완료] PR #14 merge; CI #474 105 passed, 1 xfailed.
5. [진행] CRA 한국어 통합 보고서와 조항-제품요구-검증증거 traceability matrix 작성.
6. [다음] CRA 통합 보고서 및 CRA 요구사항 추적표를 완성하고 각 주장·조항·제품 적용성·통제·시험 증거를 교차 검증한다. SIL 3는 활성 범위에서 제외.
7. [운영] 첫 3회 3-hourly production run을 관찰하고 실제 quota/Discord/guard/prune 결과를 기록.

## 과거 산출물 기록 — SIL 3 기능안전 (비활성 범위)

아래 날짜별 기록은 과거 작업 이력 보존용이다. 활성 CRA 계획의 단계·우선순위·재개 지점으로 해석하지 않는다.

## 2026-11-17 — SIL 3 서보 드라이브 기술 산출물 v0.1
1. [완료] 제조사 4개 제품군(Mitsubishi J5, Yaskawa Sigma-7 ASM7, Rockwell Kinetix 5700, Siemens S210) 공식 자료 기반 벤치마킹.
2. [완료] 2026-11-17 현재 IEC 61800-5-2 AMD1:2026 및 IEC 62061 AMD2:2026 최신판 반영.
3. [완료] 1축 기준 하드웨어 reference block design 및 안전 기능별 구현 경로 작성.
4. [완료] FS/CYB 분리 traceability matrix 작성.
5. [진행] PR CI/병합 및 링크/수치/모델 조합 검증.
6. [다음] 정격 전압·출력·축 수·부하·엔코더·안전 기능 범위를 확정한 후 회로도/BOM/PFH 계산/시험 규격 상세화.

## 2026-11-17 — SIL 3 서보 드라이브 기술 산출물 main 반영
1. [완료] 4개 제조사 벤치마킹 보고서 v0.1.
2. [완료] 1축 하드웨어 reference block design v0.1.
3. [완료] FS/CYB 분리 요구사항 추적성 매트릭스.
4. [완료] Excel/Google Sheets에서 열 수 있는 CSV 비교표.
5. [완료] PR #16 merge `34449753857c6ab004271f69aac19867a7aed1fa`, CI #488 105 passed, 1 xfailed.
6. [진행] 정격/부하/피드백/안전 기능 범위 확정 후 schematic, component selection/BOM, thermal/EMC, FMEDA/PFH calculation.
7. [운영] 3시간 주기 첫 3회 production run 관찰.


## 2026-11-17 — CRA source provenance pipeline 완료

- PR #26 merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`.
- CELLAR official source 7건, Commission official page 2건을 allowlist 기반으로 수집하고, 전체 visible text/prompt excerpt SHA-256과 retrieval metadata를 manifest에 남긴다.
- Claim ID, 본문 statement, source ID, exact quote, Article paragraph/Annex Part-point locator 검증을 추가했다.
- Run #573: 138 passed / 1 xfailed, 9개 live source fetch, Article 13(8) locator/quote canary 성공.
- 상세: [CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md).
- 제한: Guidance PDF/Annex와 M/606 decision Annex 미수집; 제품별 적용성/설계/시험 증거 미확정; merge commit 자체의 별도 CI는 미확인.


## 2026-11-17 — CRA source provenance 관리 문서 동기화 완료

- PR #27 merge commit: `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`.
- README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG.jsonl 및 source provenance 상세 보고서를 PR #26 검증 결과에 맞춰 동기화했다.
- PR #27 Run #575: 138 passed / 1 xfailed, 9개 live official source 및 Article 13(8) locator/quote canary 재통과.
- PR #27 pre/post merge safety refs는 각각 `safety/pre-merge-main-pr27-2026-11-17` 및 `safety/post-merge-main-pr27-2026-11-17`; 두 ref의 SHA readback 검증 완료.
- merge commit 자체의 별도 Actions run은 확인되지 않았으므로 PR head CI 결과만 기록한다.
