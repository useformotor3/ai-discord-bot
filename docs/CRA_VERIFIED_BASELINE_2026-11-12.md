# CRA 1차 공식 근거 기준선 — 서보 드라이브 적용 검토

**기준일:** 2026-11-12  
**법령:** Regulation (EU) 2024/2847 (Cyber Resilience Act)  
**주요 원문:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847  
**검증 상태:** 아래의 법령 문구/위치는 EUR-Lex 공식 원문과 대조. 제품별 적용성·법률 해석은 별도 검토 필요.

## 1. 적용 일정

- CRA 일반 적용일: 2027-12-11.
- Article 14 제조자 신고 의무 적용일: 2026-09-11.
- Chapter IV (Articles 35–51) 적용일: 2026-06-11.
- 기준일 현재(2026-11-12) Article 14 신고 의무는 이미 적용 중이며, 나머지 일반 CRA 의무는 2027-12-11 적용 예정.
- 근거: Article 71(2), Commission CRA reporting obligations page.

공식 출처:
- EUR-Lex, Article 71: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- European Commission, CRA Reporting obligations (last update 2026-09-11): https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

## 2. 중요 조항 — 정확한 조항 위치와 주의점

| 주제 | 공식 근거 | 정확한 의미 / 개발 적용 방향 | 흔한 오해 방지 |
|---|---|---|---|
| 위험평가 | Article 13(2)–(4) | 의도된 용도, 합리적으로 예견 가능한 사용, 운영 환경, 보호 자산, 제품 예상 사용기간을 고려해 위험평가하고 기술문서에 포함. 적용되지 않는 필수 요구사항은 명확한 정당화 포함 | 일반 IT 위협 목록만 복사하면 충분하다는 뜻이 아님 |
| 제3자 구성요소 | Article 13(5)–(7) | 제3자/오픈소스 구성요소 통합 시 실사(due diligence), 취약점 발견 시 구성요소 유지관리자 통보 및 처리, 관련 사이버보안 사항 기록 | 단순히 SBOM 파일을 만들었다고 due diligence가 완료되는 것은 아님 |
| 지원기간 | Article 13(8) | 예상 사용기간, 사용자 기대, 제품 특성/의도된 목적, 관련 EU 법령 등을 고려해 지원기간 결정. 원칙적으로 최소 5년이나, 제품 예상 사용기간이 5년 미만이면 예상 사용기간에 해당 | “모든 제품 무조건 5년 이상”으로 단순화 금지. 예외 문장 포함 |
| 지원기간 증거 | Article 13(8), Annex VII(4) | 지원기간 결정에 고려한 정보를 기술문서에 포함 | 단순 제품 웹페이지 표기만으로 기술문서 의무 대체 안 됨 |
| 보안 업데이트 보관 | Article 13(9) | 지원기간 중 사용자에게 제공된 각 보안 업데이트는 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능해야 함 | 지원기간 종료 시 모든 패치 다운로드를 즉시 제거해도 된다는 뜻이 아님 |
| SBOM/구성요소 식별 | Annex I Part II(1) | 취약점 및 구성요소를 식별·문서화. SBOM은 일반적으로 사용되고 기계 판독 가능한 형식이며 최소 최상위 의존성을 포함 | “모든 제품에서 모든 종속성까지 무조건 공개”라는 뜻이 아님 |
| SBOM 공개 | Recital 77, Annex VII(8) | Recital 77은 제조자가 SBOM을 공개할 의무가 없다고 설명. Annex VII(8)은 시장감시당국의 정당한 요청 등 조건에 따른 SBOM 제출을 규정 | SBOM 작성/보유와 일반 대중 공개를 혼동하지 말 것 |
| 보안 업데이트와 기능 업데이트 분리 | Annex I Part II(2) | 기술적으로 가능한 경우 새로운 보안 업데이트는 기능 업데이트와 별도로 제공 | 절대적·무조건적 분리 의무라고 쓰지 말 것. “where technically feasible” 조건 필수 |
| 보안 업데이트 무상 제공 | Annex I Part II(8) | 식별된 보안 문제를 해결하는 보안 업데이트가 있으면 지체 없이 배포하고, 맞춤형 제품 관련 제조자-사업 사용자 간 달리 합의한 경우를 제외하고 무상 제공 | 기능 업데이트 전부 무료라는 뜻이 아님 |
| Secure by default | Annex I Part I(2)(b) | 위험평가 및 해당 요건에 따라 기본 보안 구성으로 시장 출시. 맞춤형 제품에 대한 제조자-사업 사용자 간 합의 예외 포함. 원상태 복원 가능성 포함 | 모든 인터페이스에서 무조건 비밀번호 변경만 요구하는 단일 조항으로 축소 금지 |
| 접근통제 | Annex I Part I(2)(d) | 적절한 통제수단(인증, 신원/접근관리 포함)으로 비인가 접근 방지 및 가능한 비인가 접근 보고 | JTAG 잠금만으로 전체 접근통제 요구 충족이라고 할 수 없음 |
| 공격표면 | Annex I Part I(2)(j) | 외부 인터페이스를 포함해 공격표면 제한 | 실제 제품 인터페이스/서비스 인벤토리와 위험평가로 적용 필요 |
| CVD | Annex I Part II(5)–(6), Article 13(8) | 조율된 취약점 공개 정책을 수립·집행하고 신고를 촉진하는 연락 주소 제공 | 정책 문서만 있고 실제 접수/처리 운영이 없으면 충분하다고 보기 어려움 |
| 기술문서 | Article 31, Annex VII | 제품 설명, 아키텍처, 취약점 처리 프로세스, SBOM, CVD, 보안 업데이트 배포, 위험평가, 지원기간 근거, 표준/시험보고서 등을 해당성에 따라 포함 | Annex VII를 단순 제품 사용자 매뉴얼로 오해 금지 |
| 제조자 신고 | Article 14 | 적극적으로 악용되는 취약점 및 제품 보안에 영향을 주는 중대한 사고에 대해 조기경보 24시간, 72시간 이내 통지, 최종보고 기한 적용 | 모든 일반 취약점 발견을 Article 14에 즉시 신고하는 것으로 혼동 금지. 신고 대상은 조항상 적극 악용 취약점/중대한 사고 |
| 신고 경로 | Article 14, 16 | Single Reporting Platform을 통해 CSIRT 지정 조정기관과 ENISA로 통지 | 내부 고객지원/메일 접수만으로 CRA 법정 신고를 대체할 수 없음 |

