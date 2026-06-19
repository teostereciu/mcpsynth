import os
import requests
from typing import Any, Dict, Optional


API_VERSION = "2026-01"


def _base_url() -> str:
    store = os.environ.get("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    store = store.replace("https://", "").replace("http://", "").strip("/")
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

    Returns a JSON-serializable dict. On HTTP errors, returns {"error": ..., "status": ..., "details": ...}.
    """
    url = _base_url() + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "details": str(e)}

    content_type = resp.headers.get("content-type", "")
    data: Any = None
    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
    else:
        data = resp.text

    if 200 <= resp.status_code < 300:
        return {"status": resp.status_code, "data": data}

    return {
        "error": "http_error",
        "status": resp.status_code,
        "details": data,
    }
