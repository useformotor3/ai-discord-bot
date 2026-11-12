# 34개 표본 Pass B/C 재검증 — Batch 01 (A-001–A-008)

- 기준일: 2026-11-12
- 대상: 8개 원본 파일, 기존 감사 ID A-001–A-008
- 기준 브랜치: cra-project-foundation
- 법령 1차 출처: Regulation (EU) 2024/2847, EUR-Lex 현행 공식 원문
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 원문 재확인 구간: Article 13(8)–(9), Article 14(1)–(8), Annex I Part I(2)(b)–(m), Part II(1)–(8)
- 재검증 방식: 기존 감사 결론과 분리해 각 원본 인용을 다시 읽고, 법령 원문을 별도로 열어 문맥/조항/조건을 재대조한 뒤 반대 근거를 확인했다.
- 한계: 같은 ChatGPT 작업 세션이 수행한 별도 절차 검증이며, 독립된 제3자 법률 검토 또는 인증기관 검토는 아니다. 법령 텍스트의 권위 원문은 EUR-Lex 하나로 두고, 다른 사이트의 동일 문구 반복을 독립 증거로 과장하지 않는다.

## 1. EUR-Lex 재확인 기준

| 항목 | 최종 법령 위치 | 재확인한 내용 |
|---|---|---|
| 제조자 일반 의무/위험평가 | Article 13(1)–(4) | 제품 사이버보안 위험평가를 수행·문서화하고 제품 수명주기 단계에 반영 |
| 제3자 구성요소 | Article 13(5)–(7) | due diligence, 구성요소 취약점 보고/수정, 관련 사항 기록 |
| 지원기간 | Article 13(8) | 최소 5년. 단, 제품 예상 사용기간이 5년보다 짧으면 예상 사용기간 |
| 업데이트 보존기간 | Article 13(9) | 지원기간 중 사용자에게 제공된 각 보안 업데이트는 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 제공 가능 상태 유지 |
| 보안 업데이트와 기능 업데이트 분리 | Annex I Part II(2) | 기술적으로 가능한 경우 별도 제공 |
| 무상 보안 업데이트 | Annex I Part II(8) | 확인된 보안 문제 해결 업데이트는 지체 없이 제공하고, 맞춤형 제품에 대한 제조자-사업 사용자 별도 합의 예외 외에는 무상 |
| CVD 정책 | Annex I Part II(5) | 조율된 취약점 공개 정책 수립·시행 |
| actively exploited vulnerability 신고 | Article 14(1)–(2) | 24시간 조기 경보, 72시간 취약점 통지, 시정/완화 조치 가능 후 14일 이내 최종 보고 |
| severe incident 신고 | Article 14(3)–(4) | 별도 24시간/72시간/1개월 절차 |
| secure by default | Annex I Part I(2)(b) | 맞춤형 제품에 대한 제조자-사업 사용자 합의 예외가 있고 원래 상태 복구 가능성 포함 |
| 접근통제 | Annex I Part I(2)(d) | 적절한 통제 메커니즘으로 비인가 접근 방지 |
| attack surface | Annex I Part I(2)(j) | 외부 인터페이스를 포함한 공격 표면 제한 |
| 업데이트/자동 업데이트 | Annex I Part I(2)(c) | 취약점을 보안 업데이트로 처리 가능해야 하고, 해당되는 경우 자동 설치 기본값·opt-out·알림·일시 연기 기능 관련 요건 |

## 2. 원본별 Pass B/C 결과

