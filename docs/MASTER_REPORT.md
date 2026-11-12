# 사이버 복원력 법(CRA) 대응을 위한 서보 드라이브 개발 실무 가이드

**문서 상태:** 초안 골격  
**기준일:** 2026-11-12  
**대상 독자:** CRA를 처음 접하는 서보 드라이브 하드웨어·펌웨어·시스템·품질 개발자  
**범위:** 공개된 법령·표준·제조사 기술자료를 바탕으로 한 일반 개발 가이드  
**주의:** 본 문서는 제품별 법적 적합성 판정이나 인증을 대체하지 않는다. 각 내용은 출처 검증 및 제품 조건 확인 후 확정한다.

## 문서 사용법
각 장은 다음 순서로 설명한다.
1. 쉬운 설명
2. CRA 요구사항 및 공식 원문
3. 서보 드라이브와의 관련성
4. 하드웨어·펌웨어·시스템 설계 조치
5. 시험 및 객관적 증거
6. ST 구현 참고 및 TI 비교
7. 검증 상태, 미해결 쟁점, 출처

## 목차
1. CRA 개요 — 개발자가 알아야 하는 이유
2. 제품 적용 범위와 제품 분류 판단 절차
3. CRA 요구사항을 개발 업무로 번역하기
4. 서보 드라이브 시스템 경계와 위협 모델
5. 하드웨어 보안 설계
6. ST MCU 기반 보안 구현 가이드
7. TI 반도체 기술 비교 및 참고 설계
8. 펌웨어·통신·업데이트 보안
9. 취약점 처리, 보안 업데이트 및 지원 기간 관리
10. SBOM, 위험평가, 기술문서 및 증거 관리
11. 개발 단계별 시험 계획과 체크리스트
12. 출시 전 검토 및 유지보수 프로세스
13. 요구사항-설계-시험 추적성 매트릭스
14. 용어집 및 참고자료

## 1. CRA 개요
CRA는 EU 시장에 제공되는 디지털 요소 제품에 대한 수평적 사이버보안 규정이다. 공식 원문을 대조한 현재 기준선은 [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md)에 정리했다.

기존 990개 자동 조사 아카이브에서 주장 후보 4,400개 문단을 추출했지만 URL 후보는 0개였다. 따라서 기존 보고서들은 출처의 문서명만으로는 검증이 불충분할 수 있다. 각 주장에 EUR-Lex/Commission/제조사 공식 원문 링크, 조항/섹션 위치, 버전/개정일, 원문 대조 결과를 추가해야 한다. 전체 후보는 [archive_claim_evidence_candidates.json](../reports/archive_claim_evidence_candidates.json)에 저장.

2026-11-12 기준 Article 14 제조자 신고 의무는 2026-09-11부터 적용 중이며, 규정의 일반 적용일은 2027-12-11이다. 신고 대상은 모든 취약점이 아니라 제품 내 actively exploited vulnerability와 제품 보안에 영향을 주는 severe incident다. 구체적인 24시간·72시간·최종 보고 시한은 사건 유형별로 구분해야 한다.

Annex I Part II의 핵심 취약점 처리 의무에는 SBOM, 지체 없는 취약점 조치, 정기 보안시험, 조정된 취약점 공개 정책, 안전한 업데이트 배포, 보안 업데이트의 원칙적 무상 제공 등이 포함된다.

완제품 서보 드라이브가 Important Class I/II에 해당하는지, ST MCU가 Class I category 14에 해당하는지는 서로 별개로 판단해야 한다. 제품명이나 MCU 제조사만으로 등급을 단정하지 않는다.

근거: [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847), [Implementing Regulation (EU) 2025/2392](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392), [European Commission reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting).

## 2. 제품 적용 범위와 제품 분류 판단
제품별 사실을 기록할 입력 시트는 [SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md)에 작성했다. Article 2/3의 디지털 요소 제품 및 연결성 정의, Article 7과 Implementing Regulation (EU) 2025/2392의 core-functionality 기준을 사용한다. 드라이브 본체, 내장 펌웨어, 별도 옵션 모듈, PC 툴, 앱, 원격 데이터 처리 서비스, 센서/엔코더, 상위 시스템의 경계를 구분한다.

현재 제품 SKU, EU 판매 형태, 정확한 연결 인터페이스, 원격 데이터 처리의 기능 필수성, ST MCU 주문 코드가 확인되지 않았으므로 CRA 적용성과 Important Class I/II 판단은 UNVERIFIED로 유지한다. 서보 드라이브라는 명칭만으로 적용 여부나 분류를 단정하지 않는다.

판단에 필요한 최소 입력은 제품의 시장/판매 형태, 단독/시스템 통합 형태, 네트워크 연결/원격 처리 여부, 의도된 목적, 소프트웨어/펌웨어 기능, 업데이트 경로, 제품 경계 및 Annex III/IV 목록의 정확한 분류 문구다. 제조사·MCU가 아니라 완제품의 기능과 법령상 정의를 기준으로 판단한다.

