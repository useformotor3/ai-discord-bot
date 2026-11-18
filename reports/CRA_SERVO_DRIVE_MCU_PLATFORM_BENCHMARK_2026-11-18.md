# CRA 서보 드라이브 MCU 후보 기술 벤치마킹 — ST 기준 / TI 비교

- 문서 버전: v0.1 (공식 제조사 자료 기반 예비 비교)
- 기준일: 2026-11-18
- 목적: 실제 제품의 ST MCU를 기준으로 CRA 참조 하드웨어 아키텍처 후보를 검토하고, TI 대안 후보의 기능·성능·보안 특성을 비교
- 판정 상태: **예비 비교 / MCU 선정 보류**
- 제한: 실제 제품의 ST 부품번호, 회로도, 제어 주기, 전류/속도/위치 루프 요구, 통신 스택, BOM이 확인되지 않았다. 따라서 후보의 적합성·성능 우열·대체 가능성을 확정하지 않는다.

## 1. 핵심 결론

1. 사용 중인 ST MCU의 정확한 부품번호가 확인되지 않았다. ST가 실제 제품의 기준 플랫폼이며, 아래 STM32G474RE와 STM32H753XI는 공개 자료를 바탕으로 한 **비교 후보**이지 실제 탑재 부품이라고 단정하지 않는다.
2. TI 비교 후보는 이전에 특정한 **MSPM0G3529-Q1**이다. TI 공식 데이터시트 Rev. B는 80 MHz Cortex-M0+, 512 KB Flash, 128 KB SRAM 및 보안 부트·업데이트·AES·키 저장·TRNG 등을 기재한다.
3. STM32G474RE는 고해상도 PWM, 다중 ADC, CORDIC/FMAC 등 모터제어 주변장치 밀도가 강점이다. STM32H753XI는 훨씬 높은 CPU 성능·메모리·암호 가속과 보안 펌웨어 업데이트 기능이 강점이다.
4. MSPM0G3529-Q1은 보안 기능 통합도가 높지만 80 MHz Cortex-M0+ 제품이므로 G474/H753과 동급 CPU 성능의 직접 대체품이라고 간주하지 않는다. 저·중급 제어 또는 통신/보안 보조 MCU 역할도 포함해 실제 제어 부하로 검증한다.
5. 최종 선택 전에는 실제 제품의 제어 주기·PWM/ADC 동기화·엔코더·필드버스·실시간 jitter·메모리·업데이트 요구를 고정하고 동일 시험을 수행해야 한다.

## 2. 후보의 출처 및 정확한 범위

| 후보 | 제조사 자료 기준 상태 | 주요 범위 | 비교에서의 역할 |
|---|---|---|---|
| ST STM32G474RE | ST 제품 페이지: Active / volume production | Cortex-M4 170 MHz, FPU/DSP, 모터제어 타이머·HRTIM·ADC·CORDIC/FMAC | 모터 제어 주변장치 중심 ST 후보 |
| ST STM32H753XI | ST 제품 페이지: Active / volume production | Cortex-M7 480 MHz, 2 MB Flash, 1 MB RAM, HW crypto, secure firmware upgrade | 고성능 제어/통신 통합 ST 후보 |
| TI MSPM0G3529-Q1 | TI 제품 페이지: Active; 데이터시트 Rev. B, 2025-10 개정 | Cortex-M0+ 80 MHz, 512 KB Flash, 128 KB SRAM, CAN-FD, 보안 부트/업데이트/키 저장 | 보안 통합형 TI 비교 후보; 동급 성능 대체 여부 미확정 |

정확한 제품 주문 코드, 패키지, 온도 등급, silicon revision, errata, 공급/수명주기와 실제 구입 가능성은 설계 동결 전에 다시 확인한다.

## 3. 하드웨어·실시간 기능 비교

