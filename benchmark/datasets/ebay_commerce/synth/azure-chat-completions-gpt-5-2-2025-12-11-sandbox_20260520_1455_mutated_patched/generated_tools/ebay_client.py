from __future__ import annotations

import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.getenv(name, default)
    if v is None or v == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return v


def _environment() -> str:
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()


def _standard_base_url() -> str:
    return "https://api.ebay.com" if _environment() == "PRODUCTION" else "https://api.sandbox.ebay.com"


def _media_base_url() -> str:
    return "https://apim.ebay.com" if _environment() == "PRODUCTION" else "https://apim.sandbox.ebay.com"


def _identity_base_url() -> str:
    return "https://apiz.ebay.com" if _environment() == "PRODUCTION" else "https://apiz.sandbox.ebay.com"


def _oauth_base_url() -> str:
    return "https://api.ebay.com" if _environment() == "PRODUCTION" else "https://api.sandbox.ebay.com"


@dataclass
class _TokenCache:
    access_token: str
    expires_at: float


class EbayClient:
    def __init__(self, base_url: str, user_scoped: bool):
        self.base_url = base_url.rstrip("/")
        self.user_scoped = user_scoped
        self._token_cache: Optional[_TokenCache] = None

    @staticmethod
    def for_standard_api(user_scoped: bool) -> "EbayClient":
        return EbayClient(_standard_base_url(), user_scoped=user_scoped)

    @staticmethod
    def for_media_api(user_scoped: bool) -> "EbayClient":
        return EbayClient(_media_base_url(), user_scoped=user_scoped)

    @staticmethod
    def for_identity_api(user_scoped: bool) -> "EbayClient":
        return EbayClient(_identity_base_url(), user_scoped=user_scoped)

    def _get_access_token(self) -> str:
        now = time.time()
        if self._token_cache and self._token_cache.expires_at - 30 > now:
            return self._token_cache.access_token

        client_id = _env("EBAY_APP_ID")
        client_secret = _env("EBAY_CERT_ID")

        if self.user_scoped:
            refresh_token = _env("EBAY_REFRESH_TOKEN")
            data = {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
            }
        else:
            data = {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            }

        basic = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
        headers = {
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        resp = requests.post(f"{_oauth_base_url()}/identity/v1/oauth2/token", headers=headers, data=data, timeout=30)
        if resp.status_code >= 400:
            return json.dumps({"error": "oauth_error", "status": resp.status_code, "body": _safe_json(resp)})

        payload = resp.json()
        token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not token:
            raise RuntimeError(f"OAuth response missing access_token: {payload}")

        self._token_cache = _TokenCache(access_token=token, expires_at=now + expires_in)
        return token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Any = None,
        files: Any = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        req_headers: Dict[str, str] = {"Authorization": f"Bearer {self._get_access_token()}"}
        if headers:
            req_headers.update({k: v for k, v in headers.items() if v is not None})

        # If a query param value is a dict/list, encode as JSON string (e.g., taxonomy fetch_item_aspects).
        if params:
            params = {k: (json_dumps(v) if isinstance(v, (dict, list)) else v) for k, v in params.items() if v is not None}

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                headers=req_headers,
                json=json,
                files=files,
                timeout=60,
            )
        except requests.RequestException as e:
            return {"error": "request_exception", "message": str(e)}

        if resp.status_code == 204:
            return {"status": 204, "data": None}

        if resp.status_code >= 400:
            return {
                "error": "http_error",
                "status": resp.status_code,
                "body": _safe_json(resp),
                "headers": {k: v for k, v in resp.headers.items()},
            }

        return {"status": resp.status_code, "data": _safe_json(resp), "headers": {k: v for k, v in resp.headers.items()}}


def json_dumps(v: Any) -> str:
    return json.dumps(v, separators=(",", ":"), ensure_ascii=False)


def _safe_json(resp: requests.Response) -> Any:
    ct = (resp.headers.get("Content-Type") or "").lower()
    if "application/json" in ct or "json" in ct:
        try:
            return resp.json()
        except Exception:
            return resp.text
    try:
        return resp.json()
    except Exception:
        return resp.text