| ID / 원본 | Pass B: 원문 재대조 | Pass C: 반증·예외 확인 | 상태 및 정정 |
|---|---|---|---|
| A-001 — 2026-11-08_082432.md | Raw Text Quote의 Article 13(8) 문구는 최종 법령 Article 13(8)이 아니다. 해당 내용은 Annex I Part II(8)의 보안 업데이트 제공/무상/권고문 요건을 옮긴 것이다. 기능 업데이트 분리는 Part II(2)이지 Part II(5)가 아니다. | Article 13(8) 실제 문맥은 지원기간과 취약점 처리다. Part II(8)의 맞춤형 제품-사업 사용자 합의 예외를 확인. Part II(2)는 “where technically feasible” 조건을 확인. | **REJECTED (직접 인용 위치)**. 두 인용 모두 법령 문구 자체를 다른 위치에 잘못 붙였다. 정정: 무상 제공 Part II(8), 분리 Part II(2). CVE ID, severity, 완화 조치 advisory의 구체적 형식은 별도 의무/권고 근거를 찾아야 하며 이 두 조항만으로 모두 의무라고 단정하지 않는다. |
| A-002 — 2026-11-08_084236.md | Raw Text Quote는 Annex I Part II(1) 및 Annex VII 문구를 합성했다. 최종 Annex I Part II(1)은 구성요소·취약점 식별/문서화와 최소 top-level dependencies SBOM을 요구한다. Annex VII 2(b)는 취약점 처리 프로세스, SBOM, CVD 정책, 연락처, 업데이트 안전 배포 기술 솔루션을 기술문서에 포함한다. | Annex VII에는 일반 대중에게 SBOM을 무조건 제공하라는 문구가 없다. Annex II point 9는 제조자가 SBOM을 사용자에게 제공하기로 결정한 경우 접근 위치 정보를 안내하도록 한다. Annex VII point 8은 정당한 요청을 받은 시장감시당국에 필요한 경우 제출하는 조건부 규정이다. | **REJECTED (직접 인용)**. SBOM 의무의 범위·수신자를 과장한 합성 문구. 정정: Annex I Part II(1), Annex VII 2(b), Annex VII 8 및 Annex II 9를 각각 구분. |
| A-003 — 2026-11-08_103424.md | Raw Text Quote 첫 블록은 Annex I Part II(1)의 문구와 일치한다. 두 번째 블록의 Annex VII point 1(j)는 현행 최종 법령의 위치가 아니다. 관련 SBOM/취약점 처리 문서 요건은 Annex VII 2(b)에 있다. | Annex VII 2(b)의 전체 항목에는 SBOM 외에도 CVD 정책, 취약점 신고 연락처, 안전한 업데이트 배포 기술 솔루션이 있다. Annex VII 8은 정당한 요청 등 조건을 둔다. | **PARTIALLY_VERIFIED**. 첫 인용은 직접 인용 후보로 유지. 두 번째 인용은 조항 위치와 표현을 정정하고 직접 인용 재사용 전 문장 전체를 재복사해야 함. |
| A-004 — 2026-11-08_112818.md | Part I(2)(b) secure-by-default 및 original state reset, (d) 접근통제는 인용 취지와 문구가 대체로 일치한다. (j)는 원문이 “limit attack surfaces, including external interfaces”이며 원본의 “reduce the surfaces of attacks”는 직접 인용이 아니다. | Part I(2)는 cybersecurity risk assessment에 근거하고 “where applicable” 조건이 적용된다. 공통 기본 비밀번호 금지, eFuse/JTAG/SWD 완전 비활성화, UART 차단 등 세부 구현은 법령이 문자 그대로 지정하지 않는다. | **PARTIALLY_VERIFIED**. (b),(d)는 원문 위치를 유지하되 정확히 인용; (j)는 원문으로 교체. 공통 비밀번호·디버그 포트 조치는 위험 기반 설계 권고로 분리하고 IEC 62443 근거는 별도 표준 원문 검증 필요. |
| A-005 — 2026-11-08_120059.md | 본문은 Article 11을 제조자 신고 조항으로 표기했으나 최종 CRA Article 11은 general product safety 관련 조항이다. 신고는 Article 14. Raw quote의 Article 11 인용은 최종 법령 번호와 맞지 않는다. Annex I Part II(3)은 정기 시험/검토이며 CVD 정책은 Part II(5)다. 원본은 CVD 항목 번호도 섞었다. | Article 14는 actively exploited vulnerability와 severe incident를 구분하며 모든 취약점에 동일한 의무 신고를 부과하지 않는다. CVD 정책은 Annex I Part II(5), 취약점 신고 연락처는 Part II(6), SBOM은 Part II(1). | **REJECTED (신고 조항 직접 인용)** / **PARTIALLY_VERIFIED (CVD 취지)**. Article 14(1)–(2)/(3)–(4)와 Part II(5)/(6)을 별도로 다시 작성. |
| A-006 — 2026-11-08_141043.md | 본문은 Article 11과 Annex I Part II를 혼동한다. 두 Raw Text Quote 문장은 Annex I의 취지를 요약/합성했으며 정확한 직접 인용이 아니다. 자동 업데이트 문구의 관련 위치는 Part I(2)(c), 취약점 처리 및 기술적으로 가능한 경우 기능 업데이트 분리는 Part II(2). | Part I(2)(c)는 automatic updates 관련 default setting, opt-out, notification, postpone 관련 조건을 함께 둔다. Part II(2)는 보안 업데이트의 분리를 “where technically feasible”로 제한한다. CRA가 모든 서보 드라이브에 무중단 패치, 핫패치, 자동 설치를 일률 요구하지 않는다. | **REJECTED (직접 인용)** / **PARTIALLY_VERIFIED (일반 취약점 처리 취지)**. 서명 검증, 안전상태 확인, dual-bank/rollback은 합리적 설계 대책 후보지만 해당 조항이 직접 명령한 세부기술로 쓰면 안 된다. |
| A-007 — 2026-11-08_191039.md | Article 10(6)은 최종 CRA 근거가 아니다. Article 10은 enhancing skills이고 제조자 지원기간은 Article 13(8). 원본의 “whichever is shorter” 표현은 최종 법령과 다르다. Part I(2)(h)는 availability 보호이고 원본 자동 업데이트 인용의 위치는 Part I(2)(c). | Article 13(8)은 최소 5년, 단 제품 예상 사용기간이 5년 미만이면 예상 사용기간으로 한다. Part I(2)(c)는 자동 업데이트가 해당되는 경우의 조건을 규정하지만 모든 제품의 강제 자동설치를 단순화해 말하지 않는다. | **REJECTED (지원기간 직접 인용 및 조항 위치)**. 지원기간 Article 13(8), 업데이트 기능 Part I(2)(c), Part II(2)/(8)로 분리. |
| A-008 — 2026-11-09_012542.md | Article 14(3)은 severe incident 신고 조항이며 지원기간/무상 업데이트 문구가 아니다. Raw Text Quote는 Article 13(8)과 Annex I Part II(8)의 내용을 합성했다. Annex I Part I Section 2(1)(b)는 실제 조항 구조가 아니다. | 지원기간 예외는 5년 미만 예상 사용기간일 때 그 예상 기간이다. 무상 업데이트는 Part II(8)이며 맞춤형 제품-사업 사용자 합의 예외가 존재한다. 자동 업데이트·기능 업데이트 분리·무상 제공은 서로 다른 요건이다. | **REJECTED (직접 인용/위치)**. Article 13(8), Part I(2)(c), Part II(2),(8)로 분리하고 원본 문구는 직접 인용으로 재사용 금지. |

