# CRA 공식 법령 기준선 — 서보 드라이브 적용 검토

**기준일:** 2026-11-13  
**법령:** Regulation (EU) 2024/2847 (Cyber Resilience Act)  
**주요 원문:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847  
**검증 상태:** 아래의 법령 문구/위치는 EUR-Lex 공식 원문과 대조. 제품별 적용성·법률 해석은 별도 검토 필요.

## 1. 적용 일정

- CRA 일반 적용일: 2027-12-11.
- Article 14 제조자 신고 의무 적용일: 2026-09-11.
- Chapter IV (Articles 35–51) 적용일: 2026-06-11.
- 기준일 현재(2026-11-13) Article 14 신고 의무는 이미 적용 중이며, 나머지 일반 CRA 의무는 2027-12-11 적용 예정.
- 근거: Article 71(2), Commission CRA reporting obligations page.

공식 출처:
- EUR-Lex, Article 71: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- European Commission, CRA Reporting obligations (last update 2026-09-11): https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

## 2. 중요 조항 — 정확한 조항 위치와 주의점

| 주제 | 공식 근거 | 정확한 의미 / 개발 적용 방향 | 흔한 오해 방지 |
|---|---|---|---|
| 위험평가 | Article 13(2)–(4) | 의도된 용도, 합리적으로 예견 가능한 사용, 운영 환경, 보호 자산, 제품 예상 사용기간을 고려해 위험평가하고 기술문서에 포함. 적용되지 않는 필수 요구사항은 명확한 정당화 포함 | 일반 IT 위협 목록만 복사하면 충분하다는 뜻이 아님 |
| 제3자 구성요소 | Article 13(5)–(7) | 제3자/오픈소스 구성요소 통합 시 실사(due diligence), 통합 구성요소에서 취약점을 식별한 경우 해당 구성요소 제조사/유지관리 주체에 신고하고 제품 측에서 처리·완화, 관련 사이버보안 사항의 체계적 문서화 | Article 13(6)의 명시적 신고 방향은 제품 제조사 → 구성요소 제조사/유지관리 주체다. 모든 공급자가 상위 제조사에 자동 통지해야 한다는 일반 의무로 역전하지 않는다. |
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
| 수정 취약점 공개 | Annex I Part II(4) | 보안 업데이트를 제공한 뒤 수정된 취약점에 관한 정보를 공유·공개한다. 공개 지연이 보안상 이익보다 위험을 키우는 경우 정당한 지연 예외가 있다. | 모든 취약점을 즉시 공개하는 일반 의무가 아니다. 수정 업데이트 제공 시점 및 예외를 함께 판단한다. |
| CVD 정책 | Annex I Part II(5), Article 13(8) | 조정된 취약점 공개 정책을 수립·집행하고 내부·외부 신고 취약점의 처리·시정 절차를 운영한다. | 정책 문서만이 아니라 실제 접수·분류·처리 절차가 필요하다. |
| 취약점 신고 연락처 | Annex I Part II(6), Annex II(2), Article 13(17) | 취약점 정보 공유를 촉진하고 취약점 신고 연락 주소 및 사용자에게 제공할 단일 연락 창구를 마련한다. | CVD 정책(Part II(5)), 취약점 신고 연락처(Part II(6)), 사용자 정보(Annex II(2))를 하나의 의무로 합치지 않는다. |
| 안전한 업데이트 배포 | Annex I Part II(7) | 보안 업데이트를 안전하게 배포하는 메커니즘을 마련한다. | 특정 암호 알고리즘·서명 구조·부품을 법령이 보편적으로 지정한다고 단정하지 않는다. |
| 기술문서 | Article 31, Annex VII | 제품 설명, 아키텍처, 취약점 처리 프로세스, SBOM, CVD, 보안 업데이트 배포, 위험평가, 지원기간 근거, 표준/시험보고서 등을 해당성에 따라 포함 | Annex VII를 단순 제품 사용자 매뉴얼로 오해 금지 |
| 제조자 신고 | Article 14(1)–(4) | 적극 악용 취약점과 제품 보안에 영향을 주는 심각한 사고를 별도 트랙으로 판단한다. 두 트랙 모두 24시간 조기경보 및 72시간 신고가 적용되며 최종보고 기한은 사건 유형별로 다르다. | 모든 일반 취약점 발견이 신고 대상은 아니다. 적극 악용 취약점 최종보고는 시정/완화 조치가 가능해진 뒤 14일 이내, 심각한 사고 최종보고는 사고 신고 후 1개월 이내로 구분한다. |
| 사용자 통지 | Article 14(8) | 신고 대상 사건에서 영향을 받는 사용자 및 적절한 경우 모든 사용자에게 통지한다. 적절한 경우 구조화된 기계 판독 가능 형식으로 정보를 제공한다. | 모든 취약점 공지에 자동·기계 판독 가능 형식을 보편 적용하는 의무가 아니다. Annex I Part II(1)의 SBOM 기계 판독 가능 형식과도 구분한다. |
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


