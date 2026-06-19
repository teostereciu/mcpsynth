import os
import json
from typing import Any, Dict, Optional

import requests


class ZulipClient:
    def __init__(self, site: Optional[str] = None, email: Optional[str] = None, api_key: Optional[str] = None):
        self.site = (site or os.environ.get("ZULIP_SITE") or "").rstrip("/")
        self.email = email or os.environ.get("ZULIP_EMAIL")
        self.api_key = api_key or os.environ.get("ZULIP_API_KEY")
        if not self.site:
            raise ValueError("ZULIP_SITE is required")
        if not self.email or not self.api_key:
            raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY are required")

        self.base = f"{self.site}/api/v1"
        self.session = requests.Session()
        self.session.auth = (self.email, self.api_key)

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = self.base + path
        try:
            if method in ("GET", "DELETE"):
                resp = self.session.request(method, url, params=params, timeout=30)
            else:
                # Zulip expects form-encoded; requests uses application/x-www-form-urlencoded by default for data dict
                resp = self.session.request(method, url, data=params or {}, timeout=30)
        except requests.RequestException as e:
            return {"error": str(e)}

        try:
            data = resp.json()
        except ValueError:
            return {"error": f"Non-JSON response (status {resp.status_code})", "text": resp.text}

        if resp.status_code >= 400 or data.get("result") == "error":
            return {"error": data.get("msg") or f"HTTP {resp.status_code}", "data": data, "status": resp.status_code}
        return data


def _maybe_json_dumps(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (dict, list)):
        return json.dumps(value)
    return value
