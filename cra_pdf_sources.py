"""Fetch and hash CRA Commission PDF source documents.

This is a read-only source acquisition tool. It never changes project runtime state.
PDF text extraction is used only for source verification and locator checks.
"""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
from urllib.parse import urlparse

import requests
from pypdf import PdfReader


TIMEOUT = (5, 30)
MAX_BYTES = 25 * 1024 * 1024


class PDFSourceUnavailableError(RuntimeError):
    """Temporary network/source outage; caller may safely skip the live canary."""


class PDFSourceValidationError(RuntimeError):
    """Unexpected redirect, document identity or PDF structure."""


class PDFSourceFallbackError(PDFSourceValidationError):
    """Primary source is unavailable/non-PDF; an explicitly allowlisted mirror may be tried."""


PDF_SOURCE_CATALOG = (
    {
        "id": "CRA-GUIDANCE-2026-5252",
        "filename": "C2026_5252_guidance_annex.pdf",
        "url": "https://ec.europa.eu/newsroom/dae/redirection/document/131456",
        "allowed_hosts": ("ec.europa.eu",),
        "fallback_url": "https://www.anfr.fr/fileadmin/CRA/Commission_guidance_on_the_application_of_Regulation__EU__20242847__Cyber_Resilience_Act_.pdf",
        "fallback_allowed_hosts": ("www.anfr.fr", "anfr.fr"),
        "required_markers": (
            "C(2026) 5252 final",
            "This guidance is not binding",
            "data connection",
            "remote data processing",
        ),
    },
    {
        "id": "CRA-GUIDANCE-OJ-2026-6013",
        "filename": "C_2026_6013_cra_guidance_oj.pdf",
        "url": "https://publications.europa.eu/resource/cellar/dcbc848b-e227-11f1-aefc-01aa75ed71a1.0006.01/DOC_1",
        "allowed_hosts": ("publications.europa.eu",),
        "required_markers": (
            "C/2026/6013",
            "Cyber Resilience Act",
            "remote data processing",
        ),
    },
    {
        "id": "CRA-M606-C2026-7861-ANNEX",
        "filename": "C2026_7861_m606_annex.pdf",
        "url": "https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401",
        "allowed_hosts": ("ec.europa.eu",),
        "required_markers": (
            "C(2026) 7861 final",
            "COMMISSION IMPLEMENTING DECISION",
            "European standard",
            "31/01/2027",
        ),
    },
)


def _download(url, allowed_hosts, *, get=None):
    get = get or requests.get
    try:
        response = get(url, timeout=TIMEOUT, allow_redirects=True, stream=True)
    except (requests.Timeout, requests.ConnectionError) as exc:
        raise PDFSourceUnavailableError(f"PDF source network failure: {url}: {exc}") from exc

    status = int(getattr(response, "status_code", 0) or 0)
    if status in (408, 425, 429) or status >= 500:
        raise PDFSourceUnavailableError(
            f"PDF source temporary HTTP status {status}: {url}"
        )
    if status in (401, 403, 404):
        raise PDFSourceFallbackError(f"PDF source unavailable at primary URL (HTTP {status}): {url}")
    if status < 200 or status >= 300:
        raise PDFSourceValidationError(f"PDF source HTTP status {status}: {url}")

    final_url = getattr(response, "url", "") or url
    parsed = urlparse(final_url)
    # The Commission document service may redirect automated requests to
    # its anti-bot interstitial. Never parse that page as a PDF. The caller
    # may use only a source definition's explicit allowlisted fallback;
    # without one, the document is recorded as unavailable.
    if parsed.scheme == "https" and parsed.hostname == "sorry.ec.europa.eu":
        raise PDFSourceUnavailableError(
            "Commission document service redirected to its official anti-bot/interstitial host; "
            "no trusted PDF response is available to this unauthenticated runner"
        )
    if parsed.scheme != "https" or parsed.hostname not in allowed_hosts:
        raise PDFSourceValidationError(
            f"PDF source redirected to a non-allowlisted host: {final_url}"
        )

    content_type = str(getattr(response, "headers", {}).get("Content-Type", "")).lower()
    chunks = []
    total = 0
    try:
        iterator = response.iter_content(chunk_size=64 * 1024)
        for chunk in iterator:
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise PDFSourceValidationError(
                    f"PDF source exceeds the {MAX_BYTES}-byte safety limit: {final_url}"
                )
            chunks.append(chunk)
    except (requests.Timeout, requests.ConnectionError) as exc:
        raise PDFSourceUnavailableError(
            f"PDF source interrupted while downloading: {final_url}: {exc}"
        ) from exc
    data = b"".join(chunks)
    if not data:
        raise PDFSourceUnavailableError(f"PDF source returned an empty body: {final_url}")
    if not data.startswith(b"%PDF-"):
        raise PDFSourceFallbackError(
            f"PDF magic header missing (Content-Type={content_type or 'unknown'}): {final_url}"
        )
    return data, final_url, content_type


