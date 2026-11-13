# Main-only CRA Archive Manual Audit — Reports #38–#42

- 감사일: 2026-11-13
- 원본 브랜치: `main` (읽기 전용)
- 기록 브랜치: `cra-project-foundation`
- 감사 범위: main reports #38–#42의 archive 원문, history metadata, blob SHA, 주장·조항·직접 인용
- 방법: Pass A 주장/인용 추출 → Pass B EUR-Lex Regulation (EU) 2024/2847 현행 원문 대조 → Pass C 조항 구조·예외·제품 적용성 반증
- 공식 기준: [EUR-Lex CELEX 32024R2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847)
- 기준선 검증 한계: 이번 배치에서는 EUR-Lex 공식 HTML의 관련 조항과 Annex I/II 원문을 다시 열어 대조했다. 별도 제3자 법률 검토, E3 controlled fetch 실행, PDF 시각 검토, 제조사 제품자료 검토는 하지 않았다. 따라서 독립 법률의견이나 제품 적합성 판정이 아니다.
- 제품 적용성: 제품 SKU, intended purpose, EU 공급 형태, 제품 경계, 데이터 저장 구조 및 실제 사용자 지침서가 미확정이므로 전부 UNVERIFIED.

## 1. 원본 추적성

| Report | Archive path | Blob SHA-1 | 주제 |
|---:|---|---|---|
| 38 | `research_archive/2026-11-13_030533.md` | `f66d4335654b3b8b9836dcaebe1205eae731c532` | 안전한 폐기·데이터 소거 |
| 39 | `research_archive/2026-11-13_031039.md` | `9dfae4ba67f48e056f222bcc86ca3189f8bb384a` | 무상 보안 업데이트 |
| 40 | `research_archive/2026-11-13_031539.md` | `449b601a1df9bef3f3acd789ea2a7fcba0804ea2` | 사용자 지침·정보 |
| 41 | `research_archive/2026-11-13_032039.md` | `e8d5ef7ead0cb481d158597110e98bdcd006b07c` | 자동 알림·보안 패치 배포 |
| 42 | `research_archive/2026-11-13_032532.md` | `0c9ca2e1c69b6bed759f1afa85dd2327d29cf319` | VDP·보안 권고문 |

## 2. 보고서별 판정

### #38 — PARTIALLY_VERIFIED

- 유효한 법적 연결은 **Annex II point 8(d)**다. 제조사는 제품의 안전한 폐기에 관한 상세 지침 또는 해당 지침의 인터넷 주소를 제공해야 하며, 그 정보에는 사용자 데이터의 안전한 제거 방법이 포함된다.
- 원문은 제조사가 모든 제품에 대해 NAND/EEPROM의 모든 민감 데이터를 복구 불가능하게 지우는 전용 기능을 구현해야 한다고 직접 규정하지 않는다. 보고서는 “정보·지침 제공” 의무를 “완전한 물리/논리적 sanitization 기능 구현” 의무로 확대했다.
- Annex I Part I(2)(e)는 데이터 기밀성, (f)는 데이터·명령·프로그램·구성의 무단 변경 방지/무결성에 관한 요구다. 이 조항을 폐기 시 잔존 데이터의 영구 소각 의무로 인용할 수 없다.
- Annex I Part II는 취약점 처리 요구사항이며 폐기 지침의 직접 근거가 아니다.
- 중요한 누락: 현행 Annex I Part I point 2(m)는 제품이 사용자에게 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 제공하도록 명시한다. 따라서 CRA에는 사용자 데이터의 안전한 영구 제거에 관한 제품 기능 결과 요구가 존재한다. 보고서가 이 조항을 인용하지 않고 Part I(1), Part II를 근거로 든 것은 조항 매핑 오류다.
- Annex II point 8(d)는 제품의 안전한 폐기와 사용자 데이터의 안전한 제거 방법에 관한 상세 지침/정보를 사용자에게 제공하도록 한다. 이 사용자 지침 의무는 Part I 2(m)의 제품 기능 결과 요구와 함께 적용해 해석해야 한다.
- Part I 2(m)는 특정 NAND/EEPROM 물리 소거 방식, 특정 삭제 알고리즘, 모든 데이터의 물리적 복구 불가능성을 특정 구현으로 명령하지 않는다. 데이터·설정의 저장 형태, 전송 가능성, 제품 위험평가에 따라 안전하고 쉽게 영구 제거할 수 있는 사용자 기능/절차를 설계해야 한다.
- Raw Text Quote: REJECTED — 인용 위치와 문언은 부정확하며, Part I(2)(m)의 직접 문언을 제시하지 않았다.
- 정정: 제품 데이터·설정 저장 구조를 확인하고 Part I(2)(m)의 삭제 가능성 및 Annex II point 8(d)의 폐기 지침을 함께 추적한다. 특정 NAND/EEPROM sanitization 방식은 위험기반 구현 선택으로 분리한다.
- 판정 이유: 안전한 데이터 제거라는 중심 의무는 Part I(2)(m) 및 Annex II point 8(d)로 부분 뒷받침되지만, 원본의 법적 locator와 특정 물리/논리 sanitization 구현 주장은 과장되어 PARTIALLY_VERIFIED로 정정한다.

