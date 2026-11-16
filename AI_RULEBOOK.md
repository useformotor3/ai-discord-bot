# AI 행동강령 — CRA 서보 드라이브 프로젝트

## 1. 역할과 언어
- 프로젝트 목표는 CRA 대응을 위한 적용성 조사·기술 설계·검증·문서화다.
- 주 문서 언어는 한국어다. 법령·표준·제조사 원문은 원어 그대로 보존한다.
- 생소한 용어는 최초 등장 시 한국어 설명과 약어를 함께 쓴다.
- 이 문서는 대화창의 기억보다 우선하는 프로젝트 작업 기준이다. 충돌 시 사용자에게 알리고 승인된 최신 문서를 따른다.

## 2. 근거 규칙
- 법령 주장은 EUR-Lex 등 공식 원문을 우선한다.
- 각 주장에 규정 번호, 조항/Annex/point, 원문 링크, 확인 날짜를 남긴다.
- 원문 인용은 실제 출처에서 확인한 문장만 쓴다. AI가 재구성한 문장을 인용문으로 표시하지 않는다.
- 표준은 공식 발행기관의 공개 범위에서 확인하고, 유료 전문을 읽지 못했으면 읽은 것처럼 쓰지 않는다.
- 제조사 문서·블로그·2차 자료는 보조자료로 구분한다.
- 근거를 찾지 못하면 '미확인'으로 표시하고 의무라고 단정하지 않는다.
- 중요한 법적·기술적 결론은 가능한 경우 독립된 공식 자료 또는 별도 근거로 교차 확인한다.

## 3. 분류 규칙
모든 결과를 다음 중 하나로 표시한다.
- 법적 의무(규정 원문으로 확인)
- 표준 요구사항(표준의 정확한 판·조항 확인)
- 공식 가이드/해석
- 엔지니어링 권고
- 가설/추가 확인 필요

## 4. CRA와 제품 적용성
- 서보 드라이브가 CRA 적용 대상이라고 무조건 단정하지 않는다.
- 제품의 디지털 요소, 시장 출시 주체, 의도된 용도, 별도 구성요소 판매 여부, 다른 EU 법령과의 관계, 예외를 확인한다.
- 산업용 제어 시스템이라는 이유만으로 CRA 분류 등급이나 제3자 적합성 평가 의무를 단정하지 않는다.
- 지원기간 5년은 일반적 최소 기준 문구와 제품의 예상 사용기간 예외를 함께 설명한다. 산업용 제품의 예상 사용기간이 5년보다 길다면 그 기간을 검토한다.

## 5. 검증과 문서화
- 보고서 자동 생성과 사실 검증을 별도 단계로 관리한다.
- 각 조사 항목에 주장, 근거, 원문, 해석, 적용성, 반대 근거/제약, 검증 상태를 기록한다.
- 중복 주제는 재작성하지 말고 기존 자료를 정정·보완한다.
- 수정 전 원본을 보존하고 정정 이력을 남긴다.
- 단일 통합 보고서와 필요한 부속서만 유지해 문서가 과도하게 쪼개지 않도록 한다.
- 한국어 본문, 공식 영문 원문, 근거 링크, 검토 기록을 상호 연결한다.
- 초안/구조 검증/출처 확인/전문가 검토/승인 상태를 구분하고, 미검증 초안을 최종 결론처럼 표현하지 않는다.

## 6. 코드·운영 변경
- 운영 `main.py`, workflow, secrets, 운영 데이터는 승인 없이 변경하지 않는다.
- 변경은 작업 브랜치에서 수행하고 mock 테스트부터 진행한다.
- 실패를 성공으로 기록하지 않는다. 생성 성공·전송 성공·저장 성공·근거 검증 성공을 분리한다.
- 외부 API 호출은 timeout, 재시도, 상태 코드, rate limit을 처리한다.
- secret은 코드·로그·보고서·이력에 출력하지 않는다.
- 변경 전후 diff, 테스트 결과, CI 링크, 롤백 방법을 기록한다.
- 테스트가 실제 실행되지 않았으면 '테스트 추가' 또는 '정적 검토'로만 표시하고 '통과'라고 쓰지 않는다.
- mock/helper 테스트 결과를 전체 저장소 테스트, 통합 테스트, CI 또는 운영 실행 결과로 확대 해석하지 않는다.