def _extract_pdf_text(data, source_id):
    try:
        reader = PdfReader(BytesIO(data), strict=True)
        if getattr(reader, "is_encrypted", False):
            if reader.decrypt("") == 0:
                raise PDFSourceValidationError(f"Encrypted PDF cannot be opened: {source_id}")
        pages = list(reader.pages)
        if not pages or len(pages) > 300:
            raise PDFSourceValidationError(
                f"Unexpected PDF page count for {source_id}: {len(pages)}"
            )
        text = "\n".join((page.extract_text() or "") for page in pages)
    except PDFSourceValidationError:
        raise
    except Exception as exc:
        raise PDFSourceValidationError(
            f"PDF parsing failed for {source_id}: {type(exc).__name__}: {exc}"
        ) from exc
    if len(text.strip()) < 500:
        raise PDFSourceValidationError(
            f"PDF text layer is unexpectedly short for {source_id}: {len(text)} chars"
        )
    return text, len(pages)


def fetch_pdf_source(definition, *, get=None):
    requested_url = definition["url"]
    fallback_used = False
    try:
        data, final_url, content_type = _download(
            requested_url, definition["allowed_hosts"], get=get
        )
    except PDFSourceUnavailableError:
        if not definition.get("fallback_url"):
            raise
        data, final_url, content_type = _download(
            definition["fallback_url"],
            definition["fallback_allowed_hosts"],
            get=get,
        )
        fallback_used = True
    except PDFSourceFallbackError:
        if not definition.get("fallback_url"):
            raise
        data, final_url, content_type = _download(
            definition["fallback_url"],
            definition["fallback_allowed_hosts"],
            get=get,
        )
        fallback_used = True

    text, page_count = _extract_pdf_text(data, definition["id"])
    missing = [
        marker for marker in definition["required_markers"]
        if re.search(re.escape(marker), text, re.IGNORECASE) is None
    ]
    if missing:
        raise PDFSourceValidationError(
            f"PDF identity markers missing for {definition['id']}: {', '.join(missing)}"
        )

    return {
        "id": definition["id"],
        "requested_url": requested_url,
        "final_url": final_url,
        "fallback_used": fallback_used,
        "content_type": content_type,
        "byte_count": len(data),
        "sha256": sha256(data).hexdigest(),
        "page_count": page_count,
        "extracted_text_chars": len(text),
        "text_sha256": sha256(text.encode("utf-8")).hexdigest(),
        "required_markers": list(definition["required_markers"]),
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "bytes": data,
        "text": text,
    }


def fetch_all_pdf_sources(output_dir=None, *, get=None):
    results = [
        fetch_pdf_source(definition, get=get)
        for definition in PDF_SOURCE_CATALOG
    ]
    if output_dir is not None:
        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)
        manifest = []
        for definition, item in zip(PDF_SOURCE_CATALOG, results):
            (output / definition["filename"]).write_bytes(item["bytes"])
            (output / (definition["filename"] + ".txt")).write_text(
                item["text"], encoding="utf-8"
            )
            manifest.append({
                key: value for key, value in item.items()
                if key not in ("bytes", "text")
            })
        (output / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="artifacts/cra-pdf-sources")
    args = parser.parse_args(argv)
    try:
        results = fetch_all_pdf_sources(args.output_dir)
    except PDFSourceUnavailableError as exc:
        print(f"SKIPPED: temporary CRA PDF source outage: {exc}")
        return 0
    for item in results:
        print(
            "PASS: {id} bytes={byte_count} pages={page_count} "
            "sha256={sha256} fallback={fallback_used}".format(**item)
        )
    print(f"PASS: fetched and hashed {len(results)} CRA Commission PDF sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
