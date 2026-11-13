import hashlib
import unittest
from unittest import mock

from source_extraction import (
    ExtractionError,
    extract_eurlex_html,
    extract_eurlex_xml,
    extract_html_document,
    extract_pdf_pages,
)


class FakePage:
    def __init__(self, text):
        self.text = text

    def extract_text(self):
        return self.text


class FakeReader:
    def __init__(self, _stream):
        self.pages = [FakePage("Article 13\nParagraph 8"), FakePage("Annex II\nPoint 9")]


class SourceExtractionTests(unittest.TestCase):
    def test_html_extracts_visible_text_and_title_and_skips_script(self):
        raw = b"""<html><head><title>Official Doc</title><script>secret_bad_text</script></head>
        <body><h1>Security</h1><p>Article 13 applies.</p><style>hidden_css</style></body></html>"""
        result = extract_html_document("ST_AN5156_REV14", raw)
        self.assertEqual(result.title, "Official Doc")
        self.assertIn("Article 13 applies.", result.text)
        self.assertNotIn("secret_bad_text", result.text)
        self.assertNotIn("hidden_css", result.text)
        self.assertEqual(result.raw_sha256, hashlib.sha256(raw).hexdigest())
        self.assertEqual(result.extraction_method, "HTML_TEXT_V1")

    def test_eurlex_html_marks_locators_as_candidates_not_verified(self):
        raw = b"<html><body><h2>Article 13</h2><p>Paragraph 8 support period</p><h2>Annex II</h2></body></html>"
        result = extract_eurlex_html("CRA_EURLEX_2024_2847", raw)
        self.assertEqual(result.locator_status, "CANDIDATES_ONLY")
        self.assertIn("Article 13", [u.locator for u in result.units])
        self.assertIn("Annex II", [u.locator for u in result.units])
        self.assertNotEqual(result.locator_status, "VERIFIED")

    def test_xml_extracts_nested_article_paragraph_and_point_hierarchy(self):
        raw = b"""<?xml version="1.0" encoding="UTF-8"?>
        <ACT><TITLE>Regulation (EU) 2024/2847</TITLE>
          <ARTICLE NUMBER="13"><TI>Article 13</TI>
            <PARAG NUMBER="8"><CONTENT>Support period reflects expected use.</CONTENT>
              <POINT NUMBER="a"><CONTENT>Minimum five years unless expected use is shorter.</CONTENT></POINT>
            </PARAG>
          </ARTICLE>
          <ANNEX NUMBER="II"><PART NUMBER="I"><PARAG NUMBER="1"><CONTENT>Requirement text.</CONTENT></PARAG></PART></ANNEX>
        </ACT>"""
        result = extract_eurlex_xml("CRA_EURLEX_2024_2847", raw)
        locators = [u.locator for u in result.units]
        self.assertIn("Article 13", locators)
        self.assertIn("Article 13 / paragraph 8", locators)
        self.assertIn("Article 13 / paragraph 8 / point a", locators)
        self.assertIn("Annex II / Part I / paragraph 1", locators)
        self.assertEqual(result.locator_status, "CANDIDATES_EXTRACTED")
        paragraph = next(u for u in result.units if u.locator == "Article 13 / paragraph 8")
        self.assertIn("Support period reflects expected use.", paragraph.text)

    def test_xml_rejects_dtd_and_entity_declarations(self):
        raw = b'<!DOCTYPE foo [<!ENTITY x "boom">]><ACT>&x;</ACT>'
        with self.assertRaisesRegex(ExtractionError, "XML_DTD_OR_ENTITY_BLOCKED"):
            extract_eurlex_xml("CRA_EURLEX_2024_2847", raw)

    def test_xml_malformed_is_fail_closed(self):
        with self.assertRaisesRegex(ExtractionError, "XML_PARSE_FAILED"):
            extract_eurlex_xml("CRA_EURLEX_2024_2847", b"<ACT><ARTICLE>")

    def test_pdf_extracts_page_text_and_one_based_page_locators(self):
        raw = b"%PDF-1.7\nfixture-not-a-real-pdf"
        result = extract_pdf_pages("TI_MSPM0G3529_Q1_DATASHEET", raw, reader_factory=FakeReader)
        self.assertEqual([p.page_number for p in result.pages], [1, 2])
        self.assertIn("[Page 1]", result.text)
        self.assertIn("Annex II", result.pages[1].text)
        self.assertEqual(result.locator_status, "PAGE_LOCATORS_ONLY")
        self.assertEqual(result.extraction_method, "PDF_PAGE_TEXT_V1")

    def test_pdf_rejects_invalid_signature_and_page_limit(self):
        with self.assertRaisesRegex(ExtractionError, "PDF_SIGNATURE_INVALID"):
            extract_pdf_pages("TI_MSPM0G3529_Q1_DATASHEET", b"not a pdf", reader_factory=FakeReader)

        class TooManyPages:
            def __init__(self, _stream):
                self.pages = [FakePage("x"), FakePage("y")]

        with self.assertRaisesRegex(ExtractionError, "PDF_PAGE_LIMIT_EXCEEDED"):
            extract_pdf_pages("TI_MSPM0G3529_Q1_DATASHEET", b"%PDF-1.7 fixture", reader_factory=TooManyPages, max_pages=1)

    def test_pdf_backend_unavailable_is_explicit(self):
        # A factory import is deliberately lazy; force the no-backend branch without touching the network.
        raw = b"%PDF-1.7 fixture"
        with mock.patch.dict("sys.modules", {"pypdf": None}):
            with self.assertRaisesRegex(ExtractionError, "PDF_BACKEND_UNAVAILABLE"):
                extract_pdf_pages("TI_MSPM0G3529_Q1_DATASHEET", raw)

    def test_unknown_source_id_is_rejected(self):
        with self.assertRaisesRegex(ExtractionError, "UNKNOWN_SOURCE_ID"):
            extract_html_document("MODEL_INVENTED_SOURCE", b"<p>text</p>")

    def test_input_and_extracted_text_limits_are_enforced(self):
        with self.assertRaisesRegex(ExtractionError, "INPUT_TOO_LARGE"):
            extract_html_document("ST_AN5156_REV14", b"<p>12345</p>", max_input_bytes=4)
        with self.assertRaisesRegex(ExtractionError, "EXTRACTED_TEXT_TOO_LARGE"):
            extract_html_document("ST_AN5156_REV14", b"<p>12345</p>", max_text_chars=4)


    def test_invalid_utf8_is_rejected_instead_of_silently_replaced(self):
        raw = b"<html><body>bad-\xff-byte</body></html>"
        with self.assertRaisesRegex(ExtractionError, "CHARSET_DECODE_FAILED"):
            extract_html_document("ST_AN5156_REV14", raw)

    def test_declared_windows_1252_is_decoded_strictly(self):
        raw = b'<html><head><meta charset="windows-1252"><title>caf\xe9</title></head><body>caf\xe9</body></html>'
        result = extract_html_document("ST_AN5156_REV14", raw)
        self.assertIn("café", result.text)
        self.assertEqual(result.replacement_char_count, 0)

    def test_pdf_reports_empty_page_quality_diagnostics(self):
        class PartialReader:
            def __init__(self, _stream):
                self.pages = [FakePage("text"), FakePage(""), FakePage("more text")]
        result = extract_pdf_pages("TI_MSPM0G3529_Q1_DATASHEET", b"%PDF-1.7 fixture", reader_factory=PartialReader)
        self.assertEqual(result.page_count, 3)
        self.assertEqual(result.empty_page_count, 1)
        self.assertEqual(result.quality_status, "PARTIAL_TEXT")


if __name__ == "__main__":
    unittest.main()
