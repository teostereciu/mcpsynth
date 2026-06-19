import os
import requests
from typing import Any, Dict, Optional

API_VERSION = "2026-01"


def _base_url() -> str:
    store = os.environ.get("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    return f"https://{store}/admin/api/{API_VERSION}"


def _headers() -> Dict[str, str]:
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not token:
        raise RuntimeError("SHOPIFY_ACCESS_TOKEN is not set")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    url = _base_url() + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json_body, timeout=60)
    except Exception as e:
        return {"error": f"request_failed: {e}"}

    if resp.status_code >= 400:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return {"error": f"http_{resp.status_code}", "details": data}

    if resp.status_code == 204:
        return {"ok": True}

    try:
        return resp.json()
    except Exception:
        return resp.text
