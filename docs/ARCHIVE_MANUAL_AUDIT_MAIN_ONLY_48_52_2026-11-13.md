# CRA Main-only Archive Manual Audit — Reports #48–#52

- Audit date: 2026-11-13
- Source branch: main (read-only)
- Recording branch: cra-project-foundation
- Audit method: Pass A (exact archive claims/quotes) → Pass B (official CRA text) → Pass C (counter-evidence, exceptions, product boundary)
- Status: completed for the five identified archive files; no independent third-party legal review performed.

## 1. Scope and source identity

The five reports were mapped using the date, daily count, and exact path in main/history.json. The archive originals were fetched from main and their Git blob SHA values recorded below.

| Daily report | Original archive path | Blob SHA |
|---:|---|---|
| #48 | research_archive/2026-11-13_035531.md | 539b1d73d7053c5b1e252c775c503b055e978dd9 |
| #49 | research_archive/2026-11-13_040051.md | 3d661d5545974406fee419f60234f99d29427495 |
| #50 | research_archive/2026-11-13_040534.md | 8bbfe9b22a009c90dba493d3086462bb605a1b50 |
| #51 | research_archive/2026-11-13_041039.md | 8625c7e82389aea9cd3e5a0694cd0b920c90e8cf |
| #52 | research_archive/2026-11-13_041532.md | 3672c41635364ef99b494cd8944c4998bbfc01c8 |

## 2. Verdict summary

