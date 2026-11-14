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
