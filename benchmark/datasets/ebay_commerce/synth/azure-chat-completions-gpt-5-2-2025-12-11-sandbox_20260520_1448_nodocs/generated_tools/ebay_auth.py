import os
import time
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import requests


EBAY_OAUTH_BASE = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


@dataclass
class Token:
    access_token: str
    token_type: str
    expires_at: float
    scope: Optional[str] = None

    def is_expired(self, skew_seconds: int = 60) -> bool:
        return time.time() >= (self.expires_at - skew_seconds)


class EbayAuth:
    """OAuth helper for eBay Commerce APIs.

    Supports:
      - client credentials token (application token)
      - refresh token exchange (user token)

    Caches tokens in-memory.
    """

    def __init__(self):
        self.client_id = os.getenv("EBAY_APP_ID", "").strip()
        self.client_secret = os.getenv("EBAY_CERT_ID", "").strip()
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "").strip()
        self.environment = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
        self.oauth_base = EBAY_OAUTH_BASE.get(self.environment, EBAY_OAUTH_BASE["SANDBOX"])

        self._app_token: Optional[Token] = None
        self._user_token_by_scope: Dict[str, Token] = {}

    def _basic_auth_header(self) -> str:
        import base64

        raw = f"{self.client_id}:{self.client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _token_endpoint(self) -> str:
        return f"{self.oauth_base}/identity/v1/oauth2/token"

    def _request_token(self, data: Dict[str, str]) -> Tuple[Optional[Token], Optional[dict]]:
        if not self.client_id or not self.client_secret:
            return None, {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID env var"}

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        try:
            r = requests.post(self._token_endpoint(), headers=headers, data=data, timeout=30)
        except Exception as e:
            return None, {"error": f"Token request failed: {e}"}

        if r.status_code >= 400:
            try:
                return None, {"error": "Token request error", "status": r.status_code, "body": r.json()}
            except Exception:
                return None, {"error": "Token request error", "status": r.status_code, "body": r.text}

        payload = r.json()
        expires_in = float(payload.get("expires_in", 0))
        tok = Token(
            access_token=payload["access_token"],
            token_type=payload.get("token_type", "Bearer"),
            expires_at=time.time() + expires_in,
            scope=payload.get("scope"),
        )
        return tok, None

    def get_app_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> Tuple[Optional[str], Optional[dict]]:
        if self._app_token and not self._app_token.is_expired():
            return self._app_token.access_token, None

        tok, err = self._request_token(
            {
                "grant_type": "client_credentials",
                "scope": scope,
            }
        )
        if err:
            return None, err
        self._app_token = tok
        return tok.access_token, None

    def get_user_token(self, scope: str) -> Tuple[Optional[str], Optional[dict]]:
        if not self.refresh_token:
            return None, {"error": "Missing EBAY_REFRESH_TOKEN env var"}

        cached = self._user_token_by_scope.get(scope)
        if cached and not cached.is_expired():
            return cached.access_token, None

        tok, err = self._request_token(
            {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "scope": scope,
            }
        )
        if err:
            return None, err
        self._user_token_by_scope[scope] = tok
        return tok.access_token, None
