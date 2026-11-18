"""P1-B1 Discord 전송 결과 정책과 미구현 P1-B3 경계를 검증한다."""
import json
import pytest
from test_main_characterization import VALID_REPORT


def test_discord_connect_timeout_retries_with_explicit_timeout_and_wait(run_main):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            run_main.exception_types.ConnectTimeout("mock connect timeout"),
            {"status_code": 200, "json": {"id": "discord-message-001"}},
        ],
    )
    assert len(run_main.captured["discord_posts"]) == 3
    for post in run_main.captured["discord_posts"]:
        assert post["timeout"] == (3.05, 10)
        assert post["params"] == {"wait": "true"}
    assert namespace["discord_result"]["status"] == "sent"
    assert namespace["discord_result"]["chunks"][0]["message_id"] == "discord-message-001"


def test_discord_429_retries_using_retry_after_header(run_main):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            {"status_code": 429, "headers": {"Retry-After": "1"}},
            {"status_code": 200, "json": {"id": "after-rate-limit"}},
        ],
    )
    assert len(run_main.captured["discord_posts"]) == 3
    assert run_main.captured["sleep_calls"] == [1.0, 1]
    assert namespace["discord_result"]["status"] == "sent"


def test_discord_429_uses_json_retry_after_when_header_missing(run_main):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            {"status_code": 429, "json": {"retry_after": 2.5}},
            {"status_code": 200, "json": {"id": "after-rate-limit"}},
        ],
    )
    assert len(run_main.captured["discord_posts"]) == 3
    assert run_main.captured["sleep_calls"] == [2.5, 1]
    assert namespace["discord_result"]["status"] == "sent"


def test_discord_429_beyond_wait_budget_is_deferred(run_main):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[{"status_code": 429, "headers": {"Retry-After": "31"}}],
    )
    assert len(run_main.captured["discord_posts"]) == 1
    assert run_main.captured["sleep_calls"] == []
    assert namespace["discord_result"]["status"] == "deferred"


def test_discord_503_is_delivery_unknown_without_automatic_retry(run_main):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            {"status_code": 503},
            {"status_code": 200, "json": {"id": "must-not-be-sent"}},
        ],
    )
    assert len(run_main.captured["discord_posts"]) == 1
    assert namespace["discord_result"]["status"] == "delivery_unknown"


@pytest.mark.parametrize("status_code", [400, 401, 403, 404])
def test_discord_permanent_errors_are_not_retried(run_main, status_code):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[{"status_code": status_code}],
    )
    assert len(run_main.captured["discord_posts"]) == 1
    assert namespace["discord_result"]["status"] == "permanent_failure"
    assert len(list((run_main.workdir / "research_archive").glob("*.md"))) == 1
    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    assert state["count"] == 1
    assert len(history) == 1


@pytest.mark.parametrize("failure_type", ["ReadTimeout", "ConnectionError"])
def test_ambiguous_transport_failures_are_not_retried(run_main, failure_type):
    failure = getattr(run_main.exception_types, failure_type)(
        "mock ambiguous transport failure"
    )
    namespace = run_main.execute([VALID_REPORT], discord_responses=[failure])
    assert len(run_main.captured["discord_posts"]) == 1
    assert namespace["discord_result"]["status"] == "delivery_unknown"


def test_later_chunk_failure_is_partial_and_preserves_archive(run_main):
    long_report = VALID_REPORT + "\n" + ("추가 근거 검토 내용입니다. " * 180)
    namespace = run_main.execute(
        [long_report],
        discord_responses=[
            {"status_code": 200, "json": {"id": "first-chunk"}},
            {"status_code": 403},
        ],
    )
    result = namespace["discord_result"]
    assert len(run_main.captured["discord_posts"]) == 2
    assert result["status"] == "partial"
    assert result["sent_chunks"] == 1
    assert result["chunks"][0]["message_id"] == "first-chunk"
    assert result["chunks"][1]["status"] == "permanent_failure"
    assert len(list((run_main.workdir / "research_archive").glob("*.md"))) == 1
    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    assert state["count"] == 1
    assert len(history) == 1


def test_connect_timeout_retry_limit_is_bounded(run_main):
    namespace = run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            run_main.exception_types.ConnectTimeout("connect timeout 1"),
            run_main.exception_types.ConnectTimeout("connect timeout 2"),
            run_main.exception_types.ConnectTimeout("connect timeout 3"),
        ],
    )
    assert len(run_main.captured["discord_posts"]) == 3
    assert namespace["discord_result"]["status"] == "failed"


def test_git_push_failure_is_not_reported_as_full_success(run_main, capsys):
    with pytest.raises(SystemExit) as exc:
        run_main.execute(
            [VALID_REPORT],
            git_responses=[0, 0, 0, 0, 1],
        )

    assert exc.value.code == 1
    assert run_main.captured["git_commands"][-1] == ["git", "push"]
    assert run_main.captured["git_options"][-1]["check"] is True
    output = capsys.readouterr().out
    assert "GitHub 운영 데이터 저장 실패" in output
    assert "깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다." not in output
