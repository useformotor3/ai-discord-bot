# P1-B2 원자적 로컬 저장 설계서

- 작성일: 2026-11-16
- 저장소: `useformotor3/ai-discord-bot`
- 기준 작업 브랜치 HEAD: `227e3298066af4bda83fb0713fc1d57c749ee8c6`
- 기준 `main.py` blob SHA: `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`
- 상태: **사용자 승인 완료 / 구현 및 테스트 전용 CI 검증 완료 (2026-11-16)**
- 범위: 로컬 `research_archive/`, `state.json`, `history.json` 저장 일관성
- 제외: Discord outbox/전달 보장, Git push 상태화(P1-B3), import-time 실행구조(P1-B4), 운영 workflow, 운영 데이터 migration

## 1. 현행 동작과 문제

현재 작업 브랜치 코드의 주요 순서는 다음과 같다.

1. 상태 및 이력 JSON 읽기·검증
2. 조사 보고서 생성 및 형식 검증
3. Discord chunk 전송 시도
4. archive Markdown 파일 직접 쓰기
5. 메모리의 state count 갱신 후 `state.json`을 직접 덮어쓰기
6. history 항목 추가 후 `history.json`을 직접 덮어쓰기
7. Git add/commit/push 시도

문제:
- `write_text` / `json.dump` 직접 쓰기는 프로세스 종료·디스크 부족 시 파일이 잘리거나 JSON이 손상될 수 있다.
- archive, state, history는 각각 별도 파일이므로 한 파일 저장 성공 후 다음 파일이 실패하면 서로 불일치할 수 있다.
- 두 JSON을 별도 atomic replace만 하더라도 세 파일 전체의 트랜잭션 원자성은 확보되지 않는다.
- Discord 전송과 로컬 저장은 하나의 원자적 트랜잭션이 아니다. P1-B2만으로 Discord exactly-once를 보장할 수 없다.

## 2. 목표 불변조건

1. 기존 파일은 새 내용이 완전히 준비되기 전까지 덮어쓰지 않는다.
2. 저장 도중 실패해도 원본 파일은 유효한 이전 버전 또는 유효한 새 버전이어야 한다.
3. archive/state/history의 한 실행 단위는 동일한 transaction ID로 묶인다.
4. 복구는 재실행해도 결과가 변하지 않는 idempotent roll-forward 방식이어야 한다.
5. 예상하지 못한 파일 SHA, 손상된 journal, 누락된 stage 파일은 임의 초기화하지 않고 fail-closed 한다.
6. archive 파일명 충돌 시 덮어쓰지 않고 실행을 중단하거나 안전한 고유 ID 파일명을 사용한다.
7. 기존 JSON 스키마와 history 항목 형식은 유지한다.
8. 테스트 환경에서만 구현·검증하며 운영 state/history/archive는 변경하지 않는다.

## 3. 제안 아키텍처: durable journal + staged roll-forward

### 3.1 트랜잭션 디렉터리
같은 파일시스템 안에 `.persistence_txn/<transaction_id>/`를 둔다.

- `manifest.json`: transaction ID, schema version, target path, old SHA(신규 archive는 expected absent), new SHA, staged path, operation order, phase
- `staged/`: 완성된 archive/state/history payload
- `backup/`: 교체 전 기존 파일의 byte-for-byte 백업
- `journal.json`: 현재 트랜잭션이 PREPARED / APPLYING / COMMITTED 중 어디까지 진행됐는지 기록

임시 파일과 대상 파일은 동일 filesystem에 둬 `os.replace`가 같은 파일시스템 내 원자적 이름 교체가 되도록 한다.

### 3.2 Prepare 단계
1. archive/state/history의 최종 payload를 메모리에서 생성한다.
2. transaction ID와 archive filename을 생성하고 기존 archive path와 충돌하지 않는지 확인한다.
3. 각 staged 파일을 별도 임시 파일로 쓴다.
4. 파일별 `flush()` 및 `os.fsync()`를 수행한다.
5. 기존 state/history의 백업을 만들고 fsync한다.
6. manifest를 기록하고 fsync한다.
7. manifest/journal을 원자적 replace로 활성화하고 디렉터리 fsync를 시도한다.
8. 이 시점 전 실패는 대상 파일을 전혀 변경하지 않는다.

### 3.3 Apply 단계
1. journal을 `APPLYING`으로 갱신한다.
2. 아래 고정 순서로 staged payload를 대상 경로에 반영한다.
   - archive 신규 파일
   - history.json
   - state.json
