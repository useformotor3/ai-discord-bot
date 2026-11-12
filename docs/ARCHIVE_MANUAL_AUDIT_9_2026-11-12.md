# CRA 조사 아카이브 추가 수동 감사 — 2026-11-12

**대상:** 2026-11-08~2026-11-11 자동 조사 파일 중 Article 10/11/14, 지원기간, Class I 및 적합성 평가 위험 후보 9개  
**기준 원문:** Regulation (EU) 2024/2847, EUR-Lex 공식 원문  
**분류 기준:** CONFLICT는 원문과 조항/인용/의무 범위가 충돌함. PARTIALLY_VERIFIED는 일부 일반 취지는 맞지만 법적 표현/범위가 부정확함.  
**원본 보존:** 아래 archive 원문은 수정하지 않는다.

## 1. 이번 감사의 주요 결과

이번 표본에서는 다음의 반복 오류를 추가로 확인했다.

1. CRA Article 10/11을 제조자 의무 또는 취약점 신고 조항으로 오인.
2. Article 14(3)을 무상 보안 업데이트/지원기간 조항으로 오인. Article 14(3)은 중대한 보안 사고 신고 조항이다.
3. Article 14 신고를 모든 취약점 신고로 확대. 법정 의무 대상은 actively exploited vulnerability와 severe incident로 구분된다.
4. Article 13(8)의 지원기간 결정과 Annex I Part II point (8)의 무상 보안 업데이트 제공을 혼동.
5. 서보 드라이브라는 제품명만으로 Important Class I이라고 단정.
6. CRA conformity assessment를 Article 24로 잘못 연결. Article 24는 open-source software stewards 의무이며, 제품 적합성 평가 절차는 Article 32다.
7. Article 32의 Class I 제3자 평가 조건을 누락하고 모든 Class I 제품에 무조건 Notified Body가 필요하다고 과장.

## 2. 파일별 감사

### A-006 — `2026-11-08_141043.md`
**SHA-1 blob:** `acf99bf357d8a20ee63191bed54007a33c03499d`  
**판정:** CONFLICT

- 문서는 Article 11을 제조자 의무 조항으로 설명한다. Regulation (EU) 2024/2847의 Article 11 제목은 General product safety이며, 제조자 일반 의무는 Article 13, 신고 의무는 Article 14에 있다.
- Annex I Part II의 취약점 처리/보안 업데이트 설명 자체는 일부 취지와 부합하지만, Article 11을 직접 근거로 연결한 것은 틀렸다.
- 자동 취약점 탐지·업데이트 배포는 설계 권고로 구체화할 수 있으나, 법문이 특정 CVE 감지 도구/자동화 주기를 강제한다고 쓰지 않는다.

### A-007 — `2026-11-08_191039.md`
**SHA-1 blob:** `be44fb28b96a0340781083a65766b5c3f80f4db4`  
**판정:** CONFLICT

- Article 10은 Enhancing skills in a cyber resilient digital environment다. 제조자 의무 조항이 아니며, 문서의 Article 10(6) 인용은 해당 Article 구조와 맞지 않는다.
- 제조자 의무는 Article 13이다. Article 13(8)은 지원기간 및 취약점 처리의 효과성을 규정하며, Annex I Part II point (8)은 보안 업데이트의 지체 없는 배포와 원칙적 무상 제공을 규정한다.
- Annex I Part I Paragraph 2(h)를 취약점 업데이트 근거로 인용했으나 Part I(2)(h)는 사고 이후 필수/기본 기능의 가용성 보호에 관한 항목이다. 취약점 처리는 Annex I Part II다.
- 원문 인용 Article 10(6)과 Annex I Part I 2(h)는 근거 위치가 잘못됐다.

### A-008 — `2026-11-09_012542.md`
**SHA-1 blob:** `f7ad83d4f5dba33b5ae45c6558039c2c493b2e77`  
**판정:** CONFLICT

- Article 14는 제조자 의무 일반 조항이 아니라 Reporting obligations of manufacturers다.
- Article 14(3)은 severe incident having an impact on the security of the product 신고다. 무상 업데이트 근거가 아니다.
- 취약점 처리 지원기간은 Article 13(8), 보안 업데이트의 무상 제공은 Annex I Part II point (8)에 연결해야 한다.
- Article 14(3)로 제시된 무상 업데이트 원문 인용은 공식 조항과 일치하지 않는다.
- “최소 5년” 표현은 제품의 예상 사용기간이 5년 미만일 때 그 예상 사용기간으로 정하는 예외를 반드시 포함해야 한다.

### A-009 — `2026-11-09_094606.md`
**SHA-1 blob:** `de2e2e8dcac750ff640288d39538bb3b66550eaf`  
**판정:** CONFLICT

- Article 13(8)은 제품의 예상 사용기간, 사용자 기대, 제품의 성격/의도된 목적 및 관련 EU 법령을 고려해 지원기간을 결정하도록 한다. 최소 5년 원칙과 예상 사용기간이 5년보다 짧을 때의 예외를 함께 읽어야 한다.
- 문서의 “최소 5년 또는 제품 예상 사용기간” 표현은 예외 관계가 명확하지 않고, 직접 인용은 Article 13(8)의 실제 문장과 정확히 일치하지 않는다.
- Annex I Part II point (2)는 취약점 해결과 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리하는 조항이다. 지원기간 산정 근거는 Annex VII point 4 및 Article 13(8)이다.

