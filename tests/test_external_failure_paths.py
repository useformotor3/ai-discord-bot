"""P1-B 실패 경로 기대 동작을 고정한다.

현재 main.py가 아직 해당 정책을 구현하지 않았으므로 strict xfail로 표시한다.
운영 코드가 기대 동작을 충족하면 XPASS(strict)로 CI가 실패해 xfail 해제를 요구한다.
"""
import pytest

from test_main_characterization import VALID_REPORT


@pytest.mark.xfail(
    strict=True,
    reason="P1-B: Discord 요청에 명시적 timeout을 전달해야 함",
)
def test_discord_request_uses_explicit_timeout(run_main):
    with pytest.raises(RuntimeError, match="mock timeout"):
        run_main.execute(
            [VALID_REPORT],
            discord_responses=[RuntimeError("mock timeout")],
        )

    assert run_main.captured["discord_posts"][0]["timeout"] is not None


@pytest.mark.xfail(
    strict=True,
    reason="P1-B: Discord 429는 Retry-After 정책에 따라 제한 재시도해야 함",
)
def test_discord_429_is_retried_then_succeeds(run_main):
    run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            {"status_code": 429, "headers": {"Retry-After": "1"}},
            {"status_code": 204},
        ],
    )

    assert len(run_main.captured["discord_posts"]) == 2


@pytest.mark.xfail(
    strict=True,
    reason="P1-B: Discord 5xx는 제한 재시도해야 함",
)
def test_discord_503_is_retried_then_succeeds(run_main):
    run_main.execute(
        [VALID_REPORT],
        discord_responses=[
            {"status_code": 503},
            {"status_code": 204},
        ],
    )

    assert len(run_main.captured["discord_posts"]) == 2


@pytest.mark.xfail(
    strict=True,
    reason="P1-B: 영구 Discord 4xx 실패를 성공으로 취급하거나 후속 저장하면 안 됨",
)
def test_discord_400_blocks_archive_and_state_updates(run_main):
    run_main.execute(
        [VALID_REPORT],
        discord_responses=[{"status_code": 400}],
    )

    assert not (run_main.workdir / "research_archive").exists()
    assert not (run_main.workdir / "state.json").exists()
    assert not (run_main.workdir / "history.json").exists()


@pytest.mark.xfail(
    strict=True,
    reason="P1-B: Git push 실패를 삼키지 말고 sync 실패로 노출해야 함",
)
def test_git_push_failure_is_not_reported_as_full_success(run_main):
    run_main.execute(
        [VALID_REPORT],
        git_responses=[0, 0, 0, 0, 1],
    )

    assert run_main.captured["git_commands"][-1] == ["git", "push"]
    assert run_main.captured["git_options"][-1]["check"] is True
    assert run_main.captured["git_sync_status"] == "failed"
