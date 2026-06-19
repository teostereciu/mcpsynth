import os
import time
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.openweathermap.org"


class OpenWeatherClient:
    def __init__(self, api_key: Optional[str] = None, base_url: str = BASE_URL, timeout: int = 30):
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _request(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing OPENWEATHER_API_KEY environment variable"}

        url = f"{self.base_url}{path}"
        q = dict(params or {})
        q["appid"] = self.api_key

        try:
            resp = requests.get(url, params=q, timeout=self.timeout)
        except requests.RequestException as e:
            return {"error": f"Network error: {e}"}

        # OpenWeather often returns JSON even on errors
        try:
            data = resp.json()
        except ValueError:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            # Normalize common error shapes
            msg = None
            if isinstance(data, dict):
                msg = data.get("message") or data.get("error")
            return {
                "error": msg or f"HTTP {resp.status_code}",
                "status_code": resp.status_code,
                "response": data,
                "url": resp.url,
            }

        return data if isinstance(data, dict) else {"data": data}


def _clean_none(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


def _coerce_units(units: Optional[str]) -> Optional[str]:
    if units is None:
        return None
    u = units.lower().strip()
    if u in {"standard", "metric", "imperial"}:
        return u
    return units


def _coerce_lang(lang: Optional[str]) -> Optional[str]:
    return lang.strip() if isinstance(lang, str) and lang.strip() else None


def _sleep_if_needed(last_call_ts: Optional[float], min_interval_s: float = 1.0) -> float:
    now = time.time()
    if last_call_ts is not None:
        dt = now - last_call_ts
        if dt < min_interval_s:
            time.sleep(min_interval_s - dt)
    return time.time()
