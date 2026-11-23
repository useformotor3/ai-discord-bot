import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest
import requests

import cra_pdf_sources as pdf


class FakePage:
    def __init__(self, text):
        self.text = text

    def extract_text(self):
        return self.text


class FakeReader:
    def __init__(self, _stream, strict=True):
        self.pages = [FakePage(
            ("C(2026) 5252 final This guidance is not binding data connection "
             "remote data processing C/2026/6013 Cyber Resilience Act "             "remote data processing COMMISSION IMPLEMENTING DECISION "
             "C(2026) 7861 final European standard 31/01/2027 Version: V 2.0 Date: 2026-06-03 M/606 Publication forecast ") * 5
        )]
        self.is_encrypted = False


class FakeResponse:
    def __init__(self, *, status=200, url, body=b"%PDF-1.7\nfixture", content_type="application/pdf"):
        self.status_code = status
        self.url = url
        self.headers = {"Content-Type": content_type}
        self._body = body

    def iter_content(self, chunk_size=65536):
        yield self._body


def test_fetch_pdf_source_records_binary_hash_and_page_count():
    definition = next(item for item in pdf.PDF_SOURCE_CATALOG if item["id"] == "CRA-M606-C2026-7861-ANNEX")
    response = FakeResponse(url=definition["url"])
    with patch.object(pdf, "PdfReader", FakeReader):
        item = pdf.fetch_pdf_source(definition, get=lambda *a, **k: response)
    assert item["id"] == "CRA-M606-C2026-7861-ANNEX"
    assert item["byte_count"] == len(response._body)
    assert item["sha256"] == hashlib.sha256(response._body).hexdigest()
    assert item["page_count"] == 1
    assert item["fallback_used"] is False


def test_guidance_primary_non_pdf_uses_only_allowlisted_anfr_mirror():
    definition = pdf.PDF_SOURCE_CATALOG[0]
    responses = iter([
        FakeResponse(url=definition["url"], body=b"<html>not a PDF</html>", content_type="text/html"),
        FakeResponse(url=definition["fallback_url"]),
    ])
    with patch.object(pdf, "PdfReader", FakeReader):
        item = pdf.fetch_pdf_source(definition, get=lambda *a, **k: next(responses))
    assert item["fallback_used"] is True
    assert item["final_url"] == definition["fallback_url"]


def test_official_commission_sorry_interstitial_uses_allowlisted_anfr_mirror():
    definition = pdf.PDF_SOURCE_CATALOG[0]
    responses = iter([
        FakeResponse(
            url="https://sorry.ec.europa.eu/",
            body=b"<html>Commission automated access interstitial</html>",
            content_type="text/html",
        ),
        FakeResponse(url=definition["fallback_url"]),
    ])
    with patch.object(pdf, "PdfReader", FakeReader):
        item = pdf.fetch_pdf_source(definition, get=lambda *a, **k: next(responses))
    assert item["fallback_used"] is True
    assert item["final_url"] == definition["fallback_url"]


def test_untrusted_redirect_fails_closed_without_mirror_fallback():
    definition = pdf.PDF_SOURCE_CATALOG[0]
    response = FakeResponse(url="https://evil.example/document.pdf")
    with patch.object(pdf, "PdfReader", FakeReader):
        with pytest.raises(pdf.PDFSourceValidationError, match="non-allowlisted host"):
            pdf.fetch_pdf_source(definition, get=lambda *a, **k: response)


def test_temporary_http_outage_is_distinguished_from_validation_failure():
    definition = next(item for item in pdf.PDF_SOURCE_CATALOG if item["id"] == "CRA-M606-C2026-7861-ANNEX")
    response = FakeResponse(status=503, url=definition["url"])
    with pytest.raises(pdf.PDFSourceUnavailableError, match="temporary HTTP status"):
        pdf.fetch_pdf_source(definition, get=lambda *a, **k: response)


def test_missing_document_identity_marker_fails_validation():
    definition = next(item for item in pdf.PDF_SOURCE_CATALOG if item["id"] == "CRA-M606-C2026-7861-ANNEX")
    response = FakeResponse(url=definition["url"])

    class WrongReader:
        def __init__(self, _stream, strict=True):
            self.pages = [FakePage("unrelated document with enough text " * 30)]
            self.is_encrypted = False

    with patch.object(pdf, "PdfReader", WrongReader):
        with pytest.raises(pdf.PDFSourceValidationError, match="identity markers missing"):
            pdf.fetch_pdf_source(definition, get=lambda *a, **k: response)


def test_fetch_all_writes_pdf_text_and_manifest(tmp_path):
    responses = iter([
        FakeResponse(url=pdf.PDF_SOURCE_CATALOG[0]["url"]),
        FakeResponse(url=pdf.PDF_SOURCE_CATALOG[1]["url"]),
        FakeResponse(url=pdf.PDF_SOURCE_CATALOG[2]["url"]),
    ])
    with patch.object(pdf, "PdfReader", FakeReader):
        results = pdf.fetch_all_pdf_sources(
            tmp_path,
            get=lambda *a, **k: next(responses),
        )
    assert len(results) == 3
    assert (tmp_path / "C2026_5252_guidance_annex.pdf").read_bytes().startswith(b"%PDF-")
    assert (tmp_path / "C_2026_6013_cra_guidance_oj.pdf").read_bytes().startswith(b"%PDF-")
    assert (tmp_path / "C2026_7861_m606_annex.pdf.txt").exists()
    manifest = json.loads((tmp_path / "manifest.json").read_text(encoding="utf-8"))
    assert len(manifest) == 3
    assert all(len(item["sha256"]) == 64 for item in manifest)

def test_guidance_oj_c6013_is_fetched_from_eurlex_primary_without_fallback():
    definition = next(
        item for item in pdf.PDF_SOURCE_CATALOG
        if item["id"] == "CRA-GUIDANCE-OJ-2026-6013"
    )
    response = FakeResponse(url=definition["url"])
    with patch.object(pdf, "PdfReader", FakeReader):
        item = pdf.fetch_pdf_source(definition, get=lambda *a, **k: response)
    assert item["id"] == "CRA-GUIDANCE-OJ-2026-6013"
    assert definition["url"] == "https://publications.europa.eu/resource/cellar/dcbc848b-e227-11f1-aefc-01aa75ed71a1.0006.01/DOC_1"
    assert definition["allowed_hosts"] == ("publications.europa.eu",)
    assert item["fallback_used"] is False
    assert item["final_url"] == definition["url"]

