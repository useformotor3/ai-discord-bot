# CRA 보고서 #13 정정 및 취약점 처리·CVD 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_104039226133_f4dc7a3f.md
- 원본 blob SHA: 7523b68c1537b6ed4d2de197eeb6e5bd4698ea2e
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Article 11이 제조사 취약점 처리/CVD 의무 | 조항 오류 | Article 11은 General product safety. 제조사 의무는 Article 13, 취약점 처리 세부 요구는 Annex I Part II |
| Annex I Part II 번호와 raw quote | 구조 및 문언 오류 | 최종 OJ Part II는 (1) 식별·문서화/SBOM, (2) 지체 없는 취약점 조치, (3) 정기 보안 시험·검토, (4) 수정 취약점 공개, (5) CVD 정책, (6) 제보 연락 주소/정보 공유, (7) 안전한 업데이트 배포, (8) 적시·무상 보안 업데이트 |
| 모든 제보를 익명으로 접수해야 함 | 직접 법적 요구로 확인 불가 | 제보 채널 및 연락 주소는 요구되지만, 모든 제품에 익명 접수를 의무화한다고 단정하지 않는다 |
| 패치 준비 시점과 동시에 반드시 공개 | 과도한 단정 | Part II (4)는 보안 업데이트가 이용 가능해진 뒤 수정 취약점 정보를 공유·공개하도록 하며, 정당한 경우 공개 지연 예외를 허용 |
| 산업용 서보 드라이브는 모두 Important Class I/II | 제품 분류 오류 | 중요 제품 분류는 Annex III의 구체 범주/제품 기능에 따라 판단. 모든 servo drive를 자동으로 Class I/II로 분류할 수 없다 |
| actively exploited vulnerability 및 severe incident 신고를 Article 11에 연결 | 조항 오류 | Article 14가 의무 신고 및 24h/72h/final report 기한을 규정 |

## 2. 정확한 법적 근거

- Article 13(2)–(3): 제품의 의도된 목적, 합리적으로 예견 가능한 사용, 운영 환경 및 보호 자산을 반영한 사이버보안 위험평가와 문서화.
- Article 13(8): 지원 기간 동안 제품 및 구성요소의 취약점을 Annex I Part II에 따라 효과적으로 처리. 지원 기간은 예상 사용 기간 등을 고려하고 원칙적으로 최소 5년, 예상 사용 기간이 더 짧으면 그 기간.
- Annex I Part II (1): 취약점 및 제품 구성요소 식별·문서화, SBOM 포함.
- Part II (2)–(3): 취약점 지체 없는 해결/완화 및 정기적인 보안 시험·검토.
- Part II (4): 보안 업데이트가 이용 가능해진 후 수정 취약점 정보를 공개. 정당한 사유가 있으면 공개 지연 가능.
- Part II (5)–(6): CVD 정책 수립·시행, 취약점 제보를 위한 연락 주소 등 정보 공유 촉진.
- Part II (7)–(8): 안전한 업데이트 배포, 해당되는 경우 자동 배포, 적시에 무상 보안 업데이트 제공(맞춤형 제품에 대해 달리 합의한 경우 예외).
- Article 14: actively exploited vulnerability 및 severe incident 신고. actively exploited vulnerability의 early warning은 인지 후 24시간, vulnerability notification은 72시간, final report는 corrective/mitigating measure가 available된 후 14일 이내. severe incident는 Article 14(4)의 24h/72h/1개월 체계.
- Article 16: ENISA single reporting platform 및 CSIRT/ENISA 전파 절차.

## 3. 제품 분류 관련 정정

CRA의 기본 필수 사이버보안 요구사항은 CRA 적용 범위에 속하는 제품에 위험평가 기반으로 적용된다. Annex III의 Important products Class I/II 분류는 별도 분류 및 conformity assessment 절차와 관련되며, “산업용 서보 드라이브”라는 명칭만으로 자동 분류할 수 없다. 구체 제품의 주된 기능, 구성요소 및 Annex III의 범주 정의를 확인해야 한다.

## 4. 수정된 권고 문안

제조사는 제품 및 구성요소의 취약점을 식별·문서화하고, 위험에 비례해 지체 없이 처리하며, 정기적인 보안 시험·검토를 수행해야 한다(Annex I Part II (1)–(3)). CVD 정책을 마련·시행하고 취약점 제보 연락 주소를 제공해야 한다(Part II (5)–(6)). 수정된 취약점의 공개는 Part II (4)의 시점과 예외를 따른다. 적극 악용 취약점 및 중대한 제품 보안 사고의 규제기관 신고는 Article 14를 별도 적용한다. 익명 제보, 특정 PSIRT 도구, 공개 시점의 일률적 동시성 및 서보 드라이브의 Annex III 분류를 법령이 직접 요구한다고 단정하지 않는다.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
