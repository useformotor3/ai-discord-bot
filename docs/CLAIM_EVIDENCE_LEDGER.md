# 주장·근거 정정 대장 (Claim Evidence Ledger)

> **언어 원칙:** 이 대장의 설명·판정 사유·정정 내용은 한국어를 기본으로 작성한다. 법령명, 공식 문서명, 조항 번호, 제조사 원문 인용 및 상태 코드(VERIFIED 등)는 원문 식별을 위해 영어를 유지할 수 있다.

**목적:** 기존 조사 아카이브와 향후 설계 보고서의 핵심 주장을 원본 파일·원문 위치·정확한 출처·정정·검증 상태와 연결한다.  
**기준일:** 2026-11-13  
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

## 12. Main-only reports #37–#39 감사

| Claim ID | 주장 | 법령 근거 | 검증 결과 | 상태 |
|---|---|---|---|---|
| CRA-ARCH-037-001 | 지원기간/무상 업데이트 문구가 Annex I Part II의 단일 인용문이며 Article 11이 구체적 근거다. | Regulation (EU) 2024/2847 Article 13(8), Annex I Part II(8) | 원본 인용은 현행 원문과 일치하지 않는 합성 문구. Article 11 대신 구체 지원기간 Article 13(8), 무상 업데이트 Part II(8)로 구분 | CONFLICT / quote REJECTED |
| CRA-ARCH-037-002 | 지원기간은 예상수명과 5년 중 무조건 더 긴 기간이다. | Article 13(8), 특히 support period 문단 | 최소 5년 원칙이나 제품 예상 사용기간이 5년 미만이면 예상 사용기간으로 정함. 예외를 생략하면 오도 | CONFLICT |
| CRA-ARCH-038-001 | Annex I Part II의 (a)–(d) 인용은 원문 항목이다. | Annex I Part II(1)–(8) | Part II는 제조자 의무 8개 번호 항목. 원본 (a)–(d) 문구는 번호/본문 모두 일치하지 않음 | CONFLICT / quote REJECTED |
| CRA-ARCH-038-002 | Article 13(2)에 expected lifetime/5 years/whichever shorter 무상 업데이트 문구가 있다. | Article 13(2),(8), Annex I Part II(8) | Article 13(2)는 위험평가 의무. 원본 문구는 해당 조항에 존재하지 않는 합성 인용. 지원기간은 13(8), 무상 업데이트는 Part II(8) | CONFLICT |
| CRA-ARCH-039-001 | Article 13(6)은 지원기간 및 무료 보안 업데이트를 규정한다. | Article 13(6),(8), Annex I Part II(8) | 13(6)은 통합된 구성요소 취약점의 원 공급자 통지/수정 관련. 지원기간 13(8), 무료 업데이트 Part II(8) | CONFLICT |
| CRA-ARCH-039-002 | Annex I Part I(2)(b)는 자동 업데이트/업데이트 알림 요건이다. | Annex I Part I(2)(b),(c) | (b)는 secure-by-default 및 원래 상태 reset, 자동 보안 업데이트/통지는 (c) | CONFLICT / quote REJECTED |

**공식 원문 위치:** EUR-Lex Article 13(2),(6),(8) lines 888–908; Annex I Part I(2)(b),(c) 및 Part II(1)–(8) lines 1747–1773. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

상세 파일: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md). 원본 main archive는 수정하지 않았다.

## 13. Main-only reports #40–#55 (batch audit)

| Claim ID | Atomic claim / audit focus | Source location | Result | Status |
|---|---|---|---|---|
| CRA-ARCH-040-001 | CRA requires secure-by-default configuration and limits attack surfaces. | Annex I Part I(2)(b),(j) | Substantive requirements exist, but report's direct quotations are not exact and concrete port/account controls are implementation examples, not universal text. | PARTIALLY_VERIFIED |
| CRA-ARCH-041-001 | Annex I Part I subpoints (a)–(f) quoted in report #41 match source. | Annex I Part I(2)(a)–(m) | Report's numbering and wording do not match official source. | CONFLICT / quote REJECTED |
| CRA-ARCH-042-001 | “secure by default enforcement mechanisms” and cited access-control text are verbatim CRA clauses. | Annex I Part I(2)(b),(d) | Phrase/structure not source-verbatim; source wording differs. | CONFLICT / quote REJECTED |
| CRA-ARCH-043-001 | Industrial servo drives are automatically Important Class I and report quotes Annex I accurately. | Annex III Class I categories; Annex I Part I | Servo-drive classification not established by product name; quotation composite/non-verbatim. | CONFLICT |
| CRA-ARCH-044-001 | Article 11 requires reporting all vulnerabilities/incidents within 24h and 72h. | Article 14(1)–(5) | Reporting clause is Article 14; only actively exploited vulnerabilities and severe incidents; different final-report clocks. | CONFLICT |
| CRA-ARCH-045-001 | CRA mandates free updates under Annex I Part I(2)(h), RSA/ECDSA signing and dual-bank rollback. | Annex I Part II(7)–(8); Part I(2)(c),(f),(h) | Free update is Part II(8); specific algorithms, dual-bank and rollback not universally prescribed by cited text. | CONFLICT |
| CRA-ARCH-046-001 | Article 14 requires all vulnerability reporting and automated telemetry/EN 18031 for generic servo drives. | Article 14(1)–(7); Annex I Part I(2) | Scope/timing and quote are inaccurate; automatic telemetry not prescribed; EN 18031 scope/product applicability not demonstrated. | CONFLICT |
| CRA-ARCH-047-001 | CRA mandates safety-core segregation, STO safe state and SIL 3 update architecture. | Article 13(2); Annex I Part I/II | Risk assessment must consider health/safety impacts; specific SIL/STO/core architecture is not stated as a universal CRA requirement. | CONFLICT |
| CRA-ARCH-048-001 | Annex I Part I(1)(h) and Recital 28 contain the quoted safety-update requirements. | Annex I Part I(2)(h); Recital 28 | Cited point concerns availability/DoS resilience; quote not found at cited legal location. | CONFLICT / quote REJECTED |
| CRA-ARCH-049-001 | CRA requires secure decommissioning instructions and secure user-data removal. | Annex II point 8(d); Annex I Part I(2)(m) | Core obligation is supported, but archive mislabels Annex II as Annex VII and overstates cryptographic erasure/advance notice. | PARTIALLY_VERIFIED |
| CRA-ARCH-050-001 | CRA mandates zero-downtime/hot-patching as part of free security updates. | Annex I Part II(7)–(8) | Free security updates supported; zero-downtime/hot-patch is not a prescribed universal implementation. | CONFLICT |
| CRA-ARCH-051-001 | Article 14 and Annex II establish the five-year support period and free patch requirement. | Article 13(8); Annex I Part II(8); Annex II point 7 | Article mapping wrong; under-five-year expected-use exception omitted; quote not verbatim. | CONFLICT |
| CRA-ARCH-052-001 | Article 10(6) and Annex I labels require dual-bank, hot-patch and zero-downtime. | Article 13(8); Annex I Part II(2),(7),(8) | Article/Annex references wrong; implementation architecture is not universally mandated. | CONFLICT |
| CRA-ARCH-053-001 | Article 13(6) is support-period/free-update clause and Part I(2)(g) is DoS/update clause. | Article 13(6),(8); Annex I Part I(2)(g),(h); Part II(8) | 13(6) concerns integrated component vulnerabilities; (g) is data minimisation; free updates are Part II(8). | CONFLICT |
| CRA-ARCH-054-001 | Article 13(4) and Annex I point (h) contain the quoted five-year/free-update rule. | Article 13(4),(8); Annex I Part II(8) | 13(4) concerns technical documentation of risk assessment; cited quote is not source-verbatim. | CONFLICT |
| CRA-ARCH-055-001 | Annex I Part I Section 2 point (h) requires zero-downtime updates free of charge. | Annex I Part II(7)–(8) | Annex structure and quote wrong; free-of-charge rule has tailor-made business-user exception. | CONFLICT |