## 3. CRA 요구사항을 개발 업무로 번역하기

첫 번째 공식 근거 매핑은 [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md)에 정리했다. 주요 개발 작업은 제품 위험평가(Article 13(2)–(4)), 제3자 구성요소 due diligence(13(5)–(7)), 지원기간/취약점 처리(13(8)), SBOM(Annex I Part II(1)), 보안 업데이트 분리(Part II(2), 기술적으로 가능한 경우), CVD(Part II(5)), 안전한 업데이트 배포(Part II(7)), 원칙적 무상 업데이트(Part II(8)), Article 14 신고 절차다.

## 4. 서보 드라이브 시스템 경계와 위협 모델
작성 상태: 전원부, 제어부, MCU, 통신 인터페이스, 엔코더/센서, 서비스 포트, 부트로더, 업데이트 경로 등을 제품 조건에 따라 식별한다.

## 5. 하드웨어 보안 설계
작성 상태: 부품 선정, 디버그 포트, 키 저장, 물리적 접근, 보안 부팅 기반, 보안 경계 등을 검토한다.

## 6. ST MCU 기반 보안 구현 가이드

ST 공식 기준선은 AN5156 Rev 14 (June 2026)와 STM32Trust로 시작한다. AN5156은 보안 기능의 개요/제품군 매트릭스를 제공하지만 모든 기능이 모든 STM32에 공통 제공되는 것은 아니다. 정확한 부품번호, 실리콘 리비전, 메모리 구성, Option Bytes 및 제품 상태를 확인한 뒤 Secure Boot/SFU/SFI, TrustZone, 디버그 인증/잠금, 키 저장, TRNG, 암호 가속, 메모리 보호의 적용성을 판단한다.

