# CRA 보고서 #21 정정 및 DoS 가용성·자원 격리 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_114537400772_d80e7ac1.md
- 원본 blob SHA: e827b5396f655cb8d3fa4df3ee14a6e81d50ec09
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Annex I Part I (2)(h)가 resource isolation을 명시 | 원문에 없는 표현 | final OJ (2)(h)는 essential and basic functions availability, post-incident protection, resilience 및 DoS mitigation을 요구하지만 “isolation of resources” 문구는 포함하지 않는다 |
| CRA가 hardware/software resource isolation을 의무화 | 법적 요구를 특정 아키텍처로 확대 | CPU/DMA/buffer/priority-queue isolation은 DoS resilience를 달성하기 위한 구현 후보이지 조문이 지정한 방식이 아니다 |
| 모든 servo drive가 DoS 상황에서 STO로 천이해야 함 | 법적 근거 없음, 기능안전 위험 | CRA는 STO/SS1을 지정하지 않는다. 안전 기능 선택은 hazard analysis와 IEC 61800-5-2/기능안전 요구로 결정 |
| “essential functions”만 보호 | 문언 일부 누락 | final OJ는 “essential and basic functions”의 availability를 보호한다고 규정 |
| IEC 62443-4-2 CR 7.1/7.2를 CRA 의무처럼 표현 | 별도 표준 | DoS protection/resource management 표준 매핑은 edition, clause, product scope를 별도로 확인. CRA 문언과 혼합하지 않는다 |

## 2. 정확한 CRA 근거

Annex I Part I point (2)(h)는 제품이 사고 이후에도 essential and basic functions의 availability를 보호하고, DoS 공격에 대한 resilience 및 mitigation measures를 포함하도록 요구한다. 이 조항은 resource isolation이라는 특정 기술 아키텍처를 직접 요구하지 않는다.

Annex I Part I point (2)(f)는 stored/transmitted/processed data, commands, programs 및 configuration의 integrity에 관한 별도 요구다. (2)(h)와 혼합하지 않는다.

## 3. 수정된 권고 문안

제조사는 Article 13(2)의 위험평가에 따라 essential and basic functions의 availability를 보호하고 DoS 공격에 대한 resilience/mitigation measures를 설계해야 한다(Annex I Part I point (2)(h)). 서보 드라이브에서는 통신/관리 트래픽이 real-time control task, PWM update, watchdog 및 safety task의 CPU·DMA·buffer budget에 미치는 영향을 분석한다. 자원 격리, priority queueing, rate limiting 및 traffic filtering은 가능한 구현 후보이며, 특정 hardware/software isolation architecture가 CRA의 직접 의무라고 표현하지 않는다.

## 4. 기능안전 경계

- 통신 DoS/timeout 시 control hold, controlled stop, torque-off 및 brake behavior를 hazard analysis로 결정.
- STO는 토크 제거 기능이며 기계적 정지·하중 유지·수직축 낙하 방지를 자동 보장하지 않는다.
- STO/SS1 및 brake sequence는 IEC 61800-5-2/IEC 61508 및 제품 위험 분석으로 검증.
- 보안 자원 격리가 safety task jitter, interrupt latency, watchdog starvation 또는 safety communication timing을 악화시키지 않는지 측정.
- CRA availability 요구와 functional-safety 요구를 별도 traceability로 유지.

## 5. 공식 출처

- Official Journal Annex I: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text: https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
