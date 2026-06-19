import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://www.alphavantage.co/query"


def _get_api_key() -> Optional[str]:
    return os.getenv("ALPHAVANTAGE_API_KEY")


def av_get(params: Dict[str, Any], timeout: int = 30) -> Dict[str, Any]:
    """Perform a GET request to Alpha Vantage and return JSON-serializable dict.

    Alpha Vantage uses a single endpoint with query params including `function` and `apikey`.
    """
    apikey = _get_api_key()
    if not apikey:
        return {"error": "Missing environment variable ALPHAVANTAGE_API_KEY"}

    q = dict(params)
    q["apikey"] = apikey

    try:
        r = requests.get(BASE_URL, params=q, timeout=timeout)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}", "text": r.text}

    # Some endpoints can return CSV if format=csv; we keep it as text.
    ctype = r.headers.get("Content-Type", "")
    if "text/csv" in ctype or q.get("format") == "csv":
        return {"csv": r.text}

    try:
        data = r.json()
    except Exception:
        return {"error": "Failed to parse JSON", "text": r.text}

    # Alpha Vantage error conventions
    if isinstance(data, dict):
        if "Error Message" in data:
            return {"error": data.get("Error Message"), "raw": data}
        if "Information" in data:
            return {"error": data.get("Information"), "raw": data}
        if "Note" in data:
            return {"error": data.get("Note"), "raw": data}

    return data
