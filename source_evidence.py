"""Phase A: curated official-source registry and guarded, testable fetcher.

No production workflow imports this module yet. Fetching is opt-in by source_id;
callers cannot supply arbitrary URLs. Network behavior is injectable for tests.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
import ipaddress
import socket
from typing import Callable, Iterable
from types import MappingProxyType
from urllib.parse import urljoin, urlsplit

from source_transport import PinnedHTTPSession, PinnedTransportError, normalize_public_ips

DEFAULT_TIMEOUT = (5.0, 20.0)
DEFAULT_MAX_REDIRECTS = 3
DEFAULT_CHUNK_SIZE = 64 * 1024
EXTRACTION_METHOD = "NONE_PHASE_A_RAW_BYTES_ONLY"


@dataclass(frozen=True)
class SourceDefinition:
    source_id: str
    canonical_url: str
    publisher: str
    title: str
    document_identifier: str
    revision: str
    expected_mime_types: tuple[str, ...]
    max_bytes: int


# Exact URLs and hostnames are curated in code review. Model output is never accepted here.
SOURCE_REGISTRY = MappingProxyType({
    item.source_id: item
    for item in (
        SourceDefinition(
            "CRA_EURLEX_2024_2847",
            "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847",
            "European Union",
            "Regulation (EU) 2024/2847",
            "CELEX:32024R2847",
            "2024",
            ("text/html", "application/xhtml+xml", "application/xml", "text/xml"),
            5 * 1024 * 1024,
        ),
        SourceDefinition(
            "ST_AN5156_REV14",
            "https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html",
            "STMicroelectronics",
            "Introduction to security for STM32 MCUs",
            "AN5156",
            "Rev 14 (June 2026)",
            ("text/html", "application/xhtml+xml"),
            5 * 1024 * 1024,
        ),
        SourceDefinition(
            "ST_AN4992_REV19",
            "https://www.st.com/content/st_com/en/technical-documents/an4992-introduction-to-secure-firmware-install-sfi-for-stm32-mcus-stmicroelectronics.html",
            "STMicroelectronics",
            "Introduction to Secure Firmware Install (SFI) for STM32 MCUs",
            "AN4992",
            "Rev 19 (July 2026)",
            ("text/html", "application/xhtml+xml"),
            5 * 1024 * 1024,
        ),
        SourceDefinition(
            "ST_AN5447_REV3",
            "https://www.st.com/content/st_com/en/technical-documents/an5447-overview-of-secure-boot-and-secure-firmware-update-solution-on-arm-trustzone-stm32-microcontrollers-stmicroelectronics.html",
            "STMicroelectronics",
            "Overview of secure boot and secure firmware update solution",
            "AN5447",
            "Rev 3 (August 2021)",
            ("text/html", "application/xhtml+xml"),
            5 * 1024 * 1024,
        ),
        SourceDefinition(
            "TI_MSPM0G3529_Q1_DATASHEET",
            "https://www.ti.com/lit/ds/symlink/mspm0g3529-q1.pdf",
            "Texas Instruments",
            "MSPM0G3529-Q1 data sheet",
            "SLASFO2B",
            "Rev B (revised October 2025)",
            ("application/pdf",),
            20 * 1024 * 1024,
        ),
        SourceDefinition(
            "TI_SLAAE29A_REV_A",
            "https://www.ti.com/lit/an/slaae29a/slaae29a.pdf",
            "Texas Instruments",
            "Cybersecurity Enablers in MSPM0 MCUs",
            "SLAAE29A",
            "Rev A (December 2025)",
            ("application/pdf",),
            20 * 1024 * 1024,
        ),
        SourceDefinition(
            "TI_SFFS983A_REV_A",
            "https://www.ti.com/document-viewer/lit/html/SFFS983A",
            "Texas Instruments",
            "Functional Safety Manual for MSPM0Gx51x and MSPM0Gx52x",
            "SFFS983A",
            "Rev A (October 30, 2026)",
            ("text/html", "application/xhtml+xml"),
            5 * 1024 * 1024,
        ),
    )
})

ALLOWED_HOSTS = frozenset(urlsplit(item.canonical_url).hostname for item in SOURCE_REGISTRY.values())


class SourceFetchError(RuntimeError):
    """A source could not be fetched without violating a safety or integrity check."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class FetchMetadata:
    source_id: str
    canonical_url: str
    final_url: str
    publisher: str
    title: str
    document_identifier: str
    revision: str
    published_or_revision_date: str
    fetched_at_utc: str
    http_status: int
    mime_type: str
    byte_count: int
    sha256: str
    extraction_method: str
    status: str
    error_code: str = ""

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class FetchResult:
    metadata: FetchMetadata
    content: bytes  # In-memory only; callers must not publish full manufacturer documents.


def _default_resolver(host: str) -> Iterable[str]:
    return {entry[4][0] for entry in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)}


def _validate_https_target(url: str, expected_host: str, resolver: Callable[[str], Iterable[str]]) -> tuple[str, ...]:
    parsed = urlsplit(url)
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise SourceFetchError("HTTPS_REQUIRED")
    if parsed.username is not None or parsed.password is not None:
        raise SourceFetchError("CREDENTIAL_URL_BLOCKED")
    if parsed.hostname.lower() != expected_host.lower():
        raise SourceFetchError("REDIRECT_HOST_BLOCKED")
    if parsed.port not in (None, 443):
        raise SourceFetchError("NONSTANDARD_PORT_BLOCKED")
    if parsed.fragment:
        raise SourceFetchError("URL_FRAGMENT_BLOCKED")
    try:
        # Resolve once per hop. The returned literal IPs are passed to the
        # transport; the transport never performs a second hostname lookup.
        return normalize_public_ips(resolver(parsed.hostname))
    except PinnedTransportError as exc:
        raise SourceFetchError(str(exc)) from exc
    except Exception as exc:
        raise SourceFetchError("DNS_RESOLUTION_FAILED") from exc


