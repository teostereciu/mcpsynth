from __future__ import annotations

import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayApiError(Exception):
    """Internal exception used to normalize error handling."""


def _env_base_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


def _token_url() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "https://api.sandbox.ebay.com/identity/v1/oauth2/token" if env == "SANDBOX" else "https://api.ebay.com/identity/v1/oauth2/token"


@dataclass
class TokenCache:
    access_token: Optional[str] = None
    expires_at: float = 0.0


_TOKEN_CACHE = TokenCache()


def get_user_access_token(scope: str) -> str:
    """Get OAuth user access token using refresh token.

    eBay refresh tokens are long-lived; access tokens are short-lived.
    We cache the access token in-process.
    """

    now = time.time()
    if _TOKEN_CACHE.access_token and now < (_TOKEN_CACHE.expires_at - 30):
        return _TOKEN_CACHE.access_token

    app_id = os.environ["EBAY_APP_ID"]
    cert_id = os.environ["EBAY_CERT_ID"]
    refresh_token = os.environ["EBAY_REFRESH_TOKEN"]

    resp = requests.post(
        _token_url(),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        auth=(app_id, cert_id),
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": scope,
        },
        timeout=30,
    )
    if resp.status_code >= 400:
        raise EbayApiError(f"OAuth token error {resp.status_code}: {resp.text}")

    data = resp.json()
    _TOKEN_CACHE.access_token = data.get("access_token")
    _TOKEN_CACHE.expires_at = now + float(data.get("expires_in", 0))
    return _TOKEN_CACHE.access_token or ""


def _normalize_error(resp: requests.Response) -> Dict[str, Any]:
    try:
        payload = resp.json()
    except Exception:
        payload = {"message": resp.text}
    return {
        "error": {
            "status_code": resp.status_code,
            "reason": resp.reason,
            "details": payload,
        }
    }


def request_json(
    method: str,
    api_root: str,
    path: str,
    *,
    scope: str,
    marketplace_id: Optional[str] = None,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    json_body: Any = None,
) -> Dict[str, Any]:
    """Make an authenticated request to an eBay Sell API.

    Args:
        api_root: e.g. '/sell/inventory/v1'
        path: endpoint path beginning with '/'
    """

    token = get_user_access_token(scope)
    base_url = _env_base_url()

    req_headers: Dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if marketplace_id:
        req_headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if headers:
        req_headers.update({k: v for k, v in headers.items() if v is not None})

    url = f"{base_url}{api_root}{path}"

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=req_headers,
            params=params,
            json=json_body,
            timeout=60,
        )
    except requests.RequestException as e:
        return {"error": {"message": str(e)}}

    if resp.status_code == 204:
        return {"status": 204}

    if resp.status_code >= 400:
        return _normalize_error(resp)

    if not resp.content:
        return {"status": resp.status_code}

    try:
        return resp.json()
    except Exception:
        return {"status": resp.status_code, "text": resp.text}
