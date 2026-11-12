# Main-only CRA archive audit #79 (2026-11-12)

## Source
- Main commit: `61d596354e1e4a700915306cecb1bc29f0828698`
- Original file: `research_archive/2026-11-12_063054.md`
- Primary law: Regulation (EU) 2024/2847, Article 14(1)–(8), EUR-Lex:
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Verified text location: EUR-Lex lines 939–975.

## Findings

**File-level verdict: PARTIALLY_VERIFIED.** The report correctly identifies Article 14 as the reporting provision and correctly states the 24-hour early-warning deadline for an actively exploited vulnerability. However, it broadens the reportable category to any vulnerability affecting a product / active malicious detection. Article 14(1) is specifically an actively exploited vulnerability contained in the product with digital elements. It also describes the 72-hour notification as a “final notification” or conflates it with the final report. The legal stages are distinct:

1. **Actively exploited vulnerability (Article 14(1)–(2)):**
   - early warning: without undue delay and no later than 24 hours after awareness;
   - vulnerability notification: without undue delay and no later than 72 hours after awareness;
   - final report: no later than 14 days after a corrective or mitigating measure becomes available.
2. **Severe incident affecting product security (Article 14(3)–(5)):**
   - early warning: no later than 24 hours;
   - incident notification: no later than 72 hours;
   - final report: within one month after the incident notification.
3. **Routing:** the notification is submitted via the single reporting platform to the CSIRT designated as coordinator, and is simultaneously accessible to ENISA. Describing it as a platform operated by ENISA is imprecise.
4. **Quote:** the report's quotation says “any vulnerability having an impact on the security...” and attributes it to Article 14(2). The operative legal wording is “any actively exploited vulnerability contained in the product with digital elements” in Article 14(1). The supplied quote is not verbatim and its paragraph attribution is wrong; reject it as a direct quotation.

The servo-drive / OT consequences in the report are plausible risk scenarios, not proof that every servo drive has remote control exposure or that a particular incident necessarily meets Article 14's severe-incident threshold. Product applicability must be assessed separately.

## Corrective wording

A manufacturer must notify an actively exploited vulnerability contained in its product via the single reporting platform to the designated coordinating CSIRT, with simultaneous access for ENISA. The vulnerability track has a 24-hour early warning, a 72-hour vulnerability notification, and a final report within 14 days after a corrective or mitigating measure becomes available. A severe incident affecting product security follows a separate track, with its final report due within one month after the incident notification.

## Integrity boundary

The main archive file was not modified. This audit is recorded only on `cra-project-foundation`. No main.py, Gemini prompt, production workflow, run.yml, branch synchronization, or merge was performed.
