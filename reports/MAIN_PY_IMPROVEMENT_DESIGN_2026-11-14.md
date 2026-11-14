# main.py 자동화 개선 상세 설계 및 테스트 계획

- 작성일: 2026-11-14
- 기준 코드: main.py @ main SHA 86a7731aad5de8d75581fc953bcea2c44adf2f2b
- 기준 workflow: .github/workflows/run.yml @ main SHA 65a8cadc8eac593f551e390698e367b1d161ecf1
- 상태: Phase A 테스트 기반 구축 완료 / Phase B P0 수정 및 mock 테스트 완료 / P1 개선은 후속 단계
- 변경 제한: 이 문서는 설계 문서이며 main.py, workflow, state.json, history.json을 변경하지 않는다.

## 1. 설계 목표

자동 조사 파이프라인을 아래 상태가 명확한 단계형 처리로 전환한다.

1. 실행 환경·상태파일 검증
2. 조사 주제 선택 및 중복 확인
3. AI 초안 생성
4. 응답 구조·출처 형식 검증
5. 법령/공식 출처 원문 대조 상태 확인
6. 보고서 생성 및 아카이브
7. Discord 전송
8. GitHub 저장
9. 최종 실행 요약과 상태 기록

'프로그램이 끝까지 실행됨'과 '조사 내용이 정확함'을 절대로 같은 성공 상태로 취급하지 않는다.

## 2. 현행 코드의 구체적 위험

| ID | 심각도 | 위치/동작 | 위험 |
|---|---|---|---|
| BUG-01 | P0 | 모델 전부 실패 후 success=True | 오류 메시지가 정상 보고서로 전송·보관됨 |
| BUG-02 | P0 | 응답이 response.text만 존재하면 승인 | 빈약한 오류 문구/형식 불량 결과가 조사로 통과 |
| BUG-03 | P1 | state.json 읽기 실패 시 count=0 기본값 | 손상된 상태파일이 쿼터 초기화처럼 처리될 수 있음 |
| BUG-04 | P1 | datetime.fromisoformat 오류 미처리 | last_health_check 값 손상 시 전체 실행 중단 |
| BUG-05 | P1 | requests.post에 timeout 없음 | 네트워크가 응답하지 않으면 workflow가 장시간 멈출 수 있음 |
| BUG-06 | P1 | HTTP status/응답 검사 없음 | Discord 전송 거부·실패를 성공처럼 진행 |
| BUG-07 | P1 | Git push 실패가 경고 출력 후 종료 | 아카이브가 원격에 저장되지 않아도 실행 성공처럼 보임 |
| BUG-08 | P1 | history 최신 5개 snippet만 사용 | 반복 주제, 조항 누락, 정정 필요 주제를 식별하기 어려움 |
| BUG-09 | P1 | 공식 출처 URL과 조항을 구조화하지 않음 | 인용·법령 근거 검증을 자동화할 수 없음 |
| BUG-10 | P2 | 예외 처리에서 예외 원인·단계가 구조화되지 않음 | 장애 분석과 재현이 어려움 |
| BUG-11 | P2 | 실행·조사·전송·저장 상태가 단일 success에 종속 | 부분 성공 및 재시도 정책을 설계하기 어려움 |
| BUG-12 | P2 | 의존성 버전을 고정하지 않음 | 동일 코드가 다른 시점에 다른 라이브러리 동작을 보일 수 있음 |

## 3. 목표 아키텍처

### 3.1 상태 모델

각 실행은 다음 필드를 갖는 실행 결과 객체를 사용한다.

- run_id
- started_at / finished_at
- execution_status: success | partial | failed | skipped
- research_status: generated | invalid | failed
- source_verification_status: verified | partial | unverified | failed
- discord_status: sent | failed | skipped
- archive_status: saved | failed | skipped
- git_sync_status: pushed | failed | no_changes | skipped
- model_used
- retry_count
- topic_id / related_topics
- errors[]: stage, error_type, message, retryable

