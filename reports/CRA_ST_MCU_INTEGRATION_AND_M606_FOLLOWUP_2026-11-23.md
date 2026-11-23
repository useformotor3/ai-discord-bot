# ST MCU 통합 제품의 CRA 분류 및 M/606 AMD 1 회의 추적 메모

- 기준일: 2026-11-23 (KST)
- 기준 main: `c56299a531b54eaed48e1a2e7324175b93c0f6ad`
- 조사 범위: CRA only. ST MCU가 포함된 산업용 서보 드라이브의 제품 경계·Annex III 분류 판단 원리와 ETSI M/606 AMD 1 회의 상태 추적
- 상태: 법령 원칙 확인 / 특정 ST 부품 및 LS메카피온 모델별 분류는 미확인

## 1. 핵심 결론

**ST MCU를 사용한다는 사실만으로 서보 드라이브 완제품이 CRA Annex III Class I의 'security-related functionalities를 가진 microcontrollers'에 자동 분류되는 것은 아니다.**

이유는 두 가지다.

1. Commission Implementing Regulation (EU) 2025/2392 Annex I Class I category 14는 단순히 MCU라는 이유가 아니라, 보안 관련 기능을 추가로 제공하는 마이크로컨트롤러 제품을 기술적으로 설명한다. 예시 기능에는 암호화, 인증, 보안 키 저장, 난수 생성, Trusted Execution Environment 및 기타 하드웨어 기반 보호 기능이 포함된다. 이 기능은 MCU 자체만을 위한 것이 아니라 다른 제품·네트워크·서비스를 보호하는 목적이어야 한다.
2. CRA Article 7(1) 및 Implementing Regulation (EU) 2025/2392의 전문 (1)~(2)는 중요/핵심 제품 분류에서 제품 전체의 핵심 기능(core functionality)을 기준으로 삼는다. 구성요소의 기능이 완제품의 핵심 기능과 동일한 것은 아니다. 따라서 MCU가 완제품에 통합되었다는 사실만으로 완제품을 해당 MCU 카테고리로 분류하지 않는다.

다만 이 결론은 'MCU의 보안 기능을 무시해도 된다'는 뜻이 아니다. 완제품의 CRA 위험평가·보안 설계·기술문서에서는 MCU가 제공하는 보안 기능과 그 한계, 실제 활성화·구성 여부, 키 관리 및 펌웨어 사용 방식을 평가해야 한다.

## 2. 법적 근거와 해석 경계

### 2.1 구속력 있는 법령

- [Regulation (EU) 2024/2847 (Cyber Resilience Act), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng)
  - Article 7(1): 제품의 핵심 기능과 중요 제품 카테고리 판단의 연결
  - Article 13: 제조자의 제품 사이버보안 위험평가 및 필수 요구사항 이행
  - Annex III: 중요 제품 카테고리
- [Commission Implementing Regulation (EU) 2025/2392, EUR-Lex](https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng)
  - Annex I, Class I, category 14: security-related functionalities를 가진 microcontrollers의 기술 설명
  - 전문 (1)~(2): 제품 전체(core functionality)를 기준으로 카테고리와 적합성 평가 절차를 판단한다는 설명

### 2.2 Category 14 기능 판단

제품 데이터시트에 'secure', 'security', 'cryptography'라는 단어가 한 번 등장하는 것만으로 결론을 내리지 않는다. 최소한 다음을 확인한다.

| 확인 항목 | 필요한 증거 | 판단상 주의 |
|---|---|---|
| 정확한 MCU 식별 | 전체 orderable part number, package, silicon revision | STM32 같은 제품군 이름만으로는 부족 |
| 암호 기능 | 하드웨어 가속기 종류, 지원 알고리즘, 사용 조건 | 라이브러리 소프트웨어 기능과 MCU 하드웨어 기능 구분 |
| 인증 기능 | secure boot/authentication engine, 인증서·키 처리 구조 | 기능이 존재하는지와 실제 제품에서 사용하는지는 별도 |
| 보안 키 저장 | HUK/OTP/eFuse/secure storage 사양, 접근 통제 | 일반 Flash 저장과 보안 키 저장을 동일시하지 않음 |
| 난수 생성 | TRNG/DRBG 유무, 인증·품질 정보, 사용 API | 단순 PRNG를 TRNG로 표현하지 않음 |
| 격리 실행 | TEE/TrustZone/secure enclave 등 정확한 구현 | CPU 기능 지원과 펌웨어에서 활성화한 상태 구분 |
| 하드웨어 보호 | debug authentication/lock, tamper, lifecycle state 등 | 실제 제품 설정·잠금·시험 결과 확인 |
| 보호 대상 | MCU가 다른 제품·네트워크·서비스를 보호하도록 설계되는지 | 데이터시트의 일반 설명만으로 최종 제품 목적을 단정하지 않음 |

### 2.3 통합 MCU와 별도 판매 MCU 구분

- **드라이브에 내장된 MCU**: 드라이브 완제품의 핵심 기능을 기준으로 완제품 카테고리를 판단한다. MCU의 보안 기능은 부품 수준 위험평가와 완제품 보안 설계 증거로 반영한다.
- **별도 판매되는 MCU/보안 모듈**: 별도 제품의 intended purpose, 시장 공급 형태, 핵심 기능 및 category 14 기술 설명 충족 여부를 독립적으로 검토한다.
- **별도 통신/보안 보드**: 별도 판매 여부뿐 아니라 독립 제품인지, 드라이브에 필수 통합되는 구성요소인지, 자체 핵심 기능이 무엇인지 확인한다.

위 구분은 제품 경계를 확인하기 위한 분석 프레임이다. 개별 SKU의 법적 분류를 확정하는 결론은 아니다.

