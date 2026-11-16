"""Phase B: 유효한 보고서만 후속 처리되는지 검증한다."""
import json
from datetime import datetime

import pytest


VALID_REPORT = """# CRA 심층 조사 보고서

## 1. 주제 요약
산업용 서보 드라이브의 사이버보안 요구사항과 제조자 책임을 정리한다.
제품의 의도된 용도와 위험평가 결과를 기준으로 요구사항 적용성을 판단한다.

## 2. 규격 근거 및 상세 내용
규정 (EU) 2024/2847의 관련 조항과 부속서 요구사항을 구분해 검토한다.
제조자는 제품 설계와 개발 단계에서 적절한 사이버보안 위험평가를 수행하고,
식별된 위험을 기술문서와 제품 보안 설계에 반영해야 한다.
본 설명은 적용성 검토를 위한 조사 초안이며 제품 분류는 별도 확인이 필요하다.

## 3. 출처 자료(Source)
EU 공식 법령 데이터베이스 EUR-Lex, Regulation (EU) 2024/2847.
https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng

## 4. 출처 원문 텍스트(Raw Text Quote)
원문 조항을 확인하고 제품에 적용되는 문구를 인용해 근거를 기록한다.
인용은 원문과 대조해야 하며 요약 문구를 법령 직접 인용으로 표시하지 않는다.
"""


def test_successful_generation_uses_only_mocked_external_services(run_main):
    run_main.execute([VALID_REPORT])

    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    archives = list((run_main.workdir / "research_archive").glob("*.md"))

    assert state["count"] == 1
    assert len(history) == 1
    assert len(archives) == 1
    assert "CRA 심층 조사 보고서" in archives[0].read_text(encoding="utf-8")
    assert len(run_main.captured["model_calls"]) == 1
    assert len(run_main.captured["discord_posts"]) == 1
    assert [cmd[0] for cmd in run_main.captured["git_commands"]] == [
        "git", "git", "git", "git", "git"
    ]


def test_model_fallback_is_exercised_without_real_api_calls(run_main):
    run_main.execute([
        RuntimeError("mock transient failure 1"),
        RuntimeError("mock transient failure 2"),
        RuntimeError("mock transient failure 3"),
        VALID_REPORT,
    ])

    calls = run_main.captured["model_calls"]
    assert len(calls) == 4
    assert calls[0]["model"] == "gemini-flash-latest"
    assert calls[-1]["model"] == "gemini-3.5-flash-lite"
    assert len(run_main.captured["discord_posts"]) == 1


def test_all_model_failures_stop_without_side_effects(run_main):
    with pytest.raises(SystemExit) as exc:
        run_main.execute([RuntimeError("mock failure") for _ in range(6)])

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "state.json").exists()
    assert not (run_main.workdir / "history.json").exists()
    assert not (run_main.workdir / "research_archive").exists()


def test_invalid_short_or_malformed_output_is_retried_and_rejected(run_main):
    invalid = "단순 오류 응답입니다. 조사를 완료하지 못했습니다."
    with pytest.raises(SystemExit) as exc:
        run_main.execute([invalid] * 6)

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()


def test_invalid_first_model_response_falls_back_to_valid_second_model(run_main):
    invalid = "짧은 응답"
    run_main.execute([invalid, invalid, invalid, VALID_REPORT])

    calls = run_main.captured["model_calls"]
    assert len(calls) == 4
    assert all(call["model"] == "gemini-flash-latest" for call in calls[:3])
    assert calls[3]["model"] == "gemini-3.5-flash-lite"
    assert len(run_main.captured["discord_posts"]) == 1

def test_error_text_inside_an_otherwise_structured_report_is_rejected(run_main):
    error_report = VALID_REPORT + "\n시스템 긴급 경고: 요청 처리에 실패했습니다."
    with pytest.raises(SystemExit) as exc:
        run_main.execute([error_report] * 6)

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()


def test_all_model_failures_preserve_existing_state_and_history(run_main):
    state = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": 17,
        "last_health_check": datetime.now().isoformat(),
    }
    history = [{"date": state["date"], "count": 17, "snippet": "기존 기록"}]
    state_path = run_main.workdir / "state.json"
    history_path = run_main.workdir / "history.json"
    state_path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
    history_path.write_text(json.dumps(history, ensure_ascii=False), encoding="utf-8")
    state_before = state_path.read_bytes()
    history_before = history_path.read_bytes()

    with pytest.raises(SystemExit) as exc:
        run_main.execute([RuntimeError("mock failure") for _ in range(6)])

    assert exc.value.code == 1
    assert state_path.read_bytes() == state_before
    assert history_path.read_bytes() == history_before
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()
