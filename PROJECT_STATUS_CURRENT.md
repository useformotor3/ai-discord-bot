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
