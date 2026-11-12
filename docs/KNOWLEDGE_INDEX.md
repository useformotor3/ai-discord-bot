# CRA 지식 인덱스 및 검증대장

이 파일은 기존 조사 아카이브와 앞으로 추가할 자료의 색인 기준이다. 현재 기존 자료의 개별 주장 검증은 아직 수행하지 않았다.

## 기존 저장소 자료 현황 (초기 관찰)
- `research_archive/`: 2026-11-12 감사 시점 main 브랜치 기준 Markdown 985개
- `history.json`: 985개 항목. archive 경로 985/985 일치, 중복 경로 0개 확인
- `state.json`: 날짜별 일일 카운터. 2026-11-11 기준 count=279이며 누적 보고서 수가 아님
- `main.py`: Gemini API를 이용한 CRA 조사 및 Discord 전송, Markdown 아카이브/상태 저장 로직
- `.github/workflows/run.yml`: workflow_dispatch 및 repository_dispatch 트리거. cron 예약 실행은 확인되지 않음
- 위 내용은 인벤토리/표본 감사 결과이며, 985개 문서의 모든 주장이 전수 검증된 것은 아니다. 대표 문서의 오류 사례는 [INITIAL_AUDIT.md](INITIAL_AUDIT.md)에 기록했다.

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

## 다음 색인 작업
1. 전체 archive 파일명/크기/날짜 인벤토리 생성
2. 문서별 제목·핵심 주장·URL 추출
3. 동일 URL 및 중복 주장 식별
4. 원문 접속 및 조항/페이지 대조
5. 검증 결과를 별도 레코드로 저장하고 원본 아카이브는 보존


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
