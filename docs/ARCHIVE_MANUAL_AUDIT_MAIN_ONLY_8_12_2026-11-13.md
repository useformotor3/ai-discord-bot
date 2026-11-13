# Main-only Archive Manual Audit — Reports #8–#12

## 한국어 핵심 요약

- 대상: 2026-11-13 main 보고서 #8–#12, 총 5건.
- 판정: CONFLICT 5건 / PARTIALLY_VERIFIED 0건 / VERIFIED 0건.
- 현행 CRA 법령 직접 인용으로 재사용 가능한 Raw Text Quote: 0/5. 제품별 적용성은 모두 UNVERIFIED.
- 반복 오류: 보안 기본값을 Annex I Part II 또는 Class II 의무로 잘못 분류, 첫 접속 비밀번호 강제 변경·모든 포트/JTAG/디버그 비활성화를 보편 의무로 과장, CVD·취약점 신고 연락처·무상 업데이트·Article 14 신고를 하나의 의무처럼 혼합, 제조사 의무를 Article 11로 오기.
- 정정 기준: Annex I Part I(2)(b)=보안 기본값/초기 상태 복원, Part I(2)(d)=접근통제, Part I(2)(j)=공격표면 제한; Annex I Part II(2)=취약점 시정, (5)=CVD 정책, (6)=취약점 정보 공유/연락처, (7)=안전한 업데이트 배포, (8)=원칙적 무상 보안 업데이트; 지원기간 Article 13(8), 업데이트 가용성 Article 13(9), 단일 연락 창구 Article 13(17), 법정 신고 Article 14.
- 아래 영문 상세 기록은 원본 main commit·archive SHA·보고서별 반증을 보존한다. 최종 독자용 설명은 한국어 법령 기준선과 제1권을 참조한다.


- Audit date: 2026-11-13
- Target branch: `cra-project-foundation`
- Original source branch: `main` (read-only)
- Scope: five main-only auto-archive reports #8–#12, report body/quote/reference audit
- Protocol: Pass A claim extraction → Pass B EUR-Lex reopening → Pass C scope/exception/counter-evidence
- Limitation: same AI session performed the review; this is not independent third-party legal advice or legal review.
- Product applicability: UNVERIFIED (actual servo-drive SKU, intended purpose, network features and ST MCU order code not supplied).

## 1. Official legal baseline used

Primary source: [Regulation (EU) 2024/2847, EUR-Lex, CELEX 32024R2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847), current text shown by EUR-Lex as version 20/11/2024.

- Annex I Part I(1): appropriate cybersecurity level based on risks.
- Annex I Part I(2)(b): secure-by-default configuration, with reset to original state; tailor-made product/business-user agreement exception.
- Annex I Part I(2)(c): security updates; where applicable, automatic updates default-enabled with opt-out and temporary postponement.
- Annex I Part I(2)(d): appropriate controls to protect against unauthorised access.
- Annex I Part I(2)(j): limit attack surfaces, including external interfaces.
- Annex I Part II(2): address/remediate vulnerabilities without delay; separate security updates from functionality updates where technically feasible.
- Annex I Part II(5): put in place and enforce a coordinated vulnerability disclosure policy.
- Annex I Part II(6): facilitate vulnerability information sharing, including a contact address.
- Annex I Part II(7): secure update distribution mechanisms.
- Annex I Part II(8): disseminate available security updates without delay and free of charge, unless otherwise agreed for a tailor-made product with a business user.
- Article 13(8): support period reflects expected use; at least five years unless expected use is shorter, in which case it corresponds to expected use.
- Article 13(9): each security update made available during support remains available for at least ten years after issuance or the remainder of support period, whichever is longer.
- Article 13(17): manufacturer single point of contact.
- Article 14(1)–(4): mandatory notification tracks for actively exploited vulnerabilities and severe incidents affecting product security; not every vulnerability or bug report.
- Annex II point 2: user-facing single point of contact and location of the manufacturer's CVD policy.

The current Annex I structure is **Part I (product properties)** and **Part II (vulnerability handling)**. Annex III separately lists Important Products, Class I and Class II. Secure-by-default is Annex I Part I(2)(b), not a Class II requirement.

## 2. Report-by-report results

### Report #8 — secure-by-default / initial access controls