Detailed file-level audit: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_40_55_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_40_55_2026-11-12.md). Original main archive files remain unchanged.

## 14. TI Rev F and product-page claims (2026-11-12)

| Claim ID | Atomic claim | Source | Assessment | Status |
|---|---|---|---|---|
| TI-TRM-REVF-001 | TI MSPM0 G-Series 80-MHz TRM Rev F is listed on the official MSPM0G3507 product page with date 2026-11-05. | TI MSPM0G3507 official page, Technical documentation list | Page lists Rev F and date; this verifies publication metadata only, not the body. | VERIFIED (metadata only) |
| TI-TRM-REVF-002 | The full Rev F security chapter/register descriptions and Rev E→F changes were reviewed. | TI MSPM0 G-Series TRM Rev F | Viewer content is 25,348,105 bytes and cannot be rendered here; PDF open inaccessible. | NOT_VERIFIED |
| TI-G3507-001 | MSPM0G3507 page lists AES, TRNG, CRC, flash ECC, SRAM parity option, MPU, SWD and security-related product descriptors. | TI MSPM0G3507 official product page | Verified as a page-level claim for MSPM0G3507; must confirm in exact order-code datasheet/TRM/errata before design reliance. | PARTIALLY_VERIFIED (device applicability only) |
| TI-G3529-001 | MSPM0G3507 product-page feature list proves the same features for MSPM0G3529-Q1. | TI MSPM0G3507 page vs G3529-Q1 datasheet/support list | Different part/order code; cross-device inference is invalid. | REJECTED |
| TI-SLAAE29B-APPL-001 | SLAAE29B CSC/KEYSTORE/TRNG examples automatically apply to MSPM0G3529-Q1. | SLAAE29B supported-device scope | G3529-Q1 not listed in supported-device list reviewed; direct applicability not established. | NOT_ESTABLISHED |

## 15. Main-only reports #56–#59 (2026-11-12)

| Claim ID | Atomic claim / audit focus | Source location | Assessment | Status |
|---|---|---|---|---|
| CRA-ARCH-056-001 | Article 14 mandates automatic reporting of all exploitable vulnerabilities and severe incidents within 24/72h. | Article 14(1)–(4); Article 16(3) | Only actively exploited vulnerabilities and severe incidents are mandatory tracks; separate final-report clocks; platform routes via CSIRT and ENISA; no manufacturer-side automatic reporting mandate. | CONFLICT |
| CRA-ARCH-057-001 | CVD policy and contact address are Annex I Part I Section 2 obligations with the report's quoted wording. | Annex I Part II(5),(6); Annex II point 2 | Core CVD/contact requirements are real, but cited Part/Section is wrong and quote is composite/non-verbatim. | PARTIALLY_VERIFIED / quote REJECTED |
| CRA-ARCH-058-001 | CRA explicitly requires disabling all nonessential ports/debug interfaces and mandatory first-boot password change. | Annex I Part I(2)(b),(d),(j) | Secure-by-default/access control/attack-surface requirements are real; these concrete controls are risk-based design options, not universal express commands. | PARTIALLY_VERIFIED / quote REJECTED |
| CRA-ARCH-059-001 | Article 13(2) requires free security patches and Annex I Part I Section 1 subpoints (a),(b) quote secure-by-default/free update rules. | Article 13(2),(8); Annex I Part I(2)(b); Part II(8) | Article 13(2) is risk assessment; support period and free updates are separate provisions; quote/reference inaccurate. | CONFLICT |

Detailed audit: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_56_59_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_56_59_2026-11-12.md).


## 20. main 보고서 #60–#78 감사 (2026-11-12)

Detailed file-level findings: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md).

