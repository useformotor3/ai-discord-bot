# Main-only CRA Archive Manual Audit — Reports #43–#47

- 감사일: 2026-11-13
- 원본 브랜치: `main` (읽기 전용)
- 기록 브랜치: `cra-project-foundation`
- 범위: 2026-11-13 날짜의 main report #43–#47. 동일 count가 과거 날짜에도 반복되므로 날짜+count+archive path로 대상을 고정했다.
- 감사 절차: Pass A 원문 주장·직접인용 추출 → Pass B Regulation (EU) 2024/2847 및 현행 적용 implementing act 대조 → Pass C 범주·예외·반증·제품 경계 검토.
- 1차 공식 법령: [Regulation (EU) 2024/2847, EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847)
- 제품 분류 공식 보충 법령: [Commission Implementing Regulation (EU) 2025/2392, EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392) (2025-12-01 Official Journal; in force).
- 검증 한계: 공식 EUR-Lex PDF의 관련 Article/Annex 페이지와 Implementing Regulation HTML의 Annex I technical descriptions를 확인했다. 제3자 법률의견, 개별 제품 SKU/설계자료, 인증기관 의견, 제조사 내부 시험자료는 확보하지 않았다. 따라서 제품 적합성 결론은 아니다.

## 1. 원본 추적성

| Report | Archive path | Blob SHA-1 | 조사 주제 |
|---:|---|---|---|
| 43 | `research_archive/2026-11-13_033047.md` | `aaea865c90a6c082b172403248c07d5dda783102` | Class II 및 제3자 적합성 평가/CE |
| 44 | `research_archive/2026-11-13_033533.md` | `4641a3feeb5654f1abd3c59323825c7f7a5145cc` | 접근통제·권한관리 |
| 45 | `research_archive/2026-11-13_034038.md` | `ffe8ac1e5e41b80859631ac4c4975b0f6fc71bf5` | 취약점 처리 및 사용자 고지 |
| 46 | `research_archive/2026-11-13_034535.md` | `61c22b5a97fc0e053668da26956b21f7ea85fe5c` | CVD 및 무상 업데이트 |
| 47 | `research_archive/2026-11-13_035035.md` | `e5f3d9fb2fb4cda62a5fc04a50e64f3d05ca1218` | 지원기간 및 무상 취약점 수정 |

## 2. 보고서별 판정

### #43 — CONFLICT

- **핵심 오류: 서보 드라이브/IACS/PLC가 CRA Annex III Class II에 열거되어 있다는 주장은 허위 인용이다.** CRA Annex III Class II는 (1) hypervisors/container runtime systems, (2) firewalls/IDS/IPS, (3) tamper-resistant microprocessors, (4) tamper-resistant microcontrollers로 열거된다. IACS, PLC, motion controller, servo drive라는 항목은 없다.
- Article 7(1)은 Annex III 제품 범주에 해당하는 **core functionality**를 가진 제품을 important product로 본다. Commission Implementing Regulation (EU) 2025/2392 recitals (3)–(5)는 제품 전체의 core functionality와 단순 통합 구성요소를 구분하며, Annex III 기능을 포함한다는 사실만으로 최종 제품이 자동으로 해당 범주가 되는 것은 아니라고 설명한다.
- Implementing Regulation 2025/2392 Annex I의 기술 설명도 Class II 네 범주만 구체화한다. 일반적인 모션 제어 서보 드라이브가 그 자체로 Class II라고 결론 낼 근거는 확인되지 않았다. 단, 개별 제품이 별도 보안 제품 범주의 core functionality를 실제로 수행하는지는 제품별로 검토해야 한다.
- 적합성 평가 조항은 Article 24가 아니라 **Article 32**다. Article 24는 open-source software stewards의 의무다. Article 32(3)은 Class II 제품에 대해 Module B+C, Module H, 또는 이용 가능하고 적용 가능한 경우 assurance level ‘substantial’ 이상의 유럽 사이버보안 인증 절차를 규정한다. 이 절차는 실제 Class II 해당성이 확인된 경우에만 적용된다.
- Report의 Raw Text Quote에 기재한 “Annex III, Class II, Section 2” IACS/PLC/servo drive 문장은 최종 CRA Annex III에 존재하지 않는다. Article 24 인용도 주제와 불일치한다. **직접 인용 전부 REJECTED.**
- 과징금도 잘못됐다. Article 64(3)은 Article 32(1)–(3) 위반에 대해 최대 EUR 10,000,000 또는 기업의 전 세계 연간 매출액 2% 중 높은 금액을 규정한다. Annex I 및 Article 13/14 의무 위반은 Article 64(2)의 EUR 15,000,000 또는 2.5% 트랙이다. 보고서의 15m/3%는 정확하지 않다.
- 정정: 우선 제품 intended purpose, SKU, 제품 경계, 핵심 기능 및 통합 구성요소를 확인한다. 그 다음 Article 7 + Annex III + Implementing Regulation 2025/2392의 technical description을 적용하고, 분류가 성립할 때만 Article 32(2)/(3) 절차를 결정한다.

