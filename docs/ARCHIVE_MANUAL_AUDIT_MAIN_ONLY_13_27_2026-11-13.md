# Main-only Archive Manual Audit — Reports #13–#27

## 한국어 핵심 요약

- 대상: main 보고서 #13–#27, 총 15건.
- 판정: CONFLICT 15건 / PARTIALLY_VERIFIED 0건 / VERIFIED 0건.
- 현행 CRA 법령 직접 인용으로 재사용 가능한 Raw Text Quote: 0/15.
- 제품별 적용성: 15건 모두 UNVERIFIED.
- 반복 오류: 제조사 의무/신고 조항을 Article 11로 오기, Article 14 신고 범위 확대, CVD·신고 연락처·무상 업데이트를 Annex I Part I/II에서 혼합, 지원기간의 5년 예외를 잘못 표현, 서보 드라이브의 Class I/II 자동 분류, 첫 접속 비밀번호 변경·MFA·JTAG 잠금·모든 포트 비활성화·Secure Boot 등을 보편적 법적 의무로 과장.
- 정정 기준: 제조사 의무 Article 13, 신고 Article 14, 지원기간 Article 13(8), 업데이트 가용성 Article 13(9), CVD Annex I Part II(5), 신고 연락처/정보 공유 Part II(6), 무상 보안 업데이트 Part II(8), secure-by-default Part I(2)(b), 접근통제 Part I(2)(d), 공격표면 Part I(2)(j).
- 아래 영문 상세 감사 기록은 원본 주장·commit·archive SHA 추적을 보존한다. 독자용 정본 설명은 한국어 CRA 법령 기준선과 제1권을 참조한다.


- Audit date: 2026-11-13
- Target branch: `cra-project-foundation`
- Original source branch: `main` (read-only)
- Scope: main-only auto-archive reports #13–#27; report bodies, legal references, Raw Text Quote blocks and product-applicability claims.
- Protocol: Pass A claim/quote extraction; Pass B comparison against the repository's EUR-Lex current-law baseline (Regulation (EU) 2024/2847, CELEX 32024R2847); Pass C countercheck of provision structure, exceptions, reporting scope and product classification.
- Evidence limitation: the current EUR-Lex baseline was directly checked in the preceding #8–#12 audit and the legal-baseline record; this batch did not run the new Phase E fetcher or make a fresh live fetch. This is not independent third-party legal review.
- Product applicability: UNVERIFIED. Actual servo-drive SKU, intended purpose, product boundary, network/update configuration and ST MCU order code remain unknown.

## 1. Controlling legal map used

- Article 13(1)–(2): manufacturer design/development/manufacture and cybersecurity risk assessment duties; Article 13(8): support-period determination, normally at least five years but corresponding to expected use where expected use is shorter; Article 13(9): security-update availability for at least ten years after issuance or the remaining support period, whichever is longer; Article 13(17): manufacturer single point of contact.
- Article 14: mandatory reporting tracks are (a) actively exploited vulnerabilities contained in the product and (b) severe incidents affecting product security. Do not expand this to every vulnerability, bug or security incident. The vulnerability track has 24-hour early warning, 72-hour notification and a final report within 14 days after a corrective/mitigating measure is available; the severe-incident track has 24-hour early warning, 72-hour notification and a final report within one month after the incident notification.
- Annex I Part I(1): risk-based overall cybersecurity level. Part I(2)(b): secure-by-default configuration and reset to original state; (2)(d): appropriate access controls; (2)(e)/(f): confidentiality/integrity; (2)(j): attack-surface limitation including external interfaces.
- Annex I Part II(2): vulnerability remediation without delay and separation from functionality updates where technically feasible; (5): coordinated vulnerability disclosure policy; (6): vulnerability information sharing/contact; (7): secure update distribution; (8): available security updates without delay and free of charge, subject to the tailor-made product/business-user agreement exception.
- Annex II points 1–9 are user-facing information/instructions, not the Annex VII technical-documentation structure. Annex III separately lists Important Products and Class I/II categories; a generic servo drive is not automatically Class I or II.
- Secure Boot, cryptographic signing, anti-rollback, A/B banks, mandatory first-boot password change, MFA, blanket JTAG lockout and blanket disabling of all ports are not universal implementation commands stated by the cited CRA provisions. They may be risk-based design candidates, subject to product facts and applicable standards.

## 2. Report-by-report findings

All 15 files are **CONFLICT** at file level. Every Raw Text Quote block is **REJECTED** for reuse as a verbatim quotation of the current Regulation. Where a topic is relevant, that does not validate the report's legal mapping, direct quote or implementation mandate.

