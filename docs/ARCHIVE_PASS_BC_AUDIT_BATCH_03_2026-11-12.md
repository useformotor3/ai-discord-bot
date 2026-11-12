# 34개 표본 Pass B/C 재검증 — Batch 03 (B-003–B-010)

- 기준일: 2026-11-12
- 대상: 8개 고유 원본 B-003–B-010
- 법령 1차 출처: Regulation (EU) 2024/2847, EUR-Lex 현행 공식 원문
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 원문 재확인 구간: Article 13(8)–(9), Article 14(1)–(8), Article 28–32, Annex I Part I/II, Annex II, Annex VII/VIII
- 한계: 동일 AI 세션의 별도 원문 재확인/반증 절차이며 제3자 독립 법률 검토가 아니다.

## 1. 원본별 Pass B/C 결과

| ID / 원본 | Pass B: 원문 재대조 | Pass C: 반증·예외 확인 | 판정 |
|---|---|---|---|
| B-003 — 2026-11-11_224540.md | Raw quote는 현행 Article 13/Annex I의 직접 인용으로 확인되지 않는다. Article 14(3)은 지원기간이 아니라 severe incident 신고다. | 지원기간 Article 13(8), 무상 업데이트 Annex I Part II(8). 맞춤형 제품에 대한 제조자-사업 사용자 간 별도 합의 예외를 Part II(8)에서 확인. | **REJECTED (직접 인용/위치)**. |
| B-004 — 2026-11-11_225042.md | Article 14(3) 인용은 현행 Article 14(3) severe incident 신고와 불일치. 인용문 “5 years or expected lifetime, whichever is shorter”는 Article 13(8)의 실제 규칙을 정확히 나타내지 않는다. | Article 13(8)은 원칙 최소 5년, 예상 사용기간이 5년 미만이면 그 기간이다. Article 14(3)–(4)는 중대한 사고 신고의 별도 타이머다. | **REJECTED (직접 인용/기간 규칙)**. |
| B-005 — 2026-11-11_225540.md | Article 14(3) Raw quote는 현행 법령 문구와 다르며 지원기간/무료 업데이트 조항이 아니다. Annex I Part I(2)(g)는 데이터 최소화, (h)는 가용성 보호다. | 무상 제공은 Part II(8), 지원기간은 Article 13(8), 신고는 Article 14. Part I(2)(g)/(h)는 다른 제품 속성 요구사항이다. | **REJECTED (직접 인용/조항 연결)**. |
| B-007 — 2026-11-11_230534.md | “secure, transparent and timely manner” 및 “integrity and authenticity of the updates are verified” 문구는 제시된 Annex I Part I Section 2 point 2의 현행 직접 인용으로 확인되지 않는다. 현행 Part I(2)(f)는 데이터·명령·프로그램·구성의 무결성 보호, Part II(7)은 업데이트의 안전한 배포 메커니즘을 규정한다. | 법령은 업데이트 서명 알고리즘, 루트 CA, TLS 버전, 부트 ROM 구현을 특정하지 않는다. 해당 조치는 threat model 기반 설계 통제로 별도 정당화해야 한다. | **REJECTED (직접 인용)** / 설계 제안은 **RECOMMENDATION**으로만 유지. |
| B-008 — 2026-11-11_231044.md | 원본의 지원기간 사용자 고지 취지는 Annex II point 7 및 Article 13(19)와 관련된다. Article 13(18)은 Annex II 사용자 정보/지침 제공, Article 13(19)은 지원기간 종료일 표시다. 제시한 문장은 이 조항들을 합친 요약이며 직접 인용은 아니다. | Annex II point 7은 기술 보안 지원 유형과 지원기간 종료일 정보. Article 13(19)은 구매 시점에 종료일(최소 월/년)을 쉽게 접근 가능한 방식으로 명확히 지정하도록 한다. | **PARAPHRASE_MISLABELED + WRONG_REFERENCE**. 따옴표를 제거하고 Article 13(18),(19), Annex II point 7로 분리. |
| B-009 — 2026-11-11_231549.md | Raw quote의 핵심 문구는 Annex I Part I(2)(b)의 secure-by-default 취지와 거의 일치하지만, 인용 위치 “Section 1, point 1(g)”는 틀렸다. 현행 문구는 “original state”이며 “initial state”가 아니다. | Part I(2)(b)는 risk assessment에 기초하며 tailor-made product에 대해 제조자와 business user 간 달리 합의하는 예외가 있다. 기본 관리자 비밀번호 금지/TLS 1.3 강제는 이 조항의 직접 문언이 아니다. | **PARTIALLY_VERIFIED**. 정확한 원문/위치로 교체. 하드코딩 자격증명 및 TLS 세부사항은 별도 표준/위험 기반 권고로 관리. |
| B-010 — 2026-11-11_232045.md | Class II 적합성 평가 조항은 Article 24가 아니라 Article 32(3). Class II 절차는 Annex VIII Module B+C, Module H 또는 해당되는 경우 assurance level “substantial”의 EU cybersecurity certification scheme이다. Module A는 Article 32(1) 일반 경로이며 Class II 경로에 포함되지 않는다. DoC는 Article 28. CE marking의 general principles는 Article 29가 Regulation 765/2008 Article 30을 참조하며, Article 30은 CRA상 CE marking 부착 규칙/조건이다. | Servo drive가 Class II라는 근거는 제공되지 않았다. Article 7은 Annex III 카테고리의 core functionality를 기준으로 하며, 단순 통합만으로 완제품이 자동 분류되지 않는다. Annex III Class II는 hypervisors/container runtimes, firewalls/IDS/IPS, tamper-resistant microprocessors/microcontrollers다. | **REJECTED (Class II 단정/Article 24 인용/절차 조합)**. 실제 Class II 분류가 별도 입증될 때에만 Article 32(3)을 적용. DoC/CE 설명은 조항별로 다시 작성. |

