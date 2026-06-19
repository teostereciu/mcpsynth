import os
import re
from typing import Any, Dict, Optional

import requests

BASE_API_VERSION = "2026-01"


def _base_url() -> str:
    store = os.getenv("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise ValueError("SHOPIFY_STORE_URL is not set")
    store = re.sub(r"^https?://", "", store).rstrip("/")
    return f"https://{store}/admin/api/{BASE_API_VERSION}"


def _headers() -> Dict[str, str]:
    token = os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN is not set")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def shopify_request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Any:
    try:
        response = requests.request(
            method=method,
            url=f"{_base_url()}{path}",
            headers=_headers(),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            timeout=60,
        )
    except ValueError as e:
        return {"error": str(e)}
    except requests.RequestException as e:
        return {"error": str(e)}

    try:
        data = response.json() if response.text else {"status": response.status_code}
    except ValueError:
        data = {"status": response.status_code, "text": response.text}

    if response.ok:
        return data

    if isinstance(data, dict):
        data.setdefault("status", response.status_code)
        return data
    return {"error": str(data), "status": response.status_code}
