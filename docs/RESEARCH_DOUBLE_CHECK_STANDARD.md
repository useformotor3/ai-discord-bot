# CRA 조사 자료 이중 검증 표준

- 문서 ID: CRA-RESEARCH-DOUBLE-CHECK-001
- 버전: 1.0
- 적용: 모든 CRA 법령 조사, 제조사 기술자료, 제품 적용성 판단, HW/FW 설계 근거, 시험 기준 및 최종 보고서
- 상태: **필수 작업 규칙**

## 1. 절대 원칙

AI가 검색·요약·인용한 사실은 그 자체로 근거가 아니다. 원문과 독립적으로 대조하기 전에는 VERIFIED로 표시하지 않는다. 링크가 열리는 것만으로 문서의 정확성·개정판·인용·주장 지지가 검증된 것이 아니다.

## 2. 모든 자료에 필요한 2단계 확인

### 1차 — 원출처 검증
1. 발행기관의 공식 URL인지 확인한다.
2. 문서명, 문서번호, 제품 주문 코드(해당 시), revision, 발행/개정일을 원문 표지·메타데이터에서 확인한다.
3. 인용은 원문에서 다시 찾아 페이지/조항/문단/표 번호를 기록한다.
4. 문맥 앞뒤, 정의, 예외, 적용 조건, 개정 이력을 확인한다.
5. 수집 원문 SHA-256과 추출문 SHA-256 및 추출기 버전을 보존한다.
6. PDF는 중요 인용·표·도면의 실제 페이지 이미지를 사람이 시각 대조한다.

### 2차 — 독립 교차검증
1. 동일한 주장에 대해 다른 공식 근거를 찾는다. 예: EUR-Lex 조문과 Commission 공식 안내, 제조사 데이터시트와 reference manual/errata.
2. 별도 근거가 동일한 의미·조건을 지지하는지 확인한다.
3. 독립 근거가 없거나 상충하면 PARTIALLY_VERIFIED, CONFLICT, UNVERIFIED 중 적절한 상태로 남긴다.
4. 모델이 만든 문장·다른 AI 요약·검색 snippet을 독립 근거로 계산하지 않는다.
5. 안전·보안·법적 의무의 적용 결론은 원문 인용과 제품 사실을 각각 별도 확인한다.

## 3. 검증 상태

| 상태 | 의미 | 보고서 사용 |
|---|---|---|
| VERIFIED | 공식 원문, 정확한 위치, revision, 의미, 독립 교차검증까지 통과 | 근거로 사용 가능 |
| PARTIALLY_VERIFIED | 원문 일부 확인됐으나 독립 교차 또는 적용 조건 미완료 | 제한·미확인 명시 후 사용 |
| CONFLICT | 원문/개정판/공식 근거 간 충돌 또는 기존 인용 오류 | 결론 근거로 사용 금지 |
| UNVERIFIED | 공식 원문 또는 정확한 위치/판본 확인 불가 | 결론 근거로 사용 금지 |
| NOT_APPLICABLE | 해당 제품·구성·시장 범위에 적용되지 않음이 근거로 확인 | 적용 제외 사유 기록 |
| NOT_RUN | 시험·검증을 실행하지 않음 | 시험 통과 표현 금지 |

IDENTITY_AND_REVISION_MATCHED는 bundle 내부의 텍스트 문자열 일치만 의미한다. 이것은 위 표의 VERIFIED가 아니며 발행자 진위·원문 충실도·법적 의미를 인증하지 않는다.

## 4. 자료 유형별 교차검증

- EU 법령: EUR-Lex 현행 법령 원문을 기준으로 조문·항·호를 확인한다. Commission FAQ/안내는 보조 해석 자료이며 법령 원문을 대체하지 않는다. 위임·시행법령, 정오표, 개정 및 적용일을 확인한다.
- ST/TI 기술문서: 정확한 문서번호·revision·제품 주문 코드를 확인한다. 다른 MCU family 또는 다른 revision의 기능을 전용하지 않는다. 데이터시트, TRM, safety manual, errata 간 차이를 기록한다.
- 제품 적용성: 실제 제품 intended purpose, SKU/order code, 네트워크 기능, safety architecture, 판매 형태, 시장을 확인한다. 일반 MCU 기능만으로 제품 기능이나 CRA 분류를 추정하지 않는다.
- SIL/기능안전: IEC 61508, ISO 26262 및 제조사 component safety concept를 서로 자동 등가 처리하지 않는다. component-level claim과 complete system claim을 분리한다.

## 5. 보고서 생성 게이트

1. 각 claim은 하나 이상의 evidence ID와 locator를 참조해야 한다.
2. 원문 인용은 정확한 excerpt hash와 대조한다.
3. claim status가 VERIFIED가 아니면 최종 결론에서 사실처럼 단정하지 않는다.
4. 제품 정보 미확정은 UNKNOWN/UNVERIFIED로 유지한다.
5. AI draft, human-reviewed evidence, final report를 분리한다.
6. 보고서 버전에는 source bundle ID, source revision, fetch timestamp, extractor version, review record가 포함되어야 한다.
7. 변경된 원문 hash 또는 revision은 기존 검증을 자동 무효화하고 재검토 대상으로 만든다.

## 6. 검토 기록 필수 필드

- claim_id / report_section
- source_id / canonical_url / final_url
- publisher / document_id / expected_revision / observed_revision
- evidence_id / locator / excerpt_sha256
- raw_sha256 / extracted_text_sha256 / extractor_version
- primary_source_review / independent_cross_check
- reviewer / reviewed_at_utc
- claim_status / limitation / conflict_note

검토자 필드는 실제 사람 검토가 이뤄진 경우에만 기록한다. 자동 생성된 검토자 이름이나 승인 서명을 금지한다.

## 7. 현재 적용 제한

C1+C2 코드는 hash/locator 연결과 문자열 기반 문서 식별 상태를 제공한다. 이 문서의 2차 독립 교차검증과 PDF 시각 대조는 자동 완료되지 않으며 각 연구 자료에 대해 별도 검토 기록이 필요하다. 실제 공식 URL 수집 및 실문서 fidelity 검증은 E3 별도 승인 이후에만 한다.
