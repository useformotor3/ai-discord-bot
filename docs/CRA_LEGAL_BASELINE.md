# CRA 법령 기준선 — 서보 드라이브 개발자를 위한 핵심 원문 정리

**확인 기준일:** 2026-11-12  
**주요 1차 근거:** Regulation (EU) 2024/2847, Official Journal / EUR-Lex  
**법적 상태 주의:** 본 문서는 개발 검토용 요약이며 법률 자문이나 제품별 적합성 판정이 아니다. 법령 원문이 우선한다.

## 1. CRA가 다루는 제품
CRA는 EU 시장에 제공되는 'products with digital elements'에 관한 수평적 사이버보안 규정이다. 최종 제품뿐 아니라 별도로 시장에 제공되는 하드웨어·소프트웨어 구성품도 조건에 따라 범위에 들어갈 수 있다.
- 법적 근거: Article 1, Article 2, Article 3, Article 6
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 개발자 해석: 서보 드라이브라는 이름만으로 적용 여부를 결론내리지 않는다. 제품에 포함된 소프트웨어/하드웨어, 원격 데이터 처리 솔루션, EU 시장 제공 형태, 예외·특별 규정 등을 확인한다.

## 2. 단계별 적용일
Article 71(2)에 규정된 일정:
| 날짜 | 적용 내용 |
|---|---|
| 2026-06-11 | Chapter IV (Articles 35–51), 적합성평가기관 통보 관련 조항 |
| 2026-09-11 | Article 14, 제조자의 적극 악용 취약점 및 중대 보안 사고 신고 의무 |
| 2027-12-11 | 규정의 일반 적용일 |

중요: Article 69(3)은 Article 14 신고 의무가 2027-12-11 이전에 시장에 출시된 제품에도 적용될 수 있도록 별도 규정한다. 따라서 2026-09-11 이후에는 일반 적용일 전이라도 Article 14의 범위를 별도로 검토해야 한다.
근거: Articles 69(3), 71(2).
공식 자료:
- 법령 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- European Commission CRA reporting obligations: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

## 3. Article 14 — 제조자의 신고 의무
신고 대상은 모든 취약점이 아니다. CRA Article 14는 제품에 포함된 actively exploited vulnerability(실제로 악용되고 있는 취약점)와 제품 보안에 영향을 주는 severe incident(중대한 사고)를 대상으로 한다.
- 적극 악용 취약점: Article 14(1)–(2)
  - 인지 후 지체 없이, 늦어도 24시간 이내 조기 경보
  - 인지 후 지체 없이, 늦어도 72시간 이내 후속 취약점 신고
  - 시정/완화 조치가 가능해진 뒤 14일 이내 최종 보고
- 중대한 사고: Article 14(3)–(5)
  - 인지 후 지체 없이, 늦어도 24시간 이내 조기 경보
  - 인지 후 지체 없이, 늦어도 72시간 이내 사고 신고
  - 72시간 신고 후 1개월 이내 최종 보고
- 신고는 Article 16의 Single Reporting Platform을 통해 조정 CSIRT와 ENISA에 제출하는 구조다.
- 모든 취약점을 무조건 ENISA에 신고한다고 표현하지 않는다.
공식 근거:
- Regulation (EU) 2024/2847, Article 14 및 16: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- European Commission reporting page: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- ENISA SRP FAQ: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions

## 4. Annex I — 제품 속성 요구사항과 취약점 처리 요구사항
### Part I — 제품의 사이버보안 속성
위험평가를 기반으로 제품이 적절한 수준의 사이버보안을 갖도록 설계·개발·생산해야 한다. 관련 항목에는 알려진 악용 가능 취약점이 없는 상태로 시장 제공, secure-by-default, 보안 업데이트로 취약점 해결, 접근통제, 기밀성·무결성·가용성, 공격 표면 제한 등이 포함된다.
- 자동 보안 업데이트는 해당되는 경우의 요건이며, 원문에 적힌 기본 설정·사용자 통지·옵트아웃 및 연기 조건을 함께 해석한다.
- 모든 제품에 무조건 자동 업데이트가 강제된다고 단순화하지 않는다.
근거: Annex I, Part I, points (1)–(2).

### Part II — 취약점 처리 프로세스
제조자는 다음을 수행해야 한다.
1. 제품 구성요소와 취약점을 식별·문서화하고, 최소 최상위 의존성을 포함하는 기계 판독 가능한 형식의 SBOM을 작성
2. 위험에 비례해 취약점을 지체 없이 해결하며, 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리
3. 효과적이고 정기적인 보안 시험·검토 수행
4. 보안 업데이트 제공 후 수정된 취약점에 대한 정보 공개(정당한 보안 사유에 따른 지연 가능)
5. 조정된 취약점 공개(CVD) 정책 수립·시행
6. 제품 및 제3자 구성요소 취약점 신고를 용이하게 하는 연락 채널 제공
7. 업데이트의 안전한 배포 메커니즘 제공
8. 보안 업데이트를 지체 없이 배포하고, 맞춤형 제품에 대한 별도 합의 예외를 제외하고 원칙적으로 무상 제공하며 사용자 안내를 함께 제공
근거: Annex I, Part II, points (1)–(8).
공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
참고 원문 위치: Official Journal PDF, Annex I Part II, p. 69/81: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847

