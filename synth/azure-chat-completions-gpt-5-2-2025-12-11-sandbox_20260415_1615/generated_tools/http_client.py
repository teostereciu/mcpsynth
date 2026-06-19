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
        extra_headers: Optional[Dict[str, str]] = None,
        retry: int = 2,
    ) -> Dict[str, Any]:
        url = self._base_url() + path
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[str] = None
        for attempt in range(retry + 1):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    headers=headers,
                    params=params,
                    json=json_body,
                    timeout=self.timeout,
                )

                # Basic rate limit handling
                if resp.status_code == 429 and attempt < retry:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (0.5 * (attempt + 1))
                    time.sleep(sleep_s)
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.text.strip() == "":
                        return {"status": resp.status_code}
                    return resp.json()

                # Expected errors should be returned as dicts
                try:
                    payload = resp.json()
                except Exception:
                    payload = {"message": resp.text}

                return {
                    "error": "Shopify API error",
                    "status": resp.status_code,
                    "path": path,
                    "details": payload,
                }
            except Exception as e:
                last_err = str(e)
                if attempt < retry:
                    time.sleep(0.5 * (attempt + 1))
                    continue

        return {"error": "Request failed", "details": last_err, "path": path}


_default_client: Optional[ShopifyClient] = None


def get_client() -> ShopifyClient:
    global _default_client
    if _default_client is None:
        _default_client = ShopifyClient()
    return _default_client
