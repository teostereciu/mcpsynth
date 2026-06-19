import os
import time
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://www.alphavantage.co/query"


class AlphaVantageClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        session: Optional[requests.Session] = None,
        timeout_s: float = 30.0,
    ) -> None:
        self.api_key = api_key or os.getenv("ALPHAVANTAGE_API_KEY")
        self.session = session or requests.Session()
        self.timeout_s = timeout_s

    def request(self, function: str, **params: Any) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}

        q: Dict[str, Any] = {"function": function, "apikey": self.api_key}
        for k, v in params.items():
            if v is None:
                continue
            q[k] = v

        try:
            resp = self.session.get(BASE_URL, params=q, timeout=self.timeout_s)
        except Exception as e:
            return {"error": f"Request failed: {e}"}

        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}", "body": resp.text}

        # Alpha Vantage sometimes returns CSV for some endpoints; docs here are JSON.
        ctype = resp.headers.get("content-type", "")
        if "application/json" not in ctype and resp.text.strip().startswith("{") is False:
            return {"error": "Unexpected non-JSON response", "content_type": ctype, "body": resp.text}

        try:
            data = resp.json()
        except Exception as e:
            return {"error": f"Failed to parse JSON: {e}", "body": resp.text}

        # Standard AV error/limit fields
        if isinstance(data, dict):
            if "Error Message" in data:
                return {"error": data.get("Error Message"), "raw": data}
            if "Information" in data:
                return {"error": data.get("Information"), "raw": data}
            if "Note" in data:
                return {"error": data.get("Note"), "raw": data}

        return data


def normalize_interval(interval: str) -> str:
    allowed = {"1min", "5min", "15min", "30min", "60min"}
    if interval not in allowed:
        raise ValueError(f"interval must be one of {sorted(allowed)}")
    return interval


def normalize_outputsize(outputsize: str) -> str:
    allowed = {"compact", "full"}
    if outputsize not in allowed:
        raise ValueError(f"outputsize must be one of {sorted(allowed)}")
    return outputsize


def normalize_series_type(series_type: str) -> str:
    allowed = {"close", "open", "high", "low"}
    if series_type not in allowed:
        raise ValueError(f"series_type must be one of {sorted(allowed)}")
    return series_type


def normalize_ma_type(ma_type: int) -> int:
    if not (0 <= ma_type <= 8):
        raise ValueError("ma_type must be an integer 0..8")
    return ma_type


def safe_validate(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs), None
    except Exception as e:
        return None, str(e)
