# CRA 아카이브 34개 표본 — 법령 직접 인용문 단위 감사

- 기준 브랜치: `cra-project-foundation`
- 감사 기준일: 2026-11-12
- 법령 기준: Regulation (EU) 2024/2847, EUR-Lex 공식 원문
- 공식 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 감사 대상: 기존 수동 감사 35개 ID 행, SHA-1 기준 34개 고유 원본
- 중복: A-013과 B-006은 동일 원본 `research_archive/2026-11-11_230055.md` (blob SHA-1 `a5a455e26367625b1a4c72896cd53cb34ab5ffab`)
- 목적: 법령으로 표시된 인용·인용형 문구의 원문 일치 여부와 조항 위치를 확인한다. 제품별 CRA 적합성이나 전체 archive 오류율을 판정하지 않는다.

## 1. 판정 기준

| 판정 | 의미 |
|---|---|
| VERBATIM | 공식 법령 문구와 정확히 일치(생략 표시는 별도 확인) |
| ABRIDGED_VERBATIM | 생략 부호 등을 사용한 정확한 부분 인용 |
| PARAPHRASE_MISLABELED | 취지는 일부 맞지만 따옴표로 제시되어 직접 인용처럼 오인될 수 있음 |
| COMPOSITE_OR_FABRICATED | 서로 다른 조항을 합치거나 법령에 없는 문구를 인용문으로 제시 |
| WRONG_REFERENCE | 유사하거나 실제인 문구라도 조항·항·점·Annex 위치가 틀림 |
| DUPLICATE | 다른 감사 ID와 동일 원본이므로 별도 문서로 재집계하지 않음 |

**중요:** 이 감사는 사람이 EUR-Lex 원문과 대조한 추적성 감사다. 문자열 정규화 도구로 모든 공백·구두점 차이를 자동 증명한 법의학적 문자 단위 검사라고 주장하지 않는다. 아래에서 VERBATIM/ABRIDGED_VERBATIM으로 분류하지 않은 인용은 최종 보고서에서 법령 직접 인용으로 재사용하면 안 된다.

## 2. 법령 원문에서 확인한 기준 문구와 위치

| 주제 | 공식 위치 | 감사에서 적용한 기준 |
|---|---|---|
| 지원기간 | Article 13(8) | 제품의 예상 사용기간, 합리적 사용자 기대, 제품 성격·의도된 목적 등을 고려해 정한다. 원칙적으로 최소 5년이며, 예상 사용기간이 5년보다 짧으면 그 예상 사용기간에 맞춘다. |
| 업데이트의 지속 이용 가능성 | Article 13(9) | 지원기간 중 제공된 각 보안 업데이트는 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능해야 한다. |
| 보안 업데이트 취약점 처리 | Annex I Part II(2) | 취약점을 지체 없이 처리·수정하고, 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리한다. |
| 보안 업데이트 무상 제공 | Annex I Part II(8) | 확인된 보안 문제를 해결하는 업데이트는 지체 없이 배포하고, 맞춤형 제품에 대해 제조자와 사업 사용자 간 별도 합의가 있는 경우를 제외하고 무상 제공한다. |
| SBOM | Annex I Part II(1) | 취약점·구성요소 식별 및 문서화와 함께, 일반적이고 기계 판독 가능한 형식으로 최소 top-level dependencies를 포함하는 SBOM을 작성한다. |
| 기술문서의 SBOM | Article 31(1), Annex VII(2)(b), Annex VII(8) | 기술문서에는 취약점 처리 프로세스 및 SBOM 관련 정보가 포함된다. Annex VII(8)의 SBOM 제출은 시장감시당국의 정당한 요청 등 조건이 붙는다. 일반 대중에 대한 일률적 SBOM 공개 조항으로 바꾸면 안 된다. |
| 신고 | Article 14(1)–(4) | 적극 악용 취약점과 중대한 사고를 구분한다. 적극 악용 취약점은 24시간 조기 경보, 72시간 취약점 통지, 시정·완화 조치가 가능해진 뒤 14일 이내 최종 보고. 중대한 사고는 별도 24시간·72시간·1개월 절차다. |
| 제품 보안 속성 | Annex I Part I(2)(b),(c),(d),(f),(j) 등 | Secure-by-default, 업데이트 처리, 접근통제, 무결성, 공격표면 제한은 각각의 정확한 항목으로 연결한다. 특정 알고리즘·부트로더·JTAG 잠금은 법령이 일률 지정한 문구가 아니라 위험평가에 따른 설계 선택이다. |
| 제품 분류 | Article 7, Annex III, Implementing Regulation (EU) 2025/2392 | Annex III에 열거된 카테고리의 핵심 기능이 기준이다. 구성요소를 통합했다는 사실만으로 완제품이 자동으로 Important Class I/II가 되지 않는다. |
| 적합성 평가 | Article 32 | 일반 경로는 Article 32(1), Class I의 제3자 평가 조건은 32(2), Class II 절차는 32(3)에서 각각 확인한다. |
| 기술문서 | Article 31, Annex VII | Article 31이 기술문서 조항이다. Article 24는 open-source software stewards에 관한 조항이다. |

