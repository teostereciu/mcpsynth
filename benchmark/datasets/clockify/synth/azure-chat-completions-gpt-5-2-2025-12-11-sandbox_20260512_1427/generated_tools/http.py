import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.clockify.me/api/v1"


def _headers() -> Dict[str, str]:
    api_key = os.getenv("CLOCKIFY_API_KEY")
    if not api_key:
        return {}
    return {"X-Api-Key": api_key, "Content-Type": "application/json"}


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    """Make a Clockify API request and return JSON-serializable result or {error:...}."""
    if not os.getenv("CLOCKIFY_API_KEY"):
        return {"error": "CLOCKIFY_API_KEY environment variable is not set"}

    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=30)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    if resp.status_code >= 400:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return {"error": f"HTTP {resp.status_code}", "details": data}

    if resp.status_code == 204:
        return {"ok": True}

    try:
        return resp.json()
    except Exception:
        return resp.text
