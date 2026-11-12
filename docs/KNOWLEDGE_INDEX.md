# CRA 지식 인덱스 및 검증대장

이 파일은 기존 조사 아카이브와 앞으로 추가할 자료의 색인 기준이다. 현재 기존 자료의 개별 주장 검증은 아직 수행하지 않았다.

## 기존 저장소 자료 현황 (초기 관찰)
- `research_archive/`: cra-project-foundation 작업 브랜치에서 Markdown 990개 확인
- `history.json`: 990개 항목. archive 경로 990/990 일치, 중복 경로 0개 확인
- `state.json`: 날짜별 일일 카운터. 2026-11-11 기준 count=279이며 누적 보고서 수가 아님
- `main.py`: Gemini API를 이용한 CRA 조사 및 Discord 전송, Markdown 아카이브/상태 저장 로직
- `.github/workflows/run.yml`: workflow_dispatch 및 repository_dispatch 트리거. cron 예약 실행은 확인되지 않음
- 위 내용은 인벤토리/표본 감사 결과이며, 990개 문서의 모든 주장이 전수 검증된 것은 아니다. 대표 문서의 오류 사례는 [INITIAL_AUDIT.md](INITIAL_AUDIT.md)에 기록했다.

## 검증 상태 정의
| 상태 | 의미 |
|---|---|
| VERIFIED | 원문과 독립 근거를 확인 |
| PARTIALLY_VERIFIED | 일부 내용/근거만 확인 |
| UNVERIFIED | 아직 검증하지 않음 |
| CONFLICT | 출처 간 불일치 |
| OUTDATED | 개정·폐지·대체된 자료 |
| NOT_APPLICABLE | 제품별 적용성 검토 후 비적용 판단 |

## 자료 레지스트리 필드
| 필드 | 설명 |
|---|---|
| record_id | 고유 자료 ID |
| local_path | 저장소 내 파일 경로 |
| topic | CRA/제품분류/취약점/SBOM/업데이트/ST/TI 등 |
| document_title | 문서 제목 |
| publisher | 발행기관 |
| source_url | 원문 URL |
| source_type | 법령/표준/가이드/데이터시트/보안공지/내부 조사 |
| version_date | 문서 버전·발행일·개정일 |
| checked_at | 실제 확인일 |
| source_excerpt | 필요한 최소 원문 인용 또는 원문 위치 |
| interpretation | 한국어 해석 |
| related_claims | 연결된 주장 ID |
| verification_status | 검증 상태 |
| notes | 제한·충돌·후속 조치 |

## 주장 레지스트리 템플릿
| claim_id | 주장 | 유형 | 원문 근거 | 교차근거 | 적용성 | 상태 |
|---|---|---|---|---|---|---|
| CRA-CLM-0001 | 조사 후 입력 | 사실/해석/권고 | URL+조항 | 독립 출처 | 제품 조건 | UNVERIFIED |

## 핵심 공식 출처 후보
아래는 조사 시작점이며, 각 자료의 현재 버전과 해당 쟁점의 근거 적합성은 실제 검증 단계에서 확인한다.
- EUR-Lex — Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- European Commission — Cyber Resilience Act 정책 페이지: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- ENISA: https://www.enisa.europa.eu/
- CEN-CENELEC: https://www.cencenelec.eu/
- ETSI: https://www.etsi.org/
- STMicroelectronics: https://www.st.com/
- Texas Instruments: https://www.ti.com/

## 제조사 조사 레코드 기준
### ST
정확한 MCU 부품 번호가 확정되기 전에는 제품군 수준의 일반 조사로 표시한다. 부트 보안, 디버그 접근 제어, 키/보안 저장, 암호 가속, 펌웨어 업데이트 보호, 보안 공지, Errata, 제품 수명주기를 확인한다.

### TI
ST와 비교할 기능 범위와 제품군을 먼저 정의한다. 동급 기능이 확인되지 않으면 '비교 불가/자료 미확인'으로 표시하며 억지로 동등 비교하지 않는다.