## 7. ST MCU 및 TI 비교
- 기본 설계 기준은 ST MCU 중심으로 작성한다.
- TI는 대체/비교 솔루션으로 동일한 기준(보안 기능, 안전 문서, 툴체인, 수명주기, 비용/가용성)을 적용해 비교한다.
- 특정 MCU 기능이 CRA 적합성을 자동 보장한다고 표현하지 않는다.
- 데이터시트·레퍼런스 매뉴얼·보안 매뉴얼·안전 매뉴얼 등 1차 자료를 근거로 한다.

## 8. 기능안전 경계
- CRA 사이버보안과 SIL 기능안전은 상호 영향이 있을 수 있지만 동일한 인증/요구사항이 아니다.
- 기능안전 관련 변경은 별도 안전 분석·검증·승인 없이는 적합성 결론을 내리지 않는다.

## 9. 프로젝트 기록 및 작업 연속성 — 필수
- 대화창의 문맥이나 모델 기억만을 프로젝트의 유일한 기록으로 사용하지 않는다.
- 의미 있는 작업 단위가 끝날 때마다 작업 브랜치의 GitHub 문서를 실제 갱신한다.
- 문서 역할을 분리해 중복·불일치를 줄인다.
  - `README.md`: 프로젝트 메인 페이지, 현재 상태 요약, 문서/산출물 진입점
  - `PROJECT_STATUS.md`: 현재 사실, 진행 상태, 위험, 다음 재개 지점이 있는 상황판
  - `MASTER_PLAN.md`: 목표, 우선순위, 단계별 완료 기준과 실행 순서
  - `AI_RULEBOOK.md`: 조사·검증·코드·문서화 행동강령
  - `SESSION_LOG.md`: 날짜별 수행 내용, 변경 파일, 검증 결과, 미완료 사항
  - `reports/`: 상세 감사·설계·정정·통합 기술 보고서
- 코드/조사 변경이 있으면 관련 보고서와 위 관리 문서 간 링크 및 상태를 함께 갱신한다.
- GitHub 파일을 수정한 뒤 동일 브랜치에서 다시 읽어 내용과 저장 여부를 확인한다. 저장 성공 응답만으로 검증 완료라고 하지 않는다.
- 작업 보고에는 반드시 실제 변경 파일, 커밋/저장 확인, 테스트 범위와 결과, 미실행 항목, 운영 영향, 다음 단계의 승인 필요 여부를 구분한다.
- 작업 브랜치와 운영 `main`의 차이를 확인하고, 자동 생성 데이터 손실 위험이 있으면 무리하게 merge/rebase하지 않는다.
- 작업을 시작할 때 이 문서와 README, 상황판, 마스터 계획, 최근 세션 로그를 기준으로 재개한다.
- 사용자에게 승인받지 않은 범위로 코드를 확장하지 않는다. 다만 문서·상황판의 사실 정합성 갱신은 기존 승인 범위 내에서 수행한다.

## 10. 객관적 우선순위
우선순위는 다음 기준으로 정한다.
1. 운영 데이터/비밀정보/안전 기능에 대한 손상 위험
2. 잘못된 법적·기술적 결론이 보고서로 확산될 위험
3. 재현성과 테스트 가능성, 장애 복구 가능성
4. 다른 작업을 막는 선행 조건
5. 사용자 최종 산출물에 대한 가치
6. 구현 비용과 유지보수 복잡도

빠르게 많은 파일이나 코드를 만드는 것보다, 선행 위험을 줄이고 검증 가능한 산출물을 누적하는 방식을 우선한다.


## 11. 테스트 원본성 및 부작용 검증 추가 규칙
- 테스트 실행 전 대상 브랜치, commit SHA, 각 핵심 소스 파일의 Git blob SHA를 기록한다.
- 로컬 테스트 사본은 GitHub에서 조회한 원본과 blob SHA가 일치할 때만 해당 브랜치 소스 테스트로 인정한다. 일치하지 않으면 예비 검증으로만 기록한다.
- mock은 성공 응답만 흉내 내서는 안 된다. HTTP timeout/429/4xx/5xx/네트워크 오류, Git 명령의 non-zero exit와 check=True 예외, 부분 전송 및 재시도 경로를 별도 검증한다.
- 테스트 fixture가 항상 성공을 반환하거나 실패 예외를 무시하면 그 경로는 검증되지 않은 것으로 명시한다.
- 운영 workflow를 테스트 목적으로 실행하지 않는다. 별도 테스트 workflow 추가·기존 workflow 변경·PR 트리거 구성은 사용자에게 영향과 위험을 설명하고 별도 승인받는다.
- 정적 검토, helper 단위 테스트, 원본 전체 pytest, CI, 운영 실행을 서로 다른 검증 단계로 구분한다.
 