| Claim ID | Original report | Atomic claim / correction | Status |
|---|---|---|---|
| CRA-ARCH-060-001 | #60 | CVD is Annex I Part II(5); free security updates are Part II(8); Part I(2)(g) is data minimisation, not updates. | PARTIALLY_VERIFIED |
| CRA-ARCH-061-001 | #61 | Secure-by-default is Part I(2)(b); attack-surface limitation is Part I(2)(j); mandatory MFA/forced password change/blanket port disablement are not universal express commands. | PARTIALLY_VERIFIED |
| CRA-ARCH-062-001 | #62 | Article 13(7) is systematic documentation, not free updates or support period; cited Part I numbering is invalid. | CONFLICT |
| CRA-ARCH-063-001 | #63 | Secure-by-default and attack-surface limitation are valid themes, but cited paragraph/letter locations are wrong; blanket interface disablement is an implementation choice. | PARTIALLY_VERIFIED |
| CRA-ARCH-064-001 | #64 | Article 13(7) and Part I(2)(g) do not establish free-patch duty; Part I(2)(g) is data minimisation. | CONFLICT |
| CRA-ARCH-065-001 | #65 | Article 13(6) concerns integrated-component vulnerabilities; Article 13(8) support period has an exception where expected use is under five years. | CONFLICT |
| CRA-ARCH-066-001 | #66 | Article 14(2) is not a free-update clause; Article 14 governs mandatory reporting. | CONFLICT |
| CRA-ARCH-067-001 | #67 | Automatic updates are conditional where applicable; free updates are Part II(8), and the quote is composite/non-verbatim. | CONFLICT |
| CRA-ARCH-068-001 | #68 | Article 11 is general product safety; support period is Article 13(8), free updates Part II(8). | CONFLICT |
| CRA-ARCH-069-001 | #69 | Part I(2)(g) is data minimisation and (h) availability/DoS resilience; neither is the quoted telemetry opt-in/update rule. | CONFLICT |
| CRA-ARCH-070-001 | #70 | CRA does not universally prescribe HSM/Secure Boot/runtime integrity implementation; the cited quote is synthetic. | CONFLICT |
| CRA-ARCH-071-001 | #71 | Article 11(2) is not the claimed free-update/CVD provision; CVD is Part II(5), free updates Part II(8). | CONFLICT |
| CRA-ARCH-072-001 | #72 | Article 14(3) is severe-incident reporting; support period is Article 13(8), free updates Part II(8). | CONFLICT |
| CRA-ARCH-073-001 | #73 | Article 13(8) correctly identifies support period, but Part I(2)(g) is data minimisation and the quoted Article 13(8) text is not authentic. | PARTIALLY_VERIFIED |
| CRA-ARCH-074-001 | #74 | Article 14(3) is severe-incident reporting; Part II(1) is SBOM identification/documentation, not update automation. | CONFLICT |
| CRA-ARCH-075-001 | #75 | Five-year support rule omits the expected-use-under-five-years exception; Part II(2) is not the quoted free-update clause. | CONFLICT |
| CRA-ARCH-076-001 | #76 | Part II(8) supports timely/free updates subject to tailor-made exception; cited Part I(2)(g) is wrong and quote is not verbatim. | PARTIALLY_VERIFIED |
| CRA-ARCH-077-001 | #77 | Secure-by-default/attack-surface principles are valid; mandatory password/port/debug/signature implementation details are overstated. | PARTIALLY_VERIFIED |
| CRA-ARCH-078-001 | #78 | Article 13(8) is support period, but the quote is fabricated/oversimplified; free updates are Part II(8). | CONFLICT |

**Batch totals:** 19 files; 6 PARTIALLY_VERIFIED; 13 CONFLICT; 0 fully VERIFIED. No Raw Text Quote block from #60–#78 is cleared for verbatim reuse. These are file-level findings, not an archive-wide error rate.


## 21. main 보고서 #79 감사 (2026-11-12)

Detailed findings: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md).

| Claim ID | Original report | Atomic claim / correction | Status |
|---|---|---|---|
| CRA-ARCH-079-001 | #79 | Article 14(1) is limited to actively exploited vulnerabilities contained in the product; stages are 24h early warning, 72h vulnerability notification, and final report within 14 days after corrective/mitigating measure becomes available. Article 14(3)–(5) separately governs severe incidents. | PARTIALLY_VERIFIED |

The 24-hour early-warning theme is supported, but the report broadens scope, mislabels the 72-hour stage as a final notification, misattributes the quote to Article 14(2), and gives a non-verbatim quotation. No quote block cleared.


## 22. TI MSPM0G3529-Q1 기능안전 출처 주장 (2026-11-12)

Detailed review: [TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md](TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md).

| Claim ID | Atomic claim | Source / location | Assessment | Status |
|---|---|---|---|---|
| TI-SAFETY-001 | SFFS983A Rev A supported-device list includes MSPM0G3529-Q1. | TI SFFS983A header, https://www.ti.com/document-viewer/lit/html/SFFS983A | Direct supported-device list includes exact order code. | VERIFIED |
| TI-SAFETY-002 | SFFS983A §2 describes the Gx51x/Gx52x component as SEooC, developed to relevant ISO 26262:2018 requirements, with systematic integrity ASIL D and random-fault mechanisms up to ASIL B. | TI SFFS983A §2, https://www.ti.com/document-viewer/lit/html/SFFS983A/GUID-0E1AF9E3-352B-463D-B3C3-2CF2CDCB4E58 | Component-level statements only; not a complete-system or SIL 3 certification. | VERIFIED (component manual statement) |
| TI-SAFETY-003 | SFFS983A §4.3 assumes integrator-selected diagnostics, host-provisioned actuator disable, host communication-loss supervision, FTTI >10 ms, MPFDTI <8 h, random-fault metrics up to ASIL B and systematic requirements up to ASIL D. | TI SFFS983A §4.3, https://www.ti.com/document-viewer/lit/html/SFFS983A/GUID-6A88B39F-C64B-47C8-8816-05A909052D85 | These are stated system assumptions/conditions; not proof the servo-drive system meets them. | VERIFIED (manual assumptions) |
| TI-SAFETY-004 | SFFS983A §4.3 treats DEBUG, RTC, AES, TRNG, KEYSTORE, MATHACL and DFT as QM/not safety-critical for this safety concept. | Same SFFS983A §4.3 URL | Do not credit these IPs as safety mechanisms without separate justification; manual says QM IPs shall not be used in safety-critical applications. | VERIFIED |
| TI-SAFETY-005 | SFFS983A §6 lists 74 functional-safety mechanism entries, including PWM safe-state, watchdog, memory/flash, clock, voltage and interface diagnostics. | TI SFFS983A §6 contents and §6.3, https://www.ti.com/document-viewer/lit/html/SFFS983A | Inventory existence verified; actual diagnostic coverage, configuration and application implementation are separate. | VERIFIED (document inventory) |
| TI-TRM-REVF-004 | TI official product page lists MSPM0 G-Series 80-MHz TRM Rev F dated 2026-11-05. | TI MSPM0G3507 page, technical documentation list, https://www.ti.com/product/MSPM0G3507 | Metadata verified; 25,348,105-byte HTML/PDF body could not be rendered. Security register/body and Rev E→F diff remain NOT_VERIFIED. | VERIFIED (metadata only) |

**Do not infer:** ASIL D equals SIL 3; the MCU alone achieves SIL 3; security IP is safety-qualified; or all 74 mechanisms are automatically implemented. Exact FMEDA values, diagnostic coverage, product architecture and system validation remain open.


