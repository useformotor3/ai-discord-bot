# 제조사 MCU 보안 자료 기준선 — ST 우선 / TI 비교 (2026-11-12)

**목적:** 서보 드라이브 CRA 하드웨어·펌웨어 설계에 사용할 제조사 1차 자료를 등록하고, 기능별 비교 가능 범위와 미확인 항목을 분리한다.  
**검토 기준일:** 2026-11-12  
**브랜치:** `cra-project-foundation`  
**중요 제한:** ST 실제 MCU 주문 코드가 아직 없다. 따라서 ST는 STM32 제품군 자료 기준선이며, 특정 부품의 기능 보유를 확정하지 않는다. TI MSPM0G3529-Q1은 기능 비교용 예시 부품이지 실제 프로젝트의 동급 대체품으로 선정된 것이 아니다.

## 1. 공식 자료 레지스터

| Source ID | 제조사 / 문서 | 버전 / 날짜 | 공식 URL | 검토 범위 | 적용 상태 |
|---|---|---|---|---|---|
| ST-AN5156 | ST AN5156, *Introduction to security for STM32 MCUs* | Rev 14, June 2026 | https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html | 공격 유형, RDP/product state, 메모리 보호, 디버그 보호, secure boot/SFU, SFI, 암호·난수, STM32 제품군별 기능 표 | 문서 내용 VERIFIED; 실제 MCU 적용성 UNVERIFIED |
| ST-STM32TRUST | ST STM32Trust ecosystem | 웹 자료, 확인일 2026-11-12 | https://www.st.com/content/st_com/en/ecosystems/stm32trust.html | 보안 애플리케이션 노트/패키지의 공식 진입점 | 링크 및 자료 존재 확인; 개별 패키지 버전은 별도 확인 |
| ST-AN4992 | ST AN4992, *Introduction to secure firmware install (SFI) for STM32 MCUs* | Rev 19, July 2026 | https://www.st.com/content/st_com/en/technical-documents/an4992-introduction-to-secure-firmware-install-sfi-for-stm32-mcus-stmicroelectronics.html | 제조 과정에서 OEM 펌웨어의 기밀성·진위성·무결성을 보호하는 SFI | 문서 내용 VERIFIED; 대상 MCU 지원 여부 UNVERIFIED |
| ST-AN5447 | ST AN5447, *Overview of Secure Boot and Secure Firmware Update solution on Arm TrustZone STM32 MCUs* | Rev 3, August 2021 | https://www.st.com/content/st_com/en/technical-documents/an5447-overview-of-secure-boot-and-secure-firmware-update-solution-on-arm-trustzone-stm32-microcontrollers-stmicroelectronics.html | TrustZone 기반 STM32의 secure boot/SFU 및 SBSFU 비교 | 문서 내용 VERIFIED; 대상 제품군 적용성 UNVERIFIED |
| TI-DS-3529 | TI MSPM0G3529-Q1 datasheet, *MSPM0G352x-Q1 Automotive Mixed-Signal Microcontrollers With CAN-FD Interface* | SLASFO2B, November 2024, revised October 2025 | https://www.ti.com/lit/ds/symlink/mspm0g3529-q1.pdf | 정확한 부품의 CPU/메모리/주변장치/보안 기능 | 문서상 부품 기능 VERIFIED |
| TI-SLAAE29 | TI *Cybersecurity Enablers in MSPM0 MCUs* | TI MSPM0G3506 product technical-document index lists Rev B, Aug 27 2026; Rev A PDF (revised Dec 2025) was opened and analyzed in this session | https://www.ti.com/product/MSPM0G3506 (official index); Rev A PDF: https://www.ti.com/lit/an/slaae29a/slaae29a.pdf | MSPM0 platform BCR/BSL/CSC, secure boot, secure storage, AES/TRNG architecture and family feature mapping | Rev A content verified; Rev B existence/date verified on TI index, but its PDF contents and applicability to MSPM0G3529-Q1 are not yet checked |
| TI-TRM-G | TI MSPM0 G-Series 80-MHz Microcontrollers Technical Reference Manual | TI MSPM0G3506 product technical-document index lists Rev F, Nov 5 2026; MSPM0G3529-Q1 product page directs users to G-Series TRM but the exact applicable revision must be checked | https://www.ti.com/product/MSPM0G3529-Q1 (part page); https://www.ti.com/product/MSPM0G3506 (Rev F index) | Security registers, CSC/INITDONE, KEYSTORE, memory protection at register level | Latest Rev F listing found; part-specific applicability and direct document URL remain UNVERIFIED |

