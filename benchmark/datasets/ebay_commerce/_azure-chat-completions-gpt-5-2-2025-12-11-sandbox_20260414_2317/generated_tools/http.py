"""Shared HTTP + OAuth helpers for eBay Commerce APIs."""

from __future__ import annotations

import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayApiError(Exception):
    """Internal exception used to normalize eBay API errors."""


def _env(name: str, default: Optional[str] = None) -> str:
    val = os.environ.get(name, default)
    if val is None or val == "":
        raise ValueError(f"Missing required environment variable: {name}")
    return val


def get_environment() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "SANDBOX" if env == "SANDBOX" else "PRODUCTION"


def get_base_url(media: bool = False) -> str:
    env = get_environment()
    if media:
        return "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


@dataclass
class _TokenCache:
    access_token: str
    expires_at: float


_app_token: Optional[_TokenCache] = None
_user_token: Optional[_TokenCache] = None


def _basic_auth_header(client_id: str, client_secret: str) -> str:
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _token_url() -> str:
    return get_base_url(media=False) + "/identity/v1/oauth2/token"


def get_application_token(scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    global _app_token
    if _app_token and _app_token.expires_at > time.time() + 30:
        return _app_token.access_token

    client_id = _env("EBAY_APP_ID")
    client_secret = _env("EBAY_CERT_ID")

    resp = requests.post(
        _token_url(),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": _basic_auth_header(client_id, client_secret),
        },
        data={"grant_type": "client_credentials", "scope": scope},
        timeout=60,
    )
    if not resp.ok:
        raise EbayApiError(f"OAuth client_credentials failed: {resp.status_code} {resp.text}")
    data = resp.json()
    expires_in = int(data.get("expires_in", 7200))
    _app_token = _TokenCache(access_token=data["access_token"], expires_at=time.time() + expires_in)
    return _app_token.access_token


def get_user_access_token(scope: Optional[str] = None) -> str:
    global _user_token
    if _user_token and _user_token.expires_at > time.time() + 30:
        return _user_token.access_token

    client_id = _env("EBAY_APP_ID")
    client_secret = _env("EBAY_CERT_ID")
    refresh_token = _env("EBAY_REFRESH_TOKEN")

    form: Dict[str, str] = {"grant_type": "refresh_token", "refresh_token": refresh_token}
    if scope:
        form["scope"] = scope

    resp = requests.post(
        _token_url(),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": _basic_auth_header(client_id, client_secret),
        },
        data=form,
        timeout=60,
    )
    if not resp.ok:
        raise EbayApiError(f"OAuth refresh_token failed: {resp.status_code} {resp.text}")
    data = resp.json()
    expires_in = int(data.get("expires_in", 7200))
    _user_token = _TokenCache(access_token=data["access_token"], expires_at=time.time() + expires_in)
    return _user_token.access_token


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    user_auth: bool = False,
    media: bool = False,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Tuple[int, Dict[str, Any], Dict[str, str]]:
    """Make an authenticated request and return (status, json, headers).

    Returns empty dict for 204 or empty body.
    """

    token = get_user_access_token() if user_auth else get_application_token()
    url = get_base_url(media=media) + path

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if json_body is not None:
        headers["Content-Type"] = "application/json"
    if extra_headers:
        headers.update(extra_headers)

    resp = requests.request(method.upper(), url, headers=headers, params=params, json=json_body, timeout=60)

    out_headers = {k: v for k, v in resp.headers.items()}

    if resp.status_code == 204:
        return resp.status_code, {}, out_headers

    # Try parse JSON; if not JSON, return text.
    try:
        payload: Dict[str, Any] = resp.json() if resp.text else {}
    except Exception:
        payload = {"text": resp.text}

    if not resp.ok:
        # Normalize eBay error payloads.
        err_msg = payload.get("message") if isinstance(payload, dict) else None
        errors = payload.get("errors") if isinstance(payload, dict) else None
        return resp.status_code, {
            "error": err_msg or resp.reason,
            "status": resp.status_code,
            "errors": errors,
            "raw": payload,
        }, out_headers

    return resp.status_code, payload, out_headers
