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


| TI-008 | TI의 MSPM0G3506 제품 기술자료 목록에는 *Cybersecurity Enablers in MSPM0 MCUs* Rev B, 2026-08-27이 표시된다. | technical_fact | TI MSPM0G3506 official technical-document index / https://www.ti.com/product/MSPM0G3506, Technical documentation list | Rev B의 존재와 날짜는 목록에서 확인. Rev B 본문을 직접 확인하지 않았고 MSPM0G3529-Q1에 대한 직접 적용성도 미확인. | PARTIALLY_VERIFIED |


## 7. TI G-Series 최신 문서 확인 추가 레코드 (2026-11-12)

| Claim ID | 원자적 주장 | 유형 | 출처 및 정확한 위치 | 검증 범위 / 판정 | 상태 |
|---|---|---|---|---|---|
| TI-009 | TI MSPM0G3529-Q1 제품 페이지는 전체 모듈 설명을 위해 MSPM0 G-Series 80MHz Technical Reference Manual을 참조하도록 안내한다. | technical_fact | TI MSPM0G3529-Q1 product page, description / https://www.ti.com/product/MSPM0G3529-Q1 | 제품 페이지의 문서 참조 문구 확인. 해당 TRM 내 특정 보안 레지스터/기능의 부품 적용성은 별도 확인 필요. | VERIFIED |
| TI-010 | TI MSPM0-DIAGNOSTIC-LIB 공식 기술자료 인덱스는 MSPM0 G-Series 80-MHz Technical Reference Manual Rev F, 2026-11-05를 표시한다. | technical_fact | TI MSPM0-DIAGNOSTIC-LIB page, Technical documentation table / https://www.ti.com/tool/MSPM0-DIAGNOSTIC-LIB | 인덱스에 문서명·Rev F·날짜가 표시됨. PDF/HTML 본문을 가져오지 못했으므로 Rev F의 내용은 검증하지 않음. | VERIFIED (index metadata only) |
| TI-011 | SLAAE29 Rev B 본문이 현재 TI 공식 링크에서 확인되었다. | technical_fact | 이전 세션의 index 탐색 메모; 이번 세션에서 직접 PDF/문서 페이지 재현 실패 | 최신판 Rev B의 존재 및 본문은 이번 세션의 재검증을 통과하지 못함. 기존 Rev A 분석을 유지하고 Rev B는 확보 전까지 인용 금지. | UNVERIFIED |

**TI-008 처리 메모:** 과거 Rev B 날짜/인덱스 확인 기록은 보존하되, 이번 재점검에서 공식 원문을 재현하지 못했으므로 Rev B 내용의 근거로 사용하지 않는다. Rev B 본문을 실제 확보한 뒤 별도 revision 레코드로 갱신한다.
