# SIL 3 서보 드라이브 벤치마킹 보고서
**기준일:** 2026-11-17  
**문서 상태:** 기술조사 초안 v0.1 — 공식 제조사 자료 대조 완료, 상세 모델/전원/정격 확정 전  
**대상:** 범용 산업용 AC 서보 드라이브 및 기능안전 서브시스템

## 1. 요약 및 결론

SIL 3 서보 드라이브를 비교할 때 제품군 전체를 하나의 “SIL 3” 라벨로 평가하면 안 된다. 실제 성능은 **정확한 드라이브 형번, 안전 옵션, 모터/엔코더 조합, 펌웨어, 안전 네트워크, 외부 F-PLC 및 배선 진단**에 따라 달라진다.

2026-11-17 기준으로 공개된 제조사 자료에서 확인한 대표 제품은 다음과 같다.

| 제조사/제품 | 확인한 구성 | 공개된 안전 기능/성능 | 비교 시 주의점 |
|---|---|---|---|
| Mitsubishi MELSERVO-J5 | MR-J5-G(4)-HS/RJ 및 일반 G 계열 | STO, SS1, SS2, SOS, SBC, SLS, SSM, SDI, SLI, SLT 등. 모델별 SIL 3/PL e, Cat. 3 또는 4. PFH 3.0×10⁻⁹~7.7×10⁻⁹/h | 일반 G 계열은 STO 중심. 고급 안전 서브기능은 HS/RJ/네트워크/안전 모터/펌웨어 조합 필요. SLT 일부는 SIL 2/PL d |
| Yaskawa Sigma-7 + ASM7 | 400 V SERVOPACK SGD7S-***DA0*8**F91 + OSB01A/OSB02A | 최대 16개 안전 기능, SIL 3/PL e 구성 가능. 모듈/IO PFH 예시 최대 2.493×10⁻⁸/h | PFH는 모듈 단독 또는 모듈+I/O 범위이며 전체 드라이브 PFH가 아님. 기능별 엔코더 구성과 Cat. 2/3 차이 |
| Rockwell Kinetix 5700 | 2198-xxxx-ERS4, GuardLogix/Compact GuardLogix | STO, drive-based Timed/Monitored SS1. 일부 모니터링 기능 SIL 3/PL e, 일부 위치 기반 기능 SIL 2/PL d | SIL 3 모니터링 기능은 두 번째 피드백/엔코더 구성 필요. drive-based와 controller-based 안전 기능의 인증 범위 구분 |
| Siemens SINAMICS S210 | 6SL5… + SIMOTICS S-1FK2/S-1FT2 | STO/SS1/SS1E/SS2/SS2E/SOS, SBC, SLS/SDI/SSM/SLA 등. 제조사 선언서상 SIL 3/PL e, 기능별 Cat. 3 또는 4 | Extended 기능은 장치별 Safety Extended Runtime license 필요. 2025 선언서는 IEC 61800-5-2:2016 기준으로 2026 개정판 재확인 필요 |

**초기 설계 권고:** 1축 기준으로 표준 모션 제어부와 독립된 안전 제어 경로를 두고, 안전 엔코더/이중 피드백, 이중 채널 STO, 안전 브레이크 제어, 안전 통신 watchdog 및 진단을 포함한 기준 아키텍처를 채택한다. 다만 특정 1oo2D/Cat. 4 구성이 모든 안전 서브기능에 법적으로 일률 요구되는 것은 아니며, 최종 구조는 위험평가와 IEC 61800-5-2/IEC 61508/IEC 62061/ISO 13849의 해당 조항으로 검증한다.

## 2. 조사 범위와 전제

