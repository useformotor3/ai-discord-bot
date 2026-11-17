# CRA 산업용 서보 드라이브 참조 보안 아키텍처

- 문서 버전: v0.1 (일반 참조 설계 / 특정 제품 구현 전)
- 기준일: 2026-11-17
- 활성 범위: CRA 사이버보안 요구사항
- 관련 문서:
  - [CRA 통합 규제·기술 준수 보고서 v0.2](CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)
  - [35개 CRA 요구사항 추적표](CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv)
  - [15개 인터페이스 적용성 매트릭스](CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv)
  - [36개 보안 통제·시험 매트릭스](CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv)

## 1. 목적과 설계 원칙

본 문서는 네트워크/디지털 인터페이스가 있는 산업용 서보 드라이브의 CRA 대응을 위한 **논리적 참조 보안 아키텍처**다. 실제 회로도, MCU/SoC 모델, 메모리 구성, fieldbus stack, 업데이트 경로가 제공되지 않았으므로 특정 하드웨어 설계의 승인 또는 구현 완료를 의미하지 않는다.

설계 원칙:
1. 실시간 모터 제어 경로와 외부 통신/관리 경로를 논리적으로 분리한다.
2. 부팅·펌웨어 업데이트·설정 변경·서비스 접근의 신뢰 경계를 명확히 한다.
3. 제품 위험평가 결과에 따라 보안 통제를 선택하고, 각 통제에 시험 방법과 증거를 연결한다.
4. CRA가 요구하는 보안 결과와 특정 기술 구현(MFA, RBAC, secure element, digital signature, encryption 등)을 구분한다. 기술은 위험·성능·비용·수명주기 검토 후 선택한다.
5. STO/SS1, 안전 토크 차단, 브레이크 동작 등 기능안전 동작을 CRA의 자동 요구사항으로 가정하지 않는다. 별도 hazard analysis와 해당 안전 법령/표준의 적용성으로 결정한다.
6. 기본 구성은 현장 산업 네트워크, PLC/상위 제어기, 엔지니어링 PC, USB/serial service, 선택적 cloud/RDPS를 포함할 수 있으나, 실제 제품에 존재하는 경로만 적용한다.

## 2. 논리 블록 구조