| 항목 | STM32G474RE (ST) | STM32H753XI (ST) | MSPM0G3529-Q1 (TI) |
|---|---|---|---|
| CPU | Arm Cortex-M4, 최대 170 MHz, FPU/DSP, 213 DMIPS (ST 표기) | Arm Cortex-M7, 최대 480 MHz, double/single FPU, DSP, 1027 DMIPS (ST 표기) | Arm Cortex-M0+, 최대 80 MHz |
| 메모리 | 최대 512 KB Flash; 96 KB SRAM + 32 KB CCM SRAM | 2 MB dual-bank Flash; 최대 1 MB RAM(192 KB TCM 포함) | 512 KB ECC Flash; 128 KB SRAM |
| ADC | 5 × 12-bit ADC, 최대 4 Msps | 3 ADC (세부 채널/속도는 정확 데이터시트 확인 필요) | 동시 샘플링 2 × 12-bit ADC, 4 Msps |
| PWM/타이머 | HRTIM 12 PWM, 3개 motor-control advanced timer; dead-time/emergency stop 기능 | HRTIM 및 motor-control PWM timer 2개; 상세 채널·동기화는 DS12117로 확인 | 9 timers, 최대 28 PWM; advanced timer 2개에서 dead-band 및 complementary output 최대 12 PWM |
| 모터 수학/위치 | CORDIC, FMAC; 타이머에 quadrature encoder 입력 지원 | 고성능 CPU/DSP, timer/encoder 기능은 상세 peripheral matrix 확인 | Math accelerator(DIV/SQRT/MAC/TRIG); 16-bit QEI timer 2개 |
| 통신 후보 | 3 × FDCAN, USART/UART/SPI/I2C, USB 등 | 광범위한 통신 주변장치; 제품 구성에 필요한 실제 MAC/PHY 및 fieldbus는 별도 확인 | 2 × CAN-FD, 7 UART, 3 SPI, 3 I2C |
| 메모리 보호/무결성 | Flash ECC, SRAM parity 일부, RDP/write protection/securable area/PCROP, OTP | ROP/PC-ROP, active tamper, secure access mode, Flash/RAM 및 보안 기능은 exact datasheet 확인 | Flash ECC, SRAM Bank 0 ECC/parity, code/data firewall, Flash read/execute/write protection |
| 제어 적용 관점 | 전류 루프와 PWM/ADC 동기화에 유리한 주변장치 구성이지만 실제 FOC cycle 시험 필요 | 복잡한 제어·통신·상위 기능을 통합할 CPU 여유가 강점일 수 있으나 실시간 분리와 bus contention 시험 필요 | PWM/ADC/QEI 기능은 갖추지만 80 MHz M0+의 실제 FOC/통신 동시 부하 성능을 측정해야 함 |

**주의:** CPU MHz/DMIPS 숫자는 서로 다른 코어·컴파일러·메모리 조건의 직접적인 서보 제어 성능 비교값이 아니다. 동일 제어 알고리즘, 동일 컴파일 최적화, 동일 PWM/ADC 조건의 보드 시험이 필요하다.

## 4. 보안 기능 비교 — 제품별 증거가 있는 범위만

### 4.1 STM32G474RE

ST 제품 페이지는 MPU, Flash readout/write protection, securable memory area, PCROP, 1 KB OTP, Flash ECC 및 일부 SRAM parity를 열거한다. 확인한 G474RE 제품 페이지에는 하드웨어 AES/해시 가속기나 secure boot를 명시한 근거를 찾지 못했다. 따라서 해당 기능을 G474RE에 있다고 가정하지 않는다.

- 보안 설계 시 Flash 보호·MPU·OTP·디버그 lifecycle을 우선 검토한다.
- 암호 연산/키 보호/secure boot가 필요하다고 위험평가에서 결정되면 소프트웨어 구현의 성능·키 보호 한계와 별도 보안 MCU/소자 또는 다른 ST SKU를 비교한다.
- STM32G484 계열은 ST 제품 선택기에서 Crypto 기능이 표시되는 별도 SKU다. G484의 기능을 G474에 전이해서는 안 되며, exact part/package별 데이터시트 확인이 필요하다.

### 4.2 STM32H753XI

ST 제품 페이지는 HW crypto, ROP, PC-ROP, active tamper, secure firmware upgrade 및 Secure access mode를 표시한다. H753 데이터시트는 AES, HASH 등의 crypto acceleration을 설명한다. ST AN5156은 H74x/75x 계열에서 secure boot/firmware update가 SBSFU software package 기반의 legacy path로 분류되는 점을 보여준다.