> ST 문서 페이지는 PDF가 공식 기준 문서이며 웹 HTML은 편의·초기 평가용이라고 명시한다. 보고서의 확정 인용은 PDF revision을 기준으로 한다.

## 2. 기능별 비교 — 문서에서 확인된 범위

| 보안 기능 | ST STM32 공식 자료 | TI MSPM0G3529-Q1 공식 자료 | CRA 설계상 의미 / 추가 검증 |
|---|---|---|---|
| Secure boot | AN5156은 암호 기반 SB 구현과 고유 boot entry, 비밀 보호를 가이드. SBSFU/TF-M 등 구현 경로 설명 | 데이터시트 §8.18에 secure boot 명시. SLAAE29A는 CSC/BIM 구현과 이미지 검증 흐름 설명 | 부팅 시 승인된 펌웨어만 실행되는지, 키 교체·폐기·복구 경로까지 시험 |
| Secure firmware update | AN5156은 암호 기반 SFU 및 SFU 비밀 보호를 가이드. 제품군별 SBSFU/TF-M 경로 차이 | 데이터시트 §8.18에 secure firmware update, dual-bank/address swap. SLAAE29A는 버전 비교·rollback 보호 예시 설명 | 서명/인증, anti-rollback, 전원 차단 복구, 부분 다운로드, 실패 복귀, update package provenance 시험 |
| Debug / lifecycle | RDP, product state, debug authentication 등. 기능/잠금 단계는 STM32 부품별 상이 | 데이터시트 §8.18에 debug security. SLAAE29A는 password-authenticated debug 및 SWD disable 등 플랫폼별 매핑 | 개발·서비스·양산 상태를 분리하고 생산 잠금 후 승인된 복구/서비스 절차 확인 |
| Key storage | AN5156은 OBK/CKS, SAES/CCB 등 특정 STM32 계열 기능을 설명하나 모든 MCU에 공통이 아님 | 데이터시트 §8.18/§8.21: AES 키 최대 4개 보관. SLAAE29A는 CSC에서 KEYSTORE로 키 적재 후 애플리케이션이 키 원문을 읽지 못하는 흐름 설명 | key provisioning, rotation, revocation, backup, zeroization, debug/DMA 접근경로 시험 |
| Cryptographic acceleration | STM32 제품군별 AES/SAES/HASH/PKA/CCB 등 표에 기능 차이가 있음 | AES-128/256 및 GCM/GMAC, CCM/CBC-MAC, CBC, CTR 지원 명시 | 알고리즘 이름만 비교하지 말고 키 길이, mode, throughput, side-channel/errata, software API를 확인 |
| Random number | STM32 계열별 RNG/인증 표를 구분해 제공 | 데이터시트 §8.19에 TRNG, health tests 및 동작 모드 명시 | 엔트로피 원천, health test 처리, DRBG 구성, 부팅 실패/고장 시 fail-safe 확인 |
| Memory / code isolation | RDP, WRP, PCROP, HDP, MPU, firewall, TrustZone 등 제품군별 차등 | 데이터시트 §8.18에 flash write-erase/read-execute/IP protection, SRAM W^X firewall 명시 | MCU 내부 접근제어는 시스템 권한 모델·DMA·부트·업데이트와 함께 검증 |
| Manufacturing firmware provisioning | AN5156/AN4992 SFI: OEM 펌웨어의 제조 과정 내 안전한 설치 | 이번에 확인한 TI 문서에서는 ST SFI와 동일한 범위의 별도 제조 서비스 대조를 완료하지 않음 | 위탁 제조 시 key injection, image confidentiality, device identity, audit trail 검토 |

### 비교 해석 제한

1. 기능 표기는 **기능 존재 여부**이지 보안 수준·CRA 적합성·공격 저항성의 동등성을 뜻하지 않는다.
2. ST AN5156은 여러 STM32 시리즈를 한 문서에서 다룬다. 문서가 STM32 제품군 전체를 포괄한다고 해서 특정 MCU에 모든 기능이 있다는 뜻은 아니다. 정확한 part number의 datasheet, reference manual, errata, lifecycle 문서를 확인해야 한다.
3. TI MSPM0G3529-Q1 데이터시트는 특정 부품에 보안 기능을 열거한다. SLAAE29A의 CSC 예제/기능 매핑은 플랫폼 설명이므로, 부품 데이터시트와 G-Series TRM의 실제 지원 및 설정 조건을 함께 확인한다.
4. TI 데이터시트의 “PSA Level 1 Certification targeted”는 목표/예정 표현이다. 해당 표현만으로 PSA 인증 취득을 주장하지 않는다.
5. TI의 Automotive Q1 qualification 또는 ASIL 관련 표기는 CRA 사이버보안 인증/적합성 증거가 아니다. 기능 안전과 CRA를 혼동하지 않는다.
6. 성능/가격/전력/부품 수급 비교는 동일한 요구사항, 공정 조건, package, operating temperature, toolchain, license 및 lifecycle 기준을 정한 후 수행한다.

