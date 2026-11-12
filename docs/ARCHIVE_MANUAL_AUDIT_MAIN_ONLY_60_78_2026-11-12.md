# Main-only CRA archive audit #60–#78 (2026-11-12)

## Scope and method

This batch covers the 19 automatic research reports #60–#78 added to the public `main` branch on 2026-11-12. Each report was retrieved from its individual Git commit diff and compared with the current EUR-Lex text of Regulation (EU) 2024/2847. The original archive files, `history.json`, and `state.json` were not changed.

Primary legal source: EUR-Lex, Regulation (EU) 2024/2847, current consolidated text dated 20 November 2024:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

Key locations checked:
- Article 13(2)–(9): risk assessment, component vulnerability reporting, systematic documentation, support period, CVD policy, and update availability (EUR-Lex lines 888–908).
- Article 14(1)–(8): mandatory reporting tracks for actively exploited vulnerabilities and severe incidents (lines 939–973).
- Annex I Part I(1)–(2)(a)–(m): product cybersecurity properties (lines 1743–1762).
- Annex I Part II(1)–(8): vulnerability-handling process requirements (lines 1763–1773).
- Annex II points 2, 7, 8: user-facing contact, support-period information, secure installation/decommissioning instructions (lines 1776–1794).

## Controlling legal distinctions

1. **Support period:** Article 13(8), not Article 13(2), (6), (7), Article 11, or Article 14. It must reflect expected use, reasonable user expectations, product nature/intended purpose and relevant Union law. The general floor is five years, except where expected use is less than five years, in which case the support period corresponds to expected use.
2. **Free security updates:** Annex I Part II(8), including the exception where the manufacturer and a business user agree otherwise for a tailor-made product. Do not replace this with a fabricated Article 13(7) or Article 14 quote.
3. **Update remediation/distribution:** Annex I Part II(2) requires addressing/remediating vulnerabilities without delay and separating security updates from functionality updates where technically feasible. Part II(7) concerns secure distribution, automatic where applicable. Part I(2)(c) concerns product capability for vulnerability remediation through security updates and default-enabled automatic installation where applicable, with opt-out, notification and temporary postponement.
4. **CVD:** Annex I Part II(5). Measures/contact address for vulnerability sharing: Part II(6). User-facing single point of contact and CVD information: Annex II point 2.
5. **Secure by default / access / attack surface:** Annex I Part I(2)(b), (d), and (j), respectively. These are risk-based outcome requirements; they do not prescribe universal MFA, mandatory first-boot password change, or unconditional disablement of every service/debug interface.
6. **Data minimisation / availability / telemetry:** Part I(2)(g) is data minimisation; (h) protects essential/basic-function availability and resilience against DoS. There is no general CRA clause at Part I(2)(h) that requires all telemetry to be opt-in.
7. **Secure boot / digital signatures / hardware security modules:** CRA Annex I is technology-neutral. Secure Boot, signed firmware, HSM/SE, dual-bank, rollback, hot patching and zero downtime can be engineering controls justified by risk, but are not universally prescribed as specific hardware implementations by the cited text.
8. **Article 14:** Reporting is limited to actively exploited vulnerabilities contained in the product and severe incidents affecting product security. The tracks differ: vulnerability final report within 14 days after a corrective/mitigating measure becomes available; severe-incident final report within one month after incident notification. Article 14 is not the free-update or support-period provision.

## File-level results

