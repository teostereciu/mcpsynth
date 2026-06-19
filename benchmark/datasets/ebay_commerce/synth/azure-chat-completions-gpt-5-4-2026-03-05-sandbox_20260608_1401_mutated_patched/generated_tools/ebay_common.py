import base64
import json
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
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
        self._token_cache: Dict[str, Dict[str, Any]] = {}

    def _base_url(self, media: bool = False) -> str:
        return (MEDIA_BASES if media else STANDARD_BASES).get(self.environment, STANDARD_BASES["SANDBOX"])

    def _basic_auth(self) -> str:
        if not self.app_id or not self.cert_id:
            raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")
        raw = f"{self.app_id}:{self.cert_id}".encode("utf-8")
        return base64.b64encode(raw).decode("ascii")

    def _get_token(self, token_type: str) -> str:
        cached = self._token_cache.get(token_type)
        now = time.time()
        if cached and cached.get("expires_at", 0) > now + 60:
            return cached["access_token"]

        url = f"{self._base_url(False)}/identity/v1/oauth2/token"
        headers = {
            "Authorization": f"Basic {self._basic_auth()}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        if token_type == "app":
            data = {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            }
        else:
            if not self.refresh_token:
                raise ValueError("EBAY_REFRESH_TOKEN must be set for user-scoped APIs")
            data = {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            }
        response = requests.post(url, headers=headers, data=data, timeout=60)
        payload = self._safe_json(response)
        if response.status_code >= 400:
            raise ValueError(json.dumps(payload))
        access_token = payload.get("access_token")
        expires_in = int(payload.get("expires_in", 7200))
        self._token_cache[token_type] = {
            "access_token": access_token,
            "expires_at": now + expires_in,
        }
        return access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        token_type: str,
        media: bool = False,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Optional[Dict[str, Any]] = None,
        data: Any = None,
    ) -> Dict[str, Any]:
        try:
            token = self._get_token(token_type)
            req_headers = {"Authorization": f"Bearer {token}"}
            if headers:
                req_headers.update({k: v for k, v in headers.items() if v is not None})
            url = f"{self._base_url(media)}{path}"
            response = requests.request(
                method,
                url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                headers=req_headers,
                files=files,
                data=data,
                timeout=120,
            )
            body = self._safe_json(response)
            result: Dict[str, Any] = {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": body,
            }
            if response.status_code >= 400:
                result["error"] = body if isinstance(body, (dict, list)) else response.text
            return result
        except Exception as exc:
            return {"error": str(exc)}

    @staticmethod
    def _safe_json(response: requests.Response) -> Any:
        try:
            return response.json()
        except Exception:
            return response.text


client = EbayClient()
