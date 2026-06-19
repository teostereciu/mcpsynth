import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


API_VERSION = "2026-01"


class ShopifyClient:
    def __init__(
        self,
        store_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_version: str = API_VERSION,
        timeout_s: int = 60,
    ):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version
        self.timeout_s = timeout_s

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
        retries: int = 3,
    ) -> Dict[str, Any]:
        url = self._base_url() + path
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[str] = None
        for attempt in range(retries):
            try:
                resp = requests.request(
                    method=method.upper(),
                    url=url,
                    headers=headers,
                    params=params,
                    json=json_body,
                    timeout=self.timeout_s,
                )

                # Basic rate-limit handling
                if resp.status_code == 429 and attempt < retries - 1:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (0.5 * (attempt + 1))
                    time.sleep(sleep_s)
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.text.strip() == "":
                        return {"status": resp.status_code}
                    try:
                        return resp.json()
                    except Exception:
                        return {"status": resp.status_code, "text": resp.text}

                # Expected errors returned as dicts
                try:
                    payload = resp.json()
                except Exception:
                    payload = {"text": resp.text}
                return {
                    "error": True,
                    "status": resp.status_code,
                    "message": payload.get("errors") if isinstance(payload, dict) else payload,
                    "response": payload,
                }

            except Exception as e:
                last_err = str(e)
                if attempt < retries - 1:
                    time.sleep(0.5 * (attempt + 1))
                    continue

        return {"error": True, "message": last_err or "request failed"}