## 4.1 TI MCU 공식 기술자료 — 비교 기준 예시 (ST와 동급 판정 아님)

**Texas Instruments MSPM0G3529-Q1**
- 공식 데이터시트: https://www.ti.com/lit/ds/symlink/mspm0g3529-q1.pdf
- 문서 번호/리비전: SLASFO2B, November 2024, revised October 2025.
- Cortex-M0+ 최대 80 MHz, 최대 512 KB Flash(ECC), 128 KB SRAM(첫 64 KB ECC/parity 보호), dual-bank flash/address swap.
- 데이터시트의 보안 관련 기능: AES-128/256 가속(GCM/GMAC, CCM/CBC-MAC, CBC, CTR), 최대 4개 AES 키 보관을 위한 secure key storage, flexible flash/code-data firewalls, TRNG.
- 데이터시트에는 secure boot 및 secure in-field firmware update 지원을 기술하고 있다. 다만 구현 방식, 보호 범위, 구성 조건은 Technical Reference Manual 및 SDK 구현 문서를 확인해야 한다.
- 해당 부품은 Q1 자동차 등급 제품이다. 이를 산업용 서보 드라이브의 적합성/실시간 성능/안전 인증 대체로 해석하지 않는다.

**TI application note — Cybersecurity Enablers in MSPM0 MCUs**
- 공식 PDF: https://www.ti.com/lit/an/slaae29a/slaae29a.pdf
- SLAAE29A, January 2023, revised December 2025.
- MSPM0 제품군의 secure boot, secure storage, flash write/read-execute/IP protection, secure key storage, cryptographic acceleration, TRNG, device-specific capability matrix를 설명.
- 문서 자체가 일부 기능은 일부 MSPM0 device에서만 제공된다고 명시한다. 따라서 정확한 TI part number와 해당 문서의 capability matrix를 확인해야 한다.

**TI MSPM0G3529-Q1와 ST 비교 시 주의**
- ST AN5156은 광범위한 STM32 제품군을 다루는 보안 개요/기능표이며, TI SLAAE29A도 MSPM0 제품군의 기능 매트릭스다. 두 문서를 나란히 놓고 “모든 ST/TI MCU가 동일 기능”이라고 비교할 수 없다.
- 비교는 정확한 STM32 주문 코드와 TI 주문 코드, 데이터시트/Reference Manual revision, 보안 상태 설정, SDK 버전, 실제 boot/update implementation을 같은 항목으로 대조해야 한다.
- 현재 ST 사용 부품번호가 미확정이므로 TI는 비교 기준 예시로만 기록하며, 성능/비용/기능 동등성 결론은 보류한다.


## 2.1 #43–#52 수동 감사에서 재확인한 정정 기준

