# 저장소 브랜치 및 자료 정합성 감사

**확인일:** 2026-11-12  
**저장소:** useformotor3/ai-discord-bot  
**방법:** GitHub recursive Git Trees, history.json, state.json, Compare API 및 원문 파일 직접 조회  
**범위:** 브랜치/커밋/파일 수/이력 정합성. 문서 내용의 CRA 정확성은 별도 감사.

## 1. 현재 브랜치 관계
- 비교 기준: main...cra-project-foundation
- 상태: diverged
- 작업 브랜치만 앞선 커밋: 19
- main만 앞선 커밋: 5
- 공통 조상: b425b6db591e34abe003522157cf97ecf2240d9f
- 작업 브랜치 HEAD 확인값: d5e391b3ccb5105afb2f5d5fbdcafcbd67a40564
- main은 작업 브랜치가 아직 포함하지 않은 5개 자동 아카이브 커밋을 보유한다.

## 2. 아카이브 및 이력 수량
| 항목 | main | cra-project-foundation |
|---|---:|---:|
| research_archive/*.md | 989 | 984 |
| history.json 항목 | 989 | 984 |
| history 경로 고유성 | 989개 모두 고유 | 984개 모두 고유 |
| history 경로가 archive에 존재 | 989/989 | 984/984 |
| archive지만 history에 없는 파일 | 0 | 0 |

과거 문서의 985개는 오래된 수치다. 현재 확인값은 main 989개, 작업 브랜치 984개다.

## 3. main에만 있는 5개 자동 아카이브
아래 파일은 main의 history.json에도 등록되어 있다.
- research_archive/2026-11-11_234543.md — Count #279
- research_archive/2026-11-11_235047.md — Count #280
- research_archive/2026-11-11_235547.md — Count #281
- research_archive/2026-11-12_000106.md — Count #1
- research_archive/2026-11-12_000539.md — Count #2

main state.json은 date=2026-11-12, count=2다. count는 날짜 변경 시 초기화되는 일일 카운터이며 누적 파일 수가 아니다.

## 4. 5개 문서 표본 검토
- #279: 무상 업데이트/안전 배포를 Annex I Part I point 2로 연결하고 직접 인용문으로 표시한 문장이 공식 원문과 일치하지 않는다. 무상 제공은 Annex I Part II point (8), 안전 배포는 point (7).
- #280: SBOM은 Annex I Part II point (1)이 맞지만 기술문서를 Annex II로 표시한 부분은 부정확하다. 기술문서는 Article 31 및 Annex VII를 확인해야 한다.
- #281: 지원기간 근거는 Article 14(3)이 아니라 Article 13(8). 일반 원칙은 최소 5년이며 예상 사용기간이 5년보다 짧으면 그 기간에 맞춘다.
- #1: 무상 업데이트를 Article 13(4) 및 Annex I Part I로 연결한 부분이 부정확하다. Annex I Part II point (8)과 Article 13(8)의 역할을 구분해야 한다.
- #2: CVD 정책은 Annex I Part II point (5), 취약점 신고 연락처는 point (6), 무상 보안 업데이트는 point (8). 복합 직접 인용문은 원문 대조 전 재사용 금지.

상세 판정: [ARCHIVE_TRIAGE_MAIN_ONLY_5.md](ARCHIVE_TRIAGE_MAIN_ONLY_5.md)

## 5. 브랜치 통합 방침
두 브랜치는 diverged 상태다. 자동 merge/rebase/cherry-pick은 하지 않는다.
1. main 전용 5개 파일과 state/history 변경을 검토한다.
2. 원본을 보존하고 검증 상태를 분리한다.
3. 필요하면 정정/검증 인덱스를 별도 추가한다.
4. main 병합은 diff·충돌 검토 후 PR로 제안한다. 사용자 승인 전 main에 직접 병합하지 않는다.

## 6. 재발 방지
- 수량은 브랜치별 Git tree에서 재산출하고 history와 대조한다.
- state.json count는 일일 카운터로만 해석한다.
- 자동 생성 archive는 검증 전 초안이다.
- 기준 브랜치, HEAD SHA, 확인일을 인벤토리에 기록한다.

## 7. 감사 한계
파일 경로/이력 정합성 및 5개 파일 표본 내용 감사다. 989개 전체 주장·링크·인용 전수 검증은 아니다.

## 공식 근거
EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 13(8): 지원기간
- Article 14: 신고 의무
- Annex I Part II (1)–(8): SBOM 및 취약점 처리
- Annex II: 사용자 정보 및 지침
- Article 31 및 Annex VII: 기술문서