### #39 — CONFLICT

- 보고서는 Article 11을 제조사 의무 근거로 제시했으나 CRA의 제조사 의무는 **Article 13**이다.
- 무상 보안 업데이트의 직접 근거는 **Annex I Part II(8)**다. 보안 업데이트는 지체 없이 배포되어야 하고, tailor-made 제품에 관해 제조사와 business user가 달리 합의한 경우를 제외하고 무상이며, 관련 정보와 잠재적 조치를 담은 advisory message가 동반되어야 한다.
- **Article 13(8)**은 취약점 처리 지원기간을 정한다. 원칙적으로 최소 5년이나 예상 사용기간이 5년 미만이면 그 예상 사용기간에 대응한다. “예상 수명 동안 모든 패치를 무조건 무료”라는 단일 문장으로 합치면 조항 구조와 예외를 놓친다.
- **Article 13(9)**은 지원기간 중 제공한 각 보안 업데이트가 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 동안 계속 이용 가능해야 한다는 별도 가용성 의무다.
- 보고서가 제시한 Annex I Part I Section 1(h) 및 “expected lifetime or five years, whichever is shorter” 문구는 현행 최종 CRA 본문 구조와 맞지 않는다.
- Raw Text Quote: REJECTED — 비현행/초안 계열 문구 및 잘못된 조항·기간 표현.

### #40 — PARTIALLY_VERIFIED

- 핵심 주제인 사용자에게 안전한 설치·운영·유지관리 및 보안 관련 정보를 제공하는 의무는 현행 **Annex II**에 존재한다.
- Annex II point 7은 제공되는 기술 보안 지원의 종류와 지원기간 종료일 정보를 요구한다. Point 8(a)–(f)는 초기 시운전 및 수명주기 중 안전한 사용 조치, 데이터 보안 영향, 보안 업데이트 설치, 안전한 폐기 및 사용자 데이터 제거, 자동 보안 업데이트 설정 해제 방법, 제품 통합자에게 필요한 정보를 다룬다.
- 다만 보고서는 이를 Annex I Part I/II와 혼합했고, 기본 관리자 계정 변경, 통신 포트 활성/비활성 절차, 보안 이벤트 로깅 설정을 모든 제품에 일률적으로 명시해야 하는 항목처럼 제시했다. 이 세부사항은 제품 기능·위험·사용자 지침서에 따라 필요성을 판단해야 하며 Annex II에 그대로 열거된 보편 문구가 아니다.
- Raw Text Quote: REJECTED — Annex II의 실제 문언을 재구성한 합성 문구이며 정확한 직접 인용으로 사용할 수 없다.
- 판정 이유: 사용자 정보 제공이라는 핵심 의무는 맞지만, 법적 위치·인용 및 구체적 필수항목 표현은 수정이 필요하다.

### #41 — CONFLICT

- 보고서는 Article 11 및 Annex I Part II를 부정확하게 묶었다. 제조사 의무의 상위 조항은 Article 13이며, Annex I Part II의 각 항목은 기능이 구분된다.
- Part II(2): 위험에 비례해 취약점을 지체 없이 처리·시정하고, 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리한다.
- Part II(3): 제품 보안의 효과적이고 정기적인 시험·검토.
- Part II(4): 보안 업데이트가 제공된 후 수정된 취약점 정보 공개. 단, 공개의 보안 위험이 보안상 이익보다 크다고 정당화되는 경우 사용자가 패치를 적용할 기회를 얻을 때까지 공개를 지연할 수 있다.
- Part II(7): 취약점의 적시 수정/완화를 위한 안전한 업데이트 배포 메커니즘. 보안 업데이트의 자동 배포는 해당하는 경우에 적용된다.
- Part II(8): 보안 업데이트의 지체 없는 배포, tailor-made 제품 관련 제조사/business user 별도 합의 예외를 제외한 무상 제공, 관련 정보를 담은 advisory message.
- CRA가 모든 서보 드라이브에 디지털 서명 검증의 특정 구현이나 rollback/fail-safe 메커니즘을 동일한 방식으로 명시한다고 단정할 수 없다. 이는 위협·위험 평가를 통해 검토할 설계 통제 후보다.
- Raw Text Quote: REJECTED — 항목 번호/문언을 합성·재배열했고, 직접 인용으로 재사용할 수 없다.

