import os
import time
from typing import Any, Dict, Optional

import requests


EBAY_OAUTH_TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"
EBAY_OAUTH_TOKEN_URL_SANDBOX = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def get_base_url() -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"


class EbayClient:
    def __init__(self) -> None:
        self.app_id = _env("EBAY_APP_ID")
        self.cert_id = _env("EBAY_CERT_ID")
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0

    def _token_url(self) -> str:
        env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
        return EBAY_OAUTH_TOKEN_URL if env == "PRODUCTION" else EBAY_OAUTH_TOKEN_URL_SANDBOX

    def _get_token(self) -> str:
        if self._token and time.time() < (self._token_expiry - 30):
            return self._token
        if not self.app_id or not self.cert_id:
            raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")

        auth = requests.auth.HTTPBasicAuth(self.app_id, self.cert_id)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }
        resp = requests.post(self._token_url(), headers=headers, data=data, auth=auth, timeout=30)
        if resp.status_code >= 400:
            raise RuntimeError(f"OAuth token error {resp.status_code}: {resp.text}")
        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        self._token_expiry = time.time() + expires_in
        if not self._token:
            raise RuntimeError("OAuth token response missing access_token")
        return self._token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        url = get_base_url().rstrip("/") + "/" + path.lstrip("/")
        h: Dict[str, str] = {
            "Authorization": f"Bearer {self._get_token()}",
            "Accept": "application/json",
        }
        if headers:
            h.update({k: str(v) for k, v in headers.items()})

        try:
            resp = requests.request(method.upper(), url, params=params, json=json, headers=h, timeout=60)
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        content_type = resp.headers.get("Content-Type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = resp.json()
            except Exception:
                body = resp.text
        else:
            body = resp.text

        if resp.status_code >= 400:
            return {
                "error": "ebay_api_error",
                "status": resp.status_code,
                "url": url,
                "response": body,
            }
        return {"status": resp.status_code, "url": url, "response": body}
