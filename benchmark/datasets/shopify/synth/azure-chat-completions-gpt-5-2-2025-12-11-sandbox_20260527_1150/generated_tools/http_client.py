import os
import json
from typing import Any, Dict, Optional, Tuple

import requests


class ShopifyAdminClient:
    def __init__(
        self,
        store_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_version: str = "2026-01",
        timeout: int = 60,
    ):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version
        self.timeout = timeout

    def _base_url(self) -> str:
        if not self.store_url:
            raise ValueError("SHOPIFY_STORE_URL is not set")
        return f"https://{self.store_url}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        if not self.access_token:
            raise ValueError("SHOPIFY_ACCESS_TOKEN is not set")
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
    ) -> Dict[str, Any]:
        url = self._base_url() + path
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                headers=self._headers(),
                params=params,
                data=None if json_body is None else json.dumps(json_body),
                timeout=self.timeout,
            )
        except Exception as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except Exception:
                data = {"raw": resp.text}
        else:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "Shopify API error",
                "status": resp.status_code,
                "data": data,
            }

        return data