- CONFLICT: 3 (#49, #50, #52)
- PARTIALLY_VERIFIED: 2 (#48, #51)
- VERIFIED: 0
- Direct quote blocks accepted for verbatim reuse as current CRA text: 0/5

The verdict is file-level. It does not imply that every sentence in a CONFLICT file is false; it means the central legal claim, legal locator, or asserted obligation is materially wrong. Partial verification is limited to the specific element identified below.

## 3. Pass A/B/C findings

### #48 — PARTIALLY_VERIFIED

**Central claim:** Manufacturers must provide automated security advisories and machine-readable vulnerability notices under Annex I Part II(2), with CSAF as the expected format.

**What is supported**
- Annex I Part II(4) requires sharing and public disclosure of information about fixed vulnerabilities after a security update is available, subject to a justified delay where publication risk outweighs security benefit.
- Annex I Part II(5) requires a coordinated vulnerability disclosure policy.
- Article 14(8) requires informing impacted users, and where appropriate all users, after an actively exploited vulnerability or severe incident. Where appropriate, that user information is to be in a structured, machine-readable format that is easily automatically processable.

**What conflicts**
- Annex I Part II(2) is the obligation to address and remediate vulnerabilities without delay, including by security updates; where technically feasible, security updates are to be separate from functionality updates. It does not contain the quoted automatic advisory/machine-readable requirement.
- The machine-readable user-notification language is in Article 14(8), and is limited to the specified Article 14 events and qualified by “where appropriate”. It is not a universal obligation to issue automated notices for every vulnerability.
- CSAF is not named as a mandatory format in the cited CRA provisions. It may be considered as an implementation choice, not a universal CRA mandate.
- Automatic update language is separately addressed in Annex I Part I point 2(c) and Part II point 7, with their own conditions; it does not establish a blanket automated advisory system.

**Quote result:** The alleged Annex I Part II(2) quotation does not match the final text. The alleged Article 11 quotation is not the current CRA provision. Neither quote is reusable as a verbatim quotation.

### #49 — CONFLICT

**Central claim:** Free security updates throughout the expected lifetime are required under Annex I Part I point 2; Article 11 requires reporting all actively exploited vulnerabilities/incidents with an immediate 24-hour notice; support period is the expected lifetime or five years, whichever is shorter.

**What conflicts**
- The relevant reporting provision is Article 14, not Article 11. Article 14 separates actively exploited vulnerabilities from severe incidents affecting product security and defines staged deadlines: 24-hour early warning, 72-hour notification, and different final-report deadlines (14 days after corrective/mitigating measure for actively exploited vulnerabilities; one month after the incident notification for severe incidents).
- Free security update distribution is Annex I Part II point 8, not Annex I Part I point 2. Part II point 8 requires updates addressing identified security issues to be disseminated without delay and, unless otherwise agreed between manufacturer and business user for a tailor-made product, free of charge and accompanied by advisory messages.
- Article 13(8) governs the support period. It must reflect expected use and is at least five years, except where expected use is less than five years, in which case the support period corresponds to expected use. “Expected lifetime or five years, whichever is shorter” is not an accurate statement of the general rule.
- Article 13(9) separately requires each security update made available during the support period to remain available for at least 10 years after issue or the remainder of the support period, whichever is longer.
- The assertion that updates must not cause any functional degradation, or that a “zero-downtime/rollback” design is specifically mandated, is not established by the cited provisions. Those may be risk-based engineering choices.

**What is supported**
- CRA does require free security updates in the ordinary case under Annex I Part II point 8, subject to the tailor-made product/business-user agreement exception.
- Article 14 does contain a 24-hour early-warning deadline for the specified reportable events, but not as a single all-purpose reporting rule.

**Quote result:** Both alleged quotations are materially different from the final CRA text and cannot be reused verbatim.

### #50 — CONFLICT

**Central claim:** An industrial servo drive is an Important Product Class I because it is high-risk; all vulnerabilities require free patches and public security advisories.

**What conflicts**
- The CRA does not classify a servo drive as Class I merely because it is an industrial or high-risk product. Article 7 and Annex III require the product’s core functionality to match a listed category, read with Commission Implementing Regulation (EU) 2025/2392 technical descriptions.
- Annex III Class I category 14 is “microcontrollers with security-related functionalities”; Class II category 4 is “tamper-resistant microcontrollers”. These are distinct component/product categories. Integrating an MCU into a servo drive does not by itself classify the complete drive as Class I or II.
- The cited Article 11 is not the final manufacturer-obligations/reporting locator. Relevant provisions include Article 13(8)/(9), Article 14, and Annex I Part II(2), (4), and (8), each with different scope.
- Public disclosure under Annex I Part II point 4 concerns fixed vulnerabilities once a security update has been made available and includes a justified-delay exception. It is not an unconditional public notice for every vulnerability.
- Free distribution under Annex I Part II point 8 is subject to the express tailor-made product/business-user agreement exception.

**What is supported**
- Security updates are required to address identified security issues and are ordinarily free of charge under Annex I Part II point 8.
- Vulnerability information must be publicly disclosed after a security update under Part II point 4, subject to its stated exception.

**Quote result:** The report provides no accurate final-text verbatim quotation supporting its Class I claim or its combined Article 11/Annex I assertion. No quote accepted.

### #51 — PARTIALLY_VERIFIED

**Central claim:** Manufacturers must maintain a coordinated vulnerability disclosure policy and a clear external reporting channel, with secure reporting such as PGP.

**What is supported**
- Annex I Part II point 5 requires manufacturers to put in place and enforce a coordinated vulnerability disclosure policy.
- Annex I Part II point 6 requires measures facilitating information sharing about potential vulnerabilities in the product and third-party components, including a contact address for reporting discovered vulnerabilities.
- Article 13(8) also requires appropriate policies and procedures, including CVD policies, for processing and remediating potential vulnerabilities reported from internal or external sources.
- Annex II point 2 requires user-facing information about the single point of contact and where the manufacturer’s CVD policy can be found.

**What conflicts**
- The report incorrectly locates these duties in Annex I Part I and refers to Article 10. The relevant vulnerability-handling requirements are in Annex I Part II points 5 and 6, with Article 13(8) supporting the policy/process obligation.
- PGP encryption is an implementation option, not a specific universal CRA mandate in the cited provisions.
- The report’s proposed fixed deadlines for all third-party reports and mandatory CVE assignment/publication are not established by the cited text. Public disclosure of fixed vulnerabilities is addressed separately in Annex I Part II point 4, with a justified-delay exception.

**Quote result:** The quoted text is not a faithful verbatim extract of the final provision and its locator is wrong. No quote accepted.

### #52 — CONFLICT

**Central claim:** CRA imposes a supply-chain vulnerability information-transfer duty requiring component suppliers to notify the servo-drive manufacturer, which must then notify integrators and end users; all vulnerabilities are to be patched free of charge for a minimum five-year period.

**What conflicts**
- Article 13(6) states the direction of the explicit component-vulnerability reporting duty: when the manufacturer identifies a vulnerability in an integrated component, the manufacturer reports it to the person/entity manufacturing or maintaining that component and addresses/remediates it under Annex I Part II. Where the manufacturer develops a modification, relevant code or documentation is shared with that component manufacturer/maintainer where appropriate in machine-readable format.
- Article 13(5) requires due diligence when integrating third-party components. Article 13(7) requires systematic documentation of relevant cybersecurity aspects, including vulnerabilities and relevant third-party information. These provisions do not create the report’s blanket legal rule that every component supplier must notify every integrating manufacturer or that the manufacturer must always forward all vulnerability details to every integrator/end user.
- User notification is specifically addressed in Article 14(8) for actively exploited vulnerabilities and severe incidents, with the “where appropriate” structured machine-readable condition. It is not a general duty to automatically transfer all supply-chain vulnerability information to every downstream party.
- Article 13(8) sets the support period: at least five years, except where expected use is shorter. Free security update distribution is separately governed by Annex I Part II point 8 and its tailor-made product/business-user agreement exception.
- The report’s quoted Annex I text does not match the final Annex I Part II points (1)–(8), and the alleged Article 11 quote is not the final Article 13(8) wording.

**What is supported**
- Manufacturers must exercise due diligence on integrated third-party components and report identified component vulnerabilities to the component manufacturer/maintainer under Article 13(6).
- Manufacturers must maintain appropriate vulnerability-handling processes during the support period and generally provide security updates free of charge under Part II point 8.

**Quote result:** The quoted passages are draft-like/paraphrased composites and do not match the final legal text. No quote accepted.

## 4. Consolidated legal correction rules from this batch

| Subject | Correct legal anchor | Avoid |
|---|---|---|
| Fixed-vulnerability public disclosure | Annex I Part II(4) | Treating it as universal immediate disclosure of every vulnerability |
| CVD policy | Annex I Part II(5); Article 13(8) | Annex I Part I or Article 10 locator |
| Vulnerability reporting contact | Annex I Part II(6); Annex II point 2 | Claiming PGP or a specific encryption technology is universally mandated |
| Secure update distribution | Annex I Part II(7) | Confusing it with public advisory format |
| Free security update distribution | Annex I Part II(8) | Omitting tailor-made product/business-user agreement exception |
| Support period | Article 13(8) | “Expected lifetime or five years, whichever is shorter” as an unqualified rule |
| Security update availability | Article 13(9) | Treating support period itself as a 10-year requirement |
| Component vulnerability reporting | Article 13(6) | Reversing the express reporting direction |
| Machine-readable user notification | Article 14(8), where appropriate | Applying it to every vulnerability/advisory |
| Mandatory incident/vulnerability reporting | Article 14(1)–(4) | Article 11 or all-vulnerability reporting |
| Important product classification | Article 7, Annex III, Implementing Regulation (EU) 2025/2392 | Automatically classifying industrial servo drives as Class I/II |

## 5. Official primary sources checked

1. Regulation (EU) 2024/2847, EUR-Lex official text:
   https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
   - Article 7; Article 13(5)–(9); Article 14(1)–(8); Annex I Part I point 2(c)/(d); Annex I Part II points (1)–(8); Annex II point 2.
2. Official Journal PDF of Regulation (EU) 2024/2847:
   https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847
3. Commission Implementing Regulation (EU) 2025/2392:
   https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
   - Technical descriptions for Annex III categories, including security-related microcontrollers and tamper-resistant microcontrollers.

The final CRA text was checked directly through EUR-Lex search-returned official text excerpts for the cited provisions. The browser open endpoint itself presented a robot-check page, so this audit does not claim a fresh E3 live fetcher execution or a visual PDF-page inspection. No independent external legal counsel review was performed.

## 6. Main branch and product applicability limitations

- main is read-only; the five source archives were not modified.
- No merge, rebase, or sync was performed.
- No product SKU, intended purpose, actual MCU order code, product boundary, or technical architecture was available. Product-specific applicability/classification remains UNVERIFIED.
- This is a legal-text audit of the archive claims, not a product conformity assessment or a DUT test result.

## 7. Cumulative consecutive audit sample

Including reports #8–#47, the consecutive non-random sample #8–#52 contains 45 reports:

- CONFLICT: 40
- PARTIALLY_VERIFIED: 5
- VERIFIED: 0
- Direct quote reuse: 0/45

This is a consecutive, non-random sample. It must not be presented as an error rate for the entire main archive.
