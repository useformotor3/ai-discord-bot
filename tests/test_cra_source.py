from types import SimpleNamespace

import pytest
import requests

import cra_source
from cra_source import (
    CRA_SOURCE_CATALOG,
    SourceUnavailableError,
    SourceValidationError,
    append_source_manifest,
    fetch_official_cra_source,
    validate_source_manifest,
)


def _html_for(definition):
    markers = list(definition["required"])
    if definition["id"] == "CRA-2024-2847-consolidated":
        markers.extend(cra_source.REQUIRED_CORRIGENDA_DATES)
        intro = " ".join(markers)
        operative = (
            "<p>Article 1</p><p>Subject matter</p><p>1.</p>"
            "<p>Article 13</p><p>Obligations of manufacturers</p>"
            "<p>8.</p><p>Manufacturers shall ensure that vulnerabilities are handled effectively.</p>"
            "<p>ANNEX I</p><p>ESSENTIAL CYBERSECURITY REQUIREMENTS</p>"
        )
        return (
            "<html><body><h1>Official source</h1><p>" + intro + "</p>"
            + operative + "<p>" + ("official-source-content " * 2000) + "</p></body></html>"
        )
    if definition.get("extract") == "article_104":
        markers.extend(["Article 104", "CRA Article 32", "26 March 2027", "Article 105"])
    text = " ".join(markers) + " " + ("official-source-content " * 2000)
    return "<html><body><h1>Official source</h1><p>" + text + "</p></body></html>"


def test_normalizer_preserves_block_boundaries_for_locator_validation():
    text = cra_source._extract_visible_text(
        "<html><body><h1>Article 13</h1><p>8.</p>"
        "<p>Manufacturers shall ensure that vulnerabilities are handled effectively.</p>"
        "<p>9.</p><p>Another paragraph.</p></body></html>"
    )
    lines = text.splitlines()
    assert "Article 13" in lines
    assert "8." in lines
    assert "9." in lines


def test_source_catalog_includes_official_guidance_and_m606_pages():
    ids = {item["id"] for item in CRA_SOURCE_CATALOG}
    assert "CRA-COMMISSION-GUIDANCE-2026-07-27" in ids
    assert "CRA-M606-STANDARDISATION-2026-11-12" in ids


def test_fetch_source_pack_checks_each_allowlisted_official_host(monkeypatch):
    calls = []

    class FakeResponse:
        status_code = 200

        def __init__(self, url, text):
            self.url = url
            self.text = text

        def raise_for_status(self):
            return None

    def fake_get(url, **kwargs):
        calls.append(url)
        definition = next(item for item in CRA_SOURCE_CATALOG if item["url"] == url)
        return FakeResponse(url, _html_for(definition))

    monkeypatch.setattr(requests, "get", fake_get)
    source = fetch_official_cra_source()

    assert len(calls) == len(CRA_SOURCE_CATALOG) == 9
    assert len(source["sources"]) == 9
    assert "CRA-COMMISSION-GUIDANCE-2026-07-27" in source["text"]
    assert "CRA-M606-STANDARDISATION-2026-11-12" in source["text"]
    assert all(len(item["full_text_sha256"]) == 64 for item in source["sources"])
    assert all(len(item["prompt_excerpt_sha256"]) == 64 for item in source["sources"])
    assert all(item["retrieved_at"] == source["retrieved_at"] for item in source["sources"])


def test_source_fetch_rejects_redirect_to_non_allowlisted_host(monkeypatch):
    class FakeResponse:
        status_code = 200
        text = "Regulation (EU) 2024/2847 " + "x" * 12000
        url = "https://example.invalid/fake"

        def raise_for_status(self):
            return None

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse())
    with pytest.raises(SourceValidationError, match="허용되지 않은 공식 도메인"):
        fetch_official_cra_source()


def test_source_fetch_transient_http_429_is_a_safe_unavailable_error(monkeypatch):
    error = requests.exceptions.HTTPError("429")
    error.response = SimpleNamespace(status_code=429)

    class FakeResponse:
        status_code = 429
        url = CRA_SOURCE_CATALOG[0]["url"]
        text = ""

        def raise_for_status(self):
            raise error

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse())
    with pytest.raises(SourceUnavailableError, match="일시 HTTP 오류"):
        fetch_official_cra_source()


def test_source_fetch_missing_required_marker_fails_closed(monkeypatch):
    class FakeResponse:
        status_code = 200
        url = CRA_SOURCE_CATALOG[0]["url"]
        text = "Unrelated page " + "x" * 12000

        def raise_for_status(self):
            return None

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse())
    with pytest.raises(SourceValidationError, match="식별자를 확인하지 못했습니다"):
        fetch_official_cra_source()


def test_source_manifest_is_appended_and_every_record_is_verifiable():
    source = {
        "version": "test-version",
        "retrieved_at": "2026-11-17T00:00:00+00:00",
        "sources": [{
            "id": "CRA-test",
            "version": "test source version",
            "url": "https://eur-lex.europa.eu/test",
            "final_url": "https://eur-lex.europa.eu/test",
            "sha256": "abc123",
            "full_text_sha256": "full-abc123",
            "prompt_excerpt_sha256": "excerpt-abc123",
            "retrieved_at": "2026-11-17T00:00:00+00:00",
        }],
    }
    report = append_source_manifest("draft report", source)
    valid, reason = validate_source_manifest(report, source)
    assert valid, reason
    assert "Visible-text SHA-256: full-abc123" in report
    assert "Prompt-excerpt SHA-256: excerpt-abc123" in report



def test_consolidated_cra_excerpt_excludes_recitals_and_keeps_operative_articles():
    source_text = "\n".join([
        "Recital (1)",
        "This is recital text.",
        "Article 1",
        "Subject matter",
        "1.",
        "This Regulation lays down rules.",
        "Article 2",
        "Scope",
        "1.",
        "This Article defines the scope.",
        "ANNEX I",
        "ESSENTIAL CYBERSECURITY REQUIREMENTS",
    ])
    excerpt = cra_source._extract_relevant_excerpt(
        "CRA-2024-2847-consolidated",
        source_text,
    )

    assert "Recital (1)" not in excerpt
    assert excerpt.startswith("Article 1")
    assert "ANNEX I" in excerpt



def test_source_tls_certificate_error_fails_closed(monkeypatch):
    error = requests.exceptions.SSLError("certificate verification failed")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: (_ for _ in ()).throw(error))

    with pytest.raises(SourceValidationError, match="TLS 인증 검증 실패"):
        fetch_official_cra_source()



def test_source_http_202_is_treated_as_temporary_unavailable(monkeypatch):
    class FakeResponse:
        status_code = 202
        url = CRA_SOURCE_CATALOG[0]["url"]
        text = "<html><body>Request accepted for processing</body></html>"
        headers = {"Retry-After": "5"}

        def raise_for_status(self):
            return None

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse())
    with pytest.raises(SourceUnavailableError, match="HTTP 202 비동기 수락"):
        fetch_official_cra_source()