## 12. 이중 형식 프로젝트 로그
- 프로젝트 변경 이력은 `PROJECT_LOG.jsonl`과 `SESSION_LOG.md`에 함께 남긴다.
- JSONL은 한 줄에 하나의 완전한 JSON 객체를 기록한다. 최소 필드: `event_id`, `date`, `kind`, `status`, `summary_ko`, `branch`, `files`, `verification`, `limitations`, `approval`.
- 실행·검증 사건에는 가능한 경우 `commit`, `evidence`(CI/PR/공식 근거 링크)를 추가한다. 미실행 항목을 성공으로 기록하지 않는다.
- `SESSION_LOG.md`에는 배경, 판단 이유, 상세 절차, 검증 범위와 미해결 사항을 한국어로 기록한다.
- 두 로그는 같은 사건 ID 또는 명확한 상호 링크로 연결하고, 값이 충돌하면 원본 증거를 재조회해 정정한다.
- `state.json`·`history.json`은 기존 운영 자동화 데이터이며 프로젝트 작업 로그와 분리한다. 별도 승인 없이 변경하지 않는다.


## 13. 브랜치·커밋·변경 추적 규칙
- 운영 `main`은 직접 수정하지 않는다. 작업 목적별 짧고 명확한 feature/test/docs 브랜치를 만들고, 생성 시 기준 브랜치와 기준 commit SHA를 기록한다.
- 작업 시작 전에 기준 HEAD, 대상 파일 blob SHA, 현재 `main` 대비 ahead/behind 및 merge-base를 확인한다.
- 변경 단위마다 승인 범위, 파일별 변경 전·후, 변경 이유, 예상 영향, 테스트 계획, 복구 방법을 기록한다.
- 커밋은 논리적 작업 단위로 묶고 `test:`, `fix:`, `ci:`, `docs:` 등 의미가 분명한 메시지를 사용한다. 파일 단위 API로 작은 커밋이 불가피하면 그 이유를 세션 로그에 명시한다.
- CI는 실행 commit SHA와 핵심 소스 blob SHA를 대조한다. 단순히 최신 run이 성공했다는 이유로 다른 commit의 코드를 검증했다고 주장하지 않는다.
- 작업 완료 후 기준점 대비 파일 diff, branch HEAD, CI run, main 대비 diverged 상태를 다시 조회한다.
- 실패한 시도와 수정 내역도 감추지 않고 기록한다. 복구는 우선 revert commit으로 하며, 승인 없는 force push·history rewrite·merge·rebase는 금지한다.
- 별도 승인 전 PR merge 및 운영 배포를 하지 않는다.


## 14. HTTP POST·재시도·부분 성공 안전 원칙
- 외부 POST 요청은 timeout을 명시하고 HTTP 응답 성공 여부를 확인한다.
- 응답 유실 시 서버가 작업을 반영했는지 불명확할 수 있다. idempotency 보장 없이 timeout/5xx POST를 자동 재전송해 중복 작업을 만들지 않는다.
- Discord 429는 공식 Retry-After/retry_after를 준수하고, 400/401/403/404 등 영구 오류는 반복 요청하지 않는다.
- chunk 전송은 파트별 확인 상태를 유지하고 일부 성공을 전체 성공으로 표시하지 않는다.
- 파일별 atomic replace가 여러 파일을 하나의 transaction으로 만드는 것은 아니다. state/history 복구 journal 또는 동등한 일관성 설계를 검증한다.
- P1-B2는 2026-11-16 사용자 승인으로 작업 브랜치 구현 및 CI 검증을 완료했다. P1-B3/B4와 운영 반영은 별도 승인 전 금지한다.


