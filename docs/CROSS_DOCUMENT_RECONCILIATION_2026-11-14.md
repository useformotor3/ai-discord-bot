# CRA 서보 드라이브 문서 간 추적성 재검증 — 2026-11-14

- 문서 ID: CRA-XDOC-RECON-20261114-001
- 기준 브랜치: \`cra-project-foundation\`
- 검사 기준 작업 HEAD: \`89ce7f1160ad91ab2801bd5bbbecb96ca004ca9f\`
- 검사 기준 main HEAD: \`291b1c93905d41c9bba83b4510c3e5ef43f86e95\`
- 검사 목적: Claim Evidence Ledger, Canonical Requirement Register, 양 추적성 매트릭스, 시험 증거 대장의 ID·범위·상태를 상호 대조한다.
- 범위 제한: 이 문서는 문서 간 식별자/연결 정합성 검사다. 법령 전체 재감사, 제품별 법적 적용성 판정, DUT 시험 실행을 의미하지 않는다.

## 1. Git 및 아카이브 기준선

| 항목 | 확인 결과 |
|---|---|
| main HEAD | \`291b1c93905d41c9bba83b4510c3e5ef43f86e95\` |
| main archive / history | 1,565 / 1,565 |
| main archive/history 누락·고아·중복 | 0 / 0 / 0 |
| main state.json | 2026-11-14, count=2 (일일 카운터; 전체 아카이브 수가 아님) |
| 작업 브랜치 HEAD | \`89ce7f1160ad91ab2801bd5bbbecb96ca004ca9f\` |
| 작업 브랜치 archive / history | 990 / 990 |
| main 대 작업 브랜치 | diverged, ahead 1,000 / behind 581 (해당 시점 snapshot; 매 세션 재조회) |
| 최신 작업 브랜치 push CI | run \`43531794670\`, SUCCESS; strict audit 990/990, missing/orphan/duplicate/malformed 0 |

main은 읽기 전용으로 유지했다. 병합·rebase·sync를 수행하지 않았다. 이번 변경은 CRA 문서 및 추적성 정리에 한정되며 \`main.py\`, 운영 workflow, Gemini prompt, schema, evidence bundle을 수정하지 않았다.

## 2. Claim Evidence Ledger ID 집계

Ledger의 서로 다른 기록 범위를 혼합하지 않도록 집계를 분리한다.

| 범위 | 파일 기록 | 원자 주장 | 고유 ID |
|---|---:|---:|---:|
| 2026-11-13 main-only #8–#62 namespace | 55 | 345 | 400 |
| 이전 감사 legacy claim namespace (#35–#124) | 0 | 99 | 99 |
| Ledger 전체 | 55 | 444 | 499 |

- #48–#52의 요약행 5개는 원자 Claim ID와 중복되던 표시를 \`SUMMARY-#48\`…\`SUMMARY-#52\`로 변경했다. 이 요약행은 Claim ID 집계에서 제외한다.
- 전체 Ledger의 CRA-ARCH 식별자 499개는 현재 중복 0개다.
- legacy claim 99개(\`CRA-ARCH-035-*\`…\`CRA-ARCH-124-*\`)는 별도 crosswalk에 CANDIDATE mapping 99/99를 추가했다(32 + 67). 이는 독립 검토 전의 추적성 후보이며, 법령 검증 상태를 바꾸지 않는다.
- 2026-11-13 신규 atomic 345개 중 343개는 하나 이상의 \`CRA-REQ-*\`에 연결된다. 나머지 2개는 초안/타협안 문구와 최종 법령의 직접 인용 정확성만 다루므로 \`CRA-EVIDENCE-QUOTE-ACCURACY-001\`에 연결되어 있으며, 제품 요구사항 ID를 억지로 부여하지 않는다.

## 3. Canonical Requirement Register

- 실제 Canonical Requirement 행: **45개** (이전 일부 문서의 46개 표기는 오기).
- 2026-11-13 atomic claims에서 직접 참조되는 요구사항: **42개**.
- claim-level 직접 연결은 없고 매트릭스에 forward-map된 요구사항: **3개**
  - \`CRA-REQ-INTERCONNECTIVITY-001\`
  - \`CRA-REQ-EXPLOIT-MITIGATION-001\`
  - \`CRA-REQ-SECURE-DATA-TRANSFER-001\`
- legacy claim 99개는 위 42개 집계에 포함하지 않았다. 99/99 후보 매핑을 추가했으며, 개별 문장·근거를 재확인하는 독립 검토가 남았다.

## 4. 추적성 매트릭스 대조 결과

| 검사 | 결과 |
|---|---:|
| Canonical Requirement Register | 45개 |
| 통합 추적성 매트릭스에 연결된 Canonical ID | 45/45 |
| 요구사항-HW/FW/시험/증거 매트릭스에 연결된 Canonical ID | 45/45 |
| Security Test Evidence Register | 49개 |
| 통합 매트릭스에서 참조되는 시험 ID | 49/49 |
| 시험 ID 중복 | 0 |
| 시험 결과 NOT_RUN | 49/49 |

시험 ID 비교 시 \`TST-UPD-01..06\`, \`TST-CMD-01..03\`, \`TST-ERASE-01/03\` 등의 범위·축약 표기를 개별 ID로 확장했다. 따라서 축약 표기 때문에 발생하는 가짜 누락을 제거했다.

### 이번에 반영한 연결 보완

- 통합 매트릭스: TR-14 vulnerability handling, TR-15 user contact, TR-17 manufacturer Article 13, TR-18 support-end, TR-19 reporting scope/timeline을 명시적으로 연결했다.
- 통합 매트릭스: 사용자 정보 보존, DoC, CE 표시 및 벌칙 검토를 위한 TR-22를 추가했다.
- 요구사항 매트릭스: P2-02, M-01/M-02/M-05, R-01/R-02 매핑을 보완했다.
- 요구사항 매트릭스: 사용자 정보 보존 M-06, 제품 분류 M-07, 벌칙 M-08, Article 69(3) 전환 규칙 R-04를 추가했다.
- 중복·고아로 남아 있던 TR-21 logging 매핑은 제거하고 기존 TR-11 및 TR-11A의 역할을 유지했다.

## 5. 남은 P0 작업

1. **legacy claim 99개 candidate review:** 추가한 99개 후보 연결을 각 원문 문장/근거 조항과 대조해 승인·수정·삭제한다. 불명확하면 UNMAPPED로 유지하고 억지 매핑하지 않는다.
2. **정본 문장 대조:** 345개 신규 원자 주장과 legacy 99개를 제1권, 제2권, PSIRT SOP, 제품 분류 매트릭스, 위협 모델, 시험 대장과 문장 단위로 대조한다. 정정 내용은 독자용 정본에 반영하거나 미반영 사유를 기록한다.
3. **PSIRT SOP 연결:** Article 14 trigger, 기한, 신고 경로, 사용자 통지 및 Article 69(3) 전환 규칙을 Canonical ID와 양 매트릭스에 연결한다.
4. **다음 main-only archive audit:** 2026-11-14 일일 보고서 #1–#4가 대기열에 등록되었다. 다음 배치는 #1–#5를 목표로 하되, 실행 시점의 main HEAD/history/state 및 원본 blob SHA를 다시 고정한다.

## 6. 제품·시험 상태 경계

- 제품 SKU, intended purpose, EU 공급 형태, 제품 경계, 네트워크/원격 기능, 정확한 ST MCU 주문 코드는 미확정이다.
- Servo drive의 CRA 적용성 및 Important Product Class I/II 분류는 **UNVERIFIED**다.
- TST 49개는 설계·검증 계획이며 전부 **NOT_RUN**이다. 실제 DUT, 회로도, 펌웨어, 원시 시험 증거를 확인하기 전 PASS로 승격하지 않는다.
- ASIL/SIL 또는 기능안전 결과를 CRA 적합성으로 대체하지 않는다.

## 7. 재검증 방법

- Canonical ID: Ledger의 실제 \`CRA-REQ-*\` 등록 행과 양 매트릭스의 ID를 집합 비교.
- Test ID: 시험 대장과 통합 매트릭스의 개별 ID, \`..\` 범위 및 \`/\` 축약 표기를 확장한 후 집합 비교.
- Claim ID: Ledger 전체의 \`CRA-ARCH-*\` 행에서 중복을 확인하고 summary 표기는 별도 namespace로 분리.
- Archive: GitHub main의 recursive tree와 \`history.json\`의 경로·개수를 비교. \`state.json.count\`는 일일 카운터로 취급.

## 2026-11-14 live recheck — 00:19 UTC

- main HEAD: \`03b3ecaaa506c00146f5cb9d5855e6a66c3ef1c7\`; archive/history 1,567/1,567; state.json date/count 2026-11-14 / 4 (daily counter).
- work branch HEAD at check: \`f0fbb4954b0853987ce9f918733e5f6858150483\`; archive/history 990/990.
- compare main...cra-project-foundation: diverged, ahead 1,049 / behind 583. This is a snapshot; re-fetch live refs before every session. No merge/rebase/sync.
- latest push CI run \`43533348296\` on the checked branch HEAD: SUCCESS; strict archive audit 990/990, missing/orphan/duplicate/malformed 0. Archive integrity only, not product compliance.
- main daily report #4 is now registered in \`CRA_ARCHIVE_AUDIT_QUEUE.md\`; reports #1–#4 are queued for manual Pass A/B/C review. #4 overlaps #2 on secure-by-default and initial authentication; audit the overlap instead of treating it as a new requirement.
