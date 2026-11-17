# CRA 보고서 #20 정정 및 의무 신고·CVD·사용자 통지 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_114037069162_06b61844.md
- 원본 blob SHA: ab5c4f1e4ac91e36d22734cb8da83c9c70cfe3e1
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Article 11이 Reporting obligations of manufacturers | 조항/제목 오류 | Article 11은 General product safety. 신고 의무는 Article 14 |
| Article 11 paragraph 1 raw quote | 구판/초안 문구 | final OJ Article 14(1)–(2)의 구조와 문언이 다르며 직접 인용 불가 |
| 모든 중대한 취약점/사이버 사고에 24h/72h 동일 적용 | 범위 혼합 | actively exploited vulnerability는 24h early warning, 72h vulnerability notification, corrective measure available 후 14일 이내 final report. Severe incident는 24h/72h 및 incident notification 후 1개월 final report |
| “ENISA 및 단일 연락 창구”에 통지 | 개념 혼동 | 규제기관 신고는 Article 14/16 single reporting platform을 통해 CSIRT coordinator의 endpoint로 제출하고 ENISA에 동시에 접근 가능하게 한다. 제조사 single point of contact는 Article 13(17)의 사용자 문의 채널 |
| 모든 취약점의 의무 신고 | 범위 과장 | Article 14 의무 신고 트리거는 actively exploited vulnerability 및 severe incident having an impact on product security. Article 15는 자발적 신고 |
| CVD를 Article 14 신고 절차와 동일시 | 별도 의무 혼합 | CVD policy는 Annex I Part II (5), 제보 연락 주소는 (6), fixed-vulnerability 공개는 (4) |
| 사용자 통지 | 별도 조항 연결 필요 | Article 14(8)는 actively exploited vulnerability/severe incident 인지 후 impacted users 및 적절한 경우 all users에 통지하도록 규정 |

## 2. 정확한 법적 근거

- Article 14(1)–(2): actively exploited vulnerability를 인지하면 CSIRT designated as coordinator와 ENISA에 동시에 신고. 24시간 이내 early warning, 72시간 이내 vulnerability notification, corrective/mitigating measure가 available된 후 14일 이내 final report.
- Article 14(3)–(4): product security에 영향을 주는 severe incident를 CSIRT coordinator와 ENISA에 신고. 24시간 이내 early warning, 72시간 이내 incident notification, incident notification 제출 후 1개월 이내 final report.
- Article 14(5): severe incident 판단 기준.
- Article 14(7): 신고는 Article 16 single reporting platform을 통해 CSIRT coordinator의 endpoint로 제출하고 ENISA에 동시에 접근 가능하게 한다.
- Article 14(8): impacted users 및 적절한 경우 all users에 vulnerability/incident와 필요한 risk mitigation/corrective measures를 알린다.
- Article 15: 자발적 vulnerability/incident/near-miss reporting.
- Article 16: single reporting platform의 설립 및 전파 절차.
- Article 13(17): 제조사의 single point of contact는 사용자가 제조사에 직접·신속하게 연락할 수 있는 창구이며, Article 14 single reporting platform과 다르다.
- Annex I Part II (4)–(6): fixed-vulnerability disclosure, CVD policy, vulnerability contact address는 별도 요구.

## 3. 수정된 권고 문안

제조사는 actively exploited vulnerability를 인지한 경우 Article 14(1)–(2)의 24h/72h/14-day 신고 절차를 적용한다. 제품 보안에 영향을 주는 severe incident는 Article 14(3)–(5)의 24h/72h/1-month 절차를 별도로 적용한다. 신고는 Article 16 single reporting platform을 통해 지정 CSIRT coordinator의 endpoint로 제출하고 ENISA에 동시에 접근 가능하게 한다(Article 14(7)). impacted users 통지는 Article 14(8), 제조사 문의/취약점 제보 연락 창구는 Article 13(17), CVD policy는 Annex I Part II (5)로 분리한다. 모든 취약점을 Article 14 mandatory report로 확대하지 않는다.

## 4. 서보 드라이브 제조사 운영 권고

- PSIRT/CVD 접수, Article 14 mandatory reporting, Article 14(8) customer notification, security advisory publication을 별도 workflow로 설계.
- actively exploited vulnerability와 severe incident의 trigger/clock/final-report deadline을 별도 타이머로 관리.
- 제조사 single point of contact와 regulatory single reporting platform의 담당자/권한을 분리.
- 제품이 공급된 회원국, importer/distributor 및 impacted user 식별 데이터의 정확성을 유지.
- 규제기관 신고 내용의 민감도 및 Article 16의 정당한 dissemination delay 조건을 법무/보안 담당자와 검토.

## 5. 공식 출처

- Official Journal Article 14–16: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text: https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
