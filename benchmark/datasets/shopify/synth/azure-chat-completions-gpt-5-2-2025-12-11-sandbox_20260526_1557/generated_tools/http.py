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
        timeout: int = 30,
    ):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version
        self.timeout = timeout

    @property
    def base_url(self) -> str:
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
        retries: int = 2,
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

                if resp.status_code == 429 and attempt < retries:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (0.5 * (2**attempt))
                    time.sleep(sleep_s)
                    continue

                content_type = resp.headers.get("Content-Type", "")
                data: Any
                if "application/json" in content_type:
                    try:
                        data = resp.json()
                    except Exception:
                        data = {"raw": resp.text}
                else:
                    data = {"raw": resp.text}

                if 200 <= resp.status_code < 300:
                    return {
                        "ok": True,
                        "status": resp.status_code,
                        "data": data,
                        "headers": {
                            "link": resp.headers.get("Link"),
                            "x-request-id": resp.headers.get("X-Request-Id"),
                        },
                    }

                return {
                    "ok": False,
                    "status": resp.status_code,
                    "error": data,
                    "headers": {
                        "link": resp.headers.get("Link"),
                        "x-request-id": resp.headers.get("X-Request-Id"),
                    },
                }
            except Exception as e:
                last_err = str(e)
                if attempt < retries:
                    time.sleep(0.5 * (2**attempt))
                    continue

        return {"ok": False, "status": 0, "error": last_err or "request failed"}
