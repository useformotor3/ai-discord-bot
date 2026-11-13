import ssl
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import urllib3.util.connection

from source_transport import PinnedHTTPSession, PinnedTransportError, normalize_public_ips

PUBLIC_IP = "1.1.1.1"
HOST = "eur-lex.europa.eu"


class _LocalTLSServer(ThreadingHTTPServer):
    def handle_error(self, _request, _client_address):
        pass


class _Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    host_header = None

    def do_GET(self):
        type(self).host_header = self.headers.get("Host")
        body = b"local TLS fixture"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_args):
        pass


class SourceTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tempdir = tempfile.TemporaryDirectory()
        cls.cert_file = Path(cls._tempdir.name) / "server.crt"
        cls.key_file = Path(cls._tempdir.name) / "server.key"
        subprocess.run(
            [
                "openssl", "req", "-x509", "-nodes", "-days", "1",
                "-newkey", "rsa:2048", "-keyout", str(cls.key_file),
                "-out", str(cls.cert_file), "-subj", f"/CN={HOST}",
                "-addext", f"subjectAltName=DNS:{HOST}",
                "-addext", "basicConstraints=critical,CA:TRUE",
                "-addext", "keyUsage=critical,digitalSignature,keyCertSign,keyEncipherment",
                "-addext", "extendedKeyUsage=serverAuth",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    @classmethod
    def tearDownClass(cls):
        cls._tempdir.cleanup()

    def test_normalizes_ipv4_mapped_ipv6_and_deduplicates(self):
        self.assertEqual(normalize_public_ips(["1.1.1.1", "::ffff:1.1.1.1"]), ("1.1.1.1",))

    def test_mixed_public_and_private_answers_fail_closed(self):
        with self.assertRaisesRegex(PinnedTransportError, "NON_PUBLIC_ADDRESS_BLOCKED"):
            normalize_public_ips(["1.1.1.1", "10.0.0.1"])

    def test_rejects_loopback_link_local_reserved_and_multicast(self):
        for address in ["127.0.0.1", "169.254.1.1", "192.0.2.1", "224.0.0.1", "::1", "fe80::1", "ff02::1"]:
            with self.subTest(address=address):
                with self.assertRaises(PinnedTransportError):
                    normalize_public_ips([address])

    def test_rejects_nat64_6to4_teredo_and_scoped_ipv6(self):
        for address in ["64:ff9b::808:808", "64:ff9b:1::808:808", "2002:0808:0808::1", "2001::1", "2606:4700:4700::1111%eth0"]:
            with self.subTest(address=address):
                with self.assertRaises(PinnedTransportError):
                    normalize_public_ips([address])

    def test_empty_invalid_and_non_string_dns_answers_fail_closed(self):
        for addresses in [[], ["not-an-ip"], [None]]:
            with self.subTest(addresses=addresses):
                with self.assertRaises(PinnedTransportError):
                    normalize_public_ips(addresses)

    def _serve_tls(self):
        server = _LocalTLSServer(("127.0.0.1", 0), _Handler)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(self.cert_file, self.key_file)
        seen = []
        context.set_servername_callback(lambda _sock, name, _ctx: seen.append(name))
        server.socket = context.wrap_socket(server.socket, server_side=True)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        return server, thread, seen

    def _patch_connect(self, server, requested):
        original = urllib3.util.connection.create_connection

        def routed(address, *args, **kwargs):
            requested.append(address)
            host, _port = address
            if host == PUBLIC_IP:
                return original(("127.0.0.1", server.server_port), *args, **kwargs)
            return original(address, *args, **kwargs)

        return patch("urllib3.util.connection.create_connection", side_effect=routed)

    def test_real_tls_uses_pinned_ip_sni_and_original_host_header(self):
        server, thread, sni = self._serve_tls()
        requested = []
        try:
            with self._patch_connect(server, requested):
                response = PinnedHTTPSession().get(
                    f"https://{HOST}/fixture?q=1",
                    pinned_ips=[PUBLIC_IP],
                    verify=str(self.cert_file),
                    timeout=(2, 2),
                    headers={"User-Agent": "transport-test"},
                )
                try:
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(b"".join(response.iter_content(4096)), b"local TLS fixture")
                finally:
                    response.close()
            self.assertEqual(requested, [(PUBLIC_IP, 443)])
            self.assertEqual(sni, [HOST])
            self.assertEqual(_Handler.host_header, HOST)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

    def test_wrong_certificate_hostname_is_rejected(self):
        server, thread, _sni = self._serve_tls()
        requested = []
        try:
            with self._patch_connect(server, requested):
                with self.assertRaises(urllib3.exceptions.SSLError):
                    PinnedHTTPSession().get(
                        "https://different.example/fixture",
                        pinned_ips=[PUBLIC_IP],
                        verify=str(self.cert_file),
                        timeout=(2, 2),
                    )
            self.assertEqual(requested, [(PUBLIC_IP, 443)])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

    def test_connection_fallback_uses_only_supplied_pinned_ips(self):
        server, thread, sni = self._serve_tls()
        requested = []
        original = urllib3.util.connection.create_connection

        def routed(address, *args, **kwargs):
            requested.append(address)
            host, _port = address
            if host == "1.0.0.1":
                raise OSError("fixture connect failure")
            if host == PUBLIC_IP:
                return original(("127.0.0.1", server.server_port), *args, **kwargs)
            return original(address, *args, **kwargs)

        try:
            with patch("urllib3.util.connection.create_connection", side_effect=routed):
                response = PinnedHTTPSession().get(
                    f"https://{HOST}/fallback",
                    pinned_ips=["1.0.0.1", PUBLIC_IP],
                    verify=str(self.cert_file),
                    timeout=(2, 2),
                )
                try:
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(b"".join(response.iter_content(4096)), b"local TLS fixture")
                finally:
                    response.close()
            self.assertEqual(requested, [("1.0.0.1", 443), (PUBLIC_IP, 443)])
            self.assertEqual(sni, [HOST])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

    def test_transport_rejects_unsafe_ip_even_if_caller_supplies_it(self):
        with self.assertRaisesRegex(PinnedTransportError, "NON_PUBLIC_ADDRESS_BLOCKED"):
            PinnedHTTPSession().get("https://eur-lex.europa.eu/", pinned_ips=["127.0.0.1"])

    def test_transport_rejects_disabled_tls_and_automatic_redirects(self):
        with self.assertRaisesRegex(PinnedTransportError, "TLS_VERIFICATION_REQUIRED"):
            PinnedHTTPSession().get("https://eur-lex.europa.eu/", pinned_ips=[PUBLIC_IP], verify=False)
        with self.assertRaisesRegex(PinnedTransportError, "AUTOMATIC_REDIRECT_BLOCKED"):
            PinnedHTTPSession().get("https://eur-lex.europa.eu/", pinned_ips=[PUBLIC_IP], allow_redirects=True)


if __name__ == "__main__":
    unittest.main()
