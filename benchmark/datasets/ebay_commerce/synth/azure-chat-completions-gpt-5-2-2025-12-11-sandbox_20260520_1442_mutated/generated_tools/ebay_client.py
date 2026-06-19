import base64
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


EBAY_OAUTH_BASE = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

EBAY_API_BASE = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

EBAY_MEDIA_BASE = {
    "SANDBOX": "https://apim.sandbox.ebay.com",
    "PRODUCTION": "https://apim.ebay.com",
}


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


@dataclass
class Token:
    access_token: str
    expires_at: float

    def valid(self) -> bool:
        return time.time() < self.expires_at - 30


class EbayClient:
    def __init__(self):
        self.app_id = _env("EBAY_APP_ID")
        self.cert_id = _env("EBAY_CERT_ID")
        self.refresh_token = _env("EBAY_REFRESH_TOKEN")
        self.environment = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
        if self.environment not in EBAY_API_BASE:
            self.environment = "SANDBOX"

        self._app_token: Optional[Token] = None
        self._user_token: Optional[Token] = None

    @property
    def api_base(self) -> str:
        return EBAY_API_BASE[self.environment]

    @property
    def media_base(self) -> str:
        return EBAY_MEDIA_BASE[self.environment]

    @property
    def oauth_base(self) -> str:
        return EBAY_OAUTH_BASE[self.environment]

    def _basic_auth_header(self) -> str:
        if not self.app_id or not self.cert_id:
            raise ValueError("Missing EBAY_APP_ID or EBAY_CERT_ID")
        token = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"

    def _token_request(self, data: Dict[str, str], scope: Optional[str] = None) -> Token:
        url = f"{self.oauth_base}/identity/v1/oauth2/token"
        headers = {
            "Authorization": self._basic_auth_header(),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        if scope:
            data = dict(data)
            data["scope"] = scope
        resp = requests.post(url, headers=headers, data=data, timeout=60)
        if resp.status_code >= 400:
            try:
                return Token(access_token=json.dumps({"error": resp.text}), expires_at=0)
            except Exception:
                return Token(access_token=f"{{\"error\": {resp.text!r}}}", expires_at=0)
        payload = resp.json()
        access_token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 0))
        return Token(access_token=access_token, expires_at=time.time() + expires_in)

    def get_app_token(self, scope: Optional[str] = None) -> str:
        if self._app_token and self._app_token.valid():
            return self._app_token.access_token
        tok = self._token_request({"grant_type": "client_credentials"}, scope=scope)
        self._app_token = tok
        return tok.access_token

    def get_user_token(self, scope: Optional[str] = None) -> str:
        if self._user_token and self._user_token.valid():
            return self._user_token.access_token
        if not self.refresh_token:
            raise ValueError("Missing EBAY_REFRESH_TOKEN")
        tok = self._token_request(
            {"grant_type": "refresh_token", "refresh_token": self.refresh_token},
            scope=scope,
        )
        self._user_token = tok
        return tok.access_token

    def request(
        self,
        method: str,
        base: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        auth: str = "app",
        scope: Optional[str] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        url = base.rstrip("/") + "/" + path.lstrip("/")
        hdrs = {"Accept": "application/json"}
        if headers:
            hdrs.update({k: v for k, v in headers.items() if v is not None})

        try:
            if auth == "none":
                pass
            elif auth == "user":
                hdrs["Authorization"] = f"Bearer {self.get_user_token(scope=scope)}"
            else:
                hdrs["Authorization"] = f"Bearer {self.get_app_token(scope=scope)}"
        except Exception as e:
            return {"error": str(e)}

        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                json=json_body,
                data=data,
                headers=hdrs,
                timeout=timeout,
            )
        except Exception as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            try:
                err = resp.json() if "json" in content_type else {"message": resp.text}
            except Exception:
                err = {"message": resp.text}
            return {"error": err, "status_code": resp.status_code, "url": url}

        if resp.status_code == 204:
            return {"status_code": 204}

        if "json" in content_type:
            try:
                return resp.json()
            except Exception:
                return {"raw": resp.text}
        return {"raw": resp.text}
