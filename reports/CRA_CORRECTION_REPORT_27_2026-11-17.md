# CRA 보고서 #27 정정 — 취약점 공개·무상 업데이트와 Article 13/14 구분

- 원본: research_archive/2026-11-17_122038055293_bd72af22.md
- 원본 blob SHA: 99d226aeafd8e15d1fe53b6adda8051b3ab24519
- 원본 보존: 수정·삭제하지 않음

## 정정 사항
1. Article 10은 제조사 의무가 아니며 Article 13(8)이 support period 중 취약점 처리의 근거다.
2. CVD 정책은 Article 13(8)/Annex I Part II (5), 취약점 공유 연락 주소/조치는 Part II (6), 무상 보안 업데이트는 Part II (8)이다.
3. “취약점과 관련 정보를 사용자에게 지체 없이 무상 공개”는 잘못된 혼합이다. 무료 제공은 보안 업데이트의 배포를 의미하며, fixed vulnerability 공개는 Part II (4)의 업데이트 이후 공개 및 정당한 지연 조건을 따른다.
4. ENISA/국가기관에 모든 취약점을 즉시 신고한다는 주장은 잘못됐다. Article 14 mandatory reporting은 actively exploited vulnerability 및 product security에 영향을 주는 severe incident에 한정되며, 기타 취약점·위협·near miss는 Article 15 voluntary reporting 대상이 될 수 있다.
5. 서보 드라이브를 Important Product/Class I/II로 자동 분류할 수 없다. Annex III 카테고리별 판단이 필요하다.

## 수정 권고 문안
CVD 정책과 접수 창구는 Annex I Part II (5)/(6)에 맞춰 마련한다. 취약점은 Part II (2)에 따라 처리하고, 보안 업데이트는 (7)/(8)에 따라 안전하고 지체 없이 무상 배포한다(맞춤형 제품/business user 합의 예외). fixed-vulnerability 공개와 Article 14 신고는 별도 절차·시계로 운영한다.

## 공식 근거
- Article 13(8), 14–16
- Annex I Part II (2), (4)–(8), Annex III
- https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
