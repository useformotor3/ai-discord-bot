# 저장소 브랜치 및 자료 정합성 감사

**확인일:** 2026-11-12  
**대상 저장소:** useformotor3/ai-discord-bot  
**확인 방법:** GitHub Git Trees API의 recursive tree와 history.json을 직접 조회  
**범위:** 파일 경로/개수/이력 정합성. 개별 문서의 내용 정확성 감사와는 별개.

## 1. 확인 결과

| 항목 | main | cra-project-foundation |
|---|---:|---:|
| research_archive/*.md | 989 | 984 |
| history.json 항목 | 별도 미확인 | 984 |
| tree 기준 | main ref | 브랜치 HEAD |
| 확인된 archive/history 관계 | 아래 참고 | history file 경로 984개 모두 존재 |

cra-project-foundation 브랜치의 history.json은 984개 항목이며, file 경로 984개가 모두 유일하고 브랜치의 archive 파일과 일치한다. 누락 0, 중복 0이다.

main에는 브랜치에는 없는 archive Markdown 5개가 추가로 존재한다.
- research_archive/2026-11-11_234543.md
- research_archive/2026-11-11_235047.md
- research_archive/2026-11-11_235547.md
- research_archive/2026-11-12_000106.md
- research_archive/2026-11-12_000539.md

이 5개 파일은 main의 tree에는 있으나 cra-project-foundation에는 없다. 브랜치의 history.json에는 이 5개가 등록되어 있지 않다. 따라서 이전 문서에 기록된 985개는 현재 조회 결과와 일치하지 않는 오래된 수치다.

## 2. 해석과 주의
- 브랜치의 984개는 archive와 history가 서로 일치한다.
- main의 989개는 archive 파일 기준 개수이며, 현재 확인된 branch history 984개와 단순 비교할 수 없다.
- main의 history.json 및 state.json을 같은 시점의 tree에서 별도 조회해 비교하기 전에는 main의 history 정합성을 단정하지 않는다.
- 5개 차이가 단순히 브랜치 생성 이후 main에 추가된 것인지, 의도치 않은 누락/변경인지 commit graph와 각 파일의 생성 커밋을 조사해야 한다.
- 파일 개수는 보고서 생성 건수, 조사 횟수, API 호출 수와 동일한 개념이 아니다.

## 3. 권고 조치
1. 두 브랜치의 공통 조상 및 이후 커밋을 비교한다.
2. 5개 추가 파일의 내용·근거·history 등록 여부를 확인한다.
3. 원본을 삭제하거나 덮어쓰지 않고, 필요 시 브랜치에 명시적으로 이관한다.
4. 인벤토리 생성 스크립트를 만들어 archive 파일 수, history 항목 수, 중복/누락/고아 파일을 자동 계산한다.
5. 결과에 기준 브랜치, commit SHA, 확인 시각을 저장한다.

## 4. 재발 방지
파일 수, 상태, 완료 여부는 기존 문서 숫자를 재사용하지 말고 Git tree/API에서 재산출한다. 브랜치별 기준을 섞지 않는다. 인벤토리와 history가 일치하지 않으면 최종 보고서 갱신을 중단하고 CONFLICT로 기록한다.

## 5. 검증 한계
이 감사는 파일 목록과 history 경로의 정합성만 확인했다. 984개 또는 989개 문서의 주장·인용·출처가 정확하다는 의미가 아니며, main의 history.json 정합성도 아직 검증하지 않았다.
