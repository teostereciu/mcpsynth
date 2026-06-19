import base64
import json
import os
from typing import Any, Dict, Optional

import requests


BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


class EbayClient:
    def __init__(self) -> None:
        self.app_id = os.getenv("EBAY_APP_ID", "")
        self.cert_id = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = BASE_URLS.get(env, BASE_URLS["SANDBOX"])
        self._token: Optional[str] = None

    def _get_token(self) -> str:
        if self._token:
            return self._token
        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise ValueError("Missing one or more required environment variables: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN")
        auth = base64.b64encode(f"{self.app_id}:{self.cert_id}".encode()).decode()
        response = requests.post(
            f"{self.base_url}/identity/v1/oauth2/token",
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            },
            timeout=60,
        )
        response.raise_for_status()
        self._token = response.json()["access_token"]
        return self._token

    def request(
        self,
        api_base: str,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Any] = None,
    ) -> Any:
        token = self._get_token()
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
        if json_body is not None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update(headers)
        url = f"{self.base_url}{api_base}{path}"
        response = requests.request(
            method=method,
            url=url,
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            headers=req_headers,
            data=data,
            timeout=120,
        )
        if response.status_code >= 400:
            try:
                return {"error": response.json(), "status_code": response.status_code}
            except Exception:
                return {"error": response.text, "status_code": response.status_code}
        if not response.text:
            return {"status": "success", "status_code": response.status_code}
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return response.json()
        return {
            "content": response.text,
            "content_type": content_type,
            "status_code": response.status_code,
        }


client = EbayClient()


def compact_kwargs(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}


def parse_json_body(body: Optional[str]) -> Optional[Any]:
    if body is None:
        return None
    if isinstance(body, (dict, list)):
        return body
    return json.loads(body)