## 확인된 공식 기준선 (2026-11-12)
- Regulation (EU) 2024/2847 Article 14: 적극 악용 취약점 및 중대 보안 사고 신고 의무. 24시간 조기 경보 및 72시간 후속 신고 등은 Article 14의 구체 항목에 따라 구분한다.
- Article 71: 일반 적용일 2027-12-11, Article 14는 2026-09-11부터 적용, Chapter IV는 2026-06-11부터 적용.
- Annex I Part II point (2): 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리.
- Annex I Part II point (7): 안전한 업데이트 배포 메커니즘.
- Annex I Part II point (8): 보안 업데이트의 지체 없는 제공 및 원칙적인 무상 제공.
- Article 13(8): 지원 기간 결정 및 최소 5년 원칙(예상 사용기간이 5년보다 짧은 경우 예외).
- 제품의 Important Class I/II 여부는 제품 명칭만으로 단정하지 않고 Article 7, Annex III 및 Implementing Regulation (EU) 2025/2392의 핵심 기능/기술 정의로 판단한다.
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 분류 기술 설명: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392

## 출처 메타데이터 결손 감사 (2026-11-12)
- 990개 전체 후보 추출에서 URL 후보 0개. 대표 6개 원본을 열어보니 Source 항목에 문서명/조항만 있고 canonical URL이 없는 패턴을 확인.
- 추출기 schema 1.1은 출처 섹션, claim/quote 행 번호, 위험 후보 문맥을 보존.
- 모든 후보는 UNVERIFIED. 출처 URL 누락 원인 및 수동 검증 큐: [ARCHIVE_SOURCE_GAP_AUDIT_2026-11-12.md](ARCHIVE_SOURCE_GAP_AUDIT_2026-11-12.md).

## 다음 색인 작업
1. 위험 플래그별 표본을 원문과 대조해 실제 오류/정상 주장을 분리
2. 출처 문서명에서 공식 canonical URL을 복원하고 정확한 조항/페이지 연결
3. 직접 인용을 원문과 대조하고 불일치 인용을 정정/삭제
4. 검증 레코드와 정정 이력을 별도 저장하고 원본 아카이브 보존


## 2026-11-12 공식 원문 대조 — CRA 1차 기준선
- 상세 기록: [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md)
- EUR-Lex 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 13(2)–(4): 제품 의도된 용도/합리적으로 예견 가능한 사용/운영 환경 등을 고려한 위험평가와 기술문서 반영.
- Article 13(5)–(7): 제3자 구성요소 due diligence, 취약점 처리·기록.
- Article 13(8): 지원기간은 예상 사용기간/제품 특성/사용자 기대 등을 반영. 최소 5년 원칙이나 예상 사용기간이 5년 미만이면 그 기간 예외. 지원기간 산정 근거는 Annex VII 기술문서에 포함.
- Article 13(9): 지원기간 중 배포한 각 보안 업데이트는 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능.
- Annex I Part II(1): 기계 판독 가능한 SBOM, 최소 top-level dependencies 포함. Recital 77은 SBOM 공개 의무가 없다고 설명하며 Annex VII(8)은 시장감시당국의 정당한 요청 등 조건에 따른 제출을 규정.
- Annex I Part II(2): 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리.
- Annex I Part II(8): 보안 업데이트를 지체 없이 배포하고 맞춤형 제품 관련 제조자-사업 사용자 간 별도 합의 예외를 제외하고 무상 제공.
- Annex I Part I(2)(b),(d),(j): secure-by-default, 접근통제, 공격표면 최소화.
- Article 14: actively exploited vulnerability 및 severe incident 신고. Commission 페이지는 2026-09-11부터 적용, 조기경보 24시간, 72시간 통지 및 유형별 최종 보고를 확인.
- Article 71(2): Article 14는 2026-09-11, CRA 일반 적용은 2027-12-11.
- 공식 출처: Commission reporting obligations https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

## ST MCU 공식 기술 기준선
- ST AN5156 Rev 14, June 2026: https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html
- STM32 제품군별 메모리/디버그/부트/암호 기능을 설명하지만 개별 기능은 제품군과 정확한 부품번호별로 확인해야 한다.
- STM32Trust: https://www.st.com/content/st_com/en/ecosystems/stm32trust.html
- 정확한 사용 MCU 부품번호 미확인. 제품별 지원 여부는 미검증.


