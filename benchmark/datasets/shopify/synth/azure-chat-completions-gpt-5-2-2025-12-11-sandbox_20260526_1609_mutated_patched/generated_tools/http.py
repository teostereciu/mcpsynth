import os
import time
from typing import Any, Dict, Optional

import requests


API_VERSION = "2026-01"


class ShopifyClient:
    def __init__(self, store_url: Optional[str] = None, access_token: Optional[str] = None):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        if self.store_url.startswith("https://"):
            self.store_url = self.store_url[len("https://") :]
        if self.store_url.startswith("http://"):
            self.store_url = self.store_url[len("http://") :]

    @property
    def base_url(self) -> str:
        return f"https://{self.store_url}/admin/api/{API_VERSION}"

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
        timeout: int = 60,
        retries: int = 2,
    ) -> Dict[str, Any]:
        if not self.store_url or not self.access_token:
            return {"error": "Missing SHOPIFY_STORE_URL or SHOPIFY_ACCESS_TOKEN"}

        url = self.base_url + path
        last_err: Optional[str] = None
        for attempt in range(retries + 1):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    headers=self._headers(),
                    params=params,
                    json=json,
                    timeout=timeout,
                )
                if resp.status_code == 429 and attempt < retries:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (1.0 + attempt)
                    time.sleep(sleep_s)
                    continue

                if resp.status_code >= 400:
                    try:
                        payload = resp.json()
                    except Exception:
                        payload = {"message": resp.text}
                    return {
                        "error": "Shopify API error",
                        "status_code": resp.status_code,
                        "response": payload,
                    }

                if resp.status_code == 204:
                    return {"ok": True}

                try:
                    return resp.json()
                except Exception:
                    return {"raw": resp.text}
            except requests.RequestException as e:
                last_err = str(e)
                if attempt < retries:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return {"error": "Request failed", "message": last_err}

        return {"error": "Request failed", "message": last_err or "unknown"}
