import os
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.spoonacular.com"


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    cleaned: Dict[str, Any] = {}
    for k, v in params.items():
        if v is None:
            continue
        cleaned[k] = v
    return cleaned


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Any = None, headers: Optional[Dict[str, str]] = None, timeout: int = 30) -> Any:
    """Make a Spoonacular API request and return JSON-serializable output.

    Errors are returned as {"error": "...", "status": int, "details": ...}.
    """
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    q = dict(params or {})
    q["apiKey"] = api_key
    q = _clean_params(q)

    try:
        resp = requests.request(method.upper(), url, params=q, json=data, headers=headers, timeout=timeout)
    except Exception as e:
        return {"error": "Request failed", "details": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    try:
        if "application/json" in content_type:
            payload = resp.json()
        else:
            payload = resp.text
    except Exception as e:
        payload = resp.text
        return {"error": "Failed to parse response", "status": resp.status_code, "details": str(e), "raw": payload}

    if resp.status_code >= 400:
        return {"error": "API error", "status": resp.status_code, "details": payload}

    return payload
