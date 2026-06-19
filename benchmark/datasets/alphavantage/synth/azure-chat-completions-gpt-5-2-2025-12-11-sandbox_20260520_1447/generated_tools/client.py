import os
import time
from typing import Any, Dict, Optional, Union

import requests

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def av_get(params: Dict[str, Any], *, timeout: int = 30) -> Union[Dict[str, Any], str]:
    """Perform a GET request to Alpha Vantage.

    Returns JSON dict when possible; otherwise returns raw text.
    Never raises for API-level errors; returns {"error": ...}.
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

    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}", "body": r.text}

    # Alpha Vantage sometimes returns JSON with error fields, or CSV text.
    ct = (r.headers.get("content-type") or "").lower()
    if "application/json" in ct or r.text.strip().startswith("{"):
        try:
            data = r.json()
        except Exception:
            return {"error": "Failed to parse JSON", "body": r.text}

        # Standard AV error fields
        for k in ("Error Message", "Information", "Note"):
            if isinstance(data, dict) and k in data:
                return {"error": data.get(k), "raw": data}
        return data

    return r.text


def throttle_sleep(seconds: float = 12.0) -> None:
    """Optional helper for agents to respect free-tier throttling."""
    time.sleep(seconds)
