# main 자동 생성 CRA 아카이브 6건 — 표본 감사

**확인일:** 2026-11-12  
**검토 파일:** main에서 추가 생성되어 작업 브랜치로 복사한 6개 조사 파일  
**공식 기준:** Regulation (EU) 2024/2847, EUR-Lex  
**범위:** 주요 조항/인용 오류 식별. 6개 파일의 모든 문장 또는 전체 아카이브 전수 검증은 아님.

## 요약
6개 파일은 archive/history 연결은 정상이나 CRA 조항 위치 혼동, 공식 원문과 다른 문장을 직접 인용처럼 표시, 제품 분류의 근거 없는 단정이 반복된다. 모두 AI 자동 생성 초안으로 취급한다.

## A-279 — 업데이트 요건 파트/점 및 인용 오류
파일: research_archive/2026-11-11_234543.md
- 기존: 무상 업데이트/안전 배포를 Annex I Part I point 2로 연결.
- 정정: 안전한 배포는 Annex I Part II point (7), 지체 없는 무상 보안 업데이트는 Part II point (8).
- Part I point (2)(c)의 해당되는 경우 자동 보안 업데이트 기본 활성화 요구와 구분한다.
- 직접 인용으로 제시한 문장은 공식 원문과 일치한다고 확인되지 않음.
- 판정: PARTIALLY_VERIFIED.

## A-280 — SBOM/기술문서 근거 혼동
파일: research_archive/2026-11-11_235047.md
- SBOM은 Annex I Part II point (1).
- 기술문서는 Article 31 및 Annex VII. Annex II는 사용자 정보 및 지침이다.
- 제3자 구성요소 실사는 Article 13(5)–(7)과 함께 검토한다.
- 판정: PARTIALLY_VERIFIED.

## A-281 — 지원기간 조항 번호 및 표현 오류
파일: research_archive/2026-11-11_235547.md
- 지원기간 근거는 Article 14(3)이 아니라 Article 13(8). Article 14는 신고 의무.
- 일반 원칙은 최소 5년. 예상 사용기간이 5년보다 짧으면 지원기간은 그 예상 사용기간에 맞춘다.
- 판정: PARTIALLY_VERIFIED.

## A-001 — 무상 업데이트 조항 및 직접 인용 오류
파일: research_archive/2026-11-12_000106.md
- Article 13(4)/Annex I Part I를 무상 업데이트 근거로 표시한 것은 부정확.
- 무상·지체 없는 보안 업데이트는 Annex I Part II point (8), 지원기간은 Article 13(8).
- 직접 인용문은 공식 원문과 일치한다고 확인되지 않음.
- 판정: PARTIALLY_VERIFIED.

## A-002 — CVD 및 업데이트 조항 혼동
파일: research_archive/2026-11-12_000539.md
- CVD 정책: Annex I Part II point (5)
- 취약점 신고 연락처: point (6)
- 안전한 업데이트 배포: point (7)
- 지체 없는 무상 업데이트: point (8)
- 직접 인용문은 원문 대조 전 재사용 금지.
- 판정: PARTIALLY_VERIFIED.

## A-003 — 지원기간·업데이트 조항 및 제품 분류 오류
파일: research_archive/2026-11-12_001038.md
- 기존: 지원기간/취약점 처리 근거를 Article 14로 표시하고, 서보 드라이브를 Class I 또는 Class II 제품으로 일반화.
- 정정: 지원기간은 Article 13(8), Article 14는 적극 악용 취약점 및 중대한 보안 사고 신고 의무.
- Article 13(8)은 예상 사용기간을 반영하고, 일반적으로 최소 5년. 예상 사용기간이 5년보다 짧으면 그 기간에 맞춘다.
- Annex I Part II point (8)은 보안 업데이트를 지체 없이 제공하고 원칙적으로 무상 제공하는 요구다. 기존 인용문에 있는 Article 14(3), Annex I Part II paragraph 1(5) 문구는 실제 원문과 일치하지 않는다.
- 서보 드라이브라는 이름만으로 Important Class I/II라고 단정할 수 없다. Article 7, Annex III 및 관련 기술 정의를 완제품의 core functionality에 대조해야 한다.
- 판정: PARTIALLY_VERIFIED.

## 공통 재발 방지
1. AI 생성 raw quote는 EUR-Lex 원문과 대조 전 신뢰하지 않는다.
2. Annex I Part I(제품 보안 속성)와 Part II(취약점 처리 프로세스)를 구분한다.
3. Article 13(8) 지원기간, Article 14 신고 의무, Annex I Part II point (8) 무상 업데이트를 혼동하지 않는다.
4. 원문 그대로 확인한 문장에만 인용부호를 사용한다.
5. 제품 분류는 제품명만으로 추정하지 않는다.
6. 원본 archive는 삭제/덮어쓰기하지 않고 정정 이력을 별도 관리한다.

## 공식 근거
EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 7: Important products의 core functionality 및 Annex III 분류
- Article 13(8): 지원기간
- Article 14: 제조자의 신고 의무
- Annex I Part II (1)–(8): SBOM 및 취약점 처리
- Annex II: 사용자 정보/지침
- Article 31 및 Annex VII: 기술문서
