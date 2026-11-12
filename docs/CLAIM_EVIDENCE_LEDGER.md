# 주장·근거 정정 대장 (Claim Evidence Ledger)

**목적:** 기존 조사 아카이브와 향후 설계 보고서의 핵심 주장을 원본 파일·원문 위치·정확한 출처·정정·검증 상태와 연결한다.  
**기준일:** 2026-11-12  
**작업 브랜치:** `cra-project-foundation`

## 1. 상태 정의

- VERIFIED: 지정된 출처의 문서 내용과 위치를 직접 확인. 이 상태는 출처에 적힌 주장만 검증하며 제품 전체의 CRA 적합성을 뜻하지 않는다.
- PARTIALLY_VERIFIED: 일부 내용만 확인되거나 제품별 적용 조건이 남아 있음.
- UNVERIFIED: 원문/부품별 적용성/제품 사실 확인 전.
- CONFLICT: 기존 주장과 공식 출처가 충돌.
- OUTDATED: 이전 revision으로 대체됨.
- NOT_APPLICABLE: 제품 사실에 근거해 비적용 판단 완료.

## 2. 필수 레코드 스키마

| 필드 | 설명 |
|---|---|
| claim_id | 고유 ID |
| claim_text | 하나의 검증 가능한 원자적 주장 |
| claim_type | legal_fact / technical_fact / interpretation / recommendation / assumption |
| source_id | 제조사/법령 source register ID |
| source_title | 문서명 |
| publisher | 발행 기관 |
| canonical_url | 공식 URL |
| document_version | revision / 발행일 |
| source_location | 조항·절·표·페이지·행 등 |
| source_excerpt | 확인한 최소 원문 또는 정확한 paraphrase |
| assessment | 확인된 내용과 범위 |
| correction | 기존 주장과 다를 경우 정정 내용 |
| product_scope | 문서 일반/특정 MCU/완제품/제품군 |
| status | 위 상태값 |
| verification_date | 확인일 |
| open_questions | 추가로 확인할 내용 |

## 3. 초기 검증 레코드 — 제조사 공식 자료

