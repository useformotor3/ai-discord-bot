# CRA 보고서 #10 정정 및 지원 기간·취약점 처리 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_102121957148_dd6c7aac.md
- 원본 blob SHA: 1457bf4c03af61e5c6d9e5ca22397d0dc7c37401
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Raw Text Quote가 최종 CRA 직접 인용 | 비문언 인용 | 해당 문장은 Article 13(8) support period와 Annex I Part II (8) free security update 내용을 합쳐 요약한 문구이며 최종 OJ의 verbatim quote가 아니다 |
| “제품 전체 수명 또는 최소 5년 중 더 긴 기간” | 법적 문언 단순화 | support period는 expected product lifetime 등 relevant factors를 반영하고 원칙적으로 최소 5년. expected use period가 5년 미만이면 해당 expected use period |
| “5년 동안 무상 패치”를 Article 13(8)에 귀속 | 조항 혼합 | Article 13(8)은 support period 산정, free security update delivery는 Annex I Part II (8) |
| CVD를 취약점 수명주기 전체와 동일시 | 개념 혼합 | CVD policy는 vulnerability handling의 한 항목인 Annex I Part II (5). SBOM, remediation, testing, disclosure, contact address, secure update distribution은 별도 point |
| Article 11을 CRA 제조사 의무 근거로 인용 | 조항 오류 | 제조사 의무는 Article 13. Article 11은 General product safety |

## 2. 정확한 법적 근거

- Article 13(8): manufacturer는 expected product lifetime, reasonable user expectations, product nature/intended purpose 및 relevant EU law 등을 고려해 support period를 정한다. 원칙적으로 최소 5년이며, expected use period가 5년 미만이면 해당 expected use period.
- Article 13(9): support period 중 제공된 각 security update는 발행 후 최소 10년 또는 support period 잔여 기간 중 더 긴 기간 동안 계속 이용 가능해야 한다.
- Annex I Part II (1): 취약점 및 제품 구성요소 식별·문서화, SBOM 포함.
- Part II (2)–(3): 취약점 지체 없는 해결/완화 및 정기 보안 시험·검토.
- Part II (4): security update가 available된 뒤 fixed vulnerability 정보 공유/공개, 정당한 지연 예외.
- Part II (5): CVD policy 수립·시행.
- Part II (6): 취약점 제보 연락 주소 및 정보 공유 촉진.
- Part II (7): 보안 업데이트의 안전한 배포.
- Part II (8): identified security issues를 해결하는 security update가 available하면 지체 없이 배포하고 무료 제공. tailor-made product에 대해 manufacturer와 business user가 달리 합의한 경우 예외.

## 3. 수정된 권고 문안

제조사는 제품의 expected lifetime 및 relevant factors를 반영해 support period를 결정하고 원칙적으로 최소 5년을 보장한다(Article 13(8)). support period 동안 제공한 각 security update는 Article 13(9)의 availability retention 요건을 따른다. 확인된 보안 이슈를 해결하는 security update가 available하면 Annex I Part II (8)에 따라 지체 없이 무상 제공하되 tailor-made product의 명시적 합의 예외를 반영한다. CVD policy는 Part II (5)의 별도 의무이며, SBOM·취약점 조치·시험·공개·연락 주소·안전한 배포 요구와 혼합하지 않는다.

## 4. 서보 드라이브 적용 시 구분

- support period와 update availability retention, free update delivery, CVD policy를 각각 별도 traceability 항목으로 관리.
- 장기 산업용 설비의 expected product lifetime을 evidence로 산정하되 CRA가 모든 제품에 일률적인 10년 support period를 부과한다고 표현하지 않는다.
- 보안 패치와 기능 업데이트 분리는 Annex I Part II (2)의 technically feasible 조건을 함께 기록.
- 패치 적용의 모션 파라미터/통신/안전 기능 영향은 제품 검증 항목이며, 법령 인용과 분리.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
