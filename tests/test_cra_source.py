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
            "<p>Article 64</p><p>Penalties</p><p>10.</p>"
            "<p>By way of derogation from paragraphs 3 to 9, the administrative fines do not apply.</p>"
            "<p>Article 65</p><p>Representative actions</p>"
            "<p>Article 67</p><p>Amendment to Directive (EU) 2020/1828</p><p>1.</p>"
            "<p>In Annex I, point 69. Regulation (EU) 2024/2847 is added.</p>"
            "<p>Article 68</p><p>Amendment to Regulation (EU) No 168/2013</p>"
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
    assert "CRA-2025-2392-important-critical-product-descriptions" in ids


def test_guidance_publication_page_uses_page_markers_not_pdf_document_number():
    guidance = next(
        item for item in CRA_SOURCE_CATALOG
        if item["id"] == "CRA-COMMISSION-GUIDANCE-2026-07-27"
    )
    assert "C(2026) 5252" not in guidance["required"]
    assert "27 July 2026" in guidance["required"]
    assert "remote data processing solutions" in guidance["required"]
    assert "cra_pdf_sources.py" in guidance["related_note"]


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

    assert len(calls) == len(CRA_SOURCE_CATALOG) == 10
    assert len(source["sources"]) == 10
    assert "CRA-COMMISSION-GUIDANCE-2026-07-27" in source["text"]
    assert "CRA-M606-STANDARDISATION-2026-11-12" in source["text"]
    assert "CRA-2025-2392-important-critical-product-descriptions" in source["text"]
    implementing = next(
        item for item in source["sources"]
        if item["id"] == "CRA-2025-2392-important-critical-product-descriptions"
    )
    assert "Physical and virtual network interfaces" in implementing["text"]
    assert "Hardware Devices with Security Boxes" in implementing["text"]
    consolidated = next(item for item in source["sources"] if item["id"] == "CRA-2024-2847-consolidated")
    assert "paragraphs 2 to 9" in consolidated["text"]
    assert "paragraphs 3 to 9" not in consolidated["text"]
    assert "72. Regulation (EU) 2024/2847" in consolidated["text"]
    assert "69. Regulation (EU) 2024/2847" not in consolidated["text"]
    assert "Official corrigenda applied/verified in prompt excerpt" in source["text"]
    assert len(consolidated["applied_corrigenda"]) == 2
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



def test_cellar_http_redirect_is_upgraded_to_https_before_following():
    calls = []

    class FakeResponse:
        def __init__(self, status_code, url, headers=None, text=""):
            self.status_code = status_code
            self.url = url
            self.headers = headers or {}
            self.text = text

        def raise_for_status(self):
            return None

    class FakeRequests:
        def __init__(self):
            self.responses = [
                FakeResponse(
                    302,
                    "https://publications.europa.eu/resource/celex/02024R2847-20241120?language=eng",
                    {"Location": "http://publications.europa.eu/resource/cellar/test/DOC_1"},
                ),
                FakeResponse(
                    200,
                    "https://publications.europa.eu/resource/cellar/test/DOC_1",
                    text="<html><body>official legal content</body></html>",
                ),
            ]

        def get(self, url, **kwargs):
            calls.append((url, kwargs.get("allow_redirects")))
            return self.responses.pop(0)

    response, final_url = cra_source._request_with_safe_redirects(
        FakeRequests(),
        {
            "id": "CRA-test",
            "url": "https://publications.europa.eu/resource/celex/test?language=eng",
            "allowed_hosts": ("publications.europa.eu",),
        },
    )

    assert calls == [
        ("https://publications.europa.eu/resource/celex/test?language=eng", False),
        ("https://publications.europa.eu/resource/cellar/test/DOC_1", False),
    ]
    assert response.status_code == 200
    assert final_url.startswith("https://")


