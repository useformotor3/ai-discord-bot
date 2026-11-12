# CRA 아카이브 34건 원자적 주장 정정 대장

**기준일:** 2026-11-12  
**대상 브랜치:** `cra-project-foundation`  
**목적:** 수동 감사 34개 원본의 핵심 문제를 원본 파일·SHA-1 blob·원문 위치·정정 근거에 연결한다.  
**중요:** 이 대장은 감사 표본의 정정 추적 기록이며, 990개 전체 아카이브의 전수 검증이나 오류율 추정이 아니다. 원본 `research_archive/` 파일은 수정하지 않았다.

## 1. 판정 원칙

- **CONFLICT:** 원본의 조항 위치, 법적 의무, 인용, 적용 범위 또는 분류 주장이 공식 법령과 충돌한다.
- **PARTIALLY_VERIFIED:** 큰 방향의 취지는 일부 맞지만 법적 근거 위치, 직접 인용, 적용 범위 또는 의무 강도가 잘못되었거나 미확정이다.
- 원문 행 번호는 현재 작업 브랜치의 원본 Markdown 파일을 기준으로 한다. SHA-1 blob은 파일 동일성 확인용이다.
- 원본이 주장한 문장을 짧게 발췌하거나 요약했다. 직접 인용으로 제시되었던 문구는 EUR-Lex 법문과 정확히 대조되지 않으면 인용 재사용을 금지한다.
- **VERIFIED는 개별 법령 사실의 출처 확인 상태**이지, 제품별 CRA 적합성 또는 설계 구현 완료를 뜻하지 않는다.

## 2. 법령 기준 정정 룰

| Rule ID | 올바른 근거 | 정정 규칙 |
|---|---|---|
| L-01 | Article 13(8) | 지원기간은 예상 사용기간, 합리적 사용자 기대, 제품 성격·의도된 목적 등을 고려해 정한다. 원칙적으로 최소 5년이며, 예상 사용기간이 5년보다 짧으면 예상 사용기간에 해당한다. |
| L-02 | Annex I Part II(2) | 취약점을 지체 없이 처리하고, 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리한다. |
| L-03 | Annex I Part II(7) | 보안 업데이트의 안전한 배포 메커니즘을 마련한다. |
| L-04 | Annex I Part II(8) | 보안 업데이트는 지체 없이 제공하고, 맞춤형 제품에 대해 제조자와 사업 사용자 간 별도 합의가 있는 경우를 제외하고 무상 제공한다. |
| L-05 | Annex I Part II(1) | 구성요소와 취약점을 식별·문서화하고, 일반적으로 사용되는 기계 판독형 SBOM을 작성한다. 최소 top-level dependencies를 포함한다. 이를 모든 사용자에게 공개해야 한다는 일반 의무로 확대하지 않는다. |
| L-06 | Annex VII(2)(b), (8) 및 Recital 77 | 기술문서에 취약점 처리 프로세스·SBOM 관련 정보를 포함한다. 시장감시당국 요청에 따른 제출과 일반 대중 공개를 구분한다. |
| L-07 | Annex I Part I(2)(b), (d), (f), (j) | Secure-by-default, 접근통제, 무결성, 공격표면 제한을 각각 구분한다. 구체적인 JTAG 잠금, eFuse, 프로토콜 비활성화 등은 제품별 설계 통제 예시이지 조문이 일률적으로 지정한 구현이 아니다. |
| L-08 | Article 14(1)–(4), Article 16 | 법정 신고 대상은 actively exploited vulnerability와 severe incident로 구분한다. 취약점 신고는 24시간 early warning, 72시간 vulnerability notification, 시정/완화 조치 이용 가능 후 14일 이내 final report. Severe incident는 별도 24시간/72시간/1개월 절차다. Single Reporting Platform과 CSIRT coordinator/ENISA 흐름을 정확히 표현한다. |
| L-09 | Article 7, Annex III, Implementing Regulation (EU) 2025/2392 | 제품의 core functionality로 Important product 여부를 판단한다. 통합 MCU 또는 다른 구성요소만으로 완제품 서보 드라이브가 자동 Class I/II가 되지 않는다. |
| L-10 | Article 24, 31, 32 | Article 24는 open-source software stewards, Article 31은 technical documentation, Article 32는 conformity assessment procedures다. |
| L-11 | Article 32(2)–(3) | Class I/II의 제3자 적합성 평가 경로는 법령이 정한 조건과 적용 가능한 조화표준·공통규격·사이버보안 인증제도 적용 여부에 따라 판단한다. Class I 전체에 Notified Body가 무조건 필요하다고 일반화하지 않는다. |
| L-12 | Annex I Part I(2)(f), Part II(7) 등 | 업데이트 무결성·진위 검증은 보안 설계상 중요한 통제지만, 특정 Root CA, 알고리즘, dual-bank 부트로더를 모든 제품에 법문이 직접 지정한다고 쓰지 않는다. |

