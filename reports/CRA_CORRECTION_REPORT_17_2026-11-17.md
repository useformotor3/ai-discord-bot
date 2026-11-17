# CRA 보고서 #17 정정 및 접근제어 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_112534776361_67095946.md
- 원본 blob SHA: aed767bf716b2f1b7e830e9c2cdc6cdc3cf69394
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| CRA가 least privilege 및 RBAC를 직접 명시 | 원문 근거 없음 | Annex I Part I point (2)(d)는 적절한 control mechanisms, authentication, identity/access management systems 등을 규정하지만 least privilege/RBAC를 직접 명시하지 않는다 |
| 원본의 긴 직접 인용문 | 공식 OJ에서 확인되지 않음 | 해당 문구는 CRA 직접 인용으로 사용할 수 없다. 원문과 일치하는 인용으로 교체 |
| 하드코딩 비밀번호 금지 | 직접적인 보편 금지 문언 확인 불가 | secure-by-default 및 무단 접근 방지 요구에 맞춰 제품 위험평가와 보안 설계에서 다루되, CRA가 모든 제품에 특정 비밀번호 정책을 직접 지정한다고 단정하지 않는다 |
| MFA 의무 | 특정 구현 의무 아님 | MFA는 인증 강화를 위한 구현 후보이며 제품 위험평가에 따라 선택 |
| 세션 timeout 및 EtherCAT/PROFINET/Modbus TCP별 RBAC | 직접 명시 의무 아님 | 제품별 인터페이스·위험·기능안전 영향을 고려한 엔지니어링 권고로 분류 |

## 2. 정확한 CRA 근거

Annex I Part I point (2)(d)는 Article 13(2) 위험평가에 근거해 제품이 적절한 제어 메커니즘을 통해 무단 접근으로부터 보호되도록 요구한다. 예시로 authentication 및 identity/access management systems를 포함하며, 가능한 무단 접근을 보고하도록 규정한다.

이는 접근 통제 기능의 법적 결과를 요구하는 조항이다. 그러나 법령은 모든 제품에 RBAC, least privilege, MFA, 자동 세션 timeout 또는 하드코딩 비밀번호 전면 금지를 동일한 문장으로 직접 요구하지 않는다.

## 3. 서보 드라이브 설계에 대한 정정

- 법적 요구: 위험평가 기반 적절한 무단 접근 통제, 인증/identity/access management 수단 고려, 가능한 무단 접근 보고.
- 구현 후보: RBAC, least privilege, MFA, 개인별 계정, privileged session 제한, timeout, 감사 로그, 프로토콜별 권한 분리.
- 구현 후보는 Operator/Maintenance/Engineering/Service 역할, 로컬 HMI, 엔지니어링 포트, 원격 유지보수, 산업용 네트워크 및 안전 파라미터 변경 위험을 분석해 선정한다.
- EtherCAT, PROFINET, Modbus TCP 등 프로토콜 이름 자체가 CRA의 개별 접근제어 의무를 만드는 것은 아니다.
- 권한 오류·세션 종료·인증 장애가 안전 관련 설정, 모션 제어 가용성 또는 복구에 미치는 영향은 별도 기능안전 검토가 필요하다.

## 4. 수정된 권고 문안

제품은 Article 13(2)의 위험평가에 근거해 적절한 제어 메커니즘으로 무단 접근을 방지하고, 인증 및 identity/access management 시스템 등을 활용하며, 가능한 무단 접근을 보고해야 한다(Annex I Part I point (2)(d)). RBAC, least privilege, MFA 및 세션 timeout은 제품 위험과 사용 시나리오에 맞춰 선택할 수 있는 구현 권고이며, 법령이 모든 제품에 일률적으로 지정한 특정 기능으로 표현하지 않는다.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