### A-010 — `2026-11-09_180532.md`
**SHA-1 blob:** `1ebf8cbe4ef51dead6dd316a46198c0662f4c3af`  
**판정:** CONFLICT

- 문서는 제로데이 취약점 일반 또는 모든 취약점 발견을 24시간/72시간 의무 신고 대상으로 서술한다.
- Article 14(1)–(2)의 법정 신고 대상은 actively exploited vulnerability다. severe incident는 Article 14(3)–(4)로 별도 규정한다.
- actively exploited vulnerability의 경우 24시간 이내 early warning, 72시간 이내 vulnerability notification, 최종 보고는 시정/완화 조치가 제공된 뒤 14일 이내다.
- severe incident의 final report는 incident notification 제출 후 1개월 이내다.
- 문서의 “72시간 이내 최종 신고 완료”는 vulnerability notification과 final report를 혼동한다.
- 신고는 Single Reporting Platform을 통해 CSIRT designated as coordinator로 제출하고 ENISA에 동시에 접근 가능하도록 해야 한다. 단순히 ENISA에 직접 신고한다고 축약하지 않는다.

### A-011 — `2026-11-10_110057.md`
**SHA-1 blob:** `3475c4af9d089509447b7db304ae4fad1012f3fc`  
**판정:** PARTIALLY_VERIFIED

- 제품의 취약점 처리 체계를 갖추고 제보를 받을 창구를 마련해야 한다는 일반 취지는 Annex I Part II point (5)–(6) 및 Article 13(17)과 부합한다.
- 그러나 “중요 디지털 요소에 속하는 서보 드라이브”라는 전제는 제품 핵심 기능과 Annex III/Implementing Regulation (EU) 2025/2392의 기술 설명 대조 없이 확정할 수 없다.
- “취약점 정보를 은폐해서는 안 된다”는 문구는 법령의 정확한 문장처럼 인용하지 말고, Annex I Part II point (4)의 패치 제공 후 취약점 정보 공개 의무 및 정당한 지연 예외를 구체적으로 설명해야 한다.
- 직접 인용은 원문 위치와 전체 문맥을 별도로 재검증해야 한다.

### A-012 — `2026-11-11_120102.md`
**SHA-1 blob:** `ab4fd2df609146138e55aaee537953697e7b872c`  
**판정:** CONFLICT

- Article 14(3)은 중대한 보안 사고 신고이지 지원기간이나 무상 업데이트 조항이 아니다.
- Article 13(8)은 지원기간 및 취약점 처리 의무를 규정한다. 무상 보안 업데이트는 Annex I Part II point (8)이다.
- Annex I Part I(2)(g)는 데이터 최소화, Part I(2)(h)는 필수/기본 기능 가용성 보호에 관한 항목이다. 취약점 업데이트를 Part I(2)(g)/(h)로 연결한 것은 잘못이다.
- Article 14(3), Annex I Part I(2)(g)/(h)로 제시한 원문 인용은 법적 근거 위치와 내용이 맞지 않는다.

### A-013 — `2026-11-11_230055.md`
**SHA-1 blob:** `a5a455e26367625b1a4c72896cd53cb34ab5ffab`  
**판정:** CONFLICT

- “산업용 서보 드라이브는 Annex III Class I”이라는 단정은 법령의 분류 기준을 충족하지 않는다. Article 7은 제품이 Annex III 카테고리의 core functionality를 갖는지 판단하도록 한다.
- Annex III Class I에는 security-related functionalities를 가진 microprocessors/microcontrollers 등이 포함된다. 이 항목은 해당 MCU 자체의 기능 및 제품 역할을 확인해야 하며, MCU가 통합됐다는 이유만으로 완제품 서보 드라이브가 자동 Class I이 되는 것은 아니다.
- Commission Implementing Regulation (EU) 2025/2392 recital (2)–(5)는 core functionality가 제품 분류를 결정하고, 단순 통합 부품만으로 완제품 분류가 자동 승격되지 않는다는 점을 설명한다.
- Article 24는 open-source software stewards 의무다. 제품 적합성 평가 절차는 Article 32다.
- Article 32(2)는 Class I 제품이 관련 조화표준/공통규격/적용 가능한 인증제도를 전부 적용하지 않았거나 존재하지 않는 경우 EU-type examination(Module B)+Module C 또는 full quality assurance(Module H)를 요구한다. “모든 Class I 제품은 무조건 Notified Body 심사”라고 일반화하지 않는다.

### A-014 — `2026-11-10_024038.md`
**SHA-1 blob:** `32c78e11c61885f5d7cb31a22f3dd8eeed1cfc64`  
**판정:** CONFLICT

