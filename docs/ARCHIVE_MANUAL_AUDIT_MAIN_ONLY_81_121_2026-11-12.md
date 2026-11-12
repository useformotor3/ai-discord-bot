# Main-only CRA archive audit #81–#121 — 2026-11-12

## Scope and method

- Repository: `useformotor3/ai-discord-bot`
- Source branch: `main`; source HEAD at review: `d0ba9802e4b7fead4192263d8ebd08f44a7c547e` (Auto-archive report #121, 2026-11-12T10:01:12Z).
- Audit branch: `cra-project-foundation`; audit only. No source archive, history, state, `main.py`, Gemini prompt, production workflow, `.github/workflows/run.yml`, or `main` branch was changed.
- Scope: 41 consecutive report commits, #81–#121. Each commit diff was inspected, including the appended archive Markdown and history/state count change.
- Pass A: extracted legal propositions, clause references, quoted text and product/design recommendations.
- Pass B: checked the claims against the official EUR-Lex Regulation (EU) 2024/2847 text, especially Articles 13–14, Annex I Parts I–II and Annex II.
- Pass C: checked neighboring provisions, exceptions, the reporting tracks, and whether a legal obligation was being confused with an engineering recommendation.
- A report-level verdict is not an archive-wide error rate. A correct general theme does not validate a fabricated quotation or incorrect clause reference. No quotation block in this batch is approved for verbatim reuse.

## Batch result

- Reports reviewed: 41 / 41.
- File-level verdict: **CONFLICT 33; PARTIALLY_VERIFIED 8; VERIFIED 0.**
- Raw Text Quote blocks: **41 rejected for verbatim reuse** because the text, numbering, attribution, or a combination was not an exact quotation from the cited provision.
- Repeated pattern: several reports are near-duplicates of the same three themes (support period/free updates; secure-by-default/default credentials; vulnerability reporting) while presenting invented clause numbers and synthetic quotations as legal text.
- This is a risk-based consecutive batch, not a random sample. Do not extrapolate these results to all archive reports.

## Correct legal baseline used in this audit

1. **Article 13(8): support period.** The manufacturer determines the support period to reflect the time the product is expected to be in use, taking account of reasonable user expectations, product nature/intended purpose and relevant Union law. General minimum is five years; where expected use is less than five years, the support period corresponds to expected use. The information considered must be included in technical documentation. This is not a universal “five years or expected life, whichever is longer” rule.
2. **Article 13(9): update availability after issuance.** Each security update made available during the support period must remain available for at least 10 years after issuance or the remainder of the support period, whichever is longer.
3. **Annex I Part I(2): product properties.** Includes (a) no known exploitable vulnerabilities; (b) secure-by-default configuration, including reset to original state, subject to the stated tailor-made business-user agreement exception; (c) security updates, where applicable automatic installation enabled by default with an easy opt-out, notification and temporary postponement; (d) appropriate access controls; (e) confidentiality; (f) integrity; (g) data minimisation; (h) availability/resilience; (i) limiting negative impact on other devices/networks; (j) limiting attack surfaces; (k) incident impact mitigation; (l) recording/monitoring relevant internal activity with opt-out; (m) secure removal of data/settings.
4. **Annex I Part II(1)–(8): vulnerability handling.** Includes identifying/documenting vulnerabilities and components with an SBOM covering at least top-level dependencies; remediation without delay; effective and regular tests/reviews; disclosure of fixed vulnerabilities after an update subject to justified delay; CVD policy; vulnerability reporting contact; secure update distribution; and security updates without delay and free of charge, except where otherwise agreed between manufacturer and business user for a tailor-made product.
5. **Article 14: mandatory reporting.** Applies to actively exploited vulnerabilities contained in the product and severe incidents having an impact on product security—not every discovered vulnerability. Actively exploited vulnerability track: 24-hour early warning, 72-hour vulnerability notification, final report no later than 14 days after a corrective/mitigating measure becomes available. Severe-incident track: 24-hour early warning, 72-hour incident notification, final report within one month after incident notification. Notifications go via the single reporting platform to the designated CSIRT and ENISA.
6. **Annex II point 2 and point 8(d).** Point 2 requires user information about the single point of contact for vulnerability reports and the CVD policy. Point 8(d) requires instructions/information on secure decommissioning, including how user data can be securely removed. This does not create a blanket rule requiring advance end-of-support notice at a specified interval or a prescribed cryptographic-erase implementation.
7. **Engineering choices are not automatically CRA mandates.** Secure Boot, a hardware Root of Trust, TPM/secure element, a particular signature algorithm, dual-bank flash, automatic rollback, zero-downtime update, universal disabling of JTAG/UART/unused ports, forced first-boot password change, MFA/RBAC, and remote telemetry may be sensible risk-based design choices, but the cited CRA provisions do not impose each as a universal named implementation.

Official source: EUR-Lex, Regulation (EU) 2024/2847, CELEX 32024R2847:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

## Report-by-report findings

| Report | Source archive file | Commit (short SHA) | Verdict | Principal issue |
|---:|---|---|---|---|
| 81 | 2026-11-12_064037.md | 24624c80cded | CONFLICT | Invented default-credential prohibition and fabricated Annex I quotation; support-period details overstate the legal text. |
| 82 | 2026-11-12_064536.md | 8dd6b8a724e6 | CONFLICT | Reverses the support-period shorter-than-five-year exception and fabricates Annex I Part I/Part II wording. |
| 83 | 2026-11-12_065037.md | 6c1865043e87 | CONFLICT | Annex I numbering and quote structure are fabricated; universal credential/port requirements overstated. |
| 84 | 2026-11-12_065540.md | 85e946e2f3ff | CONFLICT | Secure-by-default theme is relevant, but quotation and subpoint attribution are composite/inaccurate; blanket unique-password mandate unsupported. |
| 85 | 2026-11-12_070055.md | 085eb3dab574 | PARTIALLY_VERIFIED | Secure-by-default and update integrity are relevant themes; quoted clause structure is inaccurate and Secure Boot/mandatory runtime integrity are not universal CRA prescriptions. |
| 86 | 2026-11-12_070534.md | eff2b6f27199 | PARTIALLY_VERIFIED | General default-security/integrity themes supported; raw quotation is fabricated and specific Secure Boot/default-password requirements are overstated. |
| 87 | 2026-11-12_071037.md | fcf907ea0f1f | CONFLICT | Invented Secure Boot/Root-of-Trust legal mandate and fabricated Annex I lettering/quotation. |
| 88 | 2026-11-12_071543.md | 8b8cf089c4ca | CONFLICT | Composite/misnumbered Annex I quotation; update and secure-default provisions conflated. |
| 89 | 2026-11-12_072037.md | 035eabe798aa | CONFLICT | Invented Annex I Part I Section 2 subpoints and universal interface/Secure Boot mandates. |
| 90 | 2026-11-12_072539.md | 03f0f574ba2e | CONFLICT | Secure Boot/rollback presented as mandatory; technical-documentation retention and Annex I quotations misattributed. |
| 91 | 2026-11-12_073043.md | 80cbd4748a98 | CONFLICT | SBOM requirement is real but is Annex I Part II(1), with top-level-dependency minimum; cited Article 13/quote and scope are fabricated. |
| 92 | 2026-11-12_073534.md | 39a5e9713bcc | CONFLICT | Secure Boot and Root of Trust stated as direct universal requirements; Annex VII/Article 24 attribution and retention claims inaccurate. |
| 93 | 2026-11-12_074042.md | 31057f483f3d | CONFLICT | Fabricated update clauses; mandatory signed firmware, dual-bank, rollback and uninterrupted control-loop requirements are engineering options, not quoted CRA mandates. |
| 94 | 2026-11-12_074549.md | e7c78aab5028 | CONFLICT | Support-period rule is reversed (“longer”); quotation is synthetic and Article/Annex attribution incorrect. |
| 95 | 2026-11-12_075037.md | 4984a8b39f0e | CONFLICT | Annex VII and Annex I subpoint references are wrong; support-period/updates wording is fabricated and “longer” is incorrect. |
| 96 | 2026-11-12_075535.md | c25cad645f53 | CONFLICT | “Longer” support period is wrong; invented Annex I subpoints and blanket cryptographic-signature mandate; IEC 62443 SL2 is not CRA text. |
| 97 | 2026-11-12_080056.md | 58788f7bdf68 | CONFLICT | CVD/contact themes are valid, but Article 14 and Annex I numbering are wrong and quotations are synthetic. |
| 98 | 2026-11-12_080532.md | c10119163eb6 | PARTIALLY_VERIFIED | Secure-by-default/access-control themes are supported; MFA/RBAC/mandatory unique credentials and quoted subpoints are not established as universal requirements. |
| 99 | 2026-11-12_081040.md | eed840c5c77f | CONFLICT | Third-party component diligence theme is partly related to Article 13(6), but “full responsibility” quote is fabricated and overbroad. |
| 100 | 2026-11-12_081537.md | e212b822aa76 | CONFLICT | Free security updates are in Annex I Part II(8); cited Part I point 2(g) and quote are false, and product class assumptions are unsupported. |
| 101 | 2026-11-12_082037.md | 227e41aed006 | CONFLICT | Article 14 reporting scope/timing is conflated; telemetry/automatic reporting and Annex I quotation are not prescribed as stated. |
| 102 | 2026-11-12_082544.md | 5a9145c6261d | CONFLICT | Support duration “longer” is wrong; Annex I Part II numbering and quotation are fabricated; Article 11 attribution incorrect. |
| 103 | 2026-11-12_083050.md | 7ee5eded945e | CONFLICT | Annex I Part II subpoints and Article 13(4) quote are invented; support-period and free-update clauses conflated. |
| 104 | 2026-11-12_083538.md | 6ba1ad079e2c | PARTIALLY_VERIFIED | Secure-by-default/access themes are valid, but point lettering/quote is wrong and blanket port/password/RBAC claims are overstatements. |
| 105 | 2026-11-12_084040.md | 7ea09c26f65e | PARTIALLY_VERIFIED | Secure-by-default is relevant; cited Section 1(h)/(i) and quote are fabricated/misnumbered, and universal default-password/port requirements overstated. |
| 106 | 2026-11-12_084537.md | 62f1fafe66da | CONFLICT | Article 14 scope is narrowed to actively exploited vulnerabilities and severe incidents; report broadens to any vulnerability/incident and invents quote text. |
| 107 | 2026-11-12_085040.md | 9fbeee6ae2be | CONFLICT | Product Class II assumption is unsupported; free-update rule and secure-update details are assigned fabricated Annex I numbering/quotation. |
| 108 | 2026-11-12_085537.md | e30045064e62 | CONFLICT | Support period and free-update requirements conflated; quote is synthetic and automatic update/signature details overstated. |
| 109 | 2026-11-12_090059.md | bd38171e8510 | CONFLICT | Cites nonexistent Article 11(7); support period and free-update rule are misattributed and quotation fabricated. |
| 110 | 2026-11-12_090530.md | 4becc618c4a6 | CONFLICT | Article 11 and Annex I citations are inaccurate; claimed raw quotation does not appear in the cited text. |
| 111 | 2026-11-12_091046.md | 19a1629b5ac3 | CONFLICT | Article 13(8) is support-period/vulnerability-handling provision, not the quoted blanket free-update sentence; minimum-five-year exception omitted. |
| 112 | 2026-11-12_091538.md | 02a00b97caae | CONFLICT | Invented Article 14(2)(h) and Annex I Part II(1)(f); Article 14 is not the general free-patch/CVD clause. |
| 113 | 2026-11-12_092039.md | 0e313c40dfcd | CONFLICT | Invented Annex I Part I/Part II paragraph numbering and wording; free updates correctly belong to Part II(8), with tailor-made business-user exception. |
| 114 | 2026-11-12_092614.md | 9ce9f542a474 | CONFLICT | Article 14 misused for secure-update design; mandatory digital signatures, encrypted delivery and rollback are overstated as express CRA commands. |
| 115 | 2026-11-12_093045.md | 51f936c69ab5 | CONFLICT | Annex I lettering and raw quote are false; universal unique-credential/forced-first-boot requirements unsupported. |
| 116 | 2026-11-12_093534.md | 3ae65dc752ae | CONFLICT | Article 11/Annex I Part II numbering and CVD quotation are inaccurate or fabricated. |
| 117 | 2026-11-12_094044.md | 6cbefc9c4f8d | PARTIALLY_VERIFIED | Secure-default/reset concept is supported; universal password replacement, port disabling and fabricated access-control quote are not. |
| 118 | 2026-11-12_094545.md | 3873512131cb | CONFLICT | Invented Annex I Part I point (g) quote; integrity/authenticity verification and automatic updates are misrepresented as a mandatory signed-update specification. |
| 119 | 2026-11-12_095040.md | 458c89629c69 | PARTIALLY_VERIFIED | Support-period topic is valid, but Article 10 is wrong, quote is composite, and the under-five-year exception is omitted. |
| 120 | 2026-11-12_095534.md | aeca2f2dd09d | CONFLICT | Reporting belongs to Article 14, not Article 11; 24h/72h theme is incomplete and final-report timelines/categories are conflated. |
| 121 | 2026-11-12_100055.md | d0ba9802e4b7 | PARTIALLY_VERIFIED | Support-period and secure-decommissioning themes have relevant provisions, but advance end-of-support notice is not stated as a fixed CRA duty; raw quote is composite and under-five-year exception omitted. |

## High-priority corrective actions

1. Do not reuse any #81–#121 Raw Text Quote as a direct legal quotation.
2. Replace report-level conclusions only in a separately versioned correction/errata document; preserve the original main archive unchanged.
3. For support period, use Article 13(8) and document expected-use reasoning and the less-than-five-year exception.
4. For free security updates, use Annex I Part II(8), including the tailor-made product/business-user agreement exception.
5. For CVD/contact, use Annex I Part II(5)–(6) and Annex II point 2.
6. For secure update distribution, use Annex I Part II(7); do not infer a particular cryptographic algorithm or dual-bank/rollback architecture from the text alone.
7. For Article 14, preserve the distinct actively-exploited-vulnerability and severe-incident reporting tracks and their different final-report deadlines.
8. Keep product classification, product applicability, and technical implementation recommendations in separate claim types. No servo-drive product class is inferred from these reports.

## Audit limitations

- Commit diffs were used to inspect the exact report text added by each archive commit; no claim is made that all external technical claims in the reports have been independently verified.
- The legal source check establishes the clause structure and the quoted provisions summarized above. Product-specific applicability, class assignment, and engineering implementation require product facts and separate technical evidence.
- No tests were run as part of this document audit. No CI PASS is claimed.
- No legal advice, conformity assessment, certification, or full archive audit is claimed.
