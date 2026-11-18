# CRA 프로젝트 현재 상태 — 2026-11-18 KST

> 이 문서는 2026-11-18 재개 시점의 최신 상태 스냅샷이다. 기존 날짜별 SESSION_LOG 및 PROJECT_LOG의 역사 기록을 대체하지 않는다. 충돌 시 본 문서의 최신 main 기준 사실과 원본 PR/Actions 증거를 우선한다.

## 활성 범위
- 활성 프로젝트: EU Cyber Resilience Act(CRA) 조사·요구사항 추적·제품 적용성/기술 설계·보고서 검증.
- SIL 3 기능안전 자료는 과거 산출물로 보존하며 비활성이다. 별도 명시적 재개 지시 전까지 후속 작업하지 않는다.
- 보고서 기본 언어: 한국어.
- 제품별 적합성/Annex III·IV 분류는 제조사·정확한 모델·의도된 목적·제품 경계·인터페이스·공급 구조 증거 없이는 확정하지 않는다.

## 최신 기준점 및 PR #42 결과
- 기준 브랜치: `main`
- PR #42: [docs: clarify CRA legal locator and SBOM requirements](https://github.com/useformotor3/ai-discord-bot/pull/42) — merged.
- Merge commit: `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`
- PR head: `0ff686be74fb5c6309b46ed9c01473251d997579`
- CI: [Run #824](https://github.com/useformotor3/ai-discord-bot/actions/runs/44061121932) — success; 155 passed / 1 xfailed.
- 검증 단계: source blob integrity, compile, CRA cross-matrix traceability, full pytest, official PDF source fetch/hash/page canary, artifact upload, 9 official HTML sources 및 Article 13(8) live locator/quote canary.
- 변경 범위: 문서·감사·상황판/프로젝트 관리 자료. production runtime, production workflow, state/history/archive, Gemini/Discord side effects, SIL 3 자료는 변경하지 않았다.
- 리뷰 스레드/리뷰 제출은 없었으며 PR은 exact head CI 성공 후 squash merge했다.

## 복구 및 main 정합성
- Pre-merge safety ref: `safety/pre-merge-main-pr42-2026-11-18` → `acfa2f583157ac541c4c60d71090197322bc8efb`
- Post-merge safety ref: `safety/post-merge-main-pr42-2026-11-18` → `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`
- GitHub compare: `main` vs post-merge safety ref = identical, 0 ahead / 0 behind.
- 롤백이 필요하면 force-push 대신 검토된 revert commit을 우선한다. safety refs는 삭제하지 않는다.

## 현재 CRA 산출물 기준선
- 통합 한국어 보고서: `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` (v0.2 draft; 제품별 검증 전)
- 요구사항 추적표: `reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv` (CRA-001–CRA-035)
- 인터페이스 적용성 매트릭스: 15 rows
- SEC 통제/시험 매트릭스: 36 rows
- Commission Guidance claim register: 13 claims
- M/606 Annex I crosswalk: 41 items
- 독립 보고서 감사: `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md`
- 법령 locator 1차 인벤토리 검토는 35행 모두 조항 번호/구조의 명백한 불일치가 보이지 않았다는 수준이다. 모든 문장의 의무 주체·조건·예외·기한을 확정한 최종 법률 검토가 아니다.

## 확정된 SBOM 해석
1. Annex I Part II(1): 제조자의 기본 SBOM 작성 의무. 일반적으로 사용되는 기계 판독 가능 형식이며 최소 최상위 의존성을 포함한다.
2. Annex VII(2)(b): 취약점 처리 프로세스 설명에 SBOM을 기술문서 내용으로 포함한다.
3. Annex VII(8): 필요한 경우 시장감시당국의 합리적 요청에 따른 추가 제공 조항이다. 기본 작성 의무를 선택사항으로 만들지 않는다.
4. Annex II(9): 제조자가 SBOM을 사용자에게 제공하기로 결정한 경우 접근 위치 정보를 제공한다. 일반 사용자 공개 의무와 기본 작성/기술문서 의무를 혼동하지 않는다.

## 남은 원문 provenance 제한
- M/606 C(2026) 7861 Annex PDF: 151,267 bytes, 6 pages, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`; primary Commission source canary fallback=False.
- Commission Guidance C(2026) 5252 Annex PDF: ANFR mirror fallback bytes 1,190,726, 84 pages, SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; fallback=True. Commission-hosted primary bytes와의 동일성은 미확인이다.
- CI artifact #14318292097, Run #824에서 업로드 성공. artifact URL: https://github.com/useformotor3/ai-discord-bot/actions/runs/44061121932/artifacts/14318292097

## 다음 실행 순서
1. CRA-001–CRA-035를 법령 원문 기준으로 행 단위 심층 검토한다. 조항 locator뿐 아니라 의무 주체, 행위, 적용 조건, 예외, 기한, 보존기간, 제품 사실 전제 및 근거 문장을 별도 확인한다.
2. 발견 사항은 CSV·통합 보고서·SEC 통제/시험 매트릭스·독립 감사 기록을 한 변경 묶음으로 정합화한다. 법적 의무와 Guidance 해석, M/606 표준화 작업, 설계 권고를 분리한다.
3. Article 14 신고 시한/범위, Article 13 지원기간·업데이트 보존, Annex I Part II SBOM/취약점 처리, Article 32 평가 경로, Article 69 전환/중복 규칙을 우선 위험 영역으로 검토한다.
4. Guidance PDF Commission-primary byte identity 취득 경로를 계속 확인하되 mirror fallback을 원본이라고 표시하지 않는다.
5. 각 작업은 main 기준 feature/docs branch, pre-merge safety ref, exact-head CI, squash merge, post-merge safety ref 및 main compare를 유지한다.

## 해석상 금지
- CRA 적용 대상/등급/적합성/인증 경로를 특정 서보 드라이브 모델에 대해 증거 없이 단정하지 않는다.
- M/606 요청/ESO adoption deadline을 조화표준 OJ 공표나 제조사 CRA 적용일로 취급하지 않는다.
- CRA와 SIL 3 기능안전 인증을 동일시하지 않는다.
- CI 통과를 법적 적합성 또는 제품 시험 완료로 확대 해석하지 않는다.


## 최신 진행 추가 — CRA 법령 문언 Batch 1 (2026-11-18)
- 작업 브랜치: `cra/legal-semantics-audit-batch1-2026-11-18` (PR 전 검증 중)
- 검토 범위: CRA-001–CRA-010, EUR-Lex Regulation (EU) 2024/2847 공식 원문 대조.
- 상세 결과: `reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md`.
- CSV locator 보완: CRA-001 연결 정의 Article 3(8)–(10)/Recital 9 추가; CRA-003의 부적절한 Article 13(2) 제거 및 Article 3(2)/Recital 11–12로 교체; CRA-006 SBOM/기록/기술문서 locator 분리.
- 해석 보완: CRA-008 정기 테스트에 법정 고정 주기 숫자는 없음; CRA-009 공개 지연 예외는 정당한 사유 및 사용자 패치 적용 기회와 연결.
- CRA-001–010 행별 심층 대조는 1차 완료. 제품별 적용성/적합성은 미확정이며 전체 35행 법률 검토 완료를 의미하지 않는다.
- 다음 대상: CRA-011–CRA-020.


## 최신 진행 추가 — CRA 법령 문언 Batch 2 (2026-11-18)
- 작업 브랜치: `cra/legal-semantics-audit-batch2-2026-11-18` (PR 전 검증 중).
- 검토 범위: CRA-011–CRA-020, EUR-Lex 공식 원문 대조.
- 상세 결과: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md`.
- CSV 보완: 연락창구 통신수단 조건, 업데이트 배포 통제와 법문 구분, 무상 제공 예외의 좁은 범위, support period 5년 예외 근거, 기술문서 작성/보관 분리, Annex V/VI DoC 구분, Article 32 Class I/II/Critical 경로 구분.
- CRA-001–020까지 1차 심층 대조 완료(제품별 증거·최종 법률 검토는 미완료). 다음 대상 CRA-021–035.


## 최신 진행 추가 — CRA 법령 문언 Batch 3 (2026-11-18)
- 작업 브랜치: `cra/legal-semantics-audit-batch3-2026-11-18` (PR 전 검증 중).
- 검토 범위: CRA-021–CRA-035, EUR-Lex 공식 CRA 및 관련 sectoral 원문 대조.
- 상세 결과: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md`.
- CSV locator/구조 보완: CRA-023 Article 14(8) 중심; CRA-026 CRA Article 2(5)/Machinery Regulation Article 9(9) 중심; CRA-028 Articles 18–22와 CRA-034 Article 23 분리; CRA-035 Article 2(8) 추가 및 Article 2(5) 조건부 제한 구분.
- CRA-001–035 전체 행의 1차 심층 문언 대조가 완료되었으나, 제품별 사실/증거 확인과 법률가 검토는 별도 미완료다.
- 다음 단계: 전체 35행 교차 검증 및 CSV·통합 보고서·SEC 매트릭스·근거 등록부의 누락/중복/표현 정합성 검토, 제품 적용성 증거 수집 설계.


## 최신 진행 추가 — 전체 교차 매트릭스 감사 (2026-11-18)
- 작업 브랜치: `cra/cross-matrix-consistency-audit-2026-11-18` (PR 전 검증 중).
- PR #46 병합: `42aca53bb735d79292be59120fb868474e728073`; exact-head CI 성공, pre/post safety refs, post-ref == main 검증 완료.
- CRA-001–CRA-035 1차 심층 문언 대조 완료. 추가로 15 interfaces, 36 SEC controls, 13 Guidance claims, 41 M/606 items 간 교차 참조를 검토.
- 교차 감사 기록: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md`.
- SEC-015/018/021/031/032/034/036의 locator/설명/연계 ID 정합화.
- 제품별 실제 구현/시험 증거가 없으므로 SEC controls 상태는 미작성/증거 미확인, interfaces는 제품별 미확인 유지.
- 다음 단계: 통합 보고서 전체 독립 재검토, 제품 증거 intake 기준 확정, Commission Guidance PDF primary byte identity 재확인.


## 최신 기준점 — 2026-11-18 (PR #47 반영)
- 최신 main: `fd9733b31e5dffa382a82a420de6a195a714e98f`.
- PR #47 cross-matrix audit merge: `fd9733b31e5dffa382a82a420de6a195a714e98f`; Run #832 exact-head CI success, post-merge safety ref와 main identical 확인.
- Pre-merge ref: `safety/pre-merge-main-pr47-2026-11-18`; post-merge ref: `safety/post-merge-main-pr47-2026-11-18`.
- 35 requirements / 15 interfaces / 36 SEC controls / 13 Guidance claims / 41 M/606 items 교차 정합성 감사 기록: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md`.
- 제품 증거 수집 기준서에 최신 Article 2/3, RDPS, Annex III/IV, Machinery Regulation, 신고 시한/전환 규칙 및 우선 제출 자료를 추가하는 작업 브랜치: `cra/product-evidence-intake-update-2026-11-18`.


## 최신 main 기준점 — PR #48 병합 후 (2026-11-18)
- 현재 main commit: `dc03173cd78f6efb6f46717850a107c8165b1d1a`.
- PR #48 제품 경계/증거 수집 기준서 보완 merge: `dc03173cd78f6efb6f46717850a107c8165b1d1a`.
- Exact-head CI Run #834 success: source integrity, compile, CRA cross-matrix traceability, full pytest, official PDF/HTML canaries, artifact upload passed.
- Pre-merge ref: `safety/pre-merge-main-pr48-2026-11-18`; post-merge ref: `safety/post-merge-main-pr48-2026-11-18`; post-ref == main identical.
- 제품 증거 기준서 업데이트: Section 13–15에 데이터 연결/RDPS/Annex III·IV/Machinery/신고·전환/자료 우선순위/모델별 판정 출력 기준 추가.
- 제품별 사실 증거는 아직 미제공. P0 자료는 정확한 모델 데이터시트/카탈로그와 사용설명서이며, 이를 받기 전 CRA 적용/등급/적합성은 Unknown 유지.
- 다음 작업: 통합 보고서 전체 독립 재검토 및 Commission Guidance PDF Commission-primary byte identity 재확인. 제품 P0 자료 확보 시 모델별 판정 착수.


## 최신 재개 추가 — 통합 보고서 독립 재검토 (2026-11-18)
- 작업 브랜치: `cra/integrated-report-audit-2026-11-18`; 기준 main: `c7b939a0fdfa559f9d68a11873c107186da423c3`.
- 독립 감사 기록: `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-18.md`.
- EUR-Lex Regulation (EU) 2024/2847 공식 OJ HTML에서 Articles 7, 8, 13(8)–(9), 14, 15, 69, 71 및 관련 Annex의 핵심 문언을 표본 대조했다.
- 통합 보고서 요약의 서보 드라이브 CRA 적용 가능성/기본 제품 분류 표현을 제품별 판정이 아닌 전형적 구성의 사전 스크리닝 가설로 한정하고, 모델별 결론은 증거 확보 전 Unknown으로 유지하도록 보완했다.
- 15 interfaces는 제품별 미확인, 36 SEC controls는 미작성/증거 미확인, 제품 scope/classification/conformity는 Unknown 유지.
- Commission Guidance PDF Commission-primary byte identity는 여전히 미확인. M/606 일정은 이번 회차 원문 bytes 신규 재취득 검증이 아니므로 기존 provenance 상태를 유지.
- 다음: 변경 파일 readback, exact-head isolated CI, PR 생성/검토, 안전 참조점 및 merge 후 main 정합성 확인. CI 성공 전 병합하지 않는다.


## 최신 main 기준점 — PR #50 통합 보고서 독립 감사 병합 완료 (2026-11-18)
- PR #50 squash merge commit: `137d096123ccf5ee478292002d2c528b41981fc7`.
- PR #50 exact-head: `49e98df9a7fef8f47cabe7b036b45cc150b88b91`; isolated CI Run #840 (ID `44200596113`) success.
- Run #840 통과 단계: source blob identity, compile, CRA cross-matrix traceability, complete pytest, official CRA PDF read-only canary 및 artifact upload, live official CRA source read-only canary.
- Pre-merge safety ref `safety/pre-merge-cra-integrated-report-audit-2026-11-18`는 main 당시 기준 commit `c7b939a0fdfa559f9d68a11873c107186da423c3`와 identical. PR #50 병합 후 main은 해당 안전 기준점보다 정확히 1 commit ahead이며, 변경 파일은 PR #50의 8개 문서 파일로만 확인.
- Post-merge safety ref: `safety/post-merge-pr50-2026-11-18`; 이 ref는 새 main 기준점 `137d096123ccf5ee478292002d2c528b41981fc7`에서 생성.
- 변경 내용: 2026-11-18 통합 CRA 보고서 독립 감사 기록 추가, 전형적 서보 드라이브의 적용 가능성/Annex III·IV 표현을 사전 스크리닝 가설로 한정, 개별 모델 결론은 제조사/모델 증거 전 Unknown 유지, README/MASTER_PLAN/SESSION_LOG/PROJECT_LOG 동기화.
- 운영 `main.py`, production workflow, secrets, state/history/archive, Gemini/Discord production execution 및 SIL 3 산출물은 변경하지 않았다.
- 미해결: Commission Guidance PDF의 Commission-primary byte identity, M/606 최신 결정 raw-byte provenance 재취득, 제품별 scope/classification/conformity 및 15 interfaces/36 SEC controls의 제품 증거.
- 다음 우선순위: Commission-hosted Guidance PDF primary byte identity 검증과 M/606 공식 결정 원문/Annex provenance 확인. 제품 P0 자료(정확한 모델 데이터시트/카탈로그 및 사용설명서) 확보 시 모델별 증거 연결.

## 최신 CRA Guidance 원문 기준 — OJ C/2026/6013 (2026-11-18)
- 기존 Commission 승인/게시 문서 참조 C(2026) 5252의 guidance는 2026-11-17 Official Journal에 Communication C/2026/6013 (CELEX 52026XC06013)으로 게재되었다.
- 현재 공식 인용/페이지 기준: EUR-Lex OJ PDF https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013
- OJ PDF: 2,709,282 bytes, 61 pages, SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`; extracted text 255,974 chars, SHA-256 `384724af44e399cb997771e9e65ea4a5fe1dd264131d0754921bd691dd1f7720`.
- C(2026) 5252 ANFR mirror는 별도 역사적 사본으로 유지: 1,190,726 bytes, 84 pages, SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`. Commission download document 131456는 2026-11-18 확인 시 HTTP 404.
- 두 PDF에서 numbered paragraph IDs 1–257 모두 발견; 정규화 토큰 multiset overlap은 mirror 99.50%, OJ 99.66%. 원본 bytes/추출 텍스트가 동일하다고 주장하지 않는다.
- Guidance claims 13개(G-001–G-013)의 source ID와 PDF page locator를 OJ C/2026/6013 기준으로 갱신했다. 세부 비교 및 페이지 crosswalk: `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` §7.
- Run #844 (44204376214): exact head CI success, 156 passed / 1 xfailed; official OJ PDF primary fetch fallback=False 및 raw SHA 검증 성공. Artifact 14381529964, 7일 보존.

### 다음 작업
1. G-001–G-013 각 claim의 실제 문장·조건·예외를 OJ C/2026/6013 본문과 대조하는 substantive redline 수행.
2. OJ page locator를 표·그림·페이지 경계 포함 PDF 이미지로 표본 재검증.
3. Guidance claim IDs를 요구사항/인터페이스/SEC 매트릭스에 연결하되 법령상 의무와 비구속적 guidance 해석을 분리.
4. M/606 C(2026) 7861 Annex provenance 및 현재 표준화 상태를 최신 공식 원문과 별도 대조.

### PR #52 최종 검증 업데이트 — Run #854
- Exact-head at validation: `0ab0fc4d9b217a4994fd6e7a1b32607c854bb693`.
- Run #854 / ID `44205498935`: success; 158 passed, 1 xfailed; source blob identity, compile, CRA traceability, full pytest, three-PDF canary, official HTML canary all passed.
- OJ C/2026/6013 primary PDF: fallback=False, 2,709,282 bytes, 61 pages, SHA-256 unchanged `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`.
- Artifact #14382388555; digest `sha256:9e8dc7f1c1d90015b7738263155ca9d6b1170aaea75ea6bd17350aeff7d36af7`; expires 2026-11-25 00:09:59 UTC.
- Run #851 failure cause (validator's stale mirror-scope phrase check) corrected; validator now enforces both historical mirror-only scope and OJ primary-source/no-fallback gate. Run #854 passed.

### PR #52 exact-head CI 업데이트 — Run #857
- Tested head `152fe0bfe00c16ab32f7cc030efcde3258b73525`; Run #857 / ID `44205723336`: success.
- 158 passed, 1 xfailed; exact source blob identity, compile, CRA traceability, full pytest, three-PDF canary and live official HTML canary passed.
- OJ C/2026/6013 primary source hash unchanged; fallback=False.
- Artifact #14383167818; digest `sha256:a2f05428d57897a20a485cabaab17cbb976dcb91f6e5628ece0953ddfe22140d`; expires 2026-11-25 00:11:31 UTC.
- Provenance metadata now points to Run #857; final head after this metadata update still requires one fresh CI before merge.

## PR #52 병합 및 사후 안전 검증 — 2026-11-18
- PR #52 `feat: acquire official CRA guidance from OJ C/2026/6013` squash merge commit: `d3956b7b364c507b8d59dcfc056763f2829ea867`.
- Final exact-head Run #861 (ID `44205897044`) success; tested head `dee79027a49dfbb1fdd7cf1036bc0ae39e83b518`; 158 passed, 1 xfailed; source identity, compile, traceability, PDF/HTML live canaries passed.
- Final artifact #14384061014; digest `sha256:2b70d0f09f620c83a531f2ec9be9de6a1ec9a669ee861e16704804fe036eb3d3`; expires 2026-11-25 00:13:02 UTC.
- Pre-merge safety ref `safety/pre-merge-cra-guidance-oj-6013-2026-11-18` matched main at `854d66fa6c145ca264dbd768c2c75fcf9f117153`. After merge, main is exactly one commit ahead of that ref and the diff is PR #52's 15 files.
- Post-merge safety ref `safety/post-merge-cra-guidance-oj-6013-2026-11-18` is identical to main at merge commit `d3956b7b364c507b8d59dcfc056763f2829ea867` (post-merge compare: identical).
- Current Guidance source is OJ C/2026/6013, EUR-Lex primary PDF, fallback=False; historical C(2026) 5252 ANFR mirror remains separate and is not claimed byte-identical.
- Next priority: substantive claim-by-claim redline for G-001–G-013 against OJ text, then update relevant interface/requirements/SEC evidence mappings. M/606 provenance review follows.

## CRA Guidance substantive redline complete — 2026-11-18
- OJ C/2026/6013 claim-by-claim review completed for G-001–G-013.
- 9 claims confirmed without substantive change; G-001 locator corrected; G-003/G-008/G-013 wording refined; G-004 expanded to make ongoing conformity/DoC/CE/vulnerability obligations explicit.
- Visual page-image checks completed for OJ pages 7–10, 24–25, 30, 32–35, 42–46, 53 and 61.
- CSV claim register and audit report §8 updated. All claims remain non-binding Commission explanations, not new legal requirements.
- Product-specific scope/classification/conformity remains Unknown; 15 interfaces remain product-unverified; 36 SEC controls remain unimplemented/unverified.
- Next: recheck cross-links from Guidance claims to CRA requirements, IF matrix and SEC matrix; then independently revalidate M/606 C(2026) 7861 and its Annex/ESO adoption and OJ citation status.

## Guidance–matrix 양방향 링크 검증 완료 — 2026-11-18
- 13 Guidance claims ↔ 35 requirements ↔ 15 interfaces ↔ 36 SEC controls를 프로그램으로 양방향 대조: 누락 링크 0, dangling claim ID 0.
- G-002의 IF-001–IF-013 범위 표기를 machine-readable 개별 ID 목록으로 확장.
- G-005 ↔ IF-015 reverse link 추가: remote diagnostics/management의 interface/dependency 변경이 substantial-modification 평가에 관련될 수 있음.
- 요구사항/IF/SEC matrix의 Commission Guidance source URL에 EUR-Lex OJ C/2026/6013 ELI를 primary로 추가하고 기존 Commission page URL은 보조/게시 이력으로 보존.
- 상세 결과: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md` 최신 섹션.
- 다음 최우선: M/606 C(2026) 7861 Annex 원문 provenance, ESO adoption dates, OJ harmonised-standard citation status 독립 검증.

### 교차 매트릭스 검증 자동화 강화 — 2026-11-18
- `cra_traceability.py`에 claim register ↔ requirements/interfaces/SEC 양방향 foreign-key 검증 추가.
- 존재하지 않는 related IDs, matrix의 dangling Guidance claim IDs, reverse link 누락을 CI에서 fail-closed 처리.
- 회귀 테스트 3개 추가: reverse link 누락, dangling matrix claim, unknown related interface ID.
- G-002의 IF range를 명시적 ID로 확장했고 G-005↔IF-015를 양방향 연결.
- 최신 변경은 exact-head CI 통과 후에만 병합한다.

### PR #54 exact-head CI result — Run #865
- Tested head `1d5ae716cc6683365f4da6236d15bb9b32be1e52`; Run #865 / ID `44207426703`: success.
- 161 passed, 1 xfailed; exact source blob identity, compile, CRA traceability (including bidirectional link checks), full pytest, three-PDF live canary, artifact upload and official HTML canary all passed.
- OJ C/2026/6013 primary PDF fallback=False, SHA-256 unchanged.
- Artifact #14383728315; digest `sha256:03b260173f643a68841f54c9f9ac1b3d99c9064762a677ed310160618170f8bb`; expires 2026-11-25 00:23:53 UTC.
- Pre-merge safety ref `safety/pre-merge-cra-guidance-claim-redline-2026-11-18` was identical to main at base `d92f14f6c275bf6b3fa0c8243ac696dca0358d50`.
- Status/project log metadata appended after Run #865; final head needs a fresh exact-head CI before merge.

## PR #54 병합 완료 및 사후 안전 확인 — 2026-11-18
- PR #54 squash merge: `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Exact-head Run #868 (ID `44207582798`) success; tested head `38fa6ef6b6cb08391a227aff7f7a795a98e3f2b4`; 161 passed, 1 xfailed; source integrity, compile, bidirectional traceability, complete pytest, PDF/HTML canaries all passed.
- Artifact #14383788351; digest `sha256:03b260173f643a68841f54c9f9ac1b3d99c9064762a677ed310160618170f8bb`; expires 2026-11-25 00:25:03 UTC.
- Pre-merge safety ref `safety/pre-merge-cra-guidance-claim-redline-2026-11-18` matched main before merge; main is now exactly one PR #54 commit ahead.
- Post-merge safety ref `safety/post-merge-cra-guidance-claim-redline-2026-11-18` is identical to main at `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Guidance claim redline G-001–G-013 and bidirectional link validator are now in main.
- Next priority: M/606 C(2026) 7861 Annex provenance, ESO adoption dates and OJ harmonised-standard citation status.

## PR #56 M/606 Annex + ESO status checkpoint — 2026-11-18
- PR #56 merged to main: `9e42dbd790816b4669793f5bbb9edc4b4686e195`.
- Exact-head Run #879 (ID `44209828986`) on `3e455c63013b895bce977ac1734b0e939827418b`: success; 161 passed, 1 xfailed; source integrity, compile, bidirectional CRA traceability, full pytest, official PDF canary and live official-source canary passed.
- Evidence artifact #14384958566; digest `sha256:84f27e218042e278bbea0157b68f7251f17c2752bda227972c67c890959a8188`; expires 2026-11-25 00:41:24 UTC.
- Pre-merge safety ref `safety/pre-merge-m606-annex-eso-2026-11-18` matched main at base `adc22e3087009db51acff53ec29054f971fa508a`; post-merge safety ref `safety/post-merge-m606-annex-eso-2026-11-18` is identical to main at `9e42dbd790816b4669793f5bbb9edc4b4686e195`.
- M/606 item 18 deadline cell corrected to printed EN 2; row description continues EN 3. All 41 item locators are row-specific.
- June 2026 ESO report is image-based (3 text-layer chars) and intentionally excluded from text-layer CI; no weakened validation threshold.
- Next: independently verify standards-stage changes after the June ESO snapshot and refresh Commission OJ harmonised-standard index before any presumption-of-conformity statement.
 

## 최신 ETSI M/606 작업계획 확인 — 2026-11-18
- 최신 확인 자료: ETSI Work Item Plan, M/606 활성 work items, 2026-11-17 표시 / Work Programme v2.3.3 / 18 items. 상세 원문 대조: [ETSI M/606 live status audit](reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md).
- 서보 드라이브와 잠재적으로 직접 관련되는 EN 304 636(방화벽/IDS/IPS) 및 EN 304 625(물리·가상 네트워크 인터페이스)의 상태/목표 일정을 별도 기록했다. 두 항목의 ETSI OJ Publication 날짜는 목표 일정이지 실제 OJ 게재 증거가 아니다.
- EN 304 636: Comments categorisation assessed (2026-10-06); adoption 목표 2027-02-11, publication 목표 2027-02-19, OJ publication 목표 2027-05-15.
- EN 304 625: 7 VR – EC assessment before EV received (2026-09-28); adoption 목표 2027-03-08, publication 목표 2027-03-15, OJ publication 목표 2027-06-23.
- 제품 자체가 방화벽/IDS/IPS 또는 네트워크 인터페이스 제품인지 intended purpose/core functionality 기준으로 판정한다. 드라이브의 Ethernet/fieldbus 포트 또는 내장 필터링만으로 제품 카테고리를 확정하지 않는다.
- Commission harmonised standards index(2026-11-18 조회)는 OJ 참조 목록을 제공하며 CRA 전용 카테고리는 보이지 않았다. 결론은 “현재 조회 범위에서 CRA OJ 참조를 식별하지 못함”으로 제한한다. Article 27 추정 적합성은 정확한 OJ 참조·범위 확인 후에만 주장한다.
- ETSI 18개 활성 항목은 M/606 41개 전체가 아니다. CEN/CENELEC 작업과 분리 추적한다. 6월 STAN4CR 공동 보고서를 ETSI 개별 item의 최신 자료로 취급하지 않도록 갱신했다.
- 다음: CEN/CENELEC의 수평 표준(EN 40000 계열) 및 산업용 OT 작업(prEN 50770 계열) 최신 공식 진행 상태를 독립 확인하고, OJ index/EUR-Lex를 재조회한다.


## PR #57 관리 문서 병합 확인 — 2026-11-18
- PR #57 docs-only merge commit: `ff3c5b7875131ef92e3fe4a7974f4420ddfcc84c`.
- Post-merge safety ref `safety/post-merge-pr57-2026-11-18`는 merge commit에서 생성되었고 main과 identical(0 ahead/0 behind)로 확인되었다.
- PR #57은 관리 문서만 변경했으며 해당 커밋에 연결된 PR CI run은 확인되지 않았다. 따라서 CI 통과로 표현하지 않는다. 이번 ETSI 연구 변경은 별도 feature branch에서 exact-head CI를 실행한다.


## PR #58 ETSI M/606 상태 갱신 병합 완료 — 2026-11-18
- PR #58 squash merge commit: `88d5eacd71c4267f64f674f0e990a25ed6fafd3a`.
- Exact-head CI Run #883 / ID `44210773892`, tested head `da1b0dce8460b84ddae5d58bd744d382d4b07e7d`: success; **161 passed, 1 xfailed**. Source blob identity, compile, CRA traceability, full pytest, three official CRA PDF fetch/hash checks, evidence upload and nine-source official HTML canary passed.
- Evidence artifact #14385358813; digest `sha256:407da234ac5ad37821bd5d00b7e0872f8abddc28932b1db9f32a14b76aacf1d4`; expires 2026-11-25 00:48:28 UTC.
- Pre-merge safety ref `safety/pre-merge-etsi-m606-status-2026-11-18` matched main at base `ff3c5b7875131ef92e3fe4a7974f4420ddfcc84c`; post-merge ref `safety/post-merge-pr58-2026-11-18` is identical to main at merge commit.
- Latest ETSI Work Programme v2.3.3 (2026-11-17) status and bounded OJ index finding are in `reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md`.
- Next: independently validate CEN/CENELEC EN 40000 horizontal standards and industrial OT prEN 50770 work. Treat third-party catalog status as secondary until official CEN/CENELEC records or published EN texts are obtained.


## CEN/CENELEC 공식 EN 40000 및 OT prEN 50770 점검 — 2026-11-18
- 중요 정정: CEN 공식 프로젝트 레코드에서 **EN 40000-1-1:2026은 Published**로 확인됐다. DOR 2026-11-02, DAV 2026-11-18, DOA 2027-02-28, DOP/DOW 2027-05-31. 같은 레코드의 CRA OJ 필드는 **No citation expected**다. 따라서 “CRA 표준은 아직 발행되지 않았다”는 포괄적 표현을 쓰지 않는다. “CEN 발행은 완료됐으나 CRA OJ 인용은 예상되지 않는다”가 정확하다.
- EN 40000-1-2:2026은 DOR 2026-11-02 / publishing 상태 및 No citation expected가 tracker·2차 카탈로그에서 확인됐다. 공식 개별 CEN 레코드 링크는 HTTP 500으로 본문 readback에 실패했으므로 원문 직접 확인 미완료로 남긴다.
- FprEN 40000-1-3:2026은 CEN 공식 레코드 Under Approval / Citation expected. prEN 40000-1-4는 Work item/drafting.
- CENELEC 공식 레코드에서 prEN 50770-1~6은 모두 Committee stage, OJ citation expected. 각 scope는 OT firewall/IDS-IPS, network management, physical/virtual network interfaces, VPN, routers/modems/switches, SIEM. 아직 DOR/DAV가 없어 발행된 표준이 아니다.
- OJ citation expected는 실제 OJ 인용이 아니다. 2026-11-18 Commission harmonised standards index 확인 범위에서 CRA OJ citation은 식별되지 않았다. Article 27 추정 적합성은 실제 OJ citation과 scope를 확인하기 전 주장하지 않는다.
- 서보 드라이브는 제품 intended purpose/core functionality 기준으로 분류한다. Ethernet/fieldbus 포트 또는 내장 필터링만으로 network-interface/firewall 제품으로 분류하지 않는다. 제품 모델/BOM/데이터시트 미확보로 drive-level classification은 Unknown.
- 상세: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md`; 구조화 추적표: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.csv`.
- 다음: EN 40000-1-1 발행본 및 EN 40000-1-2 원문 확보/검증, 50770-1~6의 최신 committee status 재확인, OJ index 재조회.


## PR #60 CEN/CENELEC 상태 정정 병합 완료 — 2026-11-18
- PR #60 merge commit: `1f39cb31d7f5e3466f1b22b798e9fc51971542da`.
- Exact-head CI Run #887 / ID `44214446339`, tested head `1707d49cdc7d24d5f3de43606e4bc31451e9bf8f`: success; **161 passed, 1 xfailed**. Source blob identity, compile, CRA traceability, full pytest, three official Commission PDF fetch/hash checks, evidence upload and nine-source official HTML canary passed.
- Artifact #14386734709; digest `sha256:aa960c3ecc5e9e89a2f64fc038ccc92cb77a9b7180e58eb5788152752ccd949c`; expires 2026-11-25 01:16:15 UTC.
- Pre-merge safety ref `safety/pre-merge-cen-ot-status-2026-11-18` matched base main; post-merge `safety/post-merge-pr60-2026-11-18` is identical to main at merge commit.
- Corrected key fact: EN 40000-1-1:2026 is CEN Published (DAV 2026-11-18) but CEN says no CRA OJ citation expected. This does not create Article 27 presumption.
- Detailed report/CSV: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md/.csv`.
- Next: obtain/inspect EN 40000-1-1 and 1-2 final texts, retry CEN 1-2 official record, and refresh CENELEC OT project stages/OJ index.



## 최신 작업 — CRA 요구사항–증거 추적 매트릭스 (2026-11-18)
- 작업 브랜치: `cra/requirements-to-evidence-matrix-2026-11-18`; 기준 main: `e461c6246a90f3a6035ba2044da800ba349352f7`.
- 신규 산출물: `reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md` 및 동반 CSV.
- CRA 법적 근거와 제품별 통제·시험·최소 증거를 16개 EVD 항목으로 연결했다. 범위는 제품 경계, 위험평가, 자산/공격면, 보안 설계, 접근통제, 통신, 입력 무결성, 업데이트, SBOM, 취약점 처리, 공개, 지원기간, 기술문서, 신고, 공급망/변경관리다.
- EN 40000-1-2는 공개 scope만 사용하고 final text/clause 확인 전 normative clause mapping을 하지 않았다. EN 40000-1-3은 Under Approval scope만 참고한다. EN 40000-1-1 Published는 용어 정합성에만 활용한다.
- 제품별 모델/설계/시험 자료가 없으므로 16개 행은 모두 Unknown / evidence pending. 이 표는 적합성 판정 또는 법률 의견이 아니다.
- 다음: CSV/보고서 정합성 검증 및 기존 CRA traceability validator/CI 범위 확인 후 exact-head CI, PR, merge 안전절차 수행.

### PR #62 1차 exact-head CI 결과 — metadata 반영 후 재검증 필요
- PR #62 head `360e83bba86a01bc83731ecd5ea5d0a6b975a8f6`, Run #891 / ID `44217500114`: success.
- pytest **161 passed, 1 xfailed**; source blob integrity, compile, CRA cross-matrix traceability, official CRA PDF 3종 fetch/hash, 9-source live official HTML canary 모두 성공.
- Artifact #14388303196; digest `sha256:47528b6e72af65dd95130a86a1442ac8f795a6eb3c34d93656369bf94734a2c2`; expiry 2026-11-25 01:40:17 UTC.
- 이 CI 결과를 상황판/세션 로그/프로젝트 로그에 추가했으므로 해당 metadata 변경이 포함된 새 PR head에서 exact-head CI를 다시 실행한 뒤 병합한다.


## PR #62 병합 및 복구 검증 완료 — 2026-11-18
- PR #62: https://github.com/useformotor3/ai-discord-bot/pull/62 — squash merged.
- Merge commit / 현재 main 기준: `612285ed720310cebd82340dc2e3b150e2c6f80a`.
- 최종 exact-head `3947e25ba1717caea3e4099404da800ba349352f7`의 Run #896 / ID `44217724257`: success; **161 passed, 1 xfailed**.
- 검증: source blob identity, compile, CRA cross-matrix traceability(13 claims/15 interfaces/35 requirements/36 SEC/41 M/606 items), full pytest, Commission 공식 PDF 3종 fetch/hash, 9-source official HTML canary.
- Artifact #14389685192; digest `sha256:e11bcbf277f32b7386e72fb063fdfac2b19e896473e30c8e775522b7f6c55d85`; expiry 2026-11-25 01:41:53 UTC.
- Pre-merge safety ref: `safety/pre-cra-evidence-matrix-2026-11-18`; post-merge safety ref: `safety/post-merge-pr62-2026-11-18`. Post-merge ref와 main은 0 ahead / 0 behind, identical 확인.
- 신규 EVD-01–EVD-16 보고서/CSV 및 통합 보고서·README·상황판·마스터 계획·세션 로그·JSONL 기록이 main에 반영됨.
- 운영 코드/workflow, secrets, state/history/archive, Gemini/Discord 실행 및 SIL 3 자료는 변경하지 않았다.
- 다음: 제품 P0 자료(정확한 모델 데이터시트·사용설명서·통신/원격접속 구조) 확보 후 EVD-01부터 모델별 evidence mapping. 표준 최종 전문 취득 시 clause-by-clause 검증.


## 신규 규제 일정 변경 — Commission C(2026) 7861 final (2026-11-18)
- Commission CRA 표준화 공식 페이지는 2026-11-10 M/606 개정을 확인한다(페이지 최종 업데이트 2026-11-12).
- 새 Annex I ESO adoption deadline: item 1 framework/risk-based design (EN 40000-1-2 work) **2026-11-30**; item 15 vulnerability handling (EN 40000-1-3 work) **2026-11-30**; items 2–14 generic security requirements **2027-10-30**; items 16–41 vertical product standards **2027-01-31**.
- 날짜는 ESO adoption deadline이지 발행일/OJ citation/CRA 적용일이 아니다. OJ citation 전 Article 27 presumption을 주장하지 않는다.
- 결정 Article 2는 ESO가 수령 후 1개월 이내 개정 비수락을 통지하면 결정이 중단되는 조건을 둔다. ESO 수령일/비수락 여부는 미확인 후속 항목이다.
- 상세 보고서: `reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md`. CEN/OT 상태 보고서에도 일정 정정 추가.
- 기존 자료의 2026-10-30 수평/수직 deadline 설명은 개정 결정으로 superseded. 이전 역사 기록은 삭제하지 않고 정정 링크를 추가한다.


### PR #64 exact-head CI 검증
- PR #64 head `ff548d64b109e95c9f63fa0666ba419f9545e11f`, Run #900 / ID `44219718958`: success.
- pytest **161 passed, 1 xfailed**; source blob integrity, compile, CRA cross-matrix traceability, official CRA PDF source canary 9종, artifact upload, official HTML source canary 모두 통과.
- CRA traceability: 13 claims, 15 interfaces, 35 requirements, 36 SEC, 41 M/606 items; bidirectional links true.
- Artifact #14390620457; digest `sha256:b7ced7629ab9e88bf44190d6d4f5fd50fc91f45bfc33a83ae09a02c1833e2f20`; expires 2026-11-25 01:58:08 UTC.
- CI metadata를 이 문서에 기록했으므로 변경된 최종 head에서 exact-head CI를 재실행한 후 병합한다.


## PR #64 병합 및 사후 안전 검증 — 2026-11-18
- PR #64 `docs: update CRA M606 deadlines from C(2026) 7861` squash merge 완료: `41229486baded6336aa43cd3b5de375476fe92f3`.
- 최종 exact-head `ae896286ee63916679afa4c6cc44655f1c125a4f`, Run #905 / ID `44219914781`: success; **161 passed, 1 xfailed**.
- Source blob identity, compile, CRA cross-matrix traceability, 공식 CRA PDF/HTML read-only canary 통과. Traceability: 13 claims / 15 interfaces / 35 requirements / 36 SEC / 41 M/606 items, bidirectional links true.
- 공식 PDF canary에서 C(2026)7861 Annex 사본: 6 pages, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276` 확인.
- Artifact #14388899741, SHA-256 `ecd0f1181457270eb5d3d9fd5e60c2271aafc730ac1250a025499aa614f5cb8b`, expires 2026-11-25 02:00:03 UTC.
- Pre-merge safety ref `safety/pre-m606-amendment-2026-11-18`; post-merge `safety/post-merge-pr64-2026-11-18`와 main identical (0 ahead / 0 behind).
- 다음: Article 2 비수락 조건의 ESO receipt/notice 확인은 계속 열어둔다. 제품 모델별 P0 evidence intake checklist 및 CRA applicability/classification decision matrix 작성.

## CRA 제품 적용성·분류 및 P0 intake 기준 초안
- `reports/CRA_SERVO_DRIVE_APPLICABILITY_CLASSIFICATION_AND_P0_INTAKE_2026-11-18.md` 추가.
- CRA Article 2 적용성, Article 3 제품/원격 데이터 처리 정의, Annex III/IV 및 Implementing Regulation (EU) 2025/2392 core functionality 기준을 분리해 정리.
- 포트/통신 기능만으로 Annex III Class I/II 또는 Annex IV 분류를 자동 결론내리지 않도록 경계 판단표를 포함.
- 모델별 증거 미제공이므로 CRA 적용성/분류/EVD-01~16은 Unknown 유지. 데이터시트·매뉴얼·블록도·통신/원격접속 구성도 등을 P0 intake로 정의.
- 다음: 문서·CSV·요구사항 추적성 CI 검증 및 PR merge. Article 2 M/606 ESO 비수락 조건은 별도 열린 조사 항목.


## PR #65/#66 병합 및 제품 분류 법령 재대조 — 2026-11-18
- PR #65 병합 커밋 `d1f96fa6bba297e31ed47ae1b96f59421c55b774`; exact-head Run #908 / ID `44221151662`: 161 passed, 1 xfailed; CRA traceability 13/15/35/36/41, bidirectional links true; JSONL event log 133 events. Artifact #14391145990, digest `sha256:f2a2f83b19d0488c874a032e83a41fcc4140dde1817d2a9c2fc171fdbd0b6c0f`, expires 2026-11-25 02:09:41 UTC. Post-merge safety `safety/post-merge-pr65-2026-11-18` identical to main.
- PR #66 병합 커밋 `9cb62579e4f45ebf57587cc19644c370cbe80ebb`; exact-head Run #910 / ID `44221522135`: 161 passed, 1 xfailed; source integrity, compile, CRA traceability 13 claims/15 interfaces/35 requirements/36 SEC/41 M606 items, bidirectional links true, PDF/HTML canaries passed. Artifact #14391145990, digest `sha256:f2a2f83b19d0488c874a032e83a41fcc4140dde1817d2a9c2fc171fdbd0b6c0f`, expires 2026-11-25 02:09:41 UTC. Post-merge safety `safety/post-merge-pr66-2026-11-18` identical to main.
- EUR-Lex 2025/2392 공식 OJ 본문 재대조: recital (2)–(6), Annex I의 #10 interface/#11 OS/#12 router-switch 기술 설명 및 Article 8(1) critical product 인증 절차를 보고서에 보완. Annex IV 카테고리 해당과 인증 의무 자동 발생을 구분.
- 다음: M/606 Article 2의 ESO 수령일/비수락 사실은 공개 확인 자료를 계속 찾되 미확인 상태 유지. P0 모델 자료가 오면 제품 경계·intended purpose·연결성·core functionality부터 검증.


## PR #67 병합 및 exact-head 검증 — 2026-11-18
- PR #67 `docs: record PR65 PR66 and CRA legal recheck` squash merge: `86af2db5fadf5098b22b39d2d6c07710ed0033ee`.
- Exact-head `58e2dc8608fc097dad87fa3ec614cb108d184fad`, CI Run #912 / ID `44223114411`: success. Source blob identity, compile, CRA cross-matrix traceability, 전체 pytest, 공식 CRA PDF/HTML read-only canaries 및 artifact upload 단계 모두 성공.
- Artifact #14391457563, digest `sha256:f172ed1762a693f626e8c5781638c557e9d5471d6750b5315a54cae9398d919c`, expires 2026-11-25 02:25:41 UTC.
- Post-merge safety ref `safety/post-merge-pr67-2026-11-18`와 main identical (0 ahead/0 behind).
- 다음: C(2026)7861 Article 2 ESO receipt/non-acceptance 공개 증거 확인 계속. 현 시점 receipt/notice 원문 확인 불가이므로 acceptance를 추정하지 않는다.


## M/606 수락 상태 추가 검증 — 2026-11-18
- CEN-CENELEC 공식 발표(2025-05-01)는 원래 M/606이 2025-04-03 CEN, CENELEC, ETSI에 의해 수락되었음을 명시. Commission Interoperable Europe 2026 rolling plan도 세 ESO가 요청을 수락했고 작업 중이라고 재확인.
- 단, 원래 요청 수락은 2026-11-10 개정 결정 C(2026)7861 Article 2의 개정 통지/수령 및 1개월 비수락 조건 충족을 증명하지 않는다. 개정 결정의 개별 수령일·비수락 통지는 미확인으로 유지.
- M/606 보고서에 원래 요청과 개정 결정의 수락 상태를 분리 기록. 공개 증거 없는 개정 수락을 추정하지 않는다.
