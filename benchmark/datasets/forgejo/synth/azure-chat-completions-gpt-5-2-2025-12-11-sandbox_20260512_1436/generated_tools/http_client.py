import os
import requests
from typing import Any, Dict, Optional


def _base_url() -> str:
    base = os.getenv("CODEBERG_BASE_URL", "https://codeberg.org").rstrip("/")
    return f"{base}/api/v1"


def _headers() -> Dict[str, str]:
    token = os.getenv("CODEBERG_TOKEN", "").strip()
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    url = _base_url() + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=30)
    except Exception as e:
        return {"error": str(e), "url": url}

    if resp.status_code >= 400:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return {"error": f"HTTP {resp.status_code}", "details": data, "url": url}

    if resp.status_code == 204:
        return {"ok": True}

    ctype = resp.headers.get("content-type", "")
    if "application/json" in ctype:
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to decode JSON", "text": resp.text, "url": url}

    return resp.text
