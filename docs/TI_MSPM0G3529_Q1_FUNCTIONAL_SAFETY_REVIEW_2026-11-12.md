# TI MSPM0G3529-Q1 Functional Safety Manual Review (2026-11-12)

## Executive finding

A significant official TI source is now available for the exact comparison part **MSPM0G3529-Q1**: *Functional Safety Manual for MSPM0Gx51x and MSPM0Gx52x*, document SFFS983A, Revision A, October 30, 2026. The TI product page for MSPM0G3529-Q1 links this manual and its supported-device list explicitly includes MSPM0G3529-Q1.

This changes the evidence state from “no directly applicable functional safety manual found” to “directly applicable component-level safety manual located and reviewed.” It does **not** establish SIL 3 capability or certification of a complete servo drive.

## Primary official sources

1. TI MSPM0G3529-Q1 product page:
   https://www.ti.com/product/MSPM0G3529-Q1
   - Product-page security summary: cryptographic acceleration, hardware-enforced isolation, secure boot, secure communication, secure debug, secure firmware/software update, secure storage, software IP protection.
   - Memory/security summary: up to 512 KB flash with ECC, dual-bank/address swap, 128 KB SRAM (first 64 KB ECC or parity protected), AES-128/256, secure key storage for up to four AES keys, code/data firewalls, TRNG.
   - Product page also marks functional safety compliance as targeted and PSA Level 1 as targeted. “Targeted” must not be reported as achieved certification.
2. TI *Functional Safety Manual for MSPM0Gx51x and MSPM0Gx52x*, SFFS983A, Rev A, August 2025–October 2026:
   https://www.ti.com/document-viewer/lit/html/SFFS983A
   - Header supported-device list includes MSPM0G3529-Q1.
   - Revision history states changes from August 13, 2025 to October 30, 2026 (Revision * to Revision A). It adds MSPM0Gx52x to the document scope/title and updates module-specific descriptions and safety mechanisms.
3. TI MSPM0 G-Series 80-MHz TRM, SLAU846 Rev F, dated November 5, 2026, listed on the official MSPM0G3507 product page:
   https://www.ti.com/product/MSPM0G3507
   - The TI HTML/PDF viewer currently rejects the 25,348,105-byte TRM as too large. Rev F title/revision/date metadata is verified; detailed security-register/body content and Rev E→F changes remain NOT_VERIFIED.

## Directly verified functional safety statements

### Component capability (SFFS983A §2)

TI states that the hardware component:
- was developed as a Functional Safety Element out of Context (SEooC);
- was developed according to relevant requirements of ISO 26262:2018;
- achieves systematic integrity level ASIL D;
- includes sufficient functional safety mechanisms for random fault integrity up to ASIL B.

These are component-level automotive functional-safety statements. They are not a declaration that the MSPM0G3529-Q1 alone is SIL 3 certified, nor that a servo drive using it achieves SIL 3.

### Integration concept and system assumptions (SFFS983A §§4.2–4.3)

- Internal component errors can lead to actuator output pins being driven to a safe state, device reset, or error communication to a host CPU for system response.
- TI assumes external sensor, actuator and host-controller interfaces.
- The system integrator reviews the recommended diagnostics in the safety analysis report (FMEDA) and safety manual and selects/implements suitable diagnostics.
- The system integrator provisions an actuator-disable-mechanism controller through the host controller.
- The host controller monitors communication loss and determines when the MCU is faulted.
- The stated system assumptions include random-fault architectural metrics up to ASIL B, systematic-fault requirements up to ASIL D, FTTI greater than 10 ms, and MPFDTI less than 8 hours.
- The manual identifies several IP blocks as not safety-critical/QM for this safety concept: DEBUG, RTC, AES, TRNG, KEYSTORE, MATHACL and DFT. It explicitly says these QM IPs shall not be used in safety-critical applications. It recommends disabling debug in safety-critical applications.
- TI assumes that the SRAM bank without ECC/parity protection is not used in safety-critical application contexts.
- TI recommends not programming flash during safety-critical tasks.
- If external safety mechanisms are used, the system integrator is responsible for dependent-failure analysis at system level.

### Mechanism inventory

