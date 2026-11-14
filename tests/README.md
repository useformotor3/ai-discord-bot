# Phase A 테스트 기반

## 목적
- 운영 `main.py`를 수정하지 않고 현재 동작을 재현한다.
- Gemini, Discord HTTP, Git subprocess, sleep을 전부 mock 처리한다.
- 테스트는 임시 디렉터리에서만 상태파일과 아카이브를 생성한다.
- 실제 API, Webhook, Git commit/push는 호출하지 않는다.

## 실행
저장소 루트에서 다음 명령을 실행한다.

```bash
python -m pip install pytest
python -m pytest -q
```

## 테스트 해석
- 정상 생성 및 모델 폴백은 현재 동작의 characterization test다.
- 전체 모델 실패 테스트는 현재 P0 결함을 재현하는 기준선이다. 경고문이 보고서로 저장되는 동작은 정상 요구사항이 아니며 Phase B에서 실패 상태/저장 차단으로 변경하고 해당 테스트 기대값도 함께 수정해야 한다.
- 이 단계에서는 workflow와 의존성 파일을 변경하지 않는다.
# Phase A/B 테스트 기반

## 목적
- 운영 코드와 분리된 mock 환경에서 `main.py`의 핵심 흐름을 검증한다.
- Gemini SDK, Discord HTTP, Git subprocess, sleep을 mock 처리한다.
- 상태파일과 아카이브는 pytest 임시 디렉터리에서만 생성한다.
- 실제 API, Webhook, Git commit/push는 호출하지 않는다.

## 실행
저장소 루트에서 다음 명령을 실행한다.

```bash
python -m pip install pytest
python -m compileall -q main.py tests
python -m pytest -q
```

## 검증 범위
- 정상 보고서 생성 및 후속 처리
- Gemini 모델 폴백 및 재시도
- 전체 모델 실패 시 비정상 종료
- 짧거나 필수 항목이 빠진 응답 거부
- 구조화된 보고서 안에 포함된 명시적 오류 문구 거부
- 실패 시 기존 state/history 보존 및 아카이브·Discord·Git 작업 미실행
- mock 경계가 실제 외부 호출을 가로채는지 검증

## 한계
- 보고서 구조 검증은 출처 원문 대조, 법률 해석의 정확성, 인용의 진위까지 검증하지 않는다.
- 테스트는 mock 기반이다. 실제 Gemini·Discord 통합 및 GitHub Actions CI 결과와 구분한다.
- Discord HTTP 응답 검증, Git push 실패 상태화, state/history 손상 복구는 후속 단계의 별도 범위다.