- 비교는 제조사가 공개한 공식 제품 페이지, 사용 설명서, 기능안전 매뉴얼 및 제조사 선언서를 우선한다.
- PFH 값은 기능/서브시스템의 범위가 다를 수 있으므로 숫자만으로 제조사 순위를 매기지 않는다.
- 서보 드라이브 단독 인증은 센서, 안전 PLC, 안전 통신, 외부 브레이크 및 기계 전체의 SIL 3를 자동 보장하지 않는다.
- 정격 전압, 출력(kW), 전류, 모터 유형, 축 수, 회생 방식, 엔코더, 안전 PLC, 네트워크가 아직 미확정이므로 본 문서는 **기능/아키텍처 벤치마킹**이다. 최종 BOM·회로도·PFH 계산은 정격 선정 후 수행한다.
- 제조사 자료가 IEC 61800-5-2:2016을 인용하는 경우, 2026-10-30 발행된 Amendment 1과의 적합성/인증 갱신 여부를 별도로 확인해야 한다.

## 3. 2026년 기준 표준 판본

| 표준 | 2026-11-17 기준 확인 상태 | 설계 적용 |
|---|---|---|
| IEC 61800-5-2:2016 + AMD1:2026 CSV, Ed. 2.1 | 2026-10-30 발행, 유효 | PDS(SR) 제품 수준의 안전 서브기능 설계·통합·검증 기준. 시험 요구, 파라미터화, EM/열/기계 내성, 피드백 센서 요구 등이 개정됨 |
| IEC 62061:2021 + AMD1:2024 + AMD2:2026 CSV, Ed. 2.2 | 2026-03-20 발행, 유효 | 기계 안전 관련 제어시스템의 기능안전 계획, 설계, 검증, 검증/유효성 확인 및 주기적 시험 |
| ISO 13849-1:2023, Ed. 4 | 2023-04 발행, 유효 | SRP/CS의 Category, PLr/PL, MTTFd, DCavg, CCF, 소프트웨어 및 검증 |
| IEC 61508-1:2010, Ed. 2 | 공식 목록상 유효 | E/E/PE 안전 관련 시스템의 기본 기능안전 프레임워크 |
| IEC 61508-1:2026 PRV, Ed. 3 | FDIS 투표는 2026-11-13 종료, 프로젝트 단계 50.60, 최종 발행 예정일 2027-01-22 | 아직 발행 전이므로 현행 규범 기준은 2010 Ed.2; 개정 영향 사전 검토에만 사용 |

### 3.1 IEC 61800-5-2 AMD1:2026의 설계 영향

최신 통합판은 단순한 오탈자 정정이 아니다. 파라미터화, 시험 요구, 전자파 내성, 열 내성, 기계적 내성, 순차 작업표, 모션/위치 피드백 센서 및 저수요 모드 PFDavg 산정 부속서가 갱신됐다. 본 설계의 안전 엔코더, 파라미터 잠금/검증, EMC 시험 및 열/기계 환경 시험 계획은 2016판만 기준으로 고정하지 않는다.

또한 개정판은 PDS(SR)에서 기존 “proof test” 용어/개념을 삭제하고 “safety function”보다 “safety sub-function”을 사용하도록 정비했다. 따라서 2022~2025년 제조사 문서의 “proof test interval” 문구를 그대로 최신 규격 요구로 취급하지 않는다. 제조사에 최신 인증서/기술문서의 개정판 적용 여부를 확인하고, diagnostic test interval과 maintenance interval은 최신 표준 및 해당 제품 매뉴얼에 맞춰 별도로 결정한다.

## 4. 제품별 벤치마킹

### 4.1 Mitsubishi Electric — MELSERVO-J5

**공식 자료:** MELSERVO-J5 Servo Amplifier Safety Sub-Functions 페이지 및 MR-J5 Safety Instructions 매뉴얼.

