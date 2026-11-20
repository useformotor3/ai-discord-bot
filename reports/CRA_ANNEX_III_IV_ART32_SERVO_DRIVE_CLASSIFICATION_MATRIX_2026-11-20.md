# CRA Annex III/IV 및 Article 32 — 산업용 서보 드라이브 제품 경계·적합성 평가 경로 분석

- 기준일: 2026-11-20
- 법적 근거: Regulation (EU) 2024/2847 (consolidated EUR-Lex text 20-11-2024, corrigenda C1–C3), Commission Implementing Regulation (EU) 2025/2392
- 범위: 산업용 서보 드라이브의 CRA scope, Annex III/IV core functionality, 통합 구성품과 별도 판매 구성품의 경계, Article 32 conformity assessment routes
- 판정 상태: 법령 구조 및 분류 기준 분석 완료; 특정 SKU의 Annex III/IV 분류는 Unknown

## 1. CRA 적용 범위 — Article 2(1), Article 3(1)

CRA는 제품의 intended purpose 또는 reasonably foreseeable use에 direct/indirect logical/physical data connection to a device or network가 포함된 제품에 적용된다. “Product with digital elements”는 software/hardware product 및 remote data processing solutions를 포함하고, 별도 시장에 출시되는 software/hardware components도 포함한다.

따라서 네트워크/필드버스/제어기와 데이터 연결을 사용하는 서보 드라이브는 CRA scope에 들어갈 가능성이 높다. 다만 exact SKU, 판매 구성, intended purpose, reasonably foreseeable use, EU market placing 상태를 증거로 확정해야 한다.

## 2. Annex III/IV 분류 원칙 — core functionality와 component boundary

CRA Article 7(1)은 Annex III product category의 **core functionality**를 가진 제품을 important product로 분류한다. 같은 조항은 그러한 기능을 가진 제품을 다른 제품에 통합했다는 사실만으로 host product가 Article 32(2)/(3) 절차 대상이 되지는 않는다고 명시한다.

Commission Implementing Regulation (EU) 2025/2392 recital (2)–(3)은 기술적 설명과 구성품 통합 원칙을 보강한다. 예시로 embedded browser를 포함한 뉴스 앱이 브라우저 제품군으로 자동 재분류되지는 않지만, 뉴스 앱 전체의 CRA essential requirements 준수는 여전히 필요하며 통합된 브라우저 구성품의 보안도 고려해야 한다.

따라서 다음을 분리한다.
1. 완제품 서보 드라이브의 core functionality
2. 드라이브 내부의 통합 구성품·보안 기능
3. 별도 SKU/옵션/부품으로 시장에 공급되는 네트워크 인터페이스, MCU, secure element, 소프트웨어
4. 제조자의 component due diligence 및 취약점 처리 의무

## 3. 서보 드라이브와 관련될 수 있는 Annex III 범주

### 3.1 Class I 후보

**Physical and virtual network interfaces (Annex III Class I, category 10)**
- Reg. 2025/2392 technical description은 physical interface를 driver API를 통해 device를 network에 직접 연결하는 제품으로 설명한다. 보통 data-link layer에서 동작하고 hardware adapter 및 firmware를 포함한다.
- 명시된 예시에 Ethernet, Wi-Fi뿐 아니라 Fieldbus controllers/adapters도 포함된다.
- 따라서 서보 드라이브의 Fieldbus/EtherCAT/이더넷 인터페이스는 제품 경계 분석에서 반드시 검토해야 한다.
- 다만 통신 포트가 존재한다는 이유만으로 모터 제어가 core functionality인 완제품 드라이브를 네트워크 인터페이스 제품으로 자동 분류할 수는 없다. 별도 판매 interface card/controller/adapter는 별도 제품으로 평가해야 한다.

**Microcontrollers with security-related functionalities (Annex III Class I, category 14)**
- MCU가 encryption, authentication, secure key storage, RNG, TEE 또는 hardware-based protection을 제공하고, 그 목적이 MCU 자체를 넘어 다른 제품·네트워크·서비스를 보호하는 것인지 확인한다.
- MCU가 존재한다는 사실 또는 보안기능 명칭만으로 전체 드라이브를 Class I로 분류하지 않는다.
- 정확한 MCU part number, vendor security manual, security 기능의 목적, 별도 판매 여부를 확인한다.

**Operating systems (Annex III Class I, category 11)**
- 기술 설명은 하드웨어 추상화 인터페이스와 software execution을 제어하는 OS를 포함하며 real-time OS도 예시 범위에 포함한다.
- 서보 드라이브에 RTOS/firmware가 내장되어 있다는 사실만으로 완제품이 OS 제품이 되지는 않는다. 별도 공급되는 OS product인지와 core functionality를 구분한다.

