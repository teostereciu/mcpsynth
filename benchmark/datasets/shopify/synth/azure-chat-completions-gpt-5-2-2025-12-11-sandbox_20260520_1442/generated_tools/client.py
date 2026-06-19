import os
import time
from typing import Any, Dict, Optional

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
        json_body: Optional[Dict[str, Any]] = None,
        retries: int = 3,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        last_err: Optional[str] = None

        for attempt in range(retries):
            try:
                resp = requests.request(
                    method,
                    url,
                    headers=self._headers(),
                    params=params,
                    json=json_body,
                    timeout=self.timeout,
                )

                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (1.0 + attempt)
                    time.sleep(sleep_s)
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.text.strip() == "":
                        return {"ok": True}
                    return resp.json()

                # Expected errors should be returned as dicts
                try:
                    payload = resp.json()
                except Exception:
                    payload = {"message": resp.text}

                return {
                    "error": True,
                    "status": resp.status_code,
                    "path": path,
                    "method": method,
                    "details": payload,
                }
            except requests.RequestException as e:
                last_err = str(e)
                time.sleep(0.5 * (attempt + 1))

        return {"error": True, "message": last_err or "request failed"}