## 3. 원본별 인용 감사 결과

표의 행 위치는 GitHub 원본 Markdown의 1-based 행 번호다. A-013/B-006은 같은 원본이므로 A-013 행에만 고유 문서 결과를 기록한다.

| 고유 원본 ID | 원본 파일 | 인용 위치 | 인용 감사 판정 및 정정 |
|---|---|---:|---|
| A-001 | `2026-11-08_082432.md` | L27, L30 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** L27의 Article 13(8) 인용은 지원기간 조항에 Annex I Part II(8)의 무상 업데이트 문구를 섞었다. L30은 업데이트 분리 요구를 Part II(5)로 연결했으나 정확한 위치는 Part II(2)이며 “where technically feasible” 조건을 포함한다. |
| A-002 | `2026-11-08_084236.md` | L20–21 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** SBOM에 모든 dependencies·vulnerabilities·open-source components를 포괄하도록 하고 기술문서에 대한 일반 제공을 포함한 인용은 법문과 일치하지 않는다. Annex I Part II(1)은 최소 top-level dependencies를 요구한다. 기술문서 관련 근거는 Article 31/Annex VII이며, Annex VII(8)은 정당한 요청 조건의 제출이다. |
| A-003 | `2026-11-08_103424.md` | L34–40 | **ABRIDGED_VERBATIM(첫 문구) + COMPOSITE_OR_FABRICATED/WRONG_REFERENCE(두 번째).** 첫 SBOM 문구는 Annex I Part II(1)의 실질 문구와 일치한다. 두 번째 “Annex VII point (j)” 인용은 해당 위치에 존재하지 않는다. 관련 기술문서 근거는 Annex VII(2)(b), 조건부 SBOM 제출은 Annex VII(8)이다. |
| A-004 | `2026-11-08_112818.md` | L23–30 | **PARAPHRASE_MISLABELED.** Secure-by-default 및 접근통제의 취지는 Part I(2)(b),(d)와 맞지만, “surfaces of attacks” 문구는 실제 “limit attack surfaces”와 다르다. 인용부호를 제거하고 요약/번역으로 표시하거나 정확한 원문으로 교체해야 한다. |
| A-005 | `2026-11-08_120059.md` | L24–32 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 11은 신고 의무가 아니라 general product safety 조항이다. 취약점 신고는 Article 14. Annex I Part II(1) SBOM, (2) 취약점 처리, (3) 정기 시험, (5) coordinated vulnerability disclosure를 서로 혼합했다. |
| A-006 | `2026-11-08_141043.md` | L26–30 | **PARAPHRASE_MISLABELED + WRONG_REFERENCE.** 첫 문구는 Part I(2)(c)의 업데이트 취지와 Part II(2)의 취약점 처리 문구를 섞은 요약이다. 두 번째 자동 설치·사용자 통지 설명도 법령의 조건과 표현을 그대로 옮긴 직접 인용이 아니다. 정확한 위치별로 분리해야 한다. |
| A-007 | `2026-11-08_191039.md` | L22, L24 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 10(6)은 존재하지 않으며 Article 10은 사이버 회복력 역량 증진이다. Part I(2)(h)는 가용성 보호이고 취약점 업데이트 항목이 아니다. 관련 근거는 Article 13(8), Annex I Part II(2),(8), Part I(2)(c)다. |
| A-008 | `2026-11-09_012542.md` | L24, L26 | **PARAPHRASE_MISLABELED + WRONG_REFERENCE.** Article 14(3)은 중대한 사고 신고다. 지원기간은 Article 13(8), 무상 업데이트는 Part II(8). 두 번째 문구는 Part II(2)와 Part I(2)(c)의 내용을 Part I Part II(2)(b)처럼 혼합했다. |
| A-009 | `2026-11-09_094606.md` | L21–22 | **PARAPHRASE_MISLABELED + WRONG_REFERENCE.** Article 13(8)의 직접 인용이 아니다. “5년 또는 예상 수명 중 짧은 기간”이라는 표현은 법문 구조와 반대 방향으로 오해를 부른다. 원칙 최소 5년, 예상 사용기간이 5년 미만이면 그 예상 사용기간으로 정정한다. |
| A-010 | `2026-11-09_180532.md` | L24–27 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 14(1) 대상은 모든 보안 영향 취약점이 아니라 적극 악용 취약점이다. 24h/72h 문구는 Article 14(2)의 각 통지 단계와 정확히 일치하지 않고, market surveillance authorities를 수신자로 넣은 문구도 해당 조항의 원문이 아니다. |
| A-011 | `2026-11-10_110057.md` | L23–27 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** 첫 인용은 Part II(1) SBOM 항목에 업데이트 관련 Part I(2)(c)/Part II(2),(8) 내용을 혼합했다. 두 번째는 Article 13 및 Annex I의 여러 요구사항을 합성한 문구이며 “expected lifetime or five years, whichever is longer”라는 문구는 지원기간 규칙과 일치하지 않는다. |
| A-012 | `2026-11-11_120102.md` | L28–32 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 14(3)은 중대한 사고 신고다. 지원기간 Article 13(8)과 무상 업데이트 Part II(8)로 분리한다. Part I(2)(g)는 데이터 최소화이지 취약점 업데이트 조항이 아니다. |
| A-014 | `2026-11-10_024038.md` | L23–27 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Annex I Part I(2)(1)은 제품의 위험 기반 적정 사이버보안 수준이지 취약점 업데이트 세부 항목이 아니다. Article 13(8) 인용도 법문과 다르며 무상 업데이트를 포함하지 않는다. |
| A-015 | `2026-11-10_192042.md` | L21–25 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** 첫 문구는 Annex I Part I의 직접 인용이 아니다. 두 번째는 Recital/Annex의 여러 취지를 합성해 무결성·진위 검증 문구를 법령 직접 인용처럼 제시했다. 안전한 업데이트 배포는 Part II(7), 데이터·명령·프로그램 무결성은 Part I(2)(f) 등으로 나누고, 구현 세부는 설계 권고로 표시한다. |
| B-001 | `2026-11-11_223547.md` | L21–25 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 11(1)(e)는 존재하지 않는다. 지원기간은 Article 13(8), 무상 업데이트는 Part II(8). Part II(1)은 제품 속성 설계 요건이 아니라 SBOM·구성요소·취약점 식별 및 문서화다. |
| B-002 | `2026-11-11_224041.md` | L24–28 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 10(6)은 존재하지 않는다. Annex I Part I Section 2(5)는 존재하지 않는 구조다. 취약점 처리·무상 업데이트·지원기간을 Article 13(8), Part II(2),(8), Part I(2)(c)로 나눈다. |
| B-003 | `2026-11-11_224540.md` | L23 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** 제시한 문구는 Article 14(지원기간)가 아니다. Article 14(3)은 중대한 사고 신고이며, 지원기간은 Article 13(8), 무상 업데이트는 Annex I Part II(8)이다. |
| B-004 | `2026-11-11_225042.md` | L24 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 14(3)은 severe incident reporting이다. 지원기간을 “5년 또는 예상 수명 중 짧은 쪽”으로 표현한 것도 법문과 반대 방향의 해석을 유발한다. |
| B-005 | `2026-11-11_225540.md` | L25–29 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 14(3)은 중대한 사고 신고이며 지원기간/무료 패치 조항이 아니다. Annex I Part I(2)(g)는 데이터 최소화다. 업데이트는 Part I(2)(c), Part II(2),(8)로 구분한다. |
| B-007 | `2026-11-11_230534.md` | L25–29 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** “secure, transparent and timely… integrity and authenticity verified”라는 문장은 CRA Annex I의 직접 인용으로 확인되지 않는다. 안전한 배포는 Part II(7), 무결성 요구 결과는 Part I(2)(f) 등으로 연결할 수 있으나, 특정 서명·진위 검증 문구를 법문에 있는 것처럼 제시하면 안 된다. |
| B-008 | `2026-11-11_231044.md` | L25–28 | **PARAPHRASE_MISLABELED + WRONG_REFERENCE.** Annex II 사용자 정보·지원기간 종료일 고지의 취지는 맞지만 인용은 Article 13(18),(19), Annex II(7)의 내용을 합친 문구다. Article 13(8)은 지원기간 산정이며 Annex II는 종료일/지원정보 고지다. |
| B-009 | `2026-11-11_231549.md` | L25–27 | **PARAPHRASE_MISLABELED + WRONG_REFERENCE.** Secure-by-default 취지는 정확하지만 법문 위치는 Annex I Part I(2)(b)이며, “initial state”가 아니라 “original state”다. “Section 1, Point 1(g)” 표기는 틀렸다. |
| B-010 | `2026-11-11_232045.md` | L28–37 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE (일부 문구는 취지만 유사).** Article 24는 Class II 적합성 평가 조항이 아니다. 실제 적합성 평가는 Article 32(3), Article 24는 open-source software stewards다. Article 28(1) DoC 문구는 취지상 근접하지만 직접 인용은 원문과 대조해 교체해야 한다. CE marking general principles는 Article 29이며 Article 30은 marking rules/conditions다. |
| B-011 | `2026-11-11_232532.md` | L25–29 | **ABRIDGED_VERBATIM(첫 문구 내용) + WRONG_REFERENCE/COMPOSITE(두 번째).** 기술문서 첫 문구는 Article 31(1)의 내용과 일치하지만 Article 24로 잘못 표기했다. 두 번째 문구는 Article 13(12), Article 31 및 다른 절차를 합성하고 조항 번호를 잘못 연결했다. |
| B-012 | `2026-11-11_233046.md` | L26–32 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 24 및 Annex VII/Article 23 참조가 잘못됐다. Article 24는 open-source software stewards, Article 31/Annex VII는 기술문서, Article 32는 적합성 평가다. Class I/II 절차는 Article 32(2),(3) 조건에 맞춰 다시 작성한다. |
| B-013 | `2026-11-11_233537.md` | L25–29 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Annex III에 “critical environments의 industrial controllers/associated servo drives” 카테고리를 추가한 인용은 법문에 없다. Annex III 실제 Class I/II 목록과 Article 7 핵심 기능 기준을 사용한다. Article 32 절차 문구도 Annex VI/VII/VIII를 임의로 조합했다. DoC 문구는 Article 28(1)로 위치를 고쳐 직접 원문과 재대조해야 한다. |
| B-014 | `2026-11-11_234037.md` | L25–26 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 11(1) 신고 의무 인용은 존재하지 않는다. 실제 Article 14(1)–(4)로, 적극 악용 취약점과 중대한 사고를 나눈다. “Annex I Part II Section 2(b)”라는 항목 구조도 존재하지 않으며 업데이트 무상 제공은 Part II(8)이다. |
| B-015 | `2026-11-11_234543.md` | L22–25 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** 자동 배포·무료 제공·업데이트 진위 검증을 하나의 Annex I Part I 인용으로 합성했다. 무료 제공은 Part II(8), 안전한 배포는 Part II(7), 업데이트/무결성 관련 제품 요구는 Part I(2)(c),(f)로 각각 연결한다. |
| B-016 | `2026-11-11_235047.md` | L23–25 | **ABRIDGED_VERBATIM(첫 문구) + PARAPHRASE_MISLABELED(두 번째).** 첫 SBOM 문구는 Annex I Part II(1)의 요건과 대체로 일치하는 생략 인용이다. 두 번째 기술문서 설명은 Article 31/Annex VII의 요약으로 직접 인용이 아니다. |
| B-017 | `2026-11-11_235547.md` | L22 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 14(3)은 중대한 사고 신고다. 지원기간 조항은 Article 13(8)이며, 5년 미만 예상 사용기간 예외를 반영해야 한다. |
| B-018 | `2026-11-12_000106.md` | L25–29 | **PARAPHRASE_MISLABELED + COMPOSITE_OR_FABRICATED.** 첫 문구는 Annex I Part II(2)의 요약에 가까우나 직접 인용은 아니다. 두 번째는 Article 13(8)과 Part II(8)의 내용을 합성했고 Article 13(4)로 잘못 연결했다. |
| B-019 | `2026-11-12_000539.md` | L22–23 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** critical vulnerabilities 자동 업데이트, 무상 제공, advisory를 합친 문구는 Annex I Part I Section 2의 직접 인용이 아니다. 취약점 수정 Part II(2), 안전한 배포 Part II(7), 무상 제공 Part II(8)로 분리한다. |
| B-020 | `2026-11-12_001038.md` | L24–28 | **COMPOSITE_OR_FABRICATED + WRONG_REFERENCE.** Article 14(3)은 중대한 사고 신고이며 지원기간 조항이 아니다. “Annex I Part II, Paragraph 1(5)”는 존재하지 않는 구조다. Part II(5)는 coordinated vulnerability disclosure policy이며, 인용된 무상 업데이트 문구는 Part II(8) 취지를 합성한 것이다. |
| B-006 | `2026-11-11_230055.md` | L23–25 | **DUPLICATE.** A-013과 동일한 파일·SHA-1이다. 별도 고유 문서로 집계하지 않는다. |

