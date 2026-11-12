# 서보 드라이브 보안 시험·증거 대장 — 초안

**기준일:** 2026-11-12  
**연결 문서:** [위협 모델](THREAT_MODEL_SERVO_DRIVE_CRA.md), [하드웨어 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md), [CRA 추적성 매트릭스](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md)  
**상태:** 시험 설계 초안 — 실제 제품 시험 미실시, 모든 결과 UNVERIFIED

## 1. 사용 규칙

- 아래 시험은 보안 설계 검증 후보이며, 법령이 이 특정 시험 절차·수치·도구를 직접 요구한다는 의미가 아니다.
- 시험 전 DUT SKU/HW revision/FW hash/MCU order code/silicon revision/설정/시험환경을 고정한다.
- 합격 기준의 수치(제어 지연, CPU 부하, packet rate, recovery time 등)는 제품 요구사항·위험평가·기능안전 분석에서 승인한 값으로 입력한다. 임의 수치를 만들지 않는다.
- 실행하지 않은 시험은 PASS로 표시하지 않는다. 기본 상태는 NOT_RUN / UNVERIFIED.
- 실패 시험도 원시 증거를 보존하고, 수정 후 재시험은 새로운 run ID로 연결한다.
- 생산장치 대상 시험은 안전한 시험환경/승인된 시험용 DUT에서 수행한다.

## 2. 증거 ID 및 파일명 규칙

권장 구조:
`evidence/<DUT_ID>/<FW_VERSION>/<TEST_ID>/<RUN_ID>_<ARTIFACT_TYPE>.<ext>`

필수 메타데이터:
- evidence_id, test_id, run_id, date/time/timezone
- DUT_ID, product SKU, HW revision, MCU order code/silicon revision
- FW version + cryptographic hash, bootloader version/hash
- test tool/version, test operator, setup/topology
- preconditions, exact steps, expected result, observed result
- raw artifact path/hash, verdict, deviations, reviewer

증거 ID 예:
- `EV-UPD-001-R01-LOG`
- `EV-NET-002-R01-PCAP`
- `EV-DBG-001-R01-CONFIG`
- `EV-AVL-001-R01-TRACE`

권장 보존 파일: UART/boot log, packet capture, fuzz corpus/seed, scope/logic-analyzer trace, MCU option-byte/config dump, signed image manifest, build hash, power interruption trace, test script/version, screenshots. 비밀키/실제 자격증명은 증거에 포함하지 않는다.

## 3. 시험 케이스

