"""Pinned-IP HTTPS transport for curated official-source fetches.

The caller resolves and validates every DNS answer before calling get(). This
transport never resolves the URL hostname: TCP connects to a supplied literal
IP while TLS SNI and certificate hostname checks use the URL hostname. It uses
only the Python standard library; redirects and implicit retries are disabled.
"""
from __future__ import annotations

import http.client
import ipaddress
import socket
import ssl
from typing import Iterable
from urllib.parse import urlsplit


class PinnedTransportError(RuntimeError):
    """A pinned connection could not be established safely."""


class _PinnedConnectError(OSError):
    """TCP connection to one explicitly pinned IP failed."""


def normalize_public_ips(addresses: Iterable[str]) -> tuple[str, ...]:
    """Normalize and validate all A/AAAA answers; fail closed on any unsafe item."""
    normalized: set[str] = set()
    nat64_wkp = ipaddress.ip_network("64:ff9b::/96")
    nat64_local = ipaddress.ip_network("64:ff9b:1::/48")
    six_to_four = ipaddress.ip_network("2002::/16")
    teredo = ipaddress.ip_network("2001::/32")

    try:
        raw_addresses = tuple(addresses)
    except Exception as exc:
        raise PinnedTransportError("DNS_INVALID_ADDRESS_SET") from exc
    if not raw_addresses:
        raise PinnedTransportError("DNS_NO_ADDRESS")

    for raw in raw_addresses:
        if not isinstance(raw, str) or "%" in raw:
            raise PinnedTransportError("DNS_INVALID_ADDRESS")
        try:
            ip = ipaddress.ip_address(raw)
        except ValueError as exc:
            raise PinnedTransportError("DNS_INVALID_ADDRESS") from exc

        if isinstance(ip, ipaddress.IPv6Address):
            if ip.ipv4_mapped is not None:
                ip = ip.ipv4_mapped
            elif ip in nat64_wkp or ip in nat64_local or ip in six_to_four or ip in teredo:
                raise PinnedTransportError("NON_PUBLIC_ADDRESS_BLOCKED")

        if (
            not ip.is_global
            or ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_multicast
            or ip.is_reserved
            or ip.is_unspecified
        ):
            raise PinnedTransportError("NON_PUBLIC_ADDRESS_BLOCKED")
        normalized.add(str(ip))

    return tuple(sorted(normalized, key=lambda value: (ipaddress.ip_address(value).version, int(ipaddress.ip_address(value)))))


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(self, host: str, address: str, connect_timeout: float, read_timeout: float, context: ssl.SSLContext):
        super().__init__(host=host, port=443, timeout=connect_timeout, context=context)
        self._pinned_address = address
        self._read_timeout = read_timeout

    def connect(self) -> None:
        try:
            raw_socket = socket.create_connection((self._pinned_address, self.port), self.timeout)
        except OSError as exc:
            raise _PinnedConnectError("PINNED_TCP_CONNECT_FAILED") from exc
        try:
            # SNI and certificate hostname verification deliberately use the
            # original allowlisted DNS hostname, never the literal IP.
            self.sock = self._context.wrap_socket(raw_socket, server_hostname=self.host)
            self.sock.settimeout(self._read_timeout)
        except Exception:
            raw_socket.close()
            raise


class _PinnedResponse:
    def __init__(self, response: http.client.HTTPResponse, connection: _PinnedHTTPSConnection):
        self._response = response
        self._connection = connection
        self.status_code = int(response.status)
        self.headers = response.headers
        self.closed = False

    def iter_content(self, chunk_size: int):
        while True:
            chunk = self._response.read(chunk_size)
            if not chunk:
                break
            yield chunk

    def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        try:
            self._response.close()
        finally:
            self._connection.close()


class PinnedHTTPSession:
    """Small requests-like adapter that only connects to caller-validated IPs."""

    def get(
        self,
        url: str,
        *,
        pinned_ips: Iterable[str],
        allow_redirects: bool = False,
        stream: bool = True,
        timeout: tuple[float, float] = (5.0, 20.0),
        verify: bool | str = True,
        headers: dict[str, str] | None = None,
    ) -> _PinnedResponse:
        parsed = urlsplit(url)
        if parsed.scheme.lower() != "https" or not parsed.hostname:
            raise PinnedTransportError("HTTPS_REQUIRED")
        if parsed.port not in (None, 443) or parsed.username is not None or parsed.password is not None or parsed.fragment:
            raise PinnedTransportError("INVALID_PINNED_URL")
        if allow_redirects:
            raise PinnedTransportError("AUTOMATIC_REDIRECT_BLOCKED")
        if not stream:
            raise PinnedTransportError("STREAMING_REQUIRED")
        if verify is False:
            raise PinnedTransportError("TLS_VERIFICATION_REQUIRED")
        if len(timeout) != 2 or timeout[0] <= 0 or timeout[1] <= 0:
            raise PinnedTransportError("INVALID_TIMEOUT")

        host = parsed.hostname.encode("idna").decode("ascii").lower()
        ips = normalize_public_ips(pinned_ips)
        try:
            context = ssl.create_default_context(cafile=verify if isinstance(verify, str) else None)
        except (OSError, ssl.SSLError) as exc:
            raise PinnedTransportError("TLS_TRUST_STORE_UNAVAILABLE") from exc
        context.check_hostname = True
        context.verify_mode = ssl.CERT_REQUIRED

        target = parsed.path or "/"
        if parsed.query:
            target += "?" + parsed.query
        reserved_headers = {"host", "accept-encoding", "connection"}
        request_headers = {
            key: value for key, value in (headers or {}).items()
            if key.lower() not in reserved_headers
        }
        # http.client supplies Host from connection.host (the original DNS
        # name) and Accept-Encoding: identity. Avoid duplicate Host headers.
        request_headers["Connection"] = "close"

        last_connection_error: Exception | None = None
        for address in ips:
            connection = _PinnedHTTPSConnection(host, address, timeout[0], timeout[1], context)
            try:
                connection.request("GET", target, headers=request_headers)
                response = connection.getresponse()
                return _PinnedResponse(response, connection)
            except _PinnedConnectError as exc:
                connection.close()
                last_connection_error = exc
                continue
            except Exception:
                connection.close()
                raise

        raise PinnedTransportError("PINNED_CONNECTION_FAILED") from last_connection_error