## 4. 감사 결과 요약

- 고유 원본: **34개** (감사 ID 35개 중 A-013/B-006 중복 1개 제거)
- 원본의 법령 인용 후보는 정확한 직접 인용, 생략 인용, 요약, 조항 오기, 합성·창작 문구가 혼재한다.
- 직접 인용으로 재사용할 수 있는 후보는 A-003의 Annex I Part II(1), B-011의 Article 31(1), B-016의 Annex I Part II(1)처럼 원문과 위치를 교정한 일부에 한정된다. 이들도 출처·문맥·생략 범위를 함께 표시해야 한다.
- 다수 파일에서 Article 11, Article 10, Article 14, Article 24를 제조자 의무·지원기간·적합성 평가로 잘못 사용했다.
- 지원기간(Article 13(8)), 업데이트의 무상 제공(Annex I Part II(8)), 업데이트 분리(Part II(2)), 신고(Article 14)는 서로 다른 조항이다.
- Annex I Part I(2)(g)는 데이터 최소화, Part I(2)(h)는 필수·기본 기능 가용성이다. 취약점 업데이트·무료 제공 조항이 아니다.
- Annex III에는 산업 자동화/서보 드라이브라는 독립 Class I/II 카테고리가 기재되어 있지 않다. 완제품 분류는 Article 7의 core functionality와 Commission Implementing Regulation (EU) 2025/2392를 함께 검토한다.
- 표본은 위험 기반·비무작위다. 34개 결과를 990개 전체 archive의 오류율로 일반화하지 않는다.
- 원본 archive는 수정하지 않았다. 이 문서는 인용 정정 추적 자료이며 법률 자문 또는 제품 적합성 판정이 아니다.