## 전체 archive 주장 후보 추출 결과 (2026-11-12)
- JSON: [reports/archive_claim_evidence_candidates.json](../reports/archive_claim_evidence_candidates.json)
- 990개 파일에서 claim candidate 4,400 blocks, Article candidate 1,224개, URL candidate 0개.
- 휴리스틱 플래그: SBOM 범위 305, 5년 고정지원 표현 500, Article 14 언급 201, Article 11 신고 오기 후보 85, Article 13(8) 14, Annex 혼동 21, CRA 인증 의무 오해 16, 업데이트 분리 조건 후보 4, 제품 분류 단정 190.
- 플래그는 확정 오류가 아니다. 중복 카운트 가능. 각 문서와 공식 원문을 대조해야 한다.
- URL 후보 0개는 과거 자료의 source field가 문서명 위주였을 가능성을 시사한다. 출처 링크 복원 작업이 필요하다.
- GitHub Actions run: https://github.com/useformotor3/ai-discord-bot/actions/runs/43127072320


## 수동 표본 감사
- [ARCHIVE_MANUAL_SAMPLE_AUDIT_5_2026-11-12.md](ARCHIVE_MANUAL_SAMPLE_AUDIT_5_2026-11-12.md): 초기 5개 파일을 EUR-Lex와 대조, 4 CONFLICT / 1 PARTIALLY_VERIFIED.
- 전체 오류율을 나타내는 무작위 표본은 아니다. 발견한 오류 유형을 전수 검증 규칙으로 전환하는 데 사용한다.


## 추가 수동 감사 — 2026-11-12
- [ARCHIVE_MANUAL_AUDIT_9_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_9_2026-11-12.md): 추가 9개 고위험 후보, 7 CONFLICT / 2 PARTIALLY_VERIFIED.
- 앞선 초기 5개 감사와 합계 14개 표본: 11 CONFLICT / 3 PARTIALLY_VERIFIED. 무작위 표본이 아니므로 전체 archive 오류율로 일반화하지 않는다.
- 추가 확인한 고위험 혼동: Article 10/11/14, Article 24/32, support period vs free updates, all-vulnerability reporting vs Article 14 scope, product Class I/II core-functionality classification.
- 제품 분류는 Article 7 + Implementing Regulation (EU) 2025/2392의 core-functionality 기준으로 판단한다.


## 서보 드라이브 제품 경계 기준
- [SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md): Article 2/3 적용 범위, 제품 경계 후보, remote data processing, Annex III/IV core functionality 분류 입력 템플릿.
- 서보 드라이브 명칭만으로 CRA 적용 또는 Important Class I/II를 확정하지 않는다. 완제품과 별도 판매 구성요소, MCU 자체를 분리해 검토한다.


## 2026-11-12 — 20개 고위험 아카이브 수동 감사
- 상세 판정/원본 SHA/정정 기준: [ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md).
- 20개 결과: 14 CONFLICT, 6 PARTIALLY_VERIFIED. 초기 5개 및 추가 9개 포함 누계 34개: 25 CONFLICT, 9 PARTIALLY_VERIFIED.
- 핵심 공식 조항 맵: 지원기간 Article 13(8), 종료일 고지 Article 13(19)/Annex II(7), SBOM Annex I Part II(1), 업데이트 분리 Part II(2), CVD Part II(5)–(6), 안전한 배포 Part II(7), 무상 보안 업데이트 Part II(8), 신고 Article 14, 제품 적합성 평가 Article 32, 기술문서 Article 31, open-source stewards Article 24.
- 제품 속성 보안은 Annex I Part I(2)(b)/(d)/(f)/(j). Article 7/Annex III의 core functionality 기준 없이 서보 드라이브 전체를 Class I/II로 단정하지 않는다.
- 모든 과거 archive 주장은 여전히 개별 검증 전까지 UNVERIFIED이며, 표본 결과를 전체 오류율로 일반화하지 않는다.