| 주제 | 정본 조항 | 통합 문서에서 반드시 지킬 해석 |
|---|---|---|
| 중요 제품 분류 | Article 7, Annex III, Implementing Regulation (EU) 2025/2392 | 산업용·네트워크 연결·모션 제어 제품이라는 이유만으로 서보 드라이브를 Class I/II로 자동 분류하지 않는다. 제품 전체의 핵심 기능과 기술 설명을 확인한다. |
| 적합성 평가 | Article 32 | Article 24는 오픈소스 소프트웨어 스튜어드 관련 조항이다. 적합성 평가 경로는 Article 32를 기준으로 한다. |
| 접근통제 | Annex I Part I point 2(d) | 적절한 무단 접근 방지 통제와 가능한 무단 접근 보고를 요구한다. RBAC, MFA, 최소 권한, 고유 자격증명 등은 위험기반 구현 선택으로 구분한다. |
| 수정 취약점 공개 | Annex I Part II point 4 | 보안 업데이트 제공 후 수정된 취약점 정보를 공개하며 정당한 지연 예외를 고려한다. 모든 취약점 즉시 공개로 확대하지 않는다. |
| CVD 정책 / 신고 연락처 | Annex I Part II points 5 and 6 | 정책 수립·집행과 연락 주소 제공은 서로 다른 항목이다. |
| 안전한 업데이트 배포 / 무상 제공 | Annex I Part II points 7 and 8 | 안전한 배포와 원칙적 무상 제공을 구분한다. 맞춤형 제품에 대해 제조자와 사업 사용자가 달리 합의한 예외를 누락하지 않는다. |
| 지원기간 / 업데이트 보존 | Article 13(8) / Article 13(9) | 지원기간은 예상 사용기간 등을 반영하고 최소 5년 원칙의 예외를 포함한다. 지원기간 중 제공한 각 보안 업데이트는 발행 후 10년 또는 남은 지원기간 중 더 긴 기간 제공한다. |
| 구성요소 취약점 보고 | Article 13(6) | 제품 제조사가 통합 구성요소 취약점을 식별한 경우 구성요소 제조사/유지관리 주체에 보고하는 방향을 유지한다. |
| 기계 판독 가능 사용자 통지 | Article 14(8) | 적극 악용 취약점 또는 심각한 제품 보안 사고의 사용자 통지에 대해 “where appropriate” 조건으로 적용한다. 일반 보안 공지의 포괄 의무가 아니다. |

## 2.2 한국어 용어·표현 통일

- coordinated vulnerability disclosure policy: **조정된 취약점 공개 정책(CVD 정책)**
- actively exploited vulnerability: **적극 악용되는 취약점**
- severe incident affecting the security of the product: **제품 보안에 영향을 미치는 심각한 사고**
- machine-readable format: **기계 판독 가능 형식**
- support period: **지원기간**
- security update: **보안 업데이트**
- core functionality: **핵심 기능**
- conformity assessment: **적합성 평가**

법령명·공식 문서명·조항 번호·정확한 원문 인용은 영어 원문을 유지하고, 설명과 판단은 한국어로 작성한다.


## 2.3 #13–#42 감사에서 반복 확인한 정정 규칙

다음 항목은 #13–#42의 연속 감사에서 반복적으로 발견된 조항 혼동·과장이다. 이후 보고서·매뉴얼·설계 매트릭스 작성 시 이 표를 공통 검토 기준으로 사용한다.

