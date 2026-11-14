"""mock 격리 구조 자체의 최소 검증."""
def test_fixture_exposes_separate_external_call_captures(run_main):
    assert set(run_main.captured) == {
        "model_calls",
        "discord_posts",
        "git_commands",
    }
    assert run_main.workdir.exists()