- 일반 MR-J5-G(4)/B/A 계열의 공개 표는 주로 STO 기능을 대상으로 하며 Category 3, PL e, SIL 3을 표시한다.
- MR-J5-G(4)-RJ, MR-J5W-G, MR-J5D 계열 및 HS 계열은 연결 방식/안전 모터/펌웨어 조건에 따라 SS1, SS2, SOS, SBC, SLS, SSM, SDI, SLI, SLT 등 추가 안전 서브기능을 제공한다.
- 공개 성능값: MTTFd ≥100년, DC Medium(약 96.5~97.6%), mission time 20년. PFH 예시는 일반 G 6.4×10⁻⁹/h, RJ 3.0×10⁻⁹/h, HS 7.7×10⁻⁹/h.
- STO 응답은 입력 장치 사용 시 8 ms 이하, 네트워크 안전 서브기능 경로는 설정 조건에 따라 60 ms 이하로 기재된다.
- HS/RJ 네트워크 안전 기능은 CC-Link IE TSN, EtherCAT/FSoE, EtherNet/IP 등 모델별 통신 및 cycle/watchdog 설정에 종속된다.
- 안전 서브기능 등급은 서보 앰프/드라이브, 안전 기능 지원 모터 및 펌웨어 조합에 따라 달라진다. Fully closed-loop 구성에서는 SS1-r, SS2, SOS, SLS, SSM, SDI, SLI가 지원되지 않는 조합이 있다.
- 직접 연결된 forced stop/safety/enable 스위치에 test-pulse 진단을 적용하지 않으면 Category 3 PL d SIL 2로 제한될 수 있다. Category 4 PL e SIL 3을 주장하려면 제조사 표에 명시된 test-pulse 진단과 해당 안전 CPU/컨트롤러 조합을 충족해야 한다.
- SLT 등 일부 기능은 Cat. 3 PL d SIL 2로 표기되므로 “모든 기능 SIL 3”이라고 요약하면 안 된다.

**벤치마크 판단:** 안전 서브기능 폭과 필드버스 선택이 강점이다. 반면 모델·모터·펌웨어·네트워크 조합표가 복잡하므로 구매 사양서에 전체 형번, 펌웨어, 모터/엔코더, 안전 통신, test-pulse 배선 조건을 고정해야 한다.

### 4.2 Yaskawa — Sigma-7 Advanced Safety Module (ASM7)

**대상 구성:** 400 V Sigma-7 SERVOPACK SGD7S-***DA0*8**F91 + SGD7S-OSB01A 또는 SGD7S-OSB02A.

- OSB01A/OSB02A는 Advanced Safety Module 옵션이다. 제조사 문서상 FSoE 기반 네트워크 안전을 제공하고 OSB02A는 추가 물리 안전 I/O 커넥터를 제공한다.
- 제조사 제품 페이지는 최대 16개 안전 기능과 SIL 3/PL e 가능 구성을 명시한다.
- 문서에 나타난 기능 예: STO, SS1-r/t, SS2-r/t, SOS, SLS, SLA, SSR, SDI, SLP, SLI, SLT, SMT, SCA, SSM 및 SHP.
- 모듈 CPU PFH 예시는 1.30×10⁻⁹/h, OSB02A의 모든 I/O 포트를 포함한 모듈 구성 예시는 최대 2.493×10⁻⁸/h다. 이는 **전체 서보 드라이브/모터/엔코더 시스템 PFH가 아니다**. 완성된 안전 서브기능의 PFH에는 SERVOPACK, CPU, encoder, 안전 I/O 및 외부 요소가 포함되어야 한다.
- mission time은 20년으로 제시된다.
- STO는 이중 엔코더가 없어도 SIL 3/PL e Cat. 3을 달성하는 구성으로 기재된다. 속도/위치 모니터링 등 다른 기능은 기능별 엔코더 구성과 이중 피드백 여부에 따라 등급이 달라진다. 매뉴얼에는 single-encoder 구성 중 SIL 2/PL d Cat. 3 예와 특정 SIL 3/PL e Cat. 2 구성 예가 각각 존재하므로, “single encoder면 항상 SIL 3” 또는 “항상 SIL 2”로 일반화하면 안 된다.
- SLT/SMT 등 일부 기능은 SIL 3/PL e를 위해 dual-channel analog input 조건이 기재되어 있다.