| Claim ID | 원자적 주장 | 유형 | 출처 및 정확한 위치 | 검증 범위 / 판정 | 상태 |
|---|---|---|---|---|---|
| ST-001 | AN5156 Rev 14는 STM32 MCU 보안의 공격 유형, 하드웨어·소프트웨어 보호, 시리즈별 보안 기능 및 시스템 설계 지침을 설명한다. | technical_fact | ST-AN5156, Rev 14 June 2026, Introduction 및 Table 1 / https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html | 문서 목적과 적용 대상 제품군 목록 확인. 각 시리즈에 기능이 모두 동일하게 존재한다는 뜻은 아님. | VERIFIED |
| ST-002 | STM32의 보안 기능은 시리즈·부품별로 다르며, 정확한 Reference Manual 및 제품 자료를 통해 기능 가용성을 확인해야 한다. | technical_fact | ST-AN5156, General information 및 linked “Security features by STM32 devices” tables / 위 ST-AN5156 URL | 제품군별 표가 존재하고, 개별 기능의 존재 여부/구현은 각 제품 reference manual로 확인하라고 명시. 실제 사용 ST MCU 미확정. | VERIFIED (문서 원칙) / 제품 적용 UNVERIFIED |
| ST-003 | ST의 설계 가이드는 secure boot(SB)와 secure firmware update(SFU)를 암호 기반 애플리케이션 및 비밀 보호와 함께 설계하도록 제시한다. | technical_fact | ST-AN5156, Guidelines, Table 18, use cases 4.2–4.3 / 위 ST-AN5156 URL | 가이드의 권고/설계 예시로 확인. 모든 STM32 부품이 동일한 SB/SFU 패키지를 지원한다는 의미가 아님. | VERIFIED (가이드 내용) / 제품 적용 UNVERIFIED |
| ST-004 | ST AN4992는 SFI를 제조 과정에서 OEM 펌웨어를 기밀성·진위성·무결성 검사와 함께 STM32 내부 Flash에 설치하는 보안 기능으로 설명한다. | technical_fact | ST-AN4992 Rev 19 July 2026, Introduction / https://www.st.com/content/st_com/en/technical-documents/an4992-introduction-to-secure-firmware-install-sfi-for-stm32-mcus-stmicroelectronics.html | SFI는 제조 프로비저닝 시나리오이며 현장 펌웨어 업데이트(SFU)와 같은 기능으로 취급하지 않는다. 부품별 지원 목록 확인 필요. | VERIFIED (문서 내용) / 제품 적용 UNVERIFIED |
| TI-001 | MSPM0G3529-Q1 데이터시트는 CPU 80 MHz Cortex-M0+, Flash 최대 512 KB, SRAM 128 KB 및 dual-bank/address swap을 명시한다. | technical_fact | TI-DS-3529 SLASFO2B Rev B, §§1, 3, 4 / https://www.ti.com/lit/ds/symlink/mspm0g3529-q1.pdf | 정확한 주문 코드 MSPM0G3529-Q1에 대한 데이터시트 확인. | VERIFIED |
| TI-002 | MSPM0G3529-Q1 데이터시트는 AES-128/256 가속, GCM/GMAC, CCM/CBC-MAC, CBC, CTR 모드 지원을 명시한다. | technical_fact | TI-DS-3529 SLASFO2B Rev B, §1 Features 및 §8.18 Security / 위 TI 데이터시트 URL | 데이터시트의 기능 설명 확인. 실제 보안 프로토콜·키관리 적합성은 별도 설계/시험 대상. | VERIFIED |
| TI-003 | MSPM0G3529-Q1 데이터시트는 secure boot, secure firmware update, debug security, code/data firewalls, customer secure code, monotonic counter, TRNG를 명시한다. | technical_fact | TI-DS-3529 SLASFO2B Rev B, §8.18 Security / 위 TI 데이터시트 URL | 데이터시트의 부품별 기능 목록 확인. CSC/BIM의 구성·운영은 TI SLAAE29A와 G-Series TRM에서 상세 확인 필요. | VERIFIED |
| TI-004 | MSPM0G3529-Q1은 AES 키 최대 4개를 위한 secure key storage를 명시한다. | technical_fact | TI-DS-3529 SLASFO2B Rev B, §8.18 및 §8.21 Keystore / 위 TI 데이터시트 URL | 키 저장 개수 및 AES engine 연계 설명 확인. 키 provisioning/rotation/revocation/zeroization의 전체 제품 정책까지 자동 보장하지 않음. | VERIFIED |
| TI-005 | MSPM0G3529-Q1 데이터시트는 TRNG의 32-bit random output 및 built-in health tests를 설명한다. | technical_fact | TI-DS-3529 SLASFO2B Rev B, §8.19 TRNG / 위 TI 데이터시트 URL | 부품 데이터시트의 TRNG 설명 확인. 상위 DRBG 구성 및 제품의 난수 사용 적절성은 별도 검증 필요. | VERIFIED |
| TI-006 | MSPM0G3529-Q1의 cybersecurity architecture는 데이터시트에 “PSA Level 1 certification targeted”로 기재되어 있다. | technical_fact | TI-DS-3529 SLASFO2B Rev B, §1 Features / 위 TI 데이터시트 URL | 목표/예정 표현 확인. 인증 취득 완료를 의미하지 않음. | VERIFIED (표현 확인) |
| TI-007 | TI SLAAE29A Rev A는 MSPM0 플랫폼의 BCR/BSL/CSC, secure boot, secure storage 및 cryptographic acceleration의 동작 구조를 설명한다. | technical_fact | TI-SLAAE29, Rev A revised December 2025, §§1.3, 2, 3, 4, 5 / https://www.ti.com/lit/an/slaae29a/slaae29a.pdf | Rev A PDF의 플랫폼 구조/예제 설명 확인. 특정 부품의 레지스터·revision별 적용은 데이터시트 및 최신 G-Series TRM과 교차 확인. | VERIFIED (Rev A 문서 내용) / 최신판 반영 PARTIALLY_VERIFIED |