| TI-SAFETY-006 | TI general functional-safety guidance says to contact local sales if a selected product's analysis report is unavailable; TI safety-collateral access may require a valid Safety NDA. | https://www.ti.com/en-us/technologies/functional-safety ; https://www.ti.com/document-viewer/lit/html/SPRAD57 | General TI access-process guidance only; exact G3529-Q1 FMEDA availability, NDA, price and delivery route are not established. | VERIFIED (general TI guidance only) |


## 23. main 보고서 #80 감사 (2026-11-12)

Detailed findings: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md).

| Claim ID | Original report | Atomic claim / correction | Status |
|---|---|---|---|
| CRA-ARCH-080-001 | #80 | Secure-by-default is Annex I Part I(2)(b), access control (d), attack-surface limitation (j); the report's Section 1 (a)–(d) quote is composite/misnumbered and universal port/debug/password/Secure Boot implementation claims are overstated. | PARTIALLY_VERIFIED |

The legal themes are supported, but the raw quote is rejected for verbatim reuse and implementation choices must remain risk-based.


## 24. main 보고서 #81–#121 감사 (2026-11-12)

Detailed report: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md). Source main HEAD: d0ba9802e4b7fead4192263d8ebd08f44a7c547e.

| Claim ID | Report | Finding | Status |
|---|---:|---|---|
| CRA-ARCH-081-001 | #81 | 기본 자격증명 금지/강제 변경 문구 및 인용 합성 | CONFLICT |
| CRA-ARCH-082-001 | #82 | 지원기간 shorter-than-five-years 예외 역전, Annex 인용 조작 | CONFLICT |
| CRA-ARCH-083-001 | #83 | Annex 번호/인용 조작, 보편적 자격증명·포트 의무 과장 | CONFLICT |
| CRA-ARCH-084-001 | #84 | secure-default 주제 일부 타당, 인용·하위항목·비밀번호 의무 오류 | CONFLICT |
| CRA-ARCH-085-001 | #85 | 기본 보안/업데이트 무결성 취지는 타당, Secure Boot 보편 의무 및 인용 오류 | PARTIALLY_VERIFIED |
| CRA-ARCH-086-001 | #86 | 기본 보안/무결성 취지는 타당, 인용과 구현 의무 과장 | PARTIALLY_VERIFIED |
| CRA-ARCH-087-001 | #87 | Secure Boot/Root of Trust 법적 의무 및 Annex 인용 조작 | CONFLICT |
| CRA-ARCH-088-001 | #88 | Annex I Part I/II 혼합, 합성 인용 | CONFLICT |
| CRA-ARCH-089-001 | #89 | 인터페이스/Secure Boot 보편 의무와 Annex 하위항목 조작 | CONFLICT |
| CRA-ARCH-090-001 | #90 | Secure Boot/rollback 보편 의무 및 기술문서 보관기간 오인용 | CONFLICT |
| CRA-ARCH-091-001 | #91 | SBOM 근거 Annex I Part II(1) 오인용, Article 13 인용 합성 | CONFLICT |
| CRA-ARCH-092-001 | #92 | Secure Boot 보편 의무, Annex VII/Article 24 인용 오류 | CONFLICT |
| CRA-ARCH-093-001 | #93 | 서명·dual-bank·무중단 업데이트를 법적 의무로 과장 | CONFLICT |
| CRA-ARCH-094-001 | #94 | 지원기간 shorter/longer 규칙 역전, 합성 인용 | CONFLICT |
| CRA-ARCH-095-001 | #95 | Annex VII/Part I 하위항목 오인용, 지원기간 문구 합성 | CONFLICT |
| CRA-ARCH-096-001 | #96 | 지원기간 longer 오인, IEC 62443 SL2를 CRA와 혼동 | CONFLICT |
| CRA-ARCH-097-001 | #97 | CVD/contact 주제는 타당하나 Article 14·Annex 번호/인용 오류 | CONFLICT |
| CRA-ARCH-098-001 | #98 | 기본 보안·접근제어 취지는 타당, MFA/RBAC/고유 비밀번호 보편 의무 과장 | PARTIALLY_VERIFIED |
| CRA-ARCH-099-001 | #99 | Article 13(6) third-party component 처리 취지 과장 및 합성 인용 | CONFLICT |
| CRA-ARCH-100-001 | #100 | 무상 업데이트 근거 Annex I Part II(8) 대신 Part I(2)(g) 오인용 | CONFLICT |
| CRA-ARCH-101-001 | #101 | Article 14 신고 범위·원격 telemetry 자동 신고 의무 과장 | CONFLICT |
| CRA-ARCH-102-001 | #102 | 지원기간 longer 오인, Part II 하위항목·인용 조작 | CONFLICT |
| CRA-ARCH-103-001 | #103 | Annex I Part II/Article 13(4) 세부 인용 조작 | CONFLICT |
| CRA-ARCH-104-001 | #104 | 기본 보안/접근제어 취지는 타당, 포트·암호·RBAC 보편 의무 과장 | PARTIALLY_VERIFIED |
| CRA-ARCH-105-001 | #105 | 기본 보안 취지는 타당, Annex 인용과 초기 인증 의무 오류 | PARTIALLY_VERIFIED |
| CRA-ARCH-106-001 | #106 | Article 14를 모든 취약점/사고로 확대, 인용 합성 | CONFLICT |
| CRA-ARCH-107-001 | #107 | 제품 Class II 추정 근거 없음, free update 및 Annex 인용 조작 | CONFLICT |
| CRA-ARCH-108-001 | #108 | 지원기간/무상업데이트 혼합, 자동업데이트·서명 의무 과장 | CONFLICT |
| CRA-ARCH-109-001 | #109 | 존재하지 않는 Article 11(7), 지원기간/무료 업데이트 오인용 | CONFLICT |
| CRA-ARCH-110-001 | #110 | Article 11 및 Annex 인용 오류, 직접 인용 합성 | CONFLICT |
| CRA-ARCH-111-001 | #111 | Article 13(8) 지원기간과 무상 업데이트 의무 혼동 | CONFLICT |
| CRA-ARCH-112-001 | #112 | 존재하지 않는 Article 14(2)(h)/Part II(1)(f) 인용 | CONFLICT |
| CRA-ARCH-113-001 | #113 | Annex I Part I/II 번호와 문구 조작, 예외 누락 | CONFLICT |
| CRA-ARCH-114-001 | #114 | Article 14를 secure update 의무로 오인, 서명·rollback 과장 | CONFLICT |
| CRA-ARCH-115-001 | #115 | Annex I 문자 번호/인용 조작, unique credential 의무 과장 | CONFLICT |
| CRA-ARCH-116-001 | #116 | Article 11 및 Annex I Part II CVD 인용 합성 | CONFLICT |
| CRA-ARCH-117-001 | #117 | secure-default/reset 취지는 타당, 비밀번호/포트 보편 의무 과장 | PARTIALLY_VERIFIED |
| CRA-ARCH-118-001 | #118 | Annex I Part I point (g) 인용 조작, 디지털 서명 의무 과장 | CONFLICT |
| CRA-ARCH-119-001 | #119 | 지원기간 주제는 타당하나 Article 10 오인용, 5년 예외 누락 | PARTIALLY_VERIFIED |
| CRA-ARCH-120-001 | #120 | Article 14 대신 Article 11, 신고 대상·최종보고 기한 혼동 | CONFLICT |
| CRA-ARCH-121-001 | #121 | 지원기간/secure decommissioning 일부 타당, 사전 EOL 통지 의무·인용 과장 | PARTIALLY_VERIFIED |

