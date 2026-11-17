# CRA 보고서 #14 정정 및 법령 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_110057754593_660202b6.md
- 원본 blob SHA: 2417779b5926f96b64c8e7f91d2baea85c7c479f
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장 | 판정 | 정정 |
|---|---|---|
| Article 11이 제조사 취약점 처리 의무를 규정 | 조항 오류 | Article 11은 General product safety. 제조사 의무는 Article 13, 세부 취약점 처리 요구는 Annex I Part II |
| CVD를 Article 11에 근거 | 조항 오류 | Annex I Part II (5)는 CVD 정책 수립·시행, Part II (6)은 취약점 제보 연락 주소 등 정보 공유 촉진 |
| 취약점 공표를 일률적으로 패치 준비 단계에서 수행 | 시점·절차 과도 단순화 | Part II (4)는 security update가 available된 후 fixed vulnerabilities의 정보 공유/공개를 규정하며, 정당한 경우 공개 지연 예외가 있다 |
| 적극 악용 취약점 및 중대한 보안 사고의 기관 신고 | 큰 방향은 맞으나 근거 누락 | Article 14가 신고 의무 및 시한을 규정한다. Article 11이 아니다 |
| Raw Text Quote가 최종 CRA 원문 | 부적합 | 인용은 제안/타협안 문구에 가까우며 최종 OJ 문언과 일치하지 않는다 |

## 2. 정확한 법적 근거

- Article 13: 제조사의 일반 의무. Article 13(2)는 제품의 사이버보안 위험평가를 요구한다.
- Annex I Part II (4): 보안 업데이트가 제공된 뒤 수정된 취약점의 설명, 영향, 심각도 및 사용자 조치 정보 등을 공유·공개. 정당한 사유가 있는 경우 공개 지연이 가능하다.
- Annex I Part II (5): “put in place and enforce a policy on coordinated vulnerability disclosure”.
- Annex I Part II (6): 제품 및 포함된 제3자 구성요소의 잠재 취약점 제보를 촉진하고 연락 주소를 제공.
- Annex II point 2: 취약점 보고·수신 및 CVD 정책을 찾을 수 있는 단일 연락 창구 정보를 제품과 함께 제공.
- Article 14: 적극 악용 취약점 및 제품 보안에 영향을 주는 중대한 사고의 신고. Article 14(2)(a)는 인지 후 24시간 이내 early warning, (b)는 72시간 이내 vulnerability notification, (c)는 시정/완화 조치가 이용 가능해진 후 14일 이내 final report를 규정한다. 중대한 사고는 Article 14(4)의 24h/72h 및 1개월 final report 체계를 따른다.
- Article 16: 단일 신고 플랫폼 및 CSIRT/ENISA 전파 절차.

## 3. 수정된 권고 문안

제조사는 제품 및 포함된 제3자 구성요소의 취약점을 식별·문서화하고, CVD 정책을 마련해 시행하며, 제보 연락 주소를 제공해야 한다(Annex I Part II (1), (5), (6)). 수정된 취약점 정보의 공개는 Part II (4)의 시점과 예외를 따른다. 적극 악용 취약점 및 중대한 제품 보안 사고는 Article 14의 신고 요건과 시한을 별도로 적용한다. CVD 운영과 규제기관 신고는 서로 다른 프로세스이므로 하나로 합치지 않는다.

## 4. 제품 적용 시 구분

- PSIRT, 접수 포털, SLA, CVE/CVSS 운영은 법령이 특정 솔루션을 지명한 것이 아니라 요구를 충족하기 위한 구현 선택이다.
- 보고 대상은 “모든 발견 취약점”과 “actively exploited vulnerability”가 다르다. Article 14의 강제 신고 트리거를 모든 취약점 제보로 확대하지 않는다.
- 제품별 CRA 적용 범위, 제조자 지위, 제품 분류 및 신고 담당자·연락 창구를 별도 확인한다.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
