# TI SFFS983A to Servo-Drive Safety Integration Matrix (reference only)

## Purpose and boundary

This matrix maps the TI *Functional Safety Manual for MSPM0Gx51x and MSPM0Gx52x* (SFFS983A Rev A, October 2026) to generic servo-drive hardware boundaries and candidate verification activities. MSPM0G3529-Q1 is included in the manual's supported-device list. The mapping is a design-review aid only; it does not select TI as the target MCU, prove implementation, establish diagnostic coverage, or claim SIL 3.

Primary source:
https://www.ti.com/document-viewer/lit/html/SFFS983A

Supporting architecture:
- `SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md` IF-01..IF-09
- `SECURITY_TEST_EVIDENCE_REGISTER.md` TST-* IDs

## Integration mapping

| SFFS983A mechanism family / example | Servo-drive boundary | Candidate system verification | Evidence required | State |
|---|---|---|---|---|
| Static configuration register readback / CRC (§6.3.1) | MCU configuration, timer/ADC/communication setup | Inject or simulate configuration corruption; confirm detection, fault reporting and safe reaction | Register list, reference CRC, diagnostic period, fault response trace | PROPOSED / NOT_RUN |
| ADC software test, trigger overflow, window comparator, plausibility (§6.3.2–6.3.6) | IF-04 encoder/resolver/current/voltage feedback front-end | Sensor open/short/out-of-range, stuck value, trigger overflow and plausibility fault injection | Sensor interface spec, diagnostic threshold/latency, fault-injection log | PROPOSED / NOT_RUN |
| Comparator test, external pin input, hysteresis, redundant comparator (§6.3.7–6.3.10) | IF-04 analog feedback / current limit / hardware fault input | Threshold drift, stuck comparator, pin short/open and redundant channel mismatch | Comparator configuration, analog tolerance budget, diagnostic coverage evidence | PROPOSED / NOT_RUN |
| WWDT/IWDT tests and redundant watchdog (§6.3.11–6.3.14) | IF-08 clock/reset/watchdog and IF-03 output inhibit | CPU stall, missed task deadline, watchdog window violation, reset-loop tests | Watchdog configuration, reset cause, output-state timing capture | PROPOSED / NOT_RUN |
| CPU software tests, bus tests, diversified redundancy (§6.3.16–6.3.18) | Motion-control compute path | CPU register/ALU/bus fault injection and task-level plausibility checks | Safety manual restrictions, test library version, diagnostic execution interval | PROPOSED / NOT_RUN |
| SRAM parity/ECC and logic tests (§6.3.21–6.3.25) | Motion state, command buffers, safety state | Correctable/uncorrectable memory fault injection; verify detection, containment and safe reaction | Exact SKU memory map, ECC/parity coverage, protected/unprotected bank allocation | PROPOSED / NOT_RUN |
| Flash SECDED, CRC, readback, ECC logic and write protection (§6.3.26–6.3.30) | IF-05 NVM / boot and firmware update | Flash corruption, ECC event, unauthorized write and image readback tests | Flash layout, protected region map, ECC response, update state machine | PROPOSED / NOT_RUN |
| DAC self-test and FIFO underrun (§6.3.31–6.3.32) | IF-04 analog output/reference or analog command path, if used | DAC output mismatch, FIFO underrun, ADC loopback diagnostic | Actual DAC use case, analog feedback topology and diagnostic coverage | PROPOSED / NOT_RUN |
| DMA function/channel/data CRC tests (§6.3.33–6.3.35) | ADC sample transfer, motion buffers, communication DMA | Corrupt DMA source/destination/length/trigger; confirm data integrity and bounded fault response | DMA channel ownership, memory access policy, CRC strategy | PROPOSED / NOT_RUN |
| GPIO loopback and redundant I/O (§6.3.36–6.3.37) | IF-03 gate enable/fault pins; IF-04 sensor digital inputs | Stuck-at, open/short, polarity and redundant input mismatch | Schematic, pull state, electrical fault model, diagnostic interval | PROPOSED / NOT_RUN |
| Timer PWM generation/fault-to-safe-state/input capture/period monitor (§6.3.38–6.3.42) | IF-03 MCU-to-gate-driver PWM/enable/fault | PWM missing/stuck/wrong period, fault input activation, timer mismatch; measure safe-state transition | Gate-driver truth table, independent inhibit path, propagation timing, safety requirement | PROPOSED / NOT_RUN |
| I2C/SPI/UART loopback, CRC, timeout and redundant transmission (§6.3.43–6.3.53) | IF-02 inter-domain links; IF-05 external NVM; IF-09 fixture | CRC error, timeout, stuck bus, replay/sequence error, channel mismatch | Protocol definition, end-to-end protection, timeout and retry policy | PROPOSED / NOT_RUN |
| Clock monitors, PLL startup, BOR, external voltage monitor (§6.3.55–6.3.65) | IF-08 power/clock/reset | Clock stop/drift, PLL failure, undervoltage/overvoltage, brownout and reset sequencing tests | Rail/clock limits, supervisor tolerances, reset cause capture, safe-output timing | PROPOSED / NOT_RUN |
| Boot process monitor (§6.3.62) | IF-05 boot chain / IF-07 service lifecycle | Boot interruption, invalid boot state, corrupted startup sequence; confirm safe state and recovery policy | Boot flow, lifecycle state, fault reaction, recovery authorization | PROPOSED / NOT_RUN |
| CAN-FD loopback, timeout, timestamp, SRAM ECC mechanisms (§6.3.66–6.3.70) | IF-01 external fieldbus; IF-02 communication-to-motion boundary | CAN-FD frame fault, timeout, timestamp error, buffer ECC and end-to-end communication protection | Actual bus selection, safety protocol, host supervision and timeout budget | PROPOSED / NOT_RUN |
| Common-cause/dependent failure mechanisms (§6.3.74) | Shared power, reset, clock, memory access bus | Analyze common clock, VDD, reset and shared-bus failure; verify independence assumptions | Dependent failure analysis, schematic, fault tree, system safety analysis | PROPOSED / NOT_RUN |