성공 판정:
- execution_status=success는 필수 단계가 완료되었음을 뜻한다.
- research_status=generated는 구조 검증을 통과한 초안이 있음을 뜻하며 정확성 보증이 아니다.
- source_verification_status=verified는 요구된 원문 검증 증거가 확보되었을 때만 사용한다.
- 출처를 확인하지 못한 결과를 verified로 승격하지 않는다.
- 모델 전부 실패는 execution_status=failed 및 research_status=failed다.

### 3.2 모듈 분리

초기 리팩터링은 외부 동작을 바꾸지 않는 범위에서 다음 함수로 분리한다.

- load_state(path, today) — 상태 로드·스키마 검사
- load_history(path) — 이력 로드·오류 보고
- select_topic(history, coverage_index) — 신규/보완/정정 주제 구분
- build_prompt(context, topic) — 조사 프롬프트 생성
- generate_research(client, models, prompt) — 모델 폴백 및 재시도
- validate_report(text) — 필수 섹션·길이·오류문구 검사
- extract_sources(text) — URL·규정 조항 후보 추출
- verify_sources(source_records) — 공식 원문 확인 결과 기록
- send_discord(text, webhook) — 분할·timeout·HTTP 검증·재시도
- save_archive(report, metadata) — 원자적 파일 저장
- sync_git(paths) — 변경 감지·commit·push
- write_run_summary(result) — 단계별 상태 기록

첫 구현에서 불필요한 프레임워크를 도입하지 않는다. Python 표준 라이브러리와 현재 google-genai/requests를 우선 사용한다.

## 4. 실패 및 재시도 정책

| 단계 | 재시도 | 실패 시 동작 |
|---|---|---|
| 상태파일 읽기 | 자동 초기화 금지 | 명시적 오류로 종료, 원본 보존 |
| Gemini 호출 | 일시적 오류만 제한 재시도 | 모든 모델 실패 시 failed 종료 |
| 응답 검증 | 모델 재생성 1회 선택 가능 | invalid 표시, 정상 보고서로 보관 금지 |
| 출처 확인 | 제한 재시도 | 미확인으로 표시, verified 금지 |
| Discord | 네트워크/429/5xx만 제한 재시도 | discord_status=failed |
| 아카이브 | 임시 파일 작성 후 원자적 교체 | archive_status=failed |
| Git push | 제한 재시도 | git_sync_status=failed, 실행 결과에 명시 |

- 4xx 오류는 무조건 재시도하지 않는다. 429와 명확히 일시적인 경우만 별도 처리한다.
- Retry-After가 있으면 이를 우선한다.
- 재시도는 지수형 backoff와 상한을 둔다.
- 비밀키·Webhook URL·민감한 응답 본문은 로그에 남기지 않는다.
- 부분 성공을 숨기지 않는다.

## 5. 출처 검증 데이터 구조

각 주장 단위로 다음 정보를 남긴다.

- claim_id
- claim_text
- legal_classification: legal_obligation | standard_requirement | official_guidance | engineering_recommendation | unverified
- source_title
- source_url
- source_publisher
- document_identifier
- article_reference
- raw_quote
- checked_at
- verification_status
- applicability_assumptions
- reviewer_note

원문에 접근하지 못했거나 조항과 인용이 맞지 않으면 verification_status=unverified 또는 failed로 남긴다. AI가 생성한 문장을 원문 인용으로 둔갑시키지 않는다.

초기 구현에서 자동 검증이 가능한 범위는 URL 형식, 공식 도메인 allowlist, 조항 식별자, 인용 필드 유무까지다. 실제 법령 문장과 의미의 일치 여부는 공식 원문을 열어 확인해야 하며 단순 문자열 검사만으로 verified를 부여하지 않는다.

## 6. 중복 및 정정 추적

history.json의 기존 필드는 하위 호환을 유지한다. 새 필드를 추가할 때 기존 항목을 일괄 재작성하지 않는다.

추가할 메타데이터:
- topic_id
- legal_references[]
- report_type: new_research | update | correction
- related_report_files[]
- coverage_status

