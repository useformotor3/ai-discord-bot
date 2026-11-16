# CRA 보고서 #2 정정 및 기술 근거 감사

- 감사 대상 원본: `research_archive/2026-11-17_081037059553_f43b5252.md` (원본 blob SHA `cf1a561f7d21e82a803020f269678ea50704a4ed`)
- 원본 보존: 완료. 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847 공식 EUR-Lex 원문(Articles 11, 13–16, 69, 71 및 Annex I Part II, Annex II, Annex VII).

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| CVD 접수 근거를 Article 11(1)로 인용 | 중대 오류 | Article 11은 **General product safety**. CVD 정책은 Article 13(8), Annex I Part II (5), 제보 연락처는 Part II (6), 단일 연락 창구는 Article 13(17)/Annex II (2) |
| Article 14를 “Handling of vulnerabilities”라고 명명 | 제목 오류 | 공식 제목은 **Reporting obligations of manufacturers** |
| Article 11 명의의 Raw Text Quote | 부정확 직접 인용 | 공식 원문과 일치하지 않는다. 여러 Annex I 항목을 혼합·재작성한 문장으로 직접 인용 불가 |
| 24h/72h 보고 시간표 | 일부 맞지만 불완전 | actively exploited vulnerability에 24h/72h 및 조치 가용 후 14일 이내 최종 보고. Severe incident에도 24h/72h가 별도로 있고 최종 보고는 incident notification 제출 후 1개월 |
| 모든 취약점에 24h/72h 적용 | 범위 과장 | Article 14 의무 신고 트리거는 actively exploited vulnerability 및 제품 보안에 영향을 주는 severe incident |
| 신고 대상/경로 설명 | 불충분 | coordinating CSIRT와 ENISA에 동시에, Article 16의 ENISA 단일 신고 플랫폼을 통해 통지 |
| Annex II를 기술문서로 표기 | 부속서 오류 | Annex II는 사용자 정보·지침, 기술문서는 Annex VII |
| 적용 시점 누락 | 중요 누락 | Article 14는 2026-09-11부터 적용. Article 69(3)은 2027-12-11 이전 시장 출시된 CRA 범위 제품에도 Article 14를 적용 |

## 2. 정확한 CVD 근거

- **Article 13(8) 후단:** 제조사는 내부·외부 출처에서 보고된 잠재 취약점을 처리·개선하기 위한 적절한 정책과 절차를 보유하고, CVD 정책을 포함해야 한다.
- **Annex I Part II (5):** CVD 정책을 마련하고 시행한다.
- **Annex I Part II (6):** 제품 및 제3자 구성요소의 잠재 취약점 공유를 촉진하고, 취약점 신고를 위한 연락 주소를 제공한다.
- **Article 13(17):** 사용자가 직접 신속히 연락할 수 있는 단일 연락 창구(single point of contact)를 지정하고 쉽게 식별할 수 있도록 한다.
- **Annex II (2):** 사용자 정보에 취약점 신고 연락 창구와 CVD 정책 위치를 포함한다.
- **Recital (76):** CVD 정책은 상세 정보가 공개되기 전에 제조사가 취약점을 진단·개선할 수 있도록 구조화된 절차를 마련하는 취지를 설명한다. 별도 시간 제한 조항은 아니다.

## 3. Article 14 의무 신고 일정

### 3.1 Actively exploited vulnerability — Article 14(1)–(2)

제품에 포함된 actively exploited vulnerability를 제조사가 인지하면 coordinating CSIRT와 ENISA에 동시에 통지하고, Article 16의 단일 신고 플랫폼을 사용한다.

| 제출물 | 법정 기한 | 주요 내용 |
|---|---|---|
| Early warning | 인지 후 지체 없이, 늦어도 24시간 | 제품이 제공된 회원국 정보(해당되는 경우) |
| Vulnerability notification | 인지 후 지체 없이, 늦어도 72시간 | 제품 일반 정보, 악용/취약점의 일반적 성격, 시정·완화 조치 및 사용자가 취할 조치, 정보 민감도(해당되는 경우) |
| Final report | 시정 또는 완화 조치가 이용 가능해진 후 늦어도 14일 | 취약점 설명·심각도·영향, 가능한 경우 악용 행위자, 제공된 업데이트/시정 조치 |

### 3.2 Severe incident — Article 14(3)–(5)

제품 보안에 영향을 미치는 severe incident도 별도 의무 신고 대상이다.

| 제출물 | 법정 기한 | 주요 내용 |
|---|---|---|
| Early warning | 인지 후 지체 없이, 늦어도 24시간 | 불법/악의적 행위 의심 여부, 제품 제공 회원국 정보(해당되는 경우) |
| Incident notification | 인지 후 지체 없이, 늦어도 72시간 | 사건 성격, 초기 평가, 시정·완화 조치 및 사용자가 취할 조치, 정보 민감도(해당되는 경우) |
| Final report | Incident notification 제출 후 1개월 | 사건 상세·심각도·영향, 위협 유형 또는 근본 원인, 적용/진행 중 완화 조치 |

