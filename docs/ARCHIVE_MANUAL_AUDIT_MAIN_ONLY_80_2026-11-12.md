# Main-only CRA archive audit #80 (2026-11-12)

## Source
- Main commit: `78e73cb118d8bd9ca4ab7ec1433afe02c5b3eb12`
- Original file: `research_archive/2026-11-12_063533.md`
- Primary law: Regulation (EU) 2024/2847, Annex I Part I, EUR-Lex:
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Verified text location: EUR-Lex lines 1743–1762.

## Findings

**File-level verdict: PARTIALLY_VERIFIED.** The report correctly focuses on secure-by-default and attack-surface limitation. The controlling legal text is:
- Annex I Part I(1): risk-based overall cybersecurity level;
- Annex I Part I(2)(b): secure-by-default configuration, including possibility to reset to original state, subject to tailor-made product/business-user agreement exception;
- Annex I Part I(2)(d): protection against unauthorised access using appropriate control mechanisms;
- Annex I Part I(2)(j): limiting attack surfaces, including external interfaces.

The report's “Raw Text Quote” is not verbatim. It invents an Annex I Part I Section 1 structure with subpoints (a)–(d) and merges requirements that are actually in Part I(2)(a)–(d). The exact Annex I Part I(2)(a) is no known exploitable vulnerabilities; (b) secure-by-default; (c) vulnerability remediation via security updates; (d) access control. The quoted “confidentiality” item is actually Part I(2)(e), not (d). Reject the quotation as a direct legal quote.

Engineering overstatements:
- Universal disablement of all JTAG/UART/debug interfaces, unused ports, or EtherCAT/PROFINET services is not stated as a blanket command. Limiting attack surfaces is a risk-based outcome; interface-specific controls should be selected from product risk assessment.
- The CRA does not prescribe a universal first-boot forced password-change workflow or a universal “unique authentication credential” implementation in those exact terms. Appropriate access controls are required, but authentication implementation must be risk-based.
- Secure Boot and firmware integrity mechanisms may be appropriate controls for protecting firmware/configuration, but the cited Annex I text does not prescribe Secure Boot as a universal hardware mechanism.
- Factory reset to original state is part of secure-by-default at Part I(2)(b); it does not mean every factory reset must restore a particular hardcoded credential scheme.

## Corrective wording

The product must be delivered with a secure-by-default configuration, including the ability to reset it to its original state (Annex I Part I(2)(b)); it must protect against unauthorised access using appropriate control mechanisms (Part I(2)(d)); and it must limit attack surfaces, including external interfaces (Part I(2)(j)). The specific treatment of debug ports, unused services, authentication setup and firmware integrity should be selected and justified through the product cybersecurity risk assessment and documented as engineering controls, not presented as verbatim universal CRA commands.

## Integrity boundary

The main archive file was not modified. Audit is recorded only on `cra-project-foundation`. No main.py, Gemini prompt, production workflow, run.yml, branch sync, merge or rebase.