### #44 — PARTIALLY_VERIFIED

- 접근통제는 CRA의 명시적 요구다. 정확한 근거는 **Annex I Part I point 2(d)**: 무단 접근으로부터 보호하기 위한 적절한 제어 메커니즘을 마련하고, 인증·ID·접근관리 시스템 등을 포함하며, 가능한 무단 접근을 보고해야 한다.
- 보고서의 주제(서보 드라이브 접근통제/권한관리)는 타당하다. 그러나 “Section 1, Point 1” 및 “Section 2, Point 1(a)”로 제시한 직접 인용은 최종 Annex I 구조·문언과 일치하지 않는다. 실제 조항은 Part I point 2(d)다.
- CRA가 모든 서보 드라이브에 RBAC, 특정 역할 3단계, 최소권한, STO/게인 파라미터 관리자 인증, 최초 접속 시 고유 비밀번호 강제, 인증서 기반 장치 인증을 각각 보편적 구현 방식으로 명시한 것은 아니다. 위험평가 결과에 따라 적절한 제어를 선택하고 Article 13(3)에 따라 적용성 및 구현 방식을 기술문서에 설명해야 한다.
- 하드코딩 자격증명·공통 기본 암호·백도어 금지는 강력한 설계 통제 후보일 수 있지만, 보고서처럼 Annex I의 직접 문언 또는 일률적 CRA 조항으로 단정할 수 없다.
- Raw Text Quote: REJECTED — 취지는 실제 Annex I point 2(d)와 유사하지만 인용한 위치와 문장이 원문과 다르다.
- 판정 이유: 법적 주제는 VERIFIED 방향이나, 세부 요구 및 인용의 법적 과장 때문에 전체 문서는 PARTIALLY_VERIFIED.

### #45 — PARTIALLY_VERIFIED

- 취약점 처리 프로세스가 필요하고, 보안 업데이트 및 사용자 안내가 요구된다는 중심 주장은 맞다. 다만 제조사 의무를 Article 11로 표기한 것은 잘못이며, 일반 제조사 의무의 중심 조항은 **Article 13**이다.
- Annex I Part II의 구조를 바로잡아야 한다: (1) 취약점·구성요소 식별/문서화 및 SBOM, (2) 위험에 비례한 취약점 처리·시정 및 보안 업데이트, (3) 효과적이고 정기적인 보안 시험/검토, (4) 보안 업데이트 제공 후 수정된 취약점 공개(정당화된 경우 패치 적용 기회까지 공개 지연 가능), (5) CVD 정책, (6) 취약점 신고 연락처 및 정보 공유 촉진, (7) 안전한 업데이트 배포 메커니즘, (8) 보안 업데이트 지체 없는 배포·원칙적 무상 제공·advisory message.
- Report의 Raw Text Quote로 제시된 Article 11(7)은 현행 최종 CRA의 정확한 조항/문언이 아니다. Annex I Part II(1)도 자동 업데이트 및 사용자 고지 문구가 아니라 취약점과 구성요소를 식별·문서화하고 SBOM을 작성하는 항목이다. 자동 업데이트 기본 설정 관련 제품 요구는 Annex I Part I point 2(c), 보안 업데이트의 안전한 배포/고지는 Part II(7)–(8) 등과 구분한다.
- 서보 드라이브의 downtime 최소화, 제어 루프·모터 동역학 영향 검증은 CRA의 제품 위험·안전한 업데이트 설계에 연결할 수 있는 기술적 실행 과제이나, 보고서의 특정 운영 방식이 법령에 그대로 명시된 것은 아니다.
- Raw Text Quote: REJECTED — 조항 번호와 문구 불일치.
- 판정 이유: 취약점 처리·업데이트 고지의 핵심은 맞지만 법적 근거 및 인용은 수정해야 하므로 PARTIALLY_VERIFIED.

### #46 — CONFLICT

- 무상 보안 업데이트의 직접 근거는 Article 11이 아니라 **Annex I Part II point 8**이다. 원칙적으로 보안 업데이트는 지체 없이 배포되고 무상이며, tailor-made product에 대해 제조사와 business user가 달리 합의한 경우는 예외다. 업데이트에는 사용자에게 관련 정보와 잠재적 조치를 안내하는 advisory message가 동반되어야 한다.
- 지원기간은 **Article 13(8)**이다. 원칙적으로 최소 5년이나 제품의 예상 사용기간이 5년 미만이면 지원기간은 예상 사용기간에 대응한다. 단순히 “예상 수명 동안 무상 패치”라는 한 문장으로 대체할 수 없다.
- Article 13(9)는 지원기간 중 제공된 각 보안 업데이트가 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 동안 계속 이용 가능하도록 하는 별도 의무다.
- CVD 정책은 Annex I Part II(5), 고정된 취약점 정보 공개는 Part II(4)다. Article 14는 모든 취약점 일반에 대한 일괄 신고 조항이 아니다. actively exploited vulnerability와 제품 보안에 영향을 미치는 severe incident라는 법정 신고 범주를 대상으로 하며, 정해진 신고 단계·기한이 별도로 적용된다.
- 보고서의 “유지보수 계약과 무관하게 모든 사용자”라는 일반화는 tailor-made product 예외를 누락한다. “ENISA 및 관련 국가 당국에 취약점 발견 시 적시에 신고”라는 설명도 Article 14의 신고 트리거를 과도하게 넓힌다.
- Raw Text Quote: REJECTED — 조항 혼합, 예외 누락, 현행 법령의 정확한 직접 인용 아님.

