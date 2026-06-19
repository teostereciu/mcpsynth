import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> Optional[str]:
    return os.getenv("SPOONACULAR_API_KEY")


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Make a Spoonacular request and return JSON-serializable dict.

    Errors are returned as {"error": ..., "status": ..., "details": ...}.
    """
    key = _api_key()
    if not key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = BASE_URL + path
    q = dict(params or {})
    q["apiKey"] = key

    try:
        resp = requests.request(method.upper(), url, params=q, timeout=30)
    except Exception as e:
        return {"error": "Request failed", "details": str(e)}

    content_type = resp.headers.get("content-type", "")
    try:
        data = resp.json() if "application/json" in content_type else resp.text
    except Exception:
        data = resp.text

    if resp.status_code >= 400:
        return {
            "error": "Spoonacular API error",
            "status": resp.status_code,
            "details": data,
        }

    # Ensure dict return for MCP friendliness
    if isinstance(data, dict):
        return data
    return {"result": data}
