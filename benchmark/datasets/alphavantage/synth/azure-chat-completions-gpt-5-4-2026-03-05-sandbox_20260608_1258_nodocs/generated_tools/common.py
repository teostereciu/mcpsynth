import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def alpha_vantage_get(params: Dict[str, Any]) -> Dict[str, Any]:
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}

    query = dict(params)
    query["apikey"] = api_key

    try:
        response = requests.get(BASE_URL, params=query, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        return {"error": f"HTTP request failed: {exc}"}
    except ValueError as exc:
        return {"error": f"Failed to parse JSON response: {exc}"}

    if isinstance(data, dict):
        if "Error Message" in data:
            return {"error": data["Error Message"], "raw": data}
        if "Note" in data:
            return {"error": data["Note"], "raw": data}
        if "Information" in data:
            return {"error": data["Information"], "raw": data}

    return data