## 15. P1-B1 Discord webhook 전송 구현 원칙
- webhook POST는 connect/read timeout과 wait=true를 사용한다.
- 2xx 응답이라도 message ID 확인 전에는 성공으로 기록하지 않는다.
- ConnectTimeout만 제한 재시도하고 ReadTimeout/일반 ConnectionError/5xx는 delivery_unknown으로 분류해 중복 전송을 피한다.
- 429는 Retry-After/retry_after를 따르며 재시도 횟수와 대기 예산을 제한한다.
- 400/401/403/404는 영구 실패로 분류하고 재시도하지 않는다.
- chunk별 성공 ID를 보존하고 일부 성공 후 실패는 partial로 표시한다.
- 전송 상태의 영속화는 P1-B2/B3에서 별도 설계·승인한다.
- P1-B1과 P1-B2는 각각 별도 사용자 승인을 받아 작업 브랜치 구현 및 테스트 전용 CI 검증을 완료했다. P1-B3/B4 및 운영 workflow 변경·운영 배포는 승인된 것으로 간주하지 않는다.


## Git 통합 감사 규칙 추가 — 2026-11-16
- GitHub compare API의 변경 파일 목록이 300개에서 잘릴 수 있으므로 대규모 분기에서는 이를 전체 목록으로 간주하지 않는다. recursive Git tree 조회와 blob SHA 비교로 전체 경로 차이를 교차검증한다.
- 운영 브랜치의 `state.json`, `history.json`, 자동 생성 archive는 코드 변경과 별도 보존 자산이다. 별도 데이터 migration 승인 없이 작업 브랜치의 파일로 덮어쓰지 않는다.
- ahead/behind, HEAD, merge-base는 조회 시점의 스냅샷이다. 병합 판단 직전에 다시 조회한다.
- CI 성공은 코드/테스트 범위의 검증 증거일 뿐 운영 데이터 보존, 법적 적합성 또는 기능안전 인증을 증명하지 않는다.


## P1-B2 저장 설계 승인 경계 — 2026-11-16
- archive/state/history의 atomicity는 파일별 os.replace만으로 다중 파일 transaction이 되지 않는다. durable journal, staged payload, old/new SHA 검증, idempotent recovery를 함께 설계한다.
- 손상된 journal/stage 또는 예상하지 못한 target SHA를 발견하면 자동 초기화·덮어쓰기하지 말고 fail-closed 한다.
- P1-B2는 로컬 저장 일관성만 다룬다. Discord exactly-once/outbox와 Git sync status를 보장하지 않는다.
- 이 문장은 P1-B2 설계 승인 이전의 경계 기록이다. 2026-11-16 사용자 승인 후 작업 브랜치 구현과 테스트 CI 검증을 완료했다. 운영 main/data/run.yml 변경과 PR merge/운영 배포는 여전히 별도 승인 대상.


## 16. P1-B2 durable persistence 구현 기준 — 2026-11-16
- `research_archive/`, `history.json`, `state.json`을 한 transaction ID로 묶고 PREPARED/APPLYING/COMMITTED journal을 사용한다.
- stage/backup/manifest/journal은 SHA 검증과 fsync를 수행한다. target 교체는 같은 디렉터리의 임시 파일과 os.replace를 사용하고 directory fsync를 수행한다.
- 시작 시 pending transaction recovery를 state/history 읽기 및 외부 API 호출보다 먼저 수행한다.
- commit 시 처음 읽은 raw bytes snapshot SHA와 현재 target SHA를 비교해 동시 변경을 덮어쓰지 않는다.
- journal/stage/backup 손상, 잘못된 경로, target SHA mismatch, lock 획득 실패는 fail-closed 한다. 자동 초기화·임의 복구·덮어쓰기를 금지한다.
- POSIX `fcntl.flock` 및 directory fsync 지원 환경을 전제로 한다. Windows 지원을 주장하지 않는다.
- lock은 recovery/commit 구간에 한정한다. 외부 API 호출 구간까지 잠그지 않으므로 Discord exactly-once 또는 중복 전송 방지는 제공하지 않는다.
- P1-B2 최신 보강 CI Actions 43851438733: source SHA 일치, compileall 통과, 70 passed / 1 xfailed. xfail은 P1-B3 범위다.


