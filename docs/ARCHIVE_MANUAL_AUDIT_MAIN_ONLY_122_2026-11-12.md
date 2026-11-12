# Main-only CRA archive audit #122 — 2026-11-12

## Source and scope
- Repository: useformotor3/ai-discord-bot
- Main commit: `39d614a760aebc98ce16fb534ddd75ddbcc5c1e3`
- Commit message: Auto-archive: Research report #122
- Archive path: `research_archive/2026-11-12_100532.md`
- Compared the full commit diff, including the report text and history/state count increment.
- Official legal baseline: EUR-Lex Regulation (EU) 2024/2847, Annex I Part I(2)(b),(d),(j), Annex I Part II, and Annex II.
- Work branch only. Original main archive/history/state remain unchanged.

## Verdict: CONFLICT

The general secure-by-default and access-control topics are relevant to CRA, but the report misnumbers and synthesizes the legal quotation and overstates implementation choices as universal statutory requirements.

### Findings
1. **Wrong Annex structure:** The report cites “Annex I Part I, Paragraph 1 - General requirements” and “Part II ... Paragraph 2 - Specific security requirements.” Actual Annex I structure is Part I, numbered points (1) and (2)(a)–(m), and Part II, numbered requirements (1)–(8).
2. **Non-verbatim quote:** The quoted (a)–(c) text is not a verbatim rendering of Annex I Part I(2). In particular, access control is Part I(2)(d), not the quoted (c) wording. “Authentication, identity or session management” is not the cited raw wording.
3. **Overstated default-credential rule:** Part I(2)(b) requires secure-by-default configuration and reset capability; Part I(2)(d) requires appropriate access controls. The text does not universally prescribe forced first-use password change, unique per-device credentials, or an absolute ban on every shared credential design irrespective of risk/context.
4. **Overstated attack-surface implementation:** Part I(2)(j) requires limiting attack surfaces, including external interfaces. It does not explicitly command every unused port, diagnostic interface or legacy protocol to be disabled in all products.
5. **RBAC:** Role separation can be a suitable design response to risk and access-control needs, but the cited CRA text does not universally mandate a specific RBAC architecture.

## Correct mapping
- Secure-by-default configuration/reset: Annex I Part I(2)(b).
- Appropriate access control: Annex I Part I(2)(d).
- Attack-surface limitation: Annex I Part I(2)(j).
- User-facing single vulnerability contact/CVD policy information: Annex II point 2; policy itself: Annex I Part II(5).
- Specific password policy, RBAC model, port configuration and service disabling must be justified by product risk assessment and documented as implementation decisions, not presented as verbatim CRA mandates.

## Correction / handling
- Do not reuse the report's Raw Text Quote as a direct legal quotation.
- Keep the original main archive immutable. Record this audit separately on `cra-project-foundation`.
- No product class or product-specific applicability is inferred.
- No tests were run; no CI PASS is claimed.
- No main.py, Gemini prompt, production workflow, run.yml, or main-branch modification; no merge/rebase/sync.

Official source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