## 3. ST MCU 및 LS메카피온 적용을 위해 필요한 자료

현재 저장소의 확정 사실은 사용자가 ST MCU를 사용한다고 알려준 것뿐이다. 정확한 ST 부품번호와 LS메카피온 드라이브 모델·하드웨어 개정·펌웨어 버전은 이 조사 시점에 확인되지 않았다. 따라서 특정 STM32 계열 또는 보안 기능을 임의로 가정하지 않는다.

다음 자료를 확보해야 한다.

1. ST MCU 전체 주문 코드(예: 제품군명이 아닌 전체 part/order code), 데이터시트와 reference manual의 개정번호
2. MCU에 탑재·활성화된 보안 하드웨어 기능 목록과 설정 상태
3. Boot ROM, bootloader, secure boot, firmware update 및 rollback 방지 구현 자료
4. 암호키 생성·저장·주입·회전·폐기 방식과 제조 단계의 provisioning 절차
5. 디버그 포트(SWD/JTAG 등) 생산/현장 접근 정책, 잠금 및 복구 절차
6. 드라이브의 전체 통신 인터페이스·프로토콜·네트워크 연결 구조와 데이터 흐름
7. LS메카피온의 정확한 모델명, HW revision, FW version, 제품 매뉴얼, BOM 및 회로도
8. MCU·펌웨어·보안 기능이 별도 판매·업데이트·서비스되는지 여부

자료가 확보되면 (a) MCU 부품 자체의 기능 사실, (b) 완제품에 실제 적용된 기능, (c) 완제품 core functionality, (d) Annex III/IV category, (e) Article 32 conformity route를 별개의 판단 단계로 검증한다.

## 4. ETSI M/606 AMD 1 회의 상태

ETSI 공식 회의 캘린더는 **GoSRSReq006-M/606 AMD 1 - examination meeting**을 2026-11-23 하루 일정, Online으로 표시한다.

- 공식 일정 출처: [ETSI Technical Bodies meeting calendar](https://portal.etsi.org/tb.aspx?TBID=945&subTB=945)
- 2026-11-23 KST 조사 시점의 상태: **당일 일정으로 게시됨**.
- 공개 캘린더 항목만으로 회의 개최 완료, 결론, 표결, 수정안 채택, ESO 전달 또는 수락을 증명할 수 없다.
- 그러므로 회의 결과는 현재 **Unknown / not yet evidenced**로 유지한다.

### 회의 후 확인해야 할 증거

1. ETSI 회의록 또는 공식 결정 기록과 문서 버전·발행일
2. M/606 AMD 1 최종 또는 개정 문서와 Annex I의 topic별 일정
3. ESO(ETSI/CEN/CENELEC)의 공식 수령일 및 수락/비수락 통지
4. Article 2의 수령 기반 1개월 조건을 계산할 수 있는 원문 통지
5. Commission/ESO 공식 발표 및 이후 Work Programme 변경 내역

회의가 열렸다는 사실과 개정안이 공식 수락되었다는 사실은 서로 다르다. Article 2 일정·비수락 조건은 실제 수령 증거가 확보되기 전까지 계산 완료로 기록하지 않는다.

## 5. 이번 조사 결과의 상태

| 항목 | 상태 | 근거/제한 |
|---|---|---|
| CRA Article 7(1) 및 제품 전체 핵심 기능 원칙 | 확인됨 | CRA 원문 및 Implementing Regulation 2025/2392 |
| Annex III Class I category 14 기술 설명 | 확인됨 | Implementing Regulation 2025/2392 Annex I |
| ST MCU 정확한 모델/보안 기능 | 미확인 | 전체 part number 및 제조사 문서 미제공 |
| LS메카피온 모델별 MCU 적용 | 미확인 | 정확한 SKU/HW/FW/BOM 미확보 |
| 완제품 Annex III/IV 분류 | Unknown | 제품 전체 core functionality 및 제품 증거 필요 |
| M/606 AMD 1 회의 일정 | 확인됨 | ETSI 공식 캘린더, 2026-11-23 Online |
| M/606 AMD 1 회의 결과/ESO 수락 | 미확인 | 회의록·결정·수령 통지 미확보 |

## 6. 다음 작업 우선순위

- P0: ETSI M/606 AMD 1 회의 후 공식 minutes/decision 및 ESO receipt/acceptance evidence 확인. 확인 전에는 일정만 Verified, 결과는 Unknown으로 유지.
- P0: ST MCU 전체 part number와 LS메카피온 정확한 드라이브 SKU/HW/FW 자료 확보 요청 목록을 제품 증거 register와 연결.
- P1: Category 14의 각 기술 요소를 ST 제조사 원문과 대조하고, '기능 지원'과 '제품에서 활성화/사용'을 구분.
- P1: Article 7(1), Implementing Regulation 2025/2392 recital (1)~(2), Annex I category 14를 통합 보고서의 Annex III 분류 설명과 교차 링크.
- P1: 확인된 제품 자료를 바탕으로 전체 드라이브 core functionality 및 Article 32 경로를 재평가. 자료가 없으면 Unknown 유지.

## 7. 조사 품질 및 한계

- 법적 분류의 우선 근거는 EUR-Lex에 게시된 구속력 있는 법령이다. ETSI 일정은 회의 일정의 증거일 뿐 법령 개정 또는 ESO 수락의 증거가 아니다.
- 이번 메모는 category 14와 제품 전체 분류 원칙을 설명한다. 특정 ST MCU가 category 14에 해당한다고 판정하지 않았다.
- 특정 LS메카피온 제품이 Annex III/IV에 해당하거나 일반 제품이라고 확정하지 않았다.
- 표준의 발행·Work Item 상태·OJ 인용·Article 27 추정 적합성은 각각 별도 증거로 관리한다.
