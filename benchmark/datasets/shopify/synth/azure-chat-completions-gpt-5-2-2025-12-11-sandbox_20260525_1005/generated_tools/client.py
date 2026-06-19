import os
import requests
from typing import Any, Dict, Optional


class ShopifyClient:
    def __init__(self, store_url: Optional[str] = None, access_token: Optional[str] = None, api_version: str = "2026-01"):
        self.store_url = store_url or os.getenv("SHOPIFY_STORE_URL")
        self.access_token = access_token or os.getenv("SHOPIFY_ACCESS_TOKEN")
        self.api_version = api_version
        if not self.store_url:
            raise ValueError("SHOPIFY_STORE_URL is required")
        if not self.access_token:
            raise ValueError("SHOPIFY_ACCESS_TOKEN is required")

        self.base_url = f"https://{self.store_url}/admin/api/{self.api_version}"

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        url = self.base_url + path
        headers = {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        try:
            resp = requests.request(method, url, headers=headers, params=params, json=json, timeout=60)
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": f"HTTP {resp.status_code}", "details": data}

        if resp.status_code == 204:
            return {"ok": True}

        try:
            return resp.json()
        except Exception:
            return resp.text