**NMS/VPN/SIEM (Annex III Class I categories 5–7)**
- VPN은 물리/가상 네트워크 자원을 통해 암호화된 논리 터널을 만드는 제품이다.
- NMS는 연결된 network elements를 모니터링하고 network operations/configuration을 제어한다.
- SIEM은 여러 출처의 데이터를 수집·분석·상관분석해 보안 목적의 actionable information을 제공한다.
- 서보 드라이브의 remote access, parameter configuration, alarm/history만으로 이 범주에 자동 해당하지 않는다. ETSI EN 304 620/621/622의 industrial OT exclusion도 별도 고려한다.

**Routers/modems/switches (Annex III Class I category 12)**
- 라우터는 network 간 data flow를 route하고, switch는 packet forwarding 및 management plane을 제공한다. 단순 Ethernet/EtherCAT port는 라우터/스위치 기능의 증거가 아니다.

### 3.2 Class II 후보

**Firewalls, IDS and IPS (Annex III Class II category 2)**
- Firewall은 연결된 network/system을 무단 접근으로부터 보호하기 위해 traffic을 감시·제한한다.
- IDS는 network traffic의 의심 행위를 감시·탐지한다.
- IPS는 탐지 기능을 바탕으로 침입에 능동 대응한다.
- 완제품의 core functionality가 보안 appliance인지가 핵심이다. 통합된 filtering/diagnostic feature만으로 서보 드라이브 전체를 Class II로 자동 분류하지 않는다.

### 3.3 Annex IV critical product 후보

**Hardware Devices with Security Boxes**
- 민감정보를 안전하게 저장·처리·관리하거나 암호 연산을 수행하고, 여러 discrete components로 구성되며, 물리적 공격에 대한 tamper evidence/resistance/response를 제공하는 physical envelope가 있어야 한다.
- 일반 금속 드라이브 enclosure만으로 해당하지 않는다.

**Smart meter gateways / advanced secure cryptoprocessing devices**
- smart metering system 및 authorised third party 사이의 통신을 제어하고 metering/data flow 보호, cryptoprocessing, firewalling, device control 등 기술 설명에 부합하는지 확인한다.
- 일반 서보 드라이브는 이 intended purpose와 다르지만, 실제 사용 목적/제품 경계 증거 없이 확정 배제하지 않는다.

**Smartcards or similar devices, including secure elements**
- secure element는 cryptographic/sensitive data 처리 및 tamper evidence/resistance/response를 갖고 AVA_VAN.4 이상 보호 수준을 충족하는지 확인한다.
- SoC에 secure element가 통합될 수 있으나, 구성품 존재가 host drive 전체를 자동으로 Annex IV critical product로 만들지는 않는다.

## 4. Article 32 적합성 평가 경로

| 제품 분류 | 법적 경로 | 핵심 조건 |
|---|---|---|
| 일반 제품(Annex III/IV core functionality 없음) | Article 32(1): Module A, Module B+C, Module H, 또는 available/applicable EUCC | 제조자가 허용된 경로 중 선택 |
| Important Class I | Article 32(2) | 관련 HEN/CS/EUCC(assurance ≥ substantial)를 적용하지 않았거나 일부만 적용했거나 존재하지 않으면 Module B+C 또는 H. 관련 수단을 완전히 적용한 경우 Article 32(1) 경로 사용 가능 |
| Important Class II | Article 32(3) | Module B+C, Module H, 또는 available/applicable EUCC at least substantial |
| Critical Annex IV | Article 32(4) + Article 8(1) | Article 8(1) delegated act가 요구하는 경우 EUCC; 해당 조건/act가 없으면 Article 32(3) 경로 |

주의:
- ETSI/CENELEC work programme의 Harmonised Standard=Yes 또는 Citation expected는 OJ citation이 아니다. Article 27 presumption은 실제 OJ reference와 해당 제품·요구사항의 scope fit가 확인되어야 한다.
- Class I의 Article 32(2)에서 Module A를 사용하려면 관련 HEN/CS/EUCC의 완전 적용 조건을 확인해야 한다. 미적용/부분 적용/부재 시 B+C 또는 H가 요구된다.
- Class II는 Module A를 기본 선택지로 두지 않는다.
- Annex IV 제품에 대한 mandatory EUCC는 Article 8(1) delegated act 및 적용 가능한 scheme 상태를 별도 확인해야 한다. delegated act가 없는 경우 Article 8(1)은 Article 32(3) 경로를 명시한다.

## 5. 구성품·공급망 의무

제품 분류와 별개로 Article 13(5)는 제3자 구성품 통합 시 due diligence를 요구한다. Article 13(6)은 통합 구성품에서 취약점을 확인하면 구성품 제조자/유지관리자에게 보고하고 해당 취약점을 처리·시정하도록 한다.

따라서 host drive가 Annex III/IV category에 속하지 않더라도 네트워크 인터페이스, MCU, RTOS, secure element, third-party libraries 등의 구성품 보안은 제품 전체의 risk assessment와 vulnerability handling에서 다뤄야 한다.