**벤치마크 판단:** FSoE 및 확장 안전 기능의 유연성이 강점이다. 그러나 PFH 수치의 경계(모듈만/모듈+I/O/전체 드라이브)와 encoder 조합을 분리해 검토해야 한다. 안전 모듈 단독 PFH를 시스템 전체 PFH로 사용하지 않는다.

### 4.3 Rockwell Automation — Allen-Bradley Kinetix 5700

**대상 구성:** 2198-xxxx-ERS4 dual-axis/single-axis inverter 및 GuardLogix/Compact GuardLogix 안전 제어기.

- Kinetix 5700은 hardwired 및 integrated STO를 지원한다. ERS4는 drive-based Timed SS1 및 Monitored SS1 기능을 제공하며, ERS3 series B 이상은 Timed SS1 기능을 제공하는 구성으로 문서화되어 있다.
- 제조사 Safety Reference Manual의 기능 등급표: Monitored SS1, SS2 velocity check, SOS velocity check, SLS는 SIL 3/PL e; SS2 position check, SOS position check, SDI, SLP는 SIL 2/PL d.
- SIL 3 모션 모니터링 기능은 이중 피드백/엔코더 구성이 필요할 수 있다. 2026년 User Manual은 Single Feedback Monitoring과 Dual Feedback Monitoring 설정을 구분하며, 실제 SIL 등급은 정확한 encoder와 안전 기능 조합을 안전 매뉴얼에서 확인하도록 안내한다.
- Safety Reference Manual의 drive-based functions PFH 예시는 3.85×10⁻⁹/h, HFT 1로 기재되어 있다. 이 수치는 해당 drive-based function 범위에 관한 값이지 GuardLogix, 외부 센서, 두 번째 엔코더, 기계 브레이크까지 포함한 완성 시스템 PFH가 아니다.
- 같은 문서에 20년 proof-test interval 문구가 있으나, 이는 IEC 61800-5-2 AMD1:2026 이전 문서다. 최신 개정판의 proof-test 개념 변경과 제조사 인증 갱신 여부를 서면으로 확인해야 한다.
- drive-based safety와 GuardLogix/controller-based safety functions를 구분해 인증서 범위를 확인한다.

**벤치마크 판단:** Rockwell/GuardLogix 생태계에 이미 투자한 현장에서는 통합성이 장점이다. 다만 SIL 3 기능을 선택할 때 ERS4, GuardLogix, dual feedback, safety connection mode, Studio 5000 버전 및 controller safety signature 절차를 묶어서 사양화해야 한다.

### 4.4 Siemens — SINAMICS S210

**대상 구성:** SINAMICS S210(6SL5…) 및 SIMOTICS S-1FK2/S-1FT2.

- Siemens 2025-09-30 Safety Manufacturer’s Declaration No. 668.DCO.B2N.40.2509.029은 S210 제품군의 Basic/Extended Safety Integrated functions가 SIL 3 및 PL e를 충족한다고 선언한다.
- Basic: STO, SS1, SBC. Basic functions는 별도 Safety Extended Runtime license 없이 사용할 수 있다.
- Extended: SLS, SDI, SSM, SOS, SLA, SS1E, SS2, SS2E, SBT 등. License 요구는 기능/제어 방식별로 다르다. 예를 들어 SS1-t/SS1E-t는 무라이선스 경로가 있으나 monitored/advanced variants 등은 Safety Extended Runtime license가 필요할 수 있으므로 정확한 기능표를 확인한다.
- 제조사 선언서 표에서 Basic functions는 Category 4, Extended functions는 Category 3로 구분된다. SBT는 진단 기능으로 IEC 61800-5-2의 safety sub-function 범위 밖이며, 별도 표에서 PL d Category 2/3로 표시된다. 이를 다른 안전 서브기능과 같은 SIL 3 인증으로 뭉뚱그리지 않는다.
- Basic 기능은 F-DI 또는 PROFIsafe로 제어할 수 있고 Extended 기능은 PROFIsafe 경로를 사용한다.
- STO/SS1은 각각 stop category 0/1에 해당한다. STO는 토크 생성 에너지를 차단하지만 모터/드라이브 간 galvanic isolation을 제공하지 않는다.
- 2025 선언서는 S210 firmware V6.4 HF4 등을 대상으로 IEC 61508:2010, IEC 61800-5-2:2016 및 ISO 13849-1:2015를 인용한다. 2026-10-30 발행된 IEC 61800-5-2 AMD1:2026 및 ISO 13849-1:2023에 대한 갱신 선언/인증 적용 여부를 Siemens에 확인해야 한다.

