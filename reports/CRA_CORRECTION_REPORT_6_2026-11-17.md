# CRA 보고서 #6 정정 및 DoS/가용성 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_090739340595_c5f72f7a.md
- 원본 blob SHA: 34de32d788d55790606193b86c355d5d7a279845
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Annex I Part I Section 1 points (f)/(h) | 구조 및 locator 오류 | 최종 OJ Annex I Part I (2)(h)가 availability/DoS 요구. (2)(f)는 data/command/program/configuration integrity |
| point (1)(f) DoS resilience | 구판/초안 구조 혼입 | final OJ point (2)(h)는 essential and basic functions availability 및 DoS resilience/mitigation |
| 모든 서보 드라이브에 dual-core/MPU-DSP 물리 분리 의무 | 법령이 특정 아키텍처를 지정하지 않음 | 통신/제어 자원 격리는 구현 후보이며 제품 위험·실시간 성능 분석으로 결정 |
| hardware rate limiting, storm control, packet drop 필수 | 구현 수단 과잉 단정 | CRA는 availability 보호 결과를 요구하지만 MAC/스위치 기능 및 특정 필터링 방식은 지정하지 않는다 |
| DoS/통신 timeout 시 STO/SS1 자동 수행 | CRA 직접 의무 아님, 기능안전 위험 존재 | 안전 상태 전이는 hazard analysis, IEC 61800-5-2/기능안전 요구 및 제품 위험평가로 결정. CRA DoS 문구만으로 STO를 일률 강제하지 않는다 |
| “essential functions”만 보호 | 문언 일부 누락 | final OJ는 “essential and basic functions”라고 규정 |

## 2. 정확한 법적 근거

Annex I Part I point (2)(h)는 제품이 사고 이후에도 essential and basic functions의 가용성을 보호해야 하며, DoS 공격에 대한 resilience 및 mitigation measures를 포함하도록 규정한다. 이 요구는 Article 13(2)의 제품별 cybersecurity risk assessment에 기초한다.

동일 Annex I Part I point (2)(f)는 data, commands, programs 및 configuration의 integrity를 다루는 별도 요구다. point (2)(f)를 DoS 조항으로 인용하지 않는다.

## 3. 수정된 권고 문안

제조사는 제품 위험평가를 바탕으로 사고 이후에도 essential and basic functions의 가용성을 보호하고 DoS 공격에 대한 resilience/mitigation measures를 설계해야 한다(Annex I Part I point (2)(h)). 서보 드라이브에서는 통신 스택 부하가 실시간 제어 태스크, PWM 업데이트, watchdog 및 안전 기능에 미치는 영향을 분석하고, 우선순위·자원 격리·트래픽 제한·비정상 패킷 처리 등을 적절한 구현 후보로 검토한다. 구체적인 dual-core 구조, rate limit 값, packet drop policy 및 STO/SS1 전이는 법령이 지정한 단일 방식이 아니다.

## 4. 서보 드라이브 적용 시 안전 설계 주의

- DoS로 필드버스 통신이 끊길 때 제어 유지, controlled stop, torque-off 등 동작을 hazard analysis로 결정.
- STO는 토크를 제거하지만 기계적 정지·하중 유지·수직축 낙하 방지를 보장하는 일반적인 정지 방식이 아니다. 필요 시 SS1, brake control, safe operating stop 등 적절한 안전 기능을 검토.
- 보안 이벤트 처리로 실시간 task jitter, interrupt latency, watchdog starvation 또는 safety task starvation이 발생하지 않는지 측정.
- 네트워크 필터링은 정상 제어 프레임/진단 트래픽을 차단하지 않도록 worst-case traffic과 fault injection으로 검증.
- CRA availability 요구와 IEC 61800-5-2/IEC 61508 기능안전 요구는 별도 traceability로 관리.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
