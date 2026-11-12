# 34개 표본 Pass B/C 재검증 — Batch 04 (B-011–B-020)

- 기준일: 2026-11-12
- 대상: 10개 고유 원본 B-011–B-020
- 법령 1차 출처: Regulation (EU) 2024/2847, EUR-Lex 현행 공식 원문
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 원문 재확인 구간: Article 7, 13(8)–(9), 14, 24, 28–32, Annex I Part I/II, Annex II, Annex III, Annex VII/VIII
- 한계: 동일 AI 세션의 별도 원문 재확인/반증 절차이며 제3자 독립 법률 검토가 아니다.

## 1. 원본별 Pass B/C 결과

| ID / 원본 | Pass B: 원문 재대조 | Pass C: 반증·예외 확인 | 판정 |
|---|---|---|---|
| B-011 — 2026-11-11_232532.md | 첫 Raw Text Quote의 핵심 문구는 현행 Article 31(1) 기술문서 조항과 일치하지만 Article 24가 아닌 Article 31이다. 두 번째 인용은 Article 13(12)와 Article 31/32 내용을 합친 문구이며, 실제 Article 13(2)는 위험평가를 계획·설계·개발·생산·납품·유지 단계에 반영하도록 한다. | Article 31(2)는 기술문서를 시장 출시 전에 작성하고 적절한 경우 지원기간 동안 계속 업데이트하도록 한다. Article 13(4)는 위험평가를 Article 31/Annex VII 기술문서에 포함한다. | **PARTIALLY_VERIFIED**. 첫 문구는 Article 31(1)로 위치 정정 후 재사용 가능. 두 번째는 직접 인용에서 제거하고 Article 13(2)–(4), Article 31로 나눠 작성. |
| B-012 — 2026-11-11_233046.md | 적합성 평가 절차는 Article 24가 아니라 Article 32. 기술문서는 Annex VII가 아니라 Annex VII의 내용과 연결되는 Article 31. Article 24는 open-source software stewards 의무다. 원본의 Article 24 quote는 현행 법령의 직접 인용이 아니다. | Article 7은 Annex III 제품 카테고리의 core functionality 기준. Class I 제3자 평가 조건은 Article 32(2), Class II 절차는 Article 32(3). 서보 드라이브가 해당 분류라는 제품 근거는 제시되지 않았다. | **REJECTED (분류 단정/조항 번호/절차 인용)**. Article 32로 정정하되 제품 분류를 먼저 입증. |
| B-013 — 2026-11-11_233537.md | Annex III Class I에 “industrial controllers, DCS, associated servo drives for critical environments”라는 카테고리는 없다. Article 24 및 Annex VII/VIII 절차 번호도 현행 법령 체계와 다르다. DoC 조항은 Article 28이지 Article 31이 아니다. | Class I 제품 절차는 Article 32(2)의 조건부 적용이며, harmonised standards/common specifications/certification의 적용 정도에 따라 Module B+C 또는 Module H 경로가 문제된다. 일반 Module A는 Article 32(1) 경로. | **REJECTED (직접 인용/Annex III 카테고리 생성/분류 단정)**. 서보 드라이브 자동 Class I 주장은 삭제. |
| B-014 — 2026-11-11_234037.md | Article 11(1) 신고 인용은 현행 법령과 불일치. 제조자 신고 의무는 Article 14. Annex I Part II의 “Section 2(b)” 구조는 존재하지 않으며 Part II(8)이 무상 보안 업데이트, Part II(5)는 CVD 정책이다. | Article 14(1)–(2)는 actively exploited vulnerability, 14(3)–(4)는 severe incident. 모든 취약점/사고에 동일한 신고 의무를 적용하면 안 된다. | **REJECTED (직접 인용/위치)**. 신고 대상을 정확히 구분하고 Part II(5)/(8)을 분리. |
| B-015 — 2026-11-11_234543.md | Raw quote의 자동 배포·무료 제공·업데이트 진위 검증을 결합한 문장은 현행 Annex I Part I의 직접 인용이 아니다. Annex I Part I(2)(c)는 업데이트 처리 및 해당되는 자동 업데이트 조건, Part II(7)은 안전한 배포, Part II(8)은 무상 제공이다. | 무결성은 Part I(2)(f)의 데이터·명령·프로그램·구성 보호와 관련될 수 있으나 법령이 서명 알고리즘/PKI/dual-bank/Secure Boot를 특정하지 않는다. | **REJECTED (직접 인용)**. 법령 요구와 설계 권고를 분리. |
| B-016 — 2026-11-11_235047.md | 첫 SBOM quote는 Annex I Part II(1)의 핵심 문구와 일치한다. 두 번째 quote의 위치 “Annex II, Section 1(a)”는 틀렸다. 기술문서 내용은 Article 31/Annex VII, 특히 Annex VII 2(a)–(c) 및 2(b)의 취약점 처리 프로세스 관련 정보에 연결된다. | Annex II는 사용자 정보·지침이다. Annex VII는 기술문서 내용이다. Article 31은 기술문서 작성/유지 의무. | **PARTIALLY_VERIFIED**. 첫 인용은 유지 가능. 두 번째는 Annex VII/Article 31로 위치 정정하고 요약과 직접 인용을 구분. |
| B-017 — 2026-11-11_235547.md | Article 14(3)은 severe incident 신고이며 지원기간/무료 패치 조항이 아니다. Raw quote의 “5 years or expected lifetime, whichever is shorter”는 현행 Article 13(8)의 규칙을 반대로 전달한다. | Article 13(8): 원칙 최소 5년, 예상 사용기간이 5년 미만이면 그 기간. Part II(8): 무상 업데이트. Article 13(9): 제공된 업데이트의 이용 가능 기간 10년 또는 지원기간 잔여기간 중 더 긴 기간. | **REJECTED (직접 인용/기간 규칙)**. |
| B-018 — 2026-11-12_000106.md | 첫 문구는 Annex I Part II(2)의 요약에 가까우나 직접 인용은 아니다. 두 번째 문구는 Article 13(8) 지원기간과 Part II(8) 무상 제공을 합성해 Article 13(4)로 잘못 연결했다. | Part II(2)는 취약점 수정 및 기술적으로 가능한 경우 기능 업데이트 분리. Part II(8)은 무상 제공. Article 13(4)는 위험평가를 기술문서에 포함하는 내용. | **PARAPHRASE_MISLABELED + COMPOSITE_OR_FABRICATED + WRONG_REFERENCE**. 따옴표 제거 후 조항별 요약으로 분리. |
| B-019 — 2026-11-12_000539.md | “critical vulnerabilities automatically … unless otherwise agreed … free of charge … advisory messages”를 합친 문구는 Annex I Part I Section 2의 현행 직접 인용으로 확인되지 않는다. CVD 정책과 취약점 연락처는 Part II(5)/(6), 무상 업데이트는 Part II(8). | 자동 업데이트 관련 제품 속성은 Part I(2)(c)에 조건이 있으며, Part II(8)의 tailor-made product exception은 제조자와 business user 간 별도 합의에 한정된다. | **REJECTED (직접 인용/조항 합성)**. |
| B-020 — 2026-11-12_001038.md | Article 14(3)은 severe incident reporting이다. “Annex I Part II, Paragraph 1(5)”라는 인용 위치 구조는 존재하지 않는다. Part II(5)는 CVD 정책이며 무상 업데이트 문구는 Part II(8)이다. | 지원기간 Article 13(8), 업데이트 보존 Article 13(9), 무상 제공 Part II(8). Article 14(3)–(4)는 사고 신고. | **REJECTED (직접 인용/위치/의무 혼합)**. |

