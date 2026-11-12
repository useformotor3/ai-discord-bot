# CRA 조사 아카이브 수동 표본 감사 — 2026-11-12

**대상:** 기존 자동 조사 자료 중 초기 5개 파일 (2026-11-08)  
**선정 방식:** 시간순 초기 5개. 무작위 표본이 아니며 전체 990개 오류율을 추정하는 데 사용할 수 없음.  
**기준 원문:** EUR-Lex Regulation (EU) 2024/2847  
**공식 원문:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847  
**검증 상태:** 5개 파일의 주장과 조항/인용 후보를 공식 원문과 직접 비교한 표본 감사.

## 요약

| 파일 | 주제 | 판정 | 핵심 문제 |
|---|---|---|---|
| 2026-11-08_082432.md | 보안 업데이트/지원기간 | CONFLICT | Article 13(8)과 Annex I Part II(2)/(8) 혼동, 직접 인용 부정확 |
| 2026-11-08_084236.md | SBOM | CONFLICT | SBOM 공개·제공 범위 과장, Annex 근거 위치 오류, 직접 인용 부정확 |
| 2026-11-08_103424.md | SBOM | CONFLICT | Annex II를 Annex I로 잘못 인용, Annex VII 항목 위치 오류 |
| 2026-11-08_112818.md | Secure by default | PARTIALLY_VERIFIED | 핵심 조항은 대체로 맞지만 세부 통제 구현을 법문 의무로 단정 |
| 2026-11-08_120059.md | CVD/신고 | CONFLICT | Article 11 오기. 제조자 신고 의무는 Article 14. 대상/신고기한 표현도 부정확 |

**중요:** 이 5건은 표본에서 실제로 확인한 오류 사례다. 990개 전체의 오류 개수/비율로 일반화하지 않는다.

## 상세 감사

### A-001 — 2026-11-08_082432.md
**파일:** [원본](../research_archive/2026-11-08_082432.md)  
**SHA-1 blob:** `3b3afabe9b3bf0bb1009e450ff135f9f6d045412`

1. **지원기간과 무상 업데이트 조항을 혼동**
   - 문서가 Article 13(8)을 무상 보안 업데이트의 직접 근거로 설명했으나, Article 13(8)은 취약점 처리 기간 및 지원기간 결정 기준을 규정한다.
   - 보안 업데이트의 원칙적 무상 제공 근거는 Annex I Part II point (8).
2. **기능 업데이트 분리 조항 위치 오류**
   - 분리 근거는 Annex I Part II point (2)이며, 법문에는 “where technically feasible” 조건이 있다.
   - 문서가 point (5)를 분리 근거로 썼으나 point (5)는 coordinated vulnerability disclosure 정책이다.
3. **직접 인용이 공식 원문과 일치하지 않음**
   - Article 13(8) 인용문은 현행 원문 조항 내용과 일치하지 않는다.
   - Annex I Part II point (5) 인용문도 point (2)의 업데이트 분리 취지를 point (5)에 잘못 붙였다.
4. **지원기간 문구 보완**
   - Article 13(8)은 원칙적으로 최소 5년이나, 제품 예상 사용기간이 5년 미만이면 그 예상 사용기간에 해당하는 예외가 있다.
5. **권고 정정**
   - 지원기간: Article 13(8).
   - 기능 업데이트 분리: Annex I Part II(2), 기술적으로 가능한 경우.
   - 무상 보안 업데이트: Annex I Part II(8), 맞춤형 제품 관련 제조자-사업 사용자 간 별도 합의 예외 포함.

### A-002 — 2026-11-08_084236.md
**파일:** [원본](../research_archive/2026-11-08_084236.md)  
**SHA-1 blob:** `ab077e1be945a856ab5bf5ee6e1e0c285a23a014`