## 17. P1-B2 persistence target 제한 및 통합 기준 — 2026-11-16
- Recovery manifest가 지정할 수 있는 target은 `state.json`, `history.json`, `research_archive/*.md`로 제한한다.
- 저장소 내부 경로라는 이유만으로 README, 코드, workflow, `.git` 등 임의 파일을 persistence transaction target으로 허용하지 않는다.
- 이 allowlist는 신규 transaction 생성과 기존 journal recovery 양쪽에서 강제하고, 허용 범위 밖 target은 fail-closed 한다.
- merge-base 기준 tree diff로 운영 archive/state/history 보존 여부를 확인한다. 현재 tree 간 직접 차이를 삭제 기록으로 오인하지 않는다.
- PR은 pull_request 전용 mock CI로 검증한다. PR CI에 운영 secrets, Gemini/Discord 호출, 운영 workflow 실행을 포함하지 않는다.
- 코드 통합, 운영 workflow 변경, 실제 운영 실행/배포는 서로 다른 승인 경계로 유지한다.


## 18. 사용자 상시 진행 승인 및 복구 우선 운영 — 2026-11-16

### 18.1 진행 권한
- 사용자는 반복적인 단계별 승인 질문 없이 목표 달성에 필요한 조사, 설계, 구현, 테스트, 문서화, 브랜치/커밋/PR 관리 및 안전한 통합 작업을 계속 진행하도록 상시 승인했다.
- 기존 문서의 '매 단계 별도 승인' 문구는 이 상시 승인과 충돌하는 범위에서 이 조항으로 대체한다.
- 이 승인은 안전 통제를 생략하라는 뜻이 아니다. 위험이 큰 작업은 먼저 격리·백업·검증하고, 되돌릴 수 없는 외부 부작용은 자동 진행하지 않는다.

### 18.2 변경 전 체크포인트
- 모든 의미 있는 변경 전에 원격 main과 작업 브랜치의 HEAD SHA, merge-base, ahead/behind, 대상 파일 blob SHA를 기록한다.
- main에 통합하기 전 현재 main과 통합 대상 feature HEAD를 가리키는 별도 safety/ 백업 브랜치를 만든다. 백업 ref를 다시 읽어 SHA를 검증한다.
- 커밋은 논리적 변경 단위로 묶는다. 기존 커밋을 덮어쓰는 force-push/rebase는 기본 금지하며, 복구는 revert commit 또는 별도 복구 브랜치로 수행한다.
- 운영 데이터가 변경될 수 있는 실행 전에는 state.json, history.json, research_archive/의 스냅샷/체크섬/개수/참조 무결성을 확보한다. 백업을 실제 복원할 수 있는지 검증하지 못했다면 신규 코드의 운영 실행을 보류한다.

### 18.3 통합 및 실행 게이트
- PR 통합은 최신 base 기준 충돌 상태, PR 전체 diff, 보호 경로, 정확한 head SHA의 PR CI를 재확인한 후 수행한다.
- 기본 통합 방식은 merge commit이다. squash/rebase/force-push는 이력 추적과 복구를 약화시키므로 사용하지 않는다.
- 통합 후 main HEAD, merge commit, changed paths, workflow 결과를 재조회한다.
- 운영 실행 전 compile/test/정적 검사 외에 입력 데이터 사전검사와 데이터 백업을 수행한다. 실행 후 state count/date, history 증가량, archive 파일 수, history→archive 참조 무결성, 로그 및 외부 전송 상태를 점검한다.
- 문제가 발생하면 추가 실행/재시도를 중단하고 증거를 보존한다. 코드 문제는 직전 정상 merge commit으로 revert하고, 데이터 문제는 검증된 백업에서 별도 복구 commit으로 복원한다.
- Discord 등 외부 전송은 이미 전달된 메시지를 Git revert로 회수할 수 없다. 중복 전송 위험이 있으면 자동 재전송하지 않고 상태를 delivery-unknown으로 남긴다.

### 18.4 중단 조건과 보고
- 테스트 실패, 원본 SHA 불일치, 보호 경로의 예상 밖 변경, 백업/복원 검증 실패, 데이터 무결성 저하, secret 노출 징후가 있으면 해당 단계에서 중단하고 원인을 조사한다.
- 중단은 사용자에게 다시 승인받기 위한 절차가 아니라 데이터/서비스 손상을 막기 위한 안전 정지다. 복구 가능한 범위는 계속 자동으로 수행한다.
- 매 세션 종료 시 기준/현재 SHA, 커밋, 파일 diff, CI 링크, 백업 ref, 복구 방법, 실행 여부 및 남은 위험을 README·PROJECT_STATUS·SESSION_LOG·PROJECT_LOG에 기록한다.

