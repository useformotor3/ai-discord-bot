"""외부 서비스가 실제로 호출되지 않는 main.py 격리 실행 fixture."""
from pathlib import Path
import runpy
import subprocess
import sys
import time
import types
from types import SimpleNamespace

import pytest
import cra_source


FAKE_ARTICLE_13_8_QUOTE = (
    "Manufacturers shall ensure, when placing a product with digital elements on the market, "
    "and for the support period, that vulnerabilities of that product, including its components, "
    "are handled effectively and in accordance with the essential cybersecurity requirements "
    "set out in Part II of Annex I."
)
FAKE_CRA_SOURCE_TEXT = "\n".join([
    "Article 13",
    "Obligations of manufacturers",
    "8.",
    FAKE_ARTICLE_13_8_QUOTE,
    "9.",
    "Manufacturers shall ensure that each security update remains available after it has been issued.",
    "Article 14",
    "Reporting obligations of manufacturers",
    "1.",
    "A manufacturer shall notify any actively exploited vulnerability.",
    "ANNEX I",
    "ESSENTIAL CYBERSECURITY REQUIREMENTS",
    "Part I",
    "(1)",
    "Products with digital elements shall be designed and developed securely.",
    "(2)",
    "The product with digital elements shall protect the availability, authenticity, integrity and confidentiality of data.",
    "(a)",
    "The product shall protect stored data.",
    "(b)",
    "The product shall prevent unauthorized access to user data.",
    "(f)",
    "The product shall protect the integrity of commands and configuration data.",
    "(g)",
    "The product shall log security-relevant events.",
    "Part II",
    "(5)",
    "Manufacturers shall have appropriate policies and procedures, including coordinated vulnerability disclosure policies.",
    "(6)",
    "Manufacturers shall facilitate the sharing of information about potential vulnerabilities.",
])
FAKE_SOURCE_PACK = {
    "version": "fixture-source-pack-v1",
    "retrieved_at": "2026-11-17T00:00:00+00:00",
    "sources": [
        {
            "id": "CRA-2024-2847-consolidated",
            "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120",
            "final_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120",
            "version": "Fixture Regulation (EU) 2024/2847 consolidated text",
            "text": FAKE_CRA_SOURCE_TEXT,
            "sha256": "fixture-sha256-cra",
            "full_text_sha256": "fixture-full-sha-cra",
            "prompt_excerpt_sha256": "fixture-prompt-sha-cra",
            "retrieved_at": "2026-11-17T00:00:00+00:00",
        },
        {
            "id": "CRA-COMMISSION-GUIDANCE-2026-07-27",
            "url": "https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation",
            "final_url": "https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation",
            "version": "Fixture Commission guidance publication page",
            "text": (
                "Commission guidance C(2026) 5252 was published on 27 July 2026. "
                "Today's guidance - though non-binding - includes practical examples "
                "and discusses remote data processing solutions."
            ),
            "sha256": "fixture-sha256-guidance",
            "full_text_sha256": "fixture-full-sha-guidance",
            "prompt_excerpt_sha256": "fixture-prompt-sha-guidance",
            "retrieved_at": "2026-11-17T00:00:00+00:00",
        },
    ],
    "text": (
        "[CRA-2024-2847-consolidated]\n" + FAKE_CRA_SOURCE_TEXT
        + "\n[CRA-COMMISSION-GUIDANCE-2026-07-27]\n"
        + "Commission guidance C(2026) 5252 was published on 27 July 2026. "
        + "Today's guidance - though non-binding - includes practical examples "
        + "and discusses remote data processing solutions."
    ),
}


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
        source_result=None,
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

        def fake_source_fetch():
            if isinstance(source_result, BaseException):
                raise source_result
            return source_result if source_result is not None else FAKE_SOURCE_PACK

        monkeypatch.setattr(cra_source, "fetch_official_cra_source", fake_source_fetch)
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
        exception_types=exception_types,
    )
