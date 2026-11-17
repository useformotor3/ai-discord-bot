# CRA 보고서 #19 정정 및 로깅·감사추적 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_113532369725_9840a64e.md
- 원본 blob SHA: 3d90ed95b47d6275e4d98d7c18cfbc5246ffa4e4
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| logging 근거를 Annex I Part I Section 1(h)로 표기 | 조항 오류 | logging/monitoring은 Annex I Part I point (2)(l). point (2)(h)는 essential/basic function availability 관련 |
| update quote를 point (h)로 표기 | 조항 오류 및 비문언 인용 | 취약점 보안 업데이트는 Part I point (2)(c); (h)는 availability |
| “Products ... referred to in Article 10(1) to (5)” 및 user-account create/modify/delete 문구 | 최종 OJ에서 확인되지 않는 인용 | 현재 Official Journal Annex I Part I (2)(l)의 문언과 다르며 직접 인용으로 사용할 수 없음 |
| 모든 인증 실패, 권한 상승, 펌웨어 검증 실패 등을 반드시 로그 | 요구 범위 과도 특정 | 법령은 관련 내부 활동을 기록·모니터링하며 데이터/서비스/기능 접근·변경을 포함한다고 규정. 개별 이벤트 유형은 제품 위험평가 및 구현 설계에서 결정 |
| tamper-proof logs, circular buffer, remote SIEM telemetry를 법적 의무처럼 표현 | 구현 권고를 법적 의무로 확대 | 로그 보호·용량·전송 방식은 보안 설계 권고이며, CRA 조문이 특정 방식이나 프로토콜을 직접 지정하지 않음 |

## 2. 정확한 CRA 근거

- Annex I Part I point (2)(l): 제품은 관련 내부 활동을 기록하고 모니터링하여 보안 관련 정보를 제공해야 한다. 여기에는 데이터, 서비스 또는 기능에 대한 접근이나 변경이 포함되며, 사용자 opt-out mechanism도 규정한다.
- Annex I Part I point (2)(c): 취약점이 보안 업데이트로 처리될 수 있도록 해야 하며, 해당되는 경우 자동 업데이트 기본 설정, 적절한 설치 시기, opt-out, 업데이트 통지 및 임시 연기 선택을 규정한다.
- Annex I Part I point (2)(h): 사고 이후를 포함해 essential/basic functions의 가용성을 보호하는 요구다. 로깅 조항이 아니다.
- Annex I Part I point (2)(d)/(f): 무단 접근 통제 및 데이터·명령·프로그램·설정 무결성 요구를 로그 보호 설계와 연계할 수 있으나, 특정 로그 저장·전송 구조를 직접 규정하지 않는다.

## 3. 수정된 권고 문안

제품은 보안 관련 정보를 제공하기 위해 관련 내부 활동을 기록·모니터링해야 하며, 여기에는 데이터, 서비스 또는 기능에 대한 접근이나 변경이 포함된다(Annex I Part I point (2)(l)). 어떤 이벤트를 기록할지, 로그 무결성 보호, 시간 동기화, 저장 용량, 원격 수집 및 보존 기간은 제품 위험평가와 운영 요구에 따라 설계한다. 실패 인증 시도, 권한 변경, 펌웨어 업데이트, 주요 파라미터 변경, 보안 fault 등은 합리적인 이벤트 후보지만 CRA가 모든 항목을 동일한 방식으로 일률적으로 열거한 것은 아니다.

## 4. 서보 드라이브 설계 시 권고

- 보안 이벤트와 기능안전 fault를 구분하되, 상호 연관성을 분석할 수 있도록 timestamp와 event ID를 설계.
- 파라미터 변경, 펌웨어 업데이트, 계정/권한 변경, service/debug access, 인증 이벤트의 기록 필요성을 위험평가.
- 로그 저장 공간 부족, flash wear, 로그 삭제/변조, 시간 동기화 손실, 원격 전송 단절 및 SIEM 장애 시 제어 기능 영향 검토.
- 로그 전송은 EtherCAT/PROFINET 등 제어주기 트래픽과 분리하거나 영향 분석을 수행. 특정 프로토콜을 CRA 직접 의무로 단정하지 않는다.
- 로그 기능이 실시간 모션 제어 및 SIL 안전 기능의 timing/resource budget을 침해하지 않는지 별도 검증.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
