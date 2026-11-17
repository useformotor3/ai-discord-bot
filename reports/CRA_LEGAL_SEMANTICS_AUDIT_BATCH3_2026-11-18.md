# CRA 법령 문언 심층 감사 — Batch 3 (CRA-021–CRA-035)

- 기준일: 2026-11-18 (KST)
- 검토 범위: CRA-021–CRA-035
- 주요 원문: Regulation (EU) 2024/2847 EUR-Lex 공식 OJ
- 관련 원문: Regulation (EU) 2023/1230 (Machinery Regulation), Regulation (EU) 2025/327 (EHDS)
- 공식 CRA 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

## 행별 검토 결과

| ID | 원문 대조 결과 | 수정/보완 사항 | 상태 |
|---|---|---|---|
| CRA-021 | Article 14(1)–(2)는 제조자가 PDE에 포함된 actively exploited vulnerability를 알게 되면 CSIRT designated as coordinator 및 ENISA에 동시에 single reporting platform을 통해 통지. early warning 24시간, vulnerability notification 72시간, final report는 corrective/mitigating measure가 available 된 후 14일 이내. Article 14(7)은 EU 내 주된 사업장(사이버보안 결정이 주로 내려지는 국가, 판별 불가 시 EU 내 직원 최다 사업장)을 기준으로 CSIRT endpoint를 정하며 EU 주된 사업장이 없는 제조자는 authorised representative, importer, distributor, users 순서로 국가를 결정. | locator 적절. 14일 final report의 기산점은 72시간 신고가 아니라 corrective/mitigating measure available 시점. EU 내 주된 사업장 기준과 EU establishment 부재 시 fallback 순서를 운영절차에 명시. '알게 된 시각' 기록 및 신고 플랫폼 endpoint는 제품별 신고 절차로 관리. | 1차 적정 |
| CRA-022 | Article 14(3)–(5)는 PDE 보안에 영향을 주는 severe incident를 인지한 제조자의 동시 신고 및 24시간 early warning, 72시간 incident notification, incident notification 제출 후 1개월 이내 final report를 규정. severe 기준은 sensitive/important data 또는 functions의 availability/authenticity/integrity/confidentiality 보호 능력에 대한 부정적 영향 가능성, 또는 PDE/사용자 네트워크·정보시스템에 악성코드 도입/실행을 야기했거나 야기할 수 있는 경우. | locator 적절. '심각한 사고'를 일반적인 중대 보안사고로 축약하지 말고 Article 14(5)(a)/(b)의 두 법정 기준을 반영. 1개월 final report 기산점은 incident notification 제출 시점. | 1차 적정 |
| CRA-023 | Article 14(8)은 actively exploited vulnerability 또는 severe incident를 인지한 제조자가 영향을 받은 사용자에게, 적절한 경우 모든 사용자에게, 해당 사건과 필요한 위험완화/시정조치를 통지하도록 함. 적절한 경우 구조화·기계판독·자동처리 가능한 형식을 사용. 제조자가 적시에 통지하지 못하면 CSIRT가 비례적·필요한 경우 사용자에게 통지 가능. | 현재 Annex II locator는 사건 후 사용자 통지의 직접 근거가 아님. Annex II는 일반 제품 정보/사용지침의 근거로 분리하고, CRA-023 법적 근거는 Article 14(8) 중심으로 수정. 필요 시 Article 17(2)는 공익상 공개 권한(제조자 통지와 별도)을 보조 근거로만 표시. | locator 수정 필요 |
| CRA-024 | Article 13(5)는 제3자 구성요소 통합 시 제품 사이버보안을 해치지 않도록 due diligence. Article 13(6)은 통합 구성요소의 취약점 식별 시 해당 구성요소 제조/유지 주체에게 보고하고, Annex I Part II에 따라 처리·수정하며, 제조자가 수정용 SW/HW 변경을 개발한 경우 적절한 기계판독 형식으로 코드/문서를 공유. | locator 적절. (5) 사전 통합 due diligence와 (6) 취약점 발견 후 보고/수정/공유 의무를 분리. SBOM 생성만으로 due diligence 전체를 입증했다고 간주하지 않는다. | 보완 필요 |
| CRA-025 | Article 69(2)는 2027-12-11 전에 시장 출시된 제품은 그 날짜부터 substantial modification 대상이 되는 경우에만 CRA 요구사항 적용. Article 69(3)은 예외적으로 Article 14 신고 의무를 CRA 범위에 속하고 그 날짜 이전에 출시된 제품에도 적용. Article 71(2)는 일반 적용일 2027-12-11, Article 14 적용일 2026-09-11, Chapter IV(Articles 35–51) 적용일 2026-06-11을 규정. | 기존 제품의 일반 요구사항 적용과 Article 14 신고 의무를 반드시 별도 분기. Regulation (EU) 2025/327 Article 104는 EHDS상 EHR system에 한해 CRA Article 13(4), 31(3), 32(5a)를 2027-03-26부터 수정/추가하는 특칙이며 일반 서보 드라이브의 CRA 전환 규칙으로 확대하면 안 됨. | 중요 보완 필요 |
| CRA-026 | CRA Article 2(5)는 다른 EU 규칙이 Annex I의 위험 전부/일부를 다루는 경우, 규제체계와 일치하고 sectoral rules가 동등/더 높은 보호수준을 달성하는 조건 아래 Commission delegated act로 CRA 적용을 제한/제외할 수 있도록 함. Machinery Regulation (EU) 2023/1230 Annex III §1.1.9는 corruption protection, §1.2.1은 control-system safety/reliability를 다룸. Machinery Regulation Article 9(9)는 Regulation (EU) 2019/881에 따른 cybersecurity scheme 인증/적합성 선언이 해당 요구를 커버하는 범위에서 두 Annex III 요구에 대한 적합성 추정을 규정. | 기존 CRA Article 69(1)은 일반적인 기계류/CRA 중복 근거가 아니라 다른 EU 법령 하 발행된 기존 EU type-examination certificates/approval decisions의 2028-06-11까지의 유효성 전환 조항이다. CRA Article 2(5)와 Machinery Regulation Article 9(9), Annex III §§1.1.9/1.2.1을 중심 근거로 정정. Machinery Regulation이 존재한다고 CRA 전체가 자동 면제되는 것은 아님. | locator 수정 필요 |
| CRA-027 | Article 27(1)은 관련 harmonised standard의 reference가 OJ에 공표된 범위에서 추정 적합성을 인정. Article 27(5)는 common specifications에 대해서도 적용 범위 내 추정 적합성, Article 27(8)–(9)는 적용 가능한 European cybersecurity certification scheme에 대한 추정 적합성/제3자 평가 면제 조건을 규정. | locator 적절. Commission Decision C(2026) 7861(M/606)은 ESO 표준화 요청/작업 범위이지 그 자체가 harmonised standard의 OJ 공표가 아님. 표준 초안·ESO 채택·Commission OJ reference publication·common specification·EU cybersecurity certificate를 구분. | 1차 적정 |
| CRA-028 | Article 18은 authorised representative의 서면 위임과 위임 범위(제조자 핵심 의무의 위임 불가 범위 포함), Article 19 importer, Article 20 distributor, Article 21 own-name/trademark 또는 substantial modification을 수행한 importer/distributor의 제조자 간주, Article 22 기타 제3자의 substantial modification 시 제조자 간주 및 영향받은 부분/제품 전체에 대한 Article 13·14 의무 적용을 규정. | 기존 Articles 18–23 묶음은 CRA-034의 Article 23 공급망 추적과 중복. CRA-028은 Articles 18–22의 역할/책임 이전으로 좁히고, authorised representative는 Article 18(2)에 따라 제조자의 핵심 Article 13 의무를 대체하지 못한다는 점을 명시. | 중복 정리 필요 |
| CRA-029 | Article 13(14)는 series production 제품이 CRA에 계속 적합하도록 절차를 마련하고, 생산/개발 프로세스, 제품 설계·특성, 적용한 harmonised standards/certification schemes/common specifications의 변경을 적절히 반영하도록 함. | locator 적절. 단순 형식적 변경관리 절차가 아니라 제품/제조 프로세스/적용 기준 변경이 지속 적합성에 미치는 영향 평가와 기록을 확인. | 1차 적정 |
| CRA-030 | Article 13(15)는 type/batch/serial 또는 기타 식별요소를 제품에 표시하고 불가능하면 포장/동봉 문서에 제공. Article 13(16)는 제조자 이름/상표 및 주소/연락처를 제품·포장·동봉 문서에 표시하고 Annex II 사용자 정보에도 포함하도록 함. Annex II(1),(3)은 제조자 연락처 및 제품 식별/이름/유형을 규정. | locator 적절. Article 13(16)의 연락처 언어는 사용자/시장감시당국이 쉽게 이해할 수 있어야 함. | 1차 적정 |
| CRA-031 | Article 13(20)은 제품과 함께 full EU DoC 사본 또는 simplified EU DoC 제공을 요구. Simplified DoC에는 full DoC에 접근할 수 있는 정확한 인터넷 주소가 포함되어야 함. Article 28(2)는 simplified DoC 양식 Annex VI를 규정. | 현재 Annex VI 근거는 적절. Full DoC는 Annex V, simplified DoC는 Annex VI임을 CRA-019와 일치시켜 표기. URL 정확성/접근성 및 제품·버전 식별 일치 시험을 포함. | 1차 적정 |
| CRA-032 | Article 13(21)은 제조자가 부적합을 알거나 믿을 이유가 있는 경우 즉시 시정, 또는 적절히 철회/리콜. (22)는 시장감시당국의 합리적 요청에 대한 정보/문서 제공과 위험 제거 조치 협력. (23)은 제조자 운영 중단으로 의무 이행이 불가능해지면 중단 전 당국 및 가능한 범위의 사용자에게 사전 통지. | locator 적절. Article 13(23)은 단순 사업중단 일반 공지가 아니라 운영중단 결과 CRA 의무 이행이 불가능한 제조자에게 적용. 'withdrawal'과 'recall'은 구분해 유지. | 보완 필요 |
| CRA-033 | Article 15(1)은 제조자 및 다른 자연인/법인이 제품 취약점 및 제품 위험 프로필에 영향을 줄 수 있는 cyber threats를 자발 신고할 수 있게 함. Article 15(2)는 제품 보안 영향 incident 및 near miss의 자발 신고. Article 15(3)–(5)는 처리/비밀보호/추가 의무 부과 금지 등을 규정. | locator 적절. Article 15 자발 신고는 Article 14 의무 신고를 대체하지 않는다. Article 15(5)의 '자발 신고만으로 신고자가 부담하지 않았을 추가 의무를 부과하지 않음'을 안내. | 1차 적정 |
| CRA-034 | Article 23은 경제운영자가 시장감시당국 요청 시 공급받은/공급한 다른 경제운영자 이름과 주소(공급받은 자 정보는 available where available)를 제공하고, 각 공급 거래 이후 10년간 제시 가능하도록 요구. | 기존 Articles 18–23은 역할/책임과 추적 의무가 중복. CRA-034는 Article 23 중심으로 좁히고, 공급받은 시점 이후 10년 및 공급한 시점 이후 10년의 양방향 기록을 별도로 관리. | 중복 정리 필요 |
| CRA-035 | Article 2(2)–(4)는 의료기기/IVD/차량형식승인 적용 제품, Regulation 2018/1139에 따라 인증된 제품, 해양장비지침 범위 장비를 명시적으로 제외. Article 2(5)는 다른 EU 규칙이 같은 사이버 위험을 다룰 때 delegated act에 의해 제한/제외될 수 있는 조건부 구조. (6)은 동일 사양의 동일 구성품 대체 예비부품, (7)은 국가안보/방위 전용 또는 기밀정보 처리 전용 제품 제외. (8)은 국가안보·공공안전·방위의 필수 이익에 반하는 정보 공개를 요구하지 않는 정보공개 예외. | locator에 Article 2(8)을 추가. Article 2(5)를 자동 제외로 표현하지 말고 Commission delegated act 필요성을 명시. Machinery Regulation은 Article 2(5)의 자동 제외 목록에 없으며, 위험 중복/인증 범위/관련 delegated act를 개별 확인. EHDS/Regulation 2025/327 특칙은 EHR systems에 한정. | 중요 보완 필요 |

