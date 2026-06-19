import os
import requests
from typing import Any, Dict, Optional

API_VERSION = "2026-01"


def _store_base_url() -> str:
    store = os.getenv("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    if store.startswith("http://") or store.startswith("https://"):
        store = store.split("//", 1)[1]
    return f"https://{store}/admin/api/{API_VERSION}"


def _headers() -> Dict[str, str]:
    token = os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not token:
        raise RuntimeError("SHOPIFY_ACCESS_TOKEN is not set")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    """Make a Shopify Admin REST request.

    Returns JSON-decoded body on success; on expected errors returns {"error": ..., "status": ...}.
    """
    url = _store_base_url() + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=60)
    except Exception as e:
        return {"error": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
    else:
        data = resp.text

    if 200 <= resp.status_code < 300:
        return data

    # Expected errors: return structured dict
    err = {
        "error": "Shopify API error",
        "status": resp.status_code,
        "body": data,
    }
    return err
