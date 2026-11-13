"""Pinned-IP HTTPS transport for curated official-source fetches.

The caller must resolve and validate every DNS answer before calling get(). This
transport never resolves the URL hostname: TCP connects to one of the supplied
literal IP addresses while TLS SNI and certificate hostname checks use the URL
hostname. Redirects are deliberately disabled and handled by the caller.
"""
from __future__ import annotations

import ipaddress
from typing import Iterable
from urllib.parse import urlsplit

import requests
import urllib3
from urllib3.exceptions import ConnectTimeoutError, MaxRetryError, NewConnectionError


class PinnedTransportError(RuntimeError):
    """A pinned connection could not be established safely."""


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


class _PinnedResponse:
    def __init__(self, response: object, pool: urllib3.HTTPSConnectionPool):
        self._response = response
        self._pool = pool
        self.status_code = int(getattr(response, "status", 0))
        self.headers = response.headers
        self.closed = False

    def iter_content(self, chunk_size: int):
        yield from self._response.stream(amt=chunk_size, decode_content=False)

    def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        try:
            self._response.close()
        finally:
            self._pool.close()


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
        if parsed.port not in (None, 443) or parsed.username is not None or parsed.password is not None:
            raise PinnedTransportError("INVALID_PINNED_URL")
        if allow_redirects:
            raise PinnedTransportError("AUTOMATIC_REDIRECT_BLOCKED")
        if not stream:
            raise PinnedTransportError("STREAMING_REQUIRED")
        if verify is False:
            raise PinnedTransportError("TLS_VERIFICATION_REQUIRED")

        host = parsed.hostname.encode("idna").decode("ascii").lower()
        ips = normalize_public_ips(pinned_ips)
        ca_bundle = verify if isinstance(verify, str) else requests.certs.where()
        target = parsed.path or "/"
        if parsed.query:
            target += "?" + parsed.query
        request_headers = dict(headers or {})
        request_headers["Host"] = host
        request_headers["Accept-Encoding"] = "identity"

        last_connection_error: Exception | None = None
        for address in ips:
            pool = urllib3.HTTPSConnectionPool(
                host=address,
                port=443,
                server_hostname=host,
                assert_hostname=host,
                cert_reqs="CERT_REQUIRED",
                ca_certs=ca_bundle,
                maxsize=1,
                block=True,
                retries=False,
            )
            try:
                response = pool.request(
                    "GET",
                    target,
                    headers=request_headers,
                    timeout=urllib3.Timeout(connect=timeout[0], read=timeout[1]),
                    retries=False,
                    redirect=False,
                    preload_content=False,
                    decode_content=False,
                )
                return _PinnedResponse(response, pool)
            except (ConnectTimeoutError, NewConnectionError, OSError) as exc:
                pool.close()
                last_connection_error = exc
                continue
            except MaxRetryError as exc:
                pool.close()
                reason = getattr(exc, "reason", None)
                if isinstance(reason, (ConnectTimeoutError, NewConnectionError, OSError)):
                    last_connection_error = exc
                    continue
                raise
            except Exception:
                pool.close()
                raise

        raise PinnedTransportError("PINNED_CONNECTION_FAILED") from last_connection_error
