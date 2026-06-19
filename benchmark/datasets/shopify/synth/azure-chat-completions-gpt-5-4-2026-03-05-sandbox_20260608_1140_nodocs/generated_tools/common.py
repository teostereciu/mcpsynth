import os
from typing import Any, Dict, Optional

import requests

API_VERSION = "2026-01"


def _base_url() -> Optional[str]:
    store = os.getenv("SHOPIFY_STORE_URL", "").strip()
    if not store:
        return None
    if store.startswith("https://"):
        store = store[len("https://"):]
    elif store.startswith("http://"):
        store = store[len("http://"):]
    return f"https://{store}/admin/api/{API_VERSION}"


def _headers() -> Dict[str, str]:
    token = os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip()
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def shopify_request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Any:
    base = _base_url()
    if not base:
        return {"error": "Missing SHOPIFY_STORE_URL environment variable"}
    if not os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip():
        return {"error": "Missing SHOPIFY_ACCESS_TOKEN environment variable"}

    url = f"{base}{path}"
    try:
        response = requests.request(method=method.upper(), url=url, headers=_headers(), params=params, json=json_body, timeout=60)
    except requests.RequestException as exc:
        return {"error": str(exc)}

    try:
        data = response.json() if response.text else {}
    except ValueError:
        data = {"raw": response.text}

    if response.ok:
        return data

    if isinstance(data, dict):
        data.setdefault("status_code", response.status_code)
        return data
    return {"error": str(data), "status_code": response.status_code}


def clean_params(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