## 제조사 MCU 보안 자료 / claim evidence ledger (2026-11-12)
- 제조사 source register 및 기능별 비교: [MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md).
- 구조화된 주장/근거 대장: [CLAIM_EVIDENCE_LEDGER.md](CLAIM_EVIDENCE_LEDGER.md).
- ST AN5156 Rev14 June 2026: 제품군별 보안 기능, RDP/product state, WRP/PCROP/HDP/MPU/firewall/TrustZone, SB/SFU, SFI, 암호·난수 가이드. 특정 MCU 지원 여부는 exact part datasheet/reference manual/errata 확인 필수.
- TI MSPM0G3529-Q1 SLASFO2B RevB Oct 2025: §8.18 secure boot/update, debug security, AES-128/256, firewalls, up to four AES keys, CSC, monotonic counter, TRNG. §8.19–8.21 TRNG/AESADV/Keystore 상세.
- TI SLAAE29A RevA Dec 2025의 CSC/secure boot/secure storage 구조를 확인. TI 공식 G3506 자료목록에서 RevB Aug 27 2026 및 G-Series TRM RevF Nov 5 2026이 최신 문서로 표시됨. RevB 본문과 G3529-Q1 적용성은 추가 확인 대기.
- TI 제품 페이지의 PSA L1 certification targeted 표현은 인증 완료 증거가 아니다. Automotive Q1 / ASIL targeted는 CRA 적합성 판단과 별개.
- ST 실제 MCU 주문 코드 미확정이므로 ST 기능은 제품군 자료 기준선이며 부품별 검증은 UNVERIFIED.


## 2026-11-12 추가 — 서보 드라이브 보안 하드웨어 참조 설계
- [서보 드라이브 CRA 보안 하드웨어 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md): 참조 블록, trust boundary, secure boot/update 흐름, 키 프로비저닝, CRA 조항-설계-시험 증거 매핑, 시험 체크리스트. 제품별 사실은 전부 UNVERIFIED로 유지.
- TI MSPM0G3529-Q1 제품 페이지는 G-Series TRM을 참조하며, TI MSPM0-DIAGNOSTIC-LIB 기술자료 표는 G-Series TRM Rev F (2026-11-05)를 표시한다. 전체 본문은 도구의 크기 제한으로 열지 못했으므로 Rev F 보안 장 내용은 미검증.
- TI SLAAE29A Rev A는 기존에 확인한 참고 자료로 유지. SLAAE29 Rev B 본문은 이번 세션에서 공식 원문 확보 실패, UNVERIFIED.
- TI 공식 인덱스: https://www.ti.com/tool/MSPM0-DIAGNOSTIC-LIB


## 기존 CRA 아카이브 표본 정정 대장
- [ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md): 34개 고유 원본 표본의 SHA-1, 원문 행 위치, 주장 요약, 법령 정정 룰, 판정 상태 연결. 감사 ID 35개 중 A-013/B-006 중복 1개를 SHA-1 기준 제거. 고유 파일 판정 25 CONFLICT / 9 PARTIALLY_VERIFIED.
- 이 결과는 비무작위 표본이며 990개 전체 오류율로 일반화하지 않는다. 원본 archive는 불변으로 유지한다.


## 2026-11-12 — CRA 법령 인용문 단위 감사
- 상세: [ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md](ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md).
- 34개 고유 원본의 법령 인용 후보를 EUR-Lex 원문과 대조했다. A-013/B-006은 같은 원본이므로 한 번만 계산한다.
- 직접 인용과 요약을 구분하고, 조항 오기 및 합성 문구를 식별했다. 특히 Article 13(8) 지원기간, Annex I Part II(8) 무상 업데이트, Part II(2) 업데이트 분리, Article 14 신고를 서로 구분한다.
- Article 10은 역량 증진, Article 11은 일반 제품 안전, Article 24는 오픈소스 소프트웨어 스튜어드, Article 31은 기술문서, Article 32는 적합성 평가다.
- 이 결과는 위험 기반 34개 표본에 한정되며, 전체 990개 archive의 전수 검증이 아니다.


