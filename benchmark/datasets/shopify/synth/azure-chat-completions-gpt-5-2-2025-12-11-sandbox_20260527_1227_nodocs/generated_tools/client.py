import os
import time
from typing import Any, Dict, Optional

import requests


class ShopifyAdminClient:
    def __init__(
        self,
        store_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_version: str = "2026-01",
        timeout_s: int = 60,
    ):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version
        self.timeout_s = timeout_s

        if self.store_url.startswith("https://"):
            self.store_url = self.store_url[len("https://") :]
        if self.store_url.endswith("/"):
            self.store_url = self.store_url[:-1]

    @property
    def base_url(self) -> str:
        return f"https://{self.store_url}/admin/api/{self.api_version}"

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
        extra_headers: Optional[Dict[str, str]] = None,
        retries: int = 3,
    ) -> Dict[str, Any]:
        if not self.store_url:
            return {"error": "SHOPIFY_STORE_URL is not set"}
        if not self.access_token:
            return {"error": "SHOPIFY_ACCESS_TOKEN is not set"}

        url = self.base_url + path
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[str] = None
        for attempt in range(retries):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    headers=headers,
                    params=params,
                    json=json,
                    timeout=self.timeout_s,
                )

                # Basic rate-limit handling
                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else min(2 ** attempt, 8)
                    time.sleep(sleep_s)
                    continue

                # Shopify sometimes returns empty body
                if resp.status_code == 204:
                    return {"ok": True, "status": 204}

                content_type = resp.headers.get("Content-Type", "")
                data: Any
                if "application/json" in content_type:
                    data = resp.json()
                else:
                    data = resp.text

                if 200 <= resp.status_code < 300:
                    return {"ok": True, "status": resp.status_code, "data": data}

                # Expected errors should be returned, not raised
                return {
                    "error": True,
                    "status": resp.status_code,
                    "data": data,
                }
            except requests.RequestException as e:
                last_err = str(e)
                time.sleep(min(2 ** attempt, 8))

        return {"error": f"Request failed after retries: {last_err or 'unknown error'}"}