| 쟁점 | 정확한 기준 | 금지할 오해·표현 |
|---|---|---|
| 제조사 일반 의무와 신고 | 제조사 일반 의무는 Article 13, 법정 취약점/사고 신고는 Article 14 | Article 11을 제조사 취약점 신고 또는 무상 업데이트의 근거로 사용 |
| 지원기간 | Article 13(8): 최소 5년 원칙, 단 예상 사용기간이 5년 미만이면 그 예상 사용기간 | “예상 수명과 5년 중 짧은 기간”을 무조건 적용하거나 예외 누락 |
| 업데이트 가용성 | Article 13(9): 지원기간 중 제공한 각 보안 업데이트를 발행 후 10년 또는 남은 지원기간 중 더 긴 기간 제공 | 지원기간 자체가 10년이라고 표현 |
| 무상 보안 업데이트 | Annex I Part II(8), 맞춤형 제품 관련 제조자-사업 사용자 합의 예외 | Annex I Part I 또는 Article 11로 오기, 예외 없이 모든 계약에 무조건 무료라고 표현 |
| 취약점 처리 항목 | Annex I Part II(1)–(8) 각각의 목적을 분리 | Part I(2)와 Part II를 혼합하거나 CVD/연락처/공개/배포/무상 업데이트를 하나의 조항으로 합침 |
| CVD/연락처/공개 | Part II(4)=수정 취약점 공개, (5)=CVD 정책, (6)=신고 연락처·정보 공유, (7)=안전한 업데이트 배포, (8)=지체 없는 원칙적 무상 업데이트 | (4)–(8)을 모두 “일반 보안 공지”로 단순화 |
| 보안 기본값/접근/공격표면 | Annex I Part I(2)(b)=secure-by-default, (d)=접근통제, (j)=공격표면 제한 | 첫 접속 비밀번호 변경, RBAC, MFA, JTAG 잠금, 모든 포트 비활성화를 보편적 직접 의무로 단정 |
| 무결성/기밀성/데이터 최소화 | Annex I Part I(2)(e)=기밀성, (f)=무결성, (g)=데이터 최소화, (h)=가용성/DoS, (i)=연결된 기기·네트워크 영향 | 서로 다른 하위 항목의 번호와 문언을 교차 배정 |
| 사용자 지침과 기술문서 | 사용자 정보·지침은 Article 13(18) 및 Annex II(1)–(9); 기술문서는 Article 31 및 Annex VII | Annex II를 기술문서로 부르거나 Annex II를 Part I/II로 나눔 |
| 데이터·설정 영구 제거 기능 | Annex I Part I point 2(m) | 해당되는 제품은 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 제공하고, 다른 제품/시스템으로 이전 가능한 경우 안전하게 이전하도록 한다. | 특정 NAND/EEPROM 소거 방식·알고리즘을 법령이 직접 지정한다고 단정하지 않는다. 제품의 저장 데이터/설정과 위험평가를 확인한다. |
| 안전한 폐기 사용자 지침 | Annex II point 8(d), Article 13(18) | 안전한 제품 폐기 및 사용자 데이터의 안전한 제거 방법에 관한 상세 지침/정보를 제공한다. | Annex II 8(d)의 사용자 지침 의무와 Annex I Part I 2(m)의 제품 기능 결과 요구를 혼합하거나 어느 하나를 누락하지 않는다. |
| 제품 분류 | Article 7, Annex III 및 Implementing Regulation (EU) 2025/2392의 핵심 기능/기술 설명 | 산업용/서보 드라이브/PLC라는 명칭만으로 Class I/II 단정 |
| 구현 기술 | Secure Boot, TPM/SE, 디지털 서명, A/B bank, anti-rollback, zero-downtime, hot-patch, 강제 비밀번호 변경 등은 해당 법령 문언에 별도 명시되지 않은 한 위험기반 설계 후보 | 구체 기술 선택을 CRA의 보편적 명문 의무로 표현 |
| 신고 기한 | Article 14: 적극 악용 취약점과 심각한 사고의 신고 트랙 및 최종 보고 기한 구분 | 24h/72h만 제시하고 최종 기한을 누락하거나 모든 취약점 신고로 확대 |
| 과징금 | Article 64(2): EUR 15m 또는 2.5%; Article 64(3): EUR 10m 또는 2% — 해당 위반 유형에 따라 적용 | 15m/3% 등 서로 다른 위반 트랙의 수치 혼합 |

이 정정 규칙은 법령 조항을 정확히 쓰기 위한 공통 기준이다. 실제 제품에 적용되는지, 설계 통제가 충분한지, 시험이 통과했는지는 별도 제품 증거로 판단한다.


## 2.4 데이터·설정 제거와 안전한 폐기 — #38/#53 재검증으로 보완

CRA의 데이터 제거 관련 요구는 두 개의 별도 근거로 관리한다.

