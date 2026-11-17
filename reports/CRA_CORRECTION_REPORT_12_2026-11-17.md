# CRA 보고서 #12 정정 및 지원 기간·무상 보안 업데이트 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_103046838716_c128fb4d.md
- 원본 blob SHA: fa7f687ecab1297436e5ced26983f8e622a0a0d9
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Article 13(14)가 무상 보안 업데이트를 규정 | 조항 오류 | Article 13(14)는 series production 제품의 지속적 적합성 절차. 무상 보안 업데이트는 Annex I Part II (8) |
| Article 13(8)의 지원 기간 quote | 직접 인용 불일치 | support period 산정은 Article 13(8)이지만 원본 quote는 최종 OJ 문언과 일치하지 않는다 |
| 최소 10년 지원 기간 | 개념 혼동 | Article 13(8)은 원칙적으로 최소 5년, 예상 사용 기간이 5년 미만이면 그 기간. Article 13(9)의 10년은 각 security update의 availability 유지기간 |
| 모든 패치·workaround가 무조건 무상 | 범위 과장 | Annex I Part II (8)은 확인된 보안 이슈를 해결하는 security update가 available한 경우 지체 없이 무상 제공하되, tailor-made product에 대해 manufacturer/business user가 달리 합의한 경우 예외 |
| 모든 제품에서 기능 업데이트와 보안 업데이트를 항상 분리 | 조건 누락 | Part II (2)는 기술적으로 가능한 경우 new security updates를 functionality updates와 분리하도록 규정 |
| 지원 종료 전 사전 고지 | 시점·근거 불명확 | Article 13(19)는 구매 시점에 support-period 종료일(최소 월/연)을 명확히 표시하고, 기술적으로 가능하면 종료 시 사용자 알림을 제공하도록 규정 |

## 2. 정확한 법적 근거

- Article 13(8): 제조사는 제품의 예상 사용 기간, 합리적인 사용자 기대, 제품의 성격/의도된 용도 및 관련 EU 법령 등을 고려해 support period를 결정한다. 원칙적으로 최소 5년이며, 예상 사용 기간이 5년 미만이면 support period는 예상 사용 기간에 해당한다.
- Article 13(9): support period 중 사용자에게 제공된 각 security update는 발행 후 최소 10년 또는 support period의 잔여 기간 중 더 긴 기간 동안 계속 이용 가능해야 한다. 이는 support period 자체를 10년으로 정하는 규정이 아니다.
- Article 13(19): support period 종료일은 최소 월과 연도로 구매 시점에 명확히 표시해야 한다. 기술적으로 가능하면 제품이 지원 종료 시점에 도달했음을 사용자에게 알린다.
- Annex I Part II (2): 취약점을 지체 없이 해결/완화하고, 기술적으로 가능한 경우 새로운 security update를 functionality update와 분리.
- Annex I Part II (8): 확인된 보안 이슈를 해결하는 security update가 available하면 지체 없이 배포하고, 원칙적으로 무료 제공. 다만 tailor-made product에 대해 manufacturer와 business user가 달리 합의한 경우 예외가 있다. 업데이트에는 사용자 조치 정보를 포함한 advisory message를 동봉.
- Article 13(14): series production 제품이 CRA에 계속 부합하도록 절차를 마련하는 조항이며, 무상 업데이트 조항이 아니다.

## 3. 수정된 권고 문안

제조사는 제품의 예상 사용 기간과 합리적인 사용자 기대 등을 고려해 support period를 결정해야 하며, 원칙적으로 최소 5년을 적용한다. 예상 사용 기간이 5년 미만이면 해당 기간을 support period로 삼는다(Article 13(8)). support period 동안 제공된 security update는 발행 후 최소 10년 또는 support period 잔여 기간 중 더 긴 기간 동안 계속 이용 가능해야 한다(Article 13(9)). 지원 종료일은 구매 시점에 명확히 표시하고, 기술적으로 가능하면 종료 시 사용자에게 알린다(Article 13(19)). 확인된 보안 이슈를 해결하는 security update가 available하면 지체 없이 무상 제공하되, tailor-made product에 관한 명시적 합의 예외를 반영한다(Annex I Part II (8)). 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리한다(Part II (2)).

## 4. 서보 드라이브 제품 적용 시 구분

- support period, update availability retention, update delivery timing은 서로 다른 개념으로 문서화한다.
- 제품의 실제 예상 사용 기간과 산업용 설비 lifecycle evidence를 support-period 결정 기록에 남긴다.
- 업데이트 무료 제공 예외는 tailor-made product에 관한 manufacturer/business user agreement 조건을 확인한다.
- “workaround”를 모든 경우에 security update와 동일한 무료 제공 의무로 단정하지 말고, 실제 조치 유형 및 Annex I Part II 요구를 구분한다.
- 업데이트 배포가 모션 제어 가용성, 파라미터 보존, 안전 상태 및 복구에 미치는 영향은 제품별 검증 항목으로 둔다.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
