# Main-only CRA archive audit #123 — 2026-11-12

## Source and scope
- Repository: `useformotor3/ai-discord-bot`
- Main commit: `1f9dc5e28d760ce5b47efda0e897a0a540d33ecb`
- Commit message: `Auto-archive: Research report #123`
- Archive path: `research_archive/2026-11-12_101044.md`
- Inspected the full commit diff, including report body, history increment and state count.
- Legal source: EUR-Lex Regulation (EU) 2024/2847, CELEX 32024R2847:
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Audit recorded on `cra-project-foundation` only. No source archive/history/state or main branch modification.

## Verdict: CONFLICT

The subject—information and instructions to users—is a real CRA obligation and directly relevant to servo-drive documentation. However, the report assigns the central duty to the wrong Article paragraph, presents a synthetic quotation as verbatim law, invents an Annex II Part I/Part II structure, overstates support-period language, and asserts a Class II product category without product/category evidence.

## Claim-by-claim findings

### 1. Accompanying user information and instructions
- The relevant manufacturer obligation is **Article 13(18)**, not Article 13(7).
- Article 13(7) requires manufacturers to systematically document relevant cybersecurity aspects proportionately to the product nature and cybersecurity risks, including known vulnerabilities and relevant third-party information, and update the cybersecurity risk assessment where applicable.
- Article 13(18) requires the product to be accompanied by Annex II information/instructions in paper or electronic form, in a language readily understood by users and market-surveillance authorities; it must be clear, understandable, intelligible and legible, allow secure installation, operation and use, and remain available for at least 10 years after placing on the market or for the support period, whichever is longer. Online material must remain accessible, user-friendly and available for the same period.
- The report's quoted sentence beginning “Products with digital elements shall be accompanied...” is not an exact quotation of Article 13(7); it is a paraphrase/composite misattributed to the wrong paragraph.

### 2. Annex II structure and required content
- Annex II is titled **Information and instructions to the user** and consists of numbered points **1–9**. It is not divided into “Part I & Part II”.
- Point 1: manufacturer identity and contact details.
- Point 2: single point of contact for vulnerability reports/receipt and location of the CVD policy.
- Points 3–6: product identification, intended purpose/security environment/essential functions/security properties, foreseeable significant cybersecurity-risk circumstances, and (where applicable) EU declaration of conformity URL.
- Point 7: type of technical security support and end-date of the support period.
- Point 8 requires detailed instructions or a URL to them, covering (a) secure-use measures at initial commissioning and throughout product lifetime; (b) effects of product changes on data security; (c) installing security-relevant updates; (d) secure decommissioning and secure user-data removal; (e) turning off the default setting enabling automatic security-update installation; and (f) information needed by integrators where the product is intended for integration into other products.
- Point 9: if the manufacturer decides to make the SBOM available to users, information on where it can be accessed.
- The report's claimed Annex II “Part I & II” quote and its enumerated subclauses are not verbatim Annex II text.

### 3. Support-period statement
- The support period is determined under **Article 13(8)**, based on expected time in use and relevant factors; general minimum is five years, but where expected use is less than five years, the support period corresponds to expected use.
- The user-facing information must include the type of technical security support and support-period end-date under Annex II point 7.
- **Article 13(19)** separately requires the support-period end date, including at least month and year, to be clearly and understandably specified at the time of purchase in an easily accessible manner and, where applicable, on the product, packaging or by digital means. Where technically feasible, manufacturers must display a notification that the product has reached end of support.
- The report's phrase “expected product life or minimum five years” is too imprecise and could be misread as an unconditional five-year period. The less-than-five-year expected-use exception must be explicit.

### 4. Vulnerability contact and CVD
- Annex II point 2 is the correct user-information entry for the single vulnerability-reporting contact and where the CVD policy can be found.
- The underlying CVD policy and vulnerability-handling duties are in Annex I Part II point (5), with facilitation/contact measures in point (6). Article 13(17) also addresses the manufacturer's single point of contact.
- This part of the report is directionally correct but should cite the exact provisions and distinguish user-facing information from the manufacturer's process obligation.

### 5. Secure decommissioning
- Annex II point 8(d) requires instructions on secure decommissioning, including information on how user data can be securely removed.
- The report's examples—tuning parameters, firmware, certificates—may be relevant product-specific data categories, but are not an exhaustive CRA-prescribed list. “Permanently securely delete” should not be treated as requiring a specific cryptographic-erasure method unless supported by product risk and technical evidence.

### 6. “Digital Product Passport” and Class II
- “Digital Product Passport” is not the title or named obligation established by CRA Annex II. It may be used as an internal document/package label only if clearly described as a manufacturer-created information bundle, not a statutory CRA passport.
- A generic servo drive is not automatically a Class II Important Product solely because it is an industrial automation device. Product category/classification requires assessment against the actual product's core functionality and the relevant Annex III category/criteria. This report supplies no such evidence; classification remains UNVERIFIED.

## Correct legal mapping for the documentation workstream

| Documentation element | Correct CRA reference |
|---|---|
| Manufacturer identity/contact | Article 13(16); Annex II(1) |
| Single vulnerability contact and CVD policy location | Article 13(17); Annex I Part II(5)–(6); Annex II(2) |
| Product identification, intended purpose, security environment, functions and security properties | Annex II(3)–(4) |
| Foreseeable significant cybersecurity-risk circumstances | Annex II(5) |
| EU DoC URL, where applicable | Annex II(6) |
| Technical support type and support end date | Article 13(19); Annex II(7) |
| Secure commissioning/lifecycle measures | Annex II(8)(a) |
| Data-security impact of product changes | Annex II(8)(b) |
| Security update installation | Annex II(8)(c) |
| Secure decommissioning and user-data removal | Annex II(8)(d) |
| Turning off default automatic security-update installation | Annex II(8)(e) |
| Integrator information, where applicable | Annex II(8)(f) |
| SBOM access location, if manufacturer chooses to make SBOM available to users | Annex II(9) |
| Paper/electronic delivery, clarity, language and retention | Article 13(18) |

## Recommended correction
1. Reject both Raw Text Quote blocks from report #123 for verbatim reuse.
2. Create a separate CRA user-information checklist/template based on the mapping above; do not alter original main archive.
3. Separate mandatory Annex II content from optional manufacturer-created material and product-specific examples.
4. Keep product classification and servo-drive applicability UNVERIFIED until actual product functionality, interfaces and intended use are documented.
5. Do not describe the checklist as a statutory “Digital Product Passport” unless explicitly qualified as an internal information pack.

## Audit limitations
- The legal clause structure and cited requirements above were checked against the official EUR-Lex text.
- No servo-drive SKU, product boundary, core functionality, EU market placement, intended use, or Class II category evidence was provided by this report. Product applicability remains open.
- No tests were run; no CI PASS is claimed.
- No main.py, Gemini prompt, parser, production workflow, `.github/workflows/run.yml`, or main branch changes. No merge/rebase/sync.
