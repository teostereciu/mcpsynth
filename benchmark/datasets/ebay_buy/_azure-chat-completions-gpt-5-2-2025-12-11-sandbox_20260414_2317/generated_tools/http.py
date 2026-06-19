"""HTTP + auth helpers for eBay Buy APIs."""

from __future__ import annotations

import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


class EbayApiError(Exception):
    """Internal exception used for control flow; should be converted to dicts at tool boundary."""


@dataclass
class EbayConfig:
    app_id: str
    cert_id: str
    environment: str = "SANDBOX"  # SANDBOX or PRODUCTION
    marketplace_id: str = "EBAY_US"

    @property
    def base_url(self) -> str:
        return "https://api.sandbox.ebay.com" if self.environment.upper() == "SANDBOX" else "https://api.ebay.com"

    @property
    def token_url(self) -> str:
        return (
            "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
            if self.environment.upper() == "SANDBOX"
            else "https://api.ebay.com/identity/v1/oauth2/token"
        )


_TOKEN_CACHE: Dict[str, Dict[str, Any]] = {}


def _basic_auth_header(client_id: str, client_secret: str) -> str:
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def get_config(
    *,
    marketplace_id: Optional[str] = None,
    environment: Optional[str] = None,
) -> EbayConfig:
    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise EbayApiError("Missing EBAY_APP_ID/EBAY_CERT_ID environment variables")

    env = (environment or os.environ.get("EBAY_ENVIRONMENT") or "SANDBOX").upper()
    mp = marketplace_id or os.environ.get("EBAY_MARKETPLACE_ID") or "EBAY_US"
    return EbayConfig(app_id=app_id, cert_id=cert_id, environment=env, marketplace_id=mp)


def get_application_token(config: EbayConfig, *, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
    cache_key = f"{config.environment}:{config.app_id}:{scope}"
    cached = _TOKEN_CACHE.get(cache_key)
    now = time.time()
    if cached and cached.get("expires_at", 0) > now + 30:
        return str(cached["access_token"])

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": _basic_auth_header(config.app_id, config.cert_id),
    }
    data = {"grant_type": "client_credentials", "scope": scope}

    resp = requests.post(config.token_url, headers=headers, data=data, timeout=30)
    if resp.status_code >= 400:
        raise EbayApiError(f"OAuth token request failed: {resp.status_code} {resp.text}")

    payload = resp.json()
    access_token = payload.get("access_token")
    expires_in = int(payload.get("expires_in", 0) or 0)
    if not access_token:
        raise EbayApiError("OAuth token response missing access_token")

    _TOKEN_CACHE[cache_key] = {"access_token": access_token, "expires_at": now + max(expires_in, 0)}
    return str(access_token)


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    marketplace_id: Optional[str] = None,
    environment: Optional[str] = None,
    extra_headers: Optional[Dict[str, str]] = None,
    scope: str = "https://api.ebay.com/oauth/api_scope",
) -> Dict[str, Any]:
    config = get_config(marketplace_id=marketplace_id, environment=environment)
    token = get_application_token(config, scope=scope)

    url = f"{config.base_url}{path}"
    headers: Dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": config.marketplace_id,
    }
    if extra_headers:
        headers.update(extra_headers)

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=params, json=json_body, timeout=30)
    except requests.RequestException as e:
        raise EbayApiError(f"Network error calling eBay API: {e}")

    if resp.status_code >= 400:
        # eBay errors are often JSON, but not always.
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        raise EbayApiError(
            f"eBay API error {resp.status_code} for {method.upper()} {path}",
        ) from EbayApiError(str(err))

    if resp.status_code == 204:
        return {}

    try:
        return resp.json()
    except Exception:
        return {"raw": resp.text}


def tool_safe_call(fn, *args, **kwargs):
    """Run an API call and convert expected errors to JSON-serializable dicts."""

    try:
        return fn(*args, **kwargs)
    except EbayApiError as e:
        # If chained exception contains JSON-ish dict in its message, include it.
        detail: Any = None
        if e.__cause__ is not None:
            detail = str(e.__cause__)
        return {"error": str(e), "detail": detail}
    except Exception as e:  # unexpected
        return {"error": "Unexpected error", "detail": str(e)}
