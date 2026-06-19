from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


class ShopifyAdminClient:
    """Minimal Shopify Admin REST API client.

    Reads credentials from environment variables:
      - SHOPIFY_ACCESS_TOKEN
      - SHOPIFY_STORE_URL

    Uses API version 2026-01.
    """

    def __init__(self, api_version: str = "2026-01", timeout_s: int = 60):
        self.api_version = api_version
        self.timeout_s = timeout_s

    def _base_url(self) -> str:
        store_url = os.environ.get("SHOPIFY_STORE_URL")
        if not store_url:
            raise RuntimeError("Missing env var SHOPIFY_STORE_URL")
        return f"https://{store_url}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
        if not token:
            raise RuntimeError("Missing env var SHOPIFY_ACCESS_TOKEN")
        return {
            "X-Shopify-Access-Token": token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @staticmethod
    def _unwrap(data: Any) -> Any:
        if isinstance(data, dict) and len(data) == 1:
            # Shopify typically wraps responses in a single top-level key.
            return next(iter(data.values()))
        return data

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        unwrap: bool = True,
    ) -> Any:
        url = f"{self._base_url()}{endpoint}"
        try:
            resp = requests.request(
                method.upper(),
                url,
                headers=self._headers(),
                params=params,
                json=body,
                timeout=self.timeout_s,
            )
        except Exception as e:
            return {"error": str(e)}

        if not resp.ok:
            # Shopify error bodies are often JSON, but can be plain text.
            try:
                err = resp.json()
            except Exception:
                err = resp.text
            return {"error": err, "status_code": resp.status_code}

        if resp.status_code == 204:
            return {"ok": True}

        try:
            data = resp.json()
        except Exception:
            return {"error": "Non-JSON response", "status_code": resp.status_code, "text": resp.text}

        return self._unwrap(data) if unwrap else data
