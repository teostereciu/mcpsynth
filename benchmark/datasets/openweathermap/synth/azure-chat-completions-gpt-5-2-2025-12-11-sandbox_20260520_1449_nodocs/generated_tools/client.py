import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.openweathermap.org"


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


def request_json(
    path: str,
    params: Dict[str, Any],
    *,
    base_url: str = BASE_URL,
    timeout: int = 30,
) -> Dict[str, Any]:
    """Internal helper. Returns JSON dict or {"error": ...}."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

    url = base_url.rstrip("/") + path
    q = dict(params or {})
    q["appid"] = api_key
    q = _clean_params(q)

    try:
        resp = requests.get(url, params=q, timeout=timeout)
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}

    # OpenWeatherMap often returns JSON even on errors
    try:
        data = resp.json()
    except ValueError:
        data = {"error": f"Non-JSON response (status {resp.status_code})", "text": resp.text}

    if resp.status_code >= 400:
        if isinstance(data, dict) and "error" not in data:
            # Normalize common OWM error fields
            msg = data.get("message") or data.get("cod") or resp.reason
            return {"error": str(msg), "status": resp.status_code, "response": data}
        if isinstance(data, dict):
            data.setdefault("status", resp.status_code)
        return data if isinstance(data, dict) else {"error": "Request failed", "status": resp.status_code, "response": data}

    return data if isinstance(data, dict) else {"data": data}
