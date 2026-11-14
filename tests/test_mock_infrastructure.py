"""mock 격리 구조와 실패 주입 동작을 검증한다."""
import subprocess

import pytest

from test_main_characterization import VALID_REPORT


def test_fixture_exposes_separate_external_call_captures(run_main):
    assert set(run_main.captured) == {
        "model_calls",
        "discord_posts",
        "git_commands",
        "git_options",
        "sleep_calls",
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
        "requests.post('https://example.invalid/mock', json={'content': 'mock'}, timeout=3)\n"
        "subprocess.run(['git', 'push'], check=True)\n"
        "time.sleep(99)\n",
        encoding="utf-8",
    )

    run_main.execute([VALID_REPORT], script_path=script)

    assert len(run_main.captured["model_calls"]) == 1
    assert run_main.captured["model_calls"][0]["model"] == "mock-model"
    assert len(run_main.captured["discord_posts"]) == 1
    assert run_main.captured["discord_posts"][0]["timeout"] == 3
    assert run_main.captured["git_commands"] == [["git", "push"]]
    assert run_main.captured["git_options"] == [{"check": True}]
    assert run_main.captured["sleep_calls"] == [99]


def test_discord_mock_can_inject_http_status_and_retry_after(run_main):
    script = run_main.workdir / "discord_failure.py"
    script.write_text(
        "import requests\n"
        "response = requests.post('https://example.invalid/mock', "
        "json={'content': 'mock'}, timeout=4)\n"
        "assert response.status_code == 429\n"
        "assert response.headers['Retry-After'] == '2'\n"
        "response.raise_for_status()\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="429"):
        run_main.execute(
            ["unused"],
            script_path=script,
            discord_responses=[{
                "status_code": 429,
                "headers": {"Retry-After": "2"},
            }],
        )

    assert run_main.captured["discord_posts"][0]["timeout"] == 4
    assert run_main.captured["discord_posts"][0]["status_code"] == 429


def test_git_mock_reproduces_check_true_called_process_error(run_main):
    script = run_main.workdir / "git_failure.py"
    script.write_text(
        "import subprocess\n"
        "subprocess.run(['git', 'push'], check=True)\n",
        encoding="utf-8",
    )

    with pytest.raises(subprocess.CalledProcessError) as exc:
        run_main.execute(
            ["unused"],
            script_path=script,
            git_responses=[1],
        )

    assert exc.value.returncode == 1
    assert run_main.captured["git_commands"] == [["git", "push"]]
    assert run_main.captured["git_options"] == [{"check": True}]


@pytest.mark.parametrize("failure", [
    RuntimeError("mock connection reset"),
    TimeoutError("mock request timeout"),
])
def test_discord_fixture_injects_transport_exceptions(run_main, failure):
    script = run_main.workdir / "discord_transport_failure.py"
    script.write_text(
        "import requests\n"
        "try:\n"
        "    requests.post('https://example.invalid/mock', "
        "json={'content': 'mock'}, timeout=5)\n"
        "except Exception as exc:\n"
        "    assert str(exc) in ('mock connection reset', 'mock request timeout')\n"
        "else:\n"
        "    raise AssertionError('transport exception was not injected')\n",
        encoding="utf-8",
    )
    run_main.execute(["unused"], script_path=script, discord_responses=[failure])
    assert len(run_main.captured["discord_posts"]) == 1
    assert run_main.captured["discord_posts"][0]["timeout"] == 5
    assert run_main.captured["discord_posts"][0]["status_code"] is None


@pytest.mark.parametrize("status_code", [401, 403])
def test_discord_fixture_injects_authentication_http_failures(run_main, status_code):
    script = run_main.workdir / "discord_auth_failure.py"
    script.write_text(
        "import requests\n"
        "response = requests.post('https://example.invalid/mock', "
        "json={'content': 'mock'}, timeout=2)\n"
        "assert response.status_code in (401, 403)\n"
        "response.raise_for_status()\n",
        encoding="utf-8",
    )
    with pytest.raises(RuntimeError, match=str(status_code)):
        run_main.execute(
            ["unused"],
            script_path=script,
            discord_responses=[{"status_code": status_code}],
        )
    assert run_main.captured["discord_posts"][0]["status_code"] == status_code


@pytest.mark.parametrize(
    ("failed_index", "expected_commands"),
    [
        (0, [["git", "add", "."]]),
        (1, [["git", "add", "."], ["git", "commit", "-m", "test"]]),
        (
            2,
            [
                ["git", "add", "."],
                ["git", "commit", "-m", "test"],
                ["git", "push"],
            ],
        ),
    ],
    ids=["git-add", "git-commit", "git-push"],
)
def test_git_fixture_injects_failure_at_each_sync_stage(
    run_main, failed_index, expected_commands
):
    script = run_main.workdir / "git_stage_failure.py"
    script.write_text(
        "import subprocess\n"
        "subprocess.run(['git', 'add', '.'], check=True)\n"
        "subprocess.run(['git', 'commit', '-m', 'test'], check=True)\n"
        "subprocess.run(['git', 'push'], check=True)\n",
        encoding="utf-8",
    )
    responses = [0] * failed_index + [1]
    with pytest.raises(subprocess.CalledProcessError) as exc:
        run_main.execute(
            ["unused"],
            script_path=script,
            git_responses=responses,
        )
    assert exc.value.returncode == 1
    assert run_main.captured["git_commands"] == expected_commands
    assert all(item["check"] is True for item in run_main.captured["git_options"])