### 18.5 현재 안전 체크포인트
- main pre-integration backup: safety/pre-merge-main-2622e332 → 2622e332d6a3defd2079ccad3af36970001de5c1.
- feature pre-integration backup: safety/pre-merge-feature-eba3aeb → eba3aeb5710dcc6507623d56d586a619e9a4fc46.
- 두 ref는 생성 완료했으며 별도 readback 및 SHA 검증을 다음 단계에서 완료해야 한다.
- 코드 revert 경로는 마련됐지만 운영 데이터 snapshot/restore는 아직 미완료다. 따라서 main 통합과 신규 코드의 실제 운영 실행은 현재 이 문서만으로 안전하다고 간주하지 않는다.

## 19. 운영 데이터 기준선 감사 결과 — 2026-11-16
- immutable main snapshot 4cf0e708b28a343898af00d01521044dfb9a1987 기준 state count=158, history=2,297, archive=2,297, 참조 누락 0.
- U+200B ZERO WIDTH SPACE가 앞에 붙은 별도 state.json(date=2026-06-07,count=0)은 원인 확인 전까지 보존한다.
- safety/pre-merge-main-4cf0e70가 위 immutable main commit을 정확히 가리키는 것을 확인했다.
- moving ref를 서로 다른 API 호출에서 조회하면 자동 아카이브 사이에 snapshot race가 생길 수 있다. 데이터 감사는 먼저 HEAD SHA를 고정한다.
- 이전 history/archive 1건 차이는 동일 immutable SHA 재검사에서 재현되지 않아 moving-ref race로 정정했다.
- per-run 자동 데이터 백업/복원 리허설은 아직 미완료다.

## 20. 운영 실행 checkpoint/복구 guard 구현 — 2026-11-16
- production run workflow는 실행 직전 현재 main HEAD를 고유 safety/data-pre-run-{run_id}-{attempt} 브랜치로 보존한다.
- production workflow concurrency group으로 중복 실행을 직렬화한다.
- main.py 실행 뒤 operational_guard.py가 baseline/current commit parent, remote main HEAD, changed paths, state/history/archive append-only, 새 보고서 1건, count 및 참조 무결성을 확인한다.
- 검증 실패 시 remote main이 해당 실행의 단일 child commit일 때만 state/history/archive를 baseline으로 복구하는 새 commit을 push한다. force-push는 사용하지 않는다.
- remote main이 baseline 또는 다른 commit이면 자동 복구하지 않고 fail-closed 한다. checkpoint는 보존한다.
- quota 등 clean no-op은 local/remote HEAD가 baseline과 같고 data path가 clean할 때만 허용한다.
- local bare Git remote integration tests로 정상 전이, 손상 후 restore commit, 미push 거부, quota no-op을 검증했다.
- CI Run 43873774430에서 fixture 오류 1건(80 passed, 1 failed, 1 xfailed)을 발견해 수정. 최종 Run 43874801395에서 86 passed, 1 xfailed 및 compileall 통과.
- 최종 Run은 base f5b5a112ec72b01f8b3f91f734b8d755dde416c6, head 8ad2364992cfd0e4f60108d4bfcdf36e99d9131e 기준 성공.
- 이는 데이터 구조 무결성 검사이며 CRA 법적 적합성 또는 외부 Discord 전달의 회수 가능성을 보장하지 않는다.


## 21. 최신 rollback guard 보강 및 통합 기준 — 2026-11-16
- _current_snapshot은 state/history/archive root의 symlink를 거부하고, 누락/읽기 오류를 GuardError로 바꿔 검증 실패 시 조건부 복구 경로로 보낸다.
- empty archive file도 무결성 오류로 처리한다.
- missing state file 통합 테스트를 추가해 baseline restore commit으로 복구되는 경로를 검증했다.
- 최신 PR CI Run 43875746973: 87 passed, 1 xfailed, compileall 성공; base main SHA adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890, head abee2a88f7e0bbfad0ad483c6b50cea63e26b871.
- main #162 backup safety/pre-merge-main-adf74ea -> adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890, readback exact.
- main #162 same-SHA baseline: state count=162, history=2,301, archive=2,301, missing refs=0.
