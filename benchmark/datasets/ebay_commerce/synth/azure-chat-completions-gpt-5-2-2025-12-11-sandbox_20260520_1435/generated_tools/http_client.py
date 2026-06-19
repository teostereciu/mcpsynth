import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


@dataclass
class OAuthToken:
    access_token: str
    expires_at: float


class EbayOAuth:
    """Handles eBay OAuth tokens for both application and user contexts."""

    def __init__(self):
        self.client_id = os.getenv("EBAY_APP_ID", "").strip()
        self.client_secret = os.getenv("EBAY_CERT_ID", "").strip()
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "").strip()
        self.environment = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()

        if self.environment not in {"SANDBOX", "PRODUCTION"}:
            self.environment = "SANDBOX"

        self._app_token: Optional[OAuthToken] = None
        self._user_token: Optional[OAuthToken] = None

    @property
    def api_base(self) -> str:
        return "https://api.ebay.com" if self.environment == "PRODUCTION" else "https://api.sandbox.ebay.com"

    @property
    def apim_base(self) -> str:
        return "https://apim.ebay.com" if self.environment == "PRODUCTION" else "https://apim.sandbox.ebay.com"

    @property
    def oauth_base(self) -> str:
        # eBay OAuth uses same host as api base
        return self.api_base

    def _basic_auth_header(self) -> str:
        raw = f"{self.client_id}:{self.client_secret}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _request_token(self, grant_type: str, scope: Optional[str] = None, refresh_token: Optional[str] = None) -> Dict[str, Any]:
        url = f"{self.oauth_base}/identity/v1/oauth2/token"
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": grant_type}
        if scope:
            data["scope"] = scope
        if refresh_token:
            data["refresh_token"] = refresh_token
        resp = requests.post(url, headers=headers, data=data, timeout=60)
        try:
            payload = resp.json()
        except Exception:
            payload = {"raw": resp.text}
        if resp.status_code >= 400:
            return {"error": "oauth_error", "status": resp.status_code, "details": payload}
        return payload

    def get_app_token(self, scope: str) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
        if not self.client_id or not self.client_secret:
            return None, {"error": "missing_credentials", "details": "Set EBAY_APP_ID and EBAY_CERT_ID"}
        now = time.time()
        if self._app_token and self._app_token.expires_at - 30 > now:
            return self._app_token.access_token, None
        payload = self._request_token("client_credentials", scope=scope)
        if "error" in payload and payload.get("error") == "oauth_error":
            return None, payload
        token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not token or expires_in <= 0:
            return None, {"error": "oauth_error", "details": payload}
        self._app_token = OAuthToken(access_token=token, expires_at=now + expires_in)
        return token, None

    def get_user_token(self, scope: str) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
        if not self.client_id or not self.client_secret or not self.refresh_token:
            return None, {"error": "missing_credentials", "details": "Set EBAY_APP_ID, EBAY_CERT_ID, and EBAY_REFRESH_TOKEN"}
        now = time.time()
        if self._user_token and self._user_token.expires_at - 30 > now:
            return self._user_token.access_token, None
        payload = self._request_token("refresh_token", scope=scope, refresh_token=self.refresh_token)
        if "error" in payload and payload.get("error") == "oauth_error":
            return None, payload
        token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        if not token or expires_in <= 0:
            return None, {"error": "oauth_error", "details": payload}
        self._user_token = OAuthToken(access_token=token, expires_at=now + expires_in)
        return token, None


class EbayHTTP:
    def __init__(self, oauth: Optional[EbayOAuth] = None):
        self.oauth = oauth or EbayOAuth()

    def request(
        self,
        method: str,
        base: str,
        path: str,
        *,
        scope: str,
        user: bool = False,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        files: Any = None,
    ) -> Dict[str, Any]:
        token, err = (self.oauth.get_user_token(scope) if user else self.oauth.get_app_token(scope))
        if err:
            return err
        url = base.rstrip("/") + "/" + path.lstrip("/")
        h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        if headers:
            h.update({k: v for k, v in headers.items() if v is not None})
        try:
            resp = requests.request(method.upper(), url, headers=h, params=params, json=json, data=data, files=files, timeout=120)
        except Exception as e:
            return {"error": "request_failed", "details": str(e), "url": url}

        content_type = resp.headers.get("Content-Type", "")
        parsed: Any
        if "application/json" in content_type:
            try:
                parsed = resp.json()
            except Exception:
                parsed = {"raw": resp.text}
        else:
            parsed = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "http_error",
                "status": resp.status_code,
                "url": url,
                "details": parsed,
            }
        return parsed
