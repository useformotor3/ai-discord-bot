# CRA 서보 드라이브 개발 프로젝트 — 상황판

> 저장소: useformotor3/ai-discord-bot  
> 작업 브랜치: cra-project-foundation  
> 마지막 원본 대조: 2026-11-12

## 목적/범위
CRA를 모르는 개발자가 서보 드라이브 개발에 적용할 수 있는 공개 근거 기반 실무 지침과 통합 보고서 구축. CRA 전용이며 SIL 3 벤치마킹 제외. ST MCU 우선, TI 비교. Public 저장소에는 공개 자료만 저장.

## 실제 저장소 상태
- main과 작업 브랜치는 diverged. 작업 브랜치는 main의 자동 아카이브 커밋 5개 이후 추가된 기록을 별도 콘텐츠 복사로 보존했으며, Git commit graph는 여전히 diverged 상태다.
- main: archive 990, history 990. 경로 중복/누락 없음.
- cra-project-foundation: archive 990, history 990. 경로 중복/누락 없음.
- 작업 브랜치의 5개 main 전용 파일뿐 아니라 이후 확인된 2026-11-12_001038.md도 원문 그대로 복사했다.
- main/작업 브랜치 state.json: date=2026-11-12, count=3 (일일 카운터).
- 6개 main 생성물의 표본 검토에서 조항/직접 인용/제품 분류 오류가 반복됨. [ARCHIVE_TRIAGE_MAIN_ONLY_6.md](ARCHIVE_TRIAGE_MAIN_ONLY_6.md)
- 브랜치 관계와 파일 정합성: [REPOSITORY_RECONCILIATION.md](REPOSITORY_RECONCILIATION.md)

## 운영 규칙
- 신규 세션은 START_HERE, AI_RULEBOOK, 상황판, 계획, 지식 인덱스, 보고서, 최근 세션 로그를 먼저 읽는다.
- 과거 기억/AI 답변보다 최신 GitHub 상태와 공식 근거 우선.
- 이전 AI 산출물도 검증 전 사실로 취급하지 않는다.
- 성공·실패·오류·재발 방지 기록.
- 문서·폴더 구조·스키마·자동화 코드 모두 개선 가능.
- 미검증 주장을 확정 보고서로 승격하지 않는다.

## 자동화 위험
- 모든 모델 실패 후 경고 문구를 정상 성공으로 저장할 수 있음.
- 출처 URL/원문 위치/문서 버전 자동 검증 없음.
- 프로젝트 운영 문서를 prompt에 로드하지 않고 최근 history snippet 5개만 사용.
- Discord timeout/HTTP status 확인 없음.
- MAX_DAILY_QUOTA=1200은 공식 무료 한도 근거가 없는 임의 상수.
- run.yml cron 미구현.

## 다음 작업
- [ ] inventory 검사 스크립트 및 테스트 작성
- [ ] main.py 실패 처리·근거 스키마·검증 게이트 설계
- [ ] 기존 990개 자료 전체 주제 분류 및 주장/출처 인벤토리
- [ ] CRA 공식 근거 전수 검증
- [ ] 서보 드라이브 적용성 분석
- [ ] ST MCU 정확한 부품 번호 확보 후 기능 검증
- [ ] TI 비교 및 통합 보고서 작성
- [ ] 브랜치 PR/병합 전 diff 및 충돌 검토

## 상태
VERIFIED / PARTIALLY_VERIFIED / UNVERIFIED / CONFLICT / OUTDATED / NOT_APPLICABLE

마지막 갱신: 2026-11-12