| Test ID | 연결 위협 | 목적/절차 요약 | 기대 결과(정성 기준) | 필요한 증거 | 상태 |
|---|---|---|---|---|---|
| TST-UPD-01 | TH-01 | 서명 없는 이미지 설치 시도 | 이미지 거부, 실행되지 않음 | EV-UPD log, image hash, boot log | NOT_RUN |
| TST-UPD-02 | TH-01 | 정상 이미지의 payload 1 bit 변조 | 진본성/무결성 검증 실패 | 원본/변조 hash, boot log | NOT_RUN |
| TST-UPD-03 | TH-01 | 서명/manifest 필드 불일치 | 검증 실패, 안전한 기존 상태 유지 | manifest, verifier log | NOT_RUN |
| TST-UPD-04 | TH-02 | 다른 제품/HW ID 이미지 설치 | 대상 불일치로 거부 | DUT identity, package manifest, log | NOT_RUN |
| TST-UPD-05 | TH-03 | 정책상 허용되지 않는 구버전 downgrade | 정책 위반 이미지 거부; 승인된 recovery 경로는 별도 확인 | version policy, boot state log | NOT_RUN |
| TST-UPD-06 | TH-04 | erase/write/swap 단계별 전원 차단 | 부팅 불능이 되지 않고 정의된 복구 상태로 진입 | power trace, boot log, flash state | NOT_RUN |
| TST-NET-01 | TH-05 | malformed frame/길이/경계값 입력 | crash, memory corruption, 임의 제어 없이 정상 거부 | PCAP, fuzz seed, crash log | NOT_RUN |
| TST-NET-02 | TH-05 | protocol parser fuzzing | 발견된 예외가 triage되고 재현 가능한 기록 확보 | corpus, tool config, coverage/crash log | NOT_RUN |
| TST-NET-03 | TH-05 | 비정상 연결/세션/요청 순서 | 상태기계 위반 없이 거부/복구 | PCAP, state log | NOT_RUN |
| TST-CMD-01 | TH-06 | 인증되지 않은 모션 명령 전송 | 권한 없는 명령 거부, 모션 명령 미반영 | PCAP, command audit log | NOT_RUN |
| TST-CMD-02 | TH-06 | 범위 밖/비정상 변화율 명령 | 승인된 범위/상태 검사에 의해 거부 또는 제한 | command trace, parameter config | NOT_RUN |
| TST-CMD-03 | TH-06 | 권한 없는 파라미터 쓰기 시도 | 권한 검사 실패, 설정 변경 없음 | before/after config hash, audit log | NOT_RUN |
| TST-CMD-04 | TH-07 | 유효 명령 재전송/순서 변경 | 제품 프로토콜의 replay/freshness 정책대로 거부 또는 처리 | PCAP, sequence/state log | NOT_RUN |
| TST-AVL-01 | TH-08 | 네트워크 트래픽 증가 단계별 부하 시험 | 승인된 제어 주기/지연/CPU/통신 기준 만족 | CPU/timing trace, PCAP | NOT_RUN |
| TST-AVL-02 | TH-08 | queue 포화/연결 폭주 | bounded resource 동작, 제어 경로 영향은 승인 한계 이내 | queue stats, timing trace | NOT_RUN |
| TST-AVL-03 | TH-08 | DoS 후 정상 트래픽 복귀 | 정의된 회복 조건과 시간 내 정상 복귀 또는 위험평가된 상태 | recovery log, timing trace | NOT_RUN |
| TST-SVC-01 | TH-09 | 비인증 서비스 포트 접근 | privileged 기능/설정 변경 거부 | service log, config hash | NOT_RUN |
| TST-SVC-02 | TH-09 | 낮은 권한으로 고권한 기능 호출 | least privilege 위반 없음 | role matrix, access log | NOT_RUN |
| TST-SVC-03 | TH-09 | 서비스 세션 종료 후 재접속/세션 재사용 | 인증·세션 정책 위반 없음 | service trace, session log | NOT_RUN |
| TST-DBG-01 | TH-10 | 양산 설정에서 SWD/JTAG/ROM boot 접근 시도 | 생산 정책에 따라 차단 또는 강하게 인증/제한 | option bytes/config dump, debug log | NOT_RUN |
| TST-DBG-02 | TH-10 | RMA/복구 경로의 권한·감사 확인 | 승인된 복구만 허용되고 추적 가능 | recovery procedure, audit record | NOT_RUN |
| TST-NVM-01 | TH-11 | 중요 설정/이미지 저장 데이터 변조 | 무결성 실패 검출 및 정의된 처리 | before/after dump hash, fault log | NOT_RUN |
| TST-NVM-02 | TH-11 | 외부 NVM 비인가 read/write | 설계된 접근통제/암호화 적용 확인 | bus trace, access test log | NOT_RUN |
| TST-NVM-03 | TH-11 | 저장 영역 경계/전원 차단 오류 주입 | 부팅/설정 일관성 유지 또는 안전한 복구 | fault trace, boot log | NOT_RUN |
| TST-KEY-01 | TH-12 | 장치 개인키/비밀정보 추출 경로 점검 | 비밀키 평문 노출이 설계 허용 범위에서 발생하지 않음 | key handling review, extraction test report | NOT_RUN |
| TST-KEY-02 | TH-12 | 개발/테스트 키가 생산 이미지에 포함되는지 검사 | 생산 artifact에 테스트 키/비밀 포함 없음 | build scan report, artifact hash | NOT_RUN |
| TST-KEY-03 | TH-12 | 키 교체·폐기·장치 RMA 시나리오 | 키 수명주기 절차와 복구가 일관됨 | key lifecycle record (secret-free) | NOT_RUN |
| TST-SNS-01 | TH-13 | 센서 단선/단락/범위 초과 주입 | 진단 검출 및 정의된 제어 반응 | fault injection trace, event log | NOT_RUN |
| TST-SNS-02 | TH-13 | feedback 값 spoofing/불연속 주입 | plausibility 검사가 비정상 입력을 검출/처리 | signal capture, control trace | NOT_RUN |
| TST-SNS-03 | TH-13 | feedback 통신 지연/누락 | 승인된 제어·고장 반응 한계 만족 | timing trace, fault log | NOT_RUN |
| TST-AUTH-01 | TH-14 | 역할별 허용/거부 기능 전수 확인 | 권한 매트릭스와 실제 결과 일치 | role matrix, test log | NOT_RUN |
| TST-AUTH-02 | TH-14 | 설정/권한 변경 감사 기록 확인 | 중요 변경의 actor/time/action/result 기록 | audit log, config diff | NOT_RUN |
| TST-AUTH-03 | TH-14 | 기본 계정/초기 비밀정보/초기화 상태 확인 | secure-by-default 정책 충족, 공통 기본 비밀 제거 | factory reset test, config dump | NOT_RUN |
| TST-LOG-01 | TH-15 | 로그 변조/삭제 시도 | 무결성/권한 정책에 따라 보호 또는 검출 | log hash, access test | NOT_RUN |
| TST-LOG-02 | TH-15 | 로그 저장공간 포화 | 정의된 순환/우선순위/알림 정책대로 동작 | saturation trace, log snapshot | NOT_RUN |
| TST-SUP-01 | TH-16 | release SBOM과 build dependency 비교 | 승인된 기준의 top-level dependency 누락 없음 | SBOM, build manifest, diff | NOT_RUN |
| TST-SUP-02 | TH-16 | 제3자 구성요소 취약점 접수 tabletop | triage·영향분석·수정·기록 책임/흐름 추적 | tabletop record, ticket timeline | NOT_RUN |
| TST-SUP-03 | TH-16 | 구성요소 버전·취약점 데이터 업데이트 | 제품 버전과 영향 판단이 추적 가능 | component inventory, advisory record | NOT_RUN |
| TST-OPS-01 | TH-17 | CVD 신고 접수부터 종결까지 모의 운영 | 접수·확인·조율·수정·공개 결정 기록 | CVD procedure, tabletop report | NOT_RUN |
| TST-OPS-02 | TH-17 | 지원기간·보안 업데이트 보존 정책 확인 | 지원기간 산정/종료일/업데이트 보존 정책 문서화 | support rationale, retention policy | NOT_RUN |
| TST-OPS-03 | TH-17 | Article 14 신고 판단 tabletop | actively exploited vulnerability와 severe incident를 구분하고 유형별 시한 적용 | incident decision log, timestamped exercise | NOT_RUN |
| TST-OPS-04 | TH-17 | 사용자 보안 공지/완화조치 통지 모의시험 | 영향 사용자 식별 및 통지 기록 확보 | advisory template, notification record | NOT_RUN |
| TST-REM-01 | TH-18 | 원격 서비스 기능/필수성/제품 경계 확인 | 실제 원격 기능과 제품 경계가 문서화됨 | data-flow map, product boundary record | NOT_RUN |
| TST-REM-02 | TH-18 | 원격 계정·세션 접근통제 시험(해당 시) | 승인된 사용자/권한만 접근 | auth test, access log | NOT_RUN |
| TST-REM-03 | TH-18 | 원격 경로 차단/서비스 장애 영향(해당 시) | 기능 필수성과 복구 영향이 위험평가와 일치 | network isolation test, recovery log | NOT_RUN |

