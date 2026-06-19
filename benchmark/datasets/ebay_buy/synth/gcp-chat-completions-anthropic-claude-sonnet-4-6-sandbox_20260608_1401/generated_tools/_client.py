"""
Internal HTTP client for eBay Buy API.
Handles OAuth 2.0 Client Credentials token management and request execution.

NOT exposed as an MCP tool — internal implementation detail only.
"""
import os
import time
import base64
import requests
from typing import Optional

# ── Environment configuration ──────────────────────────────────────────────────
_APP_ID = os.environ.get("EBAY_APP_ID", "")
_CERT_ID = os.environ.get("EBAY_CERT_ID", "")
_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

if _ENVIRONMENT == "PRODUCTION":
    _BASE_URL = "https://api.ebay.com"
    _ORDER_BASE_URL = "https://apix.ebay.com"
    _TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"
else:
    _BASE_URL = "https://api.sandbox.ebay.com"
    _ORDER_BASE_URL = "https://apix.sandbox.ebay.com"
    _TOKEN_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"

# ── Token cache ────────────────────────────────────────────────────────────────
_token_cache: dict = {}  # scope -> {access_token, expires_at}


def _get_token(scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    """Obtain (or return cached) an OAuth 2.0 client credentials access token."""
    now = time.time()
    cached = _token_cache.get(scope)
    if cached and cached["expires_at"] > now + 60:
        return cached["access_token"]

    if not _APP_ID or not _CERT_ID:
        raise RuntimeError(
            "EBAY_APP_ID and EBAY_CERT_ID environment variables must be set."
        )

    credentials = base64.b64encode(f"{_APP_ID}:{_CERT_ID}".encode()).decode()
    resp = requests.post(
        _TOKEN_URL,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
            "scope": scope,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache[scope] = {
        "access_token": data["access_token"],
        "expires_at": now + int(data.get("expires_in", 7200)),
    }
    return data["access_token"]


def _scope_for_path(path: str) -> str:
    """Infer the appropriate OAuth scope from the API path."""
    if "/buy/deal" in path:
        return "https://api.ebay.com/oauth/api_scope/buy.deal"
    if "/buy/feed" in path:
        return "https://api.ebay.com/oauth/api_scope/buy.item.feed"
    if "/buy/marketing" in path:
        return "https://api.ebay.com/oauth/api_scope/buy.marketing"
    if "/buy/offer" in path:
        return "https://api.ebay.com/oauth/api_scope/buy.offer.auction"
    if "/buy/order" in path:
        return "https://api.ebay.com/oauth/api_scope/buy.guest.order"
    if "/buy/browse" in path and "item_ids" in path:
        return "https://api.ebay.com/oauth/api_scope/buy.item.bulk"
    return "https://api.ebay.com/oauth/api_scope"


def _make_request(
    method: str,
    path: str,
    params: Optional[dict] = None,
    json: Optional[dict] = None,
    extra_headers: Optional[dict] = None,
    use_order_host: bool = False,
    binary: bool = False,
) -> dict:
    """Execute an HTTP request against the eBay API and return a JSON-serializable result."""
    scope = _scope_for_path(path)
    try:
        token = _get_token(scope)
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}

    base = _ORDER_BASE_URL if use_order_host else _BASE_URL
    url = f"{base}{path}"

    headers = {"Authorization": f"Bearer {token}"}
    if extra_headers:
        headers.update(extra_headers)

    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=60,
        )
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

    if binary:
        # Return binary content as base64 + metadata
        if resp.status_code in (200, 206):
            return {
                "status_code": resp.status_code,
                "content_range": resp.headers.get("Content-Range", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "content_type": resp.headers.get("Content-Type", ""),
                "content_base64": base64.b64encode(resp.content).decode("ascii"),
                "content_length_bytes": len(resp.content),
            }
        # Error responses from feed endpoints are JSON
        try:
            return {"error": resp.json(), "status_code": resp.status_code}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}

    # JSON responses
    if resp.status_code == 204:
        return {"status": "no_content", "status_code": 204}

    try:
        data = resp.json()
    except Exception:
        data = {"raw_response": resp.text}

    if not resp.ok:
        return {
            "error": data,
            "status_code": resp.status_code,
        }

    return data


def get(
    path: str,
    params: Optional[dict] = None,
    extra_headers: Optional[dict] = None,
    use_order_host: bool = False,
) -> dict:
    """Perform a GET request."""
    return _make_request(
        "GET", path, params=params, extra_headers=extra_headers,
        use_order_host=use_order_host,
    )


def post(
    path: str,
    json: Optional[dict] = None,
    params: Optional[dict] = None,
    extra_headers: Optional[dict] = None,
    use_order_host: bool = False,
) -> dict:
    """Perform a POST request."""
    return _make_request(
        "POST", path, params=params, json=json, extra_headers=extra_headers,
        use_order_host=use_order_host,
    )


def get_binary(
    path: str,
    params: Optional[dict] = None,
    extra_headers: Optional[dict] = None,
) -> dict:
    """Perform a GET request expecting a binary (gzip) response.

    Returns content as base64-encoded string along with response metadata.
    """
    return _make_request(
        "GET", path, params=params, extra_headers=extra_headers, binary=True,
    )