근거: [ST AN5156](https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html), [STM32Trust](https://www.st.com/content/st_com/en/ecosystems/stm32trust.html).

## 7. TI 반도체 기술 비교

TI 공식 비교 기준 예시로 MSPM0G3529-Q1 데이터시트(SLASFO2B, revised October 2025)와 SLAAE29A Cybersecurity Enablers in MSPM0 MCUs(revised December 2025)를 확보했다. 이 예시 부품은 80 MHz Cortex-M0+, 최대 512 KB ECC Flash, 128 KB SRAM, dual-bank flash/address swap, AES-128/256 가속, secure key storage, flash firewalls, TRNG, secure boot 및 secure in-field update 기능을 데이터시트에 명시한다.

이 정보는 기능 비교의 출발점이지 ST와의 동급 성능/비용/보안 동등성 판정이 아니다. ST의 정확한 주문 코드와 TI 비교 대상 주문 코드를 먼저 확정한 뒤 동일한 조건과 문서 리비전으로 비교한다.

공식 자료: [TI MSPM0G3529-Q1 datasheet](https://www.ti.com/lit/ds/symlink/mspm0g3529-q1.pdf), [TI SLAAE29A](https://www.ti.com/lit/an/slaae29a/slaae29a.pdf).

## 8–12. 개발·운영·시험·문서화
작성 상태: CRA 원문 및 관련 표준/공식 가이드 검증 후 구체화한다.

## 13. 추적성 매트릭스
| 요구사항 ID | 공식 조항 | 개발 조치 | 담당 영역 | 시험/검증 | 증거 파일 | 상태 |
|---|---|---|---|---|---|---|
| 추후 부여 | 원문 확인 후 기입 | 추후 작성 | HW/FW/SW/QA | 추후 작성 | 추후 작성 | UNVERIFIED |

## 14. 용어집 및 참고자료
검증된 공식 자료만 확정 참고문헌에 등록한다. 출처별 확인일과 버전을 함께 기록한다.

## 기존 조사 아카이브 품질 감사
- 990개 전체 후보 추출 결과: 4,400개 주장 문단, 1,224개 Article 후보, URL 문자열 후보 0개. 자동 추출은 법적 검증이 아니다.
- 수동 표본 누계 34개 파일: 25건 CONFLICT, 9건 PARTIALLY_VERIFIED. 무작위 표본이 아니므로 990개 전체 오류율로 일반화하지 않는다.
- 반복 오류: Article 10/11/14 혼동, Article 24/32 혼동, 지원기간과 무상 업데이트 조항 혼동, 24h/72h 신고 범위 과장, 서보 드라이브 Class I 자동 단정.
- 상세: [초기 5개 감사](ARCHIVE_MANUAL_SAMPLE_AUDIT_5_2026-11-12.md), [추가 9개 감사](ARCHIVE_MANUAL_AUDIT_9_2026-11-12.md).

## 미해결 사항
- ST MCU의 정확한 부품 번호/제품군 미확정
- 대상 서보 드라이브의 기능 및 인터페이스 범위 미확정
- 기존 아카이브의 전체 주장·출처 검증 미완료
- 법령/표준의 최신 적용 상태 검증 필요

## 문서 변경 이력
- 2026-11-12: 통합 보고서 기본 구조 생성. 검증 전 내용을 확정 사실로 쓰지 않도록 상태를 명시.


## 기존 조사 아카이브 품질 감사 — 추가 20개 표본 (2026-11-12)

2026-11-11~2026-11-12 생성된 지원기간, 무상 업데이트, 적합성 평가, 제품 분류, 업데이트 무결성, SBOM, CVD 관련 문서 20개를 EUR-Lex 법령 원문과 대조했다. 14개는 조항·인용·의무 범위가 원문과 충돌(CONFLICT), 6개는 일부 취지는 맞지만 근거 위치/직접 인용/구현 의무 범위가 부정확(PARTIALLY_VERIFIED)했다. 초기 5개와 추가 9개를 합산한 34개 비무작위 표본은 25 CONFLICT, 9 PARTIALLY_VERIFIED다. 이 수치는 위험 기반 표본 결과이며 전체 990개 오류율로 해석할 수 없다.

반복된 오류를 바로잡는 기준은 다음과 같다.
- 제조자 의무 및 지원기간은 Article 13(8). 최소 5년 원칙이지만 예상 사용기간이 5년 미만이면 그 예상 사용기간을 적용한다. 지원기간 종료일 고지는 Article 13(19) 및 Annex II(7)와 연결한다.
- SBOM은 Annex I Part II(1), 기술적으로 가능한 경우 보안 업데이트와 기능 업데이트 분리는 Part II(2), CVD는 Part II(5)–(6), 안전한 업데이트 배포는 Part II(7), 무상 보안 업데이트는 Part II(8).
- 제품 속성 보안은 Annex I Part I(2)(b)/(d)/(f)/(j)로 구분한다. 특정 Root CA, TLS 버전, dual-bank 구조 등은 위험 기반 설계 예시이지 법령이 일률적으로 특정한 구현으로 단정하지 않는다.
- 제조자 신고는 Article 14이며 actively exploited vulnerability와 severe incident를 구분한다. 모든 취약점 발견을 24/72시간 신고 대상으로 일반화하지 않는다.
- Article 24는 open-source software stewards, Article 31은 기술문서, Article 32는 제품 적합성 평가 절차다.
- Important Class I/II는 Article 7 및 Annex III의 core functionality 기준으로 판단한다. 일반적인 산업용 서보 드라이브/산업 자동화 시스템이 Annex III에 독립 카테고리로 열거되어 있다고 인용하면 안 된다.

파일별 판정·SHA·정정 근거는 [추가 20개 수동 감사](ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md)를 참조한다. 원본 아카이브는 보존했으며, 이 감사만으로 제품별 법적 적용성이나 CRA 적합성을 확정하지 않는다.


## 제조사 MCU 보안 기능 근거 및 비교 (2026-11-12)

제조사 1차 자료를 기능별로 분리해 등록했다. ST는 AN5156 Rev14 (June 2026)를 중심으로 STM32 제품군의 RDP/product state, memory protection, debug protection, secure boot/SFU, SFI, cryptography/TRNG 및 제품군별 기능 차이를 확인했다. ST 문서 자체가 제품별 Reference Manual 확인을 요구하므로 실제 MCU 주문 코드가 확보되기 전까지 특정 ST 부품의 기능은 확정하지 않는다.

TI 비교 예시로 MSPM0G3529-Q1 데이터시트 SLASFO2B RevB (October 2025)를 확인했다. 해당 부품의 데이터시트 §8.18–8.21은 debug security, AES-128/256 및 여러 mode, code/data firewalls, secure boot/update, up to four AES keys, CSC, hardware monotonic counter, TRNG를 명시한다. Flash 512KB, SRAM 128KB, dual-bank/address swap도 기재한다. TI SLAAE29A RevA (December 2025)는 MSPM0 플랫폼의 CSC boot flow 및 secure storage 개념을 상세 설명한다.

주의: TI 공식 제품 기술자료 인덱스에는 SLAAE29 RevB (2026-08-27)와 G-Series TRM RevF (2026-11-05)가 표시되어 최신판 본문 확인이 추가로 필요하다. 이번 문서의 SLAAE29A 분석은 RevA에 한정한다. TI 데이터시트의 PSA Level 1 “targeted”는 인증 취득 완료가 아니다. Q1/ASIL 관련 표현은 CRA 적합성 증거와 다르다.

기능별 표, source metadata, 제품 적용 한계 및 추가 시험 큐는 [제조사 보안 자료 레지스터](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md)를 참조한다. 개별 기술 주장과 원문 위치/상태는 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 등록했다. 현재 제조사 주장 15건(문서/인덱스 수준 VERIFIED 13건, PARTIALLY_VERIFIED 1건, UNVERIFIED 1건)을 등록했으며, 이 레코드는 MCU 기능 사실의 출처 검증이지 서보 드라이브 전체의 CRA 적합성 판정이 아니다.


## 추가 장 — 서보 드라이브 보안 하드웨어 참조 아키텍처 (초안)

[서보 드라이브 CRA 보안 하드웨어 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md)에 외부 통신·서비스 인터페이스, 통신 도메인, 모션 제어 MCU, NVM, 선택적 secure element, 디버그 포트, 제조 프로비저닝 및 전원/리셋 감독 블록을 정리했다. Trust boundary와 secure boot/update, 키 관리, 생산 프로비저닝, 업데이트 부정시험, CRA 요구사항-설계-증거 연결을 포함한다.

이 아키텍처는 개발자 토론용 참조 설계다. 특정 MCU/secure element/암호 알고리즘을 CRA가 직접 요구한다는 뜻이 아니며, 실제 회로도·제품 SKU·ST MCU 주문 코드가 확인되기 전까지 제품별 적용성은 UNVERIFIED다. STO 등 기능안전 경로는 별도 안전 분석의 대상이며 CRA 요구사항과 혼동하지 않는다.

### TI 최신 문서 재점검 결과
TI MSPM0G3529-Q1 제품 페이지는 MSPM0 G-Series TRM을 참조한다. TI MSPM0-DIAGNOSTIC-LIB 기술자료 인덱스는 G-Series TRM Rev F(2026-11-05)를 표시한다. 다만 전체 PDF/HTML 본문은 도구의 크기 제한으로 열람하지 못했으므로 Rev F의 보안 장 내용을 검증했다고 주장하지 않는다. SLAAE29 Rev B도 이번 세션에서 공식 본문을 재확보하지 못했으며, 기존 SLAAE29A Rev A만 본문 확인된 자료로 유지한다.


## 6. 기존 조사 아카이브 표본 정정 추적

기존 자동 생성 자료의 표본 감사 결과는 [ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md)에 원본 파일 경로, SHA-1 blob, 원문 행 위치, 핵심 주장, 법령 정정 룰, 판정 상태로 연결했다. 35개 감사 ID 중 A-013/B-006이 동일 원본 파일이므로 고유 파일은 34개이며, 고유 파일 기준 25 CONFLICT / 9 PARTIALLY_VERIFIED다. 표본은 비무작위이므로 990개 전체 오류율로 일반화하지 않는다. 원본 archive는 변경하지 않았다.


## 부록 — 기존 조사 archive 인용 신뢰성 감사 (2026-11-12)
기존 CRA 조사 archive 중 위험 기반으로 선정한 34개 고유 파일을 EUR-Lex Regulation (EU) 2024/2847과 대조했다. 감사 ID 35행 중 A-013/B-006은 동일 파일이어서 중복을 제거했다. 파일별 인용 위치, 원문 일치 여부, 잘못 연결된 조항 및 정정 위치는 [ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md](ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md)에 기록했다.

이 표본에서는 직접 인용처럼 표시된 합성 문구, 요약의 인용 오표시, Article/Annex 위치 오류가 반복적으로 확인되었다. 지원기간은 Article 13(8), 업데이트의 최소 이용 가능 기간은 Article 13(9), 업데이트 취약점 처리 및 기능 업데이트와의 분리는 Annex I Part II(2), 무상 제공은 Part II(8), 법정 신고는 Article 14다. 제품 분류는 Article 7 및 Annex III의 core functionality 기준이며, 기술문서는 Article 31/Annex VII, 적합성 평가는 Article 32다.

본 표본 결과는 전체 990개 archive의 오류율 추정치가 아니다. 원본 archive는 변경하지 않았으며, 보고서 본문에서 검증되지 않은 인용을 그대로 재사용하지 않는다. 이 감사는 법률 자문 또는 제품별 CRA 적합성 판정을 대체하지 않는다.


## 검증 방법과 결과 신뢰도 관리
프로젝트 조사 결과의 신뢰도와 완료 기준은 [검증 운영 프로토콜](VERIFICATION_PROTOCOL.md)을 따른다. 핵심 주장은 공식 원문, 문서 버전, 정확한 위치를 연결하고 최초 조사와 구분되는 별도 재검증 및 반증 확인을 거친다. 같은 AI에게 동일 질문을 반복하는 것은 독립 검증이 아니다. 법령 원문이 유일한 권위 출처인 경우에는 조항 문맥과 예외를 별도 재확인하며, 독립된 두 출처가 있다고 과장하지 않는다.

기존 34개 표본 인용 감사는 EUR-Lex 원문 대조 기록으로 유지하되, 신규 프로토콜의 Pass A/B/C 필드를 모두 충족한 재감사 완료로 간주하지 않는다. 제품별 적용성은 SKU, 시장 제공 형태, 연결성, MCU 주문 코드 등이 확인되기 전까지 UNVERIFIED로 유지한다.


## 인용 신뢰성 — 별도 Pass B/C 재검증 진행
기존 34개 표본 인용 감사와 구분하여, A-001–A-008에 대해 EUR-Lex 현행 원문을 다시 열어 조항·문맥·예외를 재확인하고 반대 근거를 점검했다. 상세 결과는 [Pass B/C Batch 01](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)에 기록했다.

이 배치에서 Article 13(8) 지원기간, Annex I Part II(8) 무상 업데이트, Part II(2) 업데이트 분리, Part I(2)(c) 자동 업데이트, Article 14 신고를 명확히 분리했다. 8개 파일 중 인용 블록 전체가 VERIFIED된 파일은 없다. 일부 정확한 인용과 잘못된 조항 연결이 한 파일에 함께 존재하므로 주장/인용 단위로 관리한다. 이 Pass B/C는 동일 AI 세션 내 별도 재확인 절차이며 독립 제3자 검토가 아니다.


## Pass B/C 재검증 Batch 02 — A-009–A-015, B-001–B-002
- EUR-Lex 현행 CRA 원문을 다시 열어 Article 13(8)–(9), Article 14, Annex I Part I/II를 재대조하고 반대 근거·예외를 확인.
- 신규 문서 docs/ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md 생성.
- 8개 파일 모두 Raw Text Quote를 현행 CRA 직접 인용으로 재사용할 수 없다고 판정. 지원기간 shorter/longer 역전, Article 14 신고 범위 과장, Part I/II 혼동, draft 조항 번호 사용이 반복됨.
- Batch 01+02 합계 16/34개 파일 재검증. 독립 제3자 검토가 아니라 동일 AI 세션의 별도 재검증이며, 이 수치를 34개 전체 검증 완료로 표현하지 않음.


## 인용 신뢰성 — Pass B/C Batch 03
B-003–B-010 8개 파일을 EUR-Lex 원문으로 재검증했다. B-009의 secure-by-default 문구는 Annex I Part I(2)(b)와 취지가 일치하지만 조항 위치 및 “original state” 표현을 바로잡아야 한다. B-010의 Class II 절차는 Article 32(3)이며, Article 24로 잘못 인용했고 Annex III Class II 분류 근거 없이 서보 드라이브를 Class II로 단정했다. 기술문서 Article 31, 적합성 평가 Article 32, DoC Article 28, CE 원칙 Article 29와 부착 규칙 Article 30을 분리한다. 상세: [Batch 03](ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md).

Pass B/C 합계 24/34개 파일 진행, 10개 남음. 동일 AI 세션의 별도 재검증 절차이며 독립 제3자 법률 검토는 아니다.


## Pass B/C 최종 검증 결과 반영
기존 위험 기반 표본 34개 고유 원본을 EUR-Lex 현행 CRA 원문으로 별도 재대조했다. 파일 단위 결과는 VERIFIED 0, PARTIALLY_VERIFIED 6, REJECTED 28이다. 이 수치는 34개 표본에 한정되며 990개 전체 오류율이 아니다. 지원기간 Article 13(8), 업데이트 보존 Article 13(9), 신고 Article 14, 업데이트 처리/분리/무상 제공 Annex I Part II(2)/(8), 기술문서 Article 31, 적합성 평가 Article 32, DoC Article 28, CE 원칙/부착 Article 29/30을 구분한다. 상세: [ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md](ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md).


## CRA 요구사항 → HW/FW/시험/증거 추적성
검증된 법령 요구를 개발자가 실행할 수 있도록 [CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md)를 작성했다. Annex I Part I의 제품 보안 속성, Part II의 취약점 처리, Articles 13–14의 제조자 의무/신고를 하드웨어 블록, 펌웨어/운영 통제, 시험 제안, 객관적 증거 후보에 연결했다. 이 문서는 일반 참조 설계 초안이며, 제품 SKU·실제 MCU 주문 코드·통신/원격 기능·안전 아키텍처가 확인되기 전에는 제품별 적용성과 시험 합격 기준을 확정하지 않는다.


## 위협 모델과 시험·증거 체계 (초안)
일반 참조 모델로 [서보 드라이브 CRA 위협 모델](THREAT_MODEL_SERVO_DRIVE_CRA.md)을 추가했다. 보호 자산(AST), 공격자(ACT), 신뢰 경계(TB), 위협 시나리오(TH)를 식별하고 HW/FW/통신/생산/운영 통제 후보에 연결했다. 제품별 사실이 없는 상태에서 위험도 점수나 적용성을 임의로 확정하지 않았다.

[보안 시험·증거 대장](SECURITY_TEST_EVIDENCE_REGISTER.md)은 각 위협을 TST-* 시험 ID와 EV-* 증거 ID로 연결한다. 시험은 모두 NOT_RUN이며, 제품 제어주기·지터·부하·복구시간 등 수치형 합격 기준은 승인된 제품 요구사항/위험평가/기능안전 분석을 입력받아 확정해야 한다. 시험 PASS는 CRA 적합성 결론과 동일하지 않다.


## 통합 요구사항–위협–설계–시험–증거 추적성
[CRA_INTEGRATED_TRACEABILITY_MATRIX.md](CRA_INTEGRATED_TRACEABILITY_MATRIX.md)는 법령 요구사항을 자산·위협·HW/FW 통제 후보·시험 ID·증거 ID까지 연결하는 통합 추적표다. TR-01..TR-20은 Annex I Part I/II, Articles 7, 13, 14 및 관련 제품 분류 검토를 포함한다. 제품별 적용성은 아직 UNVERIFIED이며 시험은 NOT_RUN이다.

## European Commission 2026 CRA guidance
Commission은 2026-07-27 C(2026) 5252 CRA 실무 가이드를 공식 게시했다. 주요 주제는 scope/remote data processing/FOSS, substantial modification, support periods, reporting, risk assessment이며 67개 예시 등을 포함한다. 가이드는 비구속적이므로 Regulation (EU) 2024/2847 원문을 대체하지 않는다. 공식 게시 사실은 확인했으나 Annex의 개별 페이지/문단은 아직 직접 검증하지 않았다. 상세 검토: [CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md](CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md).

## 제조사 문서 최신 revision 메타데이터
ST AN5156 Rev14/June 2026, TI SLAAE29 Rev B/August 2026, TI MSPM0 G-Series TRM Rev F/November 2026의 공식 페이지/인덱스 표시를 확인했다. TI Rev B 및 TRM Rev F 본문은 확보/검증되지 않았으므로 기능 상세를 근거로 인용하지 않는다. 실제 ST MCU part number가 없는 상태에서 제품별 기능을 확정하지 않는다.

## CRA 법령 인용 품질 감사 — main-only report #35

main 브랜치의 자동 생성 report #35는 Secure Boot, 하드웨어 Root of Trust, TPM/Secure Element 및 디지털 서명 기반 업데이트 검증을 CRA가 모든 서보 드라이브에 직접 요구한다고 단정한다. EUR-Lex Regulation (EU) 2024/2847 Annex I는 위험평가 기반의 기술 중립적 보안 결과를 규정하며, 특정 Secure Boot chain/TPM/SE를 일률적 부품 의무로 명시하지 않는다. 이들은 위험에 맞는 설계 통제 후보로 구분해야 한다.

해당 보고서의 “Raw Text Quote”는 Annex I Part I(2)(b)–(d)의 번호와 문구가 일치하지 않는다. 실제 (b)는 secure-by-default, (c)는 취약점을 보안 업데이트로 해결할 수 있는 속성, (d)는 비인가 접근 통제다. 원본 인용은 무결성·가용성·secure update 문장을 잘못된 항목에 배정한 합성 인용으로 판정했다. 파일 단위 CONFLICT, 인용 블록 REJECTED.

상세 판정 및 권장 정정 문안: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md). main 원본 파일은 보존했으며 수정하지 않았다.

### TI SLAAE29 Rev B 직접 확인

TI 공식 HTML 문서 뷰어에서 SLAAE29B 본문과 §9 Revision History를 확인했다. Rev B는 CSC secure boot 예제, KEYSTORE, AESADV 및 일부 MSPM0 디바이스의 TRNG를 설명한다. 다만 문서의 지원 부품 목록에는 MSPM0G3529-Q1이 없으므로, 이 Rev B 설명을 해당 Q1 부품의 직접 기능 증거로 사용하지 않는다. 정확한 부품의 데이터시트 및 적용 가능한 TRM/errata가 우선이다.

## main-only report #36 법령 인용 감사

main의 자동 생성 report #36은 Secure Boot/Measured Boot/TPM을 CRA의 보편적 하드웨어 의무로 단정하고, Annex I Part I(2)(b),(c),(g)의 항목을 잘못 인용했다. 또한 Article 14(actively exploited vulnerability 및 severe incident 신고)를 무상 보안 업데이트 의무와 혼동했다. 무상 보안 업데이트는 Annex I Part II(8), 지원기간은 Article 13(8)로 구분해야 한다. 보고서의 CRA 정식 제목에 적힌 개정 법령 번호도 EUR-Lex 원문과 일치하지 않는다.

파일 판정은 CONFLICT, 직접 인용 블록은 REJECTED다. 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md). main 원본은 수정하지 않았다.

