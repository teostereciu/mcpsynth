import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


EBAY_OAUTH_TOKEN_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com/identity/v1/oauth2/token",
    "PRODUCTION": "https://api.ebay.com/identity/v1/oauth2/token",
}

EBAY_API_BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

EBAY_MEDIA_BASE_URLS = {
    "SANDBOX": "https://apim.sandbox.ebay.com",
    "PRODUCTION": "https://apim.ebay.com",
}


@dataclass
class OAuthToken:
    access_token: str
    expires_at: float
    token_type: str = "Bearer"
    scope: Optional[str] = None

    def is_expired(self) -> bool:
        return time.time() >= (self.expires_at - 30)


class EbayAuth:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self.environment = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
        if self.environment not in ("SANDBOX", "PRODUCTION"):
            self.environment = "SANDBOX"

        self._app_token: Optional[OAuthToken] = None
        self._user_token: Optional[OAuthToken] = None

    @property
    def api_base_url(self) -> str:
        return EBAY_API_BASE_URLS[self.environment]

    @property
    def media_base_url(self) -> str:
        return EBAY_MEDIA_BASE_URLS[self.environment]

    @property
    def token_url(self) -> str:
        return EBAY_OAUTH_TOKEN_URLS[self.environment]

    def _basic_auth_header(self) -> str:
        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return "Basic " + base64.b64encode(raw).decode("ascii")

    def _request_token(self, data: Dict[str, str]) -> Tuple[Optional[OAuthToken], Optional[Dict[str, Any]]]:
        if not self.app_id or not self.cert_id:
            return None, {"error": "Missing EBAY_APP_ID/EBAY_CERT_ID env vars"}

        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        try:
            resp = requests.post(self.token_url, headers=headers, data=data, timeout=30)
        except Exception as e:
            return None, {"error": f"Token request failed: {e}"}

        if resp.status_code >= 400:
            return None, {"error": "Token request error", "status": resp.status_code, "body": _safe_json(resp)}

        payload = _safe_json(resp)
        access_token = payload.get("access_token")
        expires_in = payload.get("expires_in", 0)
        token_type = payload.get("token_type", "Bearer")
        scope = payload.get("scope")
        if not access_token:
            return None, {"error": "Token response missing access_token", "body": payload}

        return OAuthToken(access_token=access_token, expires_at=time.time() + float(expires_in), token_type=token_type, scope=scope), None

    def get_app_token(self, scope: str = "https://api.ebay.com/oauth/api_scope") -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
        if self._app_token and not self._app_token.is_expired():
            return self._app_token.access_token, None

        token, err = self._request_token(
            {
                "grant_type": "client_credentials",
                "scope": scope,
            }
        )
        if err:
            return None, err
        self._app_token = token
        return token.access_token, None

    def get_user_token(self, scope: str) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
        if self._user_token and not self._user_token.is_expired():
            return self._user_token.access_token, None

        if not self.refresh_token:
            return None, {"error": "Missing EBAY_REFRESH_TOKEN env var"}

        token, err = self._request_token(
            {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "scope": scope,
            }
        )
        if err:
            return None, err
        self._user_token = token
        return token.access_token, None


def _safe_json(resp: requests.Response) -> Any:
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text}


class EbayHttpClient:
    def __init__(self, auth: Optional[EbayAuth] = None):
        self.auth = auth or EbayAuth()

    def request(
        self,
        method: str,
        path: str,
        *,
        base: str = "api",
        token_type: str = "app",
        scope: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
    ) -> Dict[str, Any]:
        base_url = self.auth.api_base_url if base == "api" else self.auth.media_base_url
        url = base_url + path

        if token_type == "user":
            if not scope:
                return {"error": "user token requested but no scope provided"}
            token, err = self.auth.get_user_token(scope)
        else:
            token, err = self.auth.get_app_token(scope or "https://api.ebay.com/oauth/api_scope")

        if err:
            return err

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
                json=json_body,
                headers=req_headers,
                files=files,
                data=data,
                timeout=60,
            )
        except Exception as e:
            return {"error": f"HTTP request failed: {e}", "url": url}

        if resp.status_code >= 400:
            return {
                "error": "eBay API error",
                "status": resp.status_code,
                "url": url,
                "body": _safe_json(resp),
            }

        if resp.status_code == 204:
            return {"status": 204, "url": url}

        return _safe_json(resp)