## 2. Batch 04 요약

- 대상 10개 파일 중 직접 인용/조항 위치가 모두 정확한 파일은 없다.
- B-011의 Article 31(1) 기술문서 문구와 B-016의 Annex I Part II(1) SBOM 문구는 핵심 문구가 원문과 일치하지만 조항 위치 또는 같은 파일의 다른 인용을 정정해야 한다.
- B-012/B-013의 Article 24/32 혼동과 서보 드라이브 Class I/II 자동 분류는 근거가 없다.
- Annex II(사용자 정보)와 Annex VII(기술문서), Article 31(기술문서)와 Article 32(적합성 평가), Article 28(DoC)을 분리해야 한다.
- Article 14 신고와 Part II(5) CVD, Part II(8) 무상 업데이트를 한 조항처럼 합성하면 안 된다.

## 3. 통합 정정 규칙

1. 기술문서: Article 31 및 Annex VII.
2. 적합성 평가: Article 32 및 Annex VIII.
3. EU DoC: Article 28 및 Annex V.
4. CE marking 일반 원칙: Article 29. CRA상 부착 규칙/조건: Article 30.
5. Important Class I/II: Article 7 + Annex III + Implementing Regulation (EU) 2025/2392의 기술 설명. 제품 core functionality와 정확한 경계를 확인하기 전 등급 확정 금지.
6. Article 14 신고: actively exploited vulnerability와 severe incident를 구분.
7. Annex I Part II(5) CVD, (6) vulnerability contact address, (7) secure distribution, (8) free-of-charge security updates를 서로 구분.
8. Annex II 사용자 정보와 Annex VII 기술문서를 혼동하지 않는다.

## 4. 근거

- EUR-Lex Regulation (EU) 2024/2847, Article 7, 13, 14, 24, 28–32, Annex I–III, VII–VIII.
- 공식 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 법률 자문, 제3자 독립 검토 또는 제품별 적합성 판정을 대체하지 않는다.