## 하드웨어 아키텍처 법령 매핑 품질 수정

재검토에서 아키텍처 문서의 CRA-HW-05/06 매핑 오류를 발견해 수정했다. Annex I Part I(2)(e)는 기밀성, (f)는 무결성, (g)는 데이터 최소화, (h)는 필수 기능 가용성/DoS 회복력, (i)는 연결된 기기·네트워크의 가용성 영향 최소화다. 아키텍처 표는 이를 분리해 CRA-HW-05/06/11에 반영했다. 이 정정은 법령 인용 정확성을 개선한 것이며 제품별 적용성·설계 적합성을 확정하지 않는다.

## 하드웨어 블록 설계 선택 프레임워크

하드웨어 참조 아키텍처에 DEC-01..DEC-10 설계 선택 매트릭스를 추가했다. 모션/통신 MCU 토폴로지, 부트 신뢰 시작점, Flash slot/update, debug/service, 네트워크 경계, 키 저장, 전원/리셋, 센서, gate-driver 경계, 제조 프로비저닝을 비교 대상으로 정리하고, 각 선택에 판단 기준과 시험 ID를 연결했다. G-01..G-06 설계 동결 게이트는 제품 경계, 정확한 MCU, 인터페이스, timing, 기능안전 경계, 제조 키 수명주기를 요구한다. 실제 SKU/MCU/회로가 없으므로 선택은 전부 TBD이며 이 문서는 제품별 설계 확정본이 아니다.

