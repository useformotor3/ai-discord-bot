# CRA Single Reporting Platform 운영 준비 기준서 — 2026-11-20

- 버전: v1.0
- 기준일: 2026-11-20 (KST)
- 적용 대상: CRA Article 14 제조자 의무의 내부 준비 절차
- 근거: Regulation (EU) 2024/2847 Articles 14–17, 69(3), 71(2); Commission C/2026/6013; Commission reporting page; ENISA SRP FAQ (2026-10-15), Glossary v1.6 (2026-10-21), AR User Manual v1.3 (2026-11-04).
- 지위: 법령 원문을 대체하지 않는 운영 준비 가이드. 실제 사건 발생 시 최신 ENISA 문서와 관할 CSIRT 지침을 재확인.

## 1. 신고 의무를 촉발하는 사건

| 사건 | 의무 | 기한 |
|---|---|---|
| 제품에 포함된 적극 악용 취약점(AEV) 인지 | Article 14(1)–(2) | Early warning 24h, notification 72h, final report: corrective/mitigating measure available 후 14일 이내 |
| 제품 보안에 영향을 미치는 심각한 사고(SI) 인지 | Article 14(3)–(5) | Early warning 24h, notification 72h, final report: 72h notification 후 1개월 이내 |
| 기타 취약점·위협·near miss 등 | Article 15 자발적 신고 가능성 | Article 14와 분리; 현행 SRP 기능 제공 여부 재확인 |

기한은 제조자가 사건을 인지한 시각을 기준으로 관리한다. 내부 시계는 UTC로 저장하고, 'without undue delay' 의무를 단순히 24/72시간까지 기다려도 된다는 뜻으로 해석하지 않는다.

## 2. 플랫폼 운영상 현재 확인된 제약

1. SRP 운영 시작: 2026-09-11.
2. 초기 릴리스 API 미제공: 내부 시스템 연동은 자체 관리 가능하나 규제 신고는 웹 UI 제출 전제로 계획.
3. SRP UI 영어 전용(ENISA FAQ 24, 2026-10-15).
4. Article 15 voluntary reporting은 SRP에서 아직 구현되지 않음(FAQ 27).
5. SRP 일시 장애 시 복구 후 SRP에 신고. 즉시 연락이 필요한 경우 CDaC에 직접 연락할 수 있으나 SRP 복구 후 제출 필요(FAQ 25).
6. UI 72h 카운터는 24h Early Warning 제출 후 48h를 계산해 최초 인지 후 72h와 불일치할 수 있다. AEV final report 카운터는 현재 없음. SI 카운터는 72h 신고 제출 후 1개월. UI 카운터는 법정기한이 아니므로 내부 시간 계산을 별도로 운영(FAQ 26).
7. ENISA FAQ 35는 공개적으로 알려진 취약점의 EUVD 등재와 CVE ID 관련 연락 가능성을 설명한다.

## 3. 계정·담당자 구조

- AR는 개인 EU Login 계정 및 MFA 사용.
- 제조자별 Primary AR 1명, Secondary AR 최대 20명.
- Primary AR는 제조자 association 및 Secondary AR 초대/삭제 등 관리 권한을 보유.
- AR-제조자 association 검증은 CDaC가 담당하며, 검증 대기 중에도 최대 20건까지 신고할 수 있다는 ENISA FAQ 설명이 있다. 이 기능을 등록 지연의 이유로 삼지 말고 사전 준비한다.
- EU 내 주된 사업장은 제품 사이버보안 관련 의사결정이 주로 이루어지는 곳. 확인 불가 시 EU 내 직원 수가 가장 많은 사업장. EU 내 주된 사업장이 없으면 authorised representative, importer, distributor, users 순의 법정 기준을 적용해 CDaC를 결정한다.

## 4. 신고 내용 준비

ENISA Glossary v1.6은 신고 단계별 입력 항목을 나눈다. 내부 case record에는 최소한 다음을 보존한다.