## 3. 초기 5개 감사 — A-001 ~ A-005

| ID | 원본 파일 / SHA-1 blob | 원문 위치·주장 요약 | 정정 및 근거 룰 | 감사 상태 |
|---|---|---|---|---|
| A-001 | `research_archive/2026-11-08_082432.md` / `3b3afabe9b3bf0bb1009e450ff135f9f6d045412` | L14: Article 13(8)을 무상 업데이트 직접 근거로 표현. L26–30: Article 13(8), Annex I Part II(5)로 잘못된 원문 인용 | 지원기간은 Article 13(8), 업데이트 분리는 Part II(2, 기술적으로 가능한 경우), 안전한 배포는 Part II(7), 무상 제공은 Part II(8). 인용문은 법문과 불일치. L-01~L-04 | CONFLICT |
| A-002 | `research_archive/2026-11-08_084236.md` / `ab077e1be945a856ab5bf5ee6e1e0c285a23a014` | L10–13: SBOM을 모든 구성요소로 작성하고 규제당국·사용자에게 제공해야 한다고 확대. L19–21: 존재하지 않는 Annex 인용문 | Annex I Part II(1)의 SBOM 작성·문서화와 일반 공개 의무를 구분. 최소 top-level dependencies. 조건부 당국 제출과 대중 공개를 혼동하지 않음. L-05~L-06 | CONFLICT |
| A-003 | `research_archive/2026-11-08_103424.md` / `2152d213a49292116f1849184aadd76e948357ef` | L13–15: “Annex II, Part II”를 취약점 처리 근거로 표기. L37–40: Annex VII point 1(j)로 SBOM 인용 | 취약점 처리/SBOM은 Annex I Part II(1). 기술문서 세부는 Annex VII(2)(b) 등. Annex II는 사용자 정보·지침. IEC 62443 연결은 별도 표준 원문 확인 전 UNVERIFIED. L-05~L-06 | CONFLICT |
| A-004 | `research_archive/2026-11-08_112818.md` / `b6c71b0c3f22e4a4121cb840c4d225dd6c567f8c` | L10, L20–23: Secure-by-default, 접근통제, 공격표면 조항의 큰 방향은 맞지만 세부 구현을 직접 의무처럼 설명 | Annex I Part I(2)(b),(d),(j) 위치는 유지. 고유 비밀번호, JTAG/SWD 잠금, eFuse, challenge-response 등은 위험평가에 따른 설계 예시로 분리. 원문 인용 표현 수정. L-07 | PARTIALLY_VERIFIED |
| A-005 | `research_archive/2026-11-08_120059.md` / `01e0e65e9f69be0aab15c5a75bd6a82f11d6e30d` | L16, L21–31: Article 11을 신고 조항으로 표시하고 신고 대상·시간·ENISA 경로를 부정확하게 단순화 | 신고 의무는 Article 14. actively exploited vulnerability와 severe incident를 분리하고 24h/72h/final report 시한과 Single Reporting Platform 경로를 정확히 반영. L-08 | CONFLICT |

## 4. 추가 9개 감사 — A-006 ~ A-015