## main-only 자동 생성 보고서 #37–#39 감사 결과

main의 #37–#39 보고서를 EUR-Lex 원문과 대조한 결과 세 건 모두 CONFLICT로 판정했다. 지원기간은 Article 13(8), 무상 보안 업데이트는 Annex I Part II(8), CVD 정책은 Part II(5), 신고 연락처는 Part II(6)로 구분해야 한다. Article 13(6)은 통합 구성요소의 취약점 통지·수정 문맥이며 지원기간 조항이 아니다. Annex I Part II는 (a)–(d)가 아니라 (1)–(8)의 제조자 요구사항이고, Annex I Part I(2)(b)는 secure-by-default, (c)는 취약점 업데이트/자동 업데이트 조건이다. 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md).

## 하드웨어 인터페이스 설계 계약

하드웨어 참조 아키텍처에 IF-01..IF-09 인터페이스 계약을 추가했다. 외부 네트워크 입력에서 모션 명령까지, 모션 MCU와 gate driver, 센서 feedback, NVM/key storage, debug/service, power/reset, 제조 프로비저닝 경로마다 신뢰 경계와 설계 검토 항목을 정리했다. 회로도 리뷰 체크리스트는 10개 항목이며, 실제 전기 사양·핀맵·부품·타이밍·안전 경계가 확보되기 전까지 모두 설계 입력/미확인 상태다.


