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

    @property
    def base_url(self) -> str:
        return f"{self.site}/api/v1"

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, files=None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method,
                url=url,
                auth=(self.email, self.api_key),
                params=params,
                data=data,
                files=files,
                timeout=30,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("content-type", "")
        if "application/json" in content_type:
            try:
                payload = resp.json()
            except Exception:
                payload = {"error": "Failed to parse JSON response", "status_code": resp.status_code, "text": resp.text}
        else:
            payload = {"status_code": resp.status_code, "text": resp.text}

        if resp.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("status_code", resp.status_code)
                payload.setdefault("error", payload.get("msg") or resp.reason)
                return payload
            return {"error": resp.reason, "status_code": resp.status_code, "body": payload}

        return payload if isinstance(payload, dict) else {"result": payload}


def _maybe_json_dumps(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (dict, list)):
        return json.dumps(value)
    return value