- 최소 5년은 원칙이나, 제품 예상 사용기간이 5년보다 짧으면 그 예상 사용기간이 지원기간이다. “모든 제품 최소 5년”으로 단정하지 않는다.
- 무상 보안 업데이트는 Annex I Part II point (8)에 근거한다. Annex I Part I는 제품 속성에 관한 보안 요구사항이며 취약점 처리 요구사항은 Part II다.
- 보안 업데이트 분리는 Annex I Part II point (2)의 “where technically feasible” 조건이 붙는다. 무상 제공과 분리 제공은 서로 다른 요구사항이다.

### A-015 — `2026-11-10_192042.md`
**SHA-1 blob:** `7f94bcb3cf915106cee86c8608bf95b1684795cd`  
**판정:** PARTIALLY_VERIFIED

- 보안 업데이트의 출처 인증/무결성 검증 및 서명 기반 부트 체인은 서보 드라이브의 합리적인 설계 통제 예시가 될 수 있다. 다만 CRA 조문이 모든 제품에 특정 디지털 서명 알고리즘이나 구체 부트 체인 구현을 문자 그대로 지정한다고 표현하면 안 된다.
- Annex I Part I Section 2라는 위치 표기는 부정확하다. vulnerability handling은 Annex I Part II다.
- 인용문이 법령 원문과 정확히 일치하는지 추가 검증이 필요하다. Recital은 법적 요구사항 조항과 구분한다.

## 3. 제품 분류와 적합성 평가에 대한 핵심 정정

- Article 7(1): Annex III에 열거된 제품 카테고리의 **core functionality**를 가진 제품이 Important product로 분류된다.
- Implementing Regulation (EU) 2025/2392 recital (2)–(5): 제품 전체의 핵심 기능을 기술 설명과 대조한다. 통합된 구성요소가 별도 카테고리의 기능을 한다는 사실만으로 완제품이 그 카테고리로 자동 분류되지 않는다.
- Annex III Class I category 14: security-related functionalities를 갖춘 microcontrollers. 해당 기능이 MCU 자체를 넘어 다른 제품/네트워크/서비스를 보호하는 목적을 갖는지 확인한다.
- Annex III Class II category 4: tamper-resistant microcontrollers. 단순히 MCU에 암호 가속기가 있다는 이유로 이 분류를 단정하지 않는다.
- Article 24: open-source software stewards. Article 32: products with digital elements의 conformity assessment procedures.
- Article 32(2)의 Class I 제3자 평가 절차는 조화표준/공통규격/적용 가능한 사이버보안 인증제도의 적용 상황에 따라 조건부로 적용된다.

## 4. 공식 원문

1. Regulation (EU) 2024/2847 (EUR-Lex): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
   - Article 7(1)–(4): Important product core functionality 및 분류
   - Article 10: Enhancing skills
   - Article 11: General product safety
   - Article 13(8): support period 및 취약점 처리
   - Article 14(1)–(4): actively exploited vulnerability / severe incident 신고 및 기한
   - Article 24: open-source software stewards
   - Article 32(1)–(3): conformity assessment
   - Annex I Part II(1)–(8): SBOM, 취약점 처리, CVD, 안전한 업데이트 배포, 무상 업데이트
   - Annex III: Important products Class I/II
2. Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
   - Recital (2)–(5): core functionality 및 통합 구성요소와 완제품 분류의 구분
   - Annex I: Annex III 제품 카테고리의 기술적 설명

## 5. 검증 범위와 한계

- 이 보고서는 추가 9개 파일의 표본 수동 감사다. 990개 전체 오류율을 나타내지 않는다.
- 법령 조항/인용 오류가 확인된 파일은 원본을 보존하고 별도 정정대장에 기록한다.
- 제품의 실제 Class I/II 여부는 서보 드라이브의 정확한 제품 경계, 의도된 목적, 핵심 기능, 시장 제공 형태, 연결성, 포함된 보안 기능의 역할을 확인한 뒤 판단해야 한다.
- 이 문서는 법률 자문이나 제품 적합성 확정이 아니다.


## 6. ID·원본 파일 중복 정합성 보정 (2026-11-12)

후속 원본 파일 SHA-1 대조에서 이 보고서의 ID A-013과 추가 20개 감사 보고서의 B-006이 동일 원본 파일 `research_archive/2026-11-11_230055.md`, SHA-1 `a5a455e26367625b1a4c72896cd53cb34ab5ffab`임을 확인했다.

- 이 보고서에는 A-006~A-015의 10개 ID가 기재되어 있지만, A-013은 추가 20개 보고서 B-006과 중복이다.
- 따라서 이 배치의 고유 원본 파일은 9개다.
- ID 기준 판정은 8 CONFLICT / 2 PARTIALLY_VERIFIED이나, 중복 파일 A-013을 제외한 고유 파일 기준은 7 CONFLICT / 2 PARTIALLY_VERIFIED다.
- 전체 3개 배치의 고유 표본은 34개이며, 고유 파일 기준 누계는 25 CONFLICT / 9 PARTIALLY_VERIFIED다.
- 원본 감사 대상과 판정은 변경하지 않았고, 집계 중복만 명시했다.

상세 원본·SHA·정정 연결은 [ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md)를 참조한다.
