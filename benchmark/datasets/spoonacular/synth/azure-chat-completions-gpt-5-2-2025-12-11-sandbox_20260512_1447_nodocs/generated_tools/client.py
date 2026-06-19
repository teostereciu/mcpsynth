import os
import time
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.spoonacular.com"


class SpoonacularClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = BASE_URL,
        timeout_s: int = 60,
        max_retries: int = 3,
        backoff_s: float = 0.8,
    ):
        self.api_key = api_key or os.getenv("SPOONACULAR_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.timeout_s = timeout_s
        self.max_retries = max_retries
        self.backoff_s = backoff_s

    def _request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        if not self.api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

        url = f"{self.base_url}{path}"
        params = dict(params or {})
        params["apiKey"] = self.api_key

        last_err = None
        for attempt in range(self.max_retries):
            try:
                resp = requests.request(method, url, params=params, json=json, timeout=self.timeout_s)
                if resp.status_code >= 400:
                    try:
                        data = resp.json()
                    except Exception:
                        data = {"message": resp.text}
                    return {
                        "error": "HTTP error",
                        "status_code": resp.status_code,
                        "response": data,
                        "url": resp.url,
                    }
                if resp.status_code == 204:
                    return None
                ctype = resp.headers.get("content-type", "")
                if "application/json" in ctype:
                    return resp.json()
                return resp.text
            except Exception as e:
                last_err = e
                time.sleep(self.backoff_s * (2**attempt))

        return {"error": "Request failed", "message": str(last_err)}

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def post(self, path: str, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        return self._request("POST", path, params=params, json=json)