## 4. 기존 아카이브 정정 큐 연결

현재 위험 기반 수동 감사 34개는 파일별 판정 문서에 기록되어 있다. 아래 큐는 각 감사 문서의 ID를 원자적 주장 단위의 ledger 레코드로 분해하기 위한 작업 대기열이다. 원본 문서의 정확한 문장·행 번호를 추가로 추출하기 전에는 이 요약을 VERIFIED 주장으로 사용하지 않는다.

| Audit batch | 대상 레코드 | 기존 감사 결과 | Ledger 처리 상태 |
|---|---|---|---|
| 초기 5개 | A-001–A-005 | 4 CONFLICT / 1 PARTIALLY_VERIFIED | 원본 문장/행 범위로 분해 필요 |
| 추가 9개 | A-006–A-015 | 7 CONFLICT / 2 PARTIALLY_VERIFIED | 원본 문장/행 범위로 분해 필요 |
| 추가 20개 | B-001–B-020 | 14 CONFLICT / 6 PARTIALLY_VERIFIED | 원본 문장/행 범위로 분해 필요 |

각 배치의 원본 파일 SHA와 상세 판정은 다음 문서에서 확인한다.
- [초기 5개 감사](ARCHIVE_MANUAL_SAMPLE_AUDIT_5_2026-11-12.md)
- [추가 9개 감사](ARCHIVE_MANUAL_AUDIT_9_2026-11-12.md)
- [추가 20개 감사](ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md)

## 5. 사용 규칙

1. 한 레코드에는 한 가지 사실만 기록한다. 여러 의무/기능을 하나의 문장으로 묶지 않는다.
2. 출처 위치를 확인하지 못한 직접 인용은 금지한다. 요약이면 paraphrase로 명시한다.
3. 출처 문서의 사실이 VERIFIED여도 특정 제품/완제품 적용은 별도 상태로 기록한다.
4. 데이터시트에 기능이 있다고 적혀 있어도 실제 설정, lifecycle, key provisioning, firmware signing/update service, test evidence가 없으면 구현 완료로 보지 않는다.
5. 제조사 기능은 CRA 요구사항과 직접 등치하지 않는다. 법령 요구 결과 → 시스템 설계 → MCU 기능 매핑 → 시험 증거를 각각 연결한다.
6. 문서 개정이 확인되면 이전 레코드는 OUTDATED 또는 revision history가 유지되는 상태로 갱신하고, 새로운 revision을 별도 source version으로 기록한다.
7. 레코드의 상태 변경은 근거 URL, 정확한 위치, 확인일 및 변경 이유를 함께 기록한다.

## 6. 다음 확장 작업

- [ ] 34개 감사 대상 원본 파일의 정확한 문장/행 범위 수집
- [ ] CONFLICT 주장별 공식 CRA 조항 원문과 정정문 연결
- [ ] 직접 인용과 요약/해석을 별도 필드로 구분
- [ ] ST 실제 MCU 주문 코드가 확보되면 부품별 기능 claims 생성
- [ ] TI G-Series TRM 최신 revision과 SLAAE29 최신 revision의 part-specific 적용성 확인
- [ ] 각 설계 권고에 시험 절차/합격 기준/증거 산출물 연결


| TI-008 | TI의 MSPM0G3506 제품 기술자료 목록에는 *Cybersecurity Enablers in MSPM0 MCUs* Rev B, 2026-08-27이 표시된다. | technical_fact | TI MSPM0G3506 official technical-document index / https://www.ti.com/product/MSPM0G3506, Technical documentation list | 최초 인덱스 확인은 유지. Rev B 본문은 이후 TI HTML 문서 뷰어에서 직접 확인됨(TI-014..017 참조). MSPM0G3529-Q1 직접 적용성은 지원 부품 목록에 없어 미확인. | VERIFIED (metadata) / product applicability UNVERIFIED |


## 7. TI G-Series 최신 문서 확인 추가 레코드 (2026-11-12)

