import os
import time
from typing import Any, Dict, Optional

import requests


class EbayAuth:
    """OAuth2 Client Credentials for eBay Buy APIs (application access token)."""

    def __init__(self) -> None:
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    @staticmethod
    def base_url() -> str:
        env = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()
        if env == "PRODUCTION":
            return "https://api.ebay.com"
        return "https://api.sandbox.ebay.com"

    @staticmethod
    def _token_url() -> str:
        # OAuth token endpoint is on api.ebay.com / api.sandbox.ebay.com
        return f"{EbayAuth.base_url()}/identity/v1/oauth2/token"

    @staticmethod
    def _basic_auth_header(client_id: str, client_secret: str) -> str:
        import base64

        raw = f"{client_id}:{client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_token(self, scope: str) -> Dict[str, Any]:
        """Return a valid access token string in a dict: {access_token, expires_in}."""
        now = time.time()
        if self._token and now < (self._token_expiry - 30):
            return {"access_token": self._token, "expires_in": int(self._token_expiry - now)}

        client_id = os.getenv("EBAY_APP_ID")
        client_secret = os.getenv("EBAY_CERT_ID")
        if not client_id or not client_secret:
            return {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID environment variables"}

        headers = {
            "Authorization": self._basic_auth_header(client_id, client_secret),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }

        try:
            resp = requests.post(self._token_url(), headers=headers, data=data, timeout=30)
        except Exception as e:
            return {"error": f"Token request failed: {e}"}

        if resp.status_code >= 400:
            return {"error": f"Token request failed: HTTP {resp.status_code}", "details": _safe_json(resp)}

        payload = _safe_json(resp)
        token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        if not token:
            return {"error": "Token response missing access_token", "details": payload}

        self._token = token
        self._token_expiry = time.time() + int(expires_in)
        return {"access_token": token, "expires_in": int(expires_in)}


def _safe_json(resp: requests.Response) -> Any:
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text}
