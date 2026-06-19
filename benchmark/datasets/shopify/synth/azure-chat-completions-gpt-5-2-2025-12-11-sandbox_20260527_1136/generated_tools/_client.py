import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


class ShopifyClient:
    def __init__(
        self,
        store_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_version: str = "2026-01",
        timeout: int = 60,
    ):
        self.store_url = store_url or os.getenv("SHOPIFY_STORE_URL")
        self.access_token = access_token or os.getenv("SHOPIFY_ACCESS_TOKEN")
        self.api_version = api_version
        self.timeout = timeout

        if not self.store_url:
            raise ValueError("SHOPIFY_STORE_URL is required")
        if not self.access_token:
            raise ValueError("SHOPIFY_ACCESS_TOKEN is required")

        self.base_url = f"https://{self.store_url}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        try:
            resp = requests.request(
                method,
                url,
                headers=self._headers(),
                params=params,
                json=json,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = {"message": resp.text}
            return {
                "error": "Shopify API error",
                "status_code": resp.status_code,
                "url": url,
                "details": data,
            }

        if resp.status_code == 204:
            return {"ok": True}

        try:
            return resp.json()
        except Exception:
            return {"ok": True, "raw": resp.text}


def clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}
