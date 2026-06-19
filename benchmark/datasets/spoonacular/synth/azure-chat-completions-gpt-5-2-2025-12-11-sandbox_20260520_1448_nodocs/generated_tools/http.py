import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> Optional[str]:
    return os.environ.get("SPOONACULAR_API_KEY")


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Make a Spoonacular request and return JSON-serializable dict.

    Errors are returned as {"error": "...", "status": int, "details": ...}.
    """
    key = _api_key()
    if not key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    q = dict(params or {})
    q["apiKey"] = key

    try:
        resp = requests.request(method.upper(), url, params=q, timeout=30)
    except Exception as e:
        return {"error": "Request failed", "details": str(e)}

    content_type = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        details: Any
        try:
            details = resp.json() if "application/json" in content_type else resp.text
        except Exception:
            details = resp.text
        return {"error": "HTTP error", "status": resp.status_code, "details": details}

    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception as e:
            return {"error": "Failed to parse JSON", "details": str(e)}
        # Ensure dict return for MCP tool consistency
        if isinstance(data, dict):
            return data
        return {"data": data}

    # Non-JSON endpoints (e.g., visualization) return HTML/text
    return {"content": resp.text, "content_type": content_type}