## 2. Batch 03 요약

- 대상 8개 파일 중 직접 인용 전체가 정확한 위치까지 VERIFIED된 파일은 0개.
- B-009의 secure-by-default 인용만 핵심 문구가 현행 Part I(2)(b)와 대체로 일치하며, 원문 위치와 “original state” 문구를 고쳐야 한다.
- 지원기간/무상 업데이트/Article 14 신고의 반복 혼동과 Article 24/32 혼동이 확인됐다.
- B-010은 서보 드라이브를 Class II라고 단정했으나 제품 core functionality 및 Annex III 카테고리 증거가 없다. Class II로 전제한 Module 경로 설명은 제품 분류가 먼저 입증될 때만 유효하다.

## 3. 설계·보고서 반영 규칙

1. 지원기간 Article 13(8), 무상 업데이트 Annex I Part II(8), 신고 Article 14를 분리.
2. secure-by-default는 Annex I Part I(2)(b), 접근통제는 (d), 무결성은 (f), 데이터 최소화는 (g), 가용성은 (h), attack surface 제한은 (j).
3. 안전한 업데이트 배포는 Annex I Part II(7). 특정 암호 서명/CA/TLS 구현은 법령 직접 인용이 아닌 설계 선택.
4. 사용자에게 지원기간 종료일을 알리는 요구는 Article 13(18),(19) 및 Annex II point 7로 연결.
5. 기술문서는 Article 31, 적합성 평가는 Article 32, DoC는 Article 28, CE 일반 원칙은 Article 29, CE 부착 규칙은 Article 30.
6. Class I/II는 Article 7/Annex III core functionality 확인 후 분류. Servo drive 명칭만으로 Class II를 단정하지 않는다.

## 4. 근거

- EUR-Lex Regulation (EU) 2024/2847, Article 7, 13(8)–(9), 14, 28–32, Annex I Part I/II, Annex II, Annex III, Annex VII/VIII.
- 공식 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 법률 자문, 독립 제3자 검토, 제품별 적합성 판정을 대체하지 않는다.
