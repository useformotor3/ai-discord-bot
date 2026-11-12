# CRA 서보 드라이브 개발 프로젝트 — 상황판

> 저장소: useformotor3/ai-discord-bot  
> 작업 브랜치: cra-project-foundation  
> 마지막 확인일: 2026-11-12

## 목적/범위
CRA를 모르는 개발자가 서보 드라이브 개발에 적용할 수 있는 공개 근거 기반 실무 지침과 통합 보고서 구축. CRA 전용이며 SIL 3 벤치마킹 제외. ST MCU 우선, TI 비교. Public 저장소에는 공개 자료만 저장.

## 실제 저장소 상태
- main과 작업 브랜치는 Git commit graph 기준 diverged 상태. archive 콘텐츠는 동기화했지만 commit graph를 병합한 것은 아니다.
- 작업 브랜치 마지막 확인 시 archive 990, history 990, 경로 중복/누락/orphan 0.
- main 마지막 확인 시 archive 990, history 990, 경로 중복/누락 0.
- main에서 확인된 6개 추가 자동 생성물을 원문 그대로 작업 브랜치에 보존.
- main state.json: date=2026-11-12, count=3 (일일 카운터).
- 6개 자동 생성 보고서 표본에서 CRA 조항/직접 인용/제품 분류 오류 발견. [ARCHIVE_TRIAGE_MAIN_ONLY_6.md](ARCHIVE_TRIAGE_MAIN_ONLY_6.md)
- 브랜치 및 파일 정합성: [REPOSITORY_RECONCILIATION.md](REPOSITORY_RECONCILIATION.md)

## 운영 규칙
- 신규 세션은 START_HERE, AI_RULEBOOK, 상황판, 계획, 지식 인덱스, 보고서, 최근 세션 로그를 먼저 읽는다.
- 과거 기억/AI 답변보다 최신 GitHub 상태와 공식 근거 우선.
- 이전 AI 산출물도 검증 전 사실로 취급하지 않는다.
- 성공·실패·오류·재발 방지 기록.
- 문서·폴더 구조·스키마·자동화 코드 모두 개선 가능.
- 미검증 주장을 확정 보고서로 승격하지 않는다.

## 자동화 위험
- main.py의 모든 모델 실패 후 경고 문구를 정상 성공으로 저장하는 위험.
- 출처 URL/원문 위치/문서 버전 자동 검증 부재.
- 프로젝트 운영 문서를 prompt에 로드하지 않고 최근 history snippet 5개만 사용.
- Discord timeout/HTTP status 확인 부재.
- MAX_DAILY_QUOTA=1200은 공식 무료 한도 근거가 없는 임의 상수.
- 기존 research workflow에는 cron 예약 실행 없음.

## 추가한 정합성 검사
- scripts/audit_archive.py: archive/history 경로, 중복, orphan, malformed history 검사. state.count는 일일 카운터로만 표시.
- tests/test_audit_archive.py: 정상/누락/고아/중복/잘못된 이력 항목 테스트 3개.
- .github/workflows/archive-audit.yml: 작업 브랜치 push 및 수동 실행 시 테스트와 strict audit 수행.
- 로컬 unittest: 3개 테스트 통과. GitHub Actions 최근 4회 실행의 audit job 및 단위 테스트/strict 검사 단계 모두 success 확인. [실행 이력](https://github.com/useformotor3/ai-discord-bot/actions/workflows/archive-audit.yml?query=branch%3Acra-project-foundation)

## 별도 인벤토리 파이프라인
- scripts/build_archive_inventory.py: 990개 archive에서 파일 SHA-256, 크기, 제목/헤딩, URL 후보, CRA 조항/Annex 후보, 주제 키워드 후보, history 메타데이터 추출.
- 모든 레코드는 UNVERIFIED_AI_ARCHIVE로 표시. 키워드 분류/URL 추출은 후보일 뿐 법령·링크·인용 정확성 검증이 아님.
- tests/test_build_archive_inventory.py: 메타데이터 추출/미분류/중복 이력 테스트.
- .github/workflows/archive-inventory.yml: 수동 실행 및 archive 변경 시 인벤토리 JSON을 30일 Artifact로 업로드. 최초 실행 상태 확인 중.

## 인벤토리 실행 결과
- 990개 파일, 990개 history 항목을 스캔.
- 주제 키워드 후보: SBOM/공급망 779, 취약점 처리 753, 보안 업데이트 723, 지원기간 406, 제품 분류 338, 사고 신고 259, 기술문서 253, 인증/암호 121, Secure Boot 97, 위협모델 97, 표준/시험 23, 미분류 10.
- 다중 라벨이며 단순 키워드 후보. 합계는 문서 수가 아니고 사실 검증 결과가 아님.
- 상세: [ARCHIVE_INVENTORY_2026-11-12.md](ARCHIVE_INVENTORY_2026-11-12.md)

## 메인 코드 변경 제안
- [CHANGE_PROPOSAL_MAIN_GEMINI.md](CHANGE_PROPOSAL_MAIN_GEMINI.md)에 main.py/Gemini prompt 개선안 작성.
- 사용자 승인 전 main.py, Gemini prompt, 운영 research workflow는 수정하지 않음.

## 다음 작업
- [ ] 인벤토리 990개 원문에서 출처·조항·인용 후보를 별도 검증대장으로 정리
- [ ] main.py 실패 처리·근거 스키마·검증 게이트 변경 제안서 작성 (사용자 승인 전 수정 금지)
- [ ] 기존 990개 자료 전체 주제 분류 및 주장/출처 인벤토리
- [ ] CRA 공식 근거 전수 검증
- [ ] 서보 드라이브 적용성 분석
- [ ] ST MCU 정확한 부품 번호 확보 후 기능 검증
- [ ] TI 비교 및 통합 보고서 작성
- [ ] 브랜치 PR/병합 전 diff 및 충돌 검토

## 상태
VERIFIED / PARTIALLY_VERIFIED / UNVERIFIED / CONFLICT / OUTDATED / NOT_APPLICABLE

마지막 갱신: 2026-11-12