### #42 — CONFLICT

- VDP의 법적 근거는 **Annex I Part II(5)**: coordinated vulnerability disclosure 정책을 마련하고 시행하는 것이다.
- 잠재적 취약점 정보 공유를 촉진하고 신고 연락처를 제공하는 요구는 **Part II(6)**에 있다. 사용자 문서의 취약점 단일 연락 지점 및 CVD 정책 위치 안내는 **Annex II point 2**와 연결된다.
- 수정된 취약점 정보 공개는 **Part II(4)**에 있다. 보안 업데이트가 제공된 후 영향 제품 식별, 영향·심각도, 시정 정보를 공개하되, 정당화된 경우 패치 적용 기회를 먼저 제공할 수 있다.
- 보고서는 VDP와 보안 권고문 공개를 대체로 관련 주제로 잡았지만 Article 11, Annex I Part I 등 조항 위치를 혼합했다. “Class I 또는 Class II” 제품이라는 전제도 서보 드라이브 일반 명칭만으로 성립하지 않는다. Article 7 및 Annex III의 실제 열거 범주와 core functionality를 확인해야 한다.
- ENISA/각국 CSIRT에 모든 취약점 보안 권고문을 동시에 발행해야 한다는 식의 표현은 Annex I Part II(4)–(6)의 문언이 아니다. Article 14 신고는 actively exploited vulnerability 및 제품 보안에 영향을 미치는 severe incident라는 별도 법정 신고 트랙이다.
- Raw Text Quote: REJECTED — 조항·문언·제품 분류가 현행 법령 구조와 일치하지 않는다.

## 3. 배치 결과

| 항목 | 결과 |
|---|---:|
| 감사 보고서 | 5 |
| CONFLICT | 3 |
| PARTIALLY_VERIFIED | 2 |
| VERIFIED | 0 |
| 직접 인용 재사용 가능 | 0 / 5 |
| 제품별 적용성 | 5건 모두 UNVERIFIED |

이번 배치는 연속·비무작위 표본이다. 전체 history/archive 오류율로 일반화하지 않는다.

## 4. 정정 규칙 및 후속 적용

1. 안전한 폐기: Annex II point 8(d)의 사용자 지침/정보 제공 의무와 실제 데이터 삭제 기능의 설계 요구를 구분한다.
2. 지원기간: Article 13(8), 업데이트 가용성 Article 13(9), 무상 보안 업데이트 Annex I Part II(8)를 별도 필드로 관리한다.
3. 사용자 지침: Annex II point 1–9를 기준으로 하고 point 8(a)–(f)의 각 항목을 개별 추적한다. 제품별 필요성을 입증하지 않은 계정/포트/로그 항목을 법정 보편 요구로 표시하지 않는다.
4. 취약점 처리: Annex I Part II(1)–(8)을 분리하고, 특히 (4) 공개, (5) CVD 정책, (6) 연락처/정보 공유, (7) 안전한 배포, (8) 무상 제공/advisory를 혼합하지 않는다.
5. Article 14는 CVD 접수·일반 취약점 처리와 별도 트랙으로 유지한다.
6. 모든 Raw Text Quote는 공식 EUR-Lex 원문과 정확한 조항/항목 locator를 대조하기 전 재사용하지 않는다.

## 5. 다음 작업

- 다음 연속 배치: reports #43–#47. 단, 실행 직전 main HEAD, history.json, state.json을 다시 조회한다.
- Annex II 사용자 지침서 체크리스트와 Article 13/Annex I 취약점 처리 매트릭스에 이번 정정 규칙을 반영한다.
- 제1권 CRA 보고서의 EOL/decommissioning, free security updates, user instructions, VDP 절을 이번 감사 결과에 맞게 보강한다.
- 제품 SKU/제품 경계/데이터 저장 구조/지원기간이 확보되기 전 제품별 적합성은 UNVERIFIED로 유지한다.


## 5. #38 재검토 이력 — Annex I Part I point 2(m) 반영

2026-11-13 후속 교차검토에서 기존 감사가 Annex I Part I point 2(m)를 누락한 사실을 확인했다. 해당 조항은 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 제거할 수 있는 가능성을 제품에 제공하도록 요구한다. Annex II point 8(d)는 안전한 폐기 및 사용자 데이터 제거 방법에 관한 지침/정보를 별도로 요구한다.

이에 따라 #38의 파일 판정을 CONFLICT에서 PARTIALLY_VERIFIED로 정정했다. 원본이 특정 NAND/EEPROM sanitization 구현을 보편 의무로 확대하고 잘못된 조항을 인용한 문제는 유지한다. 직접 인용 재사용 판정은 계속 REJECTED이며, 제품별 적용성은 데이터 저장 구조가 미확정이므로 UNVERIFIED다.