## 5. 재사용·정정 지침

1. 위 표에서 COMPOSITE_OR_FABRICATED, PARAPHRASE_MISLABELED, WRONG_REFERENCE로 분류된 원문 문장은 따옴표가 있는 직접 인용으로 재사용하지 않는다.
2. 요약으로 살릴 수 있는 내용은 따옴표를 제거하고 “요약/해석”으로 명시하며 정확한 법령 위치를 붙인다.
3. 직접 인용은 EUR-Lex 원문에서 다시 복사하고, 조항·항·점·Annex 위치를 함께 기록한다.
4. Article 13(8)의 지원기간을 “무료 업데이트 조항”으로 표현하지 않는다. 무상 업데이트는 Annex I Part II(8)이다.
5. Article 14는 법정 신고 대상과 시한을 정확히 구분한다. 모든 취약점·모든 사고가 동일한 신고 절차를 따르는 것처럼 쓰지 않는다.
6. 제품 등급, MCU 기능, 서보 드라이브 완제품 분류는 별도 주장으로 관리한다.

## 6. 감사 한계와 다음 단계

- 이번 검토는 기존 34개 수동 표본의 법령 인용 블록을 대상으로 했다. 나머지 956개 archive 파일과 4,400개 자동 추출 claim block을 전수 법령 검증한 것이 아니다.
- 따옴표로 감싼 문장 중 법령이 아닌 표준·제조사 문서 인용은 해당 원문 별도 감사가 필요하다. 본 보고서는 CRA Regulation (EU) 2024/2847 인용에 초점을 둔다.
- 다음 작업은 이 정정 규칙을 통합 보고서에 반영하되, 원본 archive를 수정하지 않고 검증된 요약/정정본을 별도 문서로 관리하는 것이다.


## 7. 별도 Pass B/C 재검증
기존 인용 후보 감사와 별도로 A-001–A-008의 법령 인용을 EUR-Lex 현행 원문에서 다시 확인하고 반대 근거/예외를 검토했다. 결과는 [ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)에 기록했다. 기존 표의 파일 단위 판정을 최종 VERIFIED로 간주하지 말고 새 배치 보고서의 인용 블록 단위 판정을 우선한다.
