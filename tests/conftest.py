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
        "source_gets": [],
        "discord_posts": [],
        "git_commands": [],
        "git_options": [],
        "sleep_calls": [],
    }

    class RequestException(Exception):
        pass

    class Timeout(RequestException):
        pass

    class ConnectTimeout(Timeout):
        pass

    class ReadTimeout(Timeout):
        pass

    class ConnectionError(RequestException):
        pass

    exception_types = SimpleNamespace(
        RequestException=RequestException,
        Timeout=Timeout,
        ConnectTimeout=ConnectTimeout,
        ReadTimeout=ReadTimeout,
        ConnectionError=ConnectionError,
    )

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
        source_response_override=None,
    ):
        genai_module = types.ModuleType("google.genai")
        genai_module.Client = lambda api_key=None: FakeClient(responses)
        google_module = types.ModuleType("google")
        google_module.genai = genai_module

        requests_module = types.ModuleType("requests")

        class FakeResponse:
            def __init__(self, status_code=200, headers=None, text="",
                         body=None, message_id="mock-message-id"):
                self.status_code = status_code
                self.headers = headers or {}
                self.text = text
                self.body = body if body is not None else {"id": message_id}

            def json(self):
                if isinstance(self.body, BaseException):
                    raise self.body
                return self.body

            def raise_for_status(self):
                if self.status_code >= 400:
                    raise RuntimeError(
                        f"mock Discord HTTP failure: {self.status_code}"
                    )

        discord_queue = list(discord_responses or [])

        def fake_post(url, *, json, params=None, **kwargs):
            response_spec = discord_queue.pop(0) if discord_queue else None
            status_code = (
                response_spec.get("status_code", 200)
                if isinstance(response_spec, dict)
                else getattr(response_spec, "status_code", None)
            )
            captured["discord_posts"].append({
                "timeout": kwargs.get("timeout"),
                "params": params,
                "payload_length": len(json.get("content", "")),
                "status_code": status_code,
            })
            if isinstance(response_spec, BaseException):
                raise response_spec
            if isinstance(response_spec, dict):
                return FakeResponse(
                    status_code=response_spec.get("status_code", 200),
                    headers=response_spec.get("headers"),
                    text=response_spec.get("text", ""),
                    body=response_spec.get("json", {"id": "mock-message-id"}),
                    message_id=response_spec.get("message_id", "mock-message-id"),
                )
            if response_spec is None:
                return FakeResponse()
            return response_spec

        requests_module.post = fake_post

        source_response = {
            "status_code": 200,
            "text": (
                "<html><body><h1>Regulation (EU) 2024/2847</h1>"
                "<h2>Article 13</h2><p>Article 13(8)</p>"
                "<p>Manufacturers shall ensure that vulnerabilities of the product "
                "with digital elements, including its components, are handled "
                "effectively during the support period.</p></body></html>"
            ),
        }

        def fake_get(url, *, headers=None, timeout=None, **kwargs):
            captured["source_gets"].append({
                "url": url, "timeout": timeout, "headers": headers,
            })
            spec = source_response
            if isinstance(spec, BaseException):
                raise spec
            return FakeResponse(
                status_code=spec.get("status_code", 200),
                text=spec.get("text", ""),
                body=spec.get("json", {}),
            )

        requests_module.get = fake_get
        requests_module.Timeout = Timeout
        requests_module.ConnectionError = ConnectionError
        requests_module.exceptions = exception_types

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

        if source_response_override is not None:
            source_response.update(source_response_override)

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
        exception_types=exception_types,
    )