## 4. 합격 기준 확정에 필요한 제품 수치

| Parameter ID | 필요한 값 | 값의 출처 | 상태 |
|---|---|---|---|
| PAR-01 | 모션 제어 주기/최대 허용 지터 | 제어 요구사항/시스템 검증 | UNVERIFIED |
| PAR-02 | 통신 부하 시 허용 CPU/메모리/queue 한계 | 성능 요구사항/위험평가 | UNVERIFIED |
| PAR-03 | 보안 이벤트/로그 저장 용량·보존 정책 | 제품 요구사항/운영 정책 | UNVERIFIED |
| PAR-04 | 업데이트 최대 허용 중단시간/복구시간 | 제품 요구사항/안전 분석 | UNVERIFIED |
| PAR-05 | 허용되는 서비스 접근 방식/인증 정책 | 제품 보안 요구사항 | UNVERIFIED |
| PAR-06 | 센서/엔코더 오류 검출 및 반응시간 | 제어/안전 요구사항 | UNVERIFIED |
| PAR-07 | 지원기간 및 보안 업데이트 보존 기준 | Article 13(8)/(9) 적용성 분석 | UNVERIFIED |

## 5. 테스트 결과 기록 양식

| 필드 | 기록 |
|---|---|
| Test ID / Run ID | TBD |
| DUT / SKU / HW revision | TBD |
| MCU order code / silicon revision | TBD |
| FW / bootloader version + hash | TBD |
| Test tool / version | TBD |
| Setup / topology | TBD |
| Preconditions | TBD |
| Steps / input vector | TBD |
| Expected result / approved acceptance criteria | TBD |
| Observed result | TBD |
| Evidence IDs / SHA-256 | TBD |
| Verdict | NOT_RUN |
| Deviation / defect ID | TBD |
| Reviewer / date | TBD |

## 6. 상태 전이 규칙

- NOT_RUN: 시험 미실시.
- FAIL: 승인된 합격 기준 위반.
- PASS: 승인된 기준과 재현 가능한 증거가 모두 존재.
- BLOCKED: DUT/부품/환경/합격 기준 미확정으로 실행 불가.
- NOT_APPLICABLE: 제품 경계/설계 근거로 시험 비적용이 승인됨.
- PASS는 자동으로 CRA 적합성 결론이 아니다. 요구사항별 적용성 및 증거 검토가 별도 필요하다.
