import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> Optional[str]:
    return os.getenv("SPOONACULAR_API_KEY")


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None, timeout: int = 30) -> Any:
    """Make a Spoonacular API request and return JSON-serializable data.

    Errors are returned as {"error": "...", "status": int, "details": ...}.
    """
    key = _api_key()
    if not key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = BASE_URL + path
    q = dict(params or {})
    q["apiKey"] = key

    try:
        resp = requests.request(method.upper(), url, params=q, json=json, timeout=timeout)
    except Exception as e:
        return {"error": "Request failed", "details": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    try:
        data = resp.json() if "application/json" in content_type else resp.text
    except Exception:
        data = resp.text

    if resp.status_code >= 400:
        return {"error": "API error", "status": resp.status_code, "details": data}

    return data
