import base64
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


@dataclass
class EbayConfig:
    app_id: str
    cert_id: str
    environment: str = "SANDBOX"  # SANDBOX or PRODUCTION

    @property
    def base_url(self) -> str:
        env = (self.environment or "SANDBOX").upper()
        return "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"

    @property
    def oauth_base_url(self) -> str:
        # OAuth is also environment-specific
        return self.base_url


class EbayAuth:
    def __init__(self, config: EbayConfig):
        self.config = config
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _basic_auth_header(self) -> str:
        raw = f"{self.config.app_id}:{self.config.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def get_app_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> str:
        now = time.time()
        if self._token and now < (self._token_expiry - 30):
            return self._token

        url = f"{self.config.oauth_base_url}/identity/v1/oauth2/token"
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": scope,
        }
        resp = requests.post(url, headers=headers, data=data, timeout=30)
        if resp.status_code >= 400:
            return ""
        payload = resp.json()
        token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        if not token:
            return ""
        self._token = token
        self._token_expiry = now + float(expires_in)
        return token


class EbayClient:
    def __init__(self, config: Optional[EbayConfig] = None):
        if config is None:
            config = EbayConfig(
                app_id=os.environ.get("EBAY_APP_ID", ""),
                cert_id=os.environ.get("EBAY_CERT_ID", ""),
                environment=os.environ.get("EBAY_ENVIRONMENT", "SANDBOX"),
            )
        self.config = config
        self.auth = EbayAuth(config)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        scope: str = "https://api.ebay.com/oauth/api_scope",
    ) -> Dict[str, Any]:
        if not self.config.app_id or not self.config.cert_id:
            return {"error": "Missing EBAY_APP_ID/EBAY_CERT_ID environment variables"}

        token = self.auth.get_app_token(scope=scope)
        if not token:
            return {"error": "Failed to obtain OAuth token. Check credentials and environment."}

        url = self.config.base_url + path
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if headers:
            req_headers.update(headers)

        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                json=json,
                headers=req_headers,
                timeout=30,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            # Try to parse eBay error payload
            try:
                err = resp.json() if "json" in content_type else {"message": resp.text}
            except Exception:
                err = {"message": resp.text}
            return {
                "error": "eBay API error",
                "status_code": resp.status_code,
                "details": err,
            }

        if resp.status_code == 204:
            return {"status_code": 204}

        if "json" in content_type:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON response", "raw": resp.text}

        return {"raw": resp.text, "content_type": content_type, "status_code": resp.status_code}
