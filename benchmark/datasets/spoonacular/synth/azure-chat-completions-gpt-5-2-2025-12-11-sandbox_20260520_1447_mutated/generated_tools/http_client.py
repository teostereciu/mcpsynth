import os
import time
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.spoonacular.com"


def _get_api_key() -> Optional[str]:
    return os.getenv("SPOONACULAR_API_KEY")


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Any = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Make a Spoonacular request and return JSON-serializable dict.

    Errors are returned as {"error": "...", "status": int, ...}.
    """
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = BASE_URL + path
    q = dict(params or {})
    q["apiKey"] = api_key

    try:
        resp = requests.request(method.upper(), url, params=q, json=json, timeout=timeout)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        # Try to parse JSON error
        try:
            data = resp.json() if "json" in content_type else {"message": resp.text}
        except Exception:
            data = {"message": resp.text}
        return {
            "error": "Spoonacular API error",
            "status": resp.status_code,
            "details": data,
            "url": resp.url,
        }

    # Success
    if resp.status_code == 204:
        return {"status": 204}

    if "json" in content_type:
        try:
            data = resp.json()
        except Exception as e:
            return {"error": f"Failed to parse JSON: {e}", "status": resp.status_code, "text": resp.text}
        # Ensure dict return
        if isinstance(data, dict):
            return data
        return {"data": data}

    # Non-JSON response
    return {"data": resp.text, "content_type": content_type, "status": resp.status_code}
