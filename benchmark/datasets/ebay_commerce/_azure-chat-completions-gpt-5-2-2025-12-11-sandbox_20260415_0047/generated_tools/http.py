"""HTTP + OAuth helpers for eBay Commerce APIs."""

from __future__ import annotations

import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


class EbayApiError(Exception):
    """Internal exception used for control flow; tools should convert to dict errors."""


def _env(name: str, default: Optional[str] = None) -> str:
    val = os.environ.get(name, default)
    if val is None or val == "":
        raise EbayApiError(f"Missing required environment variable: {name}")
    return val


def get_environment() -> str:
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return "SANDBOX" if env not in ("SANDBOX", "PRODUCTION") else env


def get_api_base_url() -> str:
    return "https://api.sandbox.ebay.com" if get_environment() == "SANDBOX" else "https://api.ebay.com"


def get_media_base_url() -> str:
    return "https://apim.sandbox.ebay.com" if get_environment() == "SANDBOX" else "https://apim.ebay.com"


@dataclass
class _Token:
    access_token: str
    expires_at: float


_app_token: Optional[_Token] = None
_user_token: Optional[_Token] = None


def _basic_auth_header(client_id: str, client_secret: str) -> str:
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _token_url() -> str:
    return f"{get_api_base_url()}/identity/v1/oauth2/token"


def get_application_token(scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    global _app_token
    if _app_token and _app_token.expires_at - time.time() > 30:
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
    expires_in = float(data.get("expires_in", 7200))
    _app_token = _Token(access_token=data["access_token"], expires_at=time.time() + expires_in)
    return _app_token.access_token


def get_user_access_token(scope: Optional[str] = None) -> str:
    global _user_token
    if _user_token and _user_token.expires_at - time.time() > 30:
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
    expires_in = float(data.get("expires_in", 7200))
    _user_token = _Token(access_token=data["access_token"], expires_at=time.time() + expires_in)
    return _user_token.access_token


def request_json(
    *,
    method: str,
    base_url: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    user_auth: bool = False,
    scope: Optional[str] = None,
) -> Dict[str, Any]:
    """Make an authenticated request and return JSON or {} for 204.

    Tools should catch EbayApiError and return a JSON-serializable error dict.
    """

    token = get_user_access_token(scope=scope) if user_auth else get_application_token(scope=scope or "https://api.ebay.com/oauth/api_scope")

    req_headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if json_body is not None:
        req_headers["Content-Type"] = "application/json"
    if headers:
        req_headers.update(headers)

    url = f"{base_url}{path}"
    resp = requests.request(method=method.upper(), url=url, params=params, json=json_body, headers=req_headers, timeout=60)

    if resp.status_code == 204:
        return {}

    if not resp.ok:
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        raise EbayApiError(
            f"eBay API error {resp.status_code} for {method.upper()} {path}: {err}",
        ) from None

    if resp.content:
        return resp.json()
    return {}


def error_dict(exc: Exception) -> Dict[str, Any]:
    return {"error": str(exc)}