\`\`\`mermaid
flowchart LR
  subgraph EXT["외부 환경 / 신뢰 경계"]
    PLC["PLC / 산업 네트워크"]
    ENG["Engineering PC / Commissioning Tool"]
    CLOUD["선택적 Cloud / RDPS"]
    SUP["제조사 보안 운영\nSBOM · CVD · 패치 · SRP"]
  end

  subgraph DRIVE["서보 드라이브 제품 경계"]
    NET["Ethernet / Fieldbus\nEtherCAT · PROFINET · EtherNet/IP"]
    SVC["Service Interface\nUSB · UART · RS-232 · Debug"]
    COMM["통신·관리 처리\nProtocol Stack · Command Parser"]
    AUTH["접근통제·인증\nIdentity · Authorization"]
    BOOT["Boot ROM / Bootloader\nRoot of Trust (선택 설계)"]
    VERIFY["Firmware Verification\nImage Integrity · Version Policy"]
    FW["Control Firmware"]
    CTRL["Real-time Control MCU/SoC\nCurrent / Speed / Position Loop"]
    PWM["PWM / Gate Driver Interface"]
    MOTOR["Motor / Encoder"]
    NVM["Non-volatile Storage\nConfig · Logs · Update Slots"]
    KEY["Protected Key / Device Identity\nSecure Element or Protected MCU Storage"]
    WDG["Watchdog / Health Monitor"]
  end

  PLC --> NET --> COMM
  ENG --> SVC --> COMM
  CLOUD -. "필수 RDPS인 경우만" .-> COMM
  COMM --> AUTH
  AUTH --> FW
  BOOT --> VERIFY --> FW
  KEY --> VERIFY
  KEY --> AUTH
  FW <--> NVM
  FW --> CTRL --> PWM --> MOTOR
  MOTOR --> CTRL
  CTRL --> WDG
  FW --> WDG
  SUP -. "취약점·업데이트 운영" .-> CLOUD
  SUP -. "서명된 업데이트/권고" .-> ENG
\`\`\`

### 2.1 블록별 책임

| 블록 | 보안 책임 | CRA 연결 | 설계/검증 상태 |
|---|---|---|---|
| Ethernet/Fieldbus | 외부 데이터 진입점, 프로토콜·포트 최소화 | Annex I Part I (2)(d),(f),(h),(i),(j) | 제품별 인터페이스 확인 전 |
| Service/Debug | 생산·현장 서비스 접근 통제 | Annex I Part I (2)(d),(j) | 실제 포트/모드 확인 전 |
| Communication/Management | 입력 검증, 명령 권한, rate/resource limit | Annex I Part I (2)(d),(f),(h),(j),(k) | protocol stack 미확인 |
| Boot ROM/Bootloader | 부팅 신뢰 시작점, 복구/업데이트 경계 | Annex I Part I (2)(a),(b),(f); Part II (2),(7) | MCU 기능 확인 전 |
| Firmware Verification | 이미지 무결성·버전·호환성 확인 | Annex I Part I (2)(a),(f); Part II (2),(7) | 구현 후보 |
| Control MCU/SoC | 실시간 제어와 관리 코드 간 영향 제한 | Annex I Part I (2)(h),(i),(j),(k) | SoC/RTOS 미확인 |
| NVM | 설정·로그·업데이트 슬롯의 기밀성/무결성/삭제 | Annex I Part I (2)(e),(f),(l),(m) | 메모리 구성 미확인 |
| Key/Identity | 기기 식별·키 보호·인증 | Annex I Part I (2)(d),(e),(f) | secure element는 선택 후보 |
| Watchdog/Health | 장애 탐지 및 핵심 기능 복구 | Annex I Part I (2)(h),(k) | 성능/안전 영향 검증 필요 |
| Manufacturer operations | SBOM·CVD·패치·지원기간·신고 | Annex I Part II (1)-(8), Articles 13-16 | 프로세스/증거 작성 필요 |

## 3. 신뢰 경계 및 데이터 흐름

### TB-1: PLC/산업 네트워크 ↔ 드라이브 통신부
- 데이터: cyclic command/status, parameter access, diagnostics, firmware/service messages.
- 주요 위험: 무단 파라미터 변경, 악성/비정상 프레임, DoS, protocol parser 취약점, 다른 노드에 대한 네트워크 영향.
- 후보 통제: allowlist, command range checking, access control, rate/resource limit, unused service disable, network segmentation.
- 시험: valid/invalid frame, malformed packet fuzzing, unauthorized write, replay/sequence, flood/resource exhaustion, recovery.

### TB-2: Engineering PC/Service Tool ↔ 드라이브
- 데이터: commissioning, tuning, firmware update, diagnostic log, configuration import/export.
- 주요 위험: 악성 PC/도구, 권한 상승, 설정 파일 변조, 서비스 포트 오남용, 공용 자격증명.
- 후보 통제: tool identity, authenticated session, role-based function separation, signed configuration/update, production debug lock, service-mode timeout.
- 시험: unauthorized tool, expired credential, modified config, service-mode exit, debug unlock attempt, interrupted update.

### TB-3: Boot chain ↔ firmware image
- 데이터: bootloader, firmware image, version metadata, signature/hash, update manifest.
- 주요 위험: 악성 firmware, downgrade, corrupted image, update interruption, wrong model image.
- 후보 통제: hardware/ROM root of trust, signed image verification, version policy, dual-bank/recovery, model compatibility checks. 실제 필요성/방법은 MCU·제품 위험평가에 따라 결정.
- 시험: invalid signature, modified image, downgrade, wrong model, power loss during update, recovery from corrupted slot.

### TB-4: Firmware ↔ non-volatile storage
- 데이터: user configuration, credentials/keys, logs, calibration, update metadata.
- 주요 위험: 설정/키 추출, log tampering, corrupted configuration, data remnants after decommissioning.
- 후보 통제: protected storage, integrity checks, access control, secure erase/cryptographic erase where suitable, log retention policy.
- 시험: unauthorized read/write, corruption, rollback, factory reset, recovery and data remanence checks.

### TB-5: Drive ↔ optional cloud/RDPS
- 데이터: remote diagnostics, fleet management, telemetry, remote update, identity/token.
- 주요 위험: cloud account compromise, tenant crossover, API abuse, third-party service outage, remote command misuse.
- 판단: 원격 처리가 제품의 기능 수행에 필수이고 제조자가 개발했거나 책임지는 경우 RDPS 제품 경계에 포함될 수 있다. 단순 독립 SaaS는 자동 포함되지 않는다.
- 후보 통제: tenant isolation, scoped API tokens, strong authentication, access logging, secure transport, least privilege, service separation.
- 시험: tenant isolation, token revoke, unauthorized remote command, cloud outage, data export, third-party compromise tabletop.
- cloud가 실제 제품에 없다면 해당 경계는 N/A로 문서화한다.

### TB-6: 제조사 공급망/개발·릴리스 환경
- 데이터: source code, third-party dependencies, build artifacts, SBOM, signing keys, release package.
- 주요 위험: compromised dependency, build pipeline compromise, signing key theft, incorrect SBOM, untracked release.
- 후보 통제: dependency pinning, SBOM, reproducible/protected build, signing key separation, release approval, vulnerability intake.
- 시험: dependency compromise simulation, signature key access review, SBOM-to-build reconciliation, release provenance review.

## 4. 보안 통제 설계 선택지

### 4.1 하드웨어/부트 영역
- MCU/SoC가 제공하는 secure boot, immutable boot ROM, debug lock, memory protection, hardware cryptographic acceleration, secure key storage 기능을 비교한다.
- Secure element/TPM을 추가할지, MCU 내 protected storage로 충분한지 비용·공급·수명주기·복구·인증 위험을 비교한다.
- OTA/USB/serial 업데이트를 지원하는 경우 부트 체인과 복구 경로를 함께 설계한다.
- watchdog, brown-out, power-loss recovery가 업데이트·로그·설정 저장에 미치는 영향을 검증한다.
- 하드웨어 기능이 부족하더라도 위험평가상 동등한 보호 통제를 구현할 수 있는지 검토한다.

### 4.2 펌웨어/소프트웨어 영역
- 안전한 기본 구성, 불필요 서비스 제거, 명령/파라미터 범위 검증, 입력 길이/형식 검증을 구현 후보로 둔다.
- 통신 stack, bootloader, RTOS, cryptographic library, diagnostic library 등 구성요소의 SBOM과 취약점 대응을 관리한다.
- 업데이트는 모델/하드웨어 revision/firmware version을 검증하고, 변조·downgrade·중단 상황을 시험한다.
- 보안 로그에는 접근·설정·업데이트·권한 변경 등 제품 위험에 필요한 이벤트만 기록하고, 저장공간·개인정보·사용자 opt-out 요구를 고려한다.
- 실시간 control loop의 지연·jitter·CPU/memory budget에 미치는 보안 통제 영향을 측정한다.

### 4.3 통신/관리 영역
- 제품에 존재하는 인터페이스만 목록화하고, 각 프로토콜의 읽기/쓰기/관리 명령을 구분한다.
- 안전한 원격 관리 채널과 실시간 필드버스 경로를 분리할 수 있는지 검토한다. 모든 실시간 프로토콜에 무조건 암호화를 추가한다고 가정하지 않는다.
- 진단/설정 포트는 기본 비활성화 또는 제한된 서비스 모드 등 위험기반 정책을 검토한다.
- 외부 명령의 인증·권한·범위·빈도·상태 전이 검증을 수행한다.
- 네트워크 오류가 드라이브뿐 아니라 PLC·다른 노드에 미치는 영향을 검증한다.

## 5. 보안 요구사항·시험 매트릭스 연결

각 통제는 기존 문서와 다음 방식으로 연결한다.
- 법적 요구사항: [35개 CRA 요구사항 추적표](CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv)
- 인터페이스 분류: [15개 인터페이스 적용성 매트릭스](CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv)
- 통제/시험 후보: [36개 보안 통제·시험 매트릭스](CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv)

권장 검증 단계:
1. 각 SEC ID에 해당 제품 인터페이스/블록/펌웨어 모듈을 연결한다.
2. 적용되지 않는 통제는 제품 기능·데이터 흐름·위험평가 근거로 N/A 처리한다.
3. 적용 통제는 설계 산출물·시험 케이스·시험 결과·결함/시정조치 ID로 추적한다.
4. 미실시 시험은 '미검증', 증거가 없는 통제는 '증거 미확인' 상태로 유지한다.
5. 제품 변경/펌웨어 릴리스/표준 개정 시 영향 분석과 재시험 범위를 결정한다.

## 6. 제품별 확정에 필요한 자료

1. MCU/SoC 정확한 부품 번호와 silicon revision, 보안 기능 reference manual.
2. Boot ROM, bootloader, secure boot, debug lock, key storage 지원 여부.
3. Flash/RAM/EEPROM/secure storage 구성과 update slot/rollback 설계.
4. Ethernet/fieldbus/CAN/serial/USB/wireless 인터페이스와 protocol stack 버전.
5. Firmware architecture, RTOS, task/interrupt/resource budget, real-time control loop.
6. Parameter map, command set, authentication/authorization 기능.
7. PC commissioning tool, cloud/RDPS, remote access 경로 및 공급 주체.
8. Secure update package, signing key lifecycle, recovery procedure.
9. SBOM, vulnerability handling/CVD, support period, security update release process.
10. Machinery/기타 EU 법령 인증서가 있다면 해당 인증서의 제품·위험 범위.

## 7. 제한사항 및 다음 단계

- 이 문서는 제품별 회로도/펌웨어를 분석하지 않은 참조 아키텍처다.
- 특정 MCU/secure element/암호 알고리즘/필드버스 보안 기능을 CRA가 직접 의무화한다고 주장하지 않는다.
- 실제 기능안전 동작, STO/SS1, 브레이크/모터 토크 차단의 설계는 별도 안전 분석과 승인 절차를 따른다.
- 다음 단계는 제품별 자료를 확보해 블록 경계와 SEC ID를 실제 부품/펌웨어/시험 증거에 연결하는 것이다.