- HW crypto가 있다고 해서 키 수명주기·secure boot·업데이트가 자동으로 완성되는 것은 아니다.
- SBSFU/SFI 구성, root-of-trust 설정, debug lifecycle, provisioning, recovery 및 rollback 정책을 제품 수준에서 설계·검증해야 한다.
- ST AN4992 Rev.19(2026-07)는 SFI가 OEM firmware의 confidentiality/authentication/integrity를 제조 프로그래밍 단계에서 보호하는 흐름임을 설명한다. 이는 현장 업데이트와 동일한 기능이라고 간주하지 않는다.

### 4.3 TI MSPM0G3529-Q1

TI 데이터시트 Rev. B, §8.18–8.21은 다음 기능을 명시한다.

- Secure boot 및 secure firmware update
- AES-128/256 hardware accelerator (GCM/GMAC, CCM/CBC-MAC, CBC, CTR 등)
- AES key 최대 4개를 위한 secure key storage
- Code/data firewall, Flash write-erase/read-execute/IP protection, SRAM write-execute mutual exclusion
- TRNG 및 hardware monotonic counter
- Dual-bank Flash와 address swap 기반 field update
- 512 KB ECC Flash, 128 KB SRAM(첫 64 KB ECC/parity 보호)
- 2개의 동시 샘플링 12-bit 4 Msps ADC, 2개의 CAN-FD, 2개의 advanced timer, 최대 12개 complementary PWM outputs

TI 데이터시트는 이 MCU를 automotive motor control 및 DC-AC inverter 등에도 적용 대상으로 열거한다. 다만 이는 해당 서보 드라이브의 제어 주기·정밀도·축 수·통신 부하를 충족한다는 증명이 아니다. 80 MHz Cortex-M0+의 WCET, FOC loop, encoder 처리, 통신/보안 병행 부하를 실제로 측정해야 한다.

TI 페이지의 functional-safety target/ASIL 정보는 CRA 적합성 또는 서보 드라이브 제품의 CRA 분류를 증명하지 않는다. 서로 다른 규제/기능 요구로 분리한다.

## 5. 예비 적합성 판단 및 후보 역할

| 역할 후보 | 예비 판단 | 아직 확인할 사항 |
|---|---|---|
| ST STM32G474RE를 주 제어 MCU로 유지 | 모터제어 PWM/ADC/수학 가속기 구성으로 유력한 비교 기준 | 실제 FOC 주기, 축 수, encoder, ADC sampling, CPU budget, secure update 요구 |
| ST STM32H753XI로 상위 통합 | CPU/메모리/crypto 여유가 필요한 제품에 비교 가치 | HRTIM/ADC/모터제어 timer 구성의 실제 적합성, 전력·BOM·열, 보안 boot/update integration |
| TI MSPM0G3529-Q1 단독 주 제어 | 제어 peripheral은 있으나 고성능 ST와 직접 동급 대체로 볼 수 없음 | 실제 FOC/전류루프/위치루프/통신 병행 부하에서 WCET/jitter와 제어 성능 |
| TI MSPM0G3529-Q1 보조 보안/관리 MCU | Secure boot/update, key storage, TRNG 및 CAN-FD가 통합된 점에서 후보 가치 | 보조 MCU가 추가하는 신뢰 경계, inter-processor protocol, BOM/전력, provisioning 및 실패 모드 |

현재는 ST가 실제 기준 플랫폼이라는 점만 확정되어 있다. 실제 ST 부품번호가 확인되기 전에는 G474RE/H753XI를 제품 baseline으로 선언하지 않는다. TI MSPM0G3529-Q1도 비교 후보이지 선정된 대체품이 아니다.

## 6. 동일 조건 벤치마크 계획

1. **제어 성능**: 실제 모터/전력단에서 current/speed/position loop의 주기, WCET, jitter, 안정성, 축 수 및 동시 실행 task를 측정한다.
2. **ADC/PWM 타이밍**: ADC trigger 위치, 샘플 지연, simultaneous sampling, PWM dead-time, update synchronization, fault/emergency input 경로를 비교한다.
3. **엔코더/센서**: incremental encoder/QEI, resolver interface(외부 회로 포함), absolute encoder protocol 및 timestamp 정확도를 검증한다.
4. **통신 부하**: 실제 fieldbus/industrial Ethernet stack, service interface, diagnostics, parameter access를 동시에 구동하고 CPU/RAM/DMA/bus contention을 측정한다.
5. **보안 부하**: secure boot, image verification, AES/authentication, key storage, logging을 제어 task와 병행해 worst-case 지연을 측정한다.
6. **업데이트/복구**: 잘못된 서명, 다른 모델 이미지, downgrade, 전원 차단, Flash full, A/B slot 손상 및 recovery를 시험한다.
7. **제품화**: EMC/열/전원 변동, package/pin compatibility, 공급·수명주기, errata, toolchain/SDK, 제조 provisioning 비용을 평가한다.

