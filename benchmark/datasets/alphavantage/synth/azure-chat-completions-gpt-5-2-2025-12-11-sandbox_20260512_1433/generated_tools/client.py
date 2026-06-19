import os
import time
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://www.alphavantage.co/query"


def _now() -> float:
    return time.time()


class AlphaVantageClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = BASE_URL,
        timeout_s: float = 30.0,
    ):
        self.api_key = api_key or os.getenv("ALPHAVANTAGE_API_KEY")
        self.base_url = base_url
        self.timeout_s = timeout_s

    def request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing ALPHAVANTAGE_API_KEY environment variable"}

        q = dict(params)
        q["apikey"] = self.api_key

        try:
            resp = requests.get(self.base_url, params=q, timeout=self.timeout_s)
        except Exception as e:
            return {"error": f"Request failed: {e}"}

        text = resp.text or ""
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}", "body": text[:2000]}

        # Alpha Vantage sometimes returns CSV when datatype=csv
        if q.get("datatype") == "csv":
            return {"datatype": "csv", "data": text}

        try:
            data = resp.json()
        except Exception:
            return {"error": "Non-JSON response", "body": text[:2000]}

        # Standard AV error envelopes
        if isinstance(data, dict):
            for k in ("Error Message", "Information", "Note"):
                if k in data:
                    return {"error": data.get(k), "raw": data}

        return data