def _read_limited(response: object, limit: int, chunk_size: int) -> bytes:
    headers = getattr(response, "headers", {})
    content_length = headers.get("Content-Length")
    if content_length is None:
        content_length = headers.get("content-length")
    if content_length is not None:
        try:
            normalized_length = str(content_length).strip()
            if not normalized_length or not normalized_length.isdecimal():
                raise ValueError("invalid content length")
            declared_length = int(normalized_length)
        except (TypeError, ValueError) as exc:
            raise SourceFetchError("INVALID_CONTENT_LENGTH") from exc
        if declared_length > limit:
            raise SourceFetchError("RESPONSE_TOO_LARGE")

    chunks: list[bytes] = []
    total = 0
    iterator = getattr(response, "iter_content", None)
    if callable(iterator):
        parts = iterator(chunk_size=chunk_size)
    else:
        parts = (getattr(response, "content", b""),)
    for part in parts:
        if not part:
            continue
        total += len(part)
        if total > limit:
            raise SourceFetchError("RESPONSE_TOO_LARGE")
        chunks.append(bytes(part))
    return b"".join(chunks)


class OfficialSourceFetcher:
    """Fetch only registered source IDs, with strict HTTPS/host/DNS/redirect/MIME/size gates."""

    def __init__(
        self,
        session: object | None = None,
        *,
        resolver: Callable[[str], Iterable[str]] = _default_resolver,
        clock: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        max_redirects: int = DEFAULT_MAX_REDIRECTS,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
    ):
        if session is None:
            # No hostname-based HTTP client: this adapter connects only to the
            # validated literal IPs while preserving TLS SNI/certificate hostname.
            session = PinnedHTTPSession()
        self.session = session
        self.resolver = resolver
        self.clock = clock
        self.timeout = timeout
        self.max_redirects = max_redirects
        self.chunk_size = chunk_size

    def fetch(self, source_id: str) -> FetchResult:
        source = SOURCE_REGISTRY.get(source_id)
        if source is None:
            raise SourceFetchError("UNKNOWN_SOURCE_ID")
        original = urlsplit(source.canonical_url)
        expected_host = (original.hostname or "").lower()
        current_url = source.canonical_url

        for redirect_count in range(self.max_redirects + 1):
            pinned_ips = _validate_https_target(current_url, expected_host, self.resolver)
            try:
                response = self.session.get(
                    current_url,
                    pinned_ips=pinned_ips,
                    allow_redirects=False,
                    stream=True,
                    timeout=self.timeout,
                    verify=True,
                    headers={"User-Agent": "CRA-Source-Evidence-Fetcher/1.0"},
                )
            except Exception as exc:
                raise SourceFetchError("HTTP_REQUEST_FAILED") from exc

            status = int(getattr(response, "status_code", 0))
            headers = getattr(response, "headers", {})
            if status in (301, 302, 303, 307, 308):
                location = headers.get("Location") or headers.get("location")
                close = getattr(response, "close", None)
                if callable(close):
                    close()
                if not location:
                    raise SourceFetchError("REDIRECT_WITHOUT_LOCATION")
                if redirect_count >= self.max_redirects:
                    raise SourceFetchError("TOO_MANY_REDIRECTS")
                current_url = urljoin(current_url, location)
                continue
            if status != 200:
                close = getattr(response, "close", None)
                if callable(close):
                    close()
                raise SourceFetchError("HTTP_STATUS_NOT_200")

            content_encoding = (headers.get("Content-Encoding") or headers.get("content-encoding") or "identity").strip().lower()
            if content_encoding not in ("", "identity"):
                close = getattr(response, "close", None)
                if callable(close):
                    close()
                raise SourceFetchError("CONTENT_ENCODING_NOT_ALLOWED")

            mime = (headers.get("Content-Type") or headers.get("content-type") or "")
            mime = mime.split(";", 1)[0].strip().lower()
            if mime not in source.expected_mime_types:
                close = getattr(response, "close", None)
                if callable(close):
                    close()
                raise SourceFetchError("MIME_TYPE_NOT_ALLOWED")
            try:
                content = _read_limited(response, source.max_bytes, self.chunk_size)
            finally:
                close = getattr(response, "close", None)
                if callable(close):
                    close()
            if not content:
                raise SourceFetchError("EMPTY_RESPONSE")

            fetched_at = self.clock().astimezone(timezone.utc).isoformat()
            metadata = FetchMetadata(
                source_id=source.source_id,
                canonical_url=source.canonical_url,
                final_url=current_url,
                publisher=source.publisher,
                title=source.title,
                document_identifier=source.document_identifier,
                revision=source.revision,
                published_or_revision_date=source.revision,
                fetched_at_utc=fetched_at,
                http_status=status,
                mime_type=mime,
                byte_count=len(content),
                sha256=sha256(content).hexdigest(),
                extraction_method=EXTRACTION_METHOD,
                status="FETCHED",
            )
            return FetchResult(metadata=metadata, content=content)

        raise SourceFetchError("UNREACHABLE_FETCH_STATE")