| Report | Original file | Verdict | Main findings |
|---|---|---|---|
| #60 | `research_archive/2026-11-12_045535.md` | PARTIALLY_VERIFIED | CVD and no-cost security update themes are valid. Part I(2)(g) is misidentified (it is data minimisation); update handling is Part I(2)(c) and Part II(2)/(7)/(8), while CVD is Part II(5). The purported Part II quotation is incomplete/composite and is not acceptable as a verbatim quotation. |
| #61 | `research_archive/2026-11-12_050055.md` | PARTIALLY_VERIFIED | Secure-by-default is a real requirement at Part I(2)(b), and attack-surface limitation at (j). The quoted numbering/location is unreliable; mandatory MFA, forced unique passwords, and blanket disabling of named protocols/ports are not universal express CRA commands. |
| #62 | `research_archive/2026-11-12_050534.md` | CONFLICT | Article 13(7) is systematic documentation of cybersecurity aspects, not free patch/support period. Part I(2)(2) is not a valid citation structure. The quoted Article 13(7) and Annex I text are fabricated/mislocated. |
| #63 | `research_archive/2026-11-12_051044.md` | PARTIALLY_VERIFIED | Secure-by-default and attack-surface reduction are valid themes. The report misnumbers them as Annex I Section 1 paragraphs 1(b)/1(g)/1(h); actual locations are Part I(2)(b) and (j). Blanket disabling of JTAG/UART/services is an implementation choice, not a universal verbatim command. |
| #64 | `research_archive/2026-11-12_051536.md` | CONFLICT | Article 13(7) is misused as free-patch duty. Part I Section 2(g) is not the vulnerability-handling clause; Part I(2)(g) is data minimisation. The alleged Article 13(7) and Annex I quotations do not match the law. |
| #65 | `research_archive/2026-11-12_052039.md` | CONFLICT | The support-period rule is misstated as expected lifetime or minimum five years, whichever is longer; Article 13(8) instead has the under-five-year expected-use exception. The quotation is synthetic and cites Article 13(6), which concerns vulnerabilities in integrated components. |
| #66 | `research_archive/2026-11-12_052533.md` | CONFLICT | Article 14(2) is not a free-update obligation; Article 14 concerns reporting of actively exploited vulnerabilities/severe incidents. The alleged Article 14(2) quotation does not appear in the law. |
| #67 | `research_archive/2026-11-12_053050.md` | CONFLICT | Free updates belong to Part II(8), not a general Part I Section 2(2) clause. Automation is conditional (“where applicable”); mandatory remote/batch automatic application is overstated. The quote combines/non-verbatim paraphrases multiple requirements. |
| #68 | `research_archive/2026-11-12_053533.md` | CONFLICT | Article 11 is general product safety, not manufacturer support-period/free-update duties. Article 13(8) is the support-period clause. The Article 11 and Annex I quotes are fabricated/mislocated; product classification as Class I/II is unsupported. |
| #69 | `research_archive/2026-11-12_054043.md` | CONFLICT | Part I(2)(g) is data minimisation, not updates; (h) is availability/DoS resilience, not telemetry consent. Both quoted passages are not authentic legal text. |
| #70 | `research_archive/2026-11-12_054539.md` | CONFLICT | Access control is Part I(2)(d), but the alleged quote about HSM, cryptographic boot and runtime integrity is a synthetic composite. Secure Boot/HSM/runtime attestation are not universal explicit CRA implementation mandates. |
| #71 | `research_archive/2026-11-12_055036.md` | CONFLICT | Article 11(2) is not the claimed manufacturer free-update provision. CVD is Part II(5); free updates are Part II(8). Both purported quotations are not present in the Regulation. |
| #72 | `research_archive/2026-11-12_055533.md` | CONFLICT | Article 14(3) concerns severe-incident reporting, not support period/free updates. Article 13(8) governs support period; Part II(8) governs free updates. The purported quotes are not authentic. |
| #73 | `research_archive/2026-11-12_060102.md` | PARTIALLY_VERIFIED | Article 13(8) is correctly identified as the support-period provision; CVD is Part II(5). However Part I(2)(g) is data minimisation, not free updates; the Article 13(8) quote is fabricated, and Article 11 reporting reference is wrong (Article 14 is reporting). |
| #74 | `research_archive/2026-11-12_060536.md` | CONFLICT | Article 14(3) is severe-incident reporting, not free updates/support. The alleged Article 14(3) quote is not authentic. Annex I Part II(1) is SBOM identification/documentation, not automatic updates or update separation. |
| #75 | `research_archive/2026-11-12_061040.md` | CONFLICT | “Expected lifetime or minimum five years, whichever longer” omits the expected-use-under-five-years exception. Part II(2) is vulnerability remediation, not the quoted free-update/automation clause; Article 13(4) is not the support-period provision. Quotes are synthetic. |
| #76 | `research_archive/2026-11-12_061542.md` | PARTIALLY_VERIFIED | No-cost/timely security update themes are supported by Part II(8), with the tailor-made product/business-user agreement exception. The cited Part I Section 1 point 2(g) is wrong (data minimisation); the quote is not verbatim. Product-category assertions are unsubstantiated. |
| #77 | `research_archive/2026-11-12_062041.md` | PARTIALLY_VERIFIED | Secure-by-default and attack-surface limitation are supported by Part I(2)(b)/(j). The quoted clauses are not verbatim; universal bans on factory credentials, mandatory forced password setup, blanket port/debug disablement and cryptographic delivery signatures are not directly prescribed as written. |
| #78 | `research_archive/2026-11-12_062537.md` | CONFLICT | Article 13(8) support-period principle is relevant, but the quoted Article 13(8) text is not authentic and the five-year rule is oversimplified. The purported Annex I Part I Section 2(2) quotation is mislocated; free updates are Part II(8). |

## Batch result

- Total reports: 19
- PARTIALLY_VERIFIED: 6 (#60, #61, #63, #73, #76, #77)
- CONFLICT: 13
- Fully VERIFIED: 0
- Verbatim quote blocks cleared for reuse: 0

This is a file-level, risk-focused audit of these 19 reports, not a statistical estimate of error across the full archive. The file-level PARTIALLY_VERIFIED label does not approve any report's Raw Text Quote for verbatim reuse. Each quote block in this batch remains rejected pending a separate quote-level exact-text review.

## Corrective use in project work

Use the legal distinctions above as the canonical correction map. Reuse none of the original Raw Text Quote blocks. Any future legal statement must be rewritten as a paraphrase or re-quoted from the exact EUR-Lex location. Product-specific applicability, actual servo-drive design choices, and evidence remain separate from source-level legal verification.

## Integrity boundary

- Audited `main` source reports #60–#78 without modifying them.
- No changes to `main.py`, Gemini prompt, production workflow, or `.github/workflows/run.yml`.
- No merge, rebase, or synchronization of `cra-project-foundation` with `main`.
- No claim that CI passed; the relevant work-branch status has not yet been rechecked.
