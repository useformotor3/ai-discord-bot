# 서보 드라이브 CRA 보안 위협 모델 — 일반 참조 모델

**기준일:** 2026-11-12  
**기준 브랜치/커밋:** `cra-project-foundation` / `25b643ded575a5407c986defea74900a3a673ad7`  
**상태:** 일반 참조 모델 초안 — 제품별 적용성/위험도/통제 구현은 UNVERIFIED  
**범위:** 네트워크·서비스 인터페이스가 있는 임베디드 서보 드라이브의 자산, 공격자, 신뢰 경계, 위협 시나리오 및 설계 통제 후보

> 이 문서는 실제 제품 위험평가가 아니다. 실제 SKU, intended purpose, 네트워크 토폴로지, 안전 아키텍처, MCU 주문 코드가 없으므로 공격 가능성·영향·위험 등급을 확정하지 않는다. 아래 STRIDE 분류와 통제는 분석 프레임/설계 후보이지 CRA가 특정 회로나 알고리즘을 직접 명령한다는 뜻이 아니다.

## 1. 모델링 가정과 시스템 경계

가정한 논리 구성요소:
- 외부 산업용 Ethernet/fieldbus 및 상위 PLC/HMI/engineering PC
- PHY/transceiver와 통신 스택/게이트웨이 도메인
- 모션 제어 MCU, boot chain, application firmware, control loop
- 내부/외부 NVM, 파라미터·설정·로그
- USB/UART/service connector, SWD/JTAG/ROM boot/debug
- encoder/resolver/sensor feedback
- gate driver/power stage 및 전원/reset supervisor
- 제조 프로비저닝 스테이션, 펌웨어 배포·서명 환경
- 선택적 secure element 및 선택적 원격 서비스/클라우드

제품에 존재하지 않는 블록은 제품 경계 검토 후 NOT_APPLICABLE로 처리한다. 클라우드, 무선, 외부 NVM, secure element는 존재한다고 가정하지 않는다.

## 2. 보호 자산(Asset Register)

| Asset ID | 자산 | 보안 속성 | 손상 시 잠재 영향 | 확인 증거 |
|---|---|---|---|---|
| AST-01 | 펌웨어 이미지/boot chain | 진본성·무결성·가용성 | 비인가 코드 실행, 부팅 불능 | boot map, image manifest, boot test |
| AST-02 | 서명 신뢰 앵커/장치 개인키 | 기밀성·무결성·수명주기 | 위조 업데이트, 장치 사칭 | key hierarchy, provisioning record |
| AST-03 | 모션 명령(위치/속도/토크) | 진본성·무결성·신선도 | 예기치 않은 움직임/공정 손상 | protocol spec, command auth tests |
| AST-04 | 모터·엔코더 피드백 | 진본성·무결성·가용성 | 잘못된 제어 입력/성능 저하 | feedback interface spec, fault tests |
| AST-05 | 안전 관련 설정/한계 파라미터 | 무결성·접근통제 | 위험한 설정 변경 | parameter map, access matrix |
| AST-06 | 사용자·서비스 자격증명/역할 | 기밀성·무결성 | 권한 탈취·오용 | identity lifecycle, auth test |
| AST-07 | 네트워크/서비스 인터페이스 | 가용성·접근통제 | DoS, 비인가 서비스 진입 | interface inventory, scan |
| AST-08 | 취약점/로그/감사 기록 | 무결성·가용성·추적성 | 사고 분석 실패, 대응 지연 | log spec, SBOM, PSIRT records |
| AST-09 | 생산·서명·프로비저닝 자산 | 기밀성·무결성·진본성 | 생산 키 유출, 공급망 공격 | factory security procedure |
| AST-10 | 업데이트/복구 기능 | 진본성·무결성·가용성 | 악성 펌웨어, 벽돌화, 복구 실패 | update state machine, recovery tests |

## 3. 공격자 및 능력 가정

| Actor ID | 공격자 유형 | 가능한 접근/능력(가정) | 모델링 유의점 |
|---|---|---|---|
| ACT-01 | 원격 네트워크 공격자 | reachable protocol endpoint에 비정상 패킷/요청 전송 | 실제 routability, 방화벽, segmentation 확인 필요 |
| ACT-02 | 같은 산업망의 악성/침해 호스트 | 정상 프로토콜 메시지 위조·재전송·폭주 | 인증/권한/세션 신선도 확인 |
| ACT-03 | 현장 물리 접근자 | 서비스 포트·디버그 패드·저장매체 접근 | 접근통제·봉인·제품 설치환경 확인 |
| ACT-04 | 권한을 가진 운영자/서비스 계정 오용 | 합법 계정으로 과도한 설정·업데이트 실행 | 최소권한·승인·감사 추적 |
| ACT-05 | 공급망/생산 공정 공격자 | 구성요소, 빌드, 서명키, 생산 스테이션 침해 | 공급업체/빌드 파이프라인 증거 필요 |
| ACT-06 | 취약점 연구자/선의의 신고자 | 취약점 발견·신고 | CVD 프로세스 및 연락처 접근성 확인 |

