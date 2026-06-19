import os
import time
from typing import Any, Dict, Optional

import requests


class EbayOAuthError(Exception):
    pass


class EbayClient:
    """Minimal eBay REST client with refresh-token OAuth for Sell APIs."""

    TOKEN_PATH = "/identity/v1/oauth2/token"

    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()

        if self.environment not in {"SANDBOX", "PRODUCTION"}:
            self.environment = "SANDBOX"

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )

        self._access_token: Optional[str] = None
        self._access_token_exp: float = 0.0

    def _basic_auth_header(self) -> str:
        if not self.app_id or not self.cert_id:
            raise EbayOAuthError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        import base64

        token = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"

    def get_access_token(self, scopes: Optional[str] = None) -> str:
        if self._access_token and time.time() < (self._access_token_exp - 30):
            return self._access_token

        if not self.refresh_token:
            raise EbayOAuthError("Missing EBAY_REFRESH_TOKEN")

        url = self.base_url + self.TOKEN_PATH
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        if scopes:
            data["scope"] = scopes

        resp = requests.post(url, headers=headers, data=data, timeout=60)
        if resp.status_code >= 400:
            return {
                "error": "oauth_error",
                "status": resp.status_code,
                "body": _safe_json(resp),
            }  # type: ignore[return-value]

        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = payload.get("expires_in") or 0
        self._access_token_exp = time.time() + float(expires_in)
        if not self._access_token:
            raise EbayOAuthError("OAuth response missing access_token")
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_language: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        try:
            token = self.get_access_token(scope)
        except Exception as e:
            return {"error": "auth_error", "message": str(e)}

        url = self.base_url + path
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if json is not None:
            req_headers["Content-Type"] = "application/json"
        if content_language:
            req_headers["Content-Language"] = content_language
        if headers:
            req_headers.update(headers)

        try:
            resp = requests.request(method, url, params=params, json=json, headers=req_headers, timeout=60)
        except requests.RequestException as e:
            return {"error": "request_error", "message": str(e)}

        if resp.status_code == 204:
            return {"status": 204}

        body = _safe_json(resp)
        if resp.status_code >= 400:
            return {"error": "api_error", "status": resp.status_code, "body": body}
        return body if isinstance(body, dict) else {"data": body, "status": resp.status_code}


def _safe_json(resp: requests.Response):
    try:
        return resp.json()
    except Exception:
        return resp.text
