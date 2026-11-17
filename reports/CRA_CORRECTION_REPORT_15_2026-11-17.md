# CRA 보고서 #15 정정 및 기술 구현 범위 감사

- 감사 대상 원본: research_archive/2026-11-17_110535023605_188807d2.md
- 원본 blob SHA: 43e08bf8394b6477bc3fd77030f1b0d594451110
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장 | 판정 | 정정 |
|---|---|---|
| Annex I Part I Section 2 Point (f) | 구조 표기 부정확 | 정확한 locator는 Annex I Part I point (2)(f) |
| 무단 변경 방지 및 corruption 보고 | 법적 근거 있음 | 해당 요건은 Article 13(2) 위험평가를 바탕으로 적용 |
| 모든 변조/손상을 실시간으로 상위 PLC에 즉시 보고 | 법령 문언 초과 | 법령은 corruption 보고를 요구하지만 실시간 전송, 특정 상위 PLC, 즉시 보고 방식까지 지정하지 않는다 |
| MAC/HMAC/CRC/OPC UA/CIP Security를 반드시 적용 | 구현 권고를 법적 의무로 과장 | 구체적인 보호 메커니즘은 위험평가와 제품 아키텍처에 따라 선택 |
| corruption 탐지 시 STO/Interlock 강제 트리거 | 안전 영향이 큰 과도한 단정 | CRA가 STO 트리거를 지정하지 않는다. 기능안전 분석 없이 자동 트립을 의무화하면 안 된다 |

## 2. 정확한 법령 요구

Annex I Part I point (2)(f)는 Article 13(2)의 사이버보안 위험평가에 근거해 저장·전송·처리되는 데이터, 명령, 프로그램 및 설정의 무단 조작/변경을 방지하고 corruption을 보고하도록 요구한다.

이 조항은 무결성 보호 결과와 corruption 보고를 규정한다. 특정 암호 알고리즘, 메시지 인증 코드, 체크섬, 통신 프로토콜, 상위 제어기 경보 형식, 실시간 응답시간 또는 안전정지 시퀀스를 직접 지정하지 않는다.

## 3. 서보 드라이브 설계에 대한 정정

법적 요구와 설계 권고를 분리한다.

- 법적 요구: 제품 위험평가에 기초한 명령/데이터/프로그램/설정 무결성 보호 및 corruption 보고.
- 구현 후보: 파라미터 접근제어, CRC 또는 MAC, secure boot, firmware signing, authenticated communication, audit log, controller alarm.
- 구현 후보의 선택은 공격모델, 통신 주기, 지연 허용치, CPU 부하, 안전 아키텍처, 제품 인터페이스에 따라 검증한다.
- corruption 탐지 시 동작은 안전 상태, 제어 연속성, 오탐 시 위험 및 복구 절차를 함께 분석한다. STO/SS1/Interlock 작동은 기능안전 요구·위험분석에서 결정하고 CRA 문언만으로 강제하지 않는다.

## 4. 수정된 권고 문안

서보 드라이브 제조사는 Article 13(2)의 제품별 사이버보안 위험평가를 바탕으로 모션 명령, 파라미터, 프로그램 및 설정의 무단 변경을 방지하고 corruption을 보고할 수 있는 메커니즘을 설계해야 한다(Annex I Part I point (2)(f)). CRC, MAC/HMAC, 서명 검증, 보안 로그 및 상위 제어기 진단은 가능한 구현 수단이며, 특정 수단 또는 STO 트리거가 모든 제품에 일률적으로 의무라고 단정하지 않는다.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
