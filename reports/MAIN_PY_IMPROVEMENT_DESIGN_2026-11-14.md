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


## 15. 원본 테스트 fixture 및 부작용 경로 정밀 검토 — 2026-11-14

### 추가 확인 대상
- `tests/conftest.py` @ blob SHA `d55069fa82b4eb9d555033db8f8c2867ff774dd6`
- `tests/test_main_characterization.py` @ blob SHA `8019b18696bc9f1eb729feed633ecf2e32f36c04`
- `tests/test_p1_reliability.py` @ blob SHA `cff881cb0da2724f8810b88ae621909a9e23a6f9`
- `main.py` @ blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43`

### 테스트 fixture에서 확인된 검증 공백
1. `fake_subprocess_run()`은 전달된 명령의 결과와 무관하게 항상 `returncode=0`을 반환한다. `check=True`의 실패 동작도 재현하지 않는다. 따라서 Git config/add/commit/push 실패 경로를 검증하지 못한다.
2. mock Discord `fake_post()`는 항상 HTTP 204를 반환한다. timeout 인자, 429, 4xx, 5xx, 네트워크 예외, 부분 전송을 검증하지 않는다.
3. 정상 흐름 테스트는 Git 명령이 5회 호출되었는지 확인하지만 각 명령의 성공/실패 결과를 구분하지 않는다.
4. 현재 테스트는 mock 경계가 호출을 가로채는지와 일부 정상/실패 흐름을 확인하지만, 실제 네트워크 통합 또는 GitHub Actions CI의 증거는 아니다.

### main.py에서 추가로 확인한 위험
| ID | 우선순위 | 코드 근거 | 위험 및 제안 |
|---|---|---|---|
| P1-R08 | 중간 | history 각 항목이 dict인지 검사하지만 `snippet`의 타입은 확인하지 않고 이후 문자열 join에 사용 | 숫자/배열/null snippet이 포함된 legacy 항목에서 프롬프트 구성 중 TypeError 가능. 기존 데이터 표본과 호환성을 확인한 뒤 문자열 정규화 또는 명시적 검증 필요 |
| P1-R09 | 중간 | 아카이브 파일명이 날짜+시각(초 단위) | 같은 초에 두 실행이 발생하면 파일명 충돌 및 기존 보고서 덮어쓰기 가능. run_id 또는 충돌 방지 생성 필요 |
| P1-R10 | 중간 | Discord 전송 실패 예외가 아카이브 저장보다 앞에서 발생 가능 | 일부 chunk 전송 후 실패하면 Discord 부분 전송만 남고 파일/상태 저장은 실행되지 않을 수 있음. idempotency와 부분 성공 정책 필요 |
| P1-R11 | 중간 | `MAX_DAILY_QUOTA=1200` 하드코딩 | 모델/계정/정책별 실제 한도와 연결된 값인지 불명확. 공식 한도 확인 전 운영 정책값으로 단정 금지 |

### 우선순위 재평가
- P0: 원본 동일성 확인을 통과한 테스트 실행 경로 확보. 테스트 workflow를 추가하거나 기존 workflow를 수정하는 일은 별도 승인을 받기 전 금지.
- P1: Git push 실패 검증을 포함하도록 mock을 강화하고, Discord 응답/timeout 및 state/history 원자적 저장·부분 성공 처리를 별도 승인 후 구현.
- P2: snippet schema, archive collision, quota 설정, import-time 실행 구조, 출처 검증을 분리해 설계.
- 기존 history의 실제 snippet 자료형 분포와 초 단위 파일명 충돌 여부는 아직 확인하지 않았으므로 발생 사실이 아닌 잠재 위험으로 기록한다.

### 변경 및 검증 경계
- GitHub에서 원본 소스와 테스트 파일을 다시 fetch하고 blob SHA를 기록한 정적 검토다.
- 이 검토에서 실제 저장소 pytest, CI, 운영 workflow를 실행하지 않았다.
- `main.py`, tests, workflow, state/history 및 운영 main은 변경하지 않았다.


## 16. Git/Discord 실패 경로 fixture 설계 — 2026-11-14

### 현재 fixture에서 확인한 한계
- tests/conftest.py의 fake_post()는 항상 HTTP 204를 반환하고 timeout 인자를 기록하거나 검증하지 않는다.
- Discord mock 응답에는 raise_for_status(), headers, Retry-After가 없다.
- fake_subprocess_run()은 모든 명령에 returncode=0을 반환하고 check=True의 CalledProcessError 동작을 재현하지 않는다.
- 현재 fixture는 명령별 실패 순서, 재시도 횟수, 부분 전송, 단계별 결과를 관찰할 수 없다.
- main.py 자체도 Discord timeout/status 검사와 Git 실패 상태화를 하지 않으므로, 현 상태에서 실패 테스트를 추가해도 올바른 운영 동작을 검증할 수 없다.

### 제안 fixture 설계 — 테스트 전용 변경
1. Discord 응답 큐: 성공 응답, HTTP 상태, headers, requests 예외(timeout/connection error)를 순서대로 반환하도록 한다.
2. Discord 호출 기록: URL 원문은 저장하지 않고 호출 횟수, payload 길이/파트 번호, timeout 값만 기록해 webhook 비밀값 노출을 방지한다.
3. Git 명령 큐: add, commit, push를 구분해 명령별 return code 또는 예외를 지정한다.
4. check=True 동작: non-zero return code에서 실제 subprocess.CalledProcessError를 발생시킨다.
5. 테스트별 설정: 기본값은 현재와 같이 성공 mock으로 유지해 기존 characterization 테스트의 호환성을 보존한다.
6. 시간 대기: sleep mock은 호출 시간/횟수만 기록하고 실제 대기하지 않는다. 재시도 정책 테스트는 대기 함수 호출 기록으로 확인한다.

### 실패 시나리오 매트릭스

| ID | 주입 상황 | 기대 검증 |
|---|---|---|
| D01 | Discord timeout 1회 후 성공 | timeout 인자 전달, 제한 재시도, 최종 sent |
| D02 | 연결 오류 반복 | 재시도 상한, 최종 failed, 성공으로 기록하지 않음 |
| D03 | HTTP 429 + Retry-After | 헤더 기반 대기 정책, 재시도 상한 |
| D04 | HTTP 400/401/403 | 불필요한 재시도 없이 실패/설정 오류로 구분 |
| D05 | HTTP 500/502/503 | 제한 재시도 후 최종 상태 반영 |
| D06 | 여러 chunk 중 일부만 전송 성공 | 전송된 파트와 실패 파트를 구분하고 중복 재전송 위험 기록 |
| G01 | git add non-zero | commit/push 후속 명령이 실행되지 않음 |
| G02 | git commit non-zero 또는 CalledProcessError | push가 실행되지 않고 sync 실패가 명시됨 |
| G03 | git push non-zero 또는 CalledProcessError | 로컬 archive 존재와 원격 sync 실패를 분리 기록 |
| G04 | Git 명령 성공/변경 없음 | 실제 결과에 맞는 synced/no_changes 상태 |
| S01 | state 임시 파일 작성 실패 | 기존 state 원본 보존, 성공으로 표시하지 않음 |
| S02 | atomic replace 실패 | 기존 파일 보존 가능 여부와 복구 동작 검증 |
| S03 | history 저장 실패 | state/history 간 불일치 및 재실행 위험 검증 |
| L01 | 예외 메시지에 테스트용 secret 포함 | 로그·상태 기록에 secret이 노출되지 않음 |

### P1-B 최소 구현 제안 — 승인 전 미구현
- Discord: 명시적 timeout, raise_for_status() 또는 동등한 status 판정, 429/일시적 5xx/네트워크 오류만 제한 재시도, 일반 4xx 재시도 금지.
- Git: add/commit/push 단계를 구분하고 실패를 삼키지 않으며, 원격 sync 실패 상태를 실행 결과에 남긴다.
- 저장: 임시 파일에 완전한 JSON을 쓴 뒤 원자적 교체를 수행하고, 저장 실패 시 기존 파일을 보존한다.
- 부분 성공: archive 저장, Discord 전송, Git sync를 하나의 성공 boolean으로 뭉개지 않는다. 단계별 상태와 최종 partial/failed 판정 기준을 명시한다.
- 비밀정보: webhook URL, API 키, payload 원문 및 민감한 예외 문자열을 로그에 기록하지 않는다.

### 구현 경계와 승인 게이트
- 이 절은 원본 main.py와 fixture를 읽어 작성한 설계이며 코드·테스트·workflow를 수정하거나 실행한 것이 아니다.
- 테스트 fixture 변경은 별도 테스트 전용 범위로 제안한다.
- P1-B 운영 코드 변경은 별도 사용자 승인 전 금지한다.
- 승인 시에도 작업 브랜치만 수정하고 운영 main, .github/workflows/run.yml, state.json, history.json, 실제 Gemini/Discord/Git push는 건드리지 않는다.
- 승인 후 fixture 단위 검증 → 테스트 전용 Actions SHA 기준 갱신 → 전체 pytest/compileall → 실패 로그 확인 순으로 진행한다.


## 17. P1-B 전송·저장·동기화 정책 명세 — 2026-11-14 (구현 전 설계)

### 17.1 적용 범위와 설계 근거
이 절은 기존 `main.py`의 외부 부작용 순서와 Discord/Git 실패 경로 테스트를 바탕으로 작성한 설계다. **운영 코드 변경 승인이 아니며**, 구현 전 사용자 승인이 별도로 필요하다.

공식 기술 문서 교차 확인:
- Discord Rate Limits: 429 응답에서 `Retry-After` 헤더 또는 JSON `retry_after`를 읽어 대기해야 하며, 401/403/429 등의 반복 invalid request는 임시 제한 위험이 있다. 404 webhook은 재요청하지 말라는 안내가 있다. https://github.com/discord/discord-api-docs/blob/main/developers/topics/rate-limits.mdx
- Discord Execute Webhook: `wait=true`이면 서버가 메시지 전송을 확인한 후 메시지 객체를 반환한다. 기본 `wait=false`에서는 메시지가 저장되지 않아도 오류를 돌려주지 않을 수 있다. https://github.com/discord/discord-api-docs/blob/main/developers/resources/webhook.mdx
- Requests: timeout을 지정하지 않으면 요청이 무기한 대기할 수 있고, timeout은 전체 요청 wall-clock 제한이 아니라 socket read 간격 기준이다. `ConnectTimeout`은 재시도해도 안전하다고 문서화되어 있으나 `ReadTimeout`/일반 ConnectionError는 요청이 서버에 반영됐는지 불명확할 수 있다. https://docs.python-requests.org/en/latest/user/quickstart/
- Requests advanced timeout: connect/read timeout을 튜플로 분리할 수 있다. https://docs.python-requests.org/en/latest/user/advanced/

### 17.2 Discord 전송 정책 — 중복 메시지 위험 우선
현재 `requests.post()`는 timeout과 응답 확인 없이 호출되며, 메시지 POST는 네트워크 응답이 끊겼을 때 서버가 메시지를 이미 저장했는지 클라이언트가 알 수 없다. 따라서 단순 재시도는 중복 보고서를 만들 수 있다.

| 응답/오류 | 권고 동작 | 근거/주의 |
|---|---|---|
| 2xx + `wait=true` 메시지 객체 확인 | 해당 chunk를 sent로 기록하고 message ID 보존 | 서버 확인이 있는 성공 |
| HTTP 429 | `Retry-After` 또는 JSON `retry_after`를 파싱해 해당 시간 이후 제한 재시도 | Discord 공식 rate-limit 정책 |
| HTTP 400 | 영구 요청 오류로 중단, 재시도 금지 | payload/요청 수정 필요 |
| HTTP 401/403 | 즉시 중단, 설정/권한 오류로 분류, 재시도 금지 | invalid request 누적 위험 |
| HTTP 404 | 즉시 중단, webhook 설정 오류로 분류, 재시도 금지 | Discord는 404 webhook 반복 요청을 금지하도록 안내 |
| HTTP 5xx | 기본은 `delivery_unknown`으로 기록하고 자동 재시도하지 않음 | POST가 서버에 반영됐는지 불명확해 중복 전송 위험. 향후 idempotency/outbox 정책 확보 시 재검토 |
| `ConnectTimeout` | 제한 횟수 내 재시도 가능 | Requests 문서상 연결 수립 전 timeout은 재시도 안전 |
| `ReadTimeout`/일반 ConnectionError | `delivery_unknown`, 자동 재시도 보류 | 서버 수신 후 응답만 유실됐을 수 있음 |

- Timeout은 connect/read 별도 설정을 사용하고, 값은 설정 상수로 관리한다. 초기 후보값은 connect 3.05초/read 10초이며 실제 네트워크 특성 검증 후 조정한다. Requests timeout은 전체 실행시간 상한이 아님을 문서화한다.
- 429의 Retry-After가 현재 실행의 최대 대기 예산을 넘으면 더 짧은 시간으로 임의 축소해 재시도하지 않는다. `deferred`/실패 상태로 남기고 다음 실행 또는 별도 재처리로 넘긴다.
- Discord rate limit 숫자를 코드에 하드코딩하지 않고 응답 헤더/본문을 따른다.
- 429 재시도 상한, 최대 대기 예산, backoff/jitter는 설정값으로 명시하고 테스트한다.

### 17.3 Chunk/부분 전송
- 각 chunk에 `run_id`, `chunk_index`, `chunk_count`, content hash를 부여한다.
- `wait=true` 성공 응답에서 반환된 message ID를 chunk별로 기록한다.
- chunk 1..k가 확인 성공하고 k+1에서 영구 실패하면 전체 결과를 `partial`로 기록한다. 성공 chunk를 무조건 처음부터 다시 보내지 않는다.
- timeout/5xx 등 전달 여부가 불명확한 chunk는 `unknown`으로 남긴다. 중복 방지 정책 없이 자동 재전송하지 않는다.
- 현재 `state.json`/ `history.json`만으로는 chunk outbox/재처리 이력을 안전하게 보존하기 어렵다. P1-B에서 outbox 저장 구조가 필요한지 별도 결정한다.

### 17.4 Archive/state/history 저장 정책
- 보고서 archive는 임시 파일에 전체 내용을 기록하고 flush/fsync 후 atomic replace한다. 충돌 방지를 위해 run_id 또는 UUID를 파일명에 포함한다.
- `state.json`과 `history.json`은 각각 atomic replace를 해도 두 파일 사이의 원자성이 자동 보장되지 않는다.
- 두 파일 일관성을 요구한다면 transaction journal/run_id를 두고, 임시 파일 작성 → journal 기록 → 교체 → 완료 기록/정리 순서 및 시작 시 복구 절차를 설계해야 한다.
- 한 파일 교체 후 다음 파일 교체가 실패하거나 프로세스가 중단되는 경우를 테스트한다. 원본 보존 및 재시작 복구가 검증되기 전에는 저장 성공으로 표시하지 않는다.
- 운영 데이터 형식은 하위 호환을 유지하고, 기존 1,592개 history 항목을 일괄 재작성하지 않는다.

### 17.5 실행 단계 및 최종 상태
권고 순서:
1. 입력 state/history 읽기 및 검증
2. 조사 결과 생성 및 구조 검증
3. archive 및 state/history transaction 저장
4. Discord 전송(outbox 상태와 chunk 결과 기록)
5. Git add/commit/push 동기화
6. 실행 결과 요약 기록

단계별 상태를 분리한다: `research_status`, `archive_status`, `discord_status`, `git_sync_status`, `execution_status`.
- archive/state/history 필수 저장이 실패하면 `failed`.
- 필수 저장은 성공했으나 Discord 또는 Git sync가 실패/unknown이면 `partial`.
- webhook 미설정은 `skipped`로 명시하며 프로젝트 운영 정책에서 필수 채널인지에 따라 최종 상태를 결정한다.
- Git push 실패 시 이미 생성한 로컬 commit을 보존한다. 다음 실행에서 새 보고서를 만들지 말고 원격 ref를 확인해 동일 commit이 이미 반영됐는지 판정한 뒤 필요한 경우 같은 commit을 push한다.
- Git add/commit 실패 시 후속 명령을 실행하지 않는다. commit 단계에서 변경 없음은 `no_changes`로 구분한다.

### 17.6 테스트 계약의 정합성 검토 필요
초기 strict xfail의 503 자동 재시도 기대는 중복 위험과 충돌하여 테스트 계약을 수정했다. 현재 503은 `delivery_unknown` 및 자동 재전송 금지를 기대하고, 401/403/404는 `permanent_failure` 및 재시도 금지를 기대한다. 이 기대 동작들은 현행 main.py에 아직 구현되지 않았으므로 strict xfail로 남겨 CI에서 미구현 상태를 드러낸다. 429 Retry-After 처리도 구현 전 정책 테스트로 유지한다.

### 17.7 구현 전 승인 게이트
다음 구현 제안서에는 아래를 포함한다.
- 변경 전/후 `main.py` 동작 및 함수별 diff
- 신규 상태/outbox/journal 스키마와 기존 파일 하위 호환성
- Discord duplicate/unknown delivery 정책
- Git remote reconciliation 절차
- atomic write crash-recovery 테스트
- CI SHA pin 갱신, 전체 pytest, rollback 절차
- 운영 workflow/API/secret 영향 분석

**결론:** 먼저 Discord POST의 중복 가능성을 해결하는 상태 모델과 저장 일관성을 확정한다. 그 후 최소 구현 범위를 사용자에게 제안하고 별도 승인을 받는다. 이 문서 작성만으로 운영 코드나 workflow를 변경하지 않는다.