- 제조자 법인명 및 SRP association 상태
- 상용 제품명, SKU/model, HW revision, firmware/bootloader/software build, 영향 버전 범위
- 제품이 공급된 EU 회원국과 제품의 유통 경로
- 취약점/사고가 발생한 구성요소 및 구성요소 버전
- 최초 인지 UTC 시각, 사건 발생 UTC 시각(정확하지 않으면 추정 표시)
- AEV/SI 구분, 신뢰할 수 있는 악용 증거, 영향받는 기능·데이터의 availability/authenticity/integrity/confidentiality 영향
- 공격 경로, 알려진 악성 행위자 정보(미확인 시 unknown 명시), 심각성·영향 평가
- 시정/완화 조치, 고객이 수행할 수 있는 안전한 조치, 보안 업데이트 제공 시각
- PEC 적용을 검토한다면 Article 16(2) 조건별 구체적 사실과 요청 근거

모든 항목을 최초 24시간 내 확정할 수 있다고 가정하지 않는다. 단계별 required/optional/if available 구분에 맞춰 사실과 미확인을 구분하고, 후속 보고에서 보완한다.

## 5. PEC 및 공개·비밀정보 관리

- PEC는 Article 16(2)의 법정 조건에 맞는 예외 상황에서만 검토한다.
- 단순 영업비밀, 고객 비밀 또는 공개를 원하지 않는다는 사유만으로 PEC 요건이 충족된다고 보지 않는다.
- 정보 민감성, 추가 확산으로 인한 위험, 법정 조건, 요청 범위 및 시점을 기록하고 법무·보안 책임자의 승인 절차를 둔다.

## 6. 내부 역할 분담 권고

| 역할 | 책임 |
|---|---|
| PSIRT/제품보안 | 최초 분류, 악용 증거, 기술 조사, 취약점·사고 case owner |
| 제품/펌웨어 엔지니어링 | 영향 SKU/FW, 재현·완화·수정·업데이트 검증 |
| 법무/규제 | 제조자 지위, EU main establishment/CDaC, Article 14/15 및 PEC 판단 |
| 고객지원/서비스 | 고객·설치 제품 식별, 안전한 임시 조치·통지 |
| EU AR | SRP 접근, 제출·수정·후속 보고 |
| 경영진/위기대응 | 24/72h 승인·자원·공개 판단 및 기록 |

## 7. 운영 체크리스트

- [ ] 제품 자산·SKU·HW/FW 버전·EU 공급 회원국을 검색할 수 있다.
- [ ] 24h/72h/최종보고 시각을 최초 인지 UTC 기준으로 계산한다.
- [ ] AEV/SI 판단 및 근거를 문서화한다.
- [ ] CDaC와 EU main establishment 기준을 사전에 확인했다.
- [ ] Primary/Secondary AR, EU Login MFA를 준비했다.
- [ ] 영어 SRP 제출 템플릿 및 번역·승인 담당자를 지정했다.
- [ ] API 미제공을 전제로 수동 웹 제출 단계를 리허설했다(실제 운영 계정·신고 전용 모의훈련).
- [ ] SRP 장애 시 직접 CSIRT 연락 및 복구 후 재제출 절차가 있다.
- [ ] UI 카운터와 내부 법정시한 계산을 대조하되 UI를 기준으로 삼지 않는다.
- [ ] Article 15 기능과 ENISA 문서 버전을 신고 시점에 재확인한다.

## 8. 공식 원문·열람 상태

- CRA Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- Commission C/2026/6013: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013
- Commission reporting: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- ENISA SRP FAQ: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions
- ENISA Glossary v1.6: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-glossary2
- ENISA AR User Manual v1.3: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/cra-srp-ar-user-manual

**열람 한계:** FAQ/Glossary의 웹 본문을 검토했으나 raw bytes/SHA-256은 확보하지 않았다. AR User Manual은 ENISA 페이지의 v1.3/2026-11-04 메타데이터를 확인했으며 PDF 원본의 페이지별 검토·hash는 미완료. SRP live status endpoint는 직접 열람 실패. 실제 계정 등록/제출/플랫폼 시험은 수행하지 않았다.