| Claim ID | 원자적 주장 | 유형 | 출처 및 정확한 위치 | 검증 범위 / 판정 | 상태 |
|---|---|---|---|---|---|
| TI-009 | TI MSPM0G3529-Q1 제품 페이지는 전체 모듈 설명을 위해 MSPM0 G-Series 80MHz Technical Reference Manual을 참조하도록 안내한다. | technical_fact | TI MSPM0G3529-Q1 product page, description / https://www.ti.com/product/MSPM0G3529-Q1 | 제품 페이지의 문서 참조 문구 확인. 해당 TRM 내 특정 보안 레지스터/기능의 부품 적용성은 별도 확인 필요. | VERIFIED |
| TI-010 | TI MSPM0-DIAGNOSTIC-LIB 공식 기술자료 인덱스는 MSPM0 G-Series 80-MHz Technical Reference Manual Rev F, 2026-11-05를 표시한다. | technical_fact | TI MSPM0-DIAGNOSTIC-LIB page, Technical documentation table / https://www.ti.com/tool/MSPM0-DIAGNOSTIC-LIB | 인덱스에 문서명·Rev F·날짜가 표시됨. PDF/HTML 본문을 가져오지 못했으므로 Rev F의 내용은 검증하지 않음. | VERIFIED (index metadata only) |
| TI-011 | SLAAE29 Rev B 본문이 현재 TI 공식 링크에서 확인되었다. | technical_fact | TI SLAAE29B HTML document viewer / https://www.ti.com/document-viewer/lit/html/SLAAE29 | 이번 세션에서 본문 직접 확인에 성공. Revision history 및 CSC/KEYSTORE/AESADV/TRNG 섹션 확인. 구체 주장과 part scope는 TI-014..017에 분리. | VERIFIED (document body) / MSPM0G3529-Q1 applicability UNVERIFIED |

**TI-008/011 처리 메모(2026-11-12 갱신):** 최초 인덱스만 확인했던 상태는 TI HTML viewer에서 Rev B 본문을 직접 열어 확인함으로써 갱신되었다. Rev B의 문서 수준 사실은 TI-014..017에 등록했다. 다만 SLAAE29B 머리말의 supported-device list에 MSPM0G3529-Q1이 없으므로, 이 Rev B 예제의 해당 부품 적용성은 UNVERIFIED로 유지한다.


## 8. 기존 아카이브 34개 고유 표본의 원자적 정정 대장

[ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md)에 초기 5개 + 추가 9개 고유 파일 + 추가 20개 파일의 원본 경로, SHA-1 blob, 원문 행 위치, 핵심 주장, CRA 정정 룰 ID 및 감사 상태를 연결했다.

- 고유 원본 파일: 34개
- 고유 파일 기준 판정: 25 CONFLICT / 9 PARTIALLY_VERIFIED
- 감사 ID는 35개이며, A-013과 B-006이 동일 원본 파일/SHA이므로 1건 중복 제거
- 원본 archive는 수정하지 않음
- 이 정정 대장은 표본 자료에 대한 추적성 기록이며, 990개 전체 전수 검증이 아님


## 9. 2026-11-12 공식 가이드 및 제조사 개정판 메타데이터