## 신규 아카이브 감사: main reports #40–#55

main 브랜치의 #40–#55를 EUR-Lex 원문과 대조했다. 파일 단위로 #40과 #49는 PARTIALLY_VERIFIED, 나머지 14건은 CONFLICT다. 이 배치에서 완전 VERIFIED로 직접 인용 가능한 보고서는 없다. 핵심 법령 구조는 Article 13(8) 지원기간, Article 14 신고, Annex I Part II(7) 안전한 업데이트 배포, Part II(8) 무상 보안 업데이트, Annex II point 8(d) 안전한 제품 폐기 안내다. 상세 판정과 각 보고서별 오류는 [감사 보고서](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_40_55_2026-11-12.md) 및 [주장·근거 대장](CLAIM_EVIDENCE_LEDGER.md)을 참조한다. 원본 main 파일은 보존했다.


## TI 최신 TRM Rev F 상태 재검증

TI MSPM0G3507 공식 제품 페이지에서 G-Series TRM Rev F가 2026-11-05자로 등록된 것을 확인했다. 같은 페이지의 MSPM0G3507 기능 요약은 AES, TRNG, CRC, MPU, flash ECC, SRAM parity option 및 SWD 등을 나열하지만 이는 해당 제품 페이지 수준의 근거다. TRM 본문은 25,348,105 bytes의 HTML viewer 렌더링 제한으로 열람하지 못해 보안 장·레지스터·개정 차이는 아직 미검증이다. 특히 MSPM0G3507의 기능을 MSPM0G3529-Q1에 전이하지 않는다. 상세 출처 및 claim status는 [제조사 자료 등록부](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md) §9와 [주장·근거 대장](CLAIM_EVIDENCE_LEDGER.md)을 참조한다.