## 3. 서보 드라이브 적용 관점의 검증 작업

| Work ID | 확인할 내용 | 증거 / 시험 산출물 | 현재 상태 |
|---|---|---|---|
| MCU-01 | 실제 ST MCU 주문 코드, package, silicon revision | BOM, 구매명세, marking, datasheet | UNVERIFIED |
| MCU-02 | 정확한 부품의 RDP/lifecycle/debug 인증·잠금 상태 | Reference Manual, option-byte/product-state 설정, production programming record | UNVERIFIED |
| MCU-03 | ROM boot / secure boot root of trust 및 boot source | boot flow, memory map, threat model, negative boot tests | UNVERIFIED |
| MCU-04 | firmware signature, key provisioning, key rotation/revocation | key ceremony, signing procedure, test vectors, key inventory | UNVERIFIED |
| MCU-05 | anti-rollback 및 update atomicity | version counter, downgrade test, power-cut test, recovery log | UNVERIFIED |
| MCU-06 | secure update transport / service port / PC tool | protocol spec, authentication, access control, test logs | UNVERIFIED |
| MCU-07 | debug/service lifecycle | development/service/production state table, authorization and unlock logs | UNVERIFIED |
| MCU-08 | key/credential storage 및 zeroization | key hierarchy, storage map, access test, reset/erase test | UNVERIFIED |
| MCU-09 | TRNG/DRBG의 실제 사용과 failure behavior | entropy design, health-test handling, startup tests | UNVERIFIED |
| MCU-10 | 외부 Flash/EEPROM, DMA, debug, bootloader 등 경계 | block diagram, access matrix, penetration test evidence | UNVERIFIED |
| MCU-11 | 제조·위탁생산 중 firmware/key provisioning | manufacturing flow, station authorization, audit log | UNVERIFIED |
| MCU-12 | 제품별 보안 기능의 errata/known limitations | exact errata revision, deviation register | UNVERIFIED |

## 4. 다음 기술 단계

1. 사용 중인 ST MCU part number가 확보되면 AN5156 기능표와 해당 datasheet/reference manual/errata를 결합해 part-specific capability matrix를 만든다.
2. ST MCU를 기준으로 secure boot/update, debug lifecycle, key storage, crypto/TRNG, memory isolation을 회로 블록과 펌웨어 trust boundary에 배치한다.
3. TI MSPM0G3529-Q1을 참고 사례로 유지하되, 동일한 motor-control workload/real-time timing/analog performance/communications/package/cost 조건이 정해지기 전에는 동급 제품 비교를 완료 처리하지 않는다.
4. 각 기능을 CRA Annex I 요구사항과 연결할 때는 법령이 요구하는 결과와 제조사가 제공하는 구현 기능을 구분한다. MCU 기능만으로 제품 전체 CRA 준수라고 판단하지 않는다.

## 5. 공식 자료의 직접 확인 위치

- ST AN5156 Rev 14: front matter / applicable product series; device protections; debug port and interface protection; secure boot/SFU; STM32 security features by device; Guidelines; revision history.
- ST AN4992 Rev 19: SFI security features, SFI constraints, supported MCU family table.
- TI SLASFO2B Rev B: §1 Features; §3 Description; §4 Functional Block Diagram; §8.18 Security; §8.19 TRNG; §8.20 AESADV; §8.21 Keystore; §11 Revision History.
- TI SLAAE29A Rev A (analyzed copy): §1.3 Platform Security Enablers; §2 Device Security Model; §3 Secure Boot; §4 Secure Storage; §5 Cryptographic Acceleration; §9 Revision History. 이전 조사 메모에는 TI index의 SLAAE29 Rev B (Aug 27 2026) 표시가 기록되어 있으나, 이번 세션에서 해당 공식 인덱스/Rev B 원문을 재현하지 못했다. Rev B는 원문 확보 전까지 UNVERIFIED로 취급한다.

**결론:** TI MSPM0G3529-Q1은 데이터시트에서 여러 보안 기능을 명시하는 구체적 비교 사례다. ST는 AN5156의 제품군별 기능 표가 강력한 출발점이지만 실제 부품번호가 없어 현재 특정 ST MCU와의 동급 비교는 불가능하다. 실제 ST part number가 확보되기 전까지 ST 쪽의 부품별 기능은 UNVERIFIED로 유지한다.