## 핵심 교정 사항

1. CRA-023: Annex II를 사건 통지의 직접 근거에서 제거하고 Article 14(8) 중심으로 수정한다.
2. CRA-026: CRA Article 69(1)을 일반적 기계류 중복 근거로 사용하지 않는다. Article 69(1)은 기존 type-examination certificate/approval decision의 유효성 전환(2028-06-11까지) 조항이다. 일반 상호작용은 CRA Article 2(5), Machinery Regulation Article 9(9), Annex III §§1.1.9/1.2.1로 정리한다.
3. CRA-028/034: Articles 18–23을 중복 기재하지 않고, CRA-028은 Articles 18–22 경제운영자 역할/제조자 책임 전이, CRA-034는 Article 23 양방향 공급망 추적으로 분리한다.
4. CRA-035: Article 2(8) 정보공개 예외 추가. Article 2(5)는 자동 면제가 아니라 Commission delegated act를 통한 조건부 제한/제외 가능성으로 명시한다.
5. Regulation 2025/327 Article 104는 EHR system에 관한 CRA 특칙(Article 13(4), 31(3), 32(5a))이며 일반 PDE 전반에 확대 적용하지 않는다.

## 공식 근거

- CRA Articles 14–17, 18–23, 27, 69, 71 and Article 2(2)–(8): https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- Machinery Regulation (EU) 2023/1230, Article 9(9), Annex III §§1.1.9 and 1.2.1: https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng
- Regulation (EU) 2025/327, Article 104 and Article 105: https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng
- Commission Decision C(2026) 7861 / M/606 is a standardisation request, not OJ harmonised-standard publication.

## 검토 범위 제한
이 Batch는 15개 행의 1차 심층 문언 대조이며 법률가 의견서가 아니다. 제품별 적용성·등급·적합성은 제조사/모델/제품 아키텍처/시장 공급/의도된 목적/인증 증거가 없으므로 확정하지 않는다.
