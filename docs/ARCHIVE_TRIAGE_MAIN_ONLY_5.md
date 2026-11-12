# main 브랜치 전용 CRA 아카이브 5건 — 내용 표본 감사

**확인일:** 2026-11-12  
**검토 파일:** main에만 존재하는 자동 생성 조사 파일 5개  
**공식 기준:** Regulation (EU) 2024/2847, EUR-Lex  
**범위:** 주요 조항/인용 오류 식별. 전체 내용 전수 검증은 아님.

## 요약
5개 파일은 archive/history 연결은 정상이나 CRA 조항 위치 혼동과 원문과 다른 문장을 직접 인용처럼 표시한 문제가 반복된다. 모두 AI 자동 생성 초안으로 분류하며, 공식 보고서에 근거로 쓰기 전에 정정·검증해야 한다.

## A-279 — 업데이트 요건의 파트/점 및 인용 오류
파일: research_archive/2026-11-11_234543.md
- 기존: 무상 업데이트 및 안전 배포를 Annex I Part I point 2로 연결.
- 정정: 안전한 배포 메커니즘은 Annex I Part II point (7), 지체 없는 무상 보안 업데이트는 Part II point (8).
- Part I point (2)(c)의 해당되는 경우 자동 보안 업데이트 기본 활성화 요구와 구분한다.
- 직접 인용으로 제시한 문장은 공식 원문 그대로라고 확인되지 않으므로 인용 사용 금지.
- 판정: PARTIALLY_VERIFIED — 주제는 관련 있으나 조항/인용 정정 필요.

## A-280 — SBOM 및 기술문서 근거 혼동
파일: research_archive/2026-11-11_235047.md
- SBOM은 Annex I Part II point (1)에 규정.
- 기술문서는 Article 31 및 Annex VII 체계를 확인해야 한다. Annex II는 사용자 정보 및 지침이므로 기술문서 부속서로 인용하면 안 된다.
- 제3자 구성요소 실사는 Article 13(5)–(7)과 함께 검토한다.
- 판정: PARTIALLY_VERIFIED — SBOM 방향은 맞지만 기술문서 근거와 인용 위치 정정 필요.

## A-281 — 지원기간 조항 번호 및 표현 오류
파일: research_archive/2026-11-11_235547.md
- 기존: Article 14(3)을 지원기간 근거로 표시.
- 정정: 지원기간은 Article 13(8). Article 14는 제조자 신고 의무.
- 일반 원칙은 최소 5년. 제품의 예상 사용기간이 5년보다 짧으면 지원기간은 예상 사용기간에 맞춘다.
- 제품의 예상 사용기간, 합리적 사용자 기대, 제품 특성을 고려해야 하며 산업용 제어 제품의 장기 사용 특성도 고려한다.
- 판정: PARTIALLY_VERIFIED — 조항 번호와 법적 표현 정정 필요.

## A-001 — 무상 업데이트 조항 및 직접 인용 오류
파일: research_archive/2026-11-12_000106.md
- 기존: Article 13(4), Annex I Part I를 무상 업데이트 근거로 표시.
- 정정: 무상·지체 없는 보안 업데이트는 Annex I Part II point (8), 지원기간은 Article 13(8).
- 기존 따옴표 문구는 공식 원문과 일치하는 직접 인용으로 확인되지 않음.
- 판정: PARTIALLY_VERIFIED — 조항·인용 재작성 필요.

## A-002 — 취약점 공개 정책 및 업데이트 조항 혼동
파일: research_archive/2026-11-12_000539.md
- CVD 정책: Annex I Part II point (5)
- 취약점 신고 연락처: Part II point (6)
- 안전한 업데이트 배포: Part II point (7)
- 지체 없는 무상 보안 업데이트: Part II point (8)
- 직접 인용문은 원문과 일치 여부 확인 전 재사용 금지.
- 판정: PARTIALLY_VERIFIED — 요구 주제는 관련 있으나 조항 연결과 원문 인용 정정 필요.

## 공통 재발 방지
1. AI 생성 raw quote는 EUR-Lex 원문과 대조 전 신뢰하지 않는다.
2. Annex I Part I(제품 보안 속성)와 Part II(취약점 처리 프로세스)를 구분한다.
3. Article 13(8) 지원기간, Article 14 신고 의무, Annex I Part II point (8) 무상 업데이트를 혼동하지 않는다.
4. 원문 그대로 확인한 문장에만 인용부호를 사용한다.
5. archive 원본은 삭제/덮어쓰기하지 않고 정정 이력을 별도 관리한다.

## 공식 근거
EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 13(8): 지원기간 및 최소 5년 원칙/예상 사용기간 예외
- Article 14: 제조자의 취약점/중대 사고 신고
- Annex I Part II points (1)–(8): SBOM, 취약점 처리, CVD, 신고 채널, 업데이트 배포
- Annex II: 사용자 정보/지침
- Article 31 및 Annex VII: 기술문서
