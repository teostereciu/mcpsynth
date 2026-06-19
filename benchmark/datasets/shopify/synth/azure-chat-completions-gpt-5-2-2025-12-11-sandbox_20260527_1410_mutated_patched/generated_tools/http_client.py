import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


class ShopifyClient:
    def __init__(self):
        self.store_url = os.environ.get("SHOPIFY_STORE_URL", "").strip()
        self.access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "").strip()
        if not self.store_url:
            raise RuntimeError("SHOPIFY_STORE_URL is required")
        if not self.access_token:
            raise RuntimeError("SHOPIFY_ACCESS_TOKEN is required")
        self.base_url = f"https://{self.store_url}/admin/api/2026-01"

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
        json_body: Optional[Dict[str, Any]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        try:
            resp = requests.request(
                method,
                url,
                headers=self._headers(),
                params=params,
                json=json_body,
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e), "method": method, "url": url}

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except ValueError:
                data = {"raw": resp.text}
        else:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "Shopify API error",
                "status": resp.status_code,
                "method": method,
                "url": url,
                "response": data,
            }
        return data
