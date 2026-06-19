import base64
import os
import time
from typing import Any, Dict, Optional

import requests


STANDARD_BASES = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}

MEDIA_BASES = {
    "SANDBOX": "https://apim.sandbox.ebay.com",
    "PRODUCTION": "https://apim.ebay.com",
}


class EbayClient:
    def __init__(self) -> None:
        self.environment = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.client_id = os.getenv("EBAY_APP_ID", "")
        self.client_secret = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self._app_token: Optional[str] = None
        self._app_token_expiry = 0.0
        self._user_token: Optional[str] = None
        self._user_token_expiry = 0.0

    @property
    def standard_base(self) -> str:
        return STANDARD_BASES.get(self.environment, STANDARD_BASES["SANDBOX"])

    @property
    def media_base(self) -> str:
        return MEDIA_BASES.get(self.environment, MEDIA_BASES["SANDBOX"])

    def _basic_auth(self) -> str:
        raw = f"{self.client_id}:{self.client_secret}".encode()
        return base64.b64encode(raw).decode()

    def _token_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.client_id or not self.client_secret:
            return {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID"}
        try:
            response = requests.post(
                f"{self.standard_base}/identity/v1/oauth2/token",
                headers={
                    "Authorization": f"Basic {self._basic_auth()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                data=data,
                timeout=60,
            )
            payload = self._safe_json(response)
            if response.status_code >= 400:
                return {"error": f"Token request failed with status {response.status_code}", "details": payload}
            return payload
        except requests.RequestException as exc:
            return {"error": str(exc)}

    def get_app_token(self) -> Dict[str, Any]:
        if self._app_token and time.time() < self._app_token_expiry:
            return {"access_token": self._app_token}
        payload = self._token_request(
            {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            }
        )
        token = payload.get("access_token")
        if token:
            self._app_token = token
            self._app_token_expiry = time.time() + int(payload.get("expires_in", 7200)) - 60
        return payload

    def get_user_token(self, scope: Optional[str] = None) -> Dict[str, Any]:
        if self._user_token and time.time() < self._user_token_expiry:
            return {"access_token": self._user_token}
        if not self.refresh_token:
            return {"error": "Missing EBAY_REFRESH_TOKEN"}
        data: Dict[str, Any] = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        if scope:
            data["scope"] = scope
        payload = self._token_request(data)
        token = payload.get("access_token")
        if token:
            self._user_token = token
            self._user_token_expiry = time.time() + int(payload.get("expires_in", 7200)) - 60
        return payload

    def request(
        self,
        method: str,
        path: str,
        token_type: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_media_base: bool = False,
    ) -> Dict[str, Any]:
        token_payload = self.get_app_token() if token_type == "app" else self.get_user_token()
        token = token_payload.get("access_token")
        if not token:
            return token_payload
        base = self.media_base if use_media_base else self.standard_base
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if json_body is not None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update(headers)
        try:
            response = requests.request(
                method=method,
                url=f"{base}{path}",
                headers=req_headers,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                timeout=60,
            )
            payload = self._safe_json(response)
            if response.status_code >= 400:
                return {
                    "error": f"Request failed with status {response.status_code}",
                    "details": payload,
                    "status_code": response.status_code,
                }
            return payload if payload != "" else {"status": response.status_code}
        except requests.RequestException as exc:
            return {"error": str(exc)}

    @staticmethod
    def _safe_json(response: requests.Response) -> Any:
        try:
            return response.json()
        except ValueError:
            return response.text


client = EbayClient()
