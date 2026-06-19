import os
import time
from typing import Any, Dict, Optional

import requests


API_VERSION = "2026-01"


def _normalize_store_url(store_url: str) -> str:
    store_url = store_url.strip()
    store_url = store_url.replace("https://", "").replace("http://", "")
    return store_url.rstrip("/")


class ShopifyClient:
    def __init__(
        self,
        store_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_version: str = API_VERSION,
        timeout_s: int = 60,
    ):
        self.store_url = _normalize_store_url(store_url or os.getenv("SHOPIFY_STORE_URL", ""))
        self.access_token = access_token or os.getenv("SHOPIFY_ACCESS_TOKEN", "")
        self.api_version = api_version
        self.timeout_s = timeout_s

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
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        retries: int = 3,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        last_err: Optional[str] = None

        for attempt in range(retries):
            try:
                resp = requests.request(
                    method=method,
                    url=url,
                    headers=self._headers(),
                    params=params,
                    json=json_body,
                    timeout=self.timeout_s,
                )

                # Shopify rate limit: 429 with Retry-After
                if resp.status_code == 429 and attempt < retries - 1:
                    ra = resp.headers.get("Retry-After")
                    sleep_s = float(ra) if ra else (1.0 + attempt)
                    time.sleep(sleep_s)
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.text.strip() == "":
                        return {"ok": True}
                    try:
                        return resp.json()
                    except Exception:
                        return {"ok": True, "text": resp.text}

                # Expected errors: return structured dict
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

            except requests.RequestException as e:
                last_err = str(e)
                if attempt < retries - 1:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return {"error": True, "message": last_err}

        return {"error": True, "message": last_err or "Unknown error"}
