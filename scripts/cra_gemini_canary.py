"""Opt-in, non-production Gemini JSON compatibility canary.

Sends only a synthetic public test string. Never loads CRA source packs, reports,
repository contents, Discord credentials, or production state.
"""
import json
import os
import re
import urllib.error
import urllib.request


MODEL = "gemini-3.8-flash"
ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    + MODEL
    + ":generateContent"
)
SYNTHETIC_QUOTE = (
    "For this synthetic canary only, the manufacturer shall keep the sample "
    "record available throughout the stated support period."
)


def _normalize(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _extract_text(response_payload):
    candidates = response_payload.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise RuntimeError("Gemini response contains no candidates.")
    content = candidates[0].get("content", {})
    parts = content.get("parts", [])
    text = "".join(
        part.get("text", "")
        for part in parts
        if isinstance(part, dict) and isinstance(part.get("text"), str)
    )
    if not text.strip():
        raise RuntimeError("Gemini response contains no text part.")
    return text.strip()


def _validate_payload(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("claims"), list):
        raise RuntimeError("Gemini JSON response has no claims array.")
    if len(payload["claims"]) != 1:
        raise RuntimeError("Gemini canary must return exactly one synthetic claim.")
    claim = payload["claims"][0]
    if not isinstance(claim, dict):
        raise RuntimeError("Gemini canary claim is not an object.")
    expected = {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "source_id": "CANARY-SYNTHETIC",
        "locator": "Article 1",
    }
    for key, value in expected.items():
        if claim.get(key) != value:
            raise RuntimeError(f"Gemini canary returned an invalid {key}.")
    if not isinstance(claim.get("statement"), str) or len(claim["statement"]) < 10:
        raise RuntimeError("Gemini canary statement is missing or too short.")
    if _normalize(claim.get("quote")) != _normalize(SYNTHETIC_QUOTE):
        raise RuntimeError("Gemini canary quote does not match the synthetic source.")
    return claim


def run_canary(api_key, opener=None):
    """Make one bounded request and validate the expected JSON contract."""
    if not isinstance(api_key, str) or not api_key.strip():
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    if opener is None:
        opener = urllib.request.urlopen

    prompt = f"""
This is a synthetic API compatibility test, not legal research.
Use only the synthetic sentence below. Do not claim it is real law.
Return exactly one JSON object with a claims array and exactly one claim.
The claim fields must be claim_id, category, statement, source_id, locator, quote.
Use claim_id C-001, category legal_requirement, source_id CANARY-SYNTHETIC,
locator Article 1. The quote must copy the synthetic sentence exactly.
Synthetic source sentence:
{SYNTHETIC_QUOTE}
"""
    request_body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0,
            "maxOutputTokens": 256,
            "responseMimeType": "application/json",
        },
    }
    encoded_body = json.dumps(request_body).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=encoded_body,
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    try:
        with opener(request, timeout=20) as response:
            raw_response = response.read()
    except urllib.error.HTTPError as exc:
        raise RuntimeError(
            f"Gemini API returned HTTP {exc.code}; response body omitted."
        ) from None
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Gemini API connection failed: {type(exc.reason).__name__}."
        ) from None

    try:
        response_payload = json.loads(raw_response.decode("utf-8"))
    except (UnicodeError, ValueError):
        raise RuntimeError("Gemini API response is not valid UTF-8 JSON.") from None

    response_text = _extract_text(response_payload)
    try:
        claim_payload = json.loads(response_text)
    except ValueError:
        raise RuntimeError("Gemini did not return a plain JSON claim payload.") from None

    claim = _validate_payload(claim_payload)
    usage = response_payload.get("usageMetadata", {})
    return {
        "model": MODEL,
        "claim_id": claim["claim_id"],
        "prompt_tokens": usage.get("promptTokenCount"),
        "output_tokens": usage.get("candidatesTokenCount"),
    }


def main():
    result = run_canary(os.environ.get("GEMINI_API_KEY"))
    print("PASS: Gemini JSON compatibility canary")
    print(f"Model: {result['model']}")
    print(f"Claim contract: {result['claim_id']}")
    if result["prompt_tokens"] is not None:
        print(f"Prompt tokens: {result['prompt_tokens']}")
    if result["output_tokens"] is not None:
        print(f"Output tokens: {result['output_tokens']}")


if __name__ == "__main__":
    main()
