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

기능별 표, source metadata, 제품 적용 한계 및 추가 시험 큐는 [제조사 보안 자료 레지스터](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md)를 참조한다. 개별 기술 주장과 원문 위치/상태는 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 등록했다. 현재 제조사 주장 12건(문서 수준 VERIFIED 11건, 최신판 확인 대기 PARTIALLY_VERIFIED 1건)을 등록했으며, 이 레코드는 MCU 기능 사실의 출처 검증이지 서보 드라이브 전체의 CRA 적합성 판정이 아니다.