## 3. Batch 01 정량 요약

- 대상: 8개 고유 파일
- VERIFIED: 0
- PARTIALLY_VERIFIED: 3 (A-003, A-004, A-005 일부 취지)
- REJECTED: 5개 파일의 법령 직접 인용/조항 연결 (A-001, A-002, A-006, A-007, A-008); A-005의 신고 인용도 REJECTED
- 주의: 한 파일 안에 일부 맞는 주장과 틀린 인용이 함께 있을 수 있어 파일 단위 단일 상태보다 주장/인용 블록 단위 판정을 우선한다.
- 기존 수동 감사 분류(CONFLICT/PARTIALLY_VERIFIED)와 이번 직접 인용 블록 상태는 서로 다른 축이며 수치를 합산하지 않는다.

## 4. 설계 문서에 반영할 확정 규칙

1. 지원기간: Article 13(8) — 최소 5년, 예상 사용기간이 5년 미만이면 그 기간.
2. 업데이트 보존: Article 13(9) — 10년 또는 지원기간 잔여기간 중 더 긴 기간.
3. 보안 업데이트와 기능 업데이트 분리: Annex I Part II(2), 기술적으로 가능한 경우.
4. 무상 보안 업데이트: Annex I Part II(8), 맞춤형 제품 관련 제조자-사업 사용자 간 별도 합의 예외.
5. 자동 업데이트: Annex I Part I(2)(c), applicable 여부와 기본 설정/opt-out/알림/연기 조건 확인.
6. CVD: Annex I Part II(5); 취약점 연락처: Part II(6).
7. 신고: Article 14(1)–(2) 적극 악용 취약점, Article 14(3)–(4) 중대한 사고.
8. Secure Boot, 서명 검증, dual-bank, anti-rollback, hot patch는 위험평가에 따른 설계 수단으로 제시하고 법령의 특정 알고리즘/구현 의무로 표현하지 않는다.

## 5. 근거

- EUR-Lex Regulation (EU) 2024/2847, Article 13(8)–(9), 14(1)–(8), Annex I Part I(2)(b)–(m), Part II(1)–(8).
- 공식 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 검토 구간은 EUR-Lex 본문 Article 13(885–910), Article 14(939–975), Annex I(1743–1773)에서 재확인.
- 이 문서는 법령 원문 대조 기록이며 법률 자문, 독립된 제3자 검토 또는 특정 제품의 CRA 적합성 판정이 아니다.
