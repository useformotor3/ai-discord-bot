"""현재 main.py의 동작을 기록하는 Phase A characterization tests.

이 테스트들은 운영 코드를 고치지 않는 Phase A의 기준선이다.
특히 전체 모델 실패 경로의 잘못된 성공 처리는 알려진 P0 결함이며,
Phase B에서 기대 동작으로 테스트를 전환한다.
"""
import json


def test_successful_generation_uses_only_mocked_external_services(run_main):
    run_main.execute(["테스트 보고서: CRA Article 13"])

    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    archives = list((run_main.workdir / "research_archive").glob("*.md"))

    assert state["count"] == 1
    assert len(history) == 1
    assert len(archives) == 1
    assert "테스트 보고서" in archives[0].read_text(encoding="utf-8")

    # Gemini, Discord, Git은 fixture mock을 통해서만 호출된다.
    assert len(run_main.captured["model_calls"]) == 1
    assert len(run_main.captured["discord_posts"]) == 1
    assert [cmd[0] for cmd in run_main.captured["git_commands"]] == [
        "git", "git", "git", "git"
    ]


def test_model_fallback_is_exercised_without_real_api_calls(run_main):
    run_main.execute([
        RuntimeError("mock transient failure 1"),
        RuntimeError("mock transient failure 2"),
        RuntimeError("mock transient failure 3"),
        "두 번째 모델의 테스트 보고서",
    ])

    calls = run_main.captured["model_calls"]
    assert len(calls) == 4
    assert calls[0]["model"] == "gemini-flash-latest"
    assert calls[-1]["model"] == "gemini-3.5-flash-lite"
    assert len(run_main.captured["discord_posts"]) == 1


def test_all_model_failures_currently_expose_known_p0_bug(run_main):
    """현재 결함을 명시적으로 고정해 Phase B에서 수정 여부를 확인한다."""
    run_main.execute([
        RuntimeError("mock failure") for _ in range(6)
    ])

    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    archives = list((run_main.workdir / "research_archive").glob("*.md"))

    # 현재 main.py는 전체 모델 실패 후에도 경고문을 보고서로 저장한다.
    # 이는 통과해야 할 제품 요구사항이 아니라 Phase B에서 제거할 기준선이다.
    assert len(run_main.captured["model_calls"]) == 6
    assert state["count"] == 1
    assert len(history) == 1
    assert len(archives) == 1
    assert "시스템 긴급 경고" in archives[0].read_text(encoding="utf-8")
