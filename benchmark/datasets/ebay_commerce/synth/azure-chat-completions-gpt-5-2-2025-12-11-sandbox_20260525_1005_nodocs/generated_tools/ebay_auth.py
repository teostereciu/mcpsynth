import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class EbayAuthError(Exception):
    pass


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def get_environment() -> str:
    return (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()


def get_base_url() -> str:
    env = get_environment()
    return "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"


def get_media_base_url() -> str:
    env = get_environment()
    return "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"


@dataclass
class Token:
    access_token: str
    expires_at: float
    token_type: str = "Bearer"
    scope: Optional[str] = None

    def is_expired(self, skew_seconds: int = 60) -> bool:
        return time.time() >= (self.expires_at - skew_seconds)


class EbayTokenManager:
    """Caches application and user tokens in-memory."""

    def __init__(self) -> None:
        self._app_token: Optional[Token] = None
        self._user_token: Optional[Token] = None

    @staticmethod
    def _basic_auth_header(client_id: str, client_secret: str) -> str:
        import base64

        raw = f"{client_id}:{client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _token_endpoint(self) -> str:
        return get_base_url() + "/identity/v1/oauth2/token"

    def _request_token(self, grant_type: str, data: Dict[str, str]) -> Token:
        client_id = _env("EBAY_APP_ID")
        client_secret = _env("EBAY_CERT_ID")
        if not client_id or not client_secret:
            raise EbayAuthError("Missing EBAY_APP_ID or EBAY_CERT_ID")

        headers = {
            "Authorization": self._basic_auth_header(client_id, client_secret),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        payload = {"grant_type": grant_type, **data}
        r = requests.post(self._token_endpoint(), headers=headers, data=payload, timeout=30)
        if r.status_code >= 400:
            raise EbayAuthError(f"Token request failed: {r.status_code} {r.text}")
        j = r.json()
        access_token = j.get("access_token")
        expires_in = j.get("expires_in")
        if not access_token or not expires_in:
            raise EbayAuthError(f"Unexpected token response: {j}")
        return Token(
            access_token=access_token,
            expires_at=time.time() + float(expires_in),
            token_type=j.get("token_type", "Bearer"),
            scope=j.get("scope"),
        )

    def get_app_token(self, scope: Optional[str] = None) -> Token:
        if self._app_token and not self._app_token.is_expired():
            return self._app_token
        data: Dict[str, str] = {}
        if scope:
            data["scope"] = scope
        self._app_token = self._request_token("client_credentials", data)
        return self._app_token

    def get_user_token(self, scope: Optional[str] = None) -> Token:
        if self._user_token and not self._user_token.is_expired():
            return self._user_token
        refresh_token = _env("EBAY_REFRESH_TOKEN")
        if not refresh_token:
            raise EbayAuthError("Missing EBAY_REFRESH_TOKEN")
        data: Dict[str, str] = {"refresh_token": refresh_token}
        if scope:
            data["scope"] = scope
        self._user_token = self._request_token("refresh_token", data)
        return self._user_token


TOKEN_MANAGER = EbayTokenManager()


def auth_header(user: bool = False, scope: Optional[str] = None) -> Dict[str, str]:
    tok = TOKEN_MANAGER.get_user_token(scope=scope) if user else TOKEN_MANAGER.get_app_token(scope=scope)
    return {"Authorization": f"{tok.token_type} {tok.access_token}"}


def request_json(
    method: str,
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Any = None,
    timeout: int = 30,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Returns (result, error)."""
    try:
        r = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            timeout=timeout,
        )
    except Exception as e:
        return None, {"error": str(e)}

    ct = (r.headers.get("content-type") or "").lower()
    if r.status_code >= 400:
        # Try to parse JSON error
        if "application/json" in ct:
            try:
                return None, {"error": r.json(), "status": r.status_code}
            except Exception:
                return None, {"error": r.text, "status": r.status_code}
        return None, {"error": r.text, "status": r.status_code}

    if r.status_code == 204:
        return {"ok": True, "status": 204}, None

    if "application/json" in ct:
        try:
            return r.json(), None
        except Exception:
            return {"raw": r.text}, None

    return {"raw": r.text}, None