## Pass B/C 재검증 배치
- [ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md): A-001–A-008 재검증.
- EUR-Lex 현행 CRA에서 Article 13(8) 지원기간, Article 13(9) 업데이트 보존, Annex I Part I(2)(c) 자동 업데이트, Part II(2) 업데이트 분리, Part II(8) 무상 제공, Article 14 신고를 재확인.
- 동일 AI의 별도 Pass B/C 절차이며 독립 제3자 검토가 아니다. 배치 내 모든 파일은 일부 오류/부분 일치가 있어 전체 VERIFIED 없음.


## Pass B/C 재검증 인덱스
- Batch 01: [A-001–A-008](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)
- Batch 02: [A-009–A-015, B-001–B-002](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md)
- 공통 정정: Article 13(8) 지원기간, Annex I Part II(8) 무상 업데이트, Part II(2) 기능 업데이트 분리, Article 14 신고를 서로 다른 의무로 구분. 지원기간 “whichever is shorter”를 일반 규칙으로 쓰지 않는다.


## Pass B/C 재검증 인덱스
- Batch 01: [A-001–A-008](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)
- Batch 02: [A-009–A-015, B-001–B-002](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md)
- Batch 03: [B-003–B-010](ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md)
- Batch 04 예정: B-011–B-020.
- 핵심 조항 매핑: 지원기간 Article 13(8), 업데이트 보존 Article 13(9), 신고 Article 14, 기술문서 Article 31, 적합성 평가 Article 32, DoC Article 28, CE 원칙 Article 29/부착 Article 30.


## Pass B/C 최종 요약
- [34개 고유 표본 최종 재검증 요약](ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md): VERIFIED 0 / PARTIALLY_VERIFIED 6 / REJECTED 28.
- 배치 보고서: [01](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md), [02](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md), [03](ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md), [04](ARCHIVE_PASS_BC_AUDIT_BATCH_04_2026-11-12.md).
- 법령 정정 기준: Article 13(8)/(9), Article 14, Annex I Part I/II, Article 31/32, Article 28/29/30의 정확한 구분을 유지.


## 서보 드라이브 요구사항 추적성 매트릭스
- [CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md): Annex I Part I/II 및 Articles 13–14를 HW/FW/운영 통제·시험·증거 후보에 연결.
- 현재는 일반 참조 설계 초안. 제품 SKU/MCU 주문 코드/통신 구성/안전 아키텍처가 미확인이라 제품별 적용과 시험은 UNVERIFIED.


## 위협 모델 및 시험·증거 추적성 (2026-11-12)
- [일반 서보 드라이브 CRA 위협 모델](THREAT_MODEL_SERVO_DRIVE_CRA.md): AST-01..10 자산, ACT-01..06 공격자, TB-01..08 신뢰 경계, TH-01..18 시나리오 및 통제 후보.
- [보안 시험·증거 대장](SECURITY_TEST_EVIDENCE_REGISTER.md): TST-* 시험 ID, NOT_RUN 기본 상태, EV-* 증거 ID, 필수 메타데이터와 제품별 합격 기준 입력값.
- 위협·통제·시험은 일반 참조 모델이다. 실제 제품 인터페이스/MCU/안전 경계가 확인되기 전 위험 등급·제품 적용성·시험 PASS를 확정하지 않는다.


## 통합 추적성 및 2026 Commission guidance
- [통합 CRA 추적성 매트릭스](CRA_INTEGRATED_TRACEABILITY_MATRIX.md): TR-01..20을 법령, 자산/위협, HW/FW, TST, EV로 연결.
- [Commission C(2026) 5252 가이드 검토](CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md): 공식 게시 메타데이터 VERIFIED, Annex 본문 상세 검증 PENDING.
- 제조사 revision 메타데이터: ST AN5156 Rev14/June 2026; TI SLAAE29 Rev B/Aug 27 2026 및 G-Series TRM Rev F/Nov 5 2026의 공식 인덱스 표시 확인. TI 최신 revision 본문 내용은 미검증.
- [주장·근거 대장](CLAIM_EVIDENCE_LEDGER.md)에 EU-GUIDE-001, TI-012/013, ST-002 메타데이터 claim을 등록. 메타데이터 검증을 기능 claim 검증으로 확대 해석하지 않는다.
