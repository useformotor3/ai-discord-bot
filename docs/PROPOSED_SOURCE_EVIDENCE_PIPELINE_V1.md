# CRA Source Evidence Pipeline v1 — Design Proposal

- 작성일: 2026-11-13
- 상태: DESIGN_ONLY — 구현 승인 대기
- 대상 브랜치: `cra-project-foundation`
- 범위: 공식 원문 수집, 출처 무결성, 인용·조항 위치 자동 대조
- 금지: `main.py`, Gemini prompt, validator, workflow, model order, quota, production flow 변경 전 별도 명시 승인 필요
- 비용: 유료 API, Google Search grounding, 유료 검색 서비스 사용 안 함

## 1. 현재 상태와 근거

1차 Gemini 계약 구현은 mock test와 GitHub Actions에서 통과했다. 최신 검증 실행:
- Workflow run: [#43205954271](https://github.com/useformotor3/ai-discord-bot/actions/runs/43205954271)
- Commit: `aabffb6022f328caf24df58e9fa551da9b69a4d7`
- 전체 Python 테스트: 26 PASS, 0 FAIL, 0 ERROR
- 이 중 CRA report contract 테스트: 17 PASS
- Archive consistency: archive 990 / history 990, missing/orphan/duplicate paths 0

다만 현재 production prompt에는 별도 원문 수집이 없고, 모든 claim이 UNVERIFIED로 고정된다. 이는 의도한 안전한 1차 제한이다.

## 2. 목표

모델이 스스로 출처 URL·문서 버전·직접 인용·조항 위치를 만들어내지 못하도록, 모델 호출 전에 공식 출처를 수집하고 그 결과만 근거로 전달한다. 모델은 수집된 source_id를 참조할 뿐 임의 URL을 직접 fetch할 수 없다.

## 3. 제안 아키텍처

```text
Curated Official Source Registry
        |
        v
Allowlisted Source Fetcher
        |
        +--> HTTP / MIME / size / redirect checks
        |
        v
Source Metadata + SHA-256 + Retrieved Text
        |
        v
Section / Clause Locator
        |
        v
Bounded Evidence Bundle (source_id + short excerpts)
        |
        v
Gemini Structured JSON Claims
        |
        v
Deterministic Evidence Validator
        |
        +--> exact quote substring match
        +--> source_id exists in bundle
        +--> URL/title/version from registry, not model
        +--> legal locator match where structured source supports it
        |
        v
UNVERIFIED / SOURCE_MATCHED / REVIEW_REQUIRED
        |
        v
Human legal + product applicability review
```

## 4. 공식 출처 수집 원칙

### 4.1 Source Registry 우선
- 사람이 검토한 고정 source registry만 fetch한다.
- CRA 법령은 EUR-Lex CELEX 32024R2847 공식 HTML/XML을 우선한다.
- 제조사 문서는 ST.com / TI.com의 공식 product/document pages만 사용한다.
- 모델이 출력한 URL은 fetcher 입력으로 절대 사용하지 않는다.
- 검색엔진/Google Search grounding/외부 유료 API는 사용하지 않는다. registry에 없는 새 출처는 사람 검토 후 등록한다.

### 4.2 네트워크 안전장치
- HTTPS만 허용.
- 정확한 hostname allowlist 적용.
- redirect가 다른 hostname으로 이동하면 차단.
- 연결/읽기 timeout, 응답 byte cap, MIME allowlist 적용.
- private/loopback/link-local IP, credential URL, non-HTTPS URL 거부.
- 응답 실패·HTML 오류 페이지·예상과 다른 MIME은 출처로 채택하지 않는다.
- 모델이 제안한 임의 URL로 인한 SSRF를 구조적으로 차단한다.

### 4.3 출처 메타데이터
각 수집 결과에 다음을 기록한다.
- source_id, canonical URL, publisher, title, document identifier
- revision/version, publication/revision date (공식 원문에서 읽을 수 있는 경우만)
- fetched_at UTC, HTTP status, MIME, byte count
- SHA-256 of fetched bytes, extraction method/version
- section locator candidates, extracted text hash
- status: FETCHED / FETCH_FAILED / METADATA_INCOMPLETE / PARSE_FAILED

메타데이터가 없으면 빈 값과 UNVERIFIED를 유지하며 추정하지 않는다.

## 5. 증거 번들 및 저작권 처리

- 모델에 전달하는 것은 source_id, 공식 출처 메타데이터, 필요한 조항 주변의 제한된 발췌뿐이다.
- 출처당 저장·출력하는 직접 인용은 25단어 이하를 기본 상한으로 한다.
- 제조사 PDF 원본 전체를 공개 GitHub 저장소에 재배포하지 않는다.
- 원본 전체는 실행 중 메모리에서 처리하고, 저장소에는 URL, SHA-256, 메타데이터, 짧은 발췌, locator, 검증 결과만 보존한다.
- 재현성에 필요한 원문 해시와 추출기 버전을 기록한다. 동일 URL에서 문서 내용이 바뀌면 새 evidence version으로 취급한다.

## 6. Claim schema v3 제안

현재 v2는 source_excerpt를 빈 문자열로 강제한다. v3에서는 다음 필드를 추가하는 안을 검토한다.
- source_ids: registry/bundle에 실제 존재하는 ID 목록
- evidence_excerpt: bundle 안에 실제 존재하는 짧은 구절
- excerpt_type: VERBATIM_FROM_SOURCE / PARAPHRASE / NONE
- quote_match_status: MATCHED / NOT_MATCHED / NOT_APPLICABLE
- legal_locator_match: MATCHED / NOT_MATCHED / UNVERIFIED
- source_metadata_status: COMPLETE / INCOMPLETE
- interpretation_review_status: REVIEW_REQUIRED / HUMAN_REVIEWED
- product_applicability: 계속 UNVERIFIED 기본값; exact SKU와 공식 product evidence 및 별도 검토 전 자동 확정 금지

검증기는 source_id의 실재 여부, excerpt의 정확한 substring 포함 여부, 출처당 발췌 길이, 메타데이터 provenance를 결정적으로 검사한다. URL, title, publisher, version은 모델 출력이 아니라 source registry의 값을 renderer가 가져온다.

## 7. 상태 모델 — 자동 VERIFIED 금지

| 상태 | 의미 |
|---|---|
| FETCHED | 공식 URL에서 응답 수신 |
| SOURCE_MATCHED | 출처 ID/메타데이터가 registry와 일치 |
| QUOTE_MATCHED | 발췌가 수집 원문 텍스트와 정확히 일치 |
| LEGAL_LOCATOR_MATCHED | 구조화된 법령 locator가 원문 구조와 일치 |
| REVIEW_REQUIRED | 법률 해석 또는 제품 적용성의 사람 검토 필요 |
| HUMAN_REVIEWED | 검토자, 날짜, 범위, 결정 근거가 기록된 경우 |

출처/인용/조항 일치는 법률 해석의 정확성이나 제품 적합성을 의미하지 않는다. AI가 overall VERIFIED를 선언할 수 없게 유지한다. 사람 검토도 대상 claim과 제품 범위에 한정해 기록한다.

## 8. 테스트 계획

Mock-only tests:
1. HTTPS allowlist 통과 / HTTP 차단
2. redirect to untrusted host 차단
3. private/loopback IP 및 credential URL 차단
4. timeout / 4xx / 5xx / HTML error page 처리
5. byte cap 및 MIME mismatch 처리
6. canonical URL과 SHA-256 안정성
7. 문서 revision 변경 시 evidence version 분리
8. exact quote match / mismatch
9. source_id 위조 및 bundle 외 ID 거부
10. excerpt length cap
11. legal locator match / mismatch
12. URL/title/version을 model value로 덮어쓰기 불가
13. missing SKU이면 product applicability UNVERIFIED 유지
14. 모델이 VERIFIED를 출력해도 거부
15. source fetch failure가 검증 성공으로 기록되지 않음

CI는 실제 외부 API나 Gemini 호출 없이 fixture를 사용한다. 별도 HTTP fetch smoke test는 공개 공식 URL에 한정하고, 운영 API 호출과 분리한다.

## 9. 단계별 구현안

- Phase A — Source registry + allowlisted fetcher + metadata/hash, mock tests.
- Phase B — EUR-Lex structured locator 및 제조사 HTML/PDF extraction adapter.
- Phase C — evidence bundle 생성 및 schema v3 / prompt v3 연결.
- Phase D — exact quote/source_id/locator validator + review status renderer.
- Phase E — 실제 공식 URL의 저비용·저빈도 read-only fetch 검증. 네트워크 요청·외부 실행은 별도 승인 후 수행.

각 phase는 독립 diff, 테스트, rollback 계획으로 나눈다. Phase A부터 구현하더라도 main branch 및 production workflow에는 별도 승인 전 반영하지 않는다.

## 10. 미결정 사항 / 위험

- ST MCU 정확한 주문 코드가 없어 STM32 일반 보안 문서를 특정 MCU 기능으로 전이할 수 없다.
- TI MSPM0G3529-Q1은 정확한 SKU가 알려져 있지만, 각 문서의 revision과 해당 SKU 적용 범위를 개별 대조해야 한다.
- EUR-Lex HTML/XML의 실제 구조와 PDF extraction adapter는 구현 전 fixture로 확인해야 한다.
- URL 접근 가능성은 법률 주장의 정확성 검증이 아니다.
- 문서 변경 감지, cache TTL, 재수집 정책은 운영 비용/속도/재현성 trade-off가 있다.
- source retrieval 실패 시 UNVERIFIED draft를 생성할지, 해당 claim만 보류할지, 전체 run을 실패시킬지 정책 결정을 구현 전 승인받는다.

## 11. 공식 기술 문서 참조

- Google Gen AI Python SDK — JSON Schema structured output:
  https://googleapis.github.io/python-genai/
- Gemini API models:
  https://ai.google.dev/gemini-api/docs/models
- Gemini API model deprecations:
  https://ai.google.dev/gemini-api/docs/deprecations
- EUR-Lex CRA Regulation (EU) 2024/2847:
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

## 12. 승인 경계

현재는 설계 문서만 작성한다. 다음 변경은 사용자에게 구체적 diff와 영향·위험·테스트·rollback을 제시한 뒤 별도 승인을 받아야 한다.
- source registry / fetcher / PDF/HTML extraction code
- schema v3, validator, prompt v3
- `main.py` production call order
- any workflow or dependency changes
- any real external fetch or Gemini API execution
- model IDs/order, quota, archive/history/state schema