### 제안 평가 가중치(시험 전 초안; 점수 미부여)

| 평가축 | 제안 가중치 |
|---|---:|
| 실시간 제어 성능 및 jitter | 30% |
| ADC/PWM/encoder/통신 주변장치 적합성 | 20% |
| 보안 부트·키·업데이트·메모리 보호 | 20% |
| 메모리/격리/DMA 자원 경계 | 10% |
| 공급·수명주기·errata | 10% |
| 개발도구·SDK·BOM·통합 비용 | 10% |

가중치는 실제 제품 요구사항을 확보한 뒤 재검토한다. 시험 데이터가 없으므로 점수, 승자, 성능 우열을 임의로 산출하지 않는다.

## 7. P0 입력 및 결정 게이트

**가장 먼저 필요한 정보는 현재 ST MCU의 정확한 마킹/부품번호**다. 다음으로 제품의 제어 사양과 인터페이스를 확보한다.

- MCU top marking, BOM 주문 코드, silicon revision, package, 온도 등급
- 모터 정격/최대 전류·전압, 축 수, switching/PWM frequency, current/speed/position loop period
- ADC 채널·샘플링 동기화, encoder/resolver type, pulse rate 및 position feedback 요구
- EtherCAT/PROFINET/EtherNet-IP/CANopen/Modbus/RS-485 등 실제 통신 방식과 stack
- 외부 Flash/EEPROM, bootloader, update interface, debug lock, secure key provisioning
- 실제 firmware/RTOS, CPU/RAM/Flash utilization, interrupt/DMA mapping 및 safety boundary

**선정 게이트:** 위 정보가 확보되고 동일 시험 결과가 채워지기 전까지 MCU 선정·교체·보안 적합성 결론을 보류한다.

## 8. 공식 제조사 자료

- TI MSPM0G352x-Q1 datasheet Rev. B (SLASFO2B, revised October 2025): https://www.ti.com/lit/ds/symlink/mspm0g3529-q1.pdf
  - Security §8.18, TRNG §8.19, AESADV §8.20, Keystore §8.21; product details: https://www.ti.com/product/MSPM0G3529-Q1
- ST STM32G474RE product page: https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html
  - G474 family datasheet: https://www.st.com/resource/en/datasheet/stm32g474rc.pdf
- ST STM32H753XI product page: https://www.st.com/en/microcontrollers-microprocessors/stm32h753xi.html
  - STM32H753 datasheet DS12117: https://www.st.com/resource/en/datasheet/stm32h753xi.pdf
- ST AN5156, Introduction to security for STM32 MCUs: https://www.st.com/resource/en/application_note/dm00493651.pdf
- ST AN4992 Rev.19 (July 2026), Introduction to secure firmware install: https://www.st.com/content/st_com/en/technical-documents/an4992-introduction-to-secure-firmware-install-sfi-for-stm32-mcus-stmicroelectronics.html

## 9. 검토 한계

- 이 문서는 제조사 공식 제품 페이지·데이터시트·애플리케이션 노트의 공개 항목을 비교한 예비 자료다.
- 성능 수치는 제조사 표기이며 동일한 벤치마크 환경의 실측 결과가 아니다.
- ST 실제 사용 부품번호, 회로도, firmware, motor/drive ratings, protocol stack이 미확인이다.
- secure boot, secure update, key storage, hardware crypto의 구현 가능성은 MCU 제품명만으로 확정할 수 없다. SKU, silicon revision, option bytes, software package, provisioning, lifecycle 조건을 확인해야 한다.
- CRA 요구사항은 제품 위험평가와 Regulation (EU) 2024/2847에 따라 판정한다. 특정 MCU 기능이나 기능안전 표기가 CRA 적합성을 자동 증명하지 않는다.