3. 각 대상에 대해 현재 SHA가 manifest의 old SHA(또는 신규 파일의 expected absent)인지 확인한다.
4. 이미 new SHA와 같으면 해당 단계는 완료된 것으로 간주한다.
5. old SHA와 같으면 staged payload에서 새 임시 파일을 다시 만들고 fsync한 뒤 `os.replace`한다.
6. old SHA도 new SHA도 아닌 값이면 외부 변경/동시 실행 가능성이 있으므로 덮어쓰지 않고 중단한다.
7. 각 단계 후 journal progress를 기록한다.
8. 모든 대상의 SHA가 new SHA와 일치하면 journal을 COMMITTED로 바꾸고 fsync한다.

staged 원본은 replace에 직접 소비하지 않는다. 매번 staged payload로부터 대상과 같은 디렉터리에 교체용 임시 파일을 새로 만들어야 crash recovery에서 재사용할 수 있다.

### 3.4 Recovery 단계
- 애플리케이션이 state/history를 읽거나 외부 서비스 호출을 시작하기 전에 미완료 journal을 검색한다.
- POSIX advisory lock은 recovery 및 commit 구간에 한정한다. 장시간 Gemini/Discord 호출 중 lock을 유지하지 않고, 읽기 시점의 raw bytes SHA를 저장 직전에 비교해 stale update를 거부한다. 동시 실행에서 Discord 중복 전송까지 막는 보장은 제공하지 않는다.
- PREPARED: manifest와 staged SHA가 정상이라면 정책에 따라 중단 또는 안전한 roll-forward를 수행한다. 구현 전 선택을 고정한다.
- APPLYING: 각 target SHA를 검사해 이미 적용된 파일은 건너뛰고 나머지를 roll-forward 한다.
- COMMITTED: 모든 target SHA가 new SHA인지 재확인한 뒤 stage/backup/journal을 정리한다.
- journal 또는 stage가 손상됐거나 대상 SHA가 old/new 중 어느 쪽도 아니면 원본을 보존하고 fail-closed 한다.
- 복구 중 외부 Gemini/Discord/Git 호출은 하지 않는다.

권고: PREPARED 이후에는 자동 roll-forward, PREPARED 이전은 대상 파일 변경이 없으므로 미완료 stage 정리만 허용한다. journal 활성화가 durable하게 완료됐는지 구분할 수 있도록 PREPARED journal 자체를 단일 활성화 지점으로 취급한다.

## 4. 동시 실행 및 파일시스템 경계

- 프로세스 시작 시 persistence lock을 획득하고 lock이 없으면 생성한다.
- lock 획득 실패 시 두 실행이 동시에 같은 state/history를 갱신하지 않도록 종료한다.
- stale lock은 PID/호스트/시각 확인 없이 자동 삭제하지 않는다.
- stage, backup, target은 동일 파일시스템에 둔다.
- POSIX 디렉터리 fsync가 불가능한 환경에서는 durability 보장이 약해짐을 로그에 명시하고 지원 범위를 테스트한다.
- GitHub Actions의 concurrency 설정이나 workflow 수정은 이번 범위에 포함하지 않는다.

## 5. Discord 및 Git 경계

- Discord POST와 로컬 파일 저장은 원자적 트랜잭션이 아니다. P1-B2가 Discord exactly-once나 알림 유실 방지를 보장한다고 표현하지 않는다.
- Discord 결과 영속화/outbox 및 Git push 결과 상태화는 별도 설계가 필요하다.
- Git add/commit/push 실패가 로컬 저장 성공 여부를 뒤집지 않는다.
- P1-B2는 Git sync 상태를 성공으로 표시하거나 재시도하지 않는다(P1-B3 영역).
- 기존 P1-B1 전송 정책과 응답 판정은 변경하지 않는다.

## 6. 테스트 계획

실제 Gemini, Discord, Git push, 운영 파일 접근 없이 tmp_path와 주입 가능한 filesystem adapter로 테스트한다.

