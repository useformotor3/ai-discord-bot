# Main-only CRA archive audit: reports #40–#55
- Audit date: 2026-11-12
- Source branch: main (original reports preserved; no edits to main)
- Audit branch: cra-project-foundation
- Method: compare archived report text and claimed legal locations against Regulation (EU) 2024/2847 on EUR-Lex. File-level verdicts do not imply every sentence has the same status.
- Limitation: this is an AI-assisted source re-check, not independent legal advice or third-party legal review.

## Executive result

| Report | Archive file time | Commit | File verdict | Principal issue |
|---:|---|---|---|---|
| 40 | 03:15:39 | [b43a3b8](https://github.com/useformotor3/ai-discord-bot/commit/b43a3b8b2bcb32eaa6f349cb940b0a75c898f81a) | PARTIALLY_VERIFIED | Secure-by-default and attack-surface minimisation are real requirements; quoted text is not exact and implementation examples are overstated as mandatory. |
| 41 | 03:20:43 | [dd4f3d4](https://github.com/useformotor3/ai-discord-bot/commit/dd4f3d418778c7d1ed8c65c1dab29c30b8b4ed0e) | CONFLICT | Annex structure and quoted lettered subpoints do not match the Regulation; mandatory disabled interfaces/password-change claims overstate the text. |
| 42 | 03:25:33 | [7d83430](https://github.com/useformotor3/ai-discord-bot/commit/7d83430078621c46eef23f2e857d9acdf40984ac) | CONFLICT | Invented “secure by default enforcement mechanisms” and misnumbered access-control requirements. |
| 43 | 03:30:49 | [7031bf8](https://github.com/useformotor3/ai-discord-bot/commit/7031bf86858623e44e4ca49daabdec7e3deac128) | CONFLICT | Unsupported assertion that a servo drive is an Important Class I product; composite/non-verbatim legal quotation. |
| 44 | 03:35:34 | [a60edec](https://github.com/useformotor3/ai-discord-bot/commit/a60edec975b337142d0cd660c7954a2d53141152) | CONFLICT | Reporting duties attributed to Article 11 instead of Article 14; scope expanded to any vulnerability/incident; final-report timing omitted or generalized. |
| 45 | 03:40:41 | [4eef4c8](https://github.com/useformotor3/ai-discord-bot/commit/4eef4c8e3fa4fa373f8691adaba936ad953605f6) | CONFLICT | Free updates wrongly placed in Annex I Part I; signature algorithms, dual-bank and rollback presented as legal mandates without textual basis. |
| 46 | 03:45:37 | [1a814fb](https://github.com/useformotor3/ai-discord-bot/commit/1a814fbb5c4aab7e11411828f8590494346e6081) | CONFLICT | Article 14 scope/quote inaccurate; automatic reporting and telemetry architecture are not prescribed; EN 18031 applicability is not established for a generic servo drive. |
| 47 | 03:50:40 | [713c9d2](https://github.com/useformotor3/ai-discord-bot/commit/713c9d2db571404c907d079e4488f36612134479) | CONFLICT | Invented Annex I section/point quotations; CRA does not prescribe SIL-core separation, STO activation or a universal safe-state update architecture. |
| 48 | 03:55:34 | [74bd8bf](https://github.com/useformotor3/ai-discord-bot/commit/74bd8bf06c8abf77bf85b2eea278e545b32c7bbc) | CONFLICT | Annex I point (h) and Recital (28) quotes do not match the cited legal text; specific SIL/IEC update procedure is engineering/safety assessment, not quoted CRA wording. |
| 49 | 04:00:56 | [69f5e4b](https://github.com/useformotor3/ai-discord-bot/commit/69f5e4b518d57f6264757012dc8086134bf14f9e) | PARTIALLY_VERIFIED | Secure decommissioning and secure removal of user data are real Annex II/Annex I requirements, but the report misattributes Annex II text to Annex VII and adds cryptographic erasure/advance notice as if mandated. |
| 50 | 04:05:33 | [6821c06](https://github.com/useformotor3/ai-discord-bot/commit/6821c06d1e49c18acec0d8b222c80906930acc7f) | CONFLICT | Free update concept is real, but Part I/Section 2 citation and zero-downtime/hot-patching mandate are unsupported. |
| 51 | 04:10:41 | [dfc0c05](https://github.com/useformotor3/ai-discord-bot/commit/dfc0c05060894c7b5596c7238da2250e85de06ac) | CONFLICT | Article 14/Annex II/Article 13 citations are mixed; minimum-five-year wording omits expected-use-under-five-years exception; quotes are not source-verbatim. |
| 52 | 04:15:41 | [db00055](https://github.com/useformotor3/ai-discord-bot/commit/db00055bad56565c827cdc237c524a07d620c94e) | CONFLICT | Article 10(6) and Annex I point labels are wrong; dual-bank, hot-patching and zero-downtime are falsely described as forced by CRA. |
| 53 | 04:20:38 | [1fec519](https://github.com/useformotor3/ai-discord-bot/commit/1fec5198a6cad66a6305bd621da7fc0c37fbe2c0) | CONFLICT | Article 13(6) is component-vulnerability reporting/remediation, not support-period/free-update text; Annex I Part I(2)(g) is data minimisation, not DoS/update requirements. |
| 54 | 04:25:32 | [62349f3](https://github.com/useformotor3/ai-discord-bot/commit/62349f336a2ec66c5893b52df7e2a59ebbcbcef1) | CONFLICT | Article 13(4) and purported Annex I point references are wrong; quoted support-period wording is not verbatim and reverses/changes the legal test. |
| 55 | 04:30:49 | [787fb7d](https://github.com/useformotor3/ai-discord-bot/commit/787fb7d3d9f56c0639201c1a625ce19d38f721b3) | CONFLICT | Annex I Part I Section 2 does not exist in the cited form; free update text is misquoted and the tailor-made business-user exception is omitted. |

Result: 2 PARTIALLY_VERIFIED / 14 CONFLICT. No report in this batch is approved for verbatim legal quotation without correction. The original archive files remain unchanged.

## Correct legal map (authoritative EUR-Lex text)

Primary source: Regulation (EU) 2024/2847, EUR-Lex:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

1. **Article 13(2)–(4):** cybersecurity risk assessment and its documentation. Article 13(6) concerns a vulnerability in an integrated component and communication/remediation with the component manufacturer/maintainer. It is not the support-period clause.
2. **Article 13(8):** support period must reflect expected use, reasonable user expectations, product nature/intended purpose and relevant Union law. It is at least five years, except where the product is expected to be used for less than five years, in which case the support period corresponds to expected use. Basis must be included in technical documentation.
3. **Article 13(19):** end date of support period (at least month and year) must be clearly specified at purchase; a user notification when support ends is required where technically feasible.
4. **Article 14:** reporting is for (i) actively exploited vulnerabilities contained in the product and (ii) severe incidents affecting product security. It is not a blanket report of every vulnerability. For actively exploited vulnerabilities: early warning within 24 hours, vulnerability notification within 72 hours, final report no later than 14 days after corrective/mitigating measure is available. For severe incidents: early warning within 24 hours, incident notification within 72 hours, final report within one month after incident notification.
5. **Annex I Part I(2):** risk-assessment-based product properties. Relevant points include (b) secure-by-default, (c) vulnerability remediation/security-update handling, (d) access control, (e) confidentiality, (f) integrity, (g) data minimisation, (h) essential-function availability/DoS resilience, (i) impact on connected devices/networks, (j) attack-surface limitation, (k) incident-impact mitigation, (l) security-relevant activity recording/monitoring, (m) permanent secure removal of data/settings.
6. **Annex I Part II(1)–(8):** manufacturer vulnerability-handling process. Point (7) secure update distribution; point (8) disseminate available security updates without delay and, unless otherwise agreed for a tailor-made product with a business user, free of charge.
7. **Annex II point 7 and point 8(d):** user information must state support period end date and provide secure decommissioning instructions, including how user data can be securely removed.
8. **Annex VII:** technical documentation; do not relabel Annex II user-instruction requirements as Annex VII.

## Key technical/legal separation

- CRA does not name RSA-3072, ECDSA, dual-bank flash, A/B slots, hot patching, rollback, zero downtime, SIL 3, STO, safety-core separation, or a particular bootloader as universally mandatory hardware/software solutions in the cited provisions.
- These may be sensible engineering controls for a particular servo-drive risk/safety case, but they must be labelled **design proposal / risk-control option / verification target**, not direct CRA quotation or universal statutory mandate.
- CRA Article 13(2) requires risk assessment to consider health and safety impacts. That does not itself prescribe a specific SIL partition or STO response.
- Product classification as Important Class I/II cannot be inferred merely because the product is an industrial servo drive. Assess exact product boundary, intended purpose, product category, and any security-related MCU/processor functionality separately.

## Corrective actions for future archive reports

1. Reject generated direct quotations unless exact source text and exact Annex/Part/point are recorded.
2. Store article/annex/part/point as separate structured fields; do not infer numbering from a prompt summary.
3. Keep statutory obligation, Commission non-binding guidance, manufacturer implementation choice, and product-specific applicability as distinct claim types.
4. For reporting, use Article 14 and keep actively exploited vulnerability and severe incident tracks separate.
5. For support period, use Article 13(8); for free security updates use Annex I Part II(8); for secure decommissioning use Annex II point 8(d) and Annex I Part I(2)(m).
6. Treat automatic reporting, remote telemetry, hot patch, zero downtime and cryptographic erasure as design choices unless another product-specific law/standard/contract establishes them.

## Source locations checked

- EUR-Lex Article 13: lines 888–905 (risk assessment, component vulnerabilities, support period).
- EUR-Lex Article 14: lines 939–964 (reportable events and time limits).
- EUR-Lex Annex I: lines 1743–1773 (Part I product properties and Part II vulnerability handling).
- EUR-Lex Annex II: lines 1776–1794 (support information, secure installation and decommissioning).
- Commission C(2026) 5252 publication page (27 July 2026): https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation. Guidance is non-binding; use it as interpretive context, not replacement legal text.

## Addendum: Commission C(2026) 5252 guidance cross-check

The official Commission publication page confirms publication on 27 July 2026 and explicitly states that the guidance is non-binding:
https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation

The complete text was inspected through a structured reproduction that identifies the official Annex PDF filename and SHA-256 and states that its text was verified against that PDF:
https://cra.orcwg.org/official-guidance/
The reproduction is a navigation/transcription aid; the Commission PDF remains authoritative. Relevant additional interpretation:
- Points 125–126: support period reflects expected use, reasonable user expectations, product nature and relevant Union law; at least five years unless expected use is shorter.
- Point 126 explicitly says five years is not the default for every product. Point 125 and Recital 60 expect longer support where reasonable expected use is longer; the guidance specifically notes industrial control systems often remain in use significantly longer.
- Point 127 explains Article 13(19): support end date (month/year) is indicated at purchase; a notification after expiry is displayed where technically feasible.
- Points 139–145: product classification depends on the product's core functionality and actual technical capabilities; mere integration of a component with an important/critical category function does not automatically classify the whole product in that category.
- Points 209–210: Article 14 reporting applies to actively exploited vulnerabilities contained in the product and severe incidents, and continues after the vulnerability-handling support period ends.
- Point 222: Article 13(6) is upstream reporting of vulnerabilities in integrated components.

For the servo-drive project, do not default to a five-year support period without expected-use evidence. Industrial duty cycles, machine lifetime, service expectations and sector-specific legislation should be considered in the documented support-period rationale. Do not automatically classify the whole servo drive as Important Class I because it contains a security-capable MCU; evaluate the marketed product's core functionality and separately supplied component boundary.

## TI G-Series TRM Rev F access status

TI's official product pages list the MSPM0 G-Series 80-MHz Technical Reference Manual Rev F dated 5 November 2026. The TI page identifies the manual as a 25 MB PDF; the web viewer/download path failed in this session due content-size/decoding limits. Thus **revision/date metadata is verified, but the Rev F security chapter, register descriptions, and revision changes remain NOT_VERIFIED**. Do not derive register-level or security-feature claims from the title/revision index alone. Relevant TI official product page:
https://www.ti.com/product/MSPM0G3507