## 6. 서보 드라이브 판정에 필요한 증거

1. Exact model/SKU, hardware revision, firmware version, EU market configuration.
2. Network/fieldbus interface board가 내장인지 옵션인지, 별도 판매되는지, 별도 product name/SKU가 있는지.
3. Ethernet/Fieldbus driver API, protocol layer, hardware adapter, firmware, network-management/router/switch functions.
4. MCU/MPU/FPGA/ASIC exact part numbers 및 vendor security manual: encryption, authentication, key storage, RNG, TEE, secure boot, tamper features.
5. 보안기능이 해당 chip 자체를 넘어 다른 제품/네트워크/서비스를 보호하도록 설계되었는지.
6. RTOS/OS의 명칭, 라이선스/판매 경계, 별도 공급 여부.
7. Firewall/IDS/IPS/VPN/NMS/SIEM 기능이 단순 내장 보조기능인지, 완제품의 core functionality인지.
8. Enclosure tamper evidence/resistance/response, secure cryptoprocessing, secure element assurance evidence.
9. Intended purpose, reasonably foreseeable use, product manuals, marketing statements, system diagrams, BOM, manufacturer declaration.

## 7. 현 단계 결론

- CRA scope: 데이터 연결을 의도하거나 합리적으로 예상할 수 있는 서보 드라이브는 Article 2(1) 적용 가능성이 높다. exact SKU/configuration evidence로 확정한다.
- Annex III Class I: 완제품 core functionality가 어떤 category에 해당하는지 아직 증거 부족. 특히 별도 판매 Fieldbus/network interface module과 security-function MCU를 분리 검토한다.
- Annex III Class II: 완제품이 firewall/IDS/IPS security appliance라는 증거가 없다. Unknown 유지.
- Annex IV: Hardware Device with Security Box, smart meter gateway, secure element/smartcard 기술 설명에 부합하는 완제품 증거가 없다. Unknown 유지.
- Article 32 route: 최종 product classification과 현재 OJ/HEN/CS/EUCC 상태를 확인한 후 결정한다. 현재 제품별 Module A 또는 third-party route를 확정하지 않는다.

## 8. 공식 1차 출처

- Regulation (EU) 2024/2847, consolidated EUR-Lex text: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02024R2847-20241120
- Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32025R2392
- ELI / OJ text 2025/2392: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng


## 9. ETSI Work Programme class-label mismatch — legal source controls

ETSI Work Item scope pages for EN 304 635 (hypervisors/container runtime) and EN 304 636 (firewalls/IDS/IPS) currently describe the categories as CRA Annex III Class I. This conflicts with the legally binding technical descriptions in Commission Implementing Regulation (EU) 2025/2392 Annex I:
- Hypervisors/container runtime systems: Annex III Class II category 1.
- Firewalls/IDS/IPS: Annex III Class II category 2.

The discrepancy is confirmed at the ETSI Work Programme metadata/scope-text layer. The latest EN 304 636 V1.0.0 draft explicitly states Class II point 2 on PDF page 9 and aligns with the law. The latest EN 304 635 V1.0.1 file is listed in DocBox but fetch timed out; its content remains unverified. The official regulation controls the product class and conformity route.

ETSI pages: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74858 and https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74859
Official legal source: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng


### 9.1 Earlier public draft reconciliation

- EN 304 636 V0.0.9 (2025-12-15) explicitly cites Annex III Class II point 2 in Introduction and Scope. The public draft is aligned with Regulation 2025/2392; the current Work Item page's Class I label appears stale.
- EN 304 635 V0.0.8 (2025-11-10) has no Annex III/Class I/Class II label in the extracted draft text. No normative draft misclassification is established.
- Latest EN 304 636 v1.0.0 was acquired and inspected; latest EN 304 635 v1.0.1 is listed in DocBox but fetch timed out, so only its current draft content remains unverified.

Draft sources:
- https://docbox.etsi.org/CYBER/EUSR/Open/EN-304-635_V0.0.8_2025-11-10_Virtualisation_Containers.pdf
- https://docbox.etsi.org/cyber/CYBER/Open/EN-304-636_V0.0.9_2025-12-15_Firewalls_Mature-draft.pdf


### 9.2 Latest EN 304 636 V1.0.0 confirms Class II

The latest public EN 304 636 V1.0.0 (2026-07-09) PDF was opened from ETSI DocBox. Page 9 Introduction explicitly identifies firewalls, IDS and IPS as Annex III Class II point 2. This is direct evidence that the latest public draft aligns with the legal class; the current Work Item page's Class I label is stale/incorrect metadata.

The latest EN 304 635 V1.0.1 file is present in the DocBox directory (2026-06-24) but fetching timed out. Its current draft content remains unverified; earlier V0.0.8 contains no class label in extracted text.
