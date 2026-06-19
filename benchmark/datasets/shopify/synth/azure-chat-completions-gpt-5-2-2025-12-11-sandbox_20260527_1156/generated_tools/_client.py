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

        if self.store_url.startswith("https://"):
            self.store_url = self.store_url[len("https://") :]
        if self.store_url.startswith("http://"):
            self.store_url = self.store_url[len("http://") :]

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
                    timeout=self.timeout,
                )

                # Basic rate-limit handling
                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (0.5 * (attempt + 1))
                    time.sleep(min(5.0, sleep_s))
                    continue

                if 200 <= resp.status_code < 300:
                    if not resp.content:
                        return {"ok": True}
                    try:
                        return resp.json()
                    except Exception:
                        return {"raw": resp.text}

                # Expected errors: return JSON if possible
                try:
                    err_json = resp.json()
                except Exception:
                    err_json = {"raw": resp.text}

                return {
                    "error": "Shopify API error",
                    "status": resp.status_code,
                    "details": err_json,
                }
            except requests.RequestException as e:
                last_err = str(e)
                time.sleep(0.2 * (attempt + 1))

        return {"error": "Request failed", "details": last_err or "unknown"}


_client_singleton: Optional[ShopifyClient] = None


def get_client() -> ShopifyClient:
    global _client_singleton
    if _client_singleton is None:
        _client_singleton = ShopifyClient()
    return _client_singleton