## 3. 서보 드라이브 개발자에게 중요한 적용 방향

다음은 법령을 서보 드라이브에 연결하는 설계·개발 작업 후보이며, 그 자체가 제품 적합성 결론은 아니다.

1. 제품 경계와 의도된 용도: 드라이브 본체, 제어보드, MCU, 통신 모듈, PC 엔지니어링 툴, 업데이트 툴, 클라우드/원격 서비스, 외부 통신 인터페이스를 식별.
2. 위험평가: EtherCAT/PROFINET/EtherNet/IP 등 통신, 파라미터 쓰기, 펌웨어 업데이트, 부트 체인, 디버그, 키/인증서, 공급망 구성요소를 자산·공격경로로 분석.
3. 안전과 보안 인터페이스: 보안 업데이트가 토크/속도 제어, 안전기능, 실시간성, 인증된 펌웨어와 상호작용하는지 확인. CRA가 SIL 인증을 대신하거나 안전 표준 요구사항을 대체한다고 가정하지 말 것.
4. 업데이트 설계: 서명 검증, 무결성, 인증, anti-rollback, 복구/전원차단 복원성, 키 관리, 버전/릴리스 추적, 보안 업데이트와 기능 변경 분리 가능성.
5. 취약점 운영: 공개 연락처, 접수·분류·조사·패치·고객 통지·Article 14 판단 및 신고 흐름.
6. 기술문서: 요구사항 ID → CRA 조항 → 제품 적용성 → 설계 결정 → 구현 → 시험 → 증거 링크를 추적.

## 4. ST MCU 공식 자료 — 제품군 수준 기준선

