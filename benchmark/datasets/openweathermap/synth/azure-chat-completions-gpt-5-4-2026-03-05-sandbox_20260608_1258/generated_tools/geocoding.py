import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.openweathermap.org"


def _get_api_key() -> Optional[str]:
    return os.getenv("OPENWEATHER_API_KEY")


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = _get_api_key()
    if not api_key:
        return {"error": "OPENWEATHER_API_KEY environment variable is not set"}

    query = {k: v for k, v in params.items() if v is not None}
    query["appid"] = api_key

    try:
        response = requests.get(f"{BASE_URL}{path}", params=query, timeout=30)
    except requests.RequestException as exc:
        return {"error": f"Request failed: {exc}"}

    try:
        data = response.json()
    except ValueError:
        return {"error": f"Non-JSON response received with status {response.status_code}", "status_code": response.status_code, "text": response.text}

    if not response.ok:
        if isinstance(data, dict):
            data.setdefault("status_code", response.status_code)
            return data
        return {"error": "API request failed", "status_code": response.status_code, "details": data}

    return {"data": data}


def geocode_direct(query: str, limit: int = 5) -> Dict[str, Any]:
    if not query:
        return {"error": "query is required"}
    if limit < 1 or limit > 5:
        return {"error": "limit must be between 1 and 5"}
    return _request("/geo/1.0/direct", {"q": query, "limit": limit})


def geocode_zip(zip_code: str, country_code: Optional[str] = None) -> Dict[str, Any]:
    if not zip_code:
        return {"error": "zip_code is required"}
    zip_param = f"{zip_code},{country_code}" if country_code else zip_code
    return _request("/geo/1.0/zip", {"zip": zip_param})


def geocode_reverse(lat: float, lon: float, limit: int = 5) -> Dict[str, Any]:
    if limit < 1:
        return {"error": "limit must be at least 1"}
    return _request("/geo/1.0/reverse", {"lat": lat, "lon": lon, "limit": limit})
