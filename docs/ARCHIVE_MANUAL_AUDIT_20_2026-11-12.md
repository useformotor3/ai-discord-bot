# CRA 자동 조사 아카이브 추가 수동 감사 — 20개 표본 (2026-11-12)

**대상 브랜치:** `cra-project-foundation`  
**대상:** `research_archive/2026-11-11_223547.md`부터 `research_archive/2026-11-12_001038.md`까지 시간순으로 선택한 20개 연속 생성물  
**선정 성격:** 위험 주제(지원기간/무상 업데이트, 적합성 평가·분류, 업데이트 무결성, SBOM, 신고, Secure by default)가 집중된 시간 구간의 표본. 무작위 표본이 아니며 전체 990개 오류율을 추정하지 않는다.  
**기준 원문:** Regulation (EU) 2024/2847, EUR-Lex 공식 원문, 확인일 2026-11-12  
**원본 보존:** research_archive 파일은 수정하지 않았다.

## 1. 결과 요약

| 판정 | 파일 수 |
|---|---:|
| CONFLICT | 14 |
| PARTIALLY_VERIFIED | 6 |
| 합계 | 20 |

이 결과는 선정한 20개 문서의 주장/조항/인용 충돌을 의미한다. 전체 아카이브의 오류율이나 무작위 표본 추정치가 아니다. PARTIALLY_VERIFIED는 일반적인 기술·법적 취지가 일부 맞더라도 인용·조항 위치·구현 의무의 범위가 틀리거나 과장된 경우를 포함한다.

## 2. 파일별 감사 결과