**벤치마크 판단:** 기본 STO/SS1/SBC와 Extended motion monitoring 기능의 구분이 명확하고 PROFIsafe 통합이 강점이다. 다만 라이선스, F-DI/PROFIsafe, 안전 기능별 Category 및 최신 표준 판본을 구매/설계 기준서에 명시해야 한다.

## 5. 공통 비교에서 반드시 분리할 항목

1. **제품 SIL과 기계 전체 SIL:** drive certificate는 센서, F-PLC, 안전 통신, 엔코더, 외부 브레이크 및 기계 위험 저감 전체를 인증하지 않는다.
2. **STO와 전기적 격리:** STO는 토크 생성 에너지를 차단하는 안전 서브기능이며 주전원 절연/정비용 lockout-tagout을 대체하지 않는다.
3. **STO와 정지:** STO만으로 제동 정지, 수직축 하중 유지 또는 기계적 정지를 보장하지 않는다. 필요한 경우 SS1/SS2/SOS 및 fail-safe mechanical brake를 설계한다.
4. **PFH 범위:** 모듈 CPU, 드라이브 안전 기능, 드라이브+엔코더, 완성된 안전 기능의 PFH를 같은 열에 놓고 직접 순위를 매기지 않는다.
5. **기능 등급 차이:** 한 제품군 내에서도 STO는 SIL 3인데 SLP/SLI/SLT 등 일부 기능은 SIL 2일 수 있다. 기능별 표를 유지한다.
6. **피드백 구성:** dual encoder, single encoder, safe encoder, resolver, fully closed-loop 등 실제 하드웨어 조합을 명시한다.
7. **표준 판본:** 제조사 문서가 2016판을 인용하면 2026 AMD1 적용성, 인증 갱신, test/diagnostic interval을 별도 확인한다.

## 6. 기준 설계 방향

- 표준 모션 CPU와 독립된 safety CPU/FPGA 또는 인증된 safety module 경로를 구성한다.
- F-PLC와 drive 사이에 인증된 안전 통신(FSoE, CIP Safety 또는 PROFIsafe 중 프로젝트 네트워크에 맞는 하나)을 사용한다.
- STO의 두 독립 채널은 게이트 드라이버의 안전 차단 경로로 전달하고, 각 채널의 단선/단락/교차단락 진단을 검증한다.
- SS1/SS2/SOS/SLS/SDI/SLP/SLI 등 모션 안전 기능은 제품 인증 범위에 맞는 안전 엔코더/이중 피드백을 선택한다.
- 수직축 및 관성 부하에는 SBC와 fail-safe spring-applied brake, brake feedback 및 brake test를 포함한다.
- 각 안전 기능별로 reaction time, stopping distance, restart inhibit, fault response 및 PFH chain을 검증한다.
- 보안 기능(secure boot, signed update, credential protection, debug-port control, logging, CVD)은 별도 cybersecurity traceability로 관리하며, 특정 부품/기술을 CRA가 직접 지정한다고 표현하지 않는다.

## 7. 미확정 입력 및 후속 검증

