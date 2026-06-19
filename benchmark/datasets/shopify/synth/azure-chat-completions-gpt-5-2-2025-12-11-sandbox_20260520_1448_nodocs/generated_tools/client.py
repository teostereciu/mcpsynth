import os
import requests
from typing import Any, Dict, Optional

API_VERSION = "2026-01"


def _base_url() -> str:
    store = os.environ.get("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    if store.startswith("http://") or store.startswith("https://"):
        store = store.split("//", 1)[1]
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


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Dict[str, Any]:
    """Make a Shopify Admin REST request.

    Returns a JSON-serializable dict. Errors are returned as {"error": ..., "status": ...}.
    """
    try:
        url = _base_url() + path
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=60)
        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": data, "status": resp.status_code, "method": method, "path": path}
        if resp.status_code == 204:
            return {"ok": True, "status": 204}
        try:
            return resp.json()
        except Exception:
            return {"raw": resp.text, "status": resp.status_code}
    except Exception as e:
        return {"error": str(e), "method": method, "path": path}