1. **SBOM 작성/유지 주장의 범위 조정**
   - Annex I Part II(1)은 구성요소와 취약점 식별·문서화, 일반적으로 사용되는 기계 판독형 SBOM, 최소 top-level dependencies를 규정한다.
   - “모든 구성요소를 무조건 전부 나열” 또는 “모든 사용자에게 SBOM을 제공”으로 확대 해석하면 안 된다.
2. **공개 의무 과장**
   - Recital 77은 제조자가 SBOM을 공개할 의무가 없다고 명시한다.
   - Annex VII point 8은 시장감시당국의 reasoned request 등 조건에 따른 SBOM 제출을 규정한다.
   - 따라서 “규제 당국 및 사용자가 자동 스캔하도록 SBOM을 제공해야 한다”는 문장은 일반 공개/사용자 제공 의무로 오해될 수 있어 수정해야 한다.
3. **원문 위치 및 인용 문제**
   - SBOM 근거는 Annex I Part II(1)이며, Annex VII 2(b)에는 vulnerability-handling process 정보의 일부로 SBOM이 포함된다.
   - Annex VII point 8은 조건부 요청 제출 규정이다.
   - 기존 원문 인용은 “Annex I, Section 2” 등의 위치가 부정확하고 문구도 법령 원문과 일치하지 않는다.
4. **권고 정정**
   - 제품 내 SBOM 작성/문서화 의무와 공개/제출 의무를 분리해 설명.
   - 최소 top-level dependencies를 명시.
   - CycloneDX/SPDX는 실무 포맷 예시로 설명하되 법령이 특정 포맷을 강제한다고 쓰지 않는다.

### A-003 — 2026-11-08_103424.md
**파일:** [원본](../research_archive/2026-11-08_103424.md)  
**SHA-1 blob:** `2152d213a49292116f1849184aadd76e948357ef`

1. **Annex 번호 오류**
   - 문서가 “Annex II, Part II Vulnerability Handling Requirements”라고 기재했으나 올바른 위치는 Annex I Part II.
   - Annex II는 Information and Instructions to the User에 해당한다.
2. **Annex VII 항목 위치 오류**
   - 문서의 Annex VII point 1(j) 인용은 부정확하다.
   - 기술문서의 SBOM 및 CVD/업데이트 배포 정보는 Annex VII point 2(b)와 연결된다.
   - Annex VII point 8은 시장감시당국의 정당한 요청 등 조건에 따른 SBOM 제출이다.
3. **Article 13(5) 해석**
   - 제3자 구성요소 통합 시 due diligence 의무라는 설명은 조항 취지와 부합한다.
   - 다만 Article 13(5)만으로 구체적인 모든 CVE 상시 모니터링 주기/도구를 법정 형식으로 단정하면 안 된다. 실무 통제는 위험 기반으로 설계한다.
4. **표준 연결 주장**
   - IEC 62443-4-1 Practice 8과의 연계 설명은 별도 표준 원문/판본 대조 전까지 UNVERIFIED로 남긴다.
   - 표준과 CRA 법적 의무는 구분한다. 표준은 CRA의 직접 조문이 아니다.

### A-004 — 2026-11-08_112818.md
**파일:** [원본](../research_archive/2026-11-08_112818.md)  
**SHA-1 blob:** `b6c71b0c3f22e4a4121cb840c4d225dd6c567f8c`

1. **확인된 핵심 조항**
   - Annex I Part I(2)(b): secure-by-default configuration.
   - Annex I Part I(2)(d): 비인가 접근 방지 통제(인증, identity/access management 포함).
   - Annex I Part I(2)(j): 외부 인터페이스를 포함한 attack surface 제한.
2. **법문보다 강한 구현 세부를 분리해야 함**
   - 고유 초기 비밀번호, 공통 기본 비밀번호 제거, JTAG/SWD 잠금, eFuse, challenge-response, Telnet/FTP 비활성화는 제품 위협모델에 따른 합리적 구현 예시가 될 수 있다.
   - 그러나 위 세부사항을 해당 CRA 조항이 문자 그대로 각각 강제한다고 쓰면 안 된다. 제품의 위험평가와 설계 근거로 연결해야 한다.