| ID | 원본 파일 / SHA-1 blob | 원문 위치·주장 요약 | 정정 및 근거 룰 | 감사 상태 |
|---|---|---|---|---|
| A-006 | `research_archive/2026-11-08_141043.md` / `acf99bf357d8a20ee63191bed54007a33c03499d` | L14–15, L23–30: Article 11을 제조자 의무로 연결하고 Annex I Part II/Article 11의 취약점 처리 인용을 혼합 | 제조자 의무 Article 13, 취약점 처리 Annex I Part II. Article 11은 General product safety. 자동 탐지 도구/주기는 별도 위험 기반 권고. L-08 | CONFLICT |
| A-007 | `research_archive/2026-11-08_191039.md` / `be44fb28b96a0340781083a65766b5c3f80f4db4` | L13, L19–24: Article 10(6)을 제조자 무료 업데이트 의무로 인용하고 Part I(2)(h)를 취약점 업데이트 근거로 사용 | Article 10은 enhancing skills. 제조자 의무 Article 13(8), 무상 업데이트 Part II(8). Part I(2)(h)는 필수/기본 기능 가용성 보호. L-01,L-04,L-07,L-10 | CONFLICT |
| A-008 | `research_archive/2026-11-09_012542.md` / `f7ad83d4f5dba33b5ae45c6558039c2c493b2e77` | L13–15, L20–26: Article 14를 제조자 의무/무상 패치 근거로 표시하고 존재하지 않는 Article 14(3) 인용 제시 | 지원기간 Article 13(8), 무상 보안 업데이트 Annex I Part II(8), Article 14는 신고. 5년 미만 예상 사용기간 예외를 명시. L-01,L-04,L-08 | CONFLICT |
| A-009 | `research_archive/2026-11-09_094606.md` / `de2e2e8dcac750ff640288d39538bb3b66550eaf` | L13–14, L18–21: “최소 5년 또는 예상 사용기간 중 더 긴 기간”처럼 예외 관계를 모호하게 설명하고 Article 13(8) 직접 인용이 불일치 | 원칙 최소 5년, 예상 사용기간이 5년보다 짧으면 그 예상 사용기간. 종료일 고지와 사용자 정보/기술문서 근거를 분리. L-01,L-06 | CONFLICT |
| A-010 | `research_archive/2026-11-09_180532.md` / `1ebf8cbe4ef51dead6dd316a46198c0662f4c3af` | L21–27: 신고 기한과 취약점/사고 범위의 법적 근거를 혼합 | Article 14(1)–(2)는 actively exploited vulnerability, Article 14(3)–(4)는 severe incident. 72시간은 vulnerability notification/incident notification이며 모든 경우의 final report가 아님. L-08 | CONFLICT |
| A-011 | `research_archive/2026-11-10_110057.md` / `3475c4af9d089509447b7db304ae4fad1012f3fc` | L13, L20–26: 서보 드라이브를 Important product로 전제하고 취약점 공개/무상 업데이트 범위를 넓게 서술 | CVD 정책은 Annex I Part II(5), 연락처는 (6), 공개는 (4) 및 정당한 지연 예외, 무료 업데이트는 (8). 제품 등급은 Article 7/Annex III core functionality로 별도 판단. L-04,L-08,L-09 | PARTIALLY_VERIFIED |
| A-012 | `research_archive/2026-11-11_120102.md` / `ab4fd2df609146138e55aaee537953697e7b872c` | L12, L24–32: Article 14(3)을 지원기간·무료 업데이트로 인용하고 Part I(2)(g)/(h)를 취약점 업데이트 근거로 사용 | Article 13(8), Annex I Part II(8)로 정정. Part I(2)(g)는 데이터 최소화, (h)는 가용성. L-01,L-04,L-07,L-08 | CONFLICT |
| A-013 | `research_archive/2026-11-11_230055.md` / `a5a455e26367625b1a4c72896cd53cb34ab5ffab` | L10–14, L19–25: 서보 드라이브 자동 Class I, 무조건 Notified Body, Article 24 및 Annex III 산업 자동화 인용을 단정 | Article 7 core functionality와 Implementing Regulation 2025/2392에 따라 판단. Article 24는 open-source stewards, Article 32는 적합성 평가. Class I 제3자 절차는 Article 32(2)의 조건부 경로. L-09~L-11 | CONFLICT |
| A-014 | `research_archive/2026-11-10_024038.md` / `32c78e11c61885f5d7cb31a22f3dd8eeed1cfc64` | L12–15, L20–24: Part I를 취약점 처리로 사용하고 5년 지원을 일률 의무로 표현 | 지원기간 Article 13(8) 및 5년 미만 예상 사용기간 예외. 취약점 처리 Annex I Part II, 무료 업데이트 (8), 기능 업데이트 분리 (2). L-01,L-02,L-04 | CONFLICT |
| A-015 | `research_archive/2026-11-10_192042.md` / `7f94bcb3cf915106cee86c8608bf95b1684795cd` | L13, L18–22: 무료 업데이트·업데이트 무결성의 설계 취지는 타당하나 Part I Section 2를 근거로 하고 인용문이 원문과 불일치 | 무료 업데이트 Annex I Part II(8). 안전한 배포 Part II(7). 무결성 통제는 Part I(2)(f) 등 요구 결과에 연결하되 특정 알고리즘/부트 체인은 권고로 구분. L-04,L-07,L-12 | PARTIALLY_VERIFIED |

