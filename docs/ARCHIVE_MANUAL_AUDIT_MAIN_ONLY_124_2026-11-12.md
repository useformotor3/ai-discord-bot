# Main-only CRA archive audit #124 — 2026-11-12

## Source and scope
- Main commit: `17eebdb0af513ae2b6800e13d55b798d095631cc`
- Commit message: `Auto-archive: Research report #124`
- Archive path: `research_archive/2026-11-12_101546.md`
- Inspected full commit diff, including report text and history/state increment.
- Legal source: EUR-Lex Regulation (EU) 2024/2847, CELEX 32024R2847:
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Audit record only on `cra-project-foundation`; original main archive/history/state unchanged.

## Verdict: CONFLICT

The report selects a valid topic (vulnerability handling, CVD and secure update distribution), but it places vulnerability handling in Annex I Part I, invents a “Part I, Section 2” structure, supplies a synthetic quotation, and presents cryptographic signatures and fail-safe/recovery architecture as universally mandated implementations.

## Correct legal structure

1. **Annex I Part I(1) and Part I(2)(a)–(m): product cybersecurity properties.** This includes risk-based product cybersecurity, no known exploitable vulnerabilities, secure-by-default, security updates (where applicable automatic installation enabled by default with an easy opt-out, notification and temporary postponement), access control, confidentiality, integrity, data minimisation, availability/resilience, limiting negative effects on other devices/networks, attack-surface limitation, incident-impact mitigation, relevant activity logging/monitoring with opt-out, and secure removal of data/settings.
2. **Annex I Part II(1)–(8): vulnerability handling requirements.** These are process/manufacturer requirements, not “Part I Section 2”.
   - (1) identify and document vulnerabilities/components, including an SBOM covering at least top-level dependencies;
   - (2) address and remediate vulnerabilities without delay, including security updates where appropriate and separate security/function updates where technically feasible;
   - (3) apply effective and regular security tests/reviews;
   - (4) disclose information about fixed vulnerabilities after a security update, subject to justified delay;
   - (5) put in place and enforce a CVD policy;
   - (6) facilitate sharing of vulnerability information, including a contact address;
   - (7) provide mechanisms to securely distribute updates and, where applicable for security updates, automatically;
   - (8) ensure security updates are disseminated without delay and, unless otherwise agreed for a tailor-made product with a business user, free of charge, with advisory messages.
3. **Article 13(17) and Annex II(2): single point of contact.** The user-facing Annex II information includes where vulnerabilities can be reported/received and where the CVD policy can be found. Do not conflate this with the complete internal CVD process.
4. **Article 13(8): vulnerability handling during support period.** Manufacturer support period and vulnerability handling are linked, with the support period determined by expected use and other stated factors.
5. **Annex I Part I(2)(c): automatic updates.** Where applicable, automatic installation of security updates is enabled by default, with easy opt-out, user notification and temporary postponement. This is not an unconditional command that every product must install every update without user control.

## Report-specific defects

| Report statement | Audit finding |
|---|---|
| “Annex I Part I, Section 2 (Vulnerability handling requirements)” | Wrong structure and part. Vulnerability handling is Annex I Part II(1)–(8). |
| Raw quote with (a) vulnerabilities addressed by updates, (b) regular checks, (c) shared info/advisory, (d) policies/CVD | Synthetic/composite wording and incorrect numbering. It is not verbatim Annex I Part I Section 2. Reject for direct quotation. |
| Cryptographic signature verification is mandatory for every servo-drive update | The CRA requires secure update-distribution mechanisms and product integrity/security properties, but the cited provisions do not universally prescribe a particular cryptographic signature implementation. Signature verification is a strong risk-based design candidate; validate algorithm, key lifecycle, trust anchor and product architecture separately. |
| Update failure must recover through a “Fail-safe / Recovery mode” architecture | A robust recovery strategy may be appropriate for product risk and safety requirements, but this exact architecture is not universally specified by the cited CRA text. Keep it as a design proposal, not a direct quotation/legal mandate. |
| Automatic deployment with minimal user intervention | Must be qualified by “where applicable” and the actual Part I(2)(c) default/opt-out/notification/temporary-postponement conditions. |

## Recommended servo-drive implementation treatment
- Legal requirement: implement a secure update-distribution mechanism; distribute security updates without delay and free of charge subject to the tailor-made business-user exception; enable automatic security update installation by default where applicable, with the stated user controls and notifications.
- Risk-based engineering candidates: signed firmware package, signature verification before installation, protected trust anchor/key management, anti-rollback/version policy, dual-bank or recovery image, power-loss interruption testing, update audit log and safe operational-state handling.
- Product-specific validation needed: boot architecture, MCU/flash layout, network/update path, maintenance mode, control-loop state, safe torque off or other actuator inhibit, recovery behavior, update ownership and service procedures.
- Do not claim any candidate is implemented or tested until schematic, firmware, threat model, test procedure and objective results exist.

## Correction and evidence handling
1. Reject report #124 Raw Text Quote for verbatim reuse.
2. Preserve original main archive unchanged; keep this audit on the work branch.
3. Record the exact obligation-to-design distinction in the claim ledger and pipeline proposal.
4. Do not claim that a cryptographic signature or specific recovery architecture is a universal CRA mandate.
5. No product-specific applicability, implementation, test pass or certification is inferred.

## Audit limitations
- Legal clause structure and quoted provision mapping checked against official EUR-Lex Regulation (EU) 2024/2847.
- Exact servo-drive MCU, bootloader, update transport, flash architecture and operational recovery design remain unknown.
- No tests were run; no CI PASS is claimed.
- No main.py, Gemini prompt, parser, production workflow, `.github/workflows/run.yml` or main branch changes. No merge/rebase/sync.