### #47 — CONFLICT

- 무료 보안 업데이트는 Annex I Part II(8), 지원기간은 Article 13(8), 제공된 보안 업데이트의 장기 가용성은 Article 13(9)로 분리해야 한다.
- Article 13(8)의 기본 규칙은 최소 5년이지만, 제품이 5년 미만 사용될 것으로 예상되면 지원기간은 그 예상 사용기간에 대응한다. 따라서 “제품 예상 수명과 무관하게 최소 5년” 또는 “예상 수명과 5년 중 긴 기간”으로 단순화하면 잘못이다.
- “최소 5년”을 “최소 5년 또는 예상 수명 중 더 긴 기간”으로 해석하는 것도 조문과 다르다. 예상 사용기간이 5년보다 긴 제품에서는 제조사가 합리적인 지원기간 결정 근거를 문서화해야 하며, 산업용 제품은 장기간 사용을 고려해야 한다.
- Part II(8)의 무상 제공에도 tailor-made product와 business user 간 별도 합의 예외가 있다. 모든 고객·모든 계약에 무조건 적용된다고 표현하면 안 된다.
- Report의 Raw Text Quote는 CRA 최종본의 Article/Annex locator와 문언이 일치하지 않는다. 또한 제품이 Class I/II라는 일반화는 별도 입증이 없다.
- Raw Text Quote: REJECTED — 초안 계열 또는 합성 문구로 보이며 최종본 직접 인용으로 재사용 불가.

## 3. 배치 결과

| 판정 | 건수 |
|---|---:|
| CONFLICT | 3 (#43, #46, #47) |
| PARTIALLY_VERIFIED | 2 (#44, #45) |
| VERIFIED | 0 |
| 직접 인용 재사용 승인 | 0 / 5 |
| 제품별 적용성 | 모두 UNVERIFIED |

이번 #43–#47은 날짜와 count로 고정한 연속·비무작위 표본이다. 전체 archive 오류율로 일반화하지 않는다.

## 4. CRA 기준 정정 매트릭스

| 주제 | 정확한 법적 근거 | 보고서 작성 시 적용 |
|---|---|---|
| 제품 분류 | Article 7(1)–(4), Annex III, Implementing Regulation 2025/2392 | core functionality 및 기술 설명 기준. 통합 구성요소만으로 최종 제품의 중요 제품 분류가 자동 성립하지 않음 |
| 접근통제 | Annex I Part I point 2(d) | 적절한 접근 제어 메커니즘. RBAC/least privilege/인증서 등은 위험 기반 구현 수단으로 구분 |
| 취약점 식별/수정 | Annex I Part II points 1–3 | SBOM·취약점 기록, 지체 없는 위험 기반 수정, 정기 시험 |
| 공개/CVD/신고 | Annex I Part II points 4–6; Article 14 | 공개, CVD, 신고 연락처, Article 14 법정 신고 트리거를 분리 |
| 안전한 업데이트 | Annex I Part II points 7–8; Annex I Part I point 2(c) | 안전한 배포, 해당 시 자동 설치, 무상 배포 및 advisory message의 예외를 구분 |
| 지원기간 | Article 13(8) | 최소 5년, 단 예상 사용기간이 5년 미만이면 그 기간 |
| 업데이트 가용성 | Article 13(9) | 각 업데이트가 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 이용 가능 |
| 적합성 평가 | Article 32 | 일반 Module A, Class I 조건부 제3자 평가, Class II 평가 절차를 실제 범주 해당성에 따라 구분 |
| 과징금 | Article 64(2)–(3) | 위반 조항에 따라 15m/2.5% 또는 10m/2% 트랙 구분 |

## 5. 다음 작업

1. 다음 연속 감사 배치 #48–#52. 매번 main HEAD/history/state 및 날짜+count+path를 다시 조회한다.
2. 보고서 #43의 잘못된 Class II/서보 드라이브 단정은 CRA 마스터 보고서의 제품 분류 절에서 명시적으로 정정한다.
3. Annex I Part I point 2(d) 접근통제 매트릭스를 작성하되 법적 의무와 권장 설계 통제(RBAC, least privilege, unique credentials, certificate-based authentication)를 별도 컬럼으로 분리한다.
4. Article 13(8)/(9), Annex I Part II(4)–(8) 기반 취약점·지원기간·업데이트 요구사항 표를 실제 보고서에 반영한다.
5. SKU, intended purpose, core functionality, EU 공급 형태 및 제품 경계가 확보되기 전 제품별 분류/적합성은 UNVERIFIED로 유지한다.