def test_official_source_redirect_to_unapproved_host_is_rejected():
    class FakeResponse:
        status_code = 302
        url = "https://publications.europa.eu/resource/celex/test"
        headers = {"Location": "https://example.invalid/fake"}

    class FakeRequests:
        def get(self, url, **kwargs):
            return FakeResponse()

    with pytest.raises(SourceValidationError, match="허용되지 않은 공식 source 리디렉션"):
        cra_source._request_with_safe_redirects(
            FakeRequests(),
            {
                "id": "CRA-test",
                "url": "https://publications.europa.eu/resource/celex/test",
                "allowed_hosts": ("publications.europa.eu",),
            },
        )



def test_required_source_markers_match_across_formex_line_breaks():
    text = "On page 66, in Article 67:\nfor:\n‘69.\nRegulation (EU) 2024/2847’\nread:\n‘72.\nRegulation (EU) 2024/2847’"

    assert cra_source._missing_required_markers(
        text,
        ["Article 67", "69. Regulation", "72. Regulation"],
    ) == []



def _corrigenda_fixture(base_article_64, base_article_67):
    return [
        {
            "id": "CRA-2024-2847-consolidated",
            "full_text_sha256": "raw-base-sha256",
            "text": "\n".join([
                "Article 64",
                "Penalties",
                "10.",
                base_article_64,
                "Article 65",
                "Representative actions",
                "Article 67",
                "Amendment to Directive (EU) 2020/1828",
                "1.",
                base_article_67,
                "Article 68",
                "Amendment to Regulation (EU) No 168/2013",
            ]),
        },
        {
            "id": "CRA-2024-2847-corrigendum-2025-07-02",
            "text": (
                "Page 65, Article 64(10), for: paragraphs 3 to 9, "
                "read: paragraphs 2 to 9."
            ),
        },
        {
            "id": "CRA-2024-2847-corrigendum-2025-10-17",
            "text": (
                "Page 66, Article 67, for: 69. Regulation (EU) 2024/2847, "
                "read: 72. Regulation (EU) 2024/2847."
            ),
        },
    ]


def test_consolidated_source_applies_both_operative_english_corrigenda():
    source_items = _corrigenda_fixture(
        "By way of derogation from paragraphs 3 to 9, the administrative fines do not apply.",
        "In Annex I, point 69. Regulation (EU) 2024/2847 is added.",
    )

    applied = cra_source.apply_consolidated_cra_corrigenda(source_items)
    base = source_items[0]

    assert applied == [
        "CRA-2024-2847-corrigendum-2025-07-02",
        "CRA-2024-2847-corrigendum-2025-10-17",
    ]
    assert "paragraphs 2 to 9" in base["text"]
    assert "paragraphs 3 to 9" not in base["text"]
    assert "72. Regulation (EU) 2024/2847" in base["text"]
    assert "69. Regulation (EU) 2024/2847" not in base["text"]
    assert base["applied_corrigenda"] == applied
    assert base["full_text_sha256"] == "raw-base-sha256"
    assert base["prompt_excerpt_sha256"] == cra_source.hashlib.sha256(
        base["text"].encode("utf-8")
    ).hexdigest()
    assert cra_source.validate_consolidated_cra_corrections(source_items)


def test_consolidated_source_keeps_already_corrected_text_without_reapplying():
    source_items = _corrigenda_fixture(
        "By way of derogation from paragraphs 2 to 9, the administrative fines do not apply.",
        "In Annex I, point 72. Regulation (EU) 2024/2847 is added.",
    )

    cra_source.apply_consolidated_cra_corrigenda(source_items)
    before = source_items[0]["text"]
    cra_source.apply_consolidated_cra_corrigenda(source_items)

    assert source_items[0]["text"] == before


def test_consolidated_source_rejects_missing_operative_corrigendum_source():
    source_items = _corrigenda_fixture(
        "By way of derogation from paragraphs 3 to 9, the administrative fines do not apply.",
        "In Annex I, point 69. Regulation (EU) 2024/2847 is added.",
    )
    source_items.pop()

    with pytest.raises(SourceValidationError, match="정오표 2건이 모두 필요"):
        cra_source.apply_consolidated_cra_corrigenda(source_items)