**Batch result:** 41 reports; 33 CONFLICT / 8 PARTIALLY_VERIFIED / 0 VERIFIED. All 41 Raw Text Quote blocks are rejected for verbatim reuse. Consecutive risk batch only; not a random sample or archive-wide error rate. Legal baseline: Article 13(8) support period (including expected-use-under-five-years exception); Article 13(9) post-issuance update retention; Annex I Part II(8) free updates with tailor-made business-user agreement exception; Article 14 actively exploited vulnerability/severe incident reporting; Annex I Part II(5)–(7) CVD/contact/secure distribution; Annex II(2) contact point and 8(d) secure decommissioning information. Do not infer a universal Secure Boot, TPM, signature algorithm, dual-bank, rollback, zero-downtime, forced-password-change or port-disable requirement.


## 25. main 보고서 #122 감사 (2026-11-12)

Detailed report: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md).

| Claim ID | Report | Atomic finding | Status |
|---|---:|---|---|
| CRA-ARCH-122-001 | #122 | Secure-by-default/access-control/attack-surface themes map to Annex I Part I(2)(b),(d),(j), but Annex numbering and quote are composite/wrong; universal forced password change, unique credentials, port disabling and RBAC mandates are unsupported. | CONFLICT |


## 26. main 보고서 #123 감사 (2026-11-12)

Detailed report: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md).

| Claim ID | Report | Atomic finding | Status |
|---|---:|---|---|
| CRA-ARCH-123-001 | #123 | User-instructions obligation misattributed to Article 13(7) instead of 13(18); Annex II falsely described as Part I/II and quote is synthetic; support period is oversimplified; Class II servo-drive claim unsupported. | CONFLICT |

Correct mapping: Article 13(18) accompanying information/instructions and retention; Article 13(19) support-end-date display/notification; Article 13(17) single contact; Annex II(1)–(9), especially (7), (8)(a)–(f), (9). Article 13(7) is systematic documentation of cybersecurity aspects, not the user-manual provision.


## 27. main 보고서 #124 감사 (2026-11-12)

Detailed report: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md).

| Claim ID | Report | Atomic finding | Status |
|---|---:|---|---|
| CRA-ARCH-124-001 | #124 | Vulnerability handling is Annex I Part II(1)–(8), not Part I Section 2; raw quote is synthetic/wrongly numbered; cryptographic signature and fail-safe recovery are design candidates, not universal named mandates. | CONFLICT |

Correct map: Annex I Part I(2)(c) for applicable automatic-update default/user controls; Part II(5) CVD policy; Part II(6) vulnerability information/contact; Part II(7) secure update distribution; Part II(8) timely/free security updates subject to tailor-made business-user exception; Article 13(17)/Annex II(2) user-facing single point of contact.


## 28. main 아카이브 보고서 #48–#52 주장별 정정 레코드 — 2026-11-13

| 주장 ID | 원본 보고서 | 원자적 검증 결과 | 판정 |
|---|---:|---|---|
| CRA-ARCH-MAIN-20261113-048-001 | #48 | 기계 판독 가능 사용자 통지는 Article 14(8)에 규정되어 있으며, 적극 악용 취약점 또는 제품 보안에 영향을 미치는 심각한 사고에 대한 사용자 통지에서 적절한 경우 적용된다. Annex I Part II(2)는 모든 보안 공지에 대한 자동·기계 판독 형식을 일반적으로 요구하지 않는다. CSAF도 의무 형식으로 지정하지 않는다. | PARTIALLY_VERIFIED |
| CRA-ARCH-MAIN-20261113-049-001 | #49 | 무상 보안 업데이트는 Annex I Part II(8)에 근거하며 Part I(2)가 아니다. 신고 조항은 Article 11이 아니라 Article 14다. 지원기간과 업데이트 보존기간은 Article 13(8)/(9)로 구분한다. | CONFLICT |
| CRA-ARCH-MAIN-20261113-050-001 | #50 | 산업용·고위험 용도라는 이유만으로 서보 드라이브를 Annex III Class I로 자동 분류할 수 없다. 제품 전체의 핵심 기능과 시행규정의 기술 설명을 대조해야 한다. | CONFLICT |
| CRA-ARCH-MAIN-20261113-051-001 | #51 | 조정된 취약점 공개 정책(CVD)과 취약점 신고 연락처의 근거는 Annex I Part II(5)/(6)이다. Annex I Part I 또는 Article 10이라는 조항 위치와 PGP의 보편적 의무 주장은 근거가 없다. | PARTIALLY_VERIFIED |
| CRA-ARCH-MAIN-20261113-052-001 | #52 | 통합 구성요소의 취약점을 제조사가 식별한 경우 Article 13(6)의 명시적 신고 방향은 해당 구성요소 제조사/유지관리 주체를 향한다. 모든 공급자가 통합 제조사나 최종 사용자에게 자동 통지해야 한다는 포괄 의무는 인용 조항에서 확인되지 않는다. | CONFLICT |