동일 topic_id가 최근 이력에 있으면 신규 조사 대신 다음 중 하나를 선택한다.
- 신규 공식 자료가 발견됨: update
- 기존 조항/인용 오류가 발견됨: correction
- 새로운 내용이 없음: 다른 미커버 주제 선택

기존 1,592개 이력은 무리하게 전부 재분류하지 않는다. 먼저 최근 구간을 인덱싱하고 점진적으로 확장한다.

## 7. 상태파일·쿼터·시간 처리

- state.json 기존 date/count/last_health_check를 읽을 수 있어야 한다.
- 스키마 오류와 JSON 파싱 오류를 구분한다.
- 손상된 상태파일을 조용히 초기화하지 않는다.
- 날짜·시간은 timezone-aware UTC 또는 명시된 운영 시간대로 일관되게 저장한다.
- 현재 파일의 naive datetime과 기존 값은 호환 변환을 거친다.
- 쿼터 초과는 skipped이며 정상 조사 성공이 아니다.
- health check는 조사 실행과 별개 상태로 기록한다.
- 현재 1,200회 쿼터 값은 무료 티어 공식 한도라고 단정하지 않는다. 모델별 실제 quota/가격 정책을 확인한 후 설정한다.

## 8. 테스트 설계

네트워크·Gemini·Discord·Git 명령은 mock 처리한다. CI 테스트에서 실제 외부 서비스 호출이나 실제 저장소 push가 일어나면 안 된다.

| 테스트 ID | 시나리오 | 기대 결과 |
|---|---|---|
| T01 | 정상 모델 응답 | research generated |
| T02 | 첫 모델 실패, 두 번째 성공 | fallback 성공, retry 기록 |
| T03 | 모든 모델 실패 | failed, 정상 보고서 미생성 |
| T04 | 빈 응답/공백 응답 | invalid |
| T05 | 오류 경고 문자열만 응답 | invalid |
| T06 | 필수 섹션 누락 | invalid 또는 partial |
| T07 | 출처 URL 누락 | unverified |
| T08 | 공식 출처가 아닌 URL | unverified/flagged |
| T09 | 조항 인용과 claim 불일치 | unverified, 사람 검토 필요 |
| T10 | state.json 손상 | 원본 보존, 안전 실패 |
| T11 | last_health_check 날짜 오류 | 명시적 오류 또는 안전한 복구 경로 |
| T12 | quota 도달 | skipped, count 오증가 없음 |
| T13 | Discord timeout | 제한 재시도 후 failed |
| T14 | Discord 429 + Retry-After | 지정 시간 정책 적용 |
| T15 | Discord 400 | 무의미한 재시도 없이 failed |
| T16 | Discord 500 | 제한 재시도 |
| T17 | 아카이브 저장 실패 | archive failed, success 금지 |
| T18 | Git push 실패 | git_sync failed로 표시 |
| T19 | 변경사항 없음 | no_changes |
| T20 | 중복 topic_id | update/correction/skip 중 하나 |
| T21 | 구형 history 항목 | 하위 호환 로드 |
| T22 | 비밀키 예외 발생 | 로그에 secret 미노출 |
| T23 | 전체 파이프라인 정상 | 단계별 상태 success |
| T24 | 부분 성공 조합 | partial로 기록, 숨김 금지 |

## 9. CI 개선 제안

별도 테스트가 추가된 후 workflow에 다음을 순서대로 추가한다.

1. Python 버전 고정
2. 의존성 버전 고정 또는 lock 파일 도입
3. pip install
4. compileall
5. pytest
6. mock 통합 테스트
7. 테스트 통과 후에만 운영 main.py 실행

초기에는 workflow를 변경하지 않는다. 로컬/mock 테스트가 안정화된 뒤 별도 승인으로 workflow 변경을 제안한다. 운영 실행과 테스트 job은 분리하는 것이 바람직하다.

## 10. 구현 순서 및 위험 관리

