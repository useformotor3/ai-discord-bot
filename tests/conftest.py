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
    """main.py를 임시 작업 디렉터리에서 실행하고 외부 의존성을 전부 mock한다."""
    repo_root = Path(__file__).resolve().parents[1]
    captured = {
        "model_calls": [],
        "discord_posts": [],
        "git_commands": [],
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

    def execute(responses):
        genai_module = types.ModuleType("google.genai")
        genai_module.Client = lambda api_key=None: FakeClient(responses)
        google_module = types.ModuleType("google")
        google_module.genai = genai_module

        requests_module = types.ModuleType("requests")

        def fake_post(url, *, json):
            captured["discord_posts"].append({"url": url, "json": json})
            return SimpleNamespace(status_code=204, text="")

        requests_module.post = fake_post

        monkeypatch.setitem(sys.modules, "google", google_module)
        monkeypatch.setitem(sys.modules, "google.genai", genai_module)
        monkeypatch.setitem(sys.modules, "requests", requests_module)
        monkeypatch.setattr(time, "sleep", lambda seconds: None)

        def fake_subprocess_run(args, **kwargs):
            captured["git_commands"].append(list(args))
            return SimpleNamespace(returncode=0)

        monkeypatch.setattr(subprocess, "run", fake_subprocess_run)
        monkeypatch.chdir(tmp_path)
        monkeypatch.setenv("GEMINI_API_KEY", "TEST_ONLY_NOT_A_REAL_KEY")
        monkeypatch.setenv("DISCORD_WEBHOOK_URL", "https://example.invalid/mock-webhook")

        namespace = runpy.run_path(str(repo_root / "main.py"), run_name="__main__")
        return namespace

    return SimpleNamespace(
        execute=execute,
        captured=captured,
        workdir=tmp_path,
    )
