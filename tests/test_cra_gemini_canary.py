import json

import pytest

from scripts.cra_gemini_canary import (
    ENDPOINT,
    MODEL,
    SYNTHETIC_QUOTE,
    run_canary,
)


class FakeResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return self.payload


def response_payload(quote=SYNTHETIC_QUOTE):
    claim = {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "statement": "Synthetic canary statement for JSON contract validation.",
        "source_id": "CANARY-SYNTHETIC",
        "locator": "Article 1",
        "quote": quote,
    }
    return {
        "candidates": [{
            "content": {
                "parts": [{
                    "text": json.dumps({"claims": [claim]}),
                }]
            }
        }],
        "usageMetadata": {
            "promptTokenCount": 100,
            "candidatesTokenCount": 40,
        },
    }


def test_canary_sends_one_synthetic_request_and_validates_json():
    captured = {}

    def fake_opener(request, timeout):
        captured["url"] = request.full_url
        captured["headers"] = request.headers
        captured["body"] = json.loads(request.data.decode("utf-8"))
        captured["timeout"] = timeout
        return FakeResponse(response_payload())

    result = run_canary("TEST_ONLY_NOT_A_REAL_KEY", opener=fake_opener)

    assert result == {
        "model": MODEL,
        "claim_id": "C-001",
        "prompt_tokens": 100,
        "output_tokens": 40,
    }
    assert captured["url"] == ENDPOINT
    assert captured["headers"]["X-goog-api-key"] == "TEST_ONLY_NOT_A_REAL_KEY"
    assert captured["timeout"] == 20
    assert "tools" not in captured["body"]
    assert captured["body"]["generationConfig"]["maxOutputTokens"] == 256
    assert SYNTHETIC_QUOTE in captured["body"]["contents"][0]["parts"][0]["text"]


def test_canary_rejects_missing_key_without_network_call():
    def should_not_run(*args, **kwargs):
        raise AssertionError("network must not be called")

    with pytest.raises(RuntimeError, match="GEMINI_API_KEY"):
        run_canary("", opener=should_not_run)


def test_canary_rejects_quote_not_matching_synthetic_source():
    def fake_opener(request, timeout):
        return FakeResponse(response_payload("This is not the source quote."))

    with pytest.raises(RuntimeError, match="does not match"):
        run_canary("TEST_ONLY_NOT_A_REAL_KEY", opener=fake_opener)


def test_canary_rejects_invalid_json_response_text():
    payload = {
        "candidates": [{
            "content": {"parts": [{"text": "not json"}]}
        }]
    }

    def fake_opener(request, timeout):
        return FakeResponse(payload)

    with pytest.raises(RuntimeError, match="plain JSON"):
        run_canary("TEST_ONLY_NOT_A_REAL_KEY", opener=fake_opener)
