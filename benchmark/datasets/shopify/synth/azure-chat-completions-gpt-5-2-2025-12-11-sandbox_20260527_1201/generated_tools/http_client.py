import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


def _base_url() -> str:
    store = os.environ.get("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    return f"https://{store}/admin/api/2026-01"


def _headers() -> Dict[str, str]:
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not token:
        raise RuntimeError("SHOPIFY_ACCESS_TOKEN is not set")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Dict[str, Any]:
    url = _base_url() + path
    try:
        resp = requests.request(method.upper(), url, headers=_headers(), params=params, json=json_body, timeout=60)
    except Exception as e:
        return {"error": str(e), "url": url}

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
        if isinstance(data, dict):
            data.setdefault("_meta", {})
            data["_meta"].update({"status": resp.status_code, "url": url})
        return data if isinstance(data, (dict, list)) else {"data": data, "_meta": {"status": resp.status_code, "url": url}}

    return {
        "error": "Shopify API error",
        "status": resp.status_code,
        "url": url,
        "response": data,
    }
