import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def get_environment() -> str:
    return (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()


def get_base_url(is_media: bool = False) -> str:
    env = get_environment()
    if env not in ("SANDBOX", "PRODUCTION"):
        env = "SANDBOX"
    if is_media:
        return "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


@dataclass
class OAuthToken:
    access_token: str
    token_type: str
    expires_in: int
    obtained_at: float

    @property
    def expires_at(self) -> float:
        return self.obtained_at + max(0, int(self.expires_in) - 30)

    def is_expired(self) -> bool:
        return time.time() >= self.expires_at


class EbayAuth:
    """Handles both application and user tokens.

    - Application token: client_credentials
    - User token: refresh_token
    """

    def __init__(self) -> None:
        self._app_token: Optional[OAuthToken] = None
        self._user_token: Optional[OAuthToken] = None

    def _token_url(self) -> str:
        return f"{get_base_url(is_media=False)}/identity/v1/oauth2/token"

    def _basic_auth_header(self) -> str:
        client_id = _env("EBAY_APP_ID")
        client_secret = _env("EBAY_CERT_ID")
        if not client_id or not client_secret:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        raw = f"{client_id}:{client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_app_token(self, scope: str) -> str:
        if self._app_token and not self._app_token.is_expired():
            return self._app_token.access_token

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }
        r = requests.post(self._token_url(), headers=headers, data=data, timeout=30)
        if r.status_code >= 400:
            return json.dumps({"error": "oauth_error", "status": r.status_code, "body": _safe_json(r)})
        payload = r.json()
        self._app_token = OAuthToken(
            access_token=payload["access_token"],
            token_type=payload.get("token_type", "Bearer"),
            expires_in=int(payload.get("expires_in", 0)),
            obtained_at=time.time(),
        )
        return self._app_token.access_token

    def get_user_token(self, scope: str) -> str:
        if self._user_token and not self._user_token.is_expired():
            return self._user_token.access_token

        refresh_token = _env("EBAY_REFRESH_TOKEN")
        if not refresh_token:
            raise ValueError("Missing EBAY_REFRESH_TOKEN")

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": scope,
        }
        r = requests.post(self._token_url(), headers=headers, data=data, timeout=30)
        if r.status_code >= 400:
            return json.dumps({"error": "oauth_error", "status": r.status_code, "body": _safe_json(r)})
        payload = r.json()
        self._user_token = OAuthToken(
            access_token=payload["access_token"],
            token_type=payload.get("token_type", "Bearer"),
            expires_in=int(payload.get("expires_in", 0)),
            obtained_at=time.time(),
        )
        return self._user_token.access_token


def _safe_json(r: requests.Response) -> Any:
    try:
        return r.json()
    except Exception:
        return {"text": r.text}


def request_json(
    *,
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Any = None,
    is_media: bool = False,
    access_token: Optional[str] = None,
) -> Dict[str, Any]:
    url = get_base_url(is_media=is_media) + path
    h: Dict[str, str] = {"Accept": "application/json"}
    if headers:
        h.update({k: str(v) for k, v in headers.items() if v is not None})
    if access_token:
        h["Authorization"] = f"Bearer {access_token}"

    try:
        r = requests.request(method, url, params=query, headers=h, json=json_body, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        return {
            "error": "http_error",
            "status": r.status_code,
            "url": url,
            "response": _safe_json(r),
        }

    if r.status_code == 204:
        return {"status": 204, "ok": True}

    return _safe_json(r)
