import os
import time
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.openweathermap.org"


def _get_api_key() -> Optional[str]:
    return os.getenv("OPENWEATHER_API_KEY")


def owm_get(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Internal helper for OpenWeatherMap GET requests.

    Returns JSON dicts/lists wrapped in a dict when needed.
    Never raises for expected HTTP errors.
    """
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    q = dict(params or {})
    q["appid"] = api_key

    try:
        resp = requests.get(url, params=q, timeout=30)
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}

    # OpenWeatherMap often returns JSON error bodies with cod/message
    content_type = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        try:
            data = resp.json() if "json" in content_type else {"message": resp.text}
        except Exception:
            data = {"message": resp.text}
        return {
            "error": "OpenWeatherMap API error",
            "status_code": resp.status_code,
            "details": data,
            "url": resp.url,
        }

    try:
        data = resp.json()
    except Exception:
        return {"error": "Invalid JSON response", "status_code": resp.status_code, "text": resp.text}

    # Ensure JSON-serializable top-level
    if isinstance(data, (dict, list)):
        return {"data": data}
    return {"data": data}