| 테스트 | 주입 지점 | 기대 결과 |
|---|---|---|
| stage write 실패 | archive/state/history 각각 | 기존 대상 파일 byte 동일 |
| fsync 실패 | stage/journal | 대상 변경 없음 또는 journal 기반 복구 가능 |
| manifest 활성화 전 종료 | PREPARED 이전 | 대상 파일 변경 없음 |
| archive replace 직후 종료 | APPLYING | 재실행 시 history/state까지 roll-forward |
| history replace 직후 종료 | APPLYING | archive 중복 생성 없이 state까지 roll-forward |
| state replace 직후 종료 | APPLYING | SHA 검증 후 COMMITTED로 마감 |
| journal 손상 | recovery 시작 | fail-closed, 모든 원본 보존 |
| stage 누락/해시 불일치 | recovery 시작 | fail-closed, 자동 초기화 금지 |
| target old/new SHA 불일치 | recovery 시작 | 외부 변경 보호, 덮어쓰기 금지 |
| archive filename 충돌 | prepare | 기존 archive 보존, 충돌 처리 |
| 동시 실행 | lock 획득 | 두 번째 실행은 안전 종료 |
| cleanup 중 종료 | COMMITTED | 다음 시작에서 cleanup 재개 |
| legacy 파일 | 기존 state/history | 기존 포맷과 호환 |
| Discord 실패 | 로컬 transaction 후 | 기존 P1-B1 정책 유지, 로컬 데이터 무결성 보장 |

추가 property/invariant 테스트:
- 모든 종료 지점에서 각 target은 old 또는 new SHA 중 하나여야 한다.
- recovery를 여러 번 실행해도 최종 SHA와 history 항목 수가 변하지 않아야 한다.
- archive는 transaction ID 기준으로 중복 생성되지 않아야 한다.
- 실패한 트랜잭션의 history count와 state count가 서로 불일치한 채 완료 처리되지 않아야 한다.

## 7. 수용 기준

1. 신규 P1-B2 테스트가 모든 crash/failure injection 지점에서 통과한다.
2. 기존 테스트 43 passed / 1 xfailed의 기준 동작을 유지한다. xfail은 P1-B3 범위이므로 이 단계에서 임의 제거하지 않는다.
3. compileall 및 전체 pytest 통과, 정확한 source SHA가 테스트 전용 CI에서 검증된다.
4. 외부 API mock 호출 0건, 운영 파일 변경 0건.
5. 기존 state/history schema 및 archive markdown 호환성 확인.
6. 재시작 복구가 idempotent임을 확인하고, 손상/불일치 시 fail-closed함을 확인한다.
7. 사용자 승인 후 구현을 완료했고, CI Run #23에서 63 passed / 1 xfailed로 검증했다.

## 8. 롤백과 운영 적용

- 구현은 현재 작업 브랜치에서만 수행한다.
- 실패 시 작업 브랜치의 P1-B2 구현 커밋을 revert하고 기존 P1-B1 동작으로 복귀한다.
- 운영 state/history/archive에 migration이나 변환을 수행하지 않는다.
- 운영 반영은 현재 155 ahead / 660 behind의 분기 및 운영 데이터 감사가 별도 해결된 이후에만 검토한다.

## 9. 승인 경계

사용자 승인에 따라 작업 브랜치에서 `main.py`, 신규 `persistence.py`, P1-B2 장애 주입 테스트, 테스트 전용 workflow SHA pin을 구현했다. CI Run #23에서 source SHA·compileall·전체 pytest(63 passed / 1 xfailed)를 검증했다. 운영 `main.py`, 운영 `run.yml`, 운영 state/history/archive는 변경하지 않았다. P1-B3/B4 및 운영 통합은 별도 승인 전까지 금지한다.


## 10. 구현 결과 및 검증 — 2026-11-16
- 구현 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16`.
- `persistence.py`: durable journal, staged payload, backup SHA, path/manifest validation, POSIX flock, fsync, idempotent roll-forward.
- `main.py`: startup recovery → raw bytes snapshot read → report/Discord → archive/history/state transaction → existing Git sync attempt. P1-B1 Discord policy 자체는 변경하지 않았다.
- 저장 직전 old SHA가 처음 읽은 snapshot과 다르면 fail-closed 한다. lock은 recovery/commit 동안만 유지해 외부 API 대기 중 점유하지 않는다.
- CI Run #21은 테스트 파일 SHA pin 오류로 source integrity 단계에서 중단(테스트 미실행). Run #22에서 62 passed / 1 xfailed, directory fsync 및 중복 target 추가 후 Run #23에서 63 passed / 1 xfailed.
- Run #23: https://github.com/useformotor3/ai-discord-bot/actions/runs/43848498440
- 검증 commit: `045b8dbeb54d8d280ab91d6219d968bfdefed107`.
- 제한: POSIX flock/fsync 지원 환경(현재 Ubuntu CI) 전제. Windows native lock backend 미구현. Discord POST와 local persistence는 원자적이지 않으며 exactly-once/outbox는 범위 밖.
- 운영 main/data/workflow 미변경. main 대비 branch 172 ahead / 672 behind로 통합 보류.