### #13 — CVD / vulnerability and incident reporting
- Main commit: [5b46858ab88595ce9e5b7b33175b81c4e24e7905](https://github.com/useformotor3/ai-discord-bot/commit/5b46858ab88595ce9e5b7b33175b81c4e24e7905)
- Archive: `research_archive/2026-11-13_010102.md`; blob SHA-1: `2e9fb641dcebcb411dca1e686de916bf09dbfcb9`.
- Pass A: combines CVD, general vulnerability/incident notification and ENISA reporting; cites Article 11 and uses quotations referencing the NIS2 single point of contact.
- Pass B/C: CRA manufacturer reporting is Article 14, not Article 11. CVD policy is Annex I Part II(5), contact/information sharing is Part II(6), and user-facing contact/policy information is Annex II point 2. Article 14 is limited to actively exploited vulnerabilities and severe incidents. The quoted text is not a faithful quotation of the current CRA structure.
- Claim disposition: CVD/reporting concepts are relevant; article number, reporting scope and quotations rejected. **CONFLICT**.

### #14 — Secure-by-default / attack-surface reduction
- Main commit: [f4e8b82ad46f3fe5c5a6f55d0fcd33d44d0006d1](https://github.com/useformotor3/ai-discord-bot/commit/f4e8b82ad46f3fe5c5a6f55d0fcd33d44d0006d1)
- Archive: `research_archive/2026-11-13_010538.md`; blob SHA-1: `dda0e0308d5fffb11659f6c395a9b0a3da26b1de`.
- Pass A: says all default accounts, remote ports and debug interfaces must be disabled and first-use password setup forced; cites draft-era Annex I lettering.
- Pass B/C: current secure-by-default is Annex I Part I(2)(b), access controls Part I(2)(d), attack-surface limitation Part I(2)(j). The report's quoted subparagraphs do not match the current final numbering/text. CRA does not state a universal first-boot password change or blanket disablement of every interface.
- Claim disposition: high-level theme supported; universal implementation mandates and quote rejected. **CONFLICT**.

### #15 — VDP / free security updates
- Main commit: [54e67c1082d86fd8559d6c41107cdc9736ce8c76](https://github.com/useformotor3/ai-discord-bot/commit/54e67c1082d86fd8559d6c41107cdc9736ce8c76)
- Archive: `research_archive/2026-11-13_011036.md`; blob SHA-1: `f150569deac61b8d74a424bb1c76518438816de0`.
- Pass A: correctly identifies the general subjects of free security updates and VDP/CVD, but attributes them to Annex I Part I and Article 11; quotes a purported combined update/CVD obligation.
- Pass B/C: free updates are Annex I Part II(8); CVD is Part II(5); contact/information sharing is Part II(6); secure distribution is Part II(7); remediation is Part II(2). The quoted sentence is not the current provision verbatim, and the report overstates support-period duration.
- Claim disposition: themes relevant; legal mapping and quote rejected. **CONFLICT**.

### #16 — VDP / free updates / support period
- Main commit: [c0f038825fcda6f2d546846870e0505080b96cb5](https://github.com/useformotor3/ai-discord-bot/commit/c0f038825fcda6f2d546846870e0505080b96cb5)
- Archive: `research_archive/2026-11-13_011537.md`; blob SHA-1: `2f67047e45084598819a1d7b4ccd4a463c2dc168`.
- Pass A: states a blanket minimum-five-year free patch period, locates free updates in Article 11/Annex I Part I and merges single contact, CVD and update handling.
- Pass B/C: support period is Article 13(8), with the expected-use-shorter-than-five-years exception; free updates are Annex I Part II(8), CVD Part II(5), contact/information sharing Part II(6). The report's purported Article 11 and Annex I quotes do not match the current Regulation.
- Claim disposition: underlying topics relevant; duration, citations and quote rejected. **CONFLICT**.

### #17 — vulnerability handling / free updates
- Main commit: [1e5fddc195a8f94483fdffbd3aa7b7ef4704c9e7](https://github.com/useformotor3/ai-discord-bot/commit/1e5fddc195a8f94483fdffbd3aa7b7ef4704c9e7)
- Archive: `research_archive/2026-11-13_012038.md`; blob SHA-1: `a2a8c24d6e0933f5d6e3e6fcdb570037ed652e7e`.
- Pass A: combines reporting contact, free updates, CVD, A/B partitioning and atomic updates; assigns the obligations to Article 11 and Annex I Part I.
- Pass B/C: CVD/free-update duties belong to Annex I Part II(5)/(8); contact/information sharing to Part II(6); Article 14 is the narrow mandatory reporting provision. A/B partitioning and atomic update behavior are engineering options, not universal wording in these provisions. The long Raw Text Quote is a composite rather than a verbatim legal passage.
- Claim disposition: topics relevant; legal map and quote rejected; A/B/atomic update is a proposal only. **CONFLICT**.

### #18 — actively exploited vulnerabilities / incidents reporting
- Main commit: [d5b4441be57c9a33cd256b30392f546cd6026b23](https://github.com/useformotor3/ai-discord-bot/commit/d5b4441be57c9a33cd256b30392f546cd6026b23)
- Archive: `research_archive/2026-11-13_012535.md`; blob SHA-1: `a39605cfc909d39990ecc46bdd8caa5e8f97efd4`.
- Pass A: identifies actively exploited vulnerabilities and severe incidents, but calls the provision Article 11 and describes notification of vulnerabilities/incidents broadly.
- Pass B/C: CRA reporting is Article 14. Only actively exploited vulnerabilities contained in the product and severe incidents affecting product security trigger the mandatory tracks. The report gives the 24h/72h milestones but omits the distinct final-report deadlines and incorrectly references Article 11/NIS2 contact language.
- Claim disposition: topic and some timing concepts relevant; article number, scope and incomplete timeline rejected. **CONFLICT**.

### #19 — vulnerability handling / free updates / support duration
- Main commit: [eb1d64f8b60127c0d68119ce06a8f0b9e63471da](https://github.com/useformotor3/ai-discord-bot/commit/eb1d64f8b60127c0d68119ce06a8f0b9e63471da)
- Archive: `research_archive/2026-11-13_013047.md`; blob SHA-1: `8211d1c2905452bf87e41722ca408119092644d1`.
- Pass A: claims minimum five years or product lifetime, “whichever is shorter”; attributes duties to Article 11; assigns CVD/free updates to Annex I Part II(1); mandates cryptographic signing/Secure Boot.
- Pass B/C: Article 13(8) is the support-period rule and does not say “five years or expected lifetime, whichever is shorter”; the shorter-expected-use exception is narrowly stated. Annex I Part II(1) concerns identification/documentation of vulnerabilities/components and SBOM, not the quoted free-update/CVD block. Free updates and CVD are Part II(8)/(5). Signing/Secure Boot may be selected from risk assessment but are not universal commands in those cited clauses.
- Claim disposition: multiple material legal errors; quote rejected. **CONFLICT**.

### #20 — Secure-by-default / initial configuration
- Main commit: [6ec0d9eee85c141e1ab2e621d5a3989855c98c35](https://github.com/useformotor3/ai-discord-bot/commit/6ec0d9eee85c141e1ab2e621d5a3989855c98c35)
- Archive: `research_archive/2026-11-13_013528.md`; blob SHA-1: `d80151fca7d8302bd353715b3d8608412b99e065`.
- Pass A: cites Annex I Part I(2)(b) and (f) for secure-by-default and mandatory first-use credential changes.
- Pass B/C: Part I(2)(b) is secure-by-default; Part I(2)(f) is integrity. The report therefore misuses the integrity provision as a first-boot-password mandate. The final text does not universally require a password-change flow on first connection.
- Claim disposition: secure-by-default is relevant; (f) mapping, forced password mandate and quote rejected. **CONFLICT**.

### #21 — secure defaults / support / user information
- Main commit: [8fafb874c5e1427d65def1b1672459d376e33567](https://github.com/useformotor3/ai-discord-bot/commit/8fafb874c5e1427d65def1b1672459d376e33567)
- Archive: `research_archive/2026-11-13_014042.md`; blob SHA-1: `34c0a04a117ff8175bec68e93e26600b520cebb5`.
- Pass A: merges secure defaults, hardcoded credential prohibition, free patches and minimum-five-year support; labels Annex II as technical documentation.
- Pass B/C: Annex II is user information/instructions; technical documentation is Article 31/Annex VII. Support is Article 13(8), including the shorter expected-use exception; free updates are Annex I Part II(8). Secure-by-default is Part I(2)(b), access control Part I(2)(d). The quotes and subsection names do not match the final Regulation.
- Claim disposition: mixed relevant themes but materially wrong provision map and quote. **CONFLICT**.

### #22 — secure defaults / class classification
- Main commit: [3a0b1aec3c17d5ea61dcd674a71b12ba487b3b01](https://github.com/useformotor3/ai-discord-bot/commit/3a0b1aec3c17d5ea61dcd674a71b12ba487b3b01)
- Archive: `research_archive/2026-11-13_014539.md`; blob SHA-1: `a6695390839a167aa9a4b99473b2a70ba61dc838`.
- Pass A: describes servo drives as Class I/II without category/core-function evidence; requires hardcoded credentials ban, forced password/MFA and disabling all nonessential services.
- Pass B/C: Annex III classification depends on the listed category/core functionality, not the generic servo-drive label. Secure-by-default/access control/attack-surface requirements are Annex I Part I(2)(b),(d),(j), but the report's quote and point labels are wrong. The detailed mechanisms are not universal direct mandates.
- Claim disposition: general secure-default topic relevant; Class I/II assertion, quote and blanket controls rejected. **CONFLICT**.

### #23 — secure defaults / mandatory initial setup
- Main commit: [0d5cc63bd9bbe47eb84887950c056d2d4df80f73](https://github.com/useformotor3/ai-discord-bot/commit/0d5cc63bd9bbe47eb84887950c056d2d4df80f73)
- Archive: `research_archive/2026-11-13_015044.md`; blob SHA-1: `d8315ca10d9d1d811978c73ab8ffbd77e296971d`.
- Pass A: treats mandatory first-boot credential setup as a legal prerequisite; quotes secure-default and reset language using incorrect letter labels and draft-like wording.
- Pass B/C: current secure-by-default is Annex I Part I(2)(b), access controls Part I(2)(d), attack-surface limitation Part I(2)(j). The report's quotation and subpoint labels do not faithfully reproduce the final text. A forced first-use password flow is a possible design choice, not a universal CRA instruction.
- Claim disposition: broad topic relevant; quote and mandatory setup claim rejected. **CONFLICT**.

### #24 — secure defaults / ports / updates
- Main commit: [4a13cfeb9cba3e378b68e52ee5e7c03990cca3ca](https://github.com/useformotor3/ai-discord-bot/commit/4a13cfeb9cba3e378b68e52ee5e7c03990cca3ca)
- Archive: `research_archive/2026-11-13_015535.md`; blob SHA-1: `c43117db6c681bd4b6865b955ac66a0fa012a1fd`.
- Pass A: states forced password changes and disabling diagnostic/web/legacy services as mandatory; quote combines secure-default and update provisions with incorrect numbering.
- Pass B/C: secure-default is Annex I Part I(2)(b); updates are in Part I(2)(c) and vulnerability handling in Part II. The quote's paragraph/subpoint structure does not match the current Regulation. Blanket disabling of all diagnostic/web/legacy services is not stated as a universal rule.
- Claim disposition: secure-default theme relevant; direct quote and universal interface mandate rejected. **CONFLICT**.

### #25 — secure defaults / Important Product claim
- Main commit: [7d308b5a2b5c73385abde943412622bdc8f74317](https://github.com/useformotor3/ai-discord-bot/commit/7d308b5a2b5c73385abde943412622bdc8f74317)
- Archive: `research_archive/2026-11-13_020056.md`; blob SHA-1: `a482f9198569dfe173d63250eebee6d8f9a6f9e8`.
- Pass A: labels servo drives as Important Digital Elements/Class I or II and claims JTAG/UART lockout, unique credentials and disabled services as mandatory; quotes Annex I with obsolete/draft-like numbering.
- Pass B/C: Article 7/Annex III classification requires a listed category and core-functionality analysis. The report supplies no evidence for a servo-drive Class I/II classification. Current secure-default/access/attack-surface locations are Part I(2)(b),(d),(j); the quoted paragraph mapping is wrong.
- Claim disposition: no product class can be assigned; implementation details are proposals only; quote rejected. **CONFLICT**.

### #26 — secure defaults / interface minimization / integrity
- Main commit: [d079e63339d20549361bba9d4c4de71fcb3346db](https://github.com/useformotor3/ai-discord-bot/commit/d079e63339d20549361bba9d4c4de71fcb3346db)
- Archive: `research_archive/2026-11-13_020541.md`; blob SHA-1: `132dd081b4bed0d431d8f68b8e00b3fc83b9035d`.
- Pass A: asserts common/hardcoded password prohibition, forced unique credentials, disabling all unused fieldbus/USB/debug functions and backdoor/test-code exclusion; quotes Annex I as (a)/(b)/(f).
- Pass B/C: current Part I(2)(b) is secure-default, (2)(d) access control, (2)(f) integrity and (2)(j) attack-surface limitation. The report mislabels the secure-default quote and mixes several distinct requirements. Specific forced-credential and interface-disablement measures require product risk/design justification rather than being universal textual mandates.
- Claim disposition: several risk themes are relevant; quote and blanket mandates rejected. **CONFLICT**.

### #27 — CVD / free updates
- Main commit: [c7eb7296671541c1ad2268cdcee80885091f230c](https://github.com/useformotor3/ai-discord-bot/commit/c7eb7296671541c1ad2268cdcee80885091f230c)
- Archive: `research_archive/2026-11-13_021039.md`; blob SHA-1: `3b6537c40590118c43d1fbc5f1922121d7f6d276`.
- Pass A: identifies free security updates and CVD, but assigns them to Annex I Section 1/Part I and quotes Article 13(4) as a free-update obligation.
- Pass B/C: free updates are Annex I Part II(8), CVD Part II(5), contact/information sharing Part II(6), secure distribution Part II(7); Article 13(8)/(9) govern support period/update availability. Article 13(4) is not the quoted free-update provision. The quoted Annex I/Article text is not verbatim current law.
- Claim disposition: topics relevant; legal citations and quotes rejected. **CONFLICT**.

## 3. Batch summary

| Measure | Result |
|---|---:|
| Reports audited | 15 |
| File verdict CONFLICT | 15 |
| File verdict PARTIALLY_VERIFIED | 0 |
| File verdict VERIFIED | 0 |
| Raw Text Quote blocks reusable as current-law verbatim quotes | 0 / 15 |
| Product-specific applicability | UNVERIFIED for all 15 |

This is a sequential, non-random batch selected by report number/time. It is not a representative sample and must not be used to estimate the error rate of the complete archive.

## 4. Reusable correction rules

1. Use the current CRA structure: Annex I Part I covers product cybersecurity properties; Part II covers vulnerability handling.
2. Keep Part II(2) remediation, (5) CVD policy, (6) contact/information sharing, (7) secure distribution and (8) free updates separate.
3. Keep Article 13(8) support period, Article 13(9) update availability and Article 14 reporting separate.
4. Article 14 is not a catch-all vulnerability notification rule; retain the actively exploited vulnerability and severe-incident tracks and their separate final-report deadlines.
5. Annex II is user information/instructions; technical documentation is Article 31/Annex VII.
6. Do not infer Important Product Class I/II from the words “servo drive”; prove the Annex III category/core-functionality criteria.
7. Treat first-boot password change, MFA, JTAG lockout, signed firmware, anti-rollback, A/B bank and blanket port disabling as risk-based design candidates unless another applicable requirement proves them mandatory.
8. Keep product-specific applicability UNVERIFIED until actual SKU, intended purpose, interfaces, update path and MCU order code are known.

## 5. Evidence and limits

- Original main branch report files were fetched read-only; report archive blobs and auto-archive commit IDs are recorded above.
- The repository's previously checked EUR-Lex current-law baseline was used for provision mapping. This batch did not invoke Phase E live fetch, did not store raw source documents and did not modify main.
- Same AI performed the review. It is not independent legal advice, an external audit or conformity assessment.
- No tests were run for this documentation-only audit; no CI PASS is claimed.

## 원자 Claim ID 연결 — #13–#17

- #13–#17에 대해 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID 29개를 등록했다.
- 파일 단위 결과는 기존대로 5 CONFLICT / direct quote reuse 0/5다.
- Article 14는 모든 CRA 범위 제품에 적용되는 두 신고 트랙이며 Class I/II에만 한정하지 않는다. CVD·연락처·무상 업데이트는 Annex I Part II(5)/(6)/(8), 제조사 의무는 Article 13이다.
- secure-by-default Part I(2)(b), access control (d), attack surface (j)를 서로 분리하고 first-boot password/blanket interface disablement를 보편적 법적 의무로 쓰지 않는다.

## 원자 Claim ID 연결 — #18–#22

- #18–#22에 대해 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID 29개를 등록했다.
- 파일 단위 결과는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- Article 14 신고 trigger, support period Article 13(8), free updates Part II(8), CVD Part II(5), contact Part II(6), secure default Part I(2)(b), access control (d), integrity (f), attack surface (j)를 서로 분리했다.
- Secure Boot/signing/A-B partition/MFA/first-use password 등은 해당 조항의 보편적 명문 의무로 쓰지 않고 제품별 위험기반 설계 후보로 기록한다.
