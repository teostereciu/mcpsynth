from __future__ import annotations

import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayApiError(Exception):
    pass


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.environ.get(name, default)
    if v is None or v == "":
        raise EbayApiError(f"Missing required environment variable: {name}")
    return v


def _is_sandbox() -> bool:
    return os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper() == "SANDBOX"


def commerce_base_url() -> str:
    return "https://api.sandbox.ebay.com" if _is_sandbox() else "https://api.ebay.com"


def media_base_url() -> str:
    return "https://apim.sandbox.ebay.com" if _is_sandbox() else "https://apim.ebay.com"


@dataclass
class _TokenCache:
    token: str
    expires_at: float


_app_token_cache: Optional[_TokenCache] = None
_user_token_cache: Optional[_TokenCache] = None


def _oauth_token_url() -> str:
    return f"{commerce_base_url()}/identity/v1/oauth2/token"


def _basic_auth_header(client_id: str, client_secret: str) -> str:
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def get_application_token(scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    global _app_token_cache
    if _app_token_cache and _app_token_cache.expires_at - time.time() > 30:
        return _app_token_cache.token

    client_id = _env("EBAY_APP_ID")
    client_secret = _env("EBAY_CERT_ID")

    resp = requests.post(
        _oauth_token_url(),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": _basic_auth_header(client_id, client_secret),
        },
        data={"grant_type": "client_credentials", "scope": scope},
        timeout=60,
    )
    if not resp.ok:
        return _raise_as_api_error(resp)
    data = resp.json()
    token = data.get("access_token")
    expires_in = int(data.get("expires_in", 7200))
    if not token:
        raise EbayApiError("OAuth response missing access_token")
    _app_token_cache = _TokenCache(token=token, expires_at=time.time() + expires_in)
    return token


def get_user_access_token(scope: Optional[str] = None) -> str:
    global _user_token_cache
    if _user_token_cache and _user_token_cache.expires_at - time.time() > 30:
        return _user_token_cache.token

    client_id = _env("EBAY_APP_ID")
    client_secret = _env("EBAY_CERT_ID")
    refresh_token = _env("EBAY_REFRESH_TOKEN")

    form: Dict[str, str] = {"grant_type": "refresh_token", "refresh_token": refresh_token}
    if scope:
        form["scope"] = scope

    resp = requests.post(
        _oauth_token_url(),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": _basic_auth_header(client_id, client_secret),
        },
        data=form,
        timeout=60,
    )
    if not resp.ok:
        return _raise_as_api_error(resp)
    data = resp.json()
    token = data.get("access_token")
    expires_in = int(data.get("expires_in", 7200))
    if not token:
        raise EbayApiError("OAuth response missing access_token")
    _user_token_cache = _TokenCache(token=token, expires_at=time.time() + expires_in)
    return token


def _raise_as_api_error(resp: requests.Response):
    try:
        payload = resp.json()
    except Exception:
        payload = {"message": resp.text}
    raise EbayApiError(
        f"HTTP {resp.status_code} {resp.reason}: {payload}")


def request_json(
    method: str,
    base_url: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    user_auth: bool = False,
    scope: Optional[str] = None,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    token = get_user_access_token(scope=scope) if user_auth else get_application_token(scope=scope or "https://api.ebay.com/oauth/api_scope")

    headers: Dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if json_body is not None:
        headers["Content-Type"] = "application/json"
    if extra_headers:
        headers.update(extra_headers)

    url = base_url.rstrip("/") + "/" + path.lstrip("/")

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=params, json=json_body, timeout=60)
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {}

    if not resp.ok:
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {"error": {"status": resp.status_code, "reason": resp.reason, "details": err}, "url": url}

    try:
        return resp.json()
    except Exception:
        return {"raw": resp.text}
