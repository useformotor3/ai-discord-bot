# Main-only CRA archive audit: reports #56–#59
- Audit date: 2026-11-12
- Source branch: main; original archive/history/state preserved
- Audit branch: cra-project-foundation
- Method: source text reviewed from GitHub commit diffs and compared with Regulation (EU) 2024/2847 on EUR-Lex.
- Limitation: AI-assisted source comparison; not independent legal advice or third-party legal review.

## Executive result

| Report | Time | Commit | File verdict | Main issue |
|---:|---|---|---|---|
| 56 | 04:35:34 | [be6bda0](https://github.com/useformotor3/ai-discord-bot/commit/be6bda0705a01bc863ab65de07463b3f0fb52004) | CONFLICT | Article 14 reporting scope expanded; mandatory notification tracks conflated; “automatic” reporting and recipient routing overstated; final reports omitted. |
| 57 | 04:40:37 | [987b4b6](https://github.com/useformotor3/ai-discord-bot/commit/987b4b67cd31bff738bd63db4c82b282e70eb70f) | PARTIALLY_VERIFIED | CVD and vulnerability contact requirements are real, but Annex location is wrong and the purported quote is composite/non-verbatim. |
| 58 | 04:45:40 | [7d8609d](https://github.com/useformotor3/ai-discord-bot/commit/7d8609d3d9d2fa6641284d6b9249021a8bdfc68a) | PARTIALLY_VERIFIED | Secure-by-default and access control are real; default port shutdown and mandatory first-boot password change are not prescribed verbatim; legal quote/point structure inaccurate. |
| 59 | 04:50:42 | [ee5c758](https://github.com/useformotor3/ai-discord-bot/commit/ee5c75840ee4868c7d3f56f3895c8bc7b50cfe44) | CONFLICT | Article 13(2) misused for free updates; support period, free update and secure-by-default provisions conflated; quotes/Annex location inaccurate. |

Result: 2 PARTIALLY_VERIFIED / 2 CONFLICT. No report in this batch is fully VERIFIED for direct legal quotation.

## Report-specific findings

### #56 — Article 14 reporting
- Article 14(1) requires notification of an **actively exploited vulnerability contained in the product**, not every exploitable vulnerability or every vulnerability.
- Article 14(2): actively exploited vulnerability track: early warning within 24 hours; vulnerability notification within 72 hours; final report no later than 14 days after a corrective/mitigating measure is available.
- Article 14(3)–(4): severe incident affecting product security track: early warning within 24 hours; incident notification within 72 hours; final report within one month after incident notification.
- Notifications are submitted through the single reporting platform to the CSIRT designated as coordinator and are simultaneously accessible to ENISA. This is not a requirement that the manufacturer's system autonomously/automatically report, nor a direct Article 14 submission to every market-surveillance authority. Article 16(3) addresses CSIRT sharing necessary information with market-surveillance authorities.
- Article 14(8) user information applies to impacted users and, where appropriate, all users; this does not turn every detected vulnerability into a mandatory Article 14 report.
- Report #56 merges the two reporting tracks, says “exploitable vulnerabilities” broadly, describes automatic reporting infrastructure, and omits distinct final-report deadlines. File verdict CONFLICT.

### #57 — CVD and vulnerability contact
- CVD policy: Annex I Part II(5), not “Annex I Part I, Section 2”.
- Measures to facilitate vulnerability information sharing, including a contact address: Annex I Part II(6).
- User-facing single point of contact and where the CVD policy can be found: Annex II point 2.
- Report's core CVD/contact concepts are supported, but its legal location is wrong and its block quote does not match the numbered source text. Recital 76 provides additional context for the purpose of CVD but must not be quoted as Annex I text.
- File verdict PARTIALLY_VERIFIED; direct quote REJECTED pending exact-source replacement.

### #58 — Secure by default
- Annex I Part I(1) is the risk-based overall cybersecurity requirement; Annex I Part I(2)(b) is secure-by-default configuration, including ability to reset to original state.
- Part I(2)(d) concerns protection from unauthorised access through appropriate control mechanisms; Part I(2)(j) concerns limiting attack surfaces, including external interfaces.
- The CRA does not expressly prescribe that every HTTP/FTP/SSH/Telnet port or every JTAG/debug interface must always be disabled in every product, nor does it prescribe a universal forced password change on first boot. These may be risk-based design choices where appropriate, but must be labelled as implementation proposals rather than direct quotations.
- Report #58 uses inaccurate numbering/quotation and presents product-specific hardening options as universal statutory commands. The core secure-by-default principle is supported; file verdict PARTIALLY_VERIFIED, direct quote REJECTED.

### #59 — Article 13(2), support period and free updates
- Article 13(2) is the cybersecurity risk-assessment provision; it is not the free-update clause.
- Article 13(8) governs support-period determination: it reflects expected use, reasonable user expectations, product nature/intended purpose and relevant Union law; five years is the general minimum, except where expected use is less than five years, in which case support period corresponds to expected use.
- Annex I Part II(8) is the free-of-charge security-update provision, subject to the tailor-made product/business-user agreement exception.
- Secure-by-default is Annex I Part I(2)(b), not a quoted Annex I “Section 1” subpoint (a) as shown in the report.
- Report #59 merges distinct legal obligations and its Article 13(2) quote is not the cited free-update text. File verdict CONFLICT.

## Correct source locations
Primary source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 13(2),(8): risk assessment and support period.
- Article 14(1)–(4),(8): separate actively exploited vulnerability and severe-incident reporting tracks.
- Article 16(3): CSIRT sharing with market-surveillance authorities.
- Annex I Part I(1),(2)(b),(d),(j): risk-based product properties, secure-by-default, access control and attack-surface limitation.
- Annex I Part II(5),(6): CVD policy and vulnerability contact address.
- Annex I Part II(8): free security updates.
- Annex II point 2: single point of contact and CVD policy location.

## Correction rules
1. Do not replace “actively exploited vulnerability” with “any exploitable vulnerability”.
2. Preserve the separate final-report deadlines: 14 days after corrective/mitigating measure availability (actively exploited vulnerability) versus one month after incident notification (severe incident).
3. Distinguish the CSIRT/ENISA reporting platform from downstream market-surveillance information sharing.
4. Use Annex I Part II(5) and (6) for CVD/contact; Annex II point 2 for user-facing single point of contact.
5. Distinguish secure-by-default principle from implementation choices such as disabling individual services, debug ports or mandatory first-boot password reset.
6. Keep Article 13(2) risk assessment, Article 13(8) support period and Annex I Part II(8) free security updates as separate atomic requirements.

Original main archive files/history/state were not modified.
