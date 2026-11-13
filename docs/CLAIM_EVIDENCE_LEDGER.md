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

## 4. 기존 아카이브 정정 큐 연결 — historical records

이 절의 A/B 배치(#1–#34)는 2026-11-12 초기 수동 감사 기록으로 보존한다. 2026-11-13 main archive #8–#62의 최신 감사/원자 분해 현황은 아래 파일 레코드 및 Canonical Requirement Register를 기준으로 한다. 과거 A/B 레코드와 신규 CRA-ARCH-MAIN ID namespace를 혼합하지 않는다.

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
| CRA-ARCH-MAIN-20261113-053-FILE-001 | #53 | `research_archive/2026-11-13_042039.md` | `16f8497915fe4a9233cb18f27f215b4a5e0565d3` | PARTIALLY_VERIFIED | Annex I Part I 2(m)의 사용자 데이터·설정 영구 제거 기능과 Annex II 8(d) 지침은 타당하나 특정 sanitization 방식 및 사전 지원종료 통지 의무는 과장. |
| CRA-ARCH-MAIN-20261113-054-FILE-001 | #54 | `research_archive/2026-11-13_042528.md` | `f5acd2a0370dd02b42ad2409dd34cefd6823deea` | PARTIALLY_VERIFIED | Article 13(8) 지원기간 및 Annex VII/Annex II 사용자 정보는 타당하나 Part II(8) 무상 업데이트 예외와 정확한 조항 문언을 보완해야 함. |
| CRA-ARCH-MAIN-20261113-055-FILE-001 | #55 | `research_archive/2026-11-13_043042.md` | `cb622a6a4ef322b19479b96d6238cdb865b11799` | PARTIALLY_VERIFIED | 무상 업데이트 주제는 맞지만 Article 13(4)/Part I 2(1)(g) 오인용, 맞춤형 제품 예외 및 workaround 적용 범위 누락. |
| CRA-ARCH-MAIN-20261113-056-FILE-001 | #56 | `research_archive/2026-11-13_043528.md` | `aaf77db2c4f7d7d1cad9917383c6f9aa5040fc3b` | PARTIALLY_VERIFIED | CVD와 Article 14 신고 트랙은 타당하나 모든 취약점 신고로 확대하지 말고 두 신고 트랙·최종 기한을 분리해야 함. |
| CRA-ARCH-MAIN-20261113-057-FILE-001 | #57 | `research_archive/2026-11-13_044041.md` | `089f816a2d93f84f0c95aead1957f4dc78b7ccba` | CONFLICT | Article 14를 Class I/II 제품에만 한정하고 Article 11/NIS2 경로로 오인; Article 14/16은 모든 CRA 범위 제품에 적용. |

원본 경로·아카이브 blob SHA·공식 조항 매핑·인용문 판정·반증은 [#48–#52 상세 감사 보고서](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md)를 참조한다.


## 29. 2026-11-13 — #48–#52 주장 정정의 한국어 기록 확인

- #48–#52 다섯 개 주장 레코드를 한국어로 전환했다. 기존 Claim ID, 판정, 조항 위치, 원본 SHA 추적은 보존했다.
- 법령 기준선과 제품 분류·접근통제 매트릭스를 한국어 설명 정본으로 갱신했다.


## 30. 2026-11-13 main 연속 감사 배치 색인 및 원자 주장 연결 상태

> 이 절은 배치 단위 탐색 색인이다. 개별 claim record를 대체하지 않는다. 보고서 번호는 날짜가 바뀌면 반복될 수 있으므로 신규 claim ID에는 날짜/원본 범위를 포함한다.

| 감사 범위 | 상세 감사 문서 | 판정 | 직접 인용 재사용 | Ledger 원자 주장 연결 |
|---|---|---|---:|---|
| #8–#12 | [감사 #8–#12](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_8_12_2026-11-13.md) | 5 CONFLICT | 0/5 | 원자 Claim ID 32개 등록 |
| #13–#27 | [감사 #13–#27](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md) | 15 CONFLICT | 0/15 | 날짜 포함 파일 중심 주장 ID 5개 등록; 개별 세부 주장 분해는 후속 |
| #28–#32 | [감사 #28–#32](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md) | 5 CONFLICT | 0/5 | 원자 Claim ID 33개 등록 |
| #33–#37 | [감사 #33–#37](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md) | 5 CONFLICT | 0/5 | 날짜 포함 파일 중심 주장 ID 5개 등록; 과거 날짜의 별도 ID와 구분 |
| #38–#42 | [감사 #38–#42](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_38_42_2026-11-13.md) | 3 CONFLICT / 2 PARTIALLY_VERIFIED | 0/5 | #38 재검토로 PARTIALLY_VERIFIED 정정; 날짜 포함 파일 중심 주장 ID 5개 등록 |
| #43–#47 | [감사 #43–#47](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_43_47_2026-11-13.md) | 3 CONFLICT / 2 PARTIALLY_VERIFIED | 0/5 | 날짜 포함 파일 중심 주장 ID 5개 등록; 과거 날짜의 별도 ID와 구분 |
| #48–#52 | [감사 #48–#52](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md) | 3 CONFLICT / 2 PARTIALLY_VERIFIED | 0/5 | CRA-ARCH-MAIN-20261113-048–052-001 다섯 레코드 등록 |
| #53–#57 | [감사 #53–#57](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_53_57_2026-11-13.md) | 1 CONFLICT / 4 PARTIALLY_VERIFIED | 0/5 | CRA-ARCH-MAIN-20261113-053–057-001 다섯 레코드 등록 |

### 집계와 한계

- #13–#52: 40건 중 35 CONFLICT / 5 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/40.
- #8–#47: 40건 중 36 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/40. #8–#12의 5 CONFLICT는 원본 감사 문서와 각 archive blob SHA를 재확인했다.
- #8–#52: 45건 중 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/45. 각 보고서에 날짜 포함 파일 중심 주장 ID 1개씩 총 45개를 등록했다.
- #8–#57: 50건 중 40 CONFLICT / 10 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/50. #53–#57은 1 CONFLICT / 4 PARTIALLY_VERIFIED다.
- 이 결과는 날짜/번호로 연속 선택한 비무작위 표본이다. 전체 main 아카이브의 오류율로 일반화하지 않는다.
- 과거 파일 중심 레코드에 대한 설명이다. 최신 구조에서는 #8–#57 파일 단위 레코드 50개를 -FILE-001 suffix로 보존하고, 각 보고서의 세부 주장은 별도 원자 Claim ID로 분해한다.
- 다음 P0: #8–#62의 날짜+원본 경로+blob SHA를 기준으로 감사 문서와 Ledger ID를 1:1 대조하고, Volume 1/2·SOP·매트릭스·시험 대장과 중복/누락/상태 차이를 폐쇄한다.


## 31. 2026-11-13 main reports #13–#57 날짜·원본·주장별 추적 대장

> 아래는 2026-11-13 날짜의 일일 보고서 번호 #13–#57에 대한 원본 파일 식별 및 파일 단위 중심 주장 추적이다. 번호가 같은 다른 날짜의 보고서와 혼동하지 않도록 날짜와 경로, Git blob SHA를 함께 기록했다. 각 행은 배치 감사의 중심 오류/정정 요약이며, 다중 주장 문서의 모든 문장을 원자 주장으로 분해한 완전한 claim coverage를 의미하지 않는다.

| 주장 ID | 일일 번호 | 원본 archive 경로 | 원본 blob SHA | 판정 | 핵심 정정 요약 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-008-FILE-001 | #8 | `research_archive/2026-11-13_003535.md` | `8141a7ff3d71cd2899e10a85c735b15351c72161` | CONFLICT | 보안 기본값 조항 오기; 최초 비밀번호 강제 변경·모든 JTAG/포트 비활성화를 보편 의무로 과장. |
| CRA-ARCH-MAIN-20261113-009-FILE-001 | #9 | `research_archive/2026-11-13_004046.md` | `c06112da2cd050b4eb0813828beb948975fb82d4` | CONFLICT | 무상 업데이트·CVD·연락처·지원기간을 혼합; Article 11 오기 및 맞춤형 제품 예외 누락. |
| CRA-ARCH-MAIN-20261113-010-FILE-001 | #10 | `research_archive/2026-11-13_004542.md` | `e9d5f5606a95567a9535de119edbbfa34739d02b` | CONFLICT | 보안 기본값을 Class II/Annex I Part II로 오분류; 서보 드라이브 Class II 근거 없음. |
| CRA-ARCH-MAIN-20261113-011-FILE-001 | #11 | `research_archive/2026-11-13_005038.md` | `3dab8049841c07992184993c5b18fc1dcab94836` | CONFLICT | 모든 포트·JTAG 비활성화와 최초 고유 비밀번호를 보편 의무로 과장; Part I(1)/(2)(b)/(d)/(j) 구분 필요. |
| CRA-ARCH-MAIN-20261113-012-FILE-001 | #12 | `research_archive/2026-11-13_005535.md` | `acda92dbe87ffbc549a8d52d42961b4bf058b983` | CONFLICT | CVD Part II(5), 연락처 Part II(6), 시정 Part II(2), 무상 업데이트 Part II(8), Article 14 신고 혼합. |
| CRA-ARCH-MAIN-20261113-013-FILE-001 | #13 | `research_archive/2026-11-13_010102.md` | `2e9fb641dcebcb411dca1e686de916bf09dbfcb9` | CONFLICT | CVD·일반 취약점/사고 통지를 혼합하고 Article 11 및 NIS2 연락처 문구를 잘못 인용; CVD·연락처·Article 14 신고를 분리. |
| CRA-ARCH-MAIN-20261113-014-FILE-001 | #14 | `research_archive/2026-11-13_010538.md` | `dda0e0308d5fffb11659f6c395a9b0a3da26b1de` | CONFLICT | 보안 기본값·접근통제·공격표면 조항 번호 오기; 최초 비밀번호 변경·모든 포트/디버그 비활성화를 보편 의무로 과장. |
| CRA-ARCH-MAIN-20261113-015-FILE-001 | #15 | `research_archive/2026-11-13_011036.md` | `f150569deac61b8d74a424bb1c76518438816de0` | CONFLICT | 무상 보안 업데이트와 CVD를 Annex I Part I/Article 11에 잘못 배치; Part II(8)/(5)/(6)/(7)로 분리. |
| CRA-ARCH-MAIN-20261113-016-FILE-001 | #16 | `research_archive/2026-11-13_011537.md` | `2f67047e45084598819a1d7b4ccd4a463c2dc168` | CONFLICT | 지원기간 5년 예외 오해 및 Article 11/Annex I Part I 인용 오류; Article 13(8), Part II(8)/(5)/(6) 분리. |
| CRA-ARCH-MAIN-20261113-017-FILE-001 | #17 | `research_archive/2026-11-13_012038.md` | `a2a8c24d6e0933f5d6e3e6fcdb570037ed652e7e` | CONFLICT | CVD·연락처·무상 업데이트를 혼합; A/B 파티션·원자 업데이트는 위험기반 설계 후보이지 해당 조항의 보편 의무가 아님. |
| CRA-ARCH-MAIN-20261113-018-FILE-001 | #18 | `research_archive/2026-11-13_012535.md` | `a39605cfc909d39990ecc46bdd8caa5e8f97efd4` | CONFLICT | Article 14 신고 트리거를 넓게 표현하고 Article 11로 오기; 적극 악용 취약점/심각한 사고 두 트랙 및 최종 기한 구분. |
| CRA-ARCH-MAIN-20261113-019-FILE-001 | #19 | `research_archive/2026-11-13_013047.md` | `8211d1c2905452bf87e41722ca408119092644d1` | CONFLICT | 지원기간 '5년 또는 예상수명 중 짧은 기간' 오기; Part II(1)을 CVD/무상 업데이트로 오인; Secure Boot는 위험기반 후보. |
| CRA-ARCH-MAIN-20261113-020-FILE-001 | #20 | `research_archive/2026-11-13_013528.md` | `d80151fca7d8302bd353715b3d8608412b99e065` | CONFLICT | Part I(2)(f) 무결성을 최초 비밀번호 변경 의무로 오인; secure-by-default와 무결성 조항 구분. |
| CRA-ARCH-MAIN-20261113-021-FILE-001 | #21 | `research_archive/2026-11-13_014042.md` | `34c0a04a117ff8175bec68e93e26600b520cebb5` | CONFLICT | Annex II 사용자 정보와 Annex VII 기술문서 혼동; 지원기간/무상 업데이트/secure defaults 조항 혼합. |
| CRA-ARCH-MAIN-20261113-022-FILE-001 | #22 | `research_archive/2026-11-13_014539.md` | `a6695390839a167aa9a4b99473b2a70ba61dc838` | CONFLICT | 서보 드라이브 Class I/II 자동 분류 및 강제 비밀번호/MFA/포트 비활성화 과장; 핵심 기능과 위험기반 통제 필요. |
| CRA-ARCH-MAIN-20261113-023-FILE-001 | #23 | `research_archive/2026-11-13_015044.md` | `d8315ca10d9d1d811978c73ab8ffbd77e296971d` | CONFLICT | 최초 접속 비밀번호 설정을 CRA 법적 전제조건으로 과장; Part I(2)(b)/(d)/(j)와 정확한 문언 구분. |
| CRA-ARCH-MAIN-20261113-024-FILE-001 | #24 | `research_archive/2026-11-13_015535.md` | `c43117db6c681bd4b6865b955ac66a0fa012a1fd` | CONFLICT | 진단·웹·레거시 서비스 전면 비활성화를 보편 의무로 과장; secure defaults와 업데이트 요구를 분리. |
| CRA-ARCH-MAIN-20261113-025-FILE-001 | #25 | `research_archive/2026-11-13_020056.md` | `a482f9198569dfe173d63250eebee6d8f9a6f9e8` | CONFLICT | 서보 드라이브 Important Class I/II 근거 없음; JTAG/UART 잠금·고유 자격증명·서비스 비활성화는 구현 후보. |
| CRA-ARCH-MAIN-20261113-026-FILE-001 | #26 | `research_archive/2026-11-13_020541.md` | `132dd081b4bed0d431d8f68b8e00b3fc83b9035d` | CONFLICT | 기본 암호·고유 자격증명·모든 인터페이스 비활성화를 직접 의무화; Part I(2)(b)/(d)/(f)/(j) 매핑 혼합. |
| CRA-ARCH-MAIN-20261113-027-FILE-001 | #27 | `research_archive/2026-11-13_021039.md` | `3b6537c40590118c43d1fbc5f1922121d7f6d276` | CONFLICT | CVD/무상 업데이트를 Annex I Section 1 및 Article 13(4)에 잘못 연결; Part II(5)/(8), Article 13(8)/(9)로 정정. |
| CRA-ARCH-MAIN-20261113-028-FILE-001 | #28 | `research_archive/2026-11-13_021538.md` | `78de23c029c47dee16ebc82adf7123c2bf52fa4a` | CONFLICT | 지원기간 5년 예외와 Part II(8) 무상 업데이트/CVD(5)/연락처(6) 혼합; ENISA 협력은 법적 의무와 운영 권고 구분. |
| CRA-ARCH-MAIN-20261113-029-FILE-001 | #29 | `research_archive/2026-11-13_022039.md` | `e5248b9d23e94ea0ef5ad7ffb30f2dcd100e3434` | CONFLICT | Article 10 오기; Article 13(8)/(9) 지원·업데이트 가용성과 Part II(8) 무상 제공을 분리하고 맞춤형 제품 예외 포함. |
| CRA-ARCH-MAIN-20261113-030-FILE-001 | #30 | `research_archive/2026-11-13_022538.md` | `15439fdad39d1759f522023fc3f1201c1fbf4e8f` | CONFLICT | 신고 조항 Article 11 오기; Article 14 두 신고 트랙과 각각의 최종 보고 기한을 구분; 런타임 상시 모니터링은 위험기반. |
| CRA-ARCH-MAIN-20261113-031-FILE-001 | #31 | `research_archive/2026-11-13_023045.md` | `bc85eca9a24980a199e00fc13752f158b11e059e` | CONFLICT | CVD는 Part II(5)/(6), Article 14는 Class I/II에만 한정되지 않음; 서보 드라이브 분류 자동 단정 금지. |
| CRA-ARCH-MAIN-20261113-032-FILE-001 | #32 | `research_archive/2026-11-13_023540.md` | `71146baf92e406e18209f9981d8a7afc47620be2` | CONFLICT | 취약점 처리는 Annex I Part II(1)–(8), 지원 Article 13(8), 업데이트 가용성 13(9), 무상 제공 Part II(8)로 분리. |
| CRA-ARCH-MAIN-20261113-033-FILE-001 | #33 | `research_archive/2026-11-13_024039.md` | `c9c8f17bae8dd90890f9075927aa5fb6668c32b0` | CONFLICT | CVD/VDP 의무의 조항 위치 및 직접 인용 오류; Part II(5)/(6)와 Article 14 신고 분리. |
| CRA-ARCH-MAIN-20261113-034-FILE-001 | #34 | `research_archive/2026-11-13_024544.md` | `97101ee32c543adc2b684c92eec4c831cbe2c479` | CONFLICT | CVD·공급망·Article 14 범위를 혼합; Article 13(5)–(7), Part II(5)/(6), Article 14 역할 분리. |
| CRA-ARCH-MAIN-20261113-035-FILE-001 | #35 | `research_archive/2026-11-13_025045.md` | `842b48aa5ba2382ce58cdddcb1f8b836c5336eb6` | CONFLICT | Secure-by-default 및 초기 설정을 보편적 비밀번호 변경 의무로 확대; Annex I Part I(2)(b) 및 위험기반 설계 구분. |
| CRA-ARCH-MAIN-20261113-036-FILE-001 | #36 | `research_archive/2026-11-13_025531.md` | `06f32803648a15f7638add752a8b9a064d4ee3f9` | CONFLICT | 무상 업데이트와 지원기간 조항 혼동; Article 13(8)/(9), Annex I Part II(8) 분리. |
| CRA-ARCH-MAIN-20261113-037-FILE-001 | #37 | `research_archive/2026-11-13_030054.md` | `a8f77a2ecc3bc2301ab87a5f90d2ae6626489eab` | CONFLICT | Important Product 분류 및 적합성 평가 경로의 근거 부족; Article 7/Annex III/시행규정 및 Article 32 기준. |
| CRA-ARCH-MAIN-20261113-038-FILE-001 | #38 | `research_archive/2026-11-13_030533.md` | `f66d4335654b3b8b9836dcaebe1205eae731c532` | PARTIALLY_VERIFIED | Annex I Part I 2(m)의 데이터·설정 영구 제거 기능 결과 요구와 Annex II 8(d) 폐기 지침을 누락/혼합하고 특정 sanitization 구현을 과장. |
| CRA-ARCH-MAIN-20261113-039-FILE-001 | #39 | `research_archive/2026-11-13_031039.md` | `9dfae4ba67f48e056f222bcc86ca3189f8bb384a` | CONFLICT | Article 11 오기 및 지원기간·업데이트 가용성·무상 업데이트 혼합; Article 13(8)/(9), Part II(8)로 정정. |
| CRA-ARCH-MAIN-20261113-040-FILE-001 | #40 | `research_archive/2026-11-13_031539.md` | `449b601a1df9bef3f3acd789ea2a7fcba0804ea2` | PARTIALLY_VERIFIED | 사용자 정보·지침 제공 주제는 타당하나 Annex II 위치와 일부 계정/포트/로그 요구를 보편 의무로 과장. |
| CRA-ARCH-MAIN-20261113-041-FILE-001 | #41 | `research_archive/2026-11-13_032039.md` | `e8d5ef7ead0cb481d158597110e98bdcd006b07c` | CONFLICT | Annex I Part II(2)–(8) 의무 혼합; 특정 서명·rollback/fail-safe 구조를 CRA의 보편 의무로 단정. |
| CRA-ARCH-MAIN-20261113-042-FILE-001 | #42 | `research_archive/2026-11-13_032532.md` | `0c9ca2e1c69b6bed759f1afa85dd2327d29cf319` | CONFLICT | CVD/수정 취약점 공개/연락처 및 Article 14 신고 트랙 혼합; Part II(4)–(6) 정확한 구분 필요. |
| CRA-ARCH-MAIN-20261113-043-FILE-001 | #43 | `research_archive/2026-11-13_033047.md` | `aaea865c90a6c082b172403248c07d5dda783102` | CONFLICT | IACS/PLC/서보 드라이브를 Annex III Class II로 잘못 인용; Article 24를 적합성 평가로 오인; Article 32가 정확한 근거. |
| CRA-ARCH-MAIN-20261113-044-FILE-001 | #44 | `research_archive/2026-11-13_033533.md` | `4641a3feeb5654f1abd3c59323825c7f7a5145cc` | PARTIALLY_VERIFIED | 접근통제 주제는 타당하나 정확한 근거는 Annex I Part I 2(d); RBAC/MFA/고유 자격증명은 보편 의무 아님. |
| CRA-ARCH-MAIN-20261113-045-FILE-001 | #45 | `research_archive/2026-11-13_034038.md` | `ffe8ac1e5e41b80859631ac4c4975b0f6fc71bf5` | PARTIALLY_VERIFIED | 취약점 처리·사용자 안내 주제는 타당하나 Article 11 및 Annex I Part II 인용 오류; Part II(1)–(8) 구분 필요. |
| CRA-ARCH-MAIN-20261113-046-FILE-001 | #46 | `research_archive/2026-11-13_034535.md` | `61c22b5a97fc0e053668da26956b21f7ea85fe5c` | CONFLICT | 무상 업데이트 Part II(8), 지원기간 Article 13(8), 업데이트 가용성 13(9), CVD Part II(5), 신고 Article 14를 분리. |
| CRA-ARCH-MAIN-20261113-047-FILE-001 | #47 | `research_archive/2026-11-13_035035.md` | `e5f3d9fb2fb4cda62a5fc04a50e64f3d05ca1218` | CONFLICT | 지원기간 최소 5년 원칙 및 예상 사용기간 예외, 업데이트 가용성, 맞춤형 제품 무상 제공 예외를 오해. |
| CRA-ARCH-MAIN-20261113-048-FILE-001 | #48 | `research_archive/2026-11-13_035531.md` | `539b1d73d7053c5b1e252c775c503b055e978dd9` | PARTIALLY_VERIFIED | 기계 판독 가능 사용자 통지는 Article 14(8)의 제한된 사건·적절한 경우 요건; Annex I Part II(2)의 일반 공지 의무 아님. |
| CRA-ARCH-MAIN-20261113-049-FILE-001 | #49 | `research_archive/2026-11-13_040051.md` | `3d661d5545974406fee419f60234f99d29427495` | CONFLICT | Article 11 오기, Article 13(8)/(9) 지원·보존기간 오해, 무상 업데이트 Part II(8)와 예외 누락. |
| CRA-ARCH-MAIN-20261113-050-FILE-001 | #50 | `research_archive/2026-11-13_040534.md` | `8bbfe9b22a009c90dba493d3086462bb605a1b50` | CONFLICT | 산업용 서보 드라이브를 자동 Class I로 분류; 제품 전체 핵심 기능과 시행규정 기술 설명을 확인해야 함. |
| CRA-ARCH-MAIN-20261113-051-FILE-001 | #51 | `research_archive/2026-11-13_041039.md` | `8625c7e82389aea9cd3e5a0694cd0b920c90e8cf` | PARTIALLY_VERIFIED | CVD/연락처 의무는 맞으나 Part II(5)/(6) 위치, PGP 의무 주장은 오류. |
| CRA-ARCH-MAIN-20261113-052-FILE-001 | #52 | `research_archive/2026-11-13_041532.md` | `3672c41635364ef99b494cd8944c4998bbfc01c8` | CONFLICT | Article 13(6) 신고 방향은 제조사→구성요소 제조/유지 주체; 공급자→상위 제조사/사용자 일반 통지 의무로 역전 불가. |

- #13–#52 배치 합계: 40건 중 CONFLICT 35 / PARTIALLY_VERIFIED 5 / VERIFIED 0. 직접 인용 재사용 승인 0/40.
- #13–#57 배치 합계: 45건 중 CONFLICT 36 / PARTIALLY_VERIFIED 9 / VERIFIED 0. 직접 인용 재사용 승인 0/45.
- #8–#12의 원본 감사 파일과 개별 archive SHA를 재확인했고, 원자 Claim ID 32개를 아래 추적 표에 등록했다.
- 위 ID는 날짜가 포함된 신규 감사 레코드다. 과거 날짜의 `CRA-ARCH-043-001` 등 번호 기반 레코드와 동일하다고 간주하지 않는다.
- 이 표의 판정은 파일 단위 중심 주장이다. 완전한 원자 주장 분해는 #13–#57 감사 보고서의 세부 claim과 추가 대조해야 한다.


## #38 재검토에 따른 판정 정정 — 2026-11-13

- Annex I Part I point 2(m)를 누락했던 기존 #38 감사의 파일 판정을 CONFLICT에서 PARTIALLY_VERIFIED로 정정했다.
- Part I 2(m)는 해당되는 제품에서 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 요구하고, Annex II 8(d)는 안전한 폐기/사용자 데이터 제거 방법의 지침을 요구한다.
- #8–#47 누계는 40건 중 36 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED로 정정한다. #8–#52 누계는 45건 중 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED다. 직접 인용 재사용은 계속 0/45.

## 2026-11-13 main reports #58–#62 — 원자 주장 추적

공식 기준: EUR-Lex consolidated Regulation (EU) 2024/2847, 20.11.2024. 각 상태는 아래에 적힌 법령 주장만 평가하며 제품별 적용성은 별도다.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 정정·한계 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-058-001 | #58 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 법령상 정책 의무 확인. 제품별 프로세스 증거는 미확인. |
| CRA-ARCH-MAIN-20261113-058-002 | #58 | 취약점 신고 연락 주소 및 사용자 단일 연락 창구가 필요하다. | Part II(6), Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-CONTACT-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | contact address와 single point of contact, 사용자 지침을 분리. |
| CRA-ARCH-MAIN-20261113-058-003 | #58 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-058-004 | #58 | 산업용 서보 드라이브가 Class II/important product다. | Article 7, Annex III | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 전체 core functionality 및 Annex III 범주 확인 전 분류 불가. |
| CRA-ARCH-MAIN-20261113-059-001 | #59 | CVD 정책은 CRA 취약점 처리 의무에 포함된다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD 정책 의무 자체는 확인. |
| CRA-ARCH-MAIN-20261113-059-002 | #59 | 보안 업데이트는 원칙적으로 무상이며 지체 없이 배포한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored product/business user agreement exception 누락. |
| CRA-ARCH-MAIN-20261113-059-003 | #59 | 서보 드라이브가 Class I로 분류된다. | Article 7, Annex III | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | SKU/core functionality 근거 없음. |
| CRA-ARCH-MAIN-20261113-059-004 | #59 | Article 11(7) 및 Annex I Section 2 인용이 현행 직접 인용이다. | Article 11, Article 13, Annex I | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 11은 General product safety이며 제조사 의무는 Article 13. 제시 문장은 현행 원문과 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-060-001 | #60 | 적극 악용 취약점은 Article 14 의무 신고 대상이다. | Article 14(1)–(2) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 지정 CSIRT와 ENISA에 단일 신고 플랫폼으로 제출. |
| CRA-ARCH-MAIN-20261113-060-002 | #60 | 제품 보안에 영향을 미치는 severe incident도 별도 의무 신고 대상이다. | Article 14(3)–(5) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | actively exploited vulnerability 트랙과 구분. |
| CRA-ARCH-MAIN-20261113-060-003 | #60 | 24h/72h 기한은 모든 일반 취약점에 적용된다. | Article 14(1)–(4) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 두 신고 트랙의 정해진 trigger에만 적용. 최종 보고는 취약점 14일, severe incident 1개월. |
| CRA-ARCH-MAIN-20261113-060-004 | #60 | 보고서의 Article 14(1)/Annex I Part II(1) 인용은 정확한 직접 인용이다. | Article 14, Annex I Part II(1)–(2) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-COMPONENT-DUE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-SBOM-001; CRA-REQ-REMEDIATION-001 | CONFLICT | 직접 인용 불일치. Part II(1)은 SBOM/구성요소 식별, (2)는 취약점 처리·시정. |
| CRA-ARCH-MAIN-20261113-061-001 | #61 | 관련 내부 활동의 기록·모니터링으로 보안 관련 정보를 제공해야 한다. | Annex I Part I 2(l) | CRA-REQ-SECURITY-LOGGING-001 | VERIFIED | 데이터·서비스·기능의 접근/변경을 포함하며 사용자 opt-out 메커니즘 포함. |
| CRA-ARCH-MAIN-20261113-061-002 | #61 | CRA logging 요구의 위치가 Part I 2(1)(h)다. | Annex I Part I 2(h), 2(l) | CRA-REQ-AVAILABILITY-001; CRA-REQ-SECURITY-LOGGING-001 | CONFLICT | 정확한 logging 위치는 2(l); 2(h)는 availability/DoS resilience. |
| CRA-ARCH-MAIN-20261113-061-003 | #61 | tamper-proof retention, circular buffer, Syslog over TLS가 CRA의 직접 의무다. | Annex I Part I 2(l) | CRA-REQ-SECURITY-LOGGING-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | UNVERIFIED | 법령이 지정한 구현 방식이 아님. 제품 위험평가 기반 설계 후보. |
| CRA-ARCH-MAIN-20261113-061-004 | #61 | 보고서 Raw Text Quote가 2(l)의 정확한 직접 인용이다. | Annex I Part I 2(l) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURITY-LOGGING-001 | CONFLICT | 제시된 문장은 현행 원문과 불일치하는 합성 인용. |
| CRA-ARCH-MAIN-20261113-062-001 | #62 | Article 14는 actively exploited vulnerability와 severe incident를 신고 대상으로 한다. | Article 14(1)–(5) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-CVD-POLICY-001 | VERIFIED | 일반 취약점 처리/CVD와 의무 신고 트리거를 분리. |
| CRA-ARCH-MAIN-20261113-062-002 | #62 | 두 트랙 모두 24h/72h 단계가 있다. | Article 14(2), (4) | CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | 맞지만 최종 보고 기한은 취약점 14일, 사고 1개월로 다르다. |
| CRA-ARCH-MAIN-20261113-062-003 | #62 | 제조자는 Article 14 신고를 시장감시기관에 직접 제출한다. | Article 14(7), Article 16(3) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 제조자는 지정 CSIRT 엔드포인트/단일 플랫폼으로 신고하고, CSIRT가 필요한 정보를 시장감시기관에 제공한다. |
| CRA-ARCH-MAIN-20261113-062-004 | #62 | 모든 발견 취약점에 대해 Article 14(8) 사용자 통지가 필요하다. | Article 14(8) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | actively exploited vulnerability 또는 severe incident에 한정. 영향 사용자 및 적절한 경우 모든 사용자. |
| CRA-ARCH-MAIN-20261113-062-005 | #62 | Article 11(8) 및 보고서 인용이 제조사 신고/사용자 통지의 정확한 근거다. | Article 13, Article 14(8) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, 신고 Article 14. 제시 인용은 현행 조항과 불일치. |

- #58–#62 파일 단위 판정: 5 PARTIALLY_VERIFIED / 0 CONFLICT / 0 VERIFIED; 직접 인용 재사용 승인 0/5.
- 위 원자 Claim ID는 개별 법령 문장·주장을 추적하기 위한 보조 레코드다. 제품별 적용성은 전부 UNVERIFIED이며 실제 DUT 시험은 NOT_RUN.
- 누적 파일 단위 감사 #8–#62: 55건, 40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/55. 비무작위 연속 표본.

## 2026-11-13 — #8–#12 원자 주장·인용 분해 (32 claims)

- 원본 감사: [main-only #8–#12 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_8_12_2026-11-13.md).
- 법령 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024. 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02024R2847-20241120
- 원본 경로 및 SHA는 원본 감사 문서에 기록되어 있다. 아래 레코드는 파일 단위 판정이 아니라 개별 법령 주장/인용의 원자 판정이다.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-008-001 | #8 | 제품은 위험평가에 따라 secure-by-default configuration으로 시장에 제공되어야 한다. | Annex I Part I(1), (2)(b) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-RISK-BASELINE-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | VERIFIED | 법령상 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-008-002 | #8 | secure-by-default에는 제품을 original state로 reset할 가능성이 포함된다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | 원문에 명시. |
| CRA-ARCH-MAIN-20261113-008-003 | #8 | 모든 제품은 최초 접속 시 고유하고 강력한 비밀번호 변경을 강제해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 해당 세부 방식은 조항의 보편적 직접 의무가 아니다. 위험기반 설계 선택으로 분리. |
| CRA-ARCH-MAIN-20261113-008-004 | #8 | JTAG/디버그/미사용 포트·서비스를 모든 제품에서 기본 비활성화해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | 공격표면 제한이라는 결과 요구는 있으나 모든 인터페이스를 일률 비활성화하라는 문언은 없다. |
| CRA-ARCH-MAIN-20261113-008-005 | #8 | 제품 reset 기능은 원래의 secure-by-default 상태로 돌아가도록 설계해야 한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | PARTIALLY_VERIFIED | secure default와 original-state reset을 함께 읽는 해석은 타당하나 reset 구현의 세부 방식은 제품별 설계·시험으로 확인. |
| CRA-ARCH-MAIN-20261113-008-006 | #8 | Raw Text Quote의 (a)/(b) 및 default-password 변경 문구가 현행 Annex I의 정확한 직접 인용이다. | Annex I Part I(2)(b), (d) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 현행 (b)는 secure-by-default/reset, (d)는 appropriate access controls이며 default password modification 문구는 인용된 조항에 없다. |
| CRA-ARCH-MAIN-20261113-009-001 | #9 | 제조자는 support period 동안 취약점을 효과적으로 처리해야 한다. | Article 13(8), Annex I Part II(2) | CRA-REQ-REMEDIATION-001; CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 지원기간 및 지체 없는 취약점 처리 의무 확인. |
| CRA-ARCH-MAIN-20261113-009-002 | #9 | support period는 예상 사용기간 또는 최소 5년 중 더 긴 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 원칙은 최소 5년이나 예상 사용기간이 5년보다 짧으면 그 예상 사용기간에 대응한다. |
| CRA-ARCH-MAIN-20261113-009-003 | #9 | 사용 가능한 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-009-004 | #9 | 제조자는 CVD 정책을 갖추고 취약점 신고 연락처를 제공해야 한다. | Article 13(8), Annex I Part II(5), (6) | CRA-REQ-CVD-POLICY-001; CRA-REQ-CVD-CONTACT-001 | VERIFIED | CVD 정책과 연락 주소의 법적 근거 확인. |
| CRA-ARCH-MAIN-20261113-009-005 | #9 | 모든 발견 취약점과 업데이트를 동일한 방식으로 사용자에게 공지해야 한다. | Annex I Part I(2)(c), Part II(4), Annex II | CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-AUTO-UPDATE-001 | PARTIALLY_VERIFIED | 업데이트 가능 통지 및 수정 취약점 공개 요구는 있으나 모든 잠재 취약점의 즉시 공지로 확대하지 않는다. |
| CRA-ARCH-MAIN-20261113-009-006 | #9 | 제조사 취약점 처리 의무의 근거는 Article 11이다. | Article 13(8), Annex I Part II | CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무는 Article 13이며 Article 11은 General product safety다. |
| CRA-ARCH-MAIN-20261113-009-007 | #9 | 보고서의 Part I/Manufacturer Obligations 복합 인용이 현행 원문의 정확한 직접 인용이다. | Annex I Part I(2)(c), Part II(2), (8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-AUTO-UPDATE-001 | CONFLICT | 서로 다른 요구를 합성했고 현행 문언과 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-010-001 | #10 | secure-by-default는 Annex I Part I(2)(b)에 규정되어 있다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | Part I는 제품 속성 요구사항. |
| CRA-ARCH-MAIN-20261113-010-002 | #10 | Annex I Part II가 Class II 중요 제품 요구사항을 뜻한다. | Annex I Part I/II, Annex III | CRA-REQ-CLASSIFICATION-001 | CONFLICT | Part II는 vulnerability handling requirements이고 Class II는 Annex III의 별도 제품 분류다. |
| CRA-ARCH-MAIN-20261113-010-003 | #10 | 일반 산업용 서보 드라이브는 CRA Class II 제품이다. | Article 7, Annex III | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 전체 core functionality와 Annex III 범주 증거가 없어 분류할 수 없다. |
| CRA-ARCH-MAIN-20261113-010-004 | #10 | 모든 서보 드라이브는 최초 접속 시 고유·고엔트로피 비밀번호 설정을 강제해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 비밀번호 생성·변경 절차는 해당 문언의 직접 보편 의무가 아니다. |
| CRA-ARCH-MAIN-20261113-010-005 | #10 | 관리자 권한 분리/least privilege가 인용된 secure-by-default 조항의 명문 세부 요구다. | Annex I Part I(2)(d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 적절한 접근통제 결과 요구는 있으나 해당 구체 역할 설계를 직접 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-010-006 | #10 | PE-CONS 105/23의 초안/타협안 인용이 현행 최종 규정의 정확한 인용이다. | Regulation (EU) 2024/2847, Annex I | CRA-EVIDENCE-QUOTE-ACCURACY-001 | CONFLICT | 최종 현행 조항과 위치·문언을 대조해야 하며 초안 인용을 최종 법령 인용으로 재사용하지 않는다. |
| CRA-ARCH-MAIN-20261113-011-001 | #11 | 제품의 사이버보안 수준은 위험에 기반해 적절한 수준이어야 한다. | Annex I Part I(1) | CRA-REQ-RISK-BASELINE-001 | VERIFIED | 원문상 risk-based cybersecurity level 요구 확인. |
| CRA-REQ-NO-KNOWN-EXPLOIT-001 | Annex I Part I(2)(a) | 제품은 시장 출시 시 알려진 악용 가능 취약점이 없어야 한다. | SBOM/CVE triage, release gate, vulnerability acceptance record |
| CRA-REQ-CONFIDENTIALITY-001 | Annex I Part I(2)(e) | 저장·전송·처리 데이터의 기밀성을 보호한다. | data-flow map, crypto design, key management test |
| CRA-REQ-DATA-MINIMIZATION-001 | Annex I Part I(2)(g) | 의도된 목적에 필요한 적절·관련·최소 데이터만 처리한다. | data inventory, purpose mapping, minimization review |
| CRA-REQ-AVAILABILITY-001 | Annex I Part I(2)(h) | 필수·기본 기능 가용성과 DoS 공격에 대한 복원력/완화 조치를 보호한다. | DoS/flood test, timing trace, safe recovery |
| CRA-REQ-INTERCONNECTIVITY-001 | Annex I Part I(2)(i) | 제품 또는 연결된 기기가 다른 기기/네트워크가 제공하는 서비스 가용성에 미치는 부정적 영향을 최소화한다. | network load test, packet capture, integration report |
| CRA-REQ-EXPLOIT-MITIGATION-001 | Annex I Part I(2)(k) | 적절한 exploit mitigation 메커니즘/기술로 사고 영향을 줄인다. | threat model, memory protection, input validation, fuzzing |
| CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | Article 13(2)–(4), Article 31/Annex VII | intended purpose, foreseeable use/misuse 및 operating environment를 반영한 제품 사이버보안 위험평가와 기술문서화. | product boundary, risk assessment, technical file |
| CRA-ARCH-MAIN-20261113-011-002 | #11 | secure-by-default와 외부 인터페이스를 포함한 attack-surface 제한은 CRA 요구사항이다. | Annex I Part I(2)(b), (j) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | 결과 요구의 근거 확인. |
| CRA-ARCH-MAIN-20261113-011-003 | #11 | 모든 통신 포트·USB·서비스 Ethernet·테스트 계정은 모든 제품에서 기본 비활성화해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | 위험기반 공격표면 제한을 모든 인터페이스 일괄 차단 의무로 확대했다. |
| CRA-ARCH-MAIN-20261113-011-004 | #11 | 제품별 고유 기본 비밀번호 또는 최초 사용 강제 변경이 CRA의 명시적 보편 의무다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 인증 설계는 위험기반 구현 후보이며 인용 조항이 직접 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-011-005 | #11 | “a appropriate level...” 및 secure-default 인용문이 정확한 Raw Text Quote다. | Annex I Part I(1), (2)(b) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-RISK-BASELINE-001 | CONFLICT | 문법 오류·합성/요약 문구가 포함되어 현행 법령의 직접 인용으로 재사용 불가. |
| CRA-ARCH-MAIN-20261113-012-001 | #12 | 제조자는 CVD 정책을 수립하고 집행해야 한다. | Annex I Part II(5), Article 13(8) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 원문상 정책 수립·집행 의무 확인. |
| CRA-ARCH-MAIN-20261113-012-002 | #12 | 취약점 신고 연락 주소를 제공해야 한다. | Annex I Part II(6) | CRA-REQ-CVD-CONTACT-001 | VERIFIED | 연락 주소 제공 및 정보 공유 촉진 요구 확인. |
| CRA-ARCH-MAIN-20261113-012-003 | #12 | CVD 정책은 반드시 공식 웹사이트에 공개해야 한다. | Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-USER-INSTRUCTIONS-001 | PARTIALLY_VERIFIED | 정책을 찾을 수 있는 위치와 단일 연락 창구를 사용자 정보에 포함해야 하나, 특정 웹사이트 공개 방식으로 한정하지 않는다. |
| CRA-ARCH-MAIN-20261113-012-004 | #12 | 보안 패치는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품 관련 제조자-사업 사용자 합의 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-012-005 | #12 | 모든 잠재 취약점은 Article 14에 따라 ENISA/CSIRT에 의무 신고해야 한다. | Article 14(1)–(4) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | 의무 신고 트리거는 actively exploited vulnerability와 severe incident 두 트랙이다. 일반 취약점은 CVD/취약점 처리 절차와 분리. |
| CRA-ARCH-MAIN-20261113-012-006 | #12 | 제조사 사용자 정보/지침의 근거는 Article 11이다. | Article 13(18), Annex II | CRA-REQ-USER-INFO-RETENTION-001; CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, 사용자 정보·지침 Article 13(18)/Annex II. |
| CRA-ARCH-MAIN-20261113-012-007 | #12 | CVD 정책 문구 “made publicly available”가 Annex I Part II(5)의 정확한 직접 인용이다. | Annex I Part II(5), Annex II(2) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | Part II(5)는 “put in place and enforce a policy”이며 사용자 정보의 정책 위치 제공은 Annex II(2)로 구분. |
| CRA-ARCH-MAIN-20261113-012-008 | #12 | 취약점 시정 문구 “without undue delay”가 Part II(2)의 정확한 직접 인용이다. | Annex I Part II(2) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REMEDIATION-001 | CONFLICT | 현행 문언은 “without delay”; 인용문을 직접 인용으로 재사용하지 않는다. |

- #8–#12 파일 단위 판정은 기존 감사 결과대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 위 32개는 개별 claim 단위다. 일부 법령 원칙은 VERIFIED여도 원본 보고서 전체가 VERIFIED라는 뜻은 아니다.
- 제품별 적용성·Class I/II 분류는 전부 UNVERIFIED. 실제 DUT 시험은 NOT_RUN.

## 2026-11-13 — #13–#17 원자 주장·인용 분해 (29 claims)

- 원본 감사: [main-only #13–#27 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md).
- 원본 main 경로·blob SHA: #13 \`research_archive/2026-11-13_010102.md\` / \`2e9fb641dcebcb411dca1e686de916bf09dbfcb9\`; #14 \`010538.md\` / \`dda0e0308d5fffb11659f6c395a9b0a3da26b1de\`; #15 \`011036.md\` / \`f150569deac61b8d74a424bb1c76518438816de0\`; #16 \`011537.md\` / \`2f67047e45084598819a1d7b4ccd4a463c2dc168\`; #17 \`012038.md\` / \`a2a8c24d6e0933f5d6e3e6fcdb570037ed652e7e\`.
- 공식 기준: EUR-Lex consolidated Regulation (EU) 2024/2847, 20.11.2024. 개별 상태는 법령 주장만 평가하며 제품별 적용성은 별도다.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-013-001 | #13 | 제조자는 CVD 정책을 마련하고 집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-013-002 | #13 | 모든 발견 취약점과 모든 사이버 사고를 Article 14에 따라 신고해야 한다. | Article 14(1)–(4) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 의무 신고는 actively exploited vulnerability 및 제품 보안에 영향을 미치는 severe incident 두 트랙. |
| CRA-ARCH-MAIN-20261113-013-003 | #13 | 24h/72h 신고 기한은 일반 취약점 모두에 적용된다. | Article 14(2), (4) | CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 해당 기한은 Article 14의 두 신고 트리거에만 적용. 최종 보고는 취약점 14일, 사고 1개월. |
| CRA-ARCH-MAIN-20261113-013-004 | #13 | 제조사 신고 의무 조항은 Article 11이다. | Article 13, Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 일반 의무는 Article 13, 법정 신고는 Article 14. |
| CRA-ARCH-MAIN-20261113-013-005 | #13 | Article 14 신고는 Class I/II 중요 제품에만 적용된다. | Article 14, Article 69(3) | CRA-REQ-TRANSITION-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | Article 14는 CRA 범위 제품에 적용되며 Article 69(3)는 2027-12-11 전 출시 제품에도 신고 의무를 적용한다. |
| CRA-ARCH-MAIN-20261113-013-006 | #13 | 인용한 NIS2 single point of contact 문구가 CRA의 정확한 직접 인용이다. | Article 13(17), Annex II(2) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-USER-CONTACT-001; CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | CRA의 사용자 단일 연락 창구는 Article 13(17)/Annex II(2)이며 제시 문구는 다른 법령·구조를 혼합. |
| CRA-ARCH-MAIN-20261113-014-001 | #14 | 제품의 사이버보안 수준은 위험에 기반한 적절한 수준이어야 한다. | Annex I Part I(1) | CRA-REQ-RISK-BASELINE-001 | VERIFIED | 위험기반 전체 보안 수준 요구 확인. |
| CRA-ARCH-MAIN-20261113-014-002 | #14 | 제품은 secure-by-default configuration으로 제공되어야 하며 original-state reset 가능성을 포함한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | 최종 법령 문언과 일치. |
| CRA-ARCH-MAIN-20261113-014-003 | #14 | 외부 인터페이스를 포함해 attack surface를 제한해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | VERIFIED | 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-014-004 | #14 | 모든 원격 포트·디버그 인터페이스를 모든 제품에서 비활성화해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | 모든 포트의 일괄 비활성화를 요구하는 직접 문언은 없다. |
| CRA-ARCH-MAIN-20261113-014-005 | #14 | 최초 전원 인가 시 강력한 고유 인증정보 설정을 반드시 강제해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 first-boot password flow는 위험기반 설계 후보이지 보편적 직접 명령이 아니다. |
| CRA-ARCH-MAIN-20261113-014-006 | #14 | 인용한 Annex I (a)/(b) 구조가 현행 secure-default/access-control 문언과 일치한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 현행 (b)는 secure default/reset, (d)는 appropriate access controls. 보고서의 번호/문구가 다르다. |
| CRA-ARCH-MAIN-20261113-015-001 | #15 | 사용 가능한 보안 업데이트는 원칙적으로 무상 제공되어야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관한 제조자-사업 사용자 합의 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-015-002 | #15 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 법령상 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-015-003 | #15 | CVD 정책은 반드시 공식 웹사이트에 게시해야 한다. | Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-USER-INSTRUCTIONS-001 | PARTIALLY_VERIFIED | 사용자가 정책을 찾을 수 있는 위치와 단일 연락 창구를 사용자 정보에 포함해야 하나 특정 웹사이트 방식으로 한정하지 않는다. |
| CRA-ARCH-MAIN-20261113-015-004 | #15 | 무상 업데이트/CVD 의무의 근거는 Annex I Part I 및 Article 11이다. | Annex I Part II(5), (8), Article 13 | CRA-REQ-CVD-POLICY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | CVD는 Part II(5), 무상 업데이트는 Part II(8), 제조사 의무는 Article 13. |
| CRA-ARCH-MAIN-20261113-015-005 | #15 | 보고서 Raw Text Quote가 Part I/Article 11의 정확한 직접 인용이다. | Annex I Part II(5), (8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제시 문장은 서로 다른 요구를 합성한 것으로 현행 원문과 불일치. |
| CRA-ARCH-MAIN-20261113-016-001 | #16 | 지원기간은 예상 사용기간을 반영하고 원칙적으로 최소 5년이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | 예상 사용기간이 5년 미만이면 지원기간은 예상 사용기간에 대응하는 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-016-002 | #16 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품/사업 사용자 합의 예외 누락. |
| CRA-ARCH-MAIN-20261113-016-003 | #16 | 제조자는 사용자 취약점 신고를 위한 단일 연락 창구를 지정해야 한다. | Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 쉽게 식별 가능하고 사용자 정보에 포함되어야 하며 자동화 도구만으로 제한 불가. |
| CRA-ARCH-MAIN-20261113-016-004 | #16 | 취약점 처리/무상 업데이트 의무의 법적 근거는 Article 11이다. | Article 13(8), Annex I Part II | CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 11 오기. 제조사 의무는 Article 13. |
| CRA-ARCH-MAIN-20261113-016-005 | #16 | CVD/무상 업데이트는 Annex I Part I의 취약점 처리 조항이다. | Annex I Part II(5), (8) | CRA-REQ-CVD-POLICY-001; CRA-REQ-FREE-UPDATE-001 | CONFLICT | Part I는 제품 속성, Part II는 취약점 처리. |
| CRA-ARCH-MAIN-20261113-016-006 | #16 | 보고서의 Article 11/Annex I Raw Text Quote가 현행 직접 인용이다. | Article 13, Annex I Part II | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 조항 번호와 문언 모두 현행 원문과 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-017-001 | #17 | 제조자는 취약점 신고 연락 주소와 신고 접수 메커니즘을 제공해야 한다. | Annex I Part II(6), Article 13(17) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-CONTACT-001 | VERIFIED | contact address와 사용자 단일 연락 창구를 구분해 기록. |
| CRA-ARCH-MAIN-20261113-017-002 | #17 | 사용 가능한 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관한 제조자-사업 사용자 합의 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-017-003 | #17 | 지원기간은 예상 사용기간 및 최소 5년 원칙을 반영한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | 예상 사용기간이 5년 미만이면 그 예상 사용기간에 대응하는 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-017-004 | #17 | CVD/무상 업데이트의 근거는 Article 11 및 Annex I Part I다. | Article 13(8), Annex I Part II(5), (8) | CRA-REQ-CVD-POLICY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, CVD/무상 업데이트 Part II(5)/(8). |
| CRA-ARCH-MAIN-20261113-017-005 | #17 | A/B 파티션 및 atomic firmware update가 CRA가 지정한 필수 구현 방식이다. | Annex I Part II(7), risk assessment | CRA-REQ-SECURE-UPDATE-DIST-001 | UNVERIFIED | 안전한 업데이트 배포 결과 요구와 특정 구현 방식은 분리. A/B/atomic update는 제품별 설계 후보. |
| CRA-ARCH-MAIN-20261113-017-006 | #17 | 보고서의 composite Raw Text Quote가 현행 법령의 정확한 직접 인용이다. | Annex I Part II(2), (5)–(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REMEDIATION-001 | CONFLICT | 여러 하위 항목을 합성한 문장으로 직접 인용 재사용 불가. |

- #13–#17 파일 단위 판정은 기존 감사 결과대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 위 29개는 개별 claim 단위다. 일부 개별 법령 사실이 VERIFIED여도 원본 보고서 전체 판정을 바꾸지 않는다.
- 제품별 적용성·Class I/II 분류는 UNVERIFIED, 실제 DUT 시험은 NOT_RUN.

## 2026-11-13 — #18–#22 원자 주장·인용 분해 (29 claims)

- 원본 감사: [main-only #13–#27 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md).
- 원본 main 경로·blob SHA: #18 \`research_archive/2026-11-13_012535.md\` / \`a39605cfc909d39990ecc46bdd8caa5e8f97efd4\`; #19 \`013047.md\` / \`8211d1c2905452bf87e41722ca408119092644d1\`; #20 \`013528.md\` / \`d80151fca7d8302bd353715b3d8608412b99e065\`; #21 \`014042.md\` / \`34c0a04a117ff8175bec68e93e26600b520cebb5\`; #22 \`014539.md\` / \`a6695390839a167aa9a4b99473b2a70ba61dc838\`.
- 공식 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-018-001 | #18 | actively exploited vulnerability는 Article 14 의무 신고 대상이다. | Article 14(1)–(2) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 지정 CSIRT와 ENISA에 단일 신고 플랫폼으로 통지. |
| CRA-ARCH-MAIN-20261113-018-002 | #18 | actively exploited vulnerability 신고는 24h early warning 및 72h vulnerability notification 단계를 갖는다. | Article 14(2)(a), (b) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 최종 보고는 corrective/mitigating measure 이용 가능 후 14일 이내라는 별도 기한을 추가해야 한다. |
| CRA-ARCH-MAIN-20261113-018-003 | #18 | 제조사 신고 의무 조항은 Article 11이다. | Article 13, Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, 법정 신고 Article 14. |
| CRA-ARCH-MAIN-20261113-018-004 | #18 | 모든 취약점 및 모든 보안 사고가 Article 14 신고 대상이다. | Article 14(1)–(5) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | actively exploited vulnerability와 제품 보안에 영향을 미치는 severe incident로 한정. |
| CRA-ARCH-MAIN-20261113-018-005 | #18 | NIS2 Article 17 single point of contact 문구가 CRA Article 14의 직접 인용이다. | Article 14(1), (7); Article 13(17) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-USER-CONTACT-001; CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | CRA는 지정 CSIRT/ENISA 단일 신고 플랫폼과 제조사 단일 연락 창구를 별도 규정한다. |
| CRA-ARCH-MAIN-20261113-019-001 | #19 | 보안 업데이트는 원칙적으로 무상 제공되어야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-019-002 | #19 | support period는 예상 수명과 5년 중 짧은 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 원칙은 최소 5년이며 예상 사용기간이 5년 미만이면 그 예상 사용기간에 대응한다. |
| CRA-ARCH-MAIN-20261113-019-003 | #19 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 법령상 CVD 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-019-004 | #19 | 취약점 신고 연락처와 정책을 사용자에게 알리는 절차가 필요하다. | Annex I Part II(6), Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-CONTACT-001; CRA-REQ-USER-INSTRUCTIONS-001 | PARTIALLY_VERIFIED | 연락 주소·단일 연락 창구·정책 위치를 구분. 특정 웹사이트 방식으로 한정하지 않는다. |
| CRA-ARCH-MAIN-20261113-019-005 | #19 | 모든 보안 업데이트는 반드시 암호학적 서명 및 Secure Boot로 검증되어야 한다. | Annex I Part II(7), risk assessment | CRA-REQ-SECURE-UPDATE-DIST-001 | CONFLICT | 안전한 업데이트 배포 결과 요구와 특정 서명/Secure Boot 방식은 구분. 구체 기술은 위험기반 설계 후보. |
| CRA-ARCH-MAIN-20261113-019-006 | #19 | Article 11 및 Annex I Part II(1) 인용이 free update/CVD 의무의 정확한 근거다. | Article 13, Annex I Part II(5), (8) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-SBOM-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 11 오기, Part II(1)은 SBOM/구성요소 식별. CVD (5), 무상 업데이트 (8). |
| CRA-ARCH-MAIN-20261113-020-001 | #20 | 제품은 secure-by-default configuration으로 제공되어야 한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | secure-by-default와 original-state reset 가능성. |
| CRA-ARCH-MAIN-20261113-020-002 | #20 | Annex I Part I(2)(f)가 secure-by-default 또는 초기 비밀번호 변경 요구다. | Annex I Part I(2)(b), (f) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001; CRA-REQ-INTEGRITY-001; CRA-REQ-SECURITY-LOGGING-001 | CONFLICT | (b)는 secure-by-default, (f)는 데이터·명령·프로그램·설정 무결성 보호. |
| CRA-ARCH-MAIN-20261113-020-003 | #20 | 최초 접속 시 공장 비밀번호 강제 변경이 CRA의 보편적 직접 의무다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 first-use password flow는 위험기반 설계 후보. |
| CRA-ARCH-MAIN-20261113-020-004 | #20 | Raw Text Quote의 (b)/(f)/(g)가 secure default/access control에 관한 현행 조항의 정확한 인용이다. | Annex I Part I(2)(b), (d), (f), (g) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 번호와 문언이 혼합·오배정됨. |
| CRA-ARCH-MAIN-20261113-020-005 | #20 | secure-by-default에는 제품을 original state로 reset할 가능성이 포함된다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | 현행 최종 법령 문언과 일치. |
| CRA-ARCH-MAIN-20261113-021-001 | #21 | 제품은 secure-by-default 및 적절한 접근통제 상태로 제공되어야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | VERIFIED | secure default와 appropriate access controls를 분리 추적. |
| CRA-ARCH-MAIN-20261113-021-002 | #21 | 모든 제품은 고유한 초기 인증정보 또는 사용자 강제 변경을 반드시 구현해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 법령은 결과 기반 보안 기본값/접근통제를 요구하며 특정 초기 비밀번호 방식은 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-021-003 | #21 | Annex II가 CRA technical documentation의 근거다. | Article 31, Annex VII; Article 13(18), Annex II | CRA-REQ-TECHDOC-001; CRA-REQ-USER-INFO-RETENTION-001; CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | Annex II는 사용자 정보·지침, 기술문서는 Article 31/Annex VII. |
| CRA-ARCH-MAIN-20261113-021-004 | #21 | support period는 예상 수명 또는 최소 5년이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | 예상 사용기간이 5년 미만이면 그 예상 사용기간에 대응하는 예외를 함께 기록. |
| CRA-ARCH-MAIN-20261113-021-005 | #21 | 제조자는 지원기간 중 보안 업데이트를 원칙적으로 무상 제공해야 한다. | Annex I Part II(8), Article 13(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | tailored product/business-user agreement exception 누락. |
| CRA-ARCH-MAIN-20261113-021-006 | #21 | Article 13(3)이 free security update와 advisory messages를 직접 규정한다. | Article 13(8), Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | CONFLICT | 해당 인용은 현재 조항의 문언·위치와 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-021-007 | #21 | Annex II가 technical documentation 및 support 기간을 모두 규정한다. | Annex II, Annex VII, Article 13(8) | CRA-REQ-TECHDOC-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | Annex II user instructions, Annex VII technical documentation, Article 13(8) support period로 분리. |
| CRA-ARCH-MAIN-20261113-022-001 | #22 | 제품은 위험에 기반한 secure-by-default configuration으로 제공되어야 한다. | Annex I Part I(1), (2)(b) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-RISK-BASELINE-001 | VERIFIED | 위험기반 보안 수준 및 secure default 확인. |
| CRA-ARCH-MAIN-20261113-022-002 | #22 | 일반 산업용 서보 드라이브가 Annex III Class I/II 제품이다. | Article 7, Annex III | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 전체 core functionality 및 Annex III 범주 증거가 없어 분류 불가. |
| CRA-ARCH-MAIN-20261113-022-003 | #22 | 모든 hardcoded/default credential은 법령상 무조건 금지된다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 취약한 기본 설정 방지는 요구되지만 구체 자격증명 구현·금지 문구를 보편 의무로 직접 단정하지 않는다. |
| CRA-ARCH-MAIN-20261113-022-004 | #22 | 첫 접속 시 비밀번호 또는 MFA 설정을 반드시 강제해야 한다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | MFA/first-use provisioning은 위험기반 접근통제 설계 후보. |
| CRA-ARCH-MAIN-20261113-022-005 | #22 | 미사용 포트/디버그 인터페이스는 모든 제품에서 기본 비활성화해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | attack-surface limitation 결과 요구를 모든 인터페이스 일괄 차단으로 확대하지 않는다. |
| CRA-ARCH-MAIN-20261113-022-006 | #22 | Raw Text Quote의 (a)/(b) secure-default/access-control 번호가 현행 법령과 일치한다. | Annex I Part I(2)(b), (d) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 현행 (b)=secure-by-default/reset, (d)=appropriate access controls. 보고서의 문구·번호는 불일치. |

- #18–#22 파일 단위 판정은 기존 감사 결과대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 CONFLICT를 구분한다. 제품별 적용성·Class I/II 분류는 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #23–#27 원자 주장·인용 분해 (30 claims)

- 원본 감사: [main-only #13–#27 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md).
- 원본 main 경로·blob SHA: #23 \`research_archive/2026-11-13_015044.md\` / \`d8315ca10d9d1d811978c73ab8ffbd77e296971d\`; #24 \`015535.md\` / \`c43117db6c681bd4b6865b955ac66a0fa012a1fd\`; #25 \`020056.md\` / \`a482f9198569dfe173d63250eebee6d8f9a6f9e8\`; #26 \`020541.md\` / \`132dd081b4bed0d431d8f68b8e00b3fc83b9035d\`; #27 \`021039.md\` / \`3b6537c40590118c43d1fbc5f1922121d7f6d276\`.
- 공식 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-023-001 | #23 | 제품은 secure-by-default configuration으로 제공되어야 한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | secure default 요구 확인. |
| CRA-ARCH-MAIN-20261113-023-002 | #23 | secure-by-default에는 original-state reset 가능성이 포함된다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | 현행 문언과 일치. |
| CRA-ARCH-MAIN-20261113-023-003 | #23 | 최초 전원 인가 시 강력한 고유 비밀번호 변경을 강제해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 first-use password flow는 CRA의 보편적 직접 의무가 아니다. |
| CRA-ARCH-MAIN-20261113-023-004 | #23 | 공장 초기화 상태에서 약한 기본 비밀번호·관리자 계정 공백이 없도록 해야 한다. | Annex I Part I(1), (2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001; CRA-REQ-RISK-BASELINE-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | PARTIALLY_VERIFIED | secure-by-default/appropriate access controls 결과와 연결되나 구체 계정 정책은 제품별 위험평가로 정당화. |
| CRA-ARCH-MAIN-20261113-023-005 | #23 | Raw Text Quote의 (a)/(b)/(c) 문구가 현행 Annex I의 정확한 인용이다. | Annex I Part I(2)(b), (d) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001 | CONFLICT | 현행 하위 항목 번호·문언과 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-024-001 | #24 | 제품은 secure-by-default configuration으로 제공되어야 한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | secure default 요구 확인. |
| CRA-ARCH-MAIN-20261113-024-002 | #24 | 모든 기본 계정·원격 포트·디버그 인터페이스를 모든 제품에서 비활성화해야 한다. | Annex I Part I(2)(j), (d) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | attack-surface/access-control 결과 요구를 일률적인 포트 차단으로 확대했다. |
| CRA-ARCH-MAIN-20261113-024-003 | #24 | 관리자 계정 비밀번호 강제 변경이 보편적 직접 의무다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 초기 비밀번호 정책은 위험기반 설계 선택. |
| CRA-ARCH-MAIN-20261113-024-004 | #24 | 모든 서비스·포트는 사용자가 명시적으로 켜기 전 외부 접근 불가 상태여야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | 위험기반 최소화 요구는 있으나 모든 제품에 대한 이 구체 운영 모델은 법령이 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-024-005 | #24 | 보고서의 secure-default/update 복합 Raw Text Quote가 현행 원문과 일치한다. | Annex I Part I(2)(b), (c) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001 | CONFLICT | 하위 항목·문언을 합성해 직접 인용으로 재사용할 수 없다. |
| CRA-ARCH-MAIN-20261113-025-001 | #25 | 제품은 위험기반 secure-by-default 상태로 제공되어야 한다. | Annex I Part I(1), (2)(b) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-RISK-BASELINE-001 | VERIFIED | 법령상 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-025-002 | #25 | 산업용 서보 드라이브는 Important Product Class I/II다. | Article 7, Annex III | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 전체 core functionality와 Annex III 범주 증거 없음. |
| CRA-ARCH-MAIN-20261113-025-003 | #25 | 모든 hardcoded/default credentials는 CRA가 명시적으로 일률 금지한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 안전한 기본 설정 결과는 요구하지만 특정 credential 구현·금지 방식은 직접 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-025-004 | #25 | JTAG/UART는 모든 제품에서 비활성화 또는 물리 봉인해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | attack-surface limitation을 특정 디버그 포트 조치로 일률화했다. |
| CRA-ARCH-MAIN-20261113-025-005 | #25 | 최초 접속 시 고유 비밀번호/MFA 설정을 강제해야 한다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 인증 설계는 제품 위험에 따른 선택이며 해당 조항이 MFA/first-use를 직접 명시하지 않는다. |
| CRA-ARCH-MAIN-20261113-025-006 | #25 | least-privilege administrator separation이 해당 CRA 조항의 명문 세부 의무다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 적절한 접근통제 결과와 구체 권한 모델을 구분한다. |
| CRA-ARCH-MAIN-20261113-025-007 | #25 | PE-CONS 103/23 초안 문구가 현행 최종 Regulation의 정확한 인용이다. | Regulation (EU) 2024/2847, Annex I | CRA-EVIDENCE-QUOTE-ACCURACY-001 | CONFLICT | 초안/타협안 인용을 최종 법령의 현행 문언으로 재사용하지 않는다. |
| CRA-ARCH-MAIN-20261113-026-001 | #26 | 제품은 secure-by-default configuration으로 제공되어야 한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | secure default 요구 확인. |
| CRA-ARCH-MAIN-20261113-026-002 | #26 | 외부 인터페이스를 포함한 attack surface를 제한해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | VERIFIED | 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-026-003 | #26 | 모든 제품에서 공통 마스터 비밀번호를 금지하고 고유 초기 인증정보를 강제해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 credential mechanism은 보편적 직접 문언이 아니다. |
| CRA-ARCH-MAIN-20261113-026-004 | #26 | 모든 fieldbus/USB/debug interface를 기본 비활성화해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | attack-surface 결과 요구를 모든 인터페이스의 일괄 차단으로 확대했다. |
| CRA-ARCH-MAIN-20261113-026-005 | #26 | 모든 backdoor/test diagnostic code를 CRA가 특정 방식으로 제거하도록 명시한다. | Annex I Part I(1), (2)(a), (j) | CRA-REQ-NO-KNOWN-EXPLOIT-001; CRA-REQ-ATTACK-SURFACE-001; CRA-REQ-RISK-BASELINE-001 | PARTIALLY_VERIFIED | 알려진 악용 취약점 부재·공격표면 제한 결과와 관련되나 특정 코드 제거 방식은 제품별 분석 필요. |
| CRA-ARCH-MAIN-20261113-026-006 | #26 | Raw Text Quote의 (a)/(b)/(f)가 현행 secure-default/access/integrity 요구의 정확한 매핑이다. | Annex I Part I(2)(b), (d), (f) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-INTEGRITY-001 | CONFLICT | 하위 항목과 문언을 혼합·오배정했다. |
| CRA-ARCH-MAIN-20261113-027-001 | #27 | 보안 업데이트는 지체 없이 배포되고 원칙적으로 무상 제공되어야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품의 제조자-사업 사용자 합의 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-027-002 | #27 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 법령상 CVD 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-027-003 | #27 | 취약점 신고 연락 주소와 사용자 단일 연락 창구를 제공해야 한다. | Annex I Part II(6), Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-CONTACT-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | contact address와 single point of contact, 사용자 정보 제공을 구분. |
| CRA-ARCH-MAIN-20261113-027-004 | #27 | CVD 정책은 공개 웹사이트에 게시되어야 한다. | Annex II(2), Article 13(17) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-USER-INSTRUCTIONS-001 | PARTIALLY_VERIFIED | 사용자가 정책을 찾을 수 있는 위치와 연락 창구를 사용자 정보에 포함하나 특정 웹사이트만을 요구하지 않는다. |
| CRA-ARCH-MAIN-20261113-027-005 | #27 | 취약점은 예상 수명 전체에 걸쳐 무상 패치해야 한다. | Article 13(8), Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | support period 산정과 무상 업데이트 의무는 별개이며 tailored-product agreement exception을 포함한다. |
| CRA-ARCH-MAIN-20261113-027-006 | #27 | 취약점 처리/무상 업데이트 근거가 Annex I Part I Section 1 Paragraph 2다. | Annex I Part II(2), (5), (6), (8) | CRA-REQ-REMEDIATION-001; CRA-REQ-FREE-UPDATE-001 | CONFLICT | Part II가 vulnerability handling requirements이며 Part I 제품 속성 요구와 구분. |
| CRA-ARCH-MAIN-20261113-027-007 | #27 | Article 13(4) 인용문이 취약점 처리 및 무상 업데이트의 정확한 직접 인용이다. | Article 13(8), Annex I Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | CONFLICT | 조항 번호와 제시 문언이 현행 원문과 일치하지 않는다. |

- #23–#27 파일 단위 판정은 기존 감사 결과대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 CONFLICT를 구분한다. 제품별 적용성·Class I/II 분류는 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #28–#32 원자 주장·인용 분해 (33 claims)

- 원본 감사: [main-only #28–#32 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md).
- 원본 main 경로·blob SHA: #28 \`research_archive/2026-11-13_021538.md\` / \`78de23c029c47dee16ebc82adf7123c2bf52fa4a\`; #29 \`022039.md\` / \`e5248b9d23e94ea0ef5ad7ffb30f2dcd100e3434\`; #30 \`022538.md\` / \`15439fdad39d1759f522023fc3f1201c1fbf4e8f\`; #31 \`023045.md\` / \`bc85eca9a24980a199e00fc13752f158b11e059e\`; #32 \`023540.md\` / \`71146baf92e406e18209f9981d8a7afc47620be2\`.
- 공식 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-028-001 | #28 | 보안 업데이트는 원칙적으로 무상 제공되어야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관한 제조자-사업 사용자 합의 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-028-002 | #28 | support period는 expected lifetime 또는 5년 중 짧은 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 원칙적으로 최소 5년, 예상 사용기간이 5년 미만이면 그 예상 사용기간에 대응한다. |
| CRA-ARCH-MAIN-20261113-028-003 | #28 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 법령상 CVD 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-028-004 | #28 | 제조자는 취약점 신고 연락 주소를 제공하고 정보 공유를 촉진해야 한다. | Annex I Part II(6) | CRA-REQ-CVD-CONTACT-001 | VERIFIED | 연락 주소 및 정보 공유 촉진 조치 확인. |
| CRA-ARCH-MAIN-20261113-028-005 | #28 | ENISA 협력은 모든 취약점의 즉시 신고를 의미한다. | Article 14(1)–(7) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | Article 14는 actively exploited vulnerability 및 severe incident 두 신고 트랙과 지정 CSIRT/단일 플랫폼 경로로 한정. |
| CRA-ARCH-MAIN-20261113-028-006 | #28 | “whichever is shorter”가 Article 13(8)의 정확한 지원기간 문언이다. | Article 13(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 현행 조항의 예외 구조와 반대되는 표현이며 직접 인용 재사용 불가. |
| CRA-ARCH-MAIN-20261113-028-007 | #28 | Part II CVD/free update 복합 Raw Text Quote가 정확한 직접 인용이다. | Annex I Part II(5), (8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-FREE-UPDATE-001 | CONFLICT | 여러 의무를 합성했고 원문 위치/문언과 불일치. |
| CRA-ARCH-MAIN-20261113-029-001 | #29 | 사용 가능한 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-029-002 | #29 | 업데이트 가용성을 사용자에게 알리고 advisory 정보를 제공해야 한다. | Annex I Part I(2)(c), Part II(8) | CRA-REQ-UPDATE-AVAILABILITY-001; CRA-REQ-AUTO-UPDATE-001 | VERIFIED | 자동 업데이트/알림 및 advisory 관련 문언 확인. |
| CRA-ARCH-MAIN-20261113-029-003 | #29 | support period는 최소 5년 또는 주요 상용화 기간으로 정한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | support period는 expected use를 반영하며 expected use가 5년 미만이면 그 기간에 대응한다. “주요 상용화 기간”은 별도 법령 용어가 아니다. |
| CRA-ARCH-MAIN-20261113-029-004 | #29 | 제조사 일반 의무의 근거는 Article 10이다. | Article 13 | CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 현행 CRA 제조사 의무는 Article 13. |
| CRA-ARCH-MAIN-20261113-029-005 | #29 | 유상 계약 여부와 무관하게 예외 없이 무상 업데이트를 제공해야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | CONFLICT | 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 경우 예외가 있다. |
| CRA-ARCH-MAIN-20261113-029-006 | #29 | 지원기간 종료일/지원 정보를 사용자에게 제공하고 기술문서에서 지원기간 산정 근거를 기록한다. | Annex II(7), Annex VII(4), Article 13(8) | CRA-REQ-TECHDOC-001; CRA-REQ-SUPPORT-END-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 안내와 기술문서의 서로 다른 요구로 구분. |
| CRA-ARCH-MAIN-20261113-029-007 | #29 | Article 10(6)/Annex I의 Raw Text Quote가 현행 직접 인용이다. | Article 13(8), Annex I Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 조항 번호·문언이 현행 원문과 불일치. |
| CRA-ARCH-MAIN-20261113-030-001 | #30 | actively exploited vulnerability와 severe incident는 Article 14 신고 트리거다. | Article 14(1)–(4) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 두 신고 트랙 확인. |
| CRA-ARCH-MAIN-20261113-030-002 | #30 | 모든 제품 취약점 및 모든 보안 사고를 ENISA에 의무 신고해야 한다. | Article 14(1)–(7) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 일반 취약점 처리와 법정 신고를 구분하고 두 Article 14 trigger만 적용. |
| CRA-ARCH-MAIN-20261113-030-003 | #30 | 24h/72h 초기 신고 단계가 Article 14에 있다. | Article 14(2), (4) | CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | 맞지만 취약점 final report 14일, severe incident final report 1개월을 추가해야 한다. |
| CRA-ARCH-MAIN-20261113-030-004 | #30 | 제조사 신고 의무는 Article 11이다. | Article 13, Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 13 제조사 의무, Article 14 신고. |
| CRA-ARCH-MAIN-20261113-030-005 | #30 | 모든 서보 드라이브에 실시간 런타임 탐지·모니터링·로깅 체계를 법령이 직접 요구한다. | Annex I Part I(1), (2)(l) | CRA-REQ-SECURITY-LOGGING-001; CRA-REQ-RISK-BASELINE-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | CONFLICT | 관련 내부 활동 기록·모니터링 결과 요구와 특정 실시간 탐지 아키텍처는 구분. 제품 위험평가 기반 설계 후보. |
| CRA-ARCH-MAIN-20261113-030-006 | #30 | NIS2 single point of contact를 Article 11/CRA 신고의 직접 수신자로 인용한 문장이 정확하다. | Article 14(1), (7), Article 13(17) | CRA-REQ-USER-CONTACT-001; CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | CRA 단일 신고 플랫폼/지정 CSIRT와 제조사 사용자 연락 창구를 혼합. |
| CRA-ARCH-MAIN-20261113-031-001 | #31 | 제조자는 CVD 정책을 마련해야 한다. | Annex I Part II(5), Article 13(8) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-031-002 | #31 | Article 14는 severe incident와 actively exploited vulnerability를 신고 대상으로 한다. | Article 14(1)–(4) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 두 신고 트랙 확인. |
| CRA-ARCH-MAIN-20261113-031-003 | #31 | Article 14 신고 의무는 Class I/II 중요 제품에만 적용된다. | Article 14, Article 69(3) | CRA-REQ-TRANSITION-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | CRA 범위 제품의 Article 14 적용이며 Class I/II 제한으로 읽지 않는다. |
| CRA-ARCH-MAIN-20261113-031-004 | #31 | CVD 정책의 직접 근거는 Annex I Part II(2)다. | Annex I Part II(2), (5), (6) | CRA-REQ-REMEDIATION-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | Part II(2)는 취약점 처리·시정, (5)는 CVD 정책, (6)은 신고 연락/정보 공유. |
| CRA-ARCH-MAIN-20261113-031-005 | #31 | 24h/72h는 두 신고 트랙의 초기 기한이다. | Article 14(2), (4) | CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | 최종 보고 기한 14일/1개월과 구분 필요. |
| CRA-ARCH-MAIN-20261113-031-006 | #31 | Article 14의 NIS2 SPO Raw Text Quote가 현행 CRA 직접 인용이다. | Article 14(1), (7) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 현행 CRA 신고 경로·문언과 불일치. |
| CRA-ARCH-MAIN-20261113-031-007 | #31 | Annex I Part II(2)의 익명 신고/contact address quote가 CVD 정책의 정확한 직접 인용이다. | Annex I Part II(5), (6) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REMEDIATION-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-CVD-CONTACT-001 | CONFLICT | CVD policy는 (5), contact address/information sharing은 (6). 합성 인용 불가. |
| CRA-ARCH-MAIN-20261113-032-001 | #32 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-032-002 | #32 | 제조사의 free update 의무 근거는 Article 11이다. | Article 13, Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무는 Article 13, 구체 무상 업데이트는 Part II(8). |
| CRA-ARCH-MAIN-20261113-032-003 | #32 | vulnerability handling은 Annex I Part I point 2에 있다. | Annex I Part I, Part II | CRA-REQ-VULNERABILITY-HANDLING-001 | CONFLICT | Part I는 제품 속성, Part II는 vulnerability handling requirements. |
| CRA-ARCH-MAIN-20261113-032-004 | #32 | support period는 최소 5년 또는 expected market cycle로 정한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | expected use를 반영하고 expected use가 5년 미만이면 그 기간에 대응한다. “market cycle”은 법령 용어가 아니다. |
| CRA-ARCH-MAIN-20261113-032-005 | #32 | 지원기간 산정 근거를 기술문서에 포함해야 한다. | Annex VII(4), Article 13(8) | CRA-REQ-TECHDOC-001; CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 기술문서에 support period 결정에 고려한 관련 정보를 포함. |
| CRA-ARCH-MAIN-20261113-032-006 | #32 | Raw Text Quote의 Annex I Part I(2)(2) 위치와 자동 무상 업데이트 문구가 정확하다. | Annex I Part I(2)(c), Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-UPDATE-AVAILABILITY-001; CRA-REQ-AUTO-UPDATE-001 | CONFLICT | 업데이트 가용성/자동 설치/무상 제공 요구를 잘못된 위치와 합성 문구로 제시. |

- #28–#32 파일 단위 판정은 기존 감사 결과대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 CONFLICT를 구분한다. 제품별 적용성은 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #33–#37 원자 주장·인용 분해 (33 claims)

- 원본 감사: [main-only #33–#37 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md).
- 원본 main 경로·blob SHA: #33 \`research_archive/2026-11-13_024039.md\` / \`c9c8f17bae8dd90890f9075927aa5fb6668c32b0\`; #34 \`024544.md\` / \`97101ee32c543adc2b684c92eec4c831cbe2c479\`; #35 \`025045.md\` / \`842b48aa5ba2382ce58cdddcb1f8b836c5336eb6\`; #36 \`025531.md\` / \`06f32803648a15f7638add752a8b9a064d4ee3f9\`; #37 \`030054.md\` / \`a8f77a2ecc3bc2301ab87a5f90d2ae6626489eab\`.
- 공식 기준: Regulation (EU) 2024/2847 및 Commission Implementing Regulation (EU) 2025/2392.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-033-001 | #33 | 제조자는 CVD 정책을 수립·집행해야 한다. | Annex I Part II(5), Article 13(8) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD 정책 의무 확인. |
| CRA-ARCH-MAIN-20261113-033-002 | #33 | 모든 취약점 신고는 PGP 등 특정 암호 방식으로 받아야 한다. | Annex I Part II(5), (6) | CRA-REQ-CVD-POLICY-001; CRA-REQ-CVD-CONTACT-001 | CONFLICT | 안전한 신고 채널/연락 주소 요구와 PGP 키 사용은 구분. PGP는 설계 선택. |
| CRA-ARCH-MAIN-20261113-033-003 | #33 | 수정된 취약점 정보는 보안 업데이트가 제공된 후 공개해야 한다. | Annex I Part II(4) | CRA-REQ-VULN-DISCLOSURE-001 | PARTIALLY_VERIFIED | fixed vulnerability 정보 공개 의무는 있으나 duly justified security-risk case에서 사용자 patch 적용 기회 후로 공개를 지연할 수 있다. |
| CRA-ARCH-MAIN-20261113-033-004 | #33 | 모든 제보 취약점을 European Vulnerability Database/CSIRT에 일반적으로 공유해야 한다. | Annex I Part II(6), Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-CVD-CONTACT-001 | CONFLICT | 일반 취약점 정보 공유/CVD와 Article 14의 제한된 법정 신고 트리거를 구분. |
| CRA-ARCH-MAIN-20261113-033-005 | #33 | 모든 서보 드라이브는 Class I/II 중요 제품이다. | Article 7, Annex III, Implementing Regulation 2025/2392 | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품의 core functionality가 Annex III/기술 설명에 해당하는지 확인 전 분류 불가. |
| CRA-ARCH-MAIN-20261113-033-006 | #33 | Raw Text Quote의 익명 신고·보안 처리·public advisory 문장이 Part II(5)의 정확한 직접 인용이다. | Annex I Part II(4)–(6) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-VULN-DISCLOSURE-001 | CONFLICT | Part II(4),(5),(6)의 문언을 합성했다. |
| CRA-ARCH-MAIN-20261113-034-001 | #34 | 제조자는 제품 취약점과 구성요소를 식별·문서화하고 SBOM을 작성해야 한다. | Annex I Part II(1) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-USER-NOTIFY-001; CRA-REQ-SBOM-001 | VERIFIED | top-level dependencies를 포함하는 machine-readable SBOM 요구 확인. |
| CRA-ARCH-MAIN-20261113-034-002 | #34 | 제조자는 CVD 정책을 수립·집행해야 한다. | Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD 정책 요구 확인. |
| CRA-ARCH-MAIN-20261113-034-003 | #34 | 제조자는 취약점을 적시에 고칠 수 있도록 안전한 업데이트 배포 메커니즘을 제공해야 한다. | Annex I Part II(7) | CRA-REQ-SECURE-UPDATE-DIST-001 | VERIFIED | secure distribution mechanism 요구 확인. |
| CRA-ARCH-MAIN-20261113-034-004 | #34 | 모든 발견 취약점은 ENISA/CSIRT에 정해진 기한으로 신고해야 한다. | Article 14(1)–(7) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | Article 14 trigger는 actively exploited vulnerability 및 severe incident 두 트랙. |
| CRA-ARCH-MAIN-20261113-034-005 | #34 | 제조사 신고 의무 근거는 Article 11이다. | Article 13, Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, 법정 신고 Article 14. |
| CRA-ARCH-MAIN-20261113-034-006 | #34 | Annex I/Article 11의 composite Raw Text Quote가 현행 직접 인용이다. | Annex I Part II(1), (2), (5), (7); Article 14 | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-SBOM-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 서로 다른 조항을 합성한 문장으로 직접 인용 재사용 불가. |
| CRA-ARCH-MAIN-20261113-035-001 | #35 | 제품은 secure-by-default configuration으로 제공되어야 한다. | Annex I Part I(2)(b) | CRA-REQ-SECURE-DEFAULT-001 | VERIFIED | secure default와 original-state reset 가능성 확인. |
| CRA-ARCH-MAIN-20261113-035-002 | #35 | 최초 부팅 시 고유한 비밀번호/암호화 키를 반드시 강제 생성해야 한다. | Annex I Part I(2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 구체 first-boot credential flow는 보편적 직접 법적 의무가 아니다. |
| CRA-ARCH-MAIN-20261113-035-003 | #35 | 필수 작동에 불필요한 모든 네트워크 인터페이스/서비스/포트를 기본 차단해야 한다. | Annex I Part I(2)(j) | CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | attack-surface limitation은 요구되나 모든 인터페이스 일괄 차단 방식은 법령이 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-035-004 | #35 | 초기 설정 과정의 시스템 무결성을 특정 방식으로 기술문서에 증명해야 한다. | Article 31, Annex VII | CRA-REQ-TECHDOC-001; CRA-REQ-INTEGRITY-001 | UNVERIFIED | 기술문서·시험·위험평가 요구는 있으나 보고서의 구체적 “초기 설정 무결성 증명” 범위는 근거/시험 기준 미제시. |
| CRA-ARCH-MAIN-20261113-035-005 | #35 | Raw Text Quote에 latest patch/unique default password/mandatory password change 문구가 현행 Annex I에 있다. | Annex I Part I(2)(b), (c), (d) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DEFAULT-001 | CONFLICT | 제시된 문장은 현행 원문과 불일치하는 합성/비현행 인용. |
| CRA-ARCH-MAIN-20261113-036-001 | #36 | 보안 업데이트는 원칙적으로 무상 제공되어야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-036-002 | #36 | support period는 expected lifetime 또는 5년 중 짧은 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 원칙적으로 최소 5년이며 expected use가 더 짧으면 그 기간에 대응한다. |
| CRA-ARCH-MAIN-20261113-036-003 | #36 | 제조자는 CVD 신고 채널과 취약점 처리 정책을 마련해야 한다. | Annex I Part II(5), (6) | CRA-REQ-CVD-POLICY-001; CRA-REQ-CVD-CONTACT-001 | VERIFIED | CVD policy와 contact address/information sharing을 구분. |
| CRA-ARCH-MAIN-20261113-036-004 | #36 | 듀얼 뱅크 플래시/롤링 업데이트가 CRA가 지정한 필수 구현이다. | Annex I Part II(7), risk assessment | CRA-REQ-SECURE-UPDATE-DIST-001 | UNVERIFIED | 안전한 업데이트 배포 결과 요구와 구체 A/B·dual-bank 구현은 별도. 제품 설계 후보. |
| CRA-ARCH-MAIN-20261113-036-005 | #36 | Annex I Part I(2)(c)가 free security updates를 규정한다. | Annex I Part I(2)(c), Part II(8) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-AUTO-UPDATE-001 | CONFLICT | Part I(2)(c)는 자동 업데이트·사용자 통지·opt-out 관련 제품 속성, 무상 업데이트는 Part II(8). |
| CRA-ARCH-MAIN-20261113-036-006 | #36 | Article 13(6)이 무상 보안 업데이트의 직접 근거다. | Article 13(8), Annex I Part II(8) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 무상 업데이트의 직접 근거는 Part II(8); support period는 Article 13(8). |
| CRA-ARCH-MAIN-20261113-037-001 | #37 | 산업용 서보 드라이브는 Annex III Class I 또는 II에 자동 포함된다. | Article 7, Annex III, Implementing Regulation 2025/2392 | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품의 core functionality와 공식 technical description 확인 전 분류 불가. |
| CRA-ARCH-MAIN-20261113-037-002 | #37 | Class I conformity assessment는 내부 통제 Module A 또는 조건에 따라 Module B+C/Module H 경로가 있다. | Article 32(1), (2); Annex VIII Parts I–IV | CRA-REQ-CONFORMITY-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-TECHDOC-001 | PARTIALLY_VERIFIED | 큰 구조는 맞지만 Article 32(2)의 조건·B+C 경로 및 현행 Annex VIII 위치를 정확히 기술해야 한다. |
| CRA-ARCH-MAIN-20261113-037-003 | #37 | Class II 제품은 Notified Body가 관여하는 Module B+C 또는 Module H 경로를 따른다. | Article 32(3); Annex VIII Parts II–IV | CRA-REQ-CONFORMITY-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-TECHDOC-001 | PARTIALLY_VERIFIED | 제3자 관여와 B+C/H 선택은 맞으나 Module/Annex 매핑을 바로잡아야 한다. |
| CRA-ARCH-MAIN-20261113-037-004 | #37 | conformity assessment 절차의 본문 근거는 Article 24다. | Article 32 | CRA-REQ-CONFORMITY-001 | CONFLICT | 현행 CRA의 conformity assessment procedures는 Article 32. |
| CRA-ARCH-MAIN-20261113-037-005 | #37 | 기술문서의 내용은 Annex VII에 규정된다. | Article 31, Annex VII | CRA-REQ-TECHDOC-001 | VERIFIED | 기술문서 요구와 최소 내용 확인. |
| CRA-ARCH-MAIN-20261113-037-006 | #37 | EU Declaration of Conformity의 본문 근거는 Article 20이다. | Article 28, Annex V/VI | CRA-REQ-DOC-001 | CONFLICT | 현행 EU DoC는 Article 28, Annex V/VI. |
| CRA-ARCH-MAIN-20261113-037-007 | #37 | CE marking의 본문 근거는 Article 30이다. | Article 30 | CRA-REQ-CE-001 | VERIFIED | CE marking 규정 위치 확인. |
| CRA-ARCH-MAIN-20261113-037-008 | #37 | 기술문서의 본문 근거는 Article 23이다. | Article 31, Annex VII | CRA-REQ-TECHDOC-001 | CONFLICT | 현행 technical documentation은 Article 31. |
| CRA-ARCH-MAIN-20261113-037-009 | #37 | Module C는 quality assurance of production process이며 Module H는 class I 전용이다. | Article 32; Annex VIII Parts III/IV | CRA-REQ-CONFORMITY-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-TECHDOC-001 | CONFLICT | Module C는 internal production control, Module H는 full quality assurance이며 Class II에도 Article 32(3) 경로로 사용 가능. |
| CRA-ARCH-MAIN-20261113-037-010 | #37 | Class I/II 분류는 제품명보다 core functionality와 Annex III 기술 설명으로 판단한다. | Article 7(1)–(2); Implementing Regulation 2025/2392 | CRA-REQ-CLASSIFICATION-001 | VERIFIED | 제품 분류 기준 확인. 단, 실제 서보 드라이브의 적용 결과는 UNVERIFIED. |

- #33–#37 파일 단위 판정은 기존 감사 결과대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 CONFLICT를 구분한다. 서보 드라이브의 Class I/II 실제 적용성은 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #38–#42 원자 주장·인용 분해 (33 claims)

- 원본 감사: [main-only #38–#42 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_38_42_2026-11-13.md).
- 원본 main 경로·blob SHA: #38 \`research_archive/2026-11-13_030533.md\` / \`f66d4335654b3b8b9836dcaebe1205eae731c532\`; #39 \`031039.md\` / \`9dfae4ba67f48e056f222bcc86ca3189f8bb384a\`; #40 \`031539.md\` / \`449b601a1df9bef3f3acd789ea2a7fcba0804ea2\`; #41 \`032039.md\` / \`e8d5ef7ead0cb481d158597110e98bdcd006b07c\`; #42 \`032532.md\` / \`0c9ca2e1c69b6bed759f1afa85dd2327d29cf319\`.
- 공식 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-038-001 | #38 | 제품은 사용자에게 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 제공해야 한다. | Annex I Part I(2)(m) | CRA-REQ-SECURE-DATA-ERASURE-001 | VERIFIED | 안전한 영구 삭제 가능성에 관한 제품 기능 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-038-002 | #38 | 제품 안전 폐기 및 사용자 데이터 제거 방법에 관한 상세 지침/정보를 제공해야 한다. | Annex II(8)(d) | CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 지침/정보 제공 의무 확인. |
| CRA-ARCH-MAIN-20261113-038-003 | #38 | 모든 제품은 NAND/EEPROM의 모든 민감 데이터를 물리적으로 복구 불가능하게 소거하는 특정 sanitization 기능을 구현해야 한다. | Annex I Part I(2)(m), Annex II(8)(d) | CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-SECURE-DATA-ERASURE-001 | CONFLICT | 영구 삭제 결과와 특정 메모리/물리 소거 방식은 구분. 법령은 특정 NAND/EEPROM 알고리즘을 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-038-004 | #38 | Annex I Part I(2)(e)/(f)는 데이터 보호·무결성 요구다. | Annex I Part I(2)(e), (f) | CRA-REQ-CONFIDENTIALITY-001; CRA-REQ-INTEGRITY-001; CRA-REQ-SECURE-DATA-ERASURE-001 | VERIFIED | (e)=기밀성, (f)=무결성. 단, 폐기/영구 삭제의 직접 근거는 (m). |
| CRA-ARCH-MAIN-20261113-038-005 | #38 | Annex I Part II가 secure decommissioning의 직접 근거다. | Annex I Part II; Part I(2)(m) | CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-SECURE-DATA-ERASURE-001 | CONFLICT | Part II는 vulnerability handling requirements, secure deletion은 Part I(2)(m) 및 Annex II(8)(d). |
| CRA-ARCH-MAIN-20261113-038-006 | #38 | Raw Text Quote의 잔존 민감 데이터 삭제 문구가 Part I(2)(m)의 정확한 직접 인용이다. | Annex I Part I(2)(m) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-SECURE-DATA-ERASURE-001 | CONFLICT | 보고서의 quote는 다른 요구를 합성했고 현행 원문과 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-039-001 | #39 | support period 동안 취약점을 효과적으로 처리해야 하며 원칙적으로 최소 5년이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | expected use가 5년 미만이면 그 기간에 대응하는 예외 포함. |
| CRA-ARCH-MAIN-20261113-039-002 | #39 | 지원기간 중 제공한 각 보안 업데이트는 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 동안 이용 가능해야 한다. | Article 13(9) | CRA-REQ-UPDATE-AVAILABILITY-001; CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 업데이트 가용성 의무는 support period 자체와 별도. |
| CRA-ARCH-MAIN-20261113-039-003 | #39 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored product에 관한 제조자-사업 사용자 별도 합의 예외 필요. |
| CRA-ARCH-MAIN-20261113-039-004 | #39 | 제조사 의무/무상 업데이트 근거는 Article 11 및 Annex I Part I(1)(h)다. | Article 13(8), Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-RISK-BASELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 13(8)=support period, Part II(8)=free updates; Article 11/Part I(1)(h) 매핑 오류. |
| CRA-ARCH-MAIN-20261113-039-005 | #39 | support period는 expected lifetime 또는 5년 중 짧은 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 원칙은 최소 5년이며 expected use가 5년 미만일 때 그 기간에 대응. |
| CRA-ARCH-MAIN-20261113-039-006 | #39 | Raw Text Quote의 “whichever is shorter” 및 Part I(1)(h) free update 문구가 현행 직접 인용이다. | Article 13(8)–(9), Annex I Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-FREE-UPDATE-001 | CONFLICT | 현행 최종 규정과 문언·조항 위치가 불일치. |
| CRA-ARCH-MAIN-20261113-040-001 | #40 | 제품에는 안전한 설치·운영·유지관리를 위한 정보와 지침이 동반되어야 한다. | Annex II(1)–(2) | CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 정보/지침 요구 확인. |
| CRA-ARCH-MAIN-20261113-040-002 | #40 | 제공되는 기술 보안 지원의 종류와 support period 종료일 정보를 사용자에게 제공해야 한다. | Annex II(7) | CRA-REQ-SUPPORT-END-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 지원기간·지원 정보 제공 요구 확인. |
| CRA-ARCH-MAIN-20261113-040-003 | #40 | Annex II(8)(a)–(f)는 안전한 시운전/사용, 보안 영향, 업데이트, 폐기/데이터 삭제, 자동 업데이트 설정, 통합자 정보 등을 다룬다. | Annex II(8)(a)–(f) | CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-AUTO-UPDATE-001; CRA-REQ-SECURE-DATA-ERASURE-001 | VERIFIED | 항목별 사용자 지침 범위 확인. |
| CRA-ARCH-MAIN-20261113-040-004 | #40 | 기본 관리자 계정 변경, 모든 포트 활성/비활성, 보안 로깅 설정은 모든 제품의 보편적 Annex II 필수 항목이다. | Annex II(8) | CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-ATTACK-SURFACE-001 | CONFLICT | Annex II의 명시 항목과 제품별 위험·기능에 따른 추가 지침을 구분. |
| CRA-ARCH-MAIN-20261113-040-005 | #40 | 사용자 정보 제공 의무의 직접 근거는 Annex I Part I/II다. | Annex II | CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | 사용자 정보·지침의 직접 근거는 Annex II. Annex I는 제품 속성/취약점 처리 요구. |
| CRA-ARCH-MAIN-20261113-040-006 | #40 | Raw Text Quote의 default settings/secure configuration/minimum update period 문장이 Annex II의 정확한 직접 인용이다. | Annex II(1)–(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | 여러 사용자 정보 항목을 합성한 문장으로 직접 인용 재사용 불가. |
| CRA-ARCH-MAIN-20261113-041-001 | #41 | 취약점은 위험에 비례해 지체 없이 처리·시정해야 한다. | Annex I Part II(2) | CRA-REQ-REMEDIATION-001 | VERIFIED | vulnerability remediation 요구 확인. |
| CRA-ARCH-MAIN-20261113-041-002 | #41 | 제품 보안의 효과적이고 정기적인 시험·검토가 요구된다. | Annex I Part II(3) | CRA-REQ-SECURITY-TEST-001 | VERIFIED | regular testing/review 요구 확인. |
| CRA-ARCH-MAIN-20261113-041-003 | #41 | 수정된 취약점 정보는 보안 업데이트가 제공된 후 공개해야 하며 정당한 보안 위험 시 지연 가능하다. | Annex I Part II(4) | CRA-REQ-VULN-DISCLOSURE-001 | VERIFIED | 공개 시점과 justified delay 예외 확인. |
| CRA-ARCH-MAIN-20261113-041-004 | #41 | 취약점의 적시 수정·완화를 위한 안전한 업데이트 배포 메커니즘이 요구된다. | Annex I Part II(7) | CRA-REQ-SECURE-UPDATE-DIST-001 | VERIFIED | secure distribution mechanism 요구 확인. |
| CRA-ARCH-MAIN-20261113-041-005 | #41 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-041-006 | #41 | 모든 제품은 특정 digital signing/rollback/fail-safe 방식으로 패치를 배포해야 한다. | Annex I Part II(7), risk assessment | CRA-REQ-SECURE-UPDATE-DIST-001 | CONFLICT | secure distribution 결과 요구와 특정 서명·rollback 구현은 구분. 위험기반 설계 선택. |
| CRA-ARCH-MAIN-20261113-041-007 | #41 | Article 11 및 composite Raw Text Quote가 취약점 처리 요구의 정확한 근거다. | Article 13(8), Annex I Part II(2)–(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REMEDIATION-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, Part II 항목별 문언을 합성하지 않는다. |
| CRA-ARCH-MAIN-20261113-042-001 | #42 | 제조자는 CVD 정책을 수립·집행해야 한다. | Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | 정책 요구 확인. |
| CRA-ARCH-MAIN-20261113-042-002 | #42 | 제조자는 취약점 신고 연락 주소를 제공해야 한다. | Annex I Part II(6) | CRA-REQ-CVD-CONTACT-001 | VERIFIED | contact address 요구 확인. |
| CRA-ARCH-MAIN-20261113-042-003 | #42 | 수정된 취약점 정보는 보안 업데이트 제공 후 공개해야 한다. | Annex I Part II(4) | CRA-REQ-VULN-DISCLOSURE-001 | PARTIALLY_VERIFIED | justified security-risk case에서 사용자 patch 적용 기회 후로 지연 가능. |
| CRA-ARCH-MAIN-20261113-042-004 | #42 | 사용자 단일 연락 창구와 CVD 정책을 찾을 수 있는 정보를 제공해야 한다. | Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 정보 및 contact point 요구 확인. |
| CRA-ARCH-MAIN-20261113-042-005 | #42 | 모든 취약점 보안 권고문을 ENISA/CSIRT에 동시에 신고해야 한다. | Article 14(1)–(7), Annex I Part II(4)–(6) | CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | 일반 CVD/public disclosure와 Article 14의 제한된 법정 신고 트리거를 혼합. |
| CRA-ARCH-MAIN-20261113-042-006 | #42 | 일반 서보 드라이브는 Class I/II 중요 제품이다. | Article 7, Annex III | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 core functionality 및 Annex III 범주 증거 없음. |
| CRA-ARCH-MAIN-20261113-042-007 | #42 | VDP 근거는 Article 11 및 Annex I Part I이다. | Article 13(8), Annex I Part II(5)/(6) | CRA-REQ-CVD-POLICY-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, CVD/contact Part II(5)/(6). |
| CRA-ARCH-MAIN-20261113-042-008 | #42 | Raw Text Quote가 현행 CVD/Article14 문언의 정확한 직접 인용이다. | Annex I Part II(4)–(6), Article 14 | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | 조항·문언·신고 범위를 합성했으므로 재사용 불가. |

- #38–#42 파일 단위 판정은 기존 감사 결과대로 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- #38은 Annex I Part I(2)(m) 후속 확인으로 PARTIALLY_VERIFIED로 정정된 최신 판정을 유지한다.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 판정을 구분한다. 제품별 적용성 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #43–#47 원자 주장·인용 분해 (37 claims)

- 원본 감사: [main-only #43–#47 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_43_47_2026-11-13.md).
- 원본 main 경로·blob SHA: #43 \`research_archive/2026-11-13_033047.md\` / \`aaea865c90a6c082b172403248c07d5dda783102\`; #44 \`033533.md\` / \`4641a3feeb5654f1abd3c59323825c7f7a5145cc\`; #45 \`034038.md\` / \`ffe8ac1e5e41b80859631ac4c4975b0f6fc71bf5\`; #46 \`034535.md\` / \`61c22b5a97fc0e053668da26956b21f7ea85fe5c\`; #47 \`035035.md\` / \`e5f3d9fb2fb4cda62a5fc04a50e64f3d05ca1218\`.
- 공식 기준: Regulation (EU) 2024/2847 및 Commission Implementing Regulation (EU) 2025/2392.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-043-001 | #43 | CRA Annex III Class II에 IACS/PLC/servo drive가 열거되어 있다. | Annex III, Implementing Regulation 2025/2392 Annex I | CRA-REQ-CLASSIFICATION-001 | CONFLICT | Class II의 실제 범주는 hypervisor/container runtime, firewall/IDS/IPS, tamper-resistant microprocessors/controllers. |
| CRA-ARCH-MAIN-20261113-043-002 | #43 | Class II는 네 가지 공식 제품 범주로 구체화된다. | Annex III, Implementing Regulation 2025/2392 Annex I | CRA-REQ-CLASSIFICATION-001 | VERIFIED | 네 범주와 기술 설명 확인. |
| CRA-ARCH-MAIN-20261113-043-003 | #43 | 산업용 서보 드라이브는 Class II에 자동 해당한다. | Article 7(1), Annex III, Implementing Regulation 2025/2392 | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 core functionality와 technical description 증거가 없어 분류 불가. |
| CRA-ARCH-MAIN-20261113-043-004 | #43 | Class II 제품은 Module B+C 또는 Module H 등 Article 32(3)의 제3자 평가 경로를 따른다. | Article 32(3), Annex VIII | CRA-REQ-CONFORMITY-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-TECHDOC-001 | VERIFIED | 실제 Class II 해당성이 확인된 경우의 절차. |
| CRA-ARCH-MAIN-20261113-043-005 | #43 | CRA conformity assessment 절차의 근거는 Article 24다. | Article 32; Article 24 | CRA-REQ-CONFORMITY-001 | CONFLICT | Article 24는 open-source software stewards, conformity assessment는 Article 32. |
| CRA-ARCH-MAIN-20261113-043-006 | #43 | Article 32 위반 과징금은 EUR 15m 또는 3% 중 높은 금액이다. | Article 64(3) | CRA-REQ-PENALTY-001; CRA-REQ-CONFORMITY-001 | CONFLICT | Article 32(1)–(3) 위반은 EUR 10m 또는 2% 중 높은 금액. |
| CRA-ARCH-MAIN-20261113-043-007 | #43 | Annex I/Article 13/14 의무 위반은 최대 EUR 15m 또는 2.5% 중 높은 금액의 과징금 트랙이다. | Article 64(2) | CRA-REQ-PENALTY-001 | VERIFIED | 정확한 조항별 penalty track 확인. |
| CRA-ARCH-MAIN-20261113-043-008 | #43 | Annex III Class II에 IACS/PLC/servo drive를 열거한 Raw Text Quote가 최종 법령의 직접 인용이다. | Annex III | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-CLASSIFICATION-001 | CONFLICT | 해당 문장은 최종 Annex III에 존재하지 않는다. |
| CRA-ARCH-MAIN-20261113-044-001 | #44 | 제품은 무단 접근을 막기 위한 적절한 제어 메커니즘을 갖춰야 한다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | VERIFIED | 접근통제 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-044-002 | #44 | 접근통제에는 인증·ID·접근관리 시스템이 포함되며 가능한 무단 접근을 보고해야 한다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | VERIFIED | 현행 문언과 일치. |
| CRA-ARCH-MAIN-20261113-044-003 | #44 | 모든 서보 드라이브에 RBAC와 least-privilege architecture가 각각 명문 보편 의무다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 적절한 접근통제 결과 요구와 특정 권한 모델을 구분. |
| CRA-ARCH-MAIN-20261113-044-004 | #44 | Operator/Engineer/OEM 3단계 역할 및 STO/게인 변경 관리자 인증이 법령의 직접 필수 구조다. | Annex I Part I(2)(d), risk assessment | CRA-REQ-ACCESS-CONTROL-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | UNVERIFIED | 합리적인 설계 후보이나 제품 위험평가·기능 구조 없이 보편 의무로 단정 불가. |
| CRA-ARCH-MAIN-20261113-044-005 | #44 | 동일 하드코딩 비밀번호·백도어 계정이 CRA의 명시적 보편 금지 문구다. | Annex I Part I(1), (2)(b), (d) | CRA-REQ-SECURE-DEFAULT-001; CRA-REQ-ACCESS-CONTROL-001; CRA-REQ-RISK-BASELINE-001 | CONFLICT | secure-by-default/appropriate access controls와 특정 금지 문구를 혼동. |
| CRA-ARCH-MAIN-20261113-044-006 | #44 | 최초 접속 시 고유 비밀번호 강제 또는 인증서 기반 인증이 모든 제품의 명문 의무다. | Annex I Part I(2)(d) | CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 인증 방식은 위험기반 설계 선택이며 조항이 특정 방식을 일률 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-044-007 | #44 | Raw Text Quote의 Annex I Section 1/Section 2 point 1(a) 인용이 현행 직접 인용이다. | Annex I Part I(2)(d) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-ACCESS-CONTROL-001 | CONFLICT | 정확한 위치는 Part I point 2(d), 보고서의 인용 위치/문언 불일치. |
| CRA-ARCH-MAIN-20261113-045-001 | #45 | 제조자는 제품 취약점을 수집·분석·처리할 vulnerability handling 체계를 갖춰야 한다. | Article 13(8), Annex I Part II(1)–(8) | CRA-REQ-SBOM-001 | VERIFIED | 취약점 처리 체계 요구 확인. |
| CRA-ARCH-MAIN-20261113-045-002 | #45 | 제조사 의무의 상위 조항은 Article 11이다. | Article 13 | CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 현행 제조사 의무는 Article 13. |
| CRA-ARCH-MAIN-20261113-045-003 | #45 | Part II(1)은 취약점·구성요소 식별·문서화 및 SBOM을 요구한다. | Annex I Part II(1) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-SBOM-001; CRA-REQ-AUTO-UPDATE-001 | VERIFIED | 자동 업데이트 조항이 아니다. |
| CRA-ARCH-MAIN-20261113-045-004 | #45 | 취약점은 위험에 비례해 지체 없이 처리·시정해야 한다. | Annex I Part II(2) | CRA-REQ-REMEDIATION-001 | VERIFIED | remediation 요구 확인. |
| CRA-ARCH-MAIN-20261113-045-005 | #45 | 제품 보안의 효과적이고 정기적인 시험·검토가 요구된다. | Annex I Part II(3) | CRA-REQ-SECURITY-TEST-001 | VERIFIED | regular testing/review 요구 확인. |
| CRA-ARCH-MAIN-20261113-045-006 | #45 | 수정된 취약점 정보는 보안 업데이트 제공 후 공개해야 하며 정당한 경우 지연 가능하다. | Annex I Part II(4) | CRA-REQ-VULN-DISCLOSURE-001 | VERIFIED | justified delay 예외 포함. |
| CRA-ARCH-MAIN-20261113-045-007 | #45 | 취약점의 안전한 수정·완화를 위한 업데이트 배포 메커니즘이 요구된다. | Annex I Part II(7) | CRA-REQ-SECURE-UPDATE-DIST-001 | VERIFIED | secure distribution mechanism 요구 확인. |
| CRA-ARCH-MAIN-20261113-045-008 | #45 | 보안 업데이트는 원칙적으로 무상 제공되고 advisory message가 동반된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품의 제조자-사업 사용자 합의 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-045-009 | #45 | Article 11(7) 및 Part II(1) 자동 업데이트 Raw Text Quote가 현행 직접 인용이다. | Article 13(8), Annex I Part II(1)–(2) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-COMPONENT-DUE-001; CRA-REQ-SBOM-001; CRA-REQ-AUTO-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 조항·문언이 불일치; Part II(1)은 SBOM/구성요소 식별. |
| CRA-ARCH-MAIN-20261113-046-001 | #46 | 모든 발견 취약점의 보안 업데이트는 예상 수명 동안 계약과 무관하게 무상 제공된다. | Annex I Part II(8), Article 13(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | 원칙적 무상 제공은 맞지만 tailored-product/business-user agreement exception 및 support period 산정 별도. |
| CRA-ARCH-MAIN-20261113-046-002 | #46 | 무상 업데이트 의무의 근거는 Article 11이다. | Article 13, Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 11 오기; 무상 업데이트 직접 근거는 Part II(8). |
| CRA-ARCH-MAIN-20261113-046-003 | #46 | 계약/SLA와 무관하게 모든 사용자에게 예외 없이 무상 업데이트해야 한다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | CONFLICT | tailored product에 관한 제조자와 business user 간 별도 합의 예외 존재. |
| CRA-ARCH-MAIN-20261113-046-004 | #46 | support period는 예상 사용기간을 반영하고 최소 5년이며 expected use가 더 짧으면 그 기간에 대응한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 정확한 지원기간 구조 확인. |
| CRA-ARCH-MAIN-20261113-046-005 | #46 | CVD 정책과 수정 취약점 정보 공개는 CRA 요구사항이다. | Annex I Part II(4), (5) | CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-CVD-POLICY-001 | VERIFIED | 공개와 CVD 정책을 별도 항목으로 추적. |
| CRA-ARCH-MAIN-20261113-046-006 | #46 | 모든 일반 취약점은 ENISA/국가 당국에 즉시 신고해야 한다. | Article 14(1)–(7) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | Article 14의 두 신고 trigger로 제한; CVD 일반 프로세스와 분리. |
| CRA-ARCH-MAIN-20261113-046-007 | #46 | Article 11/Annex I Raw Text Quote가 현행 직접 인용이다. | Article 13(8), Annex I Part II(4), (8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 조항·문언·예외 구조 불일치. |
| CRA-ARCH-MAIN-20261113-047-001 | #47 | 지원기간은 최소 5년 또는 expected lifetime 중 더 긴 기간을 모든 제품에 예외 없이 적용한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | expected use가 5년 미만이면 그 기간에 대응하는 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-047-002 | #47 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-047-003 | #47 | Article 13(8) support period와 Article 13(9) update availability는 별도 의무다. | Article 13(8), (9) | CRA-REQ-UPDATE-AVAILABILITY-001; CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 지원기간과 업데이트 장기 가용성 구분. |
| CRA-ARCH-MAIN-20261113-047-004 | #47 | 모든 제품은 계약과 관계없이 예상 수명 전체의 패치를 무상 제공해야 한다. | Annex I Part II(8), Article 13(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | free update 예외 및 support period 구조 누락. |
| CRA-ARCH-MAIN-20261113-047-005 | #47 | Article 11/Annex I Part I/PE-CONS 103/23 인용이 현행 최종 법령 직접 인용이다. | Article 13(8), Annex I Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 조항·위치·문언이 최종 법령과 일치하지 않는다. |
| CRA-ARCH-MAIN-20261113-047-006 | #47 | 서보 드라이브가 Class I/II 제품으로 분류된다. | Article 7, Annex III, Implementing Regulation 2025/2392 | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | 제품 core functionality 및 technical description 증거 없음. |

- #43–#47 파일 단위 판정은 기존 감사 결과대로 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 판정을 구분한다. 제품별 적용성 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #48–#52 원자 주장·인용 분해 (36 claims)

- 원본 감사: [main-only #48–#52 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md).
- 원본 main 경로·blob SHA: #48 \`research_archive/2026-11-13_035531.md\` / \`539b1d73d7053c5b1e252c775c503b055e978dd9\`; #49 \`040051.md\` / \`3d661d5545974406fee419f60234f99d29427495\`; #50 \`040534.md\` / \`8bbfe9b22a009c90dba493d3086462bb605a1b50\`; #51 \`041039.md\` / \`8625c7e82389aea9cd3e5a0694cd0b920c90e8cf\`; #52 \`041532.md\` / \`3672c41635364ef99b494cd8944c4998bbfc01c8\`.
- 공식 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-048-001 | #48 | 제조자는 취약점을 처리하고 보안 업데이트를 제공해야 한다. | Article 13(8), Annex I Part II(2) | CRA-REQ-REMEDIATION-001 | VERIFIED | vulnerability handling/updates 요구 확인. |
| CRA-ARCH-MAIN-20261113-048-002 | #48 | Article 14(8)은 active exploited vulnerability/severe incident 통지에 기계 판독 가능 형식을 적절한 경우 허용한다. | Article 14(8) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | trigger 및 where appropriate 조건 확인. |
| CRA-ARCH-MAIN-20261113-048-003 | #48 | 모든 취약점 정보와 패치는 사용자/ENISA/CSIRT에 자동 기계 판독 가능 형식으로 제공해야 한다. | Article 14(8), Annex I Part II(4)–(6) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-VULN-DISCLOSURE-001 | CONFLICT | 모든 취약점 일반 의무가 아니며 CSAF 등 특정 형식은 지정되지 않는다. |
| CRA-ARCH-MAIN-20261113-048-004 | #48 | CSAF는 CRA가 지정한 의무 보안 권고 형식이다. | Article 14(8), Annex I Part II(4) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-VULN-DISCLOSURE-001 | CONFLICT | CSAF는 구현 선택지/표준 후보이지 해당 조항의 의무 형식이 아니다. |
| CRA-ARCH-MAIN-20261113-048-005 | #48 | 제조사 의무 근거는 Article 11이다. | Article 13(8), Annex I Part II | CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 현행 제조사 의무는 Article 13. |
| CRA-ARCH-MAIN-20261113-048-006 | #48 | Part II(2)/Article 11 Raw Text Quote가 현행 직접 인용이다. | Annex I Part II(2), Article 13(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REMEDIATION-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 인용문은 Part II(2)의 정확한 원문이 아니며 Article 11도 오기. |
| CRA-ARCH-MAIN-20261113-049-001 | #49 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-049-002 | #49 | 모든 취약점과 모든 사고를 ENISA에 신고해야 한다. | Article 14(1)–(7) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | actively exploited vulnerability와 severe incident 두 trigger로 한정. |
| CRA-ARCH-MAIN-20261113-049-003 | #49 | 24h early warning은 Article 14의 신고 단계다. | Article 14(2)(a), (4)(a) | CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | 두 trigger에 한정하며 72h 및 final report 14일/1개월을 함께 구분해야 한다. |
| CRA-ARCH-MAIN-20261113-049-004 | #49 | support period는 expected lifetime과 5년 중 짧은 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | CONFLICT | 최소 5년, expected use가 5년 미만이면 그 기간에 대응. |
| CRA-ARCH-MAIN-20261113-049-005 | #49 | 보안 업데이트는 기능 저하/중단을 절대 일으키지 않아야 하고 rollback/fail-safe가 법령의 직접 의무다. | Annex I Part II(7), risk assessment | CRA-REQ-SECURE-UPDATE-DIST-001 | CONFLICT | secure update distribution 결과 요구와 특정 무중단/rollback 구현을 구분. |
| CRA-ARCH-MAIN-20261113-049-006 | #49 | 제조사 의무/신고 근거는 Article 11이다. | Article 13, Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 제조사 의무 Article 13, 법정 신고 Article 14. |
| CRA-ARCH-MAIN-20261113-049-007 | #49 | Article 11(1)/Annex I Part I(2)(1) Raw Text Quote가 현행 직접 인용이다. | Article 14(2), Annex I Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 조항·기한·지원기간 문언이 최종 법령과 불일치. |
| CRA-ARCH-MAIN-20261113-050-001 | #50 | 산업용 서보 드라이브는 Important Product Class I에 자동 해당한다. | Article 7, Annex III, Implementing Regulation 2025/2392 | CRA-REQ-CLASSIFICATION-001 | UNVERIFIED | core functionality 및 technical description 증거 없으므로 제품별 분류 불가. |
| CRA-ARCH-MAIN-20261113-050-002 | #50 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | 맞춤형 제품의 제조자-사업 사용자 합의 예외 포함 필요. |
| CRA-ARCH-MAIN-20261113-050-003 | #50 | 수정 취약점 정보는 보안 업데이트 제공 후 공개해야 한다. | Annex I Part II(4) | CRA-REQ-VULN-DISCLOSURE-001 | PARTIALLY_VERIFIED | justified security-risk case의 공개 지연 예외 포함. |
| CRA-ARCH-MAIN-20261113-050-004 | #50 | CVSS 점수/영향 펌웨어 버전/공식 채널 공개 형식이 모든 제품에 법정 필수다. | Annex I Part II(4), (8) | CRA-REQ-VULN-DISCLOSURE-001 | UNVERIFIED | 유용한 advisory 필드일 수 있으나 CRA가 이 세부 형식을 일률 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-050-005 | #50 | 제조사 의무는 Article 11, CVD/free updates는 Part I/II generic 항목이다. | Article 13(8), Annex I Part II(4), (5), (8) | CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | CVD (5), disclosure (4), free updates (8), manufacturer Article 13으로 분리. |
| CRA-ARCH-MAIN-20261113-050-006 | #50 | 모든 취약점을 조건 없이 즉시 공개해야 한다. | Annex I Part II(4) | CRA-REQ-VULN-DISCLOSURE-001 | CONFLICT | fixed vulnerability 공개는 보안 업데이트 제공 후이며 justified delay 예외가 있다. |
| CRA-ARCH-MAIN-20261113-051-001 | #51 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD policy requirement 확인. |
| CRA-ARCH-MAIN-20261113-051-002 | #51 | 취약점 신고 연락 주소와 정보 공유 촉진 조치를 제공해야 한다. | Annex I Part II(6) | CRA-REQ-CVD-CONTACT-001 | VERIFIED | contact address 및 information sharing 요구 확인. |
| CRA-ARCH-MAIN-20261113-051-003 | #51 | 사용자에게 CVD 정책을 찾을 수 있는 위치와 단일 연락 창구를 안내해야 한다. | Article 13(17), Annex II(2) | CRA-REQ-USER-CONTACT-001; CRA-REQ-CVD-POLICY-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 정보에 포함하는 요구 확인. |
| CRA-ARCH-MAIN-20261113-051-004 | #51 | PGP 암호화가 CRA의 보편적 직접 의무다. | Annex I Part II(5), (6) | CRA-REQ-CVD-POLICY-001 | CONFLICT | 안전한 신고 채널 구현 선택이며 특정 암호 기술은 지정하지 않는다. |
| CRA-ARCH-MAIN-20261113-051-005 | #51 | 모든 제보에 고정된 법정 응답기한/CVE 발급/공개 타임라인이 있다. | Annex I Part II(4)–(6), Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-VULN-DISCLOSURE-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | CVD 운영 SLA와 Article 14의 제한된 신고기한을 구분. |
| CRA-ARCH-MAIN-20261113-051-006 | #51 | VDP 의무의 근거는 Annex I Part I 및 Article 10이다. | Article 13(8), Annex I Part II(5), (6) | CRA-REQ-CVD-POLICY-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 정확한 근거는 Article 13(8), Part II(5)/(6). |
| CRA-ARCH-MAIN-20261113-051-007 | #51 | Raw Text Quote가 현행 CVD policy 문언의 직접 인용이다. | Annex I Part II(5), (6) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | 인용 위치와 문언이 불일치. |
| CRA-ARCH-MAIN-20261113-052-001 | #52 | 제조자는 통합 제3자 구성요소에 대해 due diligence를 수행해야 한다. | Article 13(5) | CRA-REQ-COMPONENT-DUE-001 | VERIFIED | 제3자 구성요소 실사 의무 확인. |
| CRA-ARCH-MAIN-20261113-052-002 | #52 | 통합 구성요소의 취약점을 식별한 제조자는 해당 구성요소 제조자/유지관리 주체에 보고하고 제품 측 조치를 수행해야 한다. | Article 13(6) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-REMEDIATION-001 | VERIFIED | 공급망 취약점 보고 방향과 시정 의무 확인. |
| CRA-ARCH-MAIN-20261113-052-003 | #52 | 제조사가 취약점 수정을 위해 소프트웨어 변경을 개발한 경우 적절한 때 관련 코드/문서를 구성요소 제조자/유지관리 주체와 공유한다. | Article 13(6) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-USER-NOTIFY-001 | VERIFIED | 기계 판독 가능 형식 조건을 포함해 정확히 추적. |
| CRA-ARCH-MAIN-20261113-052-004 | #52 | 제조자는 제3자 구성요소의 사이버보안 측면과 취약점 관련 정보를 체계적으로 문서화해야 한다. | Article 13(7) | CRA-REQ-TECHDOC-001; CRA-REQ-COMPONENT-DUE-001 | VERIFIED | technical documentation/recording 요구 확인. |
| CRA-ARCH-MAIN-20261113-052-005 | #52 | 모든 구성요소 공급자는 모든 취약점을 상위 서보 드라이브 제조사에 즉시 통보해야 한다는 일반 의무가 있다. | Article 13(5)–(7) | CRA-REQ-COMPONENT-DUE-001 | CONFLICT | Article 13(6)의 명시적 보고 방향은 취약점을 식별한 제조자에서 구성요소 제조자/유지관리 주체로 향한다. |
| CRA-ARCH-MAIN-20261113-052-006 | #52 | 제조자는 모든 구성요소 취약점을 모든 통합자/최종 사용자에게 자동 통지해야 한다. | Article 14(8), Annex I Part II(4) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-VULN-DISCLOSURE-001 | CONFLICT | 사용자 통지 및 공개는 해당 trigger/조건/시점에 따라 별도 적용. |
| CRA-ARCH-MAIN-20261113-052-007 | #52 | 보안 업데이트는 원칙적으로 무상 제공된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-052-008 | #52 | support period는 최소 5년이며 expected use가 더 짧으면 그 기간에 대응한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 정확한 지원기간 구조 확인. |
| CRA-ARCH-MAIN-20261113-052-009 | #52 | Article 14는 모든 공급망 취약점 정보를 ENISA에 신고하도록 한다. | Article 14(1)–(7), Article 13(6) | CRA-REQ-COMPONENT-DUE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | 공급망 구성요소 취약점 처리와 Article 14의 active/severe 신고 트리거를 구분. |
| CRA-ARCH-MAIN-20261113-052-010 | #52 | Article 11/Annex I Part II composite Raw Text Quote가 현행 직접 인용이다. | Article 13(5)–(8), Annex I Part II(1)–(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-COMPONENT-DUE-001; CRA-REQ-SBOM-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 초안/합성 문구이며 직접 인용 재사용 불가. |

- #48–#52 파일 단위 판정은 기존 감사 결과대로 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 판정을 구분한다. 제품별 적용성 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 — #53–#57 원자 주장·인용 분해 (32 claims)

- 원본 감사: [main-only #53–#57 Pass A/B/C 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_53_57_2026-11-13.md).
- 원본 main 경로·blob SHA: #53 \`research_archive/2026-11-13_042039.md\` / \`16f8497915fe4a9233cb18f27f215b4a5e0565d3\`; #54 \`042528.md\` / \`f5acd2a0370dd02b42ad2409dd34cefd6823deea\`; #55 \`043042.md\` / \`cb622a6a4ef322b19479b96d6238cdb865b11799\`; #56 \`043528.md\` / \`aaf77db2c4f7d7d1cad9917383c6f9aa5040fc3b\`; #57 \`044041.md\` / \`089f816a2d93f84f0c95aead1957f4dc78b7ccba\`.
- 공식 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024.

| Claim ID | 원본 | 원자 주장 | 근거 위치 | Canonical ID | 상태 | 판정/정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261113-053-001 | #53 | 해당되는 제품은 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 제공해야 한다. | Annex I Part I(2)(m) | CRA-REQ-SECURE-DATA-ERASURE-001 | VERIFIED | 제품 기능 결과 요구 확인. |
| CRA-ARCH-MAIN-20261113-053-002 | #53 | 안전한 제품 폐기 및 사용자 데이터 제거 방법에 관한 상세 지침/정보를 제공해야 한다. | Annex II(8)(d) | CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 지침 의무 확인. |
| CRA-ARCH-MAIN-20261113-053-003 | #53 | 사용자 정보/지침은 Article 13(18)에 따라 법정 기간 동안 이용 가능해야 한다. | Article 13(18), Annex II | CRA-REQ-USER-INFO-RETENTION-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 최소 10년 또는 support period 중 더 긴 기간의 가용성 요구. |
| CRA-ARCH-MAIN-20261113-053-004 | #53 | 지원기간 종료일을 구매 시 명확히 표시하고 기술적으로 가능한 경우 종료 시점 알림을 제공해야 한다. | Article 13(19) | CRA-REQ-SUPPORT-END-001; CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 종료일 표시 및 where technically possible 알림 요구 확인. |
| CRA-ARCH-MAIN-20261113-053-005 | #53 | 모든 제품은 NAND/EEPROM을 특정 방식으로 물리 소거해 모든 데이터 복구를 불가능하게 해야 한다. | Annex I Part I(2)(m), Annex II(8)(d) | CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-SECURE-DATA-ERASURE-001 | CONFLICT | secure permanent erasure 결과 요구와 특정 NAND/EEPROM 알고리즘·물리 파기 방식을 구분. |
| CRA-ARCH-MAIN-20261113-053-006 | #53 | 제조사는 법령이 정한 특정 사전 통지 기간으로 모든 고객에게 EOL을 미리 통지해야 한다. | Article 13(19), Annex II(7) | CRA-REQ-SUPPORT-END-001; CRA-REQ-USER-INSTRUCTIONS-001 | CONFLICT | 구매 시 종료일 표시 및 기술적으로 가능한 종료 알림과 특정 사전 통지 기간을 혼동. |
| CRA-ARCH-MAIN-20261113-053-007 | #53 | Annex I Part I(1)/(2)(h)와 Part II 인용이 secure deletion의 직접 근거다. | Annex I Part I(2)(m), Annex II(8)(d) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-USER-INSTRUCTIONS-001; CRA-REQ-SECURE-DATA-ERASURE-001; CRA-REQ-RISK-BASELINE-001 | CONFLICT | 직접 근거는 Part I(2)(m) 및 Annex II(8)(d); Raw Text Quote 재사용 불가. |
| CRA-ARCH-MAIN-20261113-054-001 | #54 | support period는 제품 예상 사용기간을 반영하고 원칙적으로 최소 5년이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | expected use가 5년 미만이면 그 기간에 대응하는 예외 포함. |
| CRA-ARCH-MAIN-20261113-054-002 | #54 | support period 산정에 고려한 정보를 기술문서에 포함해야 한다. | Article 13(8), Annex VII(4) | CRA-REQ-TECHDOC-001; CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | support period 결정에 고려한 관련 정보 기록. |
| CRA-ARCH-MAIN-20261113-054-003 | #54 | 기술 보안 지원 유형과 support period 종료일을 사용자에게 제공해야 한다. | Annex II(7), Article 13(19) | CRA-REQ-SUPPORT-END-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-USER-INSTRUCTIONS-001 | VERIFIED | 사용자 정보 및 종료일 표시 요구 확인. |
| CRA-ARCH-MAIN-20261113-054-004 | #54 | 지원기간은 모든 제품에서 예상 사용기간과 5년 중 더 긴 기간이다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | expected use가 5년 미만이면 그 기간에 대응한다는 예외를 포함해야 한다. |
| CRA-ARCH-MAIN-20261113-054-005 | #54 | support period 동안 제공되는 보안 업데이트는 예외 없이 무상이다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001 | PARTIALLY_VERIFIED | 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 예외가 있다. |
| CRA-ARCH-MAIN-20261113-055-001 | #55 | 보안 업데이트는 원칙적으로 무상 제공되고 advisory message가 동반된다. | Annex I Part II(8) | CRA-REQ-FREE-UPDATE-001 | PARTIALLY_VERIFIED | tailored-product/business-user agreement exception 포함 필요. |
| CRA-ARCH-MAIN-20261113-055-002 | #55 | support period는 Article 13(8)에 따라 expected use와 5년 최소 원칙을 반영한다. | Article 13(8) | CRA-REQ-SUPPORT-PERIOD-001 | VERIFIED | 5년 미만 expected use 예외 포함. |
| CRA-ARCH-MAIN-20261113-055-003 | #55 | 패치가 즉시 적용되지 않으면 모든 취약점에 대해 특정 workaround를 반드시 제공해야 한다. | Annex I Part II(2), (8); Article 14(2)(b), (4)(b) | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-REMEDIATION-001 | PARTIALLY_VERIFIED | 관련 정보·잠재 조치 advisory 및 법정 신고 사건의 mitigation 정보를 구분; 모든 일반 취약점에 동일 workaround 의무는 아님. |
| CRA-ARCH-MAIN-20261113-055-004 | #55 | 패치는 모든 서보 드라이브에서 실시간 제어 성능/호환성 저하를 절대 일으키지 않아야 한다. | Annex I Part II(2), (7), risk assessment | CRA-REQ-REMEDIATION-001 | UNVERIFIED | 안전한 업데이트와 위험기반 검증은 필요하나 이 절대 성능 기준은 별도 제품 시험/승인 필요. |
| CRA-ARCH-MAIN-20261113-055-005 | #55 | 무상 업데이트의 직접 근거는 Article 13(4)다. | Annex I Part II(8), Article 13(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-SUPPORT-PERIOD-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | CONFLICT | 무상 업데이트 Part II(8), support period Article 13(8). |
| CRA-ARCH-MAIN-20261113-055-006 | #55 | Annex I Part I(2)(1)(g)가 free update 의무를 규정한다. | Annex I Part I(2)(g), Part II(8) | CRA-REQ-FREE-UPDATE-001; CRA-REQ-DATA-MINIMIZATION-001 | CONFLICT | Part I 2(g)는 data minimisation, 무상 업데이트는 Part II(8). |
| CRA-ARCH-MAIN-20261113-055-007 | #55 | Article 13(4)/Part I(2)(g) Raw Text Quote가 현행 직접 인용이다. | Article 13(8), Annex I Part II(8) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-FREE-UPDATE-001; CRA-REQ-PRODUCT-RISK-ASSESSMENT-001 | CONFLICT | 조항 번호·문언 불일치. |
| CRA-ARCH-MAIN-20261113-056-001 | #56 | 제조자는 CVD 정책을 수립·집행해야 한다. | Article 13(8), Annex I Part II(5) | CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD policy requirement 확인. |
| CRA-ARCH-MAIN-20261113-056-002 | #56 | actively exploited vulnerability와 severe incident는 Article 14 신고 대상이다. | Article 14(1)–(4) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 두 신고 트랙 확인. |
| CRA-ARCH-MAIN-20261113-056-003 | #56 | 24h/72h 초기 신고 기한이 두 트랙에 적용된다. | Article 14(2), (4) | CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | final report 기한은 취약점 14일, severe incident 1개월로 구분해야 한다. |
| CRA-ARCH-MAIN-20261113-056-004 | #56 | 모든 잠재 취약점/버그/보안 사고가 Article 14 신고 대상이다. | Article 14(1)–(4) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | actively exploited vulnerability 및 제품 보안에 영향을 미치는 severe incident로 제한. |
| CRA-ARCH-MAIN-20261113-056-005 | #56 | CVD 정책과 Article 14 법정 신고는 별도 절차다. | Annex I Part II(5)/(6), Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-CVD-POLICY-001 | VERIFIED | CVD 접수와 법정 신고 트리거 구분. |
| CRA-ARCH-MAIN-20261113-056-006 | #56 | Raw Text Quote가 Article 14/Annex I Part II의 정확한 직접 인용이다. | Article 14(1)–(8), Annex I Part II(5)/(6) | CRA-EVIDENCE-QUOTE-ACCURACY-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-CVD-POLICY-001 | CONFLICT | 조항·문언을 합성했으므로 재사용 불가. |
| CRA-ARCH-MAIN-20261113-057-001 | #57 | Article 14 신고 의무는 Class I/II뿐 아니라 CRA 범위 제품에 적용된다. | Article 14, Article 69(3) | CRA-REQ-TRANSITION-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | 2027-12-11 이전 출시 제품에도 Article 14 적용. |
| CRA-ARCH-MAIN-20261113-057-002 | #57 | actively exploited vulnerability 신고는 24h/72h 및 시정조치 이용 후 14일 final report를 갖는다. | Article 14(2) | CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | 원본은 24h/72h를 언급하나 final report 14일을 누락. |
| CRA-ARCH-MAIN-20261113-057-003 | #57 | severe incident 신고는 24h/72h 및 신고 후 1개월 final report를 갖는다. | Article 14(4) | CRA-REQ-REPORT-SEVERE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | PARTIALLY_VERIFIED | 원본의 기한 설명에 1개월 final report가 누락. |
| CRA-ARCH-MAIN-20261113-057-004 | #57 | Article 14(8)은 영향받는 사용자 및 적절한 경우 모든 사용자에게 통지하도록 한다. | Article 14(8) | CRA-REQ-USER-NOTIFY-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | VERIFIED | where appropriate 기계 판독 가능 형식 조건 포함. |
| CRA-ARCH-MAIN-20261113-057-005 | #57 | 신고 경로는 NIS2 single point of contact를 통한 Article 11 신고다. | Article 14(1), (7), Article 16 | CRA-REQ-USER-CONTACT-001; CRA-REQ-REPORT-ROUTE-001; CRA-REQ-REPORT-ACTIVE-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | Article 14/16의 지정 CSIRT·단일 신고 플랫폼과 NIS2 경로를 혼합. |
| CRA-ARCH-MAIN-20261113-057-006 | #57 | 제조사 신고 의무 조항은 Article 11이다. | Article 14 | CRA-REQ-REPORT-SCOPE-TIMELINE-001; CRA-REQ-MANUFACTURER-ARTICLE13-001 | CONFLICT | 현행 신고 조항은 Article 14. |
| CRA-ARCH-MAIN-20261113-057-007 | #57 | Article 14 신고 의무는 Class I/II 중요 제품에만 적용된다. | Article 14, Article 69(3) | CRA-REQ-TRANSITION-001; CRA-REQ-CLASSIFICATION-001; CRA-REQ-REPORT-SCOPE-TIMELINE-001 | CONFLICT | CRA 범위 제품에 적용되며 Class I/II 제한이 아니다. |

- #53–#57 파일 단위 판정은 기존 감사 결과대로 1 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED이며 direct quote reuse 0/5.
- 개별 법령 사실 VERIFIED와 원본 파일 전체 판정을 구분한다. 제품별 적용성 UNVERIFIED, DUT 시험 NOT_RUN.

## 2026-11-13 claim ID 무결성 인벤토리

- #8–#62 file-level source records: 55개, ID suffix \`-FILE-001\`; 원본 경로/blob SHA/파일 단위 판정 추적.
- #8–#62 atomic claim records: 345개, ID suffix \`-001\`, \`-002\` 등; 개별 법령 주장·인용·반증 추적.
- CRA archive ID namespace 전체: 400개 unique ID (55 file-level + 345 atomic). 중복 ID 0개를 유지해야 한다.
- Canonical requirement IDs: 46개. 345개 atomic claim의 Canonical ID 열을 정규화했으며, 하나의 claim은 여러 요구사항에 연결될 수 있다.
- 파일 단위 판정과 개별 claim 상태는 별개다. 개별 claim VERIFIED가 원본 파일 전체 VERIFIED를 의미하지 않는다.
- 제품별 적용성/Class I/II, SKU·core functionality, 실제 DUT 시험은 관련 증거가 확보되기 전까지 UNVERIFIED/NOT_RUN이다.

## 2026-11-13 Canonical Requirement Register — 정본 요구사항 ID

법령 기준: Regulation (EU) 2024/2847 consolidated 20.11.2024 및 Commission Implementing Regulation (EU) 2025/2392. 아래 Canonical ID는 원자 claim을 상위 요구사항에 연결한다. 각 원자 행의 Canonical ID 열이 crosswalk의 기준이다.

| Canonical ID | 공식 근거 | 정본 요구사항·경계 | 주요 검증 증거 |
|---|---|---|---|
| CRA-REQ-RISK-BASELINE-001 | Annex I Part I(1) | 제품의 사이버보안 수준은 위험에 기반한 적절한 수준이어야 한다. | 위험평가, threat model, 보안 요구사항 |
| CRA-REQ-SECURE-DEFAULT-001 | Annex I Part I(2)(b) | secure-by-default 설정 및 original-state reset 가능성. 특정 first-use password 방식은 별도 설계 선택. | 출하 설정, factory reset 시험, default configuration evidence |
| CRA-REQ-ACCESS-CONTROL-001 | Annex I Part I(2)(d) | 무단 접근을 막는 적절한 제어 메커니즘(인증·ID·접근관리 포함). RBAC/MFA/least privilege는 위험기반 구현 선택. | 계정·권한 모델, 인증 시험, 무단 접근 보고/감사 기록 |
| CRA-REQ-ATTACK-SURFACE-001 | Annex I Part I(2)(j) | 공격표면과 외부 인터페이스를 위험에 맞게 제한. 모든 포트/JTAG 일괄 비활성화는 보편 의무가 아님. | 인터페이스 목록, 서비스/포트 위협분석, 설정 시험 |
| CRA-REQ-INTEGRITY-001 | Annex I Part I(2)(f) | 데이터·명령·프로그램·설정의 무결성을 보호한다. | 펌웨어/설정 무결성 설계, 변조 시험 |
| CRA-REQ-AUTO-UPDATE-001 | Annex I Part I(2)(c) | 자동 보안 업데이트, 업데이트 통지 및 사용자 opt-out 등 정확한 조건을 충족한다. | 업데이트 UX, opt-out 시험, 알림 증거 |
| CRA-REQ-SECURITY-LOGGING-001 | Annex I Part I(2)(l) | 관련 내부 활동(데이터·서비스·기능 접근/변경 포함)을 기록·모니터링하고 사용자 opt-out 메커니즘 제공. | 이벤트 목록, 로그 시험, opt-out 동작, 저장공간 포화 시험 |
| CRA-REQ-SECURE-DATA-ERASURE-001 | Annex I Part I(2)(m), Annex II(8)(d) | 사용자가 모든 데이터·설정을 안전하고 쉽게 영구 제거할 수 있는 가능성과 폐기 지침 제공. 특정 NAND/EEPROM 소거 알고리즘은 지정하지 않음. | 데이터 저장 맵, 삭제 기능, 복구 가능성 시험 |
| CRA-REQ-SECURE-DATA-TRANSFER-001 | Annex I Part I(2)(m) | 해당 데이터가 다른 제품/시스템으로 전송될 수 있는 경우 그 전송을 안전하게 수행. | transfer flow, confidentiality/integrity/authenticity checks, destination verification |
| CRA-REQ-SBOM-001 | Annex I Part II(1) | 취약점 및 구성요소 식별·문서화, top-level dependencies를 포함한 machine-readable SBOM. | SBOM, component inventory, vulnerability mapping |
| CRA-REQ-REMEDIATION-001 | Annex I Part II(2) | 취약점을 위험에 비례해 지체 없이 처리·시정하고, 기술적으로 가능하면 보안 업데이트를 기능 업데이트와 분리. | PSIRT triage, remediation SLA, release separation evidence |
| CRA-REQ-SECURITY-TEST-001 | Annex I Part II(3) | 제품 보안의 효과적이고 정기적인 시험·검토. | 시험계획, 결과, 재시험 및 취약점 조치 기록 |
| CRA-REQ-VULN-DISCLOSURE-001 | Annex I Part II(4) | 수정된 취약점 정보는 보안 업데이트 제공 후 공개. 정당한 보안 위험이 있는 경우 사용자 적용 기회 후 지연 가능. | advisory, release timing, delay rationale |
| CRA-REQ-CVD-POLICY-001 | Article 13(8), Annex I Part II(5) | 내부·외부 제보 취약점 처리·시정을 위한 CVD 정책을 수립·집행. | CVD policy, intake/triage workflow, governance approval |
| CRA-REQ-CVD-CONTACT-001 | Annex I Part II(6) | 취약점 신고 연락 주소 및 취약점 정보 공유 촉진 조치 제공. PGP는 특정 법정 방식이 아님. | contact address, intake channel, response ownership |
| CRA-REQ-SECURE-UPDATE-DIST-001 | Annex I Part II(7) | 취약점 시정·완화를 위한 안전한 업데이트 배포 메커니즘 제공. A/B, dual-bank, rollback은 설계 선택. | 서명/검증, update transport, interruption/failure test |
| CRA-REQ-FREE-UPDATE-001 | Annex I Part II(8) | 보안 업데이트는 지체 없이 배포하고 원칙적으로 무상 제공. 맞춤형 제품에 관해 제조자와 사업 사용자가 달리 합의한 경우 예외. | update policy, 계약 예외 검토, release/advisory evidence |
| CRA-REQ-SUPPORT-PERIOD-001 | Article 13(8) | support period는 expected use를 반영하고 원칙적으로 최소 5년. expected use가 5년 미만이면 그 기간에 대응. | expected-use rationale, support-period decision record |
| CRA-REQ-UPDATE-AVAILABILITY-001 | Article 13(9) | 각 보안 업데이트는 발행 후 최소 10년 또는 남은 support period 중 더 긴 기간 동안 이용 가능. | release archive, download availability, version retention |
| CRA-REQ-COMPONENT-DUE-001 | Article 13(5)–(7) | 제3자 구성요소 due diligence, 식별된 취약점의 구성요소 제조자/유지관리 주체 보고, 필요한 코드/문서 공유 및 기록. | supplier/component inventory, notification records, technical documentation |
| CRA-REQ-USER-CONTACT-001 | Article 13(17) | 사용자가 쉽게 식별하고 직접·신속하게 소통할 단일 연락 창구. 선호 통신수단 선택 가능, 자동화 도구만으로 제한 금지. | user manual/contact point, response process, human contact route |
| CRA-REQ-USER-INFO-RETENTION-001 | Article 13(18), Annex II | Annex II 사용자 정보/지침을 최소 10년 또는 support period 중 더 긴 기간 제공 가능하게 유지. | controlled manual, version archive, publication evidence |
| CRA-REQ-SUPPORT-END-001 | Article 13(19), Annex II(7) | support period 종료일을 구매 시 명확히 표시하고 기술적으로 가능한 경우 종료 알림 제공. | product page/label/manual, EOL notice process |
| CRA-REQ-USER-INSTRUCTIONS-001 | Annex II(1)–(8) | 안전한 설치·운영·유지관리, 연락 창구, 업데이트, 지원기간, 폐기·데이터 삭제 등 사용자 정보 제공. | Korean user manual, installation/maintenance/disposal instructions |
| CRA-REQ-REPORT-ACTIVE-001 | Article 14(1)–(2) | actively exploited vulnerability 인지 시 24h early warning, 72h vulnerability notification, 조치 이용 후 14일 final report. | incident clock, CSIRT submission, final report evidence |
| CRA-REQ-REPORT-SEVERE-001 | Article 14(3)–(4) | 제품 보안에 영향을 미치는 severe incident는 24h/72h 및 신고 후 1개월 final report. | severity assessment, incident report, final report |
| CRA-REQ-REPORT-ROUTE-001 | Article 14(7) | 지정 CSIRT 전자 신고 엔드포인트/단일 플랫폼 사용, ENISA에 동시에 접근 가능. | submission platform receipt, CSIRT endpoint, ENISA access |
| CRA-REQ-REPORT-SCOPE-TIMELINE-001 | Article 14(1)–(7) | 일반 취약점 CVD와 법정 신고 trigger/기한을 구분. 모든 발견 취약점이 Article 14 신고 대상은 아님. | trigger decision tree, 24h/72h/14d/1m clock records |
| CRA-REQ-USER-NOTIFY-001 | Article 14(8) | active exploited vulnerability/severe incident의 영향 사용자 및 적절한 경우 모든 사용자 통지. machine-readable 형식은 where appropriate. | customer impact list, advisory, notification evidence |
| CRA-REQ-CLASSIFICATION-001 | Article 7, Annex III, Implementing Regulation 2025/2392 | Class I/II는 제품 core functionality와 technical description으로 판단. 내장 인터페이스만으로 host product 자동 분류 금지. | product boundary, intended purpose, category assessment |
| CRA-REQ-CONFORMITY-001 | Article 32, Annex VIII | 해당 Class에 맞는 Module A/B+C/H 등 절차와 조건 적용. Module C=internal production control, H=full quality assurance. | conformity assessment plan, Notified Body decision, certificates |
| CRA-REQ-TECHDOC-001 | Article 31, Annex VII | 기술문서 작성·유지 및 support period 산정 근거 포함. | technical file, risk assessment, test evidence |
| CRA-REQ-DOC-001 | Article 28, Annex V/VI | EU Declaration of Conformity 작성 및 필요한 정보 포함. | signed DoC, product/model traceability |
| CRA-REQ-CE-001 | Article 30 | CE marking 요건 준수. | marking artwork, label/photo evidence |
| CRA-REQ-PENALTY-001 | Article 64(2)–(3) | 위반 유형별 penalty tier를 구분. Annex I/Article 13/14와 Article 32(1)–(3)의 금액·비율이 다름. | legal obligation mapping, compliance decision record |
| CRA-REQ-TRANSITION-001 | Article 69(3) | 2027-12-11 이전 출시 제품에도 Article 14 신고 의무 적용. | placing-on-market date evidence, incident procedure |
| CRA-REQ-MANUFACTURER-ARTICLE13-001 | Article 13 | 제조사 의무의 정확한 본문 조항. Article 11은 General product safety로 인용하지 않음. | article-to-requirement crosswalk, legal review |
| CRA-REQ-VULNERABILITY-HANDLING-001 | Annex I Part II | Part II는 vulnerability handling requirements. Part I 제품 속성 요구와 혼동하지 않음. | legal clause map, vulnerability process traceability |
| CRA-EVIDENCE-QUOTE-ACCURACY-001 | Evidence governance rule | 직접 인용은 최종 consolidated text의 정확한 문언·조항·버전과 일치해야 한다. 요약/합성문은 paraphrase로 표시. | exact quote locator, source version, reviewer sign-off |

**매핑 원칙:** 원자 claim의 Canonical ID 열은 하나 이상의 상위 요구사항을 가리킨다. 파일 단위 판정은 별도 유지하며, Canonical ID는 제품 적합성 PASS를 뜻하지 않는다. 제품별 적용성·시험 상태는 각 evidence record에서 따로 관리한다.

## 2026-11-13 main archive file-level source records — #58–#62

Batch direct quote reuse: **0/5**. Per-file quote counts are not inferred where the audit only reports a batch total.

| File Record ID | Report | main source path | main blob SHA | File-level status | Batch quote result | Audit |
|---|---:|---|---|---|---:|---|
| CRA-ARCH-MAIN-20261113-058-FILE-001 | #58 | research_archive/2026-11-13_044541.md | a5d535859eee483d47abb4dbf809cb10fdd3b8ce | PARTIALLY_VERIFIED | See batch result below | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md |
| CRA-ARCH-MAIN-20261113-059-FILE-001 | #59 | research_archive/2026-11-13_045038.md | 798aadd8105d1b44a03823f0f058e2e5c5fdae04 | PARTIALLY_VERIFIED | See batch result below | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md |
| CRA-ARCH-MAIN-20261113-060-FILE-001 | #60 | research_archive/2026-11-13_045534.md | 412a5cb249e0f198f7c024cf1a6736c9d2d932be | PARTIALLY_VERIFIED | See batch result below | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md |
| CRA-ARCH-MAIN-20261113-061-FILE-001 | #61 | research_archive/2026-11-13_050052.md | 6d3149dfd83b1862bc2388b6ee15d376d53a4e8e | PARTIALLY_VERIFIED | See batch result below | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md |
| CRA-ARCH-MAIN-20261113-062-FILE-001 | #62 | research_archive/2026-11-13_050532.md | 5a280db701cf970c32ef85d97010e0dd1dbd7fa0 | PARTIALLY_VERIFIED | See batch result below | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md |

