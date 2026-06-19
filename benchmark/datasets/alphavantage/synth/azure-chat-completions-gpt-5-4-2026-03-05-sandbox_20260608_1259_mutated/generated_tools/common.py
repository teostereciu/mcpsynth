import os
from typing import Any, Dict

import requests

BASE_URL = "https://www.alphavantage.co/query"


def _api_key() -> str | None:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def call_alpha_vantage(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = _api_key()
    if not api_key:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}

    query = {k: v for k, v in params.items() if v is not None}
    query["apikey"] = api_key

    try:
        response = requests.get(BASE_URL, params=query, timeout=30)
        response.raise_for_status()
    except requests.RequestException as exc:
        return {"error": f"HTTP request failed: {exc}"}

    try:
        data = response.json()
    except ValueError:
        return {"error": "API returned a non-JSON response", "text": response.text[:1000]}

    if isinstance(data, dict):
        for key in ("Error Message", "Information", "Note"):
            if key in data:
                return {"error": data[key], "raw": data}
        if not data:
            return {"error": "API returned an empty response"}

    return data
