# GitHub 자동화 운영 점검 및 장애 기록 — 2026-11-17

## 요약
- 직전 정상 운영 실행 #2411은 성공했고 CRA 보고서 #234를 원격 main에 저장했다.
- 사전 실행 체크포인트 브랜치가 실행마다 생성되지만 성공 실행 후 오래된 브랜치를 정리하지 않아, 확인 시점에 `safety/data-pre-run-*` 브랜치가 94개 누적되어 있었다.
- 운영 실행 #2412는 실행 도중 main에 코드 변경 커밋이 들어와 non-fast-forward push가 거부되었다. 보고서 #235는 로컬에서 생성되고 Discord 2/2 청크 전송이 확인됐지만, 원격 main에는 저장되지 않았다. 후속 operational guard는 원격 main이 해당 실행 커밋을 가리키지 않는다는 이유로 자동 복구를 거부했고 workflow는 실패했다.
- #2412의 실패는 당시 진행 중인 운영 workflow와 main 수정 작업의 경합으로 발생했다. 변경 작업 시작 전에 활성 운영 실행을 기다리지 않은 작업 절차 오류다.

## 확인된 증거
| 항목 | 결과 |
|---|---|
| 직전 정상 실행 | #2411 / 43958205823 / success |
| 실패 실행 | #2412 / 43959068835 / failure |
| 실패 단계 | Verify run and automatically restore invalid data |
| Git push 오류 | `[rejected] main -> main (fetch first)` |
| 로컬 생성 커밋 | `ef4ca1fa`, Auto-archive: Research report #235 |
| Discord | sent, 2/2 chunks confirmed |
| Gemini 모델 | `gemini-flash-latest` 404 3회, 다음 모델 fallback 경로로 진행 |
| CI 실패 | Run 43959203356: 96 passed, 1 failed, 1 xfailed |
| 테스트 실패 원인 | 보호된 오래된 체크포인트를 최신 30개 외에 추가 보존하는 동작과 테스트 기대값이 불일치 |
| 현재 main 기준 | `b89f2bf58752045361fa088a6fc4311ba8798fcb` |
| 사전 변경 백업 | `safety/pre-checkpoint-prune-1abfcfb` → `1abfcfb26a8b414dc75eb584082ed35cab0d6412` |

## 영향 및 데이터 상태
- #2412의 보고서 본문은 실행 runner의 로컬 커밋에만 있었으며 원격 main에 push되지 않았다. 실행 환경 종료 후 해당 본문을 원격 저장소에서 복구할 수 있다고 가정하지 않는다.
- Discord 전송은 이미 완료되었으므로 Git 롤백으로 회수할 수 없다. 후속 실행에서 같은 일일 count로 새 보고서를 전송하면 사용자 채널에 중복 count가 생길 수 있으므로, 실행 결과를 별도로 추적한다.
- #2412 실행의 baseline 브랜치는 보존한다.
- 이전 성공 실행 20건은 조회 시점 기준 모두 success였다. 이것은 CRA 보고서의 법적 정확성 검증과는 별개다.

## 개선 사항
1. 성공적으로 guard 검증이 끝난 실행에서만 오래된 per-run checkpoint 브랜치를 정리한다.
2. 최신 30개를 기본 보존하고, 현재 실행의 baseline ref는 별도로 보호한다.
3. ref 이름이 예상 패턴과 다르거나 원격 ref 조회가 실패하면 삭제하지 않고 실패 처리한다.
4. guard가 실패한 실행에서는 cleanup step이 실행되지 않아 복구 증거를 보존한다.
5. 새로운 cleanup 스크립트와 테스트를 추가했다. 테스트의 보호된 오래된 ref 기대값을 수정한 후 CI 재검증한다.
6. 이후 main 변경은 활성 production workflow가 종료된 뒤에만 반영한다. 운영 데이터 변경 경합에 대한 재시도/복구 설계는 별도 검토한다.

## 제한 및 미완료
- 정리 정책 코드는 main에 반영됐으나, CI가 첫 실행에서 1개 테스트 실패로 끝나 수정 후 재검증이 필요하다.
- 아직 운영 workflow에서 실제 pruning이 성공한 것은 아니다.
- #2412의 Discord 전송과 미저장 보고서 간 관계는 중복 전송 방지를 위해 추적이 필요하다.
- Gemini 모델 404는 fallback이 동작했으나, 현재 모델 목록 및 사용 가능 여부를 별도 검증해야 한다.