공격자 능력은 분석 시나리오이며 특정 제품의 실제 노출을 뜻하지 않는다.

## 4. 신뢰 경계(Trust Boundary)와 통제 지점

| TB ID | 경계 | 비신뢰 입력/영역 | 경계 통과 조건 후보 | 관련 자산 |
|---|---|---|---|---|
| TB-01 | 외부 네트워크 → 통신 스택 | Ethernet/fieldbus 프레임, discovery, 관리 요청 | 파서 검증, 길이/상태 검사, rate limit | AST-03, AST-07 |
| TB-02 | 통신 도메인 → 모션 제어 | 명령/파라미터 쓰기/상태 전환 요청 | 인증·권한·범위·상태·속도 제한 | AST-03, AST-05 |
| TB-03 | 외부 업데이트 → boot chain | 이미지, manifest, 버전, 전송 매체 | 제품 ID/서명/무결성/버전 정책 검증 | AST-01, AST-10 |
| TB-04 | 서비스·디버그 포트 → privileged 기능 | UART/USB/SWD/JTAG/ROM boot | 생산 lifecycle 정책, 인증 서비스, 권한 분리 | AST-01, AST-02, AST-05 |
| TB-05 | MCU ↔ NVM | 저장 이미지, 파라미터, 로그, 키 | 접근통제, 무결성, 비밀 데이터 기밀성 | AST-01, AST-02, AST-05 |
| TB-06 | 제조 스테이션 → 장치 | 장치 ID, trust anchor, 펌웨어 | 스테이션 인증, 승인된 작업, 장치별 추적 | AST-02, AST-09 |
| TB-07 | 제어 MCU → gate driver/power stage | PWM/enable/fault 신호 | 리셋/고장 시 정의된 출력 상태, 별도 안전 분석 | AST-03, AST-04 |
| TB-08 | 제품 ↔ 원격 서비스(존재 시) | 진단/업데이트/원격 명령 데이터 | 제품 기능 필수성, 상호 인증, 최소 데이터 | AST-06, AST-07, AST-10 |

## 5. 위협 시나리오 및 대응 후보

위험도는 제품별 사실과 위험평가가 없어 산정하지 않는다. 우선순위는 시험 선행 순서이며 위험 등급이 아니다.

| Threat ID | 공격 시나리오 | STRIDE | 영향 자산 | 통제 후보 | 시험/증거 연결 |
|---|---|---|---|---|---|
| TH-01 | 서명되지 않았거나 변조된 펌웨어 실행 | Spoofing/Tampering | AST-01, AST-10 | 신뢰 앵커 기반 이미지 진본성·무결성 검증 | TST-UPD-01..03 |
| TH-02 | 다른 SKU/보드용 이미지 설치 | Tampering | AST-01 | target product/HW ID 검사 | TST-UPD-04 |
| TH-03 | 취약한 구버전으로 rollback | Tampering | AST-01, AST-10 | 버전 정책/rollback 예외 승인·복구 정책 | TST-UPD-05 |
| TH-04 | 업데이트 중 전원 차단으로 부팅 불능 | Denial of Service | AST-01, AST-10 | 원자적 상태 전이, 복구 슬롯/절차 | TST-UPD-06 |
| TH-05 | 네트워크 파서의 길이/상태 취약점 악용 | Tampering/DoS/EoP | AST-03, AST-07 | 경계 검사, 안전한 파서, fuzzing | TST-NET-01..03 |
| TH-06 | 인증되지 않은 위치/속도/토크 명령 주입 | Spoofing/Tampering | AST-03 | 명령 출처 인증, 권한·상태·범위 검증 | TST-CMD-01..03 |
| TH-07 | 명령 재전송/순서 바꾸기 | Spoofing/Replay | AST-03 | sequence/nonce/time-window 등 프로토콜 적합 통제 | TST-CMD-04 |
| TH-08 | 패킷 폭주로 제어 주기/통신 가용성 저하 | DoS | AST-03, AST-07 | bounded queue, rate limit, task isolation | TST-AVL-01..03 |
| TH-09 | 서비스 포트로 비인가 파라미터/펌웨어 변경 | EoP/Tampering | AST-01, AST-05, AST-06 | 생산/서비스 권한 분리, 인증, 감사 로그 | TST-SVC-01..03 |
| TH-10 | 생산 디버그 포트가 양산 상태에서 열림 | EoP/Information Disclosure | AST-01, AST-02 | lifecycle별 debug lock/승인된 복구 경로 | TST-DBG-01..02 |
| TH-11 | NVM 설정/이미지/로그 물리 변조 | Tampering | AST-01, AST-05, AST-08 | 무결성 보호, 접근통제, 복구 검증 | TST-NVM-01..03 |
| TH-12 | 키/장치 ID 추출 또는 생산키 오용 | Information Disclosure/Spoofing | AST-02, AST-09 | 키 분리, 비밀키 비노출, key ceremony | TST-KEY-01..03 |
| TH-13 | 엔코더/센서 입력 spoofing 또는 단선/단락 | Spoofing/Tampering/DoS | AST-04 | plausibility/fault detection, 입력 진단 | TST-SNS-01..03 |
| TH-14 | 권한 있는 계정 오용/과도한 권한 | Repudiation/EoP | AST-05, AST-06, AST-08 | 최소권한, 역할 분리, 변경 감사 | TST-AUTH-01..03 |
| TH-15 | 로그 변조/포화로 사고 추적 실패 | Repudiation/DoS | AST-08 | 로그 무결성/용량 정책/중요 이벤트 우선순위 | TST-LOG-01..02 |
| TH-16 | 제3자 구성요소 취약점이 제품에 잔존 | Tampering/EoP | AST-01, AST-08 | SBOM, 공급자 통지, 취약점 triage | TST-SUP-01..03 |
| TH-17 | 보안 업데이트 배포·신고·사용자 통지 지연 | Process failure | AST-08, AST-10 | PSIRT, CVD, support/update 운영 절차 | TST-OPS-01..04 |
| TH-18 | 원격 서비스 계정/경로가 침해됨(해당 시) | Spoofing/EoP/DoS | AST-06, AST-07, AST-10 | 서비스 존재·필수성 검토, MFA/상호 인증/최소권한 | TST-REM-01..03 |

