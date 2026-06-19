"""HTTP utilities for OpenWeatherMap API."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.openweathermap.org"


def _get_api_key() -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY environment variable is not set")
    return api_key


def get_json(endpoint: str, params: Optional[Dict[str, Any]] = None, timeout_s: int = 20) -> Dict[str, Any]:
    """Perform a GET request and return JSON.

    Returns an error dict for expected failures (HTTP errors, network errors).
    """
    params = dict(params or {})
    try:
        params["appid"] = _get_api_key()
    except Exception as e:
        return {"error": str(e)}

    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.get(url, params=params, timeout=timeout_s)
        # OpenWeatherMap often returns JSON even for errors.
        if resp.status_code >= 400:
            try:
                return {"error": f"HTTP {resp.status_code}", "details": resp.json()}
            except Exception:
                return {"error": f"HTTP {resp.status_code}", "details": resp.text}
        return resp.json()
    except requests.RequestException as e:
        return {"error": "request_failed", "details": str(e)}