| ID | 원본 파일 | SHA-1 blob | 판정 | 핵심 판정 |
|---|---|---|---|---|
| B-001 | `2026-11-11_223547.md` | `78c74abeb6f688e7ca487bcb0503bc23108af7c9` | CONFLICT | 제조자 의무/지원기간을 Article 11로 잘못 연결. 최소 5년과 예상 사용기간의 예외 방향을 뒤집었고, Article 11(1)(e) 인용은 원문과 불일치. |
| B-002 | `2026-11-11_224041.md` | `d48052e2699125c901e333fff3c06e40d0502930` | CONFLICT | Article 10은 제조자 의무 조항이 아님. Annex I Part I(2)(5)/(6) 취약점·무료 업데이트 인용 위치가 잘못됨. 제시된 인용문은 원문과 불일치. |
| B-003 | `2026-11-11_224540.md` | `e8950d852341645a767d6e1518b37419257e4c58` | CONFLICT | 지원기간/무상 업데이트를 Article 14로 잘못 연결. Article 14는 신고 의무이며 Article 13(8), Annex I Part II(8)과 구분해야 함. 인용문은 원문과 불일치. |
| B-004 | `2026-11-11_225042.md` | `20282b0f674c23d2b8ca288a64b9c75184226231` | CONFLICT | Article 14 및 Annex I Part I Section 1을 지원기간/무상 업데이트 근거로 잘못 사용. 지원기간 예외 방향 및 조항 인용이 부정확. |
| B-005 | `2026-11-11_225540.md` | `455a0142eade02587de54250e3f0c0e977df4660` | CONFLICT | Article 14(3)을 지원기간/무료 패치 조항으로 오인. Annex I Part I(2)(g)는 데이터 최소화이며 취약점 처리/무료 보안 업데이트 조항이 아님. 직접 인용도 원문과 불일치. |
| B-006 | `2026-11-11_230055.md` | `a5a455e26367625b1a4c72896cd53cb34ab5ffab` | CONFLICT | 서보 드라이브 자동 Class I, 산업 자동화/servo drive Annex III 카테고리 및 제3자 평가 의무를 창작·단정. Article 24는 적합성 평가가 아니라 오픈소스 steward 조항. |
| B-007 | `2026-11-11_230534.md` | `494a809ac7684557a5e1f3a734d5005b178ba1a7` | PARTIALLY_VERIFIED | 업데이트 무결성/진위 검증 및 안전한 배포라는 방향은 타당. 다만 CRA가 특정 Root CA/디지털 서명 방식을 일률적으로 명령한다고 단정할 수 없고, 제시한 Annex I Part I Section 2 인용은 원문과 다름. Annex I Part I(2)(f), Part II(7) 등 정확한 근거로 분리 필요. |
| B-008 | `2026-11-11_231044.md` | `610d619b651ab96def3e1e3fd707b2713815ffb6` | PARTIALLY_VERIFIED | 지원기간 산정·종료일 고지의 취지는 대체로 맞음. 다만 Article 13(8)은 지원기간 결정이고 종료일의 구매 시점 명시는 Article 13(19), 사용자 정보는 Annex II(7). 제시된 인용은 원문에 없는 문구를 혼합. |
| B-009 | `2026-11-11_231549.md` | `8c98fac204c1b4483401b7dcf9174b06718e50c1` | PARTIALLY_VERIFIED | Secure by default는 실제 요구사항이나 정확한 위치는 Annex I Part I(2)(b). 기존 문서의 Part I Section 1(1)(g) 및 인용은 잘못됨. Telnet/SSH/TLS 1.3/고유 비밀번호 등은 위험평가에 따른 설계 예시이지 조문이 직접 지정한 일률적 구현 규칙이 아님. |
| B-010 | `2026-11-11_232045.md` | `aae65c11425d11f5609e4270514209c5e071a588` | CONFLICT | Class II 분류를 제품 사실 없이 단정. Article 24가 아닌 Article 32가 제품 적합성 평가 절차이며 Article 24는 open-source software stewards. 모듈/Annex 번호도 현행 법문과 맞지 않음. |
| B-011 | `2026-11-11_232532.md` | `73af66a72a982d28d763b34fd7b7c583c4220ec0` | CONFLICT | 기술문서 근거 Article 24는 틀림(Article 31). Annex VII가 기술문서 내용. Article 13(2) 위험평가 언급은 방향상 관련되나, 제시한 Article 24 인용문과 Article 13(2) 인용문은 법문 구조와 불일치. |
| B-012 | `2026-11-11_233046.md` | `dc03188ec0e714305db2bb23a4744524349a25f4` | CONFLICT | 서보 드라이브가 Class I/II라는 추정, Annex II/III 역할 혼동, Article 24/Annex VII 기반 평가 경로 설명이 부정확. Class I/II 절차는 Article 32(2)/(3) 조건에 따라 판단. |
| B-013 | `2026-11-11_233537.md` | `9c38828bfee44f7fdabf7a7848271e238ba7d8af` | CONFLICT | Annex III에 “산업 자동화 구성요소/서보 드라이브”라는 카테고리 문구를 만들어 인용. 실제 Annex III 목록에 해당 항목은 없음. Article 24/절차·모듈 번호도 잘못됨. |
| B-014 | `2026-11-11_234037.md` | `d9d2250ed0012aa2045c1c7550f8f066c4da3b41` | CONFLICT | Article 11을 신고 조항으로 잘못 인용(Article 14). 신고 대상·24시간 기한을 광범위하게 일반화했고, Annex I Part II 인용도 잘못된 문구/위치. |
| B-015 | `2026-11-11_234543.md` | `f969dbb7c2a67ba4e1b8ea45078fa140e4dccdab` | PARTIALLY_VERIFIED | 업데이트 무결성·진위성 및 안전한 배포는 CRA 요구사항과 관련됨. 그러나 인용된 Annex I Part I Section 2(a)/(b)는 실제 법문과 불일치. 안전한 배포는 Part II(7), 무결성은 Part I(2)(f) 등으로 구분. 이중 뱅크/서명 부트로더는 구현 예시이지 모든 제품에 법문이 특정하는 설계가 아님. |
| B-016 | `2026-11-11_235047.md` | `0f74e28cb2995f3ea2561fa621e40d0388887cbc` | PARTIALLY_VERIFIED | SBOM 식별·문서화와 top-level dependencies는 Annex I Part II(1)에 부합. 그러나 Annex II는 사용자 정보/설명서이고 기술문서 내용은 Annex VII(2)(b). Annex II를 기술문서 부속서로 연결한 것은 잘못. |
| B-017 | `2026-11-11_235547.md` | `dd8f23dd3e200b54300e28069d245ff64f7698c6` | CONFLICT | Article 14(3)을 지원기간/취약점 처리 근거로 오인. 최소 5년 및 예상 사용기간 관계를 뒤집음. 지원기간은 Article 13(8), 신고는 Article 14, 보안 업데이트는 Annex I Part II(8). |
| B-018 | `2026-11-12_000106.md` | `a3dcbccecb3abe852cd4c111fe6d46a293bab233` | CONFLICT | Article 13(4)와 Annex I Part I를 지원기간/무상 업데이트 근거로 연결. 직접 인용 두 개가 법령 원문에 없는 문장. Article 13(8) 및 Annex I Part II(2)/(8)로 분리해야 함. |
| B-019 | `2026-11-12_000539.md` | `6dfbd0297c00d6a2fd4f9dc066037520faaa8fdb` | PARTIALLY_VERIFIED | 취약점 접수/CVD 및 보안 업데이트 무상 제공의 취지는 일부 맞음. 다만 Annex I Part I Section 2가 아니라 Part II(5)–(8)이며, 인용문은 원문과 불일치. Article 13(17) 연락 창구 및 Article 13(8) 지원기간도 구분 필요. |
| B-020 | `2026-11-12_001038.md` | `260546c35c4d8e4cb62b3c80d25f3a1ed9de47f5` | CONFLICT | Article 14(3)을 제조자 일반 의무/지원기간으로 오인. 지원기간은 Article 13(8), 신고는 Article 14. “예상 수명 동안 최소 5년”을 무조건 긴 기간으로 읽는 것은 틀리고 5년 미만 예상 사용기간 예외를 반영해야 함. 직접 인용은 원문과 불일치. |

