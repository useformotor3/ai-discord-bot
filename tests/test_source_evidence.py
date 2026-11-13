import hashlib
import unittest
from datetime import datetime, timezone
from urllib.parse import urlsplit

from source_evidence import (
    ALLOWED_HOSTS,
    EXTRACTION_METHOD,
    SOURCE_REGISTRY,
    OfficialSourceFetcher,
    SourceFetchError,
)


PUBLIC_IP = "93.184.216.34"


class FakeResponse:
    def __init__(self, status=200, body=b"official fixture", headers=None, chunks=None):
        self.status_code = status
        self.headers = headers or {"Content-Type": "text/html; charset=utf-8"}
        self.body = body
        self.chunks = chunks
        self.closed = False

    def iter_content(self, chunk_size):
        if self.chunks is not None:
            yield from self.chunks
        else:
            yield self.body

    def close(self):
        self.closed = True


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


class SourceEvidenceTests(unittest.TestCase):
    def make_fetcher(self, responses, **kwargs):
        return OfficialSourceFetcher(
            FakeSession(responses),
            resolver=lambda _host: [PUBLIC_IP],
            clock=lambda: datetime(2026, 11, 13, 0, 0, tzinfo=timezone.utc),
            **kwargs,
        )

    def test_registry_has_unique_ids_and_https_allowlisted_hosts(self):
        self.assertEqual(len(SOURCE_REGISTRY), len(set(SOURCE_REGISTRY)))
        self.assertTrue(ALLOWED_HOSTS)
        for source in SOURCE_REGISTRY.values():
            parsed = urlsplit(source.canonical_url)
            self.assertEqual(parsed.scheme, "https")
            self.assertIn(parsed.hostname, ALLOWED_HOSTS)
            self.assertGreater(source.max_bytes, 0)

    def test_registry_cannot_be_mutated_at_runtime(self):
        with self.assertRaises(TypeError):
            SOURCE_REGISTRY["UNAPPROVED"] = SOURCE_REGISTRY["CRA_EURLEX_2024_2847"]

    def test_unknown_source_id_cannot_supply_arbitrary_url(self):
        fetcher = self.make_fetcher([])
        with self.assertRaisesRegex(SourceFetchError, "UNKNOWN_SOURCE_ID"):
            fetcher.fetch("https://attacker.example/")

    def test_success_records_stable_sha256_and_metadata(self):
        body = b"official legal fixture"
        fetcher = self.make_fetcher([FakeResponse(body=body)])
        result = fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertEqual(result.content, body)
        self.assertEqual(result.metadata.sha256, hashlib.sha256(body).hexdigest())
        self.assertEqual(result.metadata.byte_count, len(body))
        self.assertEqual(result.metadata.status, "FETCHED")
        self.assertEqual(result.metadata.publisher, "European Union")
        self.assertEqual(result.metadata.document_identifier, "CELEX:32024R2847")
        self.assertEqual(result.metadata.extraction_method, EXTRACTION_METHOD)
        self.assertEqual(result.metadata.fetched_at_utc, "2026-11-13T00:00:00+00:00")

    def test_same_bytes_produce_same_hash(self):
        body = b"same source bytes"
        first = self.make_fetcher([FakeResponse(body=body)]).fetch("CRA_EURLEX_2024_2847")
        second = self.make_fetcher([FakeResponse(body=body)]).fetch("CRA_EURLEX_2024_2847")
        self.assertEqual(first.metadata.sha256, second.metadata.sha256)

    def test_non_https_registry_target_is_rejected(self):
        fetcher = self.make_fetcher([FakeResponse()])
        from source_evidence import _validate_https_target
        with self.assertRaisesRegex(SourceFetchError, "HTTPS_REQUIRED"):
            _validate_https_target("http://eur-lex.europa.eu/x", "eur-lex.europa.eu", lambda _h: [PUBLIC_IP])

    def test_redirect_to_untrusted_host_is_blocked(self):
        response = FakeResponse(status=302, headers={"Location": "https://attacker.example/file"})
        fetcher = self.make_fetcher([response])
        with self.assertRaisesRegex(SourceFetchError, "REDIRECT_HOST_BLOCKED"):
            fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertTrue(response.closed)

    def test_redirect_to_same_allowlisted_host_is_followed_and_revalidated(self):
        first = FakeResponse(status=302, headers={"Location": "/legal-content/EN/TXT/?uri=CELEX:32024R2847"})
        second = FakeResponse(body=b"final bytes")
        resolver_calls = []
        session = FakeSession([first, second])
        fetcher = OfficialSourceFetcher(
            session,
            resolver=lambda host: resolver_calls.append(host) or [PUBLIC_IP],
            clock=lambda: datetime(2026, 11, 13, 0, 0, tzinfo=timezone.utc),
        )
        result = fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertEqual(result.content, b"final bytes")
        self.assertEqual(len(fetcher.session.calls), 2)
        self.assertEqual(resolver_calls, ["eur-lex.europa.eu", "eur-lex.europa.eu"])
        self.assertTrue(first.closed)

    def test_private_or_loopback_dns_address_is_blocked(self):
        fetcher = OfficialSourceFetcher(
            FakeSession([FakeResponse()]),
            resolver=lambda _host: ["127.0.0.1"],
        )
        with self.assertRaisesRegex(SourceFetchError, "NON_PUBLIC_ADDRESS_BLOCKED"):
            fetcher.fetch("CRA_EURLEX_2024_2847")

    def test_dns_failure_is_fail_closed(self):
        def broken_resolver(_host):
            raise OSError("fixture")
        fetcher = OfficialSourceFetcher(FakeSession([FakeResponse()]), resolver=broken_resolver)
        with self.assertRaisesRegex(SourceFetchError, "DNS_RESOLUTION_FAILED"):
            fetcher.fetch("CRA_EURLEX_2024_2847")

    def test_credentials_and_nonstandard_port_are_blocked(self):
        from source_evidence import _validate_https_target
        with self.assertRaisesRegex(SourceFetchError, "CREDENTIAL_URL_BLOCKED"):
            _validate_https_target("https://user:pass@eur-lex.europa.eu/x", "eur-lex.europa.eu", lambda _h: [PUBLIC_IP])
        with self.assertRaisesRegex(SourceFetchError, "NONSTANDARD_PORT_BLOCKED"):
            _validate_https_target("https://eur-lex.europa.eu:444/x", "eur-lex.europa.eu", lambda _h: [PUBLIC_IP])

    def test_wrong_mime_type_is_blocked(self):
        fetcher = self.make_fetcher([FakeResponse(headers={"Content-Type": "text/html"})])
        with self.assertRaisesRegex(SourceFetchError, "MIME_TYPE_NOT_ALLOWED"):
            fetcher.fetch("TI_MSPM0G3529_Q1_DATASHEET")

    def test_http_error_status_is_blocked(self):
        fetcher = self.make_fetcher([FakeResponse(status=503)])
        with self.assertRaisesRegex(SourceFetchError, "HTTP_STATUS_NOT_200"):
            fetcher.fetch("CRA_EURLEX_2024_2847")

    def test_request_exception_is_sanitized(self):
        fetcher = self.make_fetcher([TimeoutError("private provider detail")])
        with self.assertRaisesRegex(SourceFetchError, "HTTP_REQUEST_FAILED") as caught:
            fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertNotIn("private provider detail", str(caught.exception))

    def test_declared_content_length_over_limit_is_blocked(self):
        source = SOURCE_REGISTRY["CRA_EURLEX_2024_2847"]
        fetcher = self.make_fetcher([FakeResponse(headers={"Content-Type": "text/html", "Content-Length": str(source.max_bytes + 1)})])
        with self.assertRaisesRegex(SourceFetchError, "RESPONSE_TOO_LARGE"):
            fetcher.fetch("CRA_EURLEX_2024_2847")


    def test_negative_and_malformed_content_lengths_are_rejected(self):
        for content_length in ["-1", "not-a-number", "1, 1", ""]:
            with self.subTest(content_length=content_length):
                response = FakeResponse(headers={
                    "Content-Type": "text/html",
                    "Content-Length": content_length,
                })
                fetcher = self.make_fetcher([response])
                with self.assertRaisesRegex(SourceFetchError, "INVALID_CONTENT_LENGTH"):
                    fetcher.fetch("CRA_EURLEX_2024_2847")
                self.assertTrue(response.closed)

    def test_streamed_body_over_limit_is_blocked(self):
        source = SOURCE_REGISTRY["CRA_EURLEX_2024_2847"]
        fetcher = self.make_fetcher([FakeResponse(chunks=[b"x" * source.max_bytes, b"y"])])
        with self.assertRaisesRegex(SourceFetchError, "RESPONSE_TOO_LARGE"):
            fetcher.fetch("CRA_EURLEX_2024_2847")


    def test_all_dns_answers_are_validated_and_passed_to_transport(self):
        answers = [PUBLIC_IP, "8.8.8.8"]
        calls = []
        fetcher = OfficialSourceFetcher(
            FakeSession([FakeResponse()]),
            resolver=lambda host: calls.append(host) or answers,
        )
        fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertEqual(calls, ["eur-lex.europa.eu"])
        self.assertEqual(
            fetcher.session.calls[0][1]["pinned_ips"],
            ("8.8.8.8", "93.184.216.34"),
        )

    def test_mixed_public_private_dns_answers_are_blocked_before_http(self):
        session = FakeSession([FakeResponse()])
        fetcher = OfficialSourceFetcher(
            session,
            resolver=lambda _host: [PUBLIC_IP, "10.0.0.1"],
        )
        with self.assertRaisesRegex(SourceFetchError, "NON_PUBLIC_ADDRESS_BLOCKED"):
            fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertEqual(session.calls, [])

    def test_dns_resolution_is_not_repeated_by_fetcher_or_transport_contract(self):
        resolver_calls = []
        session = FakeSession([FakeResponse()])
        fetcher = OfficialSourceFetcher(
            session,
            resolver=lambda host: resolver_calls.append(host) or [PUBLIC_IP],
        )
        fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertEqual(resolver_calls, ["eur-lex.europa.eu"])
        self.assertEqual(session.calls[0][1]["pinned_ips"], (PUBLIC_IP,))

    def test_compressed_response_is_rejected_and_closed(self):
        response = FakeResponse(headers={
            "Content-Type": "text/html",
            "Content-Encoding": "gzip",
        })
        fetcher = self.make_fetcher([response])
        with self.assertRaisesRegex(SourceFetchError, "CONTENT_ENCODING_NOT_ALLOWED"):
            fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertTrue(response.closed)


    def test_http_downgrade_redirect_is_blocked_and_closed(self):
        response = FakeResponse(status=302, headers={"Location": "http://eur-lex.europa.eu/file"})
        fetcher = self.make_fetcher([response])
        with self.assertRaisesRegex(SourceFetchError, "HTTPS_REQUIRED"):
            fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertTrue(response.closed)

    def test_truncated_response_body_is_rejected_and_closed(self):
        response = FakeResponse(
            body=b"short",
            headers={"Content-Type": "text/html", "Content-Length": "10"},
        )
        fetcher = self.make_fetcher([response])
        with self.assertRaisesRegex(SourceFetchError, "TRUNCATED_RESPONSE"):
            fetcher.fetch("CRA_EURLEX_2024_2847")
        self.assertTrue(response.closed)

    def test_empty_body_is_blocked(self):
        fetcher = self.make_fetcher([FakeResponse(body=b"")])
        with self.assertRaisesRegex(SourceFetchError, "EMPTY_RESPONSE"):
            fetcher.fetch("CRA_EURLEX_2024_2847")

    def test_redirect_without_location_and_redirect_limit(self):
        fetcher = self.make_fetcher([FakeResponse(status=301, headers={})])
        with self.assertRaisesRegex(SourceFetchError, "REDIRECT_WITHOUT_LOCATION"):
            fetcher.fetch("CRA_EURLEX_2024_2847")
        fetcher = self.make_fetcher(
            [FakeResponse(status=302, headers={"Location": "/a"}), FakeResponse(status=302, headers={"Location": "/b"})],
            max_redirects=1,
        )
        with self.assertRaisesRegex(SourceFetchError, "TOO_MANY_REDIRECTS"):
            fetcher.fetch("CRA_EURLEX_2024_2847")

    def test_request_disables_automatic_redirects_and_sets_timeouts(self):
        fetcher = self.make_fetcher([FakeResponse()])
        fetcher.fetch("CRA_EURLEX_2024_2847")
        kwargs = fetcher.session.calls[0][1]
        self.assertEqual(kwargs["pinned_ips"], (PUBLIC_IP,))
        self.assertFalse(kwargs["allow_redirects"])
        self.assertEqual(kwargs["timeout"], (5.0, 20.0))
        self.assertTrue(kwargs["stream"])
        self.assertTrue(kwargs["verify"])


if __name__ == "__main__":
    unittest.main()
