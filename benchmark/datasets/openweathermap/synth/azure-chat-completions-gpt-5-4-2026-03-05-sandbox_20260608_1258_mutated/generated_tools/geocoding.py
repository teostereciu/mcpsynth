import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.openweathermap.org"


def _get_api_key() -> Optional[str]:
    return os.getenv("OPENWEATHER_API_KEY")


def _request(path: str, params: Dict[str, Any]) -> Dict[str, Any] | list:
    api_key = _get_api_key()
    if not api_key:
        return {"error": "OPENWEATHER_API_KEY is not set"}

    query = {k: v for k, v in params.items() if v is not None}
    query["appid"] = api_key

    try:
        response = requests.get(f"{BASE_URL}{path}", params=query, timeout=30)
    except requests.RequestException as exc:
        return {"error": f"Request failed: {exc}"}

    try:
        data = response.json()
    except ValueError:
        return {"error": f"Unexpected non-JSON response", "status_code": response.status_code, "text": response.text}

    if not response.ok:
        if isinstance(data, dict):
            data.setdefault("status_code", response.status_code)
            return data
        return {"error": "API request failed", "status_code": response.status_code, "details": data}

    return data


def geocode_direct(query: str, limit: int = 5):
    if not query:
        return {"error": "query is required"}
    return _request("/geo/1.0/direct", {"q": query, "limit": limit})


def geocode_zip(zip_code: str):
    if not zip_code:
        return {"error": "zip_code is required"}
    return _request("/geo/1.0/zip", {"zip": zip_code})


def geocode_reverse(latitude: float, longitude: float, limit: int = 5):
    return _request("/geo/1.0/reverse", {"lat": latitude, "lon": longitude, "limit": limit, "latitude": latitude, "longitude": longitude})