### Phase A — 안전한 테스트 기반
- 테스트 디렉터리와 mock fixture 추가
- 순수 함수 분리
- 기존 정상 동작을 characterization test로 기록
- 운영 main.py 실행/외부 호출 금지

### Phase B — P0 실패 처리
- 모든 모델 실패 시 실패 반환
- 빈 응답/오류 문구 차단
- 상태 파일의 조용한 초기화 금지
- 단위 테스트 통과

### Phase C — 전송·저장 신뢰성
- Discord timeout/status/retry
- 아카이브 원자적 저장
- Git sync 상태 분리
- 부분 성공 보고

### Phase D — 조사 품질
- 출처 메타데이터
- 법령/표준/권고 분류
- 주제 중복 및 정정 추적
- 사람 검토 게이트

### Phase E — CI
- workflow test 단계
- mock 통합 테스트
- 운영 실행 분리
- 전체 CI 검증

각 Phase는 변경 전 diff, 테스트 계획, 롤백 방법을 제시하고 승인받는다. 한 번에 전면 재작성하지 않는다.

## 11. 승인 요청 범위

다음 단계로 승인받고자 하는 작업은 **Phase A만**이다.
- 작업 브랜치에서 테스트 구조와 mock만 추가한다.
- main.py 및 workflow는 수정하지 않는다.
- 테스트는 운영 API, Discord, Git push를 호출하지 않는다.
- 테스트 결과와 변경 diff를 제시한 뒤 Phase B 승인을 별도로 요청한다.

이 설계 문서는 사용자 승인을 대신하지 않는다.


## 12. Phase A 실행 기록 (2026-11-14)

- 사용자 승인 후 작업 브랜치에 mock 기반 테스트 파일 4개를 추가했다.
- Gemini SDK, Discord HTTP, Git subprocess, sleep을 mock 처리한다.
- 운영 `main.py`, workflow, `state.json`, `history.json`은 변경하지 않았다.
- 격리된 로컬 검증: compileall 통과, 전체 pytest suite 5 passed. 브랜치에서 조회한 `main.py` 원문을 격리 작업공간에 반영해 실행했으며 실제 API/Discord/Git은 mock 처리했다.
- 이 검증은 격리된 mock 테스트이며 GitHub Actions/운영 workflow 실행을 의미하지 않는다.
- 다음 단계: 실제 저장소 checkout 환경에서 characterization suite를 실행하고, 이후 Phase B 구현은 별도 승인받는다.


## 13. Phase B P0 수정 실행 기록 (2026-11-14)

### 수정 내용
- `validate_research_report()`를 추가해 응답이 문자열인지, 250자 이상인지, 프롬프트가 요구한 4개 필수 항목을 포함하는지 확인한다.
- 대표적인 모델 오류·쿼터·서비스 장애 문구를 거부한다.
- 빈 응답/무효 응답은 재시도하고 모델 폴백을 계속한다.
- 모든 모델이 실패하면 `SystemExit(1)`로 종료한다. 이 종료는 Discord 전송, 아카이브 저장, state/history 변경, Git 동기화보다 앞서 실행된다.

### 검증
- 격리 mock 테스트에서 compileall 통과, pytest 9 passed.
- 테스트는 정상 생성, 모델 폴백, 전 모델 실패, 무효 응답, 오류 문구가 섞인 응답, 기존 state/history 보존 및 외부 호출 mock을 포함한다.
- 실제 Gemini/Discord/Git 호출과 GitHub Actions CI는 실행하지 않았다.

### 한계 및 잔여 위험
- 최소 구조 검사는 법령 원문과 출처 URL의 진위·조항 적합성까지 보증하지 않는다.
- 250자/섹션 기준은 형식적 1차 필터이며 심층 내용 품질 검증은 아니다.
- state/history 손상 처리, datetime parsing, Discord timeout/status, Git push 상태화 등 P1 항목은 미수정이다.
- workflow, state.json, history.json은 변경하지 않았다.


