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
        extra_headers: Optional[Dict[str, str]] = None,
        retries: int = 3,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[str] = None
        for attempt in range(retries + 1):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    headers=headers,
                    params=params,
                    json=json_body,
                    timeout=self.timeout,
                )

                # Basic rate-limit handling
                if resp.status_code == 429 and attempt < retries:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (1.0 + attempt)
                    time.sleep(sleep_s)
                    continue

                if resp.status_code >= 400:
                    try:
                        data = resp.json()
                    except Exception:
                        data = {"message": resp.text}
                    return {
                        "error": "Shopify API error",
                        "status_code": resp.status_code,
                        "response": data,
                    }

                if resp.status_code == 204:
                    return {"ok": True}

                try:
                    return resp.json()
                except Exception:
                    return {"raw": resp.text}

            except Exception as e:
                last_err = str(e)
                if attempt < retries:
                    time.sleep(0.5 * (attempt + 1))
                    continue

        return {"error": "Request failed", "message": last_err or "unknown"}


def build_params(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