1. **제품 기능 결과:** Annex I Part I point 2(m)는 해당되는 제품에 대해 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 제공하도록 한다. 데이터가 다른 제품/시스템으로 이전될 수 있는 경우 안전한 이전도 요구한다.
2. **사용자 지침:** Annex II point 8(d)는 제품의 안전한 폐기와 사용자 데이터의 안전한 제거 방법에 관한 상세 지침 또는 해당 지침으로 연결되는 정보를 제공하도록 한다. Article 13(18)은 Annex II 사용자 정보·지침의 제공 및 보존을 규정한다.
3. **지원 종료 정보:** Article 13(19)는 지원기간 종료일을 구매 시 명확하고 쉽게 접근 가능하게 표시하고, 제품 특성상 기술적으로 가능한 경우 지원 종료 시점에 제품이 지원기간 종료에 도달했음을 알리는 알림을 표시하도록 한다. 이는 모든 제품에 대한 별도의 사전 종료 통지 기한을 정한 조항이 아니다.

서보 드라이브에 실제로 저장되는 파라미터·튜닝 데이터·로그·인증서·키와 데이터 전송 기능은 제품 SKU/아키텍처로 확인한다. CRA는 특정 NAND/EEPROM 물리 소거 회로, 특정 암호학적 삭제 알고리즘 또는 복구 불가능성 시험 방법을 이 조항에서 일률 지정하지 않는다. 설계는 Part I 2(m)의 결과를 달성하도록 제품별 위험과 저장 구조에 맞춰 정당화한다.

## 2.5 #58–#62 감사로 보완한 CVD·신고·로깅 정본

| 쟁점 | 정확한 법령 기준 | 잘못된 해석 방지 |
|---|---|---|
| CVD 정책 | Article 13(8), Annex I Part II(5) | CVD 정책과 법정 Article 14 신고를 같은 트리거로 취급하지 않는다. |
| 신고 연락 주소 | Annex I Part II(6) | 취약점 신고 연락 주소를 제공하고 잠재 취약점 정보 공유를 촉진한다. |
| 사용자 단일 연락 창구 | Article 13(17), Annex II(2) | 쉽게 식별 가능해야 하고 사용자 지침에 포함. 선호 통신 수단을 선택할 수 있으며 자동화 도구만 허용해서는 안 된다. |
| 원칙적 무상 보안 업데이트 | Annex I Part II(8) | 지체 없이 배포하고 원칙적으로 무상. 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 경우 예외. |
| 적극 악용 취약점 신고 | Article 14(1), (2), (7) | 지정 CSIRT와 ENISA에 단일 신고 플랫폼으로 제출. 24h early warning, 72h vulnerability notification, 시정/완화 조치 이용 가능 후 14일 final report. |
| 심각한 제품 보안 사고 신고 | Article 14(3)–(5), (7) | 24h early warning, 72h incident notification, incident notification 제출 후 1개월 final report. |
| 사용자 통지 | Article 14(8) | actively exploited vulnerability 또는 severe incident에 대해 영향 사용자 및 적절한 경우 모든 사용자. machine-readable 형식은 where appropriate 조건. |
| 시장감시기관 정보 공유 | Article 16(3) | 신고를 받은 CSIRT가 필요한 정보를 시장감시기관에 제공. 제조자의 Article 14 직접 신고 수신자와 혼동 금지. |
| 보안 이벤트 로깅 | Annex I Part I 2(l) | 관련 내부 활동 기록·모니터링, 데이터·서비스·기능 접근/변경 포함, 사용자 opt-out 메커니즘. |
| 가용성/DoS | Annex I Part I 2(h) | 필수·기본 기능 가용성과 DoS 복원력·완화. logging과 혼동 금지. |
| 로그 저장·전송 구현 | 위험평가 및 제품 설계 | tamper-proof storage, 보존기간, circular buffer, Syslog over TLS는 이 조항이 지정한 보편적 기술 의무가 아니다. |

직접 인용은 EUR-Lex 현행 consolidated text의 문언·위치와 일치하는 경우에만 허용한다. #58–#62의 Raw Text Quote 5건은 재사용 승인하지 않았다.
