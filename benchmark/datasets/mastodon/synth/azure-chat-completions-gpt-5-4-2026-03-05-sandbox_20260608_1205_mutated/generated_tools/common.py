import os
from typing import Any, Dict, Optional

import requests


BASE_URL = os.getenv("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN", "")
API_BASE = f"{BASE_URL}/api/v1" if BASE_URL else ""


def _headers() -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return headers


def mastodon_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, files: Any = None) -> Any:
    if not BASE_URL:
        return {"error": "MASTODON_BASE_URL is not set"}
    if not ACCESS_TOKEN:
        return {"error": "MASTODON_ACCESS_TOKEN is not set"}

    url = f"{API_BASE}{path}"
    try:
        response = requests.request(method, url, headers=_headers(), params=params, data=data, files=files, timeout=60)
    except Exception as exc:
        return {"error": str(exc)}

    try:
        payload = response.json()
    except Exception:
        payload = response.text

    if not response.ok:
        return {"error": f"HTTP {response.status_code}", "details": payload}

    return payload