## 3. 이번 표본에서 반복 확인된 정정 기준

1. **제조자 의무/지원기간:** Article 13. Article 13(8)은 제품의 예상 사용기간, 합리적인 사용자 기대, 제품의 성격 및 의도된 목적 등을 고려해 지원기간을 정하며, 원칙적으로 최소 5년이다. 제품의 예상 사용기간이 5년보다 짧으면 그 예상 사용기간에 해당한다. 지원기간 산정 근거는 Annex VII point 4 기술문서에 포함한다.
2. **보안 업데이트:** Annex I Part II(2)는 취약점의 지체 없는 처리 및 기술적으로 가능한 경우 기능 업데이트와 분리 제공. Part II(7)은 안전한 배포 메커니즘. Part II(8)은 보안 업데이트의 지체 없는 배포 및 맞춤형 제품에 대한 제조자-사업 사용자 간 별도 합의 예외를 제외한 무상 제공.
3. **제품 속성 보안:** Secure by default는 Annex I Part I(2)(b), 비인가 접근 통제는 Part I(2)(d), 데이터/명령/프로그램/구성 무결성은 Part I(2)(f), 공격표면 제한은 Part I(2)(j).
4. **신고:** Article 14는 actively exploited vulnerability 및 severe incident 신고. 적극 악용 취약점은 24시간 early warning, 72시간 vulnerability notification, 시정/완화 조치가 이용 가능해진 뒤 14일 이내 final report. Severe incident는 별도 Article 14(3)–(4) 시간표를 적용. 모든 취약점의 일률적 24/72시간 신고로 일반화하지 않는다.
5. **적합성 평가/기술문서:** Article 24는 open-source software stewards, Article 31은 technical documentation, Article 32는 conformity assessment procedures.
6. **제품 분류:** Article 7 및 Annex III의 core functionality 기준을 적용한다. Annex III에는 일반적인 산업 자동화 시스템/서보 드라이브 카테고리가 명시되어 있지 않다. Annex III Class I category 14는 security-related functionalities를 가진 microcontrollers, Class II category 4는 tamper-resistant microcontrollers다. MCU 부품 분류와 완제품 분류를 혼동하지 않는다.
7. **인용문:** 이번 표본에서 직접 인용 다수가 공식 원문과 일치하지 않았다. 인용부호가 있는 문장은 원문과 정확히 일치하는지 확인 전에는 삭제하거나 “요약/해석”으로 바꾸고, 출처 위치를 기록한다.

## 4. 공식 원문 근거

- Regulation (EU) 2024/2847, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
  - Article 7(1)–(4): Important product core functionality 및 Annex III 분류
  - Article 13(8), (9), (19): 지원기간, 보안 업데이트 보존, 지원 종료일 고지
  - Article 14(1)–(4): 적극 악용 취약점/중대한 보안 사고 신고
  - Article 24: open-source software stewards
  - Article 31: technical documentation
  - Article 32: conformity assessment procedures
  - Annex I Part I(2)(b), (d), (f), (j): 제품 보안 속성
  - Annex I Part II(1)–(8): SBOM 및 취약점 처리
  - Annex II(7): 사용자에게 제공할 보안 지원 유형 및 지원 종료일
  - Annex III: Important products with digital elements 목록
  - Annex VII(2)(b), (3), (4): 취약점 처리 프로세스/아키텍처/위험평가/지원기간 산정 정보
- Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
  - Annex III 제품 카테고리의 기술 설명 및 core functionality 해석에 사용. 제품별 분류는 정확한 제품 경계와 기능 확인 후 판단.

## 5. 전체 감사 누계 및 한계

- 초기 시간순 표본 5개: 4 CONFLICT / 1 PARTIALLY_VERIFIED.
- 추가 위험 표본 9개: 7 CONFLICT / 2 PARTIALLY_VERIFIED.
- 이번 위험 주제 연속 구간 표본 20개: 14 CONFLICT / 6 PARTIALLY_VERIFIED.
- 누계 34개: 25 CONFLICT / 9 PARTIALLY_VERIFIED.
- 34개는 서로 다른 시점/선정 방식의 표본 감사 누계이며, 무작위 추출이 아니다. 990개 전체의 오류율로 일반화할 수 없다.
- 모든 원본 archive 파일은 그대로 보존했다. 본 문서는 별도 정정/검증 기록이다.
- 법률 자문, 제품별 CRA 적용성 판정 또는 적합성 평가 완료를 의미하지 않는다.