## 신규 main 아카이브 감사: #56–#59

main 브랜치의 #56–#59를 EUR-Lex와 대조했다. #56과 #59는 CONFLICT, #57과 #58은 PARTIALLY_VERIFIED이며 완전 VERIFIED 보고서는 없다. 주요 오류는 Article 14의 신고 대상·시한 구분 누락, CVD 근거를 Annex I Part I Section 2로 잘못 연결한 것, Secure-by-default 구현 선택을 보편적 법적 명령으로 단정한 것, Article 13(2) 위험평가와 Article 13(8) 지원기간 및 Annex I Part II(8) 무상 업데이트를 혼동한 것이다. 상세는 [#56–#59 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_56_59_2026-11-12.md) 및 claim ledger를 참조한다. 원본 main archive는 수정하지 않았다.


## 신규 main 아카이브 감사: #60–#78

main 브랜치의 자동 생성 보고서 #60–#78 19건을 EUR-Lex Regulation (EU) 2024/2847 원문과 대조했다. 파일 단위 결과는 PARTIALLY_VERIFIED 6건(#60, #61, #63, #73, #76, #77), CONFLICT 13건, 완전 VERIFIED 0건이다. 이 배치의 Raw Text Quote는 모두 직접 인용으로 재사용할 수 없다. 반복 오류는 Article 13(7)과 13(8), Article 14 신고, Annex I Part I(2)(g) 데이터 최소화, Part II(5)–(8) 취약점 처리 요구를 혼동한 것이다. 정확한 매핑은 Article 13(8)=지원기간, Article 14=적극 악용 취약점/심각한 사고 신고, Annex I Part II(5)=CVD, (6)=취약점 신고 연락처, (7)=안전한 업데이트 배포, (8)=무상 보안 업데이트다. 상세: [#60–#78 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md). 원본 main archive는 보존했다.


