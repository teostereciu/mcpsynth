import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def av_get(params: Dict[str, Any], timeout: float = 30.0) -> Dict[str, Any]:
    """Perform a GET request to Alpha Vantage and return JSON-serializable dict.

    Alpha Vantage uses a single endpoint with query parameters.
    """
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}

    q = dict(params)
    q["apikey"] = api_key

    try:
        resp = requests.get(BASE_URL, params=q, timeout=timeout)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    if resp.status_code != 200:
        return {"error": f"HTTP {resp.status_code}", "body": resp.text}

    try:
        data = resp.json()
    except Exception:
        return {"error": "Non-JSON response", "body": resp.text}

    # Alpha Vantage error conventions
    if isinstance(data, dict):
        if "Error Message" in data:
            return {"error": data.get("Error Message"), "raw": data}
        if "Information" in data:
            return {"error": data.get("Information"), "raw": data}
        if "Note" in data:
            return {"error": data.get("Note"), "raw": data}

    return data
