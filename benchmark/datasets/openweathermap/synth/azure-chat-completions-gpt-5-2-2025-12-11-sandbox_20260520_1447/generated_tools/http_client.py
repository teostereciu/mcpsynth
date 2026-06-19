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

    def _request(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

        url = f"{self.base_url}{path}"
        q = dict(params or {})
        q["appid"] = self.api_key

        try:
            resp = requests.get(url, params=q, timeout=self.timeout_s)
        except requests.RequestException as e:
            return {"error": f"Network error: {e}"}

        # OpenWeather sometimes returns JSON even for errors; sometimes plain text.
        try:
            data: Any = resp.json()
        except ValueError:
            data = resp.text

        if resp.status_code >= 400:
            return {
                "error": "OpenWeather API error",
                "status_code": resp.status_code,
                "response": data,
                "url": resp.url,
            }

        # Be nice to free tier: tiny delay to reduce burstiness in agent loops.
        time.sleep(0.05)
        return data if isinstance(data, dict) else {"data": data}