3. **Factory reset 표현**
   - 법문은 원래 상태로 reset할 가능성을 요구한다. “항상 별도의 secure baseline으로 초기화”라고 단정하기보다 초기화 상태가 보안 요구사항을 훼손하지 않는지 제품 설계/위험평가로 입증하도록 설명한다.
4. **직접 인용 교정**
   - 기존 문서의 “delivered with” 및 “reduce the surfaces of attacks” 문구는 공식 법문과 일치하지 않는다. 공식 원문은 “made available on the market with a secure by default configuration” 및 “limit attack surfaces”를 사용한다.

### A-005 — 2026-11-08_120059.md
**파일:** [원본](../research_archive/2026-11-08_120059.md)  
**SHA-1 blob:** `01e0e65e9f69be0aab15c5a75bd6a82f11d6e30d`

1. **신고 조항 번호 오류**
   - 문서가 Article 11로 기재했으나 제조자의 의무 신고 조항은 Article 14.
2. **신고 대상 과장**
   - Article 14 대상은 제품 내 actively exploited vulnerability 및 제품 보안에 영향을 주는 severe incident다.
   - 모든 취약점 발견을 Article 14 법정 신고 대상으로 일반화하지 않는다. Article 15는 자발적 신고와 구별된다.
3. **신고 시한 구분**
   - 적극 악용 취약점: 인지 후 24시간 이내 early warning, 72시간 이내 vulnerability notification, 시정/완화 조치가 제공된 후 14일 이내 final report.
   - 중대한 사고: 인지 후 24시간 이내 early warning, 72시간 이내 incident notification, 72시간 통지 후 1개월 이내 final report.
4. **신고 경로**
   - Article 14/16의 Single Reporting Platform을 통해 제조자 주된 EU 사업장 관할 CSIRT designated as coordinator에 통지하고 ENISA에도 동시에 접근 가능하도록 하는 구조다.
   - 단순히 “ENISA에 신고”라고만 쓰면 제출 경로와 수신기관을 빠뜨린다.
5. **제품 등급과 신고 의무**
   - Article 14 신고 의무를 Important Class II나 특정 기본 카테고리 제품에만 한정한다고 쓰지 않는다. 적용 범위에 속하는 제품의 제조자 신고 의무로 조항을 읽어야 한다.

## 1차 정정 우선순위

| 우선순위 | 조치 | 이유 |
|---|---|---|
| P0 | Article 11/14, Annex I/II, Part II 조항 번호 정정 | 법적 의무의 대상/위치 오류 |
| P0 | 직접 인용 원문 재작성 또는 인용 삭제 | 허위 원문 인용 방지 |
| P1 | SBOM 작성/공개/요청 제출 구분 | 과도한 공개 의무 설명 방지 |
| P1 | 지원기간 최소 5년 예외 및 업데이트 분리의 기술적 가능 조건 반영 | 조건 누락 방지 |
| P1 | 법문 의무와 설계 권고/구현 예시 분리 | 과장 및 오해 방지 |
| P2 | IEC 62443 연계 주장 별도 표준 원문 확인 | 표준 판본/조항 오기 방지 |

## 근거 출처
- EUR-Lex Regulation (EU) 2024/2847, Article 13: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- EUR-Lex Regulation (EU) 2024/2847, Article 14/16: same official text.
- EUR-Lex Regulation (EU) 2024/2847, Annex I Part I/II, Annex VII: same official text.
- European Commission, CRA reporting obligations (updated 2026-09-11): https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

## 한계
- 이 보고서는 초기 5개 파일만 수동 감사한 결과다.
- 990개 전수에서 플래그된 모든 주장에 대한 판정이 아니다.
- 제품별 적용성, 완제품 분류, 표준 적합성은 별도 검토해야 한다.
- 원본 파일은 보존하고 이 문서를 정정 이력/검증 레코드로 사용한다.