**STMicroelectronics AN5156, “Introduction to security for STM32 MCUs”, Rev 14, June 2026**
- 공식 페이지: https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html
- 공식 PDF: https://www.st.com/resource/en/application_note/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.pdf
- 적용 제품군 목록에 STM32C0/C5/F0/F1/F2/F3/F4/F7/G0/G4/H5/H7/L0/L1/L4/L4+/L5/N6/U0/U3/U5/WB/WBA/WB0/WL이 포함.
- 문서의 목차 및 설명은 메모리 보호, 디버그 포트 보호, 부트 보호, 시스템 모니터링, Secure Boot, Secure Firmware Update, Secure Firmware Install, TRNG, AES/SAES, PKA, HASH 등 기능군을 다룸.
- ST는 제품군별 보안 기능 차이를 별도 표로 제시하므로, AN5156에 어떤 기능이 언급된다는 이유만으로 모든 STM32에 해당 기능이 있다고 가정하지 않는다.
- 정확한 MCU 부품번호가 없으므로 현재는 기능 적용 가능성을 판단할 수 없다. 다음 단계에서 MCU 전체 부품번호와 실리콘 리비전, 패키지/메모리 옵션, 보안 상태/Option Bytes를 확인해야 한다.

관련 ST 자료:
- STM32Trust: https://www.st.com/content/st_com/en/ecosystems/stm32trust.html
- AN5544 SBSFU on STM32CubeWL: https://www.st.com/resource/en/application_note/an5544-integration-guide-of-sbsfu-on-stm32cubewl-including-kms-stmicroelectronics.pdf
- ST Wiki Secure Boot/SFU: https://wiki.st.com/stm32mcu/wiki/Security:Introduction_to_Secure_boot_and_Secure_firmware_update

## 5. 검증된 사실과 미해결 사항 구분

### 원문으로 확인한 사실
- Article 13(8)은 지원기간 산정 기준 및 최소 5년 원칙과 5년 미만 예상 사용기간 예외를 규정.
- Annex I Part II(1)은 최소 최상위 의존성을 포함한 기계 판독 가능 SBOM을 규정.
- Recital 77은 SBOM의 일반 공개 의무가 없음을 명시.
- Annex VII(8)은 시장감시당국의 정당한 요청 등 조건에서 SBOM 제공을 규정.
- Annex I Part II(2)는 기술적으로 가능한 경우 보안 업데이트와 기능 업데이트를 분리하도록 함.
- Annex I Part II(8)은 보안 업데이트 무상 제공 원칙과 맞춤형 제품 관련 합의 예외를 규정.
- Article 14는 적극 악용 취약점 및 중대한 사고의 신고 체계를 규정.
- Article 14 적용일은 2026-09-11, CRA 일반 적용일은 2027-12-11.
- ST AN5156 Rev 14 (June 2026)는 STM32 MCU 보안 기능에 대한 공식 자료.

### 아직 결론 내릴 수 없는 사항
- 특정 서보 드라이브 모델이 CRA의 제품 범위에 해당하는지 여부: 제품 기능/의도된 용도/원격 데이터 처리/시장 제공 형태 확인 필요.
- 제품이 CRA Annex III 중요 제품 Class I/II 또는 Annex IV critical product인지 여부: 제품 분류 정의와 실제 핵심 기능을 대조해야 함. 서보 드라이브라는 이유만으로 등급을 단정하지 않는다.
- 사용 중인 STM32의 정확한 보안 기능/부트 구조/키 저장 옵션: 전체 부품번호 미확인.
- 각 과거 AI 조사 파일의 주장·인용 정확성: 별도 전수 대조 필요.

## 6. 근거 URL 목록

1. EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
2. Commission CRA reporting obligations: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
3. Commission CRA implementation: https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation
4. ST AN5156 Rev 14: https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html
5. ST STM32Trust: https://www.st.com/content/st_com/en/ecosystems/stm32trust.html
6. ST AN5544: https://www.st.com/resource/en/application_note/an5544-integration-guide-of-sbsfu-on-stm32cubewl-including-kms-stmicroelectronics.pdf

**주의:** 이 기준선은 법령·공식 제조사 자료의 첫 번째 검증된 기준점이다. 제품별 법적 적용성 판단, 표준 최신성, 세부 설계 적합성, 적합성 평가를 완료했다는 뜻은 아니다.
