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
    json_body: Optional[Dict[str, Any]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any]:
    """Make a Spoonacular API request and return JSON-serializable dict.

    Returns {"error": ...} on failure.
    """
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
    q = dict(params or {})
    q["apiKey"] = api_key

    try:
        resp = requests.request(method.upper(), url, params=q, json=json_body, timeout=timeout)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        # Try to parse JSON error
        try:
            data = resp.json()
        except Exception:
            data = {"message": resp.text}
        return {
            "error": "HTTP error",
            "status_code": resp.status_code,
            "response": data,
            "content_type": content_type,
            "url": resp.url,
        }

    # Some endpoints return HTML or images; we still want JSON-serializable output.
    if "application/json" in content_type or "application/json" in content_type.lower():
        try:
            return resp.json()
        except Exception as e:
            return {"error": f"Failed to parse JSON: {e}", "text": resp.text, "url": resp.url}

    # For non-JSON, return text plus metadata.
    return {
        "content_type": content_type,
        "text": resp.text,
        "url": resp.url,
    }