## 5. 추가 20개 감사 — B-001 ~ B-020

| ID | 원본 파일 / SHA-1 blob | 원문 위치·주장 요약 | 정정 및 근거 룰 | 감사 상태 |
|---|---|---|---|---|
| B-001 | `research_archive/2026-11-11_223547.md` / `78c74abeb6f688e7ca487bcb0503bc23108af7c9` | L13, L18, L21–25: Article 11 제조자 의무, 5년 미만 제품의 최소 5년 적용 주장, Article 11(1)(e) 인용 | Article 13(8)이며 5년 미만 예상 사용기간이면 그 기간. Part II(8) 무료 업데이트. L-01,L-04,L-10 | CONFLICT |
| B-002 | `research_archive/2026-11-11_224041.md` / `d48052e2699125c901e333fff3c06e40d0502930` | L15, L21–28: Article 10을 제조자 의무로 사용하고 Part I(2)(5)/(6)에 취약점·무료 업데이트를 연결 | Article 10은 enhancing skills. Article 13(8), Annex I Part II(5)–(8)로 분리. 인용문 재작성. L-01,L-04,L-07,L-10 | CONFLICT |
| B-003 | `research_archive/2026-11-11_224540.md` / `e8950d852341645a767d6e1518b37419257e4c58` | L13–15, L22–24: Article 14를 지원기간/무료 업데이트 조항으로 표시하고 존재하지 않는 인용문 사용 | Article 14는 신고. 지원기간 Article 13(8), 무상 업데이트 Part II(8). L-01,L-04,L-08 | CONFLICT |
| B-004 | `research_archive/2026-11-11_225042.md` / `20282b0f674c23d2b8ca288a64b9c75184226231` | L12, L16, L21–25: Article 14를 지원기간/무료 업데이트로 연결하고 최소 5년/예상 사용기간 관계를 잘못 표현 | Article 13(8)의 예외 방향으로 정정. 무료 업데이트 Part II(8). L-01,L-04,L-08 | CONFLICT |
| B-005 | `research_archive/2026-11-11_225540.md` / `455a0142eade02587de54250e3f0c0e977df4660` | L13, L16, L22–29: Article 14(3)을 지원기간/무료 패치로 오인하고 Part I(2)(g)를 취약점 처리 근거로 인용 | Article 14(3)은 severe incident 신고. Article 13(8) 및 Annex I Part II(8)로 정정. Part I(2)(g)는 data minimisation. L-01,L-04,L-08 | CONFLICT |
| B-006 | `research_archive/2026-11-11_230055.md` / `a5a455e26367625b1a4c72896cd53cb34ab5ffab` | L10, L13–14, L19–25: 서보 드라이브 Class I 단정, Article 24, Annex III 산업 자동화 카테고리 및 무조건 제3자 평가 주장 | Article 7 core functionality, Annex III 실제 카테고리, Implementing Regulation 2025/2392 대조. Article 32 절차로 정정. L-09~L-11 | CONFLICT |
| B-007 | `research_archive/2026-11-11_230534.md` / `494a809ac7684557a5e1f3a734d5005b178ba1a7` | L14, L22, L27–29: 안전한 업데이트 배포/무결성은 타당하나 Part I Section 2 인용과 원문 위치가 부정확 | 안전한 배포 Part II(7), 데이터·명령·프로그램 무결성 Part I(2)(f) 등으로 구분. Root CA/서명 방식은 제품별 권고. L-07,L-12 | PARTIALLY_VERIFIED |
| B-008 | `research_archive/2026-11-11_231044.md` / `610d619b651ab96def3e1e3fd707b2713815ffb6` | L12, L15, L22–28: 지원기간/종료일 고지의 취지는 일부 맞지만 Article 13(8) 및 Annex II 관련 직접 인용을 혼합 | 지원기간 산정 Article 13(8), 구매 시점 종료일 고지 Article 13(19), 사용자 정보 Annex II(7), 기술문서 Annex VII. L-01,L-06 | PARTIALLY_VERIFIED |
| B-009 | `research_archive/2026-11-11_231549.md` / `8c98fac204c1b4483401b7dcf9174b06718e50c1` | L14–15, L22–27: Secure by default는 맞으나 Annex I Part I Section 1(1)(g) 위치·인용이 잘못되고 구체 프로토콜 통제를 의무화 | Annex I Part I(2)(b)로 정정. Telnet/SSH/TLS/고유 비밀번호는 위험평가 기반 구현 예시. L-07 | PARTIALLY_VERIFIED |
| B-010 | `research_archive/2026-11-11_232045.md` / `aae65c11425d11f5609e4270514209c5e071a588` | L10, L15–17, L24, L28–31: Class II를 근거 없이 단정하고 Article 24/모듈·부속서 경로를 잘못 인용 | Article 7/Annex III로 분류부터 판단. Article 32(3) 및 정확한 Annex 모듈 참조로 재작성. L-09~L-11 | CONFLICT |
| B-011 | `research_archive/2026-11-11_232532.md` / `73af66a72a982d28d763b34fd7b7c583c4220ec0` | L10, L13–14, L22–29: Article 24를 기술문서 근거로 오인하고 Annex VII/Article 13 인용 구조도 부정확 | 기술문서는 Article 31 및 Annex VII. 제조자 위험평가는 Article 13(2), 적합성 평가는 Article 32. L-10 | CONFLICT |
| B-012 | `research_archive/2026-11-11_233046.md` / `dc03188ec0e714305db2bb23a4744524349a25f4` | L7, L15–17, L22–32: 서보 드라이브 Class I/II 추정, Annex II/III 혼동, Article 24 기반 평가 경로 | Article 7 core functionality와 Annex III/2025/2392 적용. Article 32 절차, Annex II는 사용자 정보. L-09~L-11 | CONFLICT |
| B-013 | `research_archive/2026-11-11_233537.md` / `9c38828bfee44f7fdabf7a7848271e238ba7d8af` | L10, L13–17, L21–29: Annex III에 산업 자동화/서보 드라이브 카테고리를 만들어 인용하고 Class I/Notified Body를 단정 | Annex III 실제 항목과 core functionality만 사용. 서보 드라이브 자동 Class I 근거 없음. Article 32(2) 조건부 절차. L-09,L-11 | CONFLICT |
| B-014 | `research_archive/2026-11-11_234037.md` / `d9d2250ed0012aa2045c1c7550f8f066c4da3b41` | L13, L16–17, L22–26: Article 11을 신고 근거로, Article 14를 업데이트 근거로 혼동하고 신고 시한·인용을 부정확하게 일반화 | Article 14 신고 대상·절차를 actively exploited vulnerability와 severe incident로 분리. 업데이트는 Annex I Part II. L-04,L-08 | CONFLICT |
| B-015 | `research_archive/2026-11-11_234543.md` / `f969dbb7c2a67ba4e1b8ea45078fa140e4dccdab` | L14, L19–25: 업데이트 무결성/안전한 배포 취지는 타당하지만 Part I Section 2로 오인용 | 안전한 배포 Part II(7), 무료 제공 Part II(8), 무결성 Part I(2)(f) 등으로 분리. 서명 부트로더는 설계 예시. L-04,L-07,L-12 | PARTIALLY_VERIFIED |
| B-016 | `research_archive/2026-11-11_235047.md` / `0f74e28cb2995f3ea2561fa621e40d0388887cbc` | L14, L19–25: SBOM 취약점 처리 Annex I Part II와 기술문서 Annex II를 혼동하고 인용 위치가 부정확 | SBOM Annex I Part II(1), 기술문서 Article 31/Annex VII, Annex II는 사용자 정보. L-05,L-06,L-10 | PARTIALLY_VERIFIED |
| B-017 | `research_archive/2026-11-11_235547.md` / `dd8f23dd3e200b54300e28069d245ff64f7698c6` | L14, L19–22: Article 14를 제조자 의무/지원기간으로 표시하고 5년 예외 관계가 부정확 | Article 13(8)으로 정정, 5년 미만 예상 사용기간 예외 반영. 신고는 Article 14. L-01,L-08,L-10 | CONFLICT |
| B-018 | `research_archive/2026-11-12_000106.md` / `a3dcbccecb3abe852cd4c111fe6d46a293bab233` | L18, L22–29: 존재하지 않는 Article 13(4)/Annex I 인용문을 사용해 무료 업데이트·지원기간을 설명 | Article 13(8), Annex I Part II(8) 및 Part II(2)로 정정. 직접 인용은 EUR-Lex와 다시 대조. L-01,L-02,L-04 | CONFLICT |
| B-019 | `research_archive/2026-11-12_000539.md` / `6dfbd0297c00d6a2fd4f9dc066037520faaa8fdb` | L14, L19–23: 취약점 처리·무상 업데이트의 취지는 일부 맞지만 Part I Section 2를 인용하고 원문을 합성 | CVD/연락처/안전한 배포/무상 제공은 Annex I Part II(5)–(8)로 각각 분리. L-04,L-05,L-06 | PARTIALLY_VERIFIED |
| B-020 | `research_archive/2026-11-12_001038.md` / `260546c35c4d8e4cb62b3c80d25f3a1ed9de47f5` | L14–16, L21–28: Article 14(3)을 제조자 의무·지원기간으로 오인하고 최소 5년과 예상 사용기간 관계를 잘못 설명 | 지원기간 Article 13(8), 신고 Article 14, 무료 업데이트 Annex I Part II(8). 5년 미만 예상 사용기간 예외 적용. L-01,L-04,L-08 | CONFLICT |