## 14. P1-A 반영 코드 정적 재검토 — 2026-11-14

### 검토 대상 및 방법
- GitHub 작업 브랜치에서 조회한 `main.py` 원문(조회 blob SHA: `470ac101d5cc4fdb2c5077d5468ef00327af3d43`)과 테스트 모듈을 정적 검토했다.
- 이 검토는 코드 경로·예외 처리·부작용 순서를 읽어 확인한 것이며, 원본 파일과 동일성이 입증된 전체 실행 테스트가 아니다.
- 임시 재구성 사본의 21 passed는 원본 blob SHA 불일치로 예비 검증으로만 분류한다.

### 확인된 개선점
- state/history 파일을 외부 API 호출 전에 읽고 JSON 및 최상위 구조를 검사한다.
- 손상된 파일을 빈 데이터로 덮어쓰지 않고 종료한다.
- state count의 bool/음수/비정수 값을 거부한다.
- aware datetime을 현재 시스템 로컬 시각의 naive datetime으로 변환해 기존 NOW 비교와 맞춘다.
- 모든 모델 실패 시 Discord·아카이브·상태 갱신·Git 명령보다 먼저 비정상 종료한다.

### 남은 위험 — 코드에서 확인
| ID | 우선순위 | 관찰 | 위험 및 후속 조치 |
|---|---|---|---|
| P1-R01 | 높음 | Discord `requests.post`에 timeout이 없고 응답 status/본문을 확인하지 않음 | 네트워크 hang 및 HTTP 실패를 성공처럼 취급할 수 있음. timeout, 429/5xx 제한 재시도, 4xx 정책, 응답 검증 필요 |
| P1-R02 | 높음 | Discord 전송이 아카이브/상태 저장보다 먼저 수행됨 | Discord 전송 후 파일 저장이 실패하면 외부 알림만 남는 부분 성공 발생. 단계별 상태와 재실행 정책 필요 |
| P1-R03 | 높음 | state/history를 목적 파일에 직접 write함 | 프로세스 중단/디스크 오류 시 JSON이 잘리거나 손상될 수 있음. 임시 파일+flush/fsync+atomic replace 검토 |
| P1-R04 | 높음 | Git commit/push 예외를 출력만 하고 삼킴 | 원격 동기화가 실패해도 프로세스 종료 코드는 성공으로 남을 수 있음. sync 상태 분리와 실패 반환 필요 |
| P1-R05 | 중간 | Webhook이 비어 있으면 Discord 전송 함수를 조용히 건너뜀 | 전송 생략이 의도된 것인지 실행 결과에서 식별되지 않음. skipped 상태 명시 필요 |
| P1-R06 | 중간 | 보고서 검증은 길이·섹션·일부 오류 문구에 한정됨 | URL 실재성, 공식 도메인, 조항 번호, 원문 인용 일치, 제품 적용성은 검증하지 않음. 형식 통과를 법적 정확성으로 해석하면 안 됨 |
| P1-R07 | 중간 | 코드가 모듈 import 시점에 전체 파이프라인을 실행함 | 테스트와 재사용이 runpy/모킹에 의존하고 단위 테스트 범위가 제한됨. 단계별 함수와 main guard 분리는 별도 리팩터링 검토 대상 |

### 우선순위 판단
1. 원본 소스의 blob 동일성이 확보된 테스트 실행 환경을 먼저 해결한다.
2. 그 후 P1-R01~R04의 전송·저장·동기화 부분 성공과 데이터 손상 위험을 우선 처리한다.
3. P1-R05~R07 및 출처 검증 구조는 후속 개선으로 분리한다.
4. P1-B 구현과 workflow 변경은 별도 사용자 승인 전까지 수행하지 않는다.

### 변경 범위
- 이번 절은 정적 코드 리뷰 기록만 추가했다.
- `main.py`, workflow, `state.json`, `history.json`, 운영 `main`은 수정하지 않았다.
- 실제 Gemini/Discord/Git push 및 운영 workflow는 실행하지 않았다.
