# European Commission CRA Guidance — 출처 검증 및 프로젝트 영향 검토

**검토일:** 2026-11-12  
**공식 문서:** Commission Guidance on the application of Regulation (EU) 2024/2847 (Cyber Resilience Act), C(2026) 5252 final  
**공식 게시일:** 2026-07-27  
**공식 게시 페이지:** https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation  
**상태:** 공식 게시 사실 및 안내 범위 VERIFIED; Annex 본문 조항별 해석·인용 검증은 PENDING

## 1. 확인된 사실

European Commission 공식 게시 페이지는 2026-07-27 CRA 실무 가이드를 게시했다고 명시한다. 가이드 범위는 다음 주제를 포함한다.

- CRA 적용 범위: remote data processing solutions, free/open-source software
- substantial modification
- support periods
- reporting obligations
- risk assessment requirements
- 중소기업 등을 위한 67개 실무 예시, use case, flowchart, graph

Commission은 가이드가 비구속적(non-binding)이라고 명시한다. 따라서 법령(Regulation (EU) 2024/2847)의 문언을 대체하거나 수정하는 법적 근거로 취급하지 않는다. 법령과 가이드가 다르게 읽히는 경우 법령 원문과 법적 검토를 우선하고, 가이드는 Commission의 적용 설명·행정적 해석 참고자료로 분리한다.

## 2. 공식 원문 접근

- Official publication page: 위 URL
- Communication: C(2026) 5252
- Annex: Commission guidance on the application of the CRA
- Annex download endpoint surfaced by the official page: https://ec.europa.eu/newsroom/dae/redirection/document/131456

이 검토 세션에서 Annex 다운로드 링크는 확인했으나 PDF 원문을 도구로 안정적으로 열어 페이지/문단을 직접 대조하지 못했다. 따라서 개별 예시·문단 번호·직접 인용은 아직 등록하지 않는다. 다음 검토에서 공식 Annex PDF를 확보해 page/paragraph 단위로 Pass B/C 검증한다.

## 3. 현재 프로젝트에 미치는 영향 — 검토 우선순위

| Topic | 연결 프로젝트 문서/입력 | 해야 할 검토 | 현재 상태 |
|---|---|---|---|
| Product scope / remote processing | SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md BD-01..BD-15 | PC engineering tool, mobile app, cloud diagnostics/remote service, separately marketed module의 경계를 가이드 예시와 대조 | PENDING |
| Support period | CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md M-03/M-04, TR-18 | Article 13(8)/(9) 원문과 가이드의 support-period 해석을 함께 검토. 법정 최소/예외 문언을 가이드가 변경한다고 보지 않음 | PENDING |
| Substantial modification | product change/release management | firmware update, hardware revision, feature addition 및 third-party component 변경이 substantial modification에 해당하는지 사실관계별 분석 | PENDING |
| Risk assessment | threat model / traceability matrix | intended purpose, reasonably foreseeable use, environment, assets, threats, mitigations 및 residual risk 기록을 가이드의 설명과 비교 | PENDING |
| Article 14 reporting | SECURITY_TEST_EVIDENCE_REGISTER.md TST-OPS-03 | actively exploited vulnerability와 severe incident의 트리거/시한/사용자 통지를 원문 및 가이드와 대조 | PENDING |
| FOSS / supplier components | SBOM, supplier due diligence, PSIRT | open-source components와 stewards의 지위, manufacturer obligations, supply-chain evidence를 정확히 분리 | PENDING |

## 4. 정정·해석 통제

- Guidance는 법령과 구분된 출처 ID로 관리한다.
- 가이드 문장만으로 법적 의무를 새로 만들거나 조항 번호를 바꾸지 않는다.
- 직접 인용은 Annex PDF 원문에서 페이지/문단을 재확인한 후에만 VERIFIED로 승격한다.
- 제품 적용은 SKU, 공급 형태, intended purpose, 연결 구조 및 제품 경계 증거를 별도로 요구한다.
- AI의 해석과 법률 자문/법원의 구속력 있는 해석을 혼동하지 않는다.

## 5. 다음 검증

1. 공식 Annex PDF 다운로드·열기 및 SHA-256 기록.
2. Scope, remote processing, support period, substantial modification, risk assessment, reporting, FOSS 각 주제의 문단/페이지 추출.
3. Regulation 2024/2847 원문과 나란히 Pass B/C 비교.
4. 변경이 필요한 기존 제품 경계 템플릿/추적성 매트릭스만 최소 수정.
5. 변경 전후 근거와 문서 revision을 CLAIM_EVIDENCE_LEDGER.md에 기록.

## 6. 출처

- European Commission official publication page: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
- Official Annex download endpoint: https://ec.europa.eu/newsroom/dae/redirection/document/131456
- Binding Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