| 항목 | 현재 상태 | 다음 확인 |
|---|---|---|
| 입력 전압/주파수 | 미확정 | 200 V/400 V 계열 및 국가별 전원 |
| 정격 출력/전류/과부하 | 미확정 | kW, Arms, peak current, duty cycle |
| 축 수/공유 DC bus | 미확정 | 단축/다축, regenerative supply |
| 모터/부하 | 미확정 | rotary/linear/direct drive, 관성비, 수직축 여부 |
| 피드백 | 미확정 | safety encoder, dual encoder, resolver, fully closed-loop |
| 안전 기능 | 잠정 | STO/SS1/SS2/SOS/SLS/SDI/SLP/SBC/SBT 중 필수 범위 |
| 안전 제어기/네트워크 | 미확정 | GuardLogix, F-CPU/PROFIsafe, FSoE 등 |
| 목표 SIL/PL | SIL 3 벤치마킹 | 위험평가로 각 기능의 SIL/PLr 확정 |
| mission time/diagnostic interval | 미확정 | 최신 IEC 61800-5-2 AMD1:2026 및 제조사 최신 선언서 확인 |

## 8. 출처 및 검증 수준

### 표준기관
- IEC 61800-5-2:2016+AMD1:2026 CSV Ed. 2.1 (2026-10-30): https://webstore.iec.ch/en/publication/117563
- IEC 62061:2021+AMD1:2024+AMD2:2026 CSV Ed. 2.2 (2026-03-20): https://webstore.iec.ch/en/publication/112847
- ISO 13849-1:2023 Ed. 4: https://www.iso.org/standard/73481.html
- IEC 61508-1:2026 PRV Ed. 3 (FDIS 투표 2026-11-13 종료, 최종 발행 예정 2027-01-22): https://webstore.iec.ch/en/publication/117296

### 제조사
- Mitsubishi MELSERVO-J5 Safety Sub-Functions: https://www.mitsubishielectric.com/fa/products/drv/servo/pmerit/mr_j5/amp/safety_sub-functions.html
- Mitsubishi MR-J5 Safety Instructions: https://dl.mitsubishielectric.com/dl/fa/document/manual/servo/ib0300391e/ib0300391engl.pdf
- Yaskawa Sigma-7 Advanced Safety Module product page and current documents: https://www.yaskawa.ie/motion-control/option-modules/productdetail/product/advanced-safety-module_15806
- Yaskawa ASM7 Product Manual: https://www.yaskawa.it/Global%20Assets/Downloads/Technical_Documentation/Servo_Drives/Sigma7_Series/S7_OptionsAccessories/SIEP%20YEUOS7S%2001B%20ASM7%20Product%20Manual.pdf
- Rockwell Kinetix 5700 Safe Monitor Functions Safety Reference Manual 2198-RM001: https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/2198-rm001_-en-p.pdf
- Rockwell Kinetix 5700 User Manual 2198-UM002Q-EN-P (June 2026): https://literature.rockwellautomation.com/idc/groups/literature/documents/um/2198-um002_-en-p.pdf
- Siemens S210 Safety Manufacturer’s Declaration 668.DCO.B2N.40.2509.029 (2025-09-30): https://cache.industry.siemens.com/dl/files/250/109996250/att_1346004/v1/Safety_Manufacturers_Declaration_-_SINAMICS_S210_668.DCO.B2N.40.2509.029.pdf
- Siemens S210 Operating Instructions (03/2023, FW V6.1): https://support.industry.siemens.com/cs/attachments/109818069/S210_S-1FK2_S-1FT2_op_instr_0323_en-US.pdf

**검증 한계:** 공개 자료는 제조사 자료를 우선했지만, 제품별 최신 TÜV/UL 인증서 원본과 2026-10-30 표준 개정판에 대한 재인증 여부는 아직 제조사에 직접 확인하지 않았다. 따라서 이 보고서는 벤치마킹 근거자료이며, 인증 적합성 선언이나 최종 회로 설계 승인 문서가 아니다.
