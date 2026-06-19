import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://www.alphavantage.co/query"
TIMEOUT = 30


def alpha_vantage_get(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    if not api_key:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}

    query = {k: v for k, v in params.items() if v is not None}
    query["apikey"] = api_key

    try:
        response = requests.get(BASE_URL, params=query, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        return {"error": f"HTTP request failed: {exc}"}

    try:
        data = response.json()
    except ValueError:
        return {"error": "API returned a non-JSON response", "text": response.text[:1000]}

    if isinstance(data, dict):
        if data.get("Error Message"):
            return {"error": data["Error Message"], "params": query}
        if data.get("Information"):
            return {"error": data["Information"], "params": query}
        if data.get("Note"):
            return {"error": data["Note"], "params": query}

    return data


def build_result(tool: str, params: Dict[str, Any], data: Dict[str, Any]) -> Dict[str, Any]:
    if isinstance(data, dict) and data.get("error"):
        return data
    return {"tool": tool, "params": {k: v for k, v in params.items() if v is not None}, "data": data}
