"""mock 격리 구조 자체의 최소 검증."""
def test_fixture_exposes_separate_external_call_captures(run_main):
    assert set(run_main.captured) == {
        "model_calls",
        "discord_posts",
        "git_commands",
    }
    assert run_main.workdir.exists()


def test_fixture_intercepts_all_external_boundaries(run_main):
    script = run_main.workdir / "mock_subject.py"
    script.write_text(
        "from google import genai\n"
        "import requests\n"
        "import subprocess\n"
        "import time\n"
        "client = genai.Client(api_key='fake')\n"
        "client.models.generate_content(model='mock-model', contents='mock-prompt')\n"
        "requests.post('https://example.invalid/mock', json={'content': 'mock'})\n"
        "subprocess.run(['git', 'push'], check=True)\n"
        "time.sleep(99)\n",
        encoding="utf-8",
    )

    run_main.execute(["mock response"], script_path=script)

    assert len(run_main.captured["model_calls"]) == 1
    assert run_main.captured["model_calls"][0]["model"] == "mock-model"
    assert len(run_main.captured["discord_posts"]) == 1
    assert run_main.captured["git_commands"] == [["git", "push"]]
