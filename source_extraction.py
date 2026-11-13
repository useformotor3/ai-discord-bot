"""Phase B source extraction adapters.

Pure parsing only: this module performs no network access and writes no files.
All extracted locators are structural/candidate metadata, never legal interpretation.
PDF support uses an optional pypdf-compatible reader; tests inject a fake reader.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from html.parser import HTMLParser
import re
from typing import Callable, Iterable
import xml.etree.ElementTree as ET

from source_evidence import SOURCE_REGISTRY

EXTRACTOR_VERSION = "1.1.0"
DEFAULT_MAX_INPUT_BYTES = 25 * 1024 * 1024
DEFAULT_MAX_TEXT_CHARS = 5_000_000
PDF_BACKEND_UNAVAILABLE = "PDF_BACKEND_UNAVAILABLE"


class ExtractionError(RuntimeError):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class LegalUnit:
    locator: str
    unit_type: str
    number: str
    text: str


@dataclass(frozen=True)
class PageText:
    page_number: int
    text: str


@dataclass(frozen=True)
class ExtractedDocument:
    source_id: str
    extraction_method: str
    extractor_version: str
    raw_sha256: str
    text_sha256: str
    text: str
    title: str
    units: tuple[LegalUnit, ...]
    pages: tuple[PageText, ...]
    locator_status: str
    decode_charset: str = "utf-8-sig"
    replacement_char_count: int = 0
    page_count: int = 0
    empty_page_count: int = 0
    quality_status: str = "NOT_ASSESSED"

    def to_dict(self) -> dict[str, object]:
        return {
            "source_id": self.source_id,
            "extraction_method": self.extraction_method,
            "extractor_version": self.extractor_version,
            "raw_sha256": self.raw_sha256,
            "text_sha256": self.text_sha256,
            "text": self.text,
            "title": self.title,
            "units": [asdict(unit) for unit in self.units],
            "pages": [asdict(page) for page in self.pages],
            "locator_status": self.locator_status,
            "decode_charset": self.decode_charset,
            "replacement_char_count": self.replacement_char_count,
            "page_count": self.page_count,
            "empty_page_count": self.empty_page_count,
            "quality_status": self.quality_status,
        }


def _validate_source_id(source_id: str) -> None:
    if source_id not in SOURCE_REGISTRY:
        raise ExtractionError("UNKNOWN_SOURCE_ID")


def _decode_bytes(data: bytes, max_input_bytes: int) -> str:
    if not isinstance(data, (bytes, bytearray)):
        raise ExtractionError("INPUT_MUST_BE_BYTES")
    if len(data) > max_input_bytes:
        raise ExtractionError("INPUT_TOO_LARGE")
    if not data:
        raise ExtractionError("EMPTY_INPUT")
    raw = bytes(data)
    # Never silently replace damaged bytes: loss is a hard extraction failure.
        try:
            return raw.decode("utf-16", errors="strict")
        except UnicodeDecodeError as exc:
            raise ExtractionError("CHARSET_DECODE_FAILED") from exc
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
    if raw.startswith((b"\x00\x00\xfe\xff", b"\xff\xfe\x00\x00")):
        try:
            return raw.decode("utf-32", errors="strict")
        except UnicodeDecodeError as exc:
            raise ExtractionError("CHARSET_DECODE_FAILED") from exc
    # XML declarations and HTML charset declarations are accepted only when
    # the declared codec decodes strictly. Otherwise UTF-8 is the default.
    head = raw[:4096].decode("ascii", errors="ignore")
    match = re.search(r"(?:encoding|charset)\s*=\s*['\"]?([A-Za-z0-9._-]+)", head, re.I)
    encoding = match.group(1) if match else "utf-8"
    try:
        return raw.decode(encoding, errors="strict")
    except (LookupError, UnicodeDecodeError) as exc:
        raise ExtractionError("CHARSET_DECODE_FAILED") from exc
            raise ExtractionError("CHARSET_DECODE_FAILED") from exc
    raise ExtractionError("CHARSET_DECODE_FAILED")


def _clean_text(value: str) -> str:
    value = value.replace("\u00a0", " ")
    value = re.sub(r"[\t\r\f\v ]+", " ", value)
    value = re.sub(r" *\n *", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


class _HTMLTextParser(HTMLParser):
    BLOCK_TAGS = {
        "address", "article", "blockquote", "br", "dd", "div", "dl", "dt",
        "h1", "h2", "h3", "h4", "h5", "h6", "li", "ol", "p", "section",
        "table", "td", "th", "tr", "ul",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.title_parts: list[str] = []
        self.in_title = False
        self.suppressed = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in ("script", "style", "noscript", "svg"):
            self.suppressed += 1
            return
        if tag == "title":
            self.in_title = True
        if not self.suppressed and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in ("script", "style", "noscript", "svg") and self.suppressed:
            self.suppressed -= 1
            return
        if tag == "title":
            self.in_title = False
        if not self.suppressed and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if not self.suppressed:
            self.parts.append(data)


def _document(
    source_id: str,
    method: str,
    raw: bytes,
    text: str,
    title: str = "",
    units: Iterable[LegalUnit] = (),
    pages: Iterable[PageText] = (),
    locator_status: str = "NOT_APPLICABLE",
    page_count: int = 0,
    empty_page_count: int = 0,
    quality_status: str = "NOT_ASSESSED",
) -> ExtractedDocument:
    cleaned = _clean_text(text)
    return ExtractedDocument(
        source_id=source_id,
        extraction_method=method,
        extractor_version=EXTRACTOR_VERSION,
        raw_sha256=sha256(raw).hexdigest(),
        text_sha256=sha256(cleaned.encode("utf-8")).hexdigest(),
        text=cleaned,
        title=_clean_text(title),
        units=tuple(units),
        pages=tuple(pages),
        locator_status=locator_status,
        decode_charset="strict-auto",
        replacement_char_count=0,
        page_count=page_count,
        empty_page_count=empty_page_count,
        quality_status=quality_status,
    )


def extract_html_document(
    source_id: str,
    data: bytes,
    *,
    max_input_bytes: int = DEFAULT_MAX_INPUT_BYTES,
    max_text_chars: int = DEFAULT_MAX_TEXT_CHARS,
) -> ExtractedDocument:
    _validate_source_id(source_id)
    raw = bytes(data)
    html = _decode_bytes(raw, max_input_bytes)
    parser = _HTMLTextParser()
    try:
        parser.feed(html)
        parser.close()
    except Exception as exc:
        raise ExtractionError("HTML_PARSE_FAILED") from exc
    text = _clean_text("".join(parser.parts))
    if len(text) > max_text_chars:
        raise ExtractionError("EXTRACTED_TEXT_TOO_LARGE")
    return _document(
        source_id, "HTML_TEXT_V1", raw, text,
        title=" ".join(parser.title_parts),
    )


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].split(":")[-1].upper()


def _element_text(element: ET.Element) -> str:
    return _clean_text(" ".join(part for part in element.itertext() if part and part.strip()))


def _number_for(element: ET.Element, kind: str) -> str:
    attrs = {key.upper().split("}")[-1]: value for key, value in element.attrib.items()}
    for key in ("NUMBER", "NUM", "N", "IDENTIFIER", "ID"):
        value = attrs.get(key)
        if value:
            return _clean_text(value)
    # EUR-Lex/Formex documents may place the number in a direct NUM/NO child.
    for child in list(element):
        if _local_name(child.tag) in {"NUM", "NO", "NUMBER", "TI", "TITLE"}:
            candidate = _element_text(child)
            if candidate:
                match = re.search(r"(?:ARTICLE|ANNEX|PARAGRAPH|POINT|PART)?\s*([IVXLC]+|\d+[A-Z]?)", candidate, re.I)
                if match:
                    return match.group(1)
    return ""


def extract_eurlex_xml(
    source_id: str,
    data: bytes,
    *,
    max_input_bytes: int = DEFAULT_MAX_INPUT_BYTES,
    max_text_chars: int = DEFAULT_MAX_TEXT_CHARS,
) -> ExtractedDocument:
    _validate_source_id(source_id)
    raw = bytes(data)
    xml_text = _decode_bytes(raw, max_input_bytes)
    # Reject DTD/entity declarations rather than relying on parser-specific expansion behavior.
    if re.search(r"<!\s*(DOCTYPE|ENTITY)\b", xml_text, re.I):
        raise ExtractionError("XML_DTD_OR_ENTITY_BLOCKED")
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise ExtractionError("XML_PARSE_FAILED") from exc

    all_text = _element_text(root)
    if len(all_text) > max_text_chars:
        raise ExtractionError("EXTRACTED_TEXT_TOO_LARGE")

    units: list[LegalUnit] = []
    context: list[tuple[str, str]] = []
    relevant = {
        "ARTICLE": "Article", "ART": "Article",
        "ANNEX": "Annex", "PART": "Part",
        "PARAG": "paragraph", "PARAGRAPH": "paragraph",
        "POINT": "point", "SUBPOINT": "subpoint",
    }

    def walk(node: ET.Element, parents: list[tuple[str, str]]) -> None:
        tag = _local_name(node.tag)
        next_parents = parents
        if tag in relevant:
            kind = relevant[tag]
            number = _number_for(node, kind)
            if not number and kind in {"Article", "Annex", "Part"}:
                number = "UNNUMBERED"
            if number:
                next_parents = parents + [(kind, number)]
                locator = " / ".join(f"{k} {n}" for k, n in next_parents)
                node_text = _element_text(node)
                if node_text:
                    units.append(LegalUnit(locator, kind.upper(), number, node_text))
        for child in list(node):
            walk(child, next_parents)

    walk(root, [])
    # De-duplicate exact structural units while preserving source order.
    seen: set[tuple[str, str]] = set()
    unique_units: list[LegalUnit] = []
    for unit in units:
        key = (unit.locator, unit.text)
        if key not in seen:
            seen.add(key)
            unique_units.append(unit)

    title = ""
    for node in root.iter():
        if _local_name(node.tag) in {"TITLE", "TI"}:
            candidate = _element_text(node)
            if candidate:
                title = candidate
                break
    return _document(
        source_id, "EURLEX_XML_STRUCTURED_V1", raw, all_text,
        title=title, units=unique_units,
        locator_status="CANDIDATES_EXTRACTED" if unique_units else "NO_STRUCTURED_LOCATORS",
    )


def extract_eurlex_html(
    source_id: str,
    data: bytes,
    *,
    max_input_bytes: int = DEFAULT_MAX_INPUT_BYTES,
    max_text_chars: int = DEFAULT_MAX_TEXT_CHARS,
) -> ExtractedDocument:
    base = extract_html_document(
        source_id, data, max_input_bytes=max_input_bytes, max_text_chars=max_text_chars
    )
    # HTML locators are text-derived candidates only; XML remains preferred for hierarchy.
    patterns = (
        (r"\bArticle\s+(\d+[a-z]?)\b", "ARTICLE", "Article"),
        (r"\bAnnex\s+([IVXLC]+|\d+)\b", "ANNEX", "Annex"),
    )
    units: list[LegalUnit] = []
    lines = [line.strip() for line in base.text.splitlines() if line.strip()]
    for line in lines:
        for pattern, kind, label in patterns:
            match = re.search(pattern, line, re.I)
            if match:
                number = match.group(1)
                units.append(LegalUnit(f"{label} {number}", kind, number, line[:2000]))
    unique = {(unit.locator, unit.text): unit for unit in units}
    return _document(
        source_id, "EURLEX_HTML_CANDIDATE_V1", bytes(data), base.text,
        title=base.title, units=unique.values(),
        locator_status="CANDIDATES_ONLY" if unique else "NO_LOCATOR_CANDIDATES",
    )


def extract_pdf_pages(
    source_id: str,
    data: bytes,
    *,
    reader_factory: Callable[[object], object] | None = None,
    max_input_bytes: int = DEFAULT_MAX_INPUT_BYTES,
    max_text_chars: int = DEFAULT_MAX_TEXT_CHARS,
    max_pages: int = 1000,
) -> ExtractedDocument:
    _validate_source_id(source_id)
    raw = bytes(data)
    if len(raw) > max_input_bytes:
        raise ExtractionError("INPUT_TOO_LARGE")
    if not raw:
        raise ExtractionError("EMPTY_INPUT")
    if not raw.startswith(b"%PDF-"):
        raise ExtractionError("PDF_SIGNATURE_INVALID")
    if reader_factory is None:
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise ExtractionError(PDF_BACKEND_UNAVAILABLE) from exc
        reader_factory = PdfReader
    try:
        import io
        reader = reader_factory(io.BytesIO(raw))
        source_pages = getattr(reader, "pages")
        if len(source_pages) > max_pages:
            raise ExtractionError("PDF_PAGE_LIMIT_EXCEEDED")
        pages: list[PageText] = []
        for index, page in enumerate(source_pages, start=1):
            try:
                page_text = _clean_text(page.extract_text() or "")
            except Exception as exc:
                raise ExtractionError("PDF_PAGE_EXTRACTION_FAILED") from exc
            pages.append(PageText(index, page_text))
    except ExtractionError:
        raise
    except Exception as exc:
        raise ExtractionError("PDF_PARSE_FAILED") from exc

    text = "\n\n".join(f"[Page {page.page_number}]\n{page.text}" for page in pages)
    if len(text) > max_text_chars:
        raise ExtractionError("EXTRACTED_TEXT_TOO_LARGE")
    return _document(
        source_id, "PDF_PAGE_TEXT_V1", raw, text,
        pages=pages,
        locator_status="PAGE_LOCATORS_ONLY",
        page_count=len(pages),
        empty_page_count=sum(1 for page in pages if not page.text.strip()),
        quality_status=("REVIEW_REQUIRED" if not pages or all(not page.text.strip() for page in pages) else ("PARTIAL_TEXT" if any(not page.text.strip() for page in pages) else "TEXT_EXTRACTED_NOT_VISUALLY_VERIFIED")),
    )