- Main commit: [2a295906507f0f2540a3c09cd760b5c77c4fb373](https://github.com/useformotor3/ai-discord-bot/commit/2a295906507f0f2540a3c09cd760b5c77c4fb373)
- Archive: `research_archive/2026-11-13_003535.md`
- Archive blob SHA: `8141a7ff3d71cd2899e10a85c735b15351c72161`
- Pass A: identifies secure-by-default, reset, default credentials, debug ports, unused services and first-boot password setup.
- Pass B: the report's alleged Annex I(a)/(b) quotation does not match the current final Regulation. Current secure-by-default is Annex I Part I(2)(b); access controls are Part I(2)(d); attack-surface limitation is Part I(2)(j).
- Pass C: the text does not prescribe a universal first-boot forced password change, blanket JTAG/debug disablement, or disabling every unused port/service in all products. Such measures may be risk-based design choices depending on interfaces, intended purpose and threat assessment. Reset to original state is expressly included in Part I(2)(b).
- File verdict: **CONFLICT**.
- Raw Text Quote verdict: **REJECTED** (draft/legacy wording and incorrect subpoint mapping; not a verbatim quotation of the current Regulation).
- Claim verdict: secure-by-default/reset theme PARTIALLY_SUPPORTED; forced password-change and blanket debug/port-disablement claims REJECTED as universal statutory mandates.
- Product applicability: UNVERIFIED.

### Report #9 — vulnerability handling and free updates

- Main commit: [fda58af984b8e5d0ad06d0f2e6bcdb19563e6914](https://github.com/useformotor3/ai-discord-bot/commit/fda58af984b8e5d0ad06d0f2e6bcdb19563e6914)
- Archive: `research_archive/2026-11-13_004046.md`
- Archive blob SHA: `c06112da2cd050b4eb0813828beb948975fb82d4`
- Pass A: claims free security patches throughout product expected lifetime/minimum five years; merges update availability, user notification, CVD and manufacturer duties.
- Pass B: free updates are Annex I Part II(8), not the quoted combined Annex I Part I/Manufacturer Obligations passage. CVD is Part II(5), information-sharing/contact is Part II(6), secure distribution is Part II(7), remediation without delay is Part II(2). Manufacturer duties are in Article 13, not Article 11.
- Pass C: the support period rule is Article 13(8), with an exception when expected use is less than five years. Article 13(9)'s ten-year-or-remaining-support availability rule is separate from free update provision. Part II(8) has the tailor-made product/business-user agreement exception. Article 14 reporting is not a universal reporting duty for all vulnerabilities.
- File verdict: **CONFLICT**.
- Raw Text Quote verdict: **REJECTED** (composite wording, wrong provision mapping and non-verbatim text).
- Claim verdict: free update/CVD/remediation themes are present in the Regulation but the report's legal structure, support-period wording and scope are materially incorrect.
- Product applicability: UNVERIFIED.

### Report #10 — secure-by-default mislabeled as Class II

- Main commit: [5f45f1c28fd3b1542c4b574d495fadd009716e09](https://github.com/useformotor3/ai-discord-bot/commit/5f45f1c28fd3b1542c4b574d495fadd009716e09)
- Archive: `research_archive/2026-11-13_004542.md`
- Archive blob SHA: `e9d5f5606a95567a9535de119edbbfa34739d02b`
- Pass A: repeats secure-by-default and forced first-use password change; labels it Annex I Part II / Class II and cites PE-CONS 105/23 draft text.
- Pass B: secure-by-default is Annex I Part I(2)(b); Part II concerns vulnerability handling. Class I/II categories are separately listed in Annex III. Current Annex I Part I(2)(d) addresses access controls.
- Pass C: the report supplies no evidence that a generic servo drive is an Annex III Class II product. The cited proposal/final compromise text is not a substitute for checking the final Regulation. Forced unique password generation and least-privilege administrator separation are not prescribed by the cited provision as universal implementation details.
- File verdict: **CONFLICT**.
- Raw Text Quote verdict: **REJECTED** (draft text/incorrect structure and location).
- Claim verdict: secure-by-default topic is relevant, but Class II and Annex Part attribution are wrong; detailed password/privilege requirements are overclaimed.
- Product applicability: UNVERIFIED.

### Report #11 — secure-by-default / out-of-the-box security

- Main commit: [76589196b933c1da5ffbff47270dacf16dc4044a](https://github.com/useformotor3/ai-discord-bot/commit/76589196b933c1da5ffbff47270dacf16dc4044a)
- Archive: `research_archive/2026-11-13_005038.md`
- Archive blob SHA: `3dab8049841c07992184993c5b18fc1dcab94836`
- Pass A: asserts all open ports/USB/service Ethernet/JTAG/test accounts must be disabled by default and unique strong passwords must be forced at first commissioning; cites vague/placeholder Regulation identifier and Annex I sections.
- Pass B: current law supports risk-based appropriate cybersecurity (Part I(1)), secure-by-default (Part I(2)(b)), appropriate access controls (Part I(2)(d)) and attack-surface limitation including external interfaces (Part I(2)(j)).
- Pass C: those outcome-oriented requirements do not literally prescribe blanket disabling of every port/interface or universal first-use password creation. The alleged quote “a appropriate level...” is grammatically malformed and merges/paraphrases separate legal concepts; the following secure-default line is not a complete faithful quotation with the correct final provision reference.
- File verdict: **CONFLICT**.
- Raw Text Quote verdict: **REJECTED** (malformed/composite/paraphrased quote).
- Claim verdict: broad security-by-default and attack-surface themes are supported; universal implementation mandates are not.
- Product applicability: UNVERIFIED.

### Report #12 — CVD policy and reporting

- Main commit: [59d1b14dcdb95badace59a13fe46a00e1e4177f9](https://github.com/useformotor3/ai-discord-bot/commit/59d1b14dcdb95badace59a13fe46a00e1e4177f9)
- Archive: `research_archive/2026-11-13_005535.md`
- Archive blob SHA: `acda92dbe87ffbc549a8d52d42961b4bf058b983`
- Pass A: states manufacturers must establish VDP/CVD, accept vulnerability reports, publish a contact route, provide free patches and report to ENISA/CSIRT; labels Article 11 as manufacturer instructions/information and quotes Annex I Part II “Section 1/2”.
- Pass B: CVD policy is Annex I Part II(5); vulnerability information-sharing/contact is Part II(6); remediation is Part II(2); secure distribution is Part II(7); free security updates are Part II(8). Article 13(8) requires appropriate policies/procedures including CVD. Article 13(17) establishes a single point of contact; Annex II point 2 places that contact and CVD-policy location in user information. Article 14 applies to actively exploited vulnerabilities and severe incidents affecting product security.
- Pass C: the quoted CVD sentence is not the exact wording of current Part II(5), which says to “put in place and enforce” a CVD policy. The remediation quote changes the statutory phrase “without delay” to “without undue delay”. Article 14 reporting must not be expanded to every potential vulnerability. The report mislabels Article 11 and conflates CVD policy, user-facing contact and Article 14 notifications.
- File verdict: **CONFLICT**.
- Raw Text Quote verdict: **REJECTED** (non-verbatim wording and incorrect Article/Annex point references).
- Claim verdict: CVD and contact obligations exist, but the report's citations, direct quotes and reporting scope are materially inaccurate.
- Product applicability: UNVERIFIED.

## 3. Batch summary

| Measure | Result |
|---|---:|
| Reports audited | 5 |
| File verdict CONFLICT | 5 |
| File verdict PARTIALLY_VERIFIED | 0 |
| File verdict VERIFIED | 0 |
| Raw Text Quote blocks reusable as direct current-law quotations | 0 / 5 |
| Product-specific applicability | UNVERIFIED for all 5 |

This is a time-sequenced, non-random five-report batch. It is not a representative sample and must not be used to estimate the error rate of the full archive.

## 4. Corrections reusable in project documents

1. Use exact current structure: Annex I Part I(1) risk-based overall level; Part I(2)(b) secure-by-default/reset; Part I(2)(d) access control; Part I(2)(j) attack-surface limitation.
2. Do not claim the CRA universally requires forced first-boot password change, unique default password, blanket JTAG disablement or disabling all ports. Treat these as risk-based design candidates unless another applicable rule/standard/product requirement proves otherwise.
3. Keep Annex I Part II(2) remediation, (5) CVD, (6) contact/information sharing, (7) secure update distribution and (8) free updates separate.
4. Keep Article 13(8) support period, Article 13(9) security-update availability, Article 13(17) single contact and Article 14 reporting scope separate.
5. Do not assign a servo drive to Annex III Class I/II without core-functionality/category evidence.
6. Preserve original archive files unchanged; record corrections in this separate audit.

## 5. Sources

- EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 13(8)–(9), Article 13(17), Article 14(1)–(4): same EUR-Lex document, Articles 13 and 14.
- Annex I Part I(1)–(2), Part II(2),(5)–(8), Annex II point 2, Annex III: same EUR-Lex document, Annexes I–III.

## 원자 Claim ID 연결 — #8–#12

- #8–#12에 대해 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID 31개를 등록했다.
- VERIFIED는 해당 법령 문장만 확인했다는 뜻이며 제품별 적용성/제품 적합성 판정이 아니다.
- 파일 단위 결과는 그대로 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED, direct quote reuse 0/5다.
- 주요 반증: secure-by-default는 Annex I Part I(2)(b), access control은 Part I(2)(d), attack-surface limitation은 Part I(2)(j); Class II는 Annex III의 별도 분류. Part II는 vulnerability handling requirements다.
- 강제 첫 접속 비밀번호 변경, 모든 JTAG/포트 비활성화, 일률적 least-privilege 구현은 해당 조항의 보편적 직접 의무가 아니다.