원본 경로·아카이브 blob SHA·공식 조항 매핑·인용문 판정·반증은 [#48–#52 상세 감사 보고서](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md)를 참조한다.


## 29. 2026-11-13 — #48–#52 주장 정정의 한국어 기록 확인

- #48–#52 다섯 개 주장 레코드를 한국어로 전환했다. 기존 Claim ID, 판정, 조항 위치, 원본 SHA 추적은 보존했다.
- 법령 기준선과 제품 분류·접근통제 매트릭스를 한국어 설명 정본으로 갱신했다.


## 30. 2026-11-13 main 연속 감사 배치 색인 및 원자 주장 연결 상태

> 이 절은 배치 단위 탐색 색인이다. 개별 claim record를 대체하지 않는다. 보고서 번호는 날짜가 바뀌면 반복될 수 있으므로 신규 claim ID에는 날짜/원본 범위를 포함한다.

| 감사 범위 | 상세 감사 문서 | 판정 | 직접 인용 재사용 | Ledger 원자 주장 연결 |
|---|---|---|---:|---|
| #8–#12 | 세부 파일 경로/문서 ID 재확인 필요 | 이전 누적 요약에서 5 CONFLICT로 계산되나 원본 감사 문서 링크 재확인 필요 | 누적 #8–#47 집계에 포함되어 0/5 | 개별 claim ID 미확인 |
| #13–#27 | [감사 #13–#27](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md) | 15 CONFLICT | 0/15 | 개별 원자 claim ID 미등록 |
| #28–#32 | [감사 #28–#32](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md) | 5 CONFLICT | 0/5 | 개별 원자 claim ID 미등록 |
| #33–#37 | [감사 #33–#37](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md) | 5 CONFLICT | 0/5 | #35–#37의 일부 ID가 과거 기록에 있으나 날짜/경로 기준 재매핑 필요 |
| #38–#42 | [감사 #38–#42](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_38_42_2026-11-13.md) | 4 CONFLICT / 1 PARTIALLY_VERIFIED | 0/5 | #40–#42 일부 ID가 과거 기록에 있으나 날짜/경로 기준 재매핑 필요 |
| #43–#47 | [감사 #43–#47](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_43_47_2026-11-13.md) | 3 CONFLICT / 2 PARTIALLY_VERIFIED | 0/5 | CRA-ARCH-043–047 레코드 존재 여부와 원본 날짜/경로를 재대조해야 함 |
| #48–#52 | [감사 #48–#52](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md) | 3 CONFLICT / 2 PARTIALLY_VERIFIED | 0/5 | CRA-ARCH-MAIN-20261113-048–052-001 다섯 레코드 등록 |

### 집계와 한계

- #13–#52: 40건 중 35 CONFLICT / 5 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/40.
- #8–#47: 40건 중 37 CONFLICT / 3 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/40. #8–#12의 5 CONFLICT는 이전 누적 집계에서 역산한 값이며, 원본 감사 문서·개별 판정 링크를 이번 대조에서 재확인하지 못했다.
- #8–#52: 45건 중 40 CONFLICT / 5 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/45.
- 이 결과는 날짜/번호로 연속 선택한 비무작위 표본이다. 전체 main 아카이브의 오류율로 일반화하지 않는다.
- Ledger에 개별 원자 주장 ID가 없는 #13–#34 및 일부 #35–#47은 상세 감사 문서가 존재하더라도 주장 단위 추적은 미완료다. 이 배치 색인을 추가한 것만으로 원자 claim coverage가 완료된 것으로 간주하지 않는다.
- 다음 P0: #8–#52의 날짜+원본 경로+blob SHA를 기준으로 감사 문서와 Ledger ID를 1:1 대조하고, 중복/누락/상태 차이를 폐쇄한다.


## 31. 2026-11-13 main reports #13–#52 날짜·원본·주장별 추적 대장

> 아래는 2026-11-13 날짜의 일일 보고서 번호 #13–#52에 대한 원본 파일 식별 및 파일 단위 중심 주장 추적이다. 번호가 같은 다른 날짜의 보고서와 혼동하지 않도록 날짜와 경로, Git blob SHA를 함께 기록했다. 각 행은 배치 감사의 중심 오류/정정 요약이며, 다중 주장 문서의 모든 문장을 원자 주장으로 분해한 완전한 claim coverage를 의미하지 않는다.

| 주장 ID | 일일 번호 | 원본 archive 경로 | 원본 blob SHA | 판정 | 핵심 정정 요약 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-013-001 | #13 | `research_archive/2026-11-13_010102.md` | `2e9fb641dcebcb411dca1e686de916bf09dbfcb9` | CONFLICT | CVD·일반 취약점/사고 통지를 혼합하고 Article 11 및 NIS2 연락처 문구를 잘못 인용; CVD·연락처·Article 14 신고를 분리. |
| CRA-ARCH-MAIN-20261113-014-001 | #14 | `research_archive/2026-11-13_010538.md` | `dda0e0308d5fffb11659f6c395a9b0a3da26b1de` | CONFLICT | 보안 기본값·접근통제·공격표면 조항 번호 오기; 최초 비밀번호 변경·모든 포트/디버그 비활성화를 보편 의무로 과장. |
| CRA-ARCH-MAIN-20261113-015-001 | #15 | `research_archive/2026-11-13_011036.md` | `f150569deac61b8d74a424bb1c76518438816de0` | CONFLICT | 무상 보안 업데이트와 CVD를 Annex I Part I/Article 11에 잘못 배치; Part II(8)/(5)/(6)/(7)로 분리. |
| CRA-ARCH-MAIN-20261113-016-001 | #16 | `research_archive/2026-11-13_011537.md` | `2f67047e45084598819a1d7b4ccd4a463c2dc168` | CONFLICT | 지원기간 5년 예외 오해 및 Article 11/Annex I Part I 인용 오류; Article 13(8), Part II(8)/(5)/(6) 분리. |
| CRA-ARCH-MAIN-20261113-017-001 | #17 | `research_archive/2026-11-13_012038.md` | `a2a8c24d6e0933f5d6e3e6fcdb570037ed652e7e` | CONFLICT | CVD·연락처·무상 업데이트를 혼합; A/B 파티션·원자 업데이트는 위험기반 설계 후보이지 해당 조항의 보편 의무가 아님. |
| CRA-ARCH-MAIN-20261113-018-001 | #18 | `research_archive/2026-11-13_012535.md` | `a39605cfc909d39990ecc46bdd8caa5e8f97efd4` | CONFLICT | Article 14 신고 트리거를 넓게 표현하고 Article 11로 오기; 적극 악용 취약점/심각한 사고 두 트랙 및 최종 기한 구분. |
| CRA-ARCH-MAIN-20261113-019-001 | #19 | `research_archive/2026-11-13_013047.md` | `8211d1c2905452bf87e41722ca408119092644d1` | CONFLICT | 지원기간 '5년 또는 예상수명 중 짧은 기간' 오기; Part II(1)을 CVD/무상 업데이트로 오인; Secure Boot는 위험기반 후보. |
| CRA-ARCH-MAIN-20261113-020-001 | #20 | `research_archive/2026-11-13_013528.md` | `d80151fca7d8302bd353715b3d8608412b99e065` | CONFLICT | Part I(2)(f) 무결성을 최초 비밀번호 변경 의무로 오인; secure-by-default와 무결성 조항 구분. |
| CRA-ARCH-MAIN-20261113-021-001 | #21 | `research_archive/2026-11-13_014042.md` | `34c0a04a117ff8175bec68e93e26600b520cebb5` | CONFLICT | Annex II 사용자 정보와 Annex VII 기술문서 혼동; 지원기간/무상 업데이트/secure defaults 조항 혼합. |
| CRA-ARCH-MAIN-20261113-022-001 | #22 | `research_archive/2026-11-13_014539.md` | `a6695390839a167aa9a4b99473b2a70ba61dc838` | CONFLICT | 서보 드라이브 Class I/II 자동 분류 및 강제 비밀번호/MFA/포트 비활성화 과장; 핵심 기능과 위험기반 통제 필요. |
| CRA-ARCH-MAIN-20261113-023-001 | #23 | `research_archive/2026-11-13_015044.md` | `d8315ca10d9d1d811978c73ab8ffbd77e296971d` | CONFLICT | 최초 접속 비밀번호 설정을 CRA 법적 전제조건으로 과장; Part I(2)(b)/(d)/(j)와 정확한 문언 구분. |
| CRA-ARCH-MAIN-20261113-024-001 | #24 | `research_archive/2026-11-13_015535.md` | `c43117db6c681bd4b6865b955ac66a0fa012a1fd` | CONFLICT | 진단·웹·레거시 서비스 전면 비활성화를 보편 의무로 과장; secure defaults와 업데이트 요구를 분리. |
| CRA-ARCH-MAIN-20261113-025-001 | #25 | `research_archive/2026-11-13_020056.md` | `a482f9198569dfe173d63250eebee6d8f9a6f9e8` | CONFLICT | 서보 드라이브 Important Class I/II 근거 없음; JTAG/UART 잠금·고유 자격증명·서비스 비활성화는 구현 후보. |
| CRA-ARCH-MAIN-20261113-026-001 | #26 | `research_archive/2026-11-13_020541.md` | `132dd081b4bed0d431d8f68b8e00b3fc83b9035d` | CONFLICT | 기본 암호·고유 자격증명·모든 인터페이스 비활성화를 직접 의무화; Part I(2)(b)/(d)/(f)/(j) 매핑 혼합. |
| CRA-ARCH-MAIN-20261113-027-001 | #27 | `research_archive/2026-11-13_021039.md` | `3b6537c40590118c43d1fbc5f1922121d7f6d276` | CONFLICT | CVD/무상 업데이트를 Annex I Section 1 및 Article 13(4)에 잘못 연결; Part II(5)/(8), Article 13(8)/(9)로 정정. |
| CRA-ARCH-MAIN-20261113-028-001 | #28 | `research_archive/2026-11-13_021538.md` | `78de23c029c47dee16ebc82adf7123c2bf52fa4a` | CONFLICT | 지원기간 5년 예외와 Part II(8) 무상 업데이트/CVD(5)/연락처(6) 혼합; ENISA 협력은 법적 의무와 운영 권고 구분. |
| CRA-ARCH-MAIN-20261113-029-001 | #29 | `research_archive/2026-11-13_022039.md` | `e5248b9d23e94ea0ef5ad7ffb30f2dcd100e3434` | CONFLICT | Article 10 오기; Article 13(8)/(9) 지원·업데이트 가용성과 Part II(8) 무상 제공을 분리하고 맞춤형 제품 예외 포함. |
| CRA-ARCH-MAIN-20261113-030-001 | #30 | `research_archive/2026-11-13_022538.md` | `15439fdad39d1759f522023fc3f1201c1fbf4e8f` | CONFLICT | 신고 조항 Article 11 오기; Article 14 두 신고 트랙과 각각의 최종 보고 기한을 구분; 런타임 상시 모니터링은 위험기반. |
| CRA-ARCH-MAIN-20261113-031-001 | #31 | `research_archive/2026-11-13_023045.md` | `bc85eca9a24980a199e00fc13752f158b11e059e` | CONFLICT | CVD는 Part II(5)/(6), Article 14는 Class I/II에만 한정되지 않음; 서보 드라이브 분류 자동 단정 금지. |
| CRA-ARCH-MAIN-20261113-032-001 | #32 | `research_archive/2026-11-13_023540.md` | `71146baf92e406e18209f9981d8a7afc47620be2` | CONFLICT | 취약점 처리는 Annex I Part II(1)–(8), 지원 Article 13(8), 업데이트 가용성 13(9), 무상 제공 Part II(8)로 분리. |
| CRA-ARCH-MAIN-20261113-033-001 | #33 | `research_archive/2026-11-13_024039.md` | `c9c8f17bae8dd90890f9075927aa5fb6668c32b0` | CONFLICT | CVD/VDP 의무의 조항 위치 및 직접 인용 오류; Part II(5)/(6)와 Article 14 신고 분리. |
| CRA-ARCH-MAIN-20261113-034-001 | #34 | `research_archive/2026-11-13_024544.md` | `97101ee32c543adc2b684c92eec4c831cbe2c479` | CONFLICT | CVD·공급망·Article 14 범위를 혼합; Article 13(5)–(7), Part II(5)/(6), Article 14 역할 분리. |
| CRA-ARCH-MAIN-20261113-035-001 | #35 | `research_archive/2026-11-13_025045.md` | `842b48aa5ba2382ce58cdddcb1f8b836c5336eb6` | CONFLICT | Secure-by-default 및 초기 설정을 보편적 비밀번호 변경 의무로 확대; Annex I Part I(2)(b) 및 위험기반 설계 구분. |
| CRA-ARCH-MAIN-20261113-036-001 | #36 | `research_archive/2026-11-13_025531.md` | `06f32803648a15f7638add752a8b9a064d4ee3f9` | CONFLICT | 무상 업데이트와 지원기간 조항 혼동; Article 13(8)/(9), Annex I Part II(8) 분리. |
| CRA-ARCH-MAIN-20261113-037-001 | #37 | `research_archive/2026-11-13_030054.md` | `a8f77a2ecc3bc2301ab87a5f90d2ae6626489eab` | CONFLICT | Important Product 분류 및 적합성 평가 경로의 근거 부족; Article 7/Annex III/시행규정 및 Article 32 기준. |
| CRA-ARCH-MAIN-20261113-038-001 | #38 | `research_archive/2026-11-13_030533.md` | `f66d4335654b3b8b9836dcaebe1205eae731c532` | CONFLICT | Annex II point 8(d)의 안전한 폐기·데이터 제거 사용자 지침을 실제 데이터 sanitization 기능 의무로 확대. |
| CRA-ARCH-MAIN-20261113-039-001 | #39 | `research_archive/2026-11-13_031039.md` | `9dfae4ba67f48e056f222bcc86ca3189f8bb384a` | CONFLICT | Article 11 오기 및 지원기간·업데이트 가용성·무상 업데이트 혼합; Article 13(8)/(9), Part II(8)로 정정. |
| CRA-ARCH-MAIN-20261113-040-001 | #40 | `research_archive/2026-11-13_031539.md` | `449b601a1df9bef3f3acd789ea2a7fcba0804ea2` | PARTIALLY_VERIFIED | 사용자 정보·지침 제공 주제는 타당하나 Annex II 위치와 일부 계정/포트/로그 요구를 보편 의무로 과장. |
| CRA-ARCH-MAIN-20261113-041-001 | #41 | `research_archive/2026-11-13_032039.md` | `e8d5ef7ead0cb481d158597110e98bdcd006b07c` | CONFLICT | Annex I Part II(2)–(8) 의무 혼합; 특정 서명·rollback/fail-safe 구조를 CRA의 보편 의무로 단정. |
| CRA-ARCH-MAIN-20261113-042-001 | #42 | `research_archive/2026-11-13_032532.md` | `0c9ca2e1c69b6bed759f1afa85dd2327d29cf319` | CONFLICT | CVD/수정 취약점 공개/연락처 및 Article 14 신고 트랙 혼합; Part II(4)–(6) 정확한 구분 필요. |
| CRA-ARCH-MAIN-20261113-043-001 | #43 | `research_archive/2026-11-13_033047.md` | `aaea865c90a6c082b172403248c07d5dda783102` | CONFLICT | IACS/PLC/서보 드라이브를 Annex III Class II로 잘못 인용; Article 24를 적합성 평가로 오인; Article 32가 정확한 근거. |
| CRA-ARCH-MAIN-20261113-044-001 | #44 | `research_archive/2026-11-13_033533.md` | `4641a3feeb5654f1abd3c59323825c7f7a5145cc` | PARTIALLY_VERIFIED | 접근통제 주제는 타당하나 정확한 근거는 Annex I Part I 2(d); RBAC/MFA/고유 자격증명은 보편 의무 아님. |
| CRA-ARCH-MAIN-20261113-045-001 | #45 | `research_archive/2026-11-13_034038.md` | `ffe8ac1e5e41b80859631ac4c4975b0f6fc71bf5` | PARTIALLY_VERIFIED | 취약점 처리·사용자 안내 주제는 타당하나 Article 11 및 Annex I Part II 인용 오류; Part II(1)–(8) 구분 필요. |
| CRA-ARCH-MAIN-20261113-046-001 | #46 | `research_archive/2026-11-13_034535.md` | `61c22b5a97fc0e053668da26956b21f7ea85fe5c` | CONFLICT | 무상 업데이트 Part II(8), 지원기간 Article 13(8), 업데이트 가용성 13(9), CVD Part II(5), 신고 Article 14를 분리. |
| CRA-ARCH-MAIN-20261113-047-001 | #47 | `research_archive/2026-11-13_035035.md` | `e5f3d9fb2fb4cda62a5fc04a50e64f3d05ca1218` | CONFLICT | 지원기간 최소 5년 원칙 및 예상 사용기간 예외, 업데이트 가용성, 맞춤형 제품 무상 제공 예외를 오해. |
| CRA-ARCH-MAIN-20261113-048-001 | #48 | `research_archive/2026-11-13_035531.md` | `539b1d73d7053c5b1e252c775c503b055e978dd9` | PARTIALLY_VERIFIED | 기계 판독 가능 사용자 통지는 Article 14(8)의 제한된 사건·적절한 경우 요건; Annex I Part II(2)의 일반 공지 의무 아님. |
| CRA-ARCH-MAIN-20261113-049-001 | #49 | `research_archive/2026-11-13_040051.md` | `3d661d5545974406fee419f60234f99d29427495` | CONFLICT | Article 11 오기, Article 13(8)/(9) 지원·보존기간 오해, 무상 업데이트 Part II(8)와 예외 누락. |
| CRA-ARCH-MAIN-20261113-050-001 | #50 | `research_archive/2026-11-13_040534.md` | `8bbfe9b22a009c90dba493d3086462bb605a1b50` | CONFLICT | 산업용 서보 드라이브를 자동 Class I로 분류; 제품 전체 핵심 기능과 시행규정 기술 설명을 확인해야 함. |
| CRA-ARCH-MAIN-20261113-051-001 | #51 | `research_archive/2026-11-13_041039.md` | `8625c7e82389aea9cd3e5a0694cd0b920c90e8cf` | PARTIALLY_VERIFIED | CVD/연락처 의무는 맞으나 Part II(5)/(6) 위치, PGP 의무 주장은 오류. |
| CRA-ARCH-MAIN-20261113-052-001 | #52 | `research_archive/2026-11-13_041532.md` | `3672c41635364ef99b494cd8944c4998bbfc01c8` | CONFLICT | Article 13(6) 신고 방향은 제조사→구성요소 제조/유지 주체; 공급자→상위 제조사/사용자 일반 통지 의무로 역전 불가. |

- #13–#52 배치 합계: 40건 중 CONFLICT 35 / PARTIALLY_VERIFIED 5 / VERIFIED 0. 직접 인용 재사용 승인 0/40.
- #8–#12는 기존 누적 통계에 포함되지만, 이번 원본/경로 재대조에서 상세 감사 파일과 개별 SHA를 아직 식별하지 못했다. 추정된 누계로 개별 레코드를 생성하지 않는다.
- 위 ID는 날짜가 포함된 신규 감사 레코드다. 과거 날짜의 `CRA-ARCH-043-001` 등 번호 기반 레코드와 동일하다고 간주하지 않는다.
- 이 표의 판정은 파일 단위 중심 주장이다. 완전한 원자 주장 분해는 #13–#52 감사 보고서의 세부 claim과 추가 대조해야 한다.
