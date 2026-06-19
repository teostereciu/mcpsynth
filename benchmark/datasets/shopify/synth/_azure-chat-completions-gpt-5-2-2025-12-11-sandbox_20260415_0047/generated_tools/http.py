import os
from typing import Any, Dict, Optional

import requests


class ShopifyClient:
    """Minimal Shopify Admin REST API client."""

    def __init__(self, api_version: str = "2026-01") -> None:
        self.api_version = api_version

    @property
    def base_url(self) -> str:
        store_url = os.environ.get("SHOPIFY_STORE_URL")
        if not store_url:
            raise RuntimeError("Missing SHOPIFY_STORE_URL env var")
        return f"https://{store_url}/admin/api/{self.api_version}"

    @property
    def headers(self) -> Dict[str, str]:
        token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
        if not token:
            raise RuntimeError("Missing SHOPIFY_ACCESS_TOKEN env var")
        return {
            "X-Shopify-Access-Token": token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        url = f"{self.base_url}{endpoint}"
        try:
            resp = requests.request(
                method.upper(),
                url,
                headers=self.headers,
                params=params,
                json=body,
                timeout=timeout,
            )
        except Exception as e:
            return {"error": str(e)}

        if not resp.ok:
            # Shopify often returns JSON errors, but sometimes plain text.
            try:
                payload = resp.json()
            except Exception:
                payload = resp.text
            return {
                "error": payload,
                "status_code": resp.status_code,
                "method": method.upper(),
                "endpoint": endpoint,
            }

        if resp.status_code == 204:
            return {"ok": True}

        try:
            return resp.json()
        except Exception:
            return {"ok": True, "text": resp.text}


def unwrap_envelope(data: Any) -> Any:
    """Unwrap Shopify REST envelope: {"resource": ...} -> ... when safe."""
    if isinstance(data, dict) and len(data) == 1:
        return next(iter(data.values()))
    return data
