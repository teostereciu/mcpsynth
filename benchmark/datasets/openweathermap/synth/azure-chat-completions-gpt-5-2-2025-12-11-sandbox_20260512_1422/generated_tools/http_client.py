import os
import time
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.openweathermap.org"


class OpenWeatherClient:
    def __init__(self, api_key: Optional[str] = None, base_url: str = BASE_URL, timeout_s: int = 30):
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.timeout_s = timeout_s

    def _request(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

        url = f"{self.base_url}{path}"
        q = dict(params or {})
        q["appid"] = self.api_key

        try:
            resp = requests.get(url, params=q, timeout=self.timeout_s)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

        content_type = resp.headers.get("Content-Type", "")
        is_json = "application/json" in content_type

        if resp.status_code >= 400:
            body: Any
            if is_json:
                try:
                    body = resp.json()
                except Exception:
                    body = resp.text
            else:
                body = resp.text
            return {
                "error": "OpenWeather API error",
                "status_code": resp.status_code,
                "url": resp.url,
                "response": body,
            }

        if is_json:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON response", "status_code": resp.status_code, "text": resp.text}

        return {"status_code": resp.status_code, "text": resp.text}


def unix_now() -> int:
    return int(time.time())