SFFS983A §6 lists 74 functional-safety mechanism entries, including:
- periodic static-configuration register reads/CRC comparison;
- ADC plausibility and window checks;
- comparator and watchdog tests;
- CPU software tests and diversified redundancy;
- SRAM parity/ECC and flash SECDED/ECC-related checks;
- flash CRC, periodic readback and write protection;
- PWM generation/fault checks and timer fault-to-safe-state handling;
- clock, brownout, external voltage and boot-process monitoring;
- CAN-FD and serial-interface diagnostics;
- common-cause-failure mechanisms.

The presence of a mechanism in the manual is not proof that an application has implemented it. The system integrator must select, configure, execute and verify the applicable diagnostics under the manual's assumptions and the safety analysis report.

## Important implications for servo-drive architecture

1. Do not place AES/TRNG/KEYSTORE/debug inside the credited safety function without a separate safety justification; the manual explicitly classifies these IPs as QM/non-safety-critical for this safety concept.
2. Keep the cybersecurity trust domain and the safety control path distinct in the architecture and evidence model. Security features can support CRA/product security but do not automatically contribute to functional-safety metrics.
3. Treat the external actuator-disable mechanism and host-controller communication-loss monitoring as system-level design responsibilities. The MCU alone does not complete the safe-state chain.
4. Use only the SRAM region with ECC/parity protection in safety-critical application contexts, subject to exact device documentation and implementation constraints.
5. Avoid flash programming during safety-critical tasks unless a justified system design and the applicable safety manual explicitly permit the relevant operation.
6. Before using any ASIL capability claim, retrieve the exact TI FMEDA/safety analysis report and confirm its scope, assumptions, diagnostic coverage, failure rates, hardware metrics, safety manual conditions, and device/revision applicability.

## SIL 3 interpretation boundary

ASIL D is not interchangeable with IEC 61508 SIL 3. No direct SIL 3 claim can be inferred from ASIL D systematic capability or ASIL B random-fault capability. A SIL 3 servo-drive claim requires a complete IEC 61508/IEC 61800-5-2 safety lifecycle and system-level evidence, including architecture, failure-rate calculations, diagnostic coverage, systematic capability, independence/dependent failure analysis, safe-state timing, software lifecycle and validation. This TI manual is useful component evidence, not the product's SIL certificate.

## Status and next verification

| Item | Status |
|---|---|
| SFFS983A Rev A document metadata | VERIFIED |
| MSPM0G3529-Q1 included in supported-device list | VERIFIED |
| Component systematic ASIL D / random ASIL B statements | VERIFIED |
| Stated assumptions, including FTTI >10 ms and MPFDTI <8 h | VERIFIED |
| QM/non-safety-critical status for AES/TRNG/KEYSTORE/DEBUG | VERIFIED |
| Application-level implementation/diagnostic selection | UNVERIFIED |
| Exact G3529-Q1 FMEDA values and diagnostic coverage | NOT YET RETRIEVED |
| G3529-Q1 TRM Rev F register-level security details | NOT_VERIFIED |
| IEC 61508 SIL 3 / IEC 61800-5-2 product achievement | NOT ESTABLISHED |

Next: obtain the exact G3529-Q1 FMEDA/safety analysis report and full TRM Rev F content, then map the safety manual's host/actuator assumptions to IF-01..IF-09 and the test/evidence register. Do not infer numeric FMEDA values or SIL equivalence from the manual's ASIL summary.


## FMEDA / safety-analysis report access route

A public web search did not locate an exact MSPM0G3529-Q1 FMEDA or Safety Analysis Report. TI's general Functional Safety page says customers should contact their local sales representative when a selected product's analysis report is not available:
https://www.ti.com/en-us/technologies/functional-safety

TI's general safety-collateral overview also states that access to the safety manual / safety analysis report / FMEDA package may require a valid Safety NDA:
https://www.ti.com/document-viewer/lit/html/SPRAD57

These are general TI process statements, not proof that a G3529-Q1 FMEDA is unavailable or that its specific access terms are identical. The exact G3529-Q1 FMEDA availability, NDA requirements, cost and delivery route remain UNVERIFIED. Do not invent or assume a free download route.
