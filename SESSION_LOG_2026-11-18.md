# 세션 로그 — 2026-11-18

## CRA 재개 및 PR #42 통합

- 최신 프로젝트 상태를 기준으로 CRA 작업을 재개했다. SIL 3는 과거 자료로 보존하며 활성 범위에서 제외한다.
- PR #42 `docs: clarify CRA legal locator and SBOM requirements`의 exact head `0ff686be74fb5c6309b46ed9c01473251d997579`에 연결된 GitHub Actions Run #824 (ID `44061121932`) 성공을 확인했다.
- 전체 테스트: 155 passed / 1 xfailed. Source integrity, compile, CRA cross-matrix traceability, live official source canary, Commission PDF source canary 및 artifact upload가 통과했다.
- Guidance PDF는 ANFR mirror fallback=True로 취득했다. Commission primary PDF bytes와의 동일성은 확인되지 않았음을 유지했다.
- PR 리뷰 스레드 및 제출 리뷰가 없는 것을 확인한 뒤 exact head SHA guard로 squash merge했다.
- Merge commit: `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`.
- Pre-merge ref `safety/pre-merge-main-pr42-2026-11-18` 및 post-merge ref `safety/post-merge-main-pr42-2026-11-18` 생성. post-merge ref와 main compare는 identical (0 ahead/0 behind).
- PR #42는 CRA-001–CRA-035 법령 locator의 1차 인벤토리 검토 및 SBOM 의무 체계(Annex I Part II(1), Annex VII(2)(b)/(8), Annex II(9))를 명확히 했다.
- 새 현재 상태 스냅샷 `PROJECT_STATUS_CURRENT.md`를 추가해 최신 main/PR/CI/복구 ref/미완료 사항을 한곳에 기록한다.
- 다음 작업은 35개 요구사항의 법령 문언·의무 주체·조건·예외·기한을 행 단위로 심층 검토하고 관련 보고서/매트릭스를 함께 정합화하는 것이다.


## CRA 법령 문언 심층 감사 Batch 1
- EUR-Lex 공식 Regulation (EU) 2024/2847 원문을 기준으로 CRA-001–CRA-010을 행별 대조했다.
- 신규 상세 감사: `reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md`.
- 추적표 locator 수정: CRA-001(Article 3(8)–(10), Recital 9 보강), CRA-003(Article 13(2) 제거, Article 3(2)/Recital 11–12로 정정), CRA-006(Annex I Part II(1), Article 13(7), Annex VII(2)(b)/(8) 분리 및 Article 13(5) due diligence 구분).
- CRA-008의 regular testing은 고정 법정 주기 숫자 미규정, CRA-009의 공개 지연 예외를 감사 문서와 통합 보고서에 기록했다.
- 추적표·통합 보고서·독립 감사·상황판/세션 로그를 같은 작업 브랜치에서 정합화했다. exact-head CI 통과 전 병합하지 않는다.
- 다음 대상은 CRA-011–CRA-020.


## CRA 법령 문언 심층 감사 Batch 2
- EUR-Lex 공식 Regulation (EU) 2024/2847 원문으로 CRA-011–CRA-020을 행별 대조했다.
- 신규 상세 감사: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md`.
- 요구사항 CSV에 연락창구의 비자동화 연락 수단 선택, 보안 업데이트의 무상 제공 예외, support period의 5년 미만 조건, 기술문서 작성/갱신과 보관 분리, Annex V/VI DoC, Article 32 평가경로 차이를 반영했다.
- CRA-020의 중요 해석: Annex III/IV core functionality 기준, 통합만으로 host product 분류 전이 금지, Class I/II/Critical 평가경로 분리.
- 통합 보고서·독립 감사·상황판을 같은 브랜치에서 동기화한다. exact-head CI 성공 전 병합 금지.
- 다음 대상: CRA-021–CRA-035.
