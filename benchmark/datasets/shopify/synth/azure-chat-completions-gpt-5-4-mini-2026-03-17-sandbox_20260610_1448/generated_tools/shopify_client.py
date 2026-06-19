import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://{store}/admin/api/2026-01"


class ShopifyClient:
    def __init__(self, access_token: Optional[str] = None, store_url: Optional[str] = None):
        self.access_token = access_token or os.getenv("SHOPIFY_ACCESS_TOKEN")
        self.store_url = store_url or os.getenv("SHOPIFY_STORE_URL")
        if not self.access_token or not self.store_url:
            raise ValueError("SHOPIFY_ACCESS_TOKEN and SHOPIFY_STORE_URL are required")
        self.base_url = BASE_URL.format(store=self.store_url)

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None):
        url = f"{self.base_url}{path}"
        resp = requests.request(
            method,
            url,
            headers={"X-Shopify-Access-Token": self.access_token, "Content-Type": "application/json"},
            params=params,
            json=json,
            timeout=60,
        )
        resp.raise_for_status()
        if resp.text:
            return resp.json()
        return {}
