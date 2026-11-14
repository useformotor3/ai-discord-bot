# main.py 자동화 개선 상세 설계 및 테스트 계획

- 작성일: 2026-11-14
- 기준 코드: main.py @ main SHA 86a7731aad5de8d75581fc953bcea2c44adf2f2b
- 기준 workflow: .github/workflows/run.yml @ main SHA 65a8cadc8eac593f551e390698e367b1d161ecf1
- 상태: 설계 완료 / Phase A 테스트 기반 파일 추가 완료 / Phase B 코드 수정은 별도 승인 대기
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