| Claim ID | 원자적 주장 | 유형 | 출처 및 정확한 위치 | 검증 범위 / 판정 | 상태 |
|---|---|---|---|---|---|
| EU-GUIDE-001 | European Commission은 2026-07-27 CRA 적용 실무 가이드 C(2026) 5252를 공식 게시했다. | official_publication_fact | Commission publication page, publication date / https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation | 공식 게시 페이지에서 문서명, 게시일, 주요 주제 및 non-binding 안내를 확인. Annex 본문 문단/페이지별 직접 검증은 별도 진행. | VERIFIED (publication metadata only) |
| TI-012 | TI 공식 MSPM0G3506 기술자료 목록은 *Cybersecurity Enablers in MSPM0 MCUs (Rev. B)*, 2026-08-27을 표시한다. | technical_fact | TI MSPM0G3506 product page, Technical documentation list / https://www.ti.com/product/MSPM0G3506 | 공식 제품 페이지 목록의 문서명·Rev B·날짜만 확인. Rev B 본문 및 MSPM0G3529-Q1 적용성은 검증하지 않음. | VERIFIED (index metadata only) |
| TI-013 | TI 공식 MSPM0-DIAGNOSTIC-LIB 기술자료 인덱스는 MSPM0 G-Series TRM Rev F, 2026-11-05를 표시한다. | technical_fact | TI MSPM0-DIAGNOSTIC-LIB, Technical documentation table / https://www.ti.com/tool/MSPM0-DIAGNOSTIC-LIB | 인덱스 메타데이터만 확인. 본문 보안 장/레지스터 내용은 미확인. | VERIFIED (index metadata only) |
| ST-002 | ST 공식 AN5156 페이지는 Rev 14, June 2026을 표시한다. | technical_fact | ST AN5156 official page / https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html | 문서 revision/date와 범위 확인. 특정 MCU 기능은 part-specific 자료가 필요. | VERIFIED (document metadata only) |

**주의:** 위 VERIFIED는 게시/문서 메타데이터 사실만을 의미한다. 가이드 해석, TI Rev B/TRM Rev F 본문 내용, ST 특정 부품 기능의 VERIFIED를 의미하지 않는다.

## 10. TI SLAAE29 Rev B 본문 및 main-only 보고서 #35 감사

| Claim ID | 원자적 주장 | 유형 | 출처 및 정확한 위치 | 검증 범위 / 판정 | 상태 |
|---|---|---|---|---|---|
| TI-014 | SLAAE29 Rev B는 Rev A 대비 MSPM0L211x/G511x/G321x 지원표 갱신, 256-byte vector alignment, AESADV DMA element size 성능표 갱신을 기록한다. | technical_fact | TI SLAAE29B, §9 Revision History / https://www.ti.com/document-viewer/lit/html/SLAAE29 | Rev B HTML 본문 직접 확인. | VERIFIED |
| TI-015 | SLAAE29B 문서의 머리말 지원 부품 목록에는 MSPM0G3529-Q1이 포함되지 않는다. | technical_fact | TI SLAAE29B document header / 위 URL | 문서 목록에 포함된 device IDs를 직접 확인. 이 문서에서 G3529-Q1의 CSC/KEYSTORE/TRNG 기능을 입증할 수 없음. | VERIFIED (문서 scope list only) |
| TI-016 | SLAAE29B §3.2.1은 CSC 예제에서 rollback check 및 AES-CMAC 또는 SHA-256+ECDSA 기반 이미지 검증 흐름을 설명한다. | technical_fact | TI SLAAE29B §3.2.1 / https://www.ti.com/document-viewer/lit/html/SLAAE29B/GUID-A5D8BF2B-16E3-460E-9288-A0EB8F6E7431 | 문서 예제 내용 확인. G3529-Q1 적용성은 입증되지 않음. | VERIFIED (document example) / product application UNVERIFIED |
| TI-017 | SLAAE29B §4.5는 CSC가 INITDONE 전 KEYSTORE를 설정하고, INITDONE 이후 애플리케이션은 저장 키를 직접 읽거나 쓸 수 없다고 설명한다. | technical_fact | TI SLAAE29B §4.5 / https://www.ti.com/document-viewer/lit/html/SLAAE29B/GUID-5E58A744-C68A-49E7-9E40-427EB637E0C9 | 문서 설명 직접 확인. G3529-Q1 적용성은 별도 문서 확인 필요. | VERIFIED (document example) / product application UNVERIFIED |
| CRA-ARCH-035-001 | Annex I는 모든 대상 제품에 하드웨어 기반 Secure Boot를 특정 회로/체인으로 구현하라고 명시하지 않는다. | legal_fact | Regulation (EU) 2024/2847, Annex I Part I(1)–(2), Part II / https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 | Annex I 전체의 기술 중립적 결과 요구를 직접 대조. Secure Boot는 위험 기반 설계 통제 후보로 구분. | VERIFIED (법령 문언 범위) |
| CRA-ARCH-035-002 | Annex I는 TPM/Secure Element/Secure Enclave를 모든 대상 제품의 의무 부품으로 특정하지 않는다. | legal_fact | 같은 EUR-Lex 원문, Annex I Part I(2)(d)–(f), Part II(7) | 접근통제·기밀성·무결성·안전한 업데이트 결과 요구와 특정 부품 지정 여부를 분리해 확인. | VERIFIED (법령 문언 범위) |
| CRA-ARCH-035-003 | main-only 보고서 #35의 “Raw Text Quote”는 Annex I Part I(2)(b)–(d)의 실제 문구/번호와 일치한다. | legal_fact | 원본 main file research_archive/2026-11-12_025041.md, blob SHA f4bdaf84c19da80707b43f9db616712a7d17061d; EUR-Lex Annex I Part I | (b) secure-by-default, (c) security-update remediation, (d) access control임을 대조. 원본 인용은 integrity/availability/update 문구를 잘못된 항목에 배정하고 원문에 없는 문장을 합성. | CONFLICT / quote REJECTED |
| CRA-ARCH-035-004 | CRA Annex I가 모든 firmware update package에 제조자 개인키 서명을 명시적으로 요구한다. | legal_fact | EUR-Lex Annex I Part I(2)(c),(f), Part II(2),(7) | 업데이트 가능성·안전한 배포 및 무결성 요구는 확인되나, 특정 digital-signature/key architecture를 일률 지정하지 않음. | CONFLICT |