## 6. CRA 요구사항 연결 원칙

- Annex I Part I의 제품 보안 속성은 위협과 제품 맥락에 맞춰 설계·시험에 연결한다.
- Annex I Part II의 SBOM, 취약점 처리, 정기 시험, CVD, 신고 연락처, 안전한 업데이트 배포 및 무상 보안 업데이트는 제조자 프로세스와 증거에 연결한다.
- Articles 13–14의 위험평가·지원기간·신고는 제품 수명주기 운영 기록과 연결한다.
- 특정 TLS 버전, secure element, dual-bank flash, 특정 암호 알고리즘, 특정 네트워크 분리 회로는 제품 위험평가/부품 기능에 따른 선택지이며 이 문서만으로 법령상 의무라고 결론 내리지 않는다.
- 기능안전 요구(STO/SS1 등) 및 위험한 출력 상태의 판정은 별도 기능안전/제품 위험 분석과 조정한다.

## 7. 미확인 입력과 승격 게이트

| Input ID | 필요 입력 | 필요한 이유 | 현재 상태 |
|---|---|---|---|
| IN-01 | 제품 SKU/모델/HW revision | 제품 경계·시험 대상 식별 | UNVERIFIED |
| IN-02 | intended purpose 및 EU 공급 방식 | CRA scope/applicability | UNVERIFIED |
| IN-03 | Ethernet/fieldbus/USB/무선 인터페이스 목록 | 실제 공격 표면 | UNVERIFIED |
| IN-04 | 원격 데이터 처리/클라우드 기능 | Article 3 remote processing 판단 | UNVERIFIED |
| IN-05 | ST MCU 전체 주문 코드/실리콘 revision | boot/debug/crypto/NVM 기능 확인 | UNVERIFIED |
| IN-06 | boot/update/recovery 설계 및 키 구조 | TH-01..04, TH-12 검증 | UNVERIFIED |
| IN-07 | 서비스/디버그 양산 정책 | TH-09/10 검증 | UNVERIFIED |
| IN-08 | 모션 제어 주기·허용 지연·안전 상태 요구 | DoS/보안 실패 시험 기준 | UNVERIFIED |
| IN-09 | encoder/sensor 종류와 진단 방식 | TH-13 시험 정의 | UNVERIFIED |
| IN-10 | 생산 프로비저닝·서명키 custody 절차 | TH-12/16 검증 | UNVERIFIED |

제품 입력이 확보되기 전에는 위험도, 제품 적용성, 실제 구현 여부, 합격 수치를 확정하지 않는다. 시험 합격 기준은 제품 요구사항/위험평가/안전 분석에서 승인한 수치로 채운다.

## 8. 검토 완료 조건

- [ ] 제품 경계 및 실제 인터페이스 목록 확인
- [ ] 자산 소유자/보안 속성/영향 검토
- [ ] 공격자 능력과 설치환경 가정 승인
- [ ] 각 위협의 가능성·영향·위험평가 및 잔여위험 승인
- [ ] 통제 선택/제외 이유와 부품별 제약 기록
- [ ] 시험 ID, 시험 환경, 재현 절차, 승인된 합격 기준 정의
- [ ] 원시 로그/패킷/빌드 해시/설정 덤프 등 증거 보존
- [ ] 독립 검토자 또는 별도 검증 단계 완료