## 6. 표본 감사 결과와 범위

| 배치 | 표본 수 | CONFLICT | PARTIALLY_VERIFIED |
|---|---:|---:|---:|
| 초기 5개 감사 배치 | 5개 고유 파일 | 4 | 1 |
| 추가 9개 감사 배치 | 9개 고유 파일(10개 ID, 중복 1개) | 7 | 2 |
| 추가 20개 감사 배치 | 19개 순증 고유 파일(20개 ID, 중복 1개) | 13 | 6 |
| **합계** | **34개 고유 원본** | **25** | **9** |

**집계 정정:** 추가 9개 감사 보고서는 제목상 9개 파일을 대상으로 하지만 ID가 A-006~A-015로 10개 기재되어 있다. 원본 경로와 SHA-1을 대조한 결과 A-013과 B-006은 동일 원본 `research_archive/2026-11-11_230055.md`, SHA-1 `a5a455e26367625b1a4c72896cd53cb34ab5ffab`이다. 따라서 35개 감사 ID 행은 34개 고유 원본 파일을 가리킨다. 고유 파일 기준 판정은 CONFLICT 25개, PARTIALLY_VERIFIED 9개이며, 기존 상황판의 누계 34/25/9가 맞다. 추가 9개 배치의 고유 대상은 A-006~A-012, A-014~A-015의 9개 파일이며, 고유 파일 기준 7 CONFLICT / 2 PARTIALLY_VERIFIED다. ID 기준 집계는 중복 A-013/B-006 때문에 CONFLICT가 26개로 한 번 중복 계산된다.

## 7. 미해결 후속 작업

- [x] A-013/B-006 중복을 SHA-1로 확인하고 고유 파일 기준 집계 보정
- [ ] 각 원본의 직접 인용 블록을 EUR-Lex 원문과 문자 단위 비교하고 인용 오류를 개별 quote claim으로 분리
- [x] A-001~A-015, B-001~B-020의 원본 경로·SHA-1 중복 여부 대조 완료 (A-013/B-006만 중복)
- [ ] 각 claim에 canonical URL, 조항·항·점, 최소 원문 excerpt, 한국어 정정문을 개별 레코드로 확장
- [ ] 원본 archive 파일은 계속 불변으로 유지

## 8. 공식 근거

1. Regulation (EU) 2024/2847, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
2. Commission Implementing Regulation (EU) 2025/2392, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392

**법령 적용 주의:** Article 14 신고 의무는 2026-09-11부터 적용되며, CRA 일반 적용일은 2027-12-11이다(Article 71). 이 문서는 법률 자문이나 제품별 적합성 판정이 아니다.