원본 #35 파일은 main 브랜치에만 존재하며 cra-project-foundation에는 포함되지 않는다. 감사는 작업 브랜치에만 기록하고 main 원본은 수정하지 않았다. 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md).

## 11. Main-only report #36 감사

| Claim ID | 원자적 주장 | 유형 | 출처 및 위치 | 검증 범위 / 판정 | 상태 |
|---|---|---|---|---|---|
| CRA-ARCH-036-001 | CRA Annex I는 모든 제품에 TPM/하드웨어 Root of Trust/Measured Boot/Secure Boot를 일률적으로 요구한다. | legal_fact | Regulation (EU) 2024/2847, Annex I Part I(1)–(2) / https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 | 특정 하드웨어/부트 구조가 보편적 법정 의무로 열거되지 않음을 원문 대조. 위험 기반 구현 통제 후보로 구분. | CONFLICT |
| CRA-ARCH-036-002 | Article 14는 무상 보안 업데이트 제공 의무를 규정한다. | legal_fact | 같은 원문 Article 13(8), Article 14(1)–(4), Annex I Part II(8) | Article 14는 actively exploited vulnerability/severe incident 신고; 무상 보안 업데이트는 Part II(8), 지원기간은 Article 13(8). | CONFLICT |
| CRA-ARCH-036-003 | Annex I Part I(2)(b),(c),(g)는 데이터 변조 방지, Secure Boot, 취약점 업데이트를 각각 규정한다. | legal_fact | 같은 원문 Annex I Part I(2)(b),(c),(e),(f),(g),(h) | (b) secure-by-default, (c) update remediation, (g) data minimisation. 원본은 기밀성/무결성 문구를 혼합하고 secure boot 문장을 창작. | CONFLICT / quote REJECTED |
| CRA-ARCH-036-004 | CRA 정식 제목은 Regulation (EU) No 165/2014 및 Directive (EU) 2019/1939를 개정한다고 적는다. | legal_fact | 같은 원문 document title, EUR-Lex lines 160–161 / URL above | 정식 제목은 Regulations (EU) No 168/2013 및 (EU) 2019/1020, Directive (EU) 2020/1828의 개정을 명시. | CONFLICT |

원본 main 파일 research_archive/2026-11-12_025529.md, blob SHA 0d5b3f17b13f8935a90c23400173e401a76e1953, commit 5cd4a18dbf5dc4712d669b29b8846af799f5efc1. 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md). 원본은 main에 보존하고 수정하지 않았다.
