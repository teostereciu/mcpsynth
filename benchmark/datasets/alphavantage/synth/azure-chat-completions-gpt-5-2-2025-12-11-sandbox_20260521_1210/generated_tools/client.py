import os
import time
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def call_alpha_vantage(params: Dict[str, Any], timeout: int = 30) -> Dict[str, Any]:
    """Call Alpha Vantage query endpoint.

    Returns JSON dict on success, or {"error": ...} on failure.
    """
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing environment variable ALPHAVANTAGE_API_KEY"}

    q = dict(params)
    q["apikey"] = api_key

    try:
        resp = requests.get(BASE_URL, params=q, timeout=timeout)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    if resp.status_code != 200:
        return {"error": f"HTTP {resp.status_code}", "text": resp.text}

    # Alpha Vantage sometimes returns JSON error payloads with 200
    try:
        data = resp.json()
    except Exception:
        return {"error": "Non-JSON response", "text": resp.text}

    if isinstance(data, dict):
        for k in ("Error Message", "Information", "Note"):
            if k in data:
                return {"error": data[k], "raw": data}

    return data


def maybe_sleep_for_rate_limit(seconds: float = 0.0) -> None:
    """Optional helper for callers that want to throttle."""
    if seconds and seconds > 0:
        time.sleep(seconds)
