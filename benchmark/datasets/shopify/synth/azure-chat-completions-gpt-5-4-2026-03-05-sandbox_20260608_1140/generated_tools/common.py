import os
from typing import Any, Dict, Optional

import requests

API_VERSION = "2026-01"


def _base_url() -> str:
    store = os.getenv("SHOPIFY_STORE_URL", "").strip()
    if not store:
        return ""
    return f"https://{store}/admin/api/{API_VERSION}"


def shopify_request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Any:
    base = _base_url()
    token = os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not base:
        return {"error": "Missing SHOPIFY_STORE_URL"}
    if not token:
        return {"error": "Missing SHOPIFY_ACCESS_TOKEN"}

    url = f"{base}{path}"
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        response = requests.request(method=method.upper(), url=url, headers=headers, params=params, json=json_body, timeout=60)
    except requests.RequestException as exc:
        return {"error": str(exc)}

    try:
        data = response.json() if response.text else {"status": response.status_code}
    except ValueError:
        data = {"status": response.status_code, "text": response.text}

    if response.ok:
        return data
    if isinstance(data, dict):
        data.setdefault("status", response.status_code)
        return data
    return {"error": "Request failed", "status": response.status_code, "details": data}