## 신규 main 아카이브 감사: #79

main의 #79 보고서는 Article 14의 적극 악용 취약점 신고와 24시간 조기 경고를 다루지만, 신고 대상 범위를 넓히고 72시간 취약점 통보와 최종 보고를 혼동했다. 정확한 취약점 신고 흐름은 24시간 조기 경고, 72시간 취약점 통보, 시정/완화 조치 가용 후 14일 이내 최종 보고다. 심각한 사고는 별도 24시간/72시간/1개월 흐름이다. 파일 단위 PARTIALLY_VERIFIED이며 원문 인용은 재사용 불가다. 상세: [#79 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md).


## TI MSPM0G3529-Q1 기능안전 자료 직접 확인

TI 공식 기능안전 매뉴얼 SFFS983A Rev A(2026-10-30)의 지원 부품 목록에 MSPM0G3529-Q1이 명시되어 있음을 확인했다. §2는 SEooC 및 ISO 26262:2018 관련 개발, 체계적 무결성 ASIL D, 랜덤 고장 메커니즘 최대 ASIL B를 기술한다. §4.3은 FMEDA/안전 매뉴얼에 따른 통합자의 진단 선택, 호스트에 의한 actuator-disable 및 통신 손실 감시, FTTI >10 ms, MPFDTI <8 h 등의 시스템 가정을 명시한다. DEBUG/AES/TRNG/KEYSTORE 등은 이 안전 개념에서 QM/안전 비중요 IP로 분류된다. 따라서 ASIL D를 SIL 3와 등치하거나 해당 MCU 단독으로 서보 드라이브 SIL 3 달성을 주장해서는 안 된다. 상세: [TI 기능안전 검토](TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md).


## 신규 main 아카이브 감사: #80

main의 #80 보고서는 secure-by-default, 접근통제, 공격면 최소화 주제는 CRA Annex I Part I(2)(b),(d),(j)에 부합한다. 그러나 원문 인용은 Annex I Part I Section 1(a)–(d)라는 존재하지 않는 구조를 만들고 여러 요건을 합성했다. 모든 debug/port 비활성화, 강제 비밀번호 변경, Secure Boot의 보편 의무화는 법문을 과장한다. 파일 단위 PARTIALLY_VERIFIED이며 원문 인용은 재사용 불가다. 상세: [#80 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md).


## 신규 main archive 감사 #81–#122

main의 #81–#121 41개 연속 보고서를 EUR-Lex와 대조한 결과 파일 단위 CONFLICT 33 / PARTIALLY_VERIFIED 8 / VERIFIED 0이며, 41개 Raw Text Quote 블록은 모두 직접 인용으로 재사용할 수 없다. 반복 오류는 Article 13(8) 지원기간과 Annex I Part II(8) 무상 업데이트 혼동, 5년 미만 예상 사용기간 예외 역전/누락, Article 14 신고 범위 오해, 존재하지 않는 세부 항목과 합성 인용, Secure Boot·서명·rollback·RBAC·비밀번호·포트 설정을 보편적 법적 의무로 과장한 것이다. 상세: [#81–#121 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md).

후속 main report #122도 별도 감사하여 CONFLICT 판정했다. Secure-by-default/access-control/attack-surface 주제는 관련성이 있으나 Annex I 번호와 인용이 틀리고, 강제 비밀번호 변경·RBAC·모든 포트 비활성화는 보편적 직접 의무가 아니다. 상세: [#122 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md).

원본 main archive/history/state는 수정하지 않았고 작업 브랜치에 감사 기록만 추가했다.


## 신규 main archive 감사 #123 — 사용자 지침서/보안 정보

main report #123은 사용자 정보·지침서 제공이라는 유효한 CRA 주제를 다루지만, 핵심 근거를 Article 13(7)로 잘못 인용했다. 실제 사용자 지침서 동봉/전자 제공·명료성·보관 의무는 Article 13(18), 지원 종료일 표시·가능한 경우 종료 알림은 Article 13(19)다. Annex II는 Part I/II가 아니라 1~9번 구조이며, 보안 초기 설정·업데이트 설치·안전한 폐기·자동 업데이트 기본 설정 해제·통합자 정보는 8(a)~(f)에 있다. SBOM 접근 위치는 제조사가 사용자에게 SBOM을 제공하기로 결정한 경우의 9번이다. “Digital Product Passport”는 CRA Annex II의 법정 명칭이 아니며, 서보 드라이브 Class II 분류도 실제 제품 기능/Annex III 근거 없이 단정할 수 없다. 파일 단위 CONFLICT. 상세: [#123 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md).
