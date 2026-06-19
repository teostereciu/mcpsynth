import os
import time
from typing import Any, Dict, Optional

import requests


SLACK_API_BASE_URL = "https://slack.com/api"


class SlackWebAPIClient:
    def __init__(self, token: Optional[str] = None, base_url: str = SLACK_API_BASE_URL, timeout_s: int = 30):
        self.token = token or os.getenv("SLACK_BOT_TOKEN")
        self.base_url = base_url.rstrip("/")
        self.timeout_s = timeout_s

    def _headers(self) -> Dict[str, str]:
        if not self.token:
            return {"Content-Type": "application/json"}
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def request(self, method: str, api_method: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not api_method.startswith("/"):
            api_method = "/" + api_method
        url = self.base_url + api_method
        try:
            if method.upper() == "GET":
                resp = requests.get(url, headers=self._headers(), params=params or {}, timeout=self.timeout_s)
            else:
                resp = requests.post(url, headers=self._headers(), json=params or {}, timeout=self.timeout_s)
        except requests.RequestException as e:
            return {"ok": False, "error": "request_exception", "detail": str(e)}

        # Slack returns JSON even on errors
        try:
            data = resp.json()
        except ValueError:
            return {"ok": False, "error": "non_json_response", "status": resp.status_code, "text": resp.text}

        # Handle rate limiting hints
        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            if retry_after is not None:
                try:
                    data["retry_after"] = int(retry_after)
                except ValueError:
                    data["retry_after"] = retry_after
            data.setdefault("error", "rate_limited")
            data["ok"] = False

        data.setdefault("http_status", resp.status_code)
        return data

    def get(self, method_name: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.request("GET", f"/{method_name}", params=params)

    def post(self, method_name: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.request("POST", f"/{method_name}", params=params)


def _clean_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}
