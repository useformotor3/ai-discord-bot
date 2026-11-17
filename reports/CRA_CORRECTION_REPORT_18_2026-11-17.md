# CRA 보고서 #18 정정 및 접근제어·감사로그 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_113050521395_bc370668.md
- 원본 blob SHA: f986f2f2db5f74ca8dd072deb2fe90e013b4a63c
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| CRA가 least privilege를 직접 필수 요건으로 명시 | 공식 OJ 문언에서 확인되지 않음 | Annex I Part I (2)(d)는 적절한 control mechanisms, authentication, identity/access management systems 등을 규정하지만 least privilege 문구를 포함하지 않는다 |
| 원본 raw quote | 여러 조항을 혼합하고 법령에 없는 표현 추가 | Part I (2)(b), (2)(d), (2)(l)의 주제를 한 문장으로 합치고 “including the principle of least privilege”를 추가한 문구는 공식 원문 직접 인용이 아니다 |
| 초기 비밀번호 강제/MFA | 법령의 특정 구현 요구로 단정 불가 | secure-by-default 및 접근통제 요구를 충족하기 위한 설계 후보로 분류 |
| 성공·실패 인증 시도 전부 기록 | 범위를 과도하게 특정 | Part I (2)(l)는 관련 내부 활동의 기록·모니터링을 요구하며 접근 또는 데이터/서비스/기능 변경을 포함하지만, 모든 제품에 실패한 인증 시도까지 동일하게 명시하지 않는다 |
| ENISA IoT/IIoT 가이드 인용 | 문서 식별정보 불충분 | 제목·판본·발행일·정확한 URL·해당 절을 제시하기 전에는 근거로 사용하지 않는다 |

## 2. 정확한 CRA 근거

- Annex I Part I (2)(b): secure-by-default configuration 및 제품을 원래 상태로 재설정할 수 있는 기능.
- Annex I Part I (2)(d): 위험평가에 기초한 적절한 제어 메커니즘으로 무단 접근을 방지하며 authentication, identity/access management systems 등을 포함하고 가능한 무단 접근을 보고.
- Annex I Part I (2)(l): 관련 내부 활동을 기록·모니터링하며 데이터, 서비스 또는 기능에 대한 접근이나 변경을 포함하고 사용자 opt-out mechanism을 둔다.
- Article 13(2)–(3): 제품의 의도된 목적과 합리적으로 예견 가능한 사용, 운영 환경 및 보호 자산을 고려한 사이버보안 위험평가를 수행·문서화한다.

## 3. 수정된 권고 문안

제품은 Article 13(2)의 위험평가를 바탕으로 적절한 제어 메커니즘을 통해 무단 접근을 방지해야 하며, 인증 및 identity/access management systems 등을 사용할 수 있다(Annex I Part I (2)(d)). 또한 관련 내부 활동을 기록·모니터링해야 하며, 접근 또는 데이터·서비스·기능 변경이 포함된다(Part I (2)(l)). RBAC, least privilege, MFA, 개인별 계정, 비밀번호 정책 및 실패 인증 이벤트 로깅은 제품 위험과 아키텍처에 따라 선택할 구현 권고로 분류하고 CRA의 일률적 직접 의무로 표현하지 않는다.

## 4. 서보 드라이브 설계 시 추가 검토

- Operator, Maintenance, Engineering, Service 역할 및 원격/로컬 접속 경로를 자산·위협 모델에 포함.
- 파라미터 쓰기, 펌웨어 업데이트, 안전 관련 설정 변경의 권한 분리.
- 접근 로그는 누가, 언제, 어떤 인터페이스로, 어떤 데이터/기능에 접근·변경했는지 추적 가능하도록 설계.
- 실패 인증 시도 로깅, rate limit, lockout, MFA, unique initial credential은 위험 기반 설계 후보로 평가.
- 인증 장애 또는 권한 오류가 모션 제어 가용성 및 안전 기능에 미치는 영향은 별도 기능안전 검토.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
