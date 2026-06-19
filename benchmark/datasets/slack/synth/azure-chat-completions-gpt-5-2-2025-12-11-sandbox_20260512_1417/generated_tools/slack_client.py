import os
import time
from typing import Any, Dict, Optional

import requests


SLACK_BASE_URL = "https://slack.com/api"


class SlackClient:
    def __init__(self, token: Optional[str] = None, base_url: str = SLACK_BASE_URL, timeout: int = 30):
        self.token = token or os.getenv("SLACK_BOT_TOKEN")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        if not self.token:
            return {"Content-Type": "application/json"}
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def request(self, method: str, api_method: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not api_method.startswith("/"):
            api_method = "/" + api_method
        url = self.base_url + api_method
        try:
            resp = requests.request(method.upper(), url, headers=self._headers(), json=json or {}, timeout=self.timeout)
        except requests.RequestException as e:
            return {"ok": False, "error": str(e)}

        # Slack returns JSON always
        try:
            data = resp.json()
        except ValueError:
            return {"ok": False, "error": f"non_json_response status={resp.status_code}", "text": resp.text}

        # Normalize rate limiting info if present
        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            if retry_after is not None:
                data.setdefault("retry_after", retry_after)
            data.setdefault("error", "rate_limited")
            data.setdefault("ok", False)

        # If Slack says ok=false, just return it; don't raise.
        data.setdefault("http_status", resp.status_code)
        return data


_client_singleton: Optional[SlackClient] = None


def get_client() -> SlackClient:
    global _client_singleton
    if _client_singleton is None:
        _client_singleton = SlackClient()
    return _client_singleton
