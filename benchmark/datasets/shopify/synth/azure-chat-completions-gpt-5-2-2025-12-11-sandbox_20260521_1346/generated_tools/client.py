import os
import requests
from typing import Any, Dict, Optional


class ShopifyClient:
    def __init__(self, store_url: Optional[str] = None, access_token: Optional[str] = None, api_version: str = "2026-01"):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version

    @property
    def base_url(self) -> str:
        if not self.store_url:
            return ""
        return f"https://{self.store_url}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        if not self.store_url:
            return {"error": "SHOPIFY_STORE_URL is not set"}
        if not self.access_token:
            return {"error": "SHOPIFY_ACCESS_TOKEN is not set"}

        url = self.base_url + path
        try:
            resp = requests.request(method, url, headers=self._headers(), params=params, json=json, timeout=60)
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except ValueError:
                data = {"raw": resp.text}
        else:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "Shopify API error",
                "status_code": resp.status_code,
                "response": data,
            }
        return data


def clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}
