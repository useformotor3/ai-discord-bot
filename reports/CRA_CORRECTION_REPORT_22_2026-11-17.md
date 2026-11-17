# CRA 보고서 #22 정정 — Secure by Default와 기본 자격 증명

- 원본: research_archive/2026-11-17_115529848650_11a1a677.md
- 원본 blob SHA: ac97b06b1ef40763c2fea449e69dfdd38f66d619
- 원본 보존: 수정·삭제하지 않음

## 정정 사항
1. 최종 OJ Annex I Part I (2)(b)는 제품을 secure-by-default configuration으로 시장에 출시하고 초기 상태로 재설정할 수 있게 하도록 요구한다(맞춤형 제품에 대해 제조사와 business user가 달리 합의한 예외 포함).
2. Annex I Part I (2)(d)는 적절한 control mechanisms(인증, identity/access management 포함)에 의한 무단 접근 방지와 가능한 무단 접근 보고를 요구한다.
3. 원본의 “default credentials … changed easily and securely” 및 “initial access is restricted to the specific product unit through unique credentials or actions” 문구는 최종 OJ에서 확인되지 않는다. CRA 직접 인용으로 사용하면 안 된다.
4. 공장 공통 비밀번호 제거, 장치별 초기 비밀값, 최초 로그인 변경, QR/토큰 기반 초기 인증은 합리적인 설계 선택일 수 있으나 CRA가 구체 방식을 직접 지정하지 않는다.
5. Annex I Part I (2)는 Article 13(2) 위험평가를 바탕으로 “where applicable” 적용된다.

## 수정 권고 문안
서보 드라이브는 위험평가에 따라 secure-by-default 구성으로 제공하고 초기 상태 재설정 수단을 갖추며(Annex I Part I (2)(b)), 적절한 인증·ID·접근관리 수단으로 무단 접근을 방지하고 가능한 무단 접근을 보고해야 한다((2)(d)). 장치별 고유 초기 credential 및 최초 설정 흐름은 구현 선택으로 검토하되 CRA 직접 인용으로 표현하지 않는다.

## 공식 근거
- Article 13(2)–(4)
- Annex I Part I (2)(b), (d)
- https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
