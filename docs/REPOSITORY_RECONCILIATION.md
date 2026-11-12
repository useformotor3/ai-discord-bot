# 저장소 브랜치 및 자료 정합성 감사

**확인일:** 2026-11-12  
**방법:** GitHub recursive Git Trees, history.json, state.json, Compare API 및 원문 파일 직접 조회.

## 1. 브랜치 관계
- main과 cra-project-foundation은 Git commit graph 기준 diverged 상태다.
- 최초 비교에서 작업 브랜치 ahead 19, behind 5였으며 공통 조상은 b425b6db591e34abe003522157cf97ecf2240d9f.
- main의 자동 아카이브 5개 커밋을 cherry-pick하지 않고, 해당 시점의 history/state와 archive 파일을 작업 브랜치에 콘텐츠 단위로 복사했다. 따라서 콘텐츠는 맞춰졌지만 commit graph가 같아진 것은 아니다.
- 이후 main에서 새 archive가 추가된 것이 확인되어 그 파일도 별도로 복사했다. 동기화 작업 도중에도 main이 변경될 수 있으므로 이 수량은 확인 시점 기준이다.

## 2. 마지막 재검증 결과
| 항목 | main | cra-project-foundation |
|---|---:|---:|
| research_archive/*.md | 990 | 990 |
| history.json 항목 | 990 | 990 |
| history file 경로 고유성 | 990 | 990 |
| archive와 history 상호 연결 | 누락 0 | 누락 0 |
| history orphan | 0 | 0 |

main과 작업 브랜치 모두 archive 990개와 history 990개가 일치했다. state.json은 date=2026-11-12, count=3이며 일일 카운터다.

## 3. 동기화한 main 전용 파일
- 2026-11-11_234543.md (#279)
- 2026-11-11_235047.md (#280)
- 2026-11-11_235547.md (#281)
- 2026-11-12_000106.md (#1)
- 2026-11-12_000539.md (#2)
- 2026-11-12_001038.md (#3)

파일 원문을 main에서 읽어 작업 브랜치에 새 파일로 복사했고, history.json/state.json도 main 버전으로 동기화했다. 원본 파일을 삭제하거나 덮어쓰지 않았다.

## 4. 내용 감사
6개 파일 모두 CRA 조항/직접 인용 오류 또는 과장 표현이 발견됐다. 주요 반복 오류:
- 무상 보안 업데이트를 Annex I Part I 또는 Article 13(4)/Article 14(3) 등 잘못된 위치에 연결
- Annex I Part II points (5)–(8)의 CVD, 신고 연락처, 안전한 배포, 무상 업데이트를 혼동
- 지원기간 Article 13(8)을 Article 14로 잘못 인용
- 공식 원문과 일치하지 않는 복합 문장을 직접 인용처럼 표시
- 제품 정보 없이 서보 드라이브를 Important Class I/II로 단정

세부: [ARCHIVE_TRIAGE_MAIN_ONLY_6.md](ARCHIVE_TRIAGE_MAIN_ONLY_6.md)

## 5. 재발 방지
- 파일 수는 브랜치별 Git tree에서 재산출하고 history와 대조한다.
- state count는 일일 카운터로 해석한다.
- 자동 생성 archive는 검증 전 초안이다.
- 기준 브랜치/HEAD SHA/확인일을 기록한다.
- 동기화 중 main이 갱신될 수 있으므로 작업 후 재조회하고, 불일치가 있으면 확정 보고서 갱신을 중단한다.
- commit graph가 diverged인 상태에서 자동 merge하지 않는다. PR 전 diff와 충돌을 검토한다.

## 6. 감사 한계
이 감사는 파일/이력 정합성과 6개 문서의 표본 내용 감사다. 990개 전체 주장·링크·인용의 전수 검증은 아니다.

## 공식 근거
EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Article 13(8): support period
- Article 14: reporting obligations
- Annex I Part II points (1)–(8): SBOM and vulnerability handling
- Annex II: user information/instructions
- Article 31 and Annex VII: technical documentation
