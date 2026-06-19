import os
import time
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def call_alpha_vantage(params: Dict[str, Any], timeout: float = 30.0) -> Dict[str, Any]:
    """Call Alpha Vantage and return a JSON-serializable dict.

    Alpha Vantage uses a single endpoint with query parameters.
    This helper appends the apikey and normalizes common error payloads.
    """
    api_key = _get_api_key()
    if not api_key:
        return {"error": "Missing environment variable ALPHAVANTAGE_API_KEY"}

    q = dict(params)
    q["apikey"] = api_key

    try:
        r = requests.get(BASE_URL, params=q, timeout=timeout)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    # Alpha Vantage sometimes returns 200 with an error message in JSON.
    content_type = r.headers.get("content-type", "")
    if "application/json" not in content_type and "text/json" not in content_type:
        # Could be CSV or HTML error.
        return {
            "error": "Non-JSON response from Alpha Vantage",
            "status_code": r.status_code,
            "content_type": content_type,
            "text": r.text[:2000],
        }

    try:
        data = r.json()
    except Exception as e:
        return {"error": f"Failed to parse JSON: {e}", "text": r.text[:2000]}

    if isinstance(data, dict):
        for k in ("Error Message", "Information", "Note"):
            if k in data:
                return {"error": data[k], "raw": data}

    return data


def throttle_if_needed(last_call_epoch: Optional[float], min_interval_s: float) -> float:
    """Simple client-side throttling helper."""
    now = time.time()
    if last_call_epoch is not None:
        sleep_for = (last_call_epoch + min_interval_s) - now
        if sleep_for > 0:
            time.sleep(sleep_for)
    return time.time()
