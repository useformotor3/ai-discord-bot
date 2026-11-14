"""외부 서비스가 실제로 호출되지 않는 main.py 격리 실행 fixture."""
from pathlib import Path
import runpy
import subprocess
import sys
import time
import types
from types import SimpleNamespace

import pytest


@pytest.fixture
def run_main(tmp_path, monkeypatch):
    """성공 기본값과 주입 가능한 실패 응답으로 외부 경계를 격리한다."""
    repo_root = Path(__file__).resolve().parents[1]
    captured = {
        "model_calls": [],
        "discord_posts": [],
        "git_commands": [],
        "git_options": [],
        "sleep_calls": [],
    }

    class FakeModels:
        def __init__(self, responses):
            self.responses = list(responses)

        def generate_content(self, *, model, contents):
            captured["model_calls"].append({"model": model, "prompt": contents})
            if not self.responses:
                raise AssertionError("테스트 응답 fixture가 소진되었습니다.")
            result = self.responses.pop(0)
            if isinstance(result, BaseException):
                raise result
            return SimpleNamespace(text=result)

    class FakeClient:
        def __init__(self, responses):
            self.models = FakeModels(responses)

    def execute(
        responses,
        script_path=None,
        discord_responses=None,
        git_responses=None,
    ):
        genai_module = types.ModuleType("google.genai")
        genai_module.Client = lambda api_key=None: FakeClient(responses)
        google_module = types.ModuleType("google")
        google_module.genai = genai_module

        requests_module = types.ModuleType("requests")

        class FakeResponse:
            def __init__(self, status_code=204, headers=None, text=""):
                self.status_code = status_code
                self.headers = headers or {}
                self.text = text

            def raise_for_status(self):
                if self.status_code >= 400:
                    raise RuntimeError(
                        f"mock Discord HTTP failure: {self.status_code}"
                    )

        discord_queue = list(discord_responses or [])

        def fake_post(url, *, json, **kwargs):
            response_spec = discord_queue.pop(0) if discord_queue else None
            captured["discord_posts"].append({
                "timeout": kwargs.get("timeout"),
                "payload_length": len(json.get("content", "")),
                "status_code": getattr(response_spec, "status_code", None),
            })
            if isinstance(response_spec, BaseException):
                raise response_spec
            if isinstance(response_spec, dict):
                return FakeResponse(
                    status_code=response_spec.get("status_code", 204),
                    headers=response_spec.get("headers"),
                    text=response_spec.get("text", ""),
                )
            if response_spec is None:
                return FakeResponse()
            return response_spec

        requests_module.post = fake_post
        requests_module.Timeout = type("Timeout", (Exception,), {})
        requests_module.ConnectionError = type("ConnectionError", (Exception,), {})

        monkeypatch.setitem(sys.modules, "google", google_module)
        monkeypatch.setitem(sys.modules, "google.genai", genai_module)
        monkeypatch.setitem(sys.modules, "requests", requests_module)
        monkeypatch.setattr(
            time,
            "sleep",
            lambda seconds: captured["sleep_calls"].append(seconds),
        )

        git_queue = list(git_responses or [])

        def fake_subprocess_run(args, **kwargs):
            command = list(args)
            captured["git_commands"].append(command)
            captured["git_options"].append({"check": kwargs.get("check", False)})
            result = git_queue.pop(0) if git_queue else None
            if isinstance(result, BaseException):
                raise result
            returncode = 0 if result is None else result
            completed = subprocess.CompletedProcess(command, returncode)
            if kwargs.get("check") and returncode:
                raise subprocess.CalledProcessError(returncode, command)
            return completed

        monkeypatch.setattr(subprocess, "run", fake_subprocess_run)
        monkeypatch.chdir(tmp_path)
        monkeypatch.setenv("GEMINI_API_KEY", "TEST_ONLY_NOT_A_REAL_KEY")
        monkeypatch.setenv(
            "DISCORD_WEBHOOK_URL",
            "https://example.invalid/mock-webhook",
        )

        target_script = (
            Path(script_path)
            if script_path is not None
            else repo_root / "main.py"
        )
        namespace = runpy.run_path(str(target_script), run_name="__main__")
        return namespace

    return SimpleNamespace(
        execute=execute,
        captured=captured,
        workdir=tmp_path,
    )