Article 14(5)의 severe incident는 민감/중요 데이터 또는 기능의 가용성·진정성·무결성·기밀성 보호 능력에 부정적 영향을 주거나 줄 수 있는 경우, 또는 제품/사용자 네트워크에 악성 코드 도입·실행을 초래했거나 초래할 수 있는 경우를 포함한다.

### 3.3 신고 경로와 사용자 통지

- Article 14(7), Article 16: ENISA 단일 신고 플랫폼을 사용하며 제조사의 EU 내 주된 사업장이 있는 회원국의 coordinating CSIRT endpoint로 신고하고 ENISA가 동시에 접근할 수 있도록 한다. EU 내 주된 사업장이 없는 경우 Article 14(7)의 대리인·수입업자·유통업자·사용자 분포 순서 규칙을 따른다.
- Article 14(8): 제조사는 영향을 받는 사용자 및 적절한 경우 모든 사용자에게 취약점/사건과 필요한 위험 완화·시정 조치를 알려야 한다. 적절한 경우 구조화된 기계가독형 형식을 사용할 수 있다.
- Article 15는 자발적 신고를 규정하므로 Article 14의 의무 신고와 구분한다.

## 4. 적용 시점 및 제품 적용성

- Article 71(2): CRA 일반 적용일은 2027-12-11이나 Article 14는 예외적으로 **2026-09-11부터 적용**한다.
- Article 69(3): Article 14 의무는 2027-12-11 이전에 시장 출시된 CRA 범위 제품에도 적용한다.
- 따라서 2026-11-17 현재 Article 14 신고 의무는 이미 적용 중이다. 이는 CRA의 모든 제조사 의무가 2026-09-11부터 전부 적용된다는 의미는 아니다.
- 서보 드라이브가 디지털 요소를 가진다는 이유만으로 제품별 CRA 적용 범위를 자동 확정하지 않는다. CRA 정의, EU 시장 제공, 상업적 활동, 제품 구조 및 예외를 먼저 판단한다.

## 5. 수정된 권고 문안

> CRA 적용 대상 제품의 제조사는 제품 및 구성요소의 잠재 취약점을 처리하기 위한 정책·절차와 CVD 정책을 운영하고, 취약점 신고 연락 주소 및 단일 연락 창구를 제공해야 한다(Article 13(8), (17), Annex I Part II (5)–(6), Annex II (2)). 제품 내 actively exploited vulnerability를 인지하면 coordinating CSIRT와 ENISA에 단일 신고 플랫폼을 통해 동시에 통지하고, 24시간 이내 early warning, 72시간 이내 vulnerability notification, 시정·완화 조치가 이용 가능해진 뒤 14일 이내 final report를 제출해야 한다(Article 14(1)–(2)). 제품 보안에 영향을 주는 severe incident는 별도 신고 대상으로 24시간 이내 early warning, 72시간 이내 incident notification, incident notification 제출 후 1개월 이내 final report가 요구된다(Article 14(3)–(5)). 영향을 받는 사용자에게도 필요한 정보를 제공해야 한다(Article 14(8)). Article 14는 2026-09-11부터 적용되며 Article 69(3)에 따라 그 이전 시장 출시된 CRA 범위 제품에도 적용된다. 제품별 적용 범위 및 신고 트리거 충족 여부는 별도로 평가한다.

## 6. 출처 및 결론

1. EUR-Lex Regulation (EU) 2024/2847 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
2. Article 11: General product safety.
3. Article 13(8), (17): CVD 정책·단일 연락 창구.
4. Article 14(1)–(8): actively exploited vulnerability 및 severe incident 신고, 기한, 경로, 사용자 통지.
5. Article 15–16: 자발적 신고 및 단일 신고 플랫폼.
6. Annex I Part II (5)–(6): CVD 정책 및 제보 연락 주소.
7. Annex II (2): 사용자 정보의 취약점 연락처/CVD 정책.
8. Annex VII: 기술문서.
9. Article 69(3), 71(2): 경과 규정 및 Article 14 적용일.

원본은 Article 11과 Article 14의 제목·범위를 잘못 설명했고, Article 11 명의의 인용문은 공식 원문과 일치하지 않는다. 24h/72h 일정은 두 신고 트리거에 각각 적용되며 final report 기한은 서로 다르다. 본 정정은 법령 근거 감사이며 특정 제품의 CRA 적합성 또는 실제 사건의 신고 의무 충족 여부를 선언하지 않는다.
