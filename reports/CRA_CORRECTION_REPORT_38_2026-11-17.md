# CRA 보고서 #38 정정 — 취약점 지원기간·무상 업데이트 및 제품 분류

- 원본: `research_archive/2026-11-17_131544512153_7ae85554.md`
- 원본 blob SHA: `6ce0491de760c96a14bd3e7fce9e0683bb451deb`
- 원본 보존: 변경하지 않음
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 핵심 정정

1. Article 11은 General product safety이고 Article 10은 Enhancing skills in a cyber resilient digital environment다. 제조사 의무는 Article 13이며, Article 11/Annex I를 제조사의 지원기간·무상 업데이트 의무 근거로 인용하지 않는다.
2. 지원기간은 Article 13(8)에 따라 제품 예상 사용기간, 합리적 사용자 기대, 제품 성격 및 관련 EU 법령 등을 고려해 정한다. 최소 5년이 기본이나, 제품의 예상 사용기간이 5년 미만이면 그 예상 사용기간에 맞춘다. 원본의 '최소 5년 이상' 단정은 이 예외를 누락했다.
3. 보안 업데이트 무상 배포는 Annex I Part II (8)이다. 맞춤형 제품에 대해 제조사와 business user가 달리 합의한 예외가 있다.
4. 업데이트를 기능 업데이트와 기술적으로 가능한 경우 분리하는 근거는 Annex I Part II (2)다. Part II (7)은 취약점을 적시에 해결/완화하기 위한 안전한 배포 메커니즘이다.
5. Article 13(9)은 지원기간 중 배포된 보안 업데이트가 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능하도록 하는 별도 의무다. '5년 지원기간'과 혼합하지 않는다.
6. 일반 산업용 서보 드라이브가 Annex III Class I/II에 자동 포함된다는 근거는 없다. Annex III의 열거 카테고리와 제품의 core functionality를 기준으로 분류한다.
7. 원본의 Annex I Section 2 및 Article 11 인용은 final OJ의 정확한 구조와 다르다. 최종 Annex I는 Part I 및 Part II로 구성되고, 취약점 처리 요구는 Part II의 numbered points (1)–(8)이다.

## 수정 권고 문안

제품별 CRA 적용성과 Annex III 분류는 intended purpose 및 core functionality를 기준으로 별도 평가한다. 제조사는 Article 13(8)에 따라 예상 사용기간에 맞는 지원기간을 설정하고, 최소 5년 원칙 및 예상 사용기간이 더 짧은 경우의 예외를 적용한다. 취약점 처리는 Annex I Part II (2), 안전한 배포는 (7), 무상 업데이트는 (8)을 근거로 관리하고, Article 13(9)의 보안 업데이트 장기 이용 가능성은 별도 정책으로 관리한다.

## 공식 근거

- Article 10–11, Article 13(8)–(9)
- Annex I Part II (2), (7), (8)
- Annex III
- 공식 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