## 5. 지원 기간
Article 13(8)은 제조자가 제품의 예상 사용 기간과 제품의 특성 등을 고려하여 지원 기간을 결정하도록 하며, 원칙적으로 최소 5년을 요구한다. 다만 제품의 예상 사용 기간이 5년보다 짧은 경우에는 그 예상 사용 기간을 고려하는 예외가 있다.
- '무조건 모든 제품 5년'으로 단순화하지 않는다.
- 제품의 예상 사용 기간, 유사 제품, 운영 환경, 핵심 구성요소의 지원 기간 등을 고려한 합리적 근거를 기록한다.
- 지원 종료일은 사용자에게 명확하게 안내해야 한다.
근거: Article 13(8) 및 Annex II.
공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

## 6. Important product Class I/II — 서보 드라이브와 ST MCU의 구분
### 완제품 서보 드라이브
Article 7(1)은 Annex III에 열거된 제품 범주의 'core functionality'를 가진 제품을 important product로 규정한다. 따라서 '서보 드라이브'라는 명칭만으로 Class I 또는 Class II라고 분류할 수 없다. 완제품의 핵심 기능이 Annex III의 어느 기술 범주에 해당하는지와 Implementing Regulation (EU) 2025/2392의 기술 설명을 제품 기능에 대조해야 한다.
또한 Article 7(1)은 중요 제품이 다른 제품에 통합되었다는 사실만으로 통합된 제품 전체가 Article 32(2)/(3) 적합성평가 대상이 되는 것은 아니라고 명시한다.
### ST MCU 부품
Commission Implementing Regulation (EU) 2025/2392 Annex I에는 Class I category 14로 'security-related functionalities'를 갖춘 microcontrollers가 기술적으로 정의되어 있다. 정의에는 암호화, 인증, 보안 키 저장, 난수 생성, trusted execution environment 또는 다른 하드웨어 보호 기능이 포함될 수 있으며, 이러한 기능이 MCU 자체를 넘어 다른 제품·네트워크·서비스를 보호하도록 설계된 경우를 설명한다.
따라서 특정 ST MCU가 category 14에 해당하는지는 부품 번호, 기능, 제조사 문서, 기능의 목적을 확인해야 한다. 모든 ST MCU가 자동으로 Class I인 것은 아니다. MCU 구성품의 분류와 서보 드라이브 완제품의 분류는 서로 별도 판단한다.
공식 근거:
- CRA Article 7 및 Annex III: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Implementing Regulation (EU) 2025/2392, Annex I, Class I, category 14: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392

## 7. 개발 프로젝트에 적용할 때의 실무 번역
| CRA 주제 | 서보 드라이브 개발에서 확인할 항목 | 객관적 증거 예시 |
|---|---|---|
| 제품 범위/분류 | 제품 경계, 시장 제공 형태, 통신·원격 기능, 별도 판매되는 구성품 | 제품 정의서, 분류 검토서 |
| 위험평가 | 제어 명령, 파라미터, 펌웨어, 서비스 포트, 네트워크 위협 | 위협 모델, 위험평가 기록 |
| Secure by default | 초기 계정·비밀번호, 서비스 포트, 디버그 접근, 기본 통신 설정 | 초기 설정 시험, 보안 설정표 |
| 업데이트 | 서명 검증, 무결성·인증성, 실패 복구, 업데이트 전달 채널 | 부트 체인 설계, 업데이트 시험 |
| 취약점 처리 | 신고 채널, 분류·우선순위, 패치·공개·지원기간 | PSIRT 절차, 취약점 기록 |
| SBOM | MCU 펌웨어 및 소프트웨어 의존성, 오픈소스 구성 | SPDX/CycloneDX 등 SBOM |
| 신고 의무 | actively exploited vulnerability / severe incident 인지 및 24h·72h 절차 | 사고 대응 절차, 신고 기록 |
| 보안 시험 | 인증, 접근통제, 통신, 업데이트, 공격 표면, 복구 | 시험 계획서·결과서 |

## 8. 현재 검증 상태
- CRA 법령 핵심 조항과 적용 일정: 공식 원문 기준선 확인 완료
- 2025/2392의 MCU Class I category 14 기술 정의: 공식 원문 확인 완료
- 개별 서보 드라이브의 CRA 적용성/등급: 제품 사양 미제공으로 미판정
- ST MCU의 category 14 해당 여부: 정확한 부품 번호 미확정으로 미판정
- 조화표준의 최신 상태와 서보 드라이브별 적용성: 별도 조사 필요

## 9. 주요 1차 출처
1. Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
2. Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
3. European Commission — CRA reporting obligations: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
4. ENISA — Single Reporting Platform FAQ: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions
