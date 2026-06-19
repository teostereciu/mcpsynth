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
        timeout_s: int = 30,
        max_retries: int = 3,
    ):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version
        self.timeout_s = timeout_s
        self.max_retries = max_retries

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
        last_err: Optional[str] = None

        for attempt in range(self.max_retries):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    headers=self._headers(),
                    params=params,
                    json=json_body,
                    timeout=self.timeout_s,
                )

                # Retry on rate limiting / transient errors
                if resp.status_code in (429, 500, 502, 503, 504) and attempt < self.max_retries - 1:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (0.5 * (2**attempt))
                    time.sleep(min(8.0, sleep_s))
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.text.strip() == "":
                        return {"status": resp.status_code}
                    return resp.json()

                # Expected errors: return as dict
                try:
                    err_json = resp.json()
                except Exception:
                    err_json = {"error": resp.text}

                return {
                    "error": "Shopify API error",
                    "status": resp.status_code,
                    "details": err_json,
                    "method": method.upper(),
                    "path": path,
                }

            except ValueError as e:
                return {"error": str(e)}
            except Exception as e:
                last_err = str(e)
                if attempt < self.max_retries - 1:
                    time.sleep(min(8.0, 0.5 * (2**attempt)))
                    continue

        return {"error": "Request failed", "details": last_err, "method": method.upper(), "path": path}


_client: Optional[ShopifyClient] = None


def get_client() -> ShopifyClient:
    global _client
    if _client is None:
        _client = ShopifyClient()
    return _client
