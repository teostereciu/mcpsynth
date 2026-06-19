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

    def _base_url(self) -> str:
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
        retry: int = 2,
    ) -> Dict[str, Any]:
        if not self.store_url:
            return {"error": "SHOPIFY_STORE_URL is not set"}
        if not self.access_token:
            return {"error": "SHOPIFY_ACCESS_TOKEN is not set"}

        url = self._base_url() + path
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[Dict[str, Any]] = None
        for attempt in range(retry + 1):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    params=params,
                    json=json,
                    headers=headers,
                    timeout=self.timeout,
                )

                # Basic rate-limit handling
                if resp.status_code == 429 and attempt < retry:
                    wait_s = float(resp.headers.get("Retry-After", "1"))
                    time.sleep(max(0.5, wait_s))
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.text.strip() == "":
                        return {"status": resp.status_code}
                    try:
                        return resp.json()
                    except Exception:
                        return {"status": resp.status_code, "text": resp.text}

                # Expected errors should be returned, not raised
                try:
                    body = resp.json()
                except Exception:
                    body = {"text": resp.text}

                last_err = {
                    "error": "Shopify API error",
                    "status": resp.status_code,
                    "path": path,
                    "body": body,
                }

                # Retry on transient 5xx
                if resp.status_code >= 500 and attempt < retry:
                    time.sleep(0.5 * (attempt + 1))
                    continue

                return last_err

            except requests.RequestException as e:
                last_err = {"error": "Request failed", "detail": str(e), "path": path}
                if attempt < retry:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return last_err

        return last_err or {"error": "Unknown error"}


def build_params(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