## Required system-level constraints to carry forward

SFFS983A §4.3 makes the following assumptions for the TI component safety concept:
- The system integrator selects and implements applicable diagnostics using the FMEDA and safety manual.
- The host controller provisions the actuator-disable mechanism and monitors communication loss.
- FTTI >10 ms and MPFDTI <8 h are assumptions of this TI safety concept, not universal servo-drive limits.
- DEBUG, RTC, AES, TRNG, KEYSTORE, MATHACL and DFT are QM/non-safety-critical IPs in this safety concept; they must not be credited as safety mechanisms.
- The SRAM bank without ECC/parity protection is not used in safety-critical application contexts.
- Flash programming is not performed during safety-critical tasks per TI's recommendation.

These conditions must be checked against the actual product safety requirements and exact part documentation. The matrix does not replace the device FMEDA or system safety case.

## Separation from CRA cybersecurity evidence

A diagnostic test for functional safety is not automatically a CRA cybersecurity test, and vice versa. For example, flash CRC/ECC diagnostics do not prove firmware authenticity; secure boot does not by itself prove random-hardware-fault metrics. Keep separate evidence chains:
- functional safety: safety requirement → safety mechanism → FMEDA assumptions/metrics → implementation → validation;
- cybersecurity/CRA: threat/requirement → security control → vulnerability handling/update process → security test → technical documentation.

## Open items

1. Retrieve exact MSPM0G3529-Q1 FMEDA/safety analysis report and verify failure rates, diagnostic coverage, device mission-profile assumptions and safety metrics.
2. Confirm all SFFS983A safety mechanisms against the exact G3529-Q1 data sheet, TRM and errata.
3. Define target servo-drive safety functions, safe state, FTTI and diagnostic requirements from hazard/risk analysis.
4. Map the selected mechanisms to the actual schematic, firmware task architecture and test equipment.
5. Run tests only on a defined DUT with approved procedures and record measured results. Until then all rows remain NOT_RUN.
6. Do not infer IEC 61508 SIL 3 from ASIL D/ASIL B statements.