## 6. TI 최신 G-Series TRM 원문 접근성 재점검 (2026-11-12)

- MSPM0G3529-Q1 공식 제품 페이지는 해당 제품군의 전체 모듈 설명을 위해 *MSPM0 G-Series 80MHz Microcontrollers Technical Reference Manual*을 참조하도록 연결한다. 데이터시트 Rev B도 해당 G-Series TRM을 안내한다.
- TI의 공식 MSPM0-DIAGNOSTIC-LIB 기술자료 인덱스에는 G-Series TRM **Rev F, 2026-11-05**가 표시된다. 해당 페이지는 MSPM0G3529-Q1을 포함하는 MSPM0 제품군 자료와 함께 제공된다.
- TRM 문헌 번호는 **SLAU846**으로 확인된다. TI의 HTML/PDF 열기 시 문서가 너무 커서 현재 도구가 전체 본문을 가져오지 못했다. 따라서 Rev F의 SECURITY 장, CSC/KEYSTORE/debug 관련 레지스터 설명을 직접 확인한 것으로 기록하지 않는다.
- 이전 검색에서 제기된 SLAAE29 Rev B는 이번 재점검에서 TI 공식 Rev B PDF/직접 문서 페이지를 재현하지 못했다. 현재 검증 가능한 분석 자료는 **SLAAE29A Rev A, revised December 2025**다. Rev B는 원문 확보 전까지 UNVERIFIED로 둔다.
- 공식 링크:
  - MSPM0G3529-Q1 제품 페이지: https://www.ti.com/product/MSPM0G3529-Q1
  - TI MSPM0-DIAGNOSTIC-LIB 기술자료 인덱스(TRM Rev F 표시): https://www.ti.com/tool/MSPM0-DIAGNOSTIC-LIB
  - G-Series TRM 문헌번호 기반 공식 링크(열람 실패): https://www.ti.com/lit/pdf/SLAU846
  - SLAAE29A Rev A: https://www.ti.com/lit/an/slaae29a/slaae29a.pdf

**정확성 보정:** Rev F의 문서명/개정일 인덱스 확인과 Rev F 본문 내용 검증은 별개다. 본문 직접 열람 전까지 보안 장 상세 주장은 SLAAE29A Rev A 및 MSPM0G3529-Q1 데이터시트에서 실제 확인한 범위로 한정한다.


## 7. 2026-11-12 추가 공식 자료 변경 감시 결과

### TI SLAAE29 Rev B — 공식 인덱스 메타데이터 재확인
- TI 공식 MSPM0G3506 제품 페이지의 Technical documentation 목록에 *Cybersecurity Enablers in MSPM0 MCUs (Rev. B)*, 2026-08-27이 표시된다: https://www.ti.com/product/MSPM0G3506
- 별도 TI 공식 제품 페이지 검색 결과에서도 동일 문서명/Rev B/날짜가 표시되지만, 이 세션에서 TI PDF/HTML 본문 링크를 안정적으로 열지 못했다.
- 판정: Rev B 문서가 공식 기술자료 목록에 등록된 메타데이터는 확인. Rev B의 본문 내용, Rev A와의 차이, MSPM0G3529-Q1에 대한 적용성은 UNVERIFIED. Rev B 내용을 인용하지 않고 SLAAE29A Rev A의 분석만 유지한다.

### TI MSPM0 G-Series TRM Rev F
- TI 공식 MSPM0-DIAGNOSTIC-LIB 기술자료 인덱스에 *MSPM0 G-Series 80-MHz Microcontrollers Technical Reference Manual (Rev. F)*, 2026-11-05가 표시된다: https://www.ti.com/tool/MSPM0-DIAGNOSTIC-LIB
- 문헌번호 SLAU846 확인 기록은 유지한다. 대용량 PDF/HTML 본문을 이번 세션에서 열람하지 못했으므로 보안 관련 장/레지스터 상세 내용은 검증하지 않았다.

### ST AN5156
- ST 공식 문서 페이지는 AN5156 Rev 14, June 2026을 표시한다: https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html
- 해당 문서는 제품군별 개요이며 정확한 MCU 주문 코드의 기능 보증 자료가 아니다. part-specific datasheet/RM/errata 대조가 계속 필요하다.

**운영 규칙:** 공식 인덱스에 개정판이 표시된 사실과 개정판 본문 내용 검증을 별개로 기록한다. URL/검색 스니펫만으로 기능 상세 claim을 승격하지 않는다.
