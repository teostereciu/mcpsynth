import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def call_alpha_vantage(params: Dict[str, Any], timeout: float = 30.0) -> Dict[str, Any]:
    """Call Alpha Vantage query endpoint.

    Returns JSON dict or {"error": ...}.
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
        if "Information" in data and ("Thank you" not in str(data.get("Information"))):
            return {"error": data.get("Information"), "raw": data}
        if "Note" in data:
            return {"error": data.get("Note"), "raw": data}

    return data
