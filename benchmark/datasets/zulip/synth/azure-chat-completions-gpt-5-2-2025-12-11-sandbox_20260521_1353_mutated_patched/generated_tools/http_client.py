import os
import json
from typing import Any, Dict, Optional, Tuple

import requests


class ZulipClient:
    def __init__(self):
        self.email = os.environ.get("ZULIP_EMAIL")
        self.api_key = os.environ.get("ZULIP_API_KEY")
        self.site = os.environ.get("ZULIP_SITE")
        if not self.email or not self.api_key or not self.site:
            raise RuntimeError(
                "Missing env vars: ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE are required"
            )
        self.base_url = self.site.rstrip("/") + "/api/v1"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        try:
            resp = requests.request(
                method,
                url,
                params=params,
                data=data,
                json=json_body,
                files=files,
                auth=(self.email, self.api_key),
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        try:
            payload = resp.json()
        except ValueError:
            payload = {"raw": resp.text}

        if resp.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("http_status", resp.status_code)
                return payload
            return {"error": "HTTP error", "http_status": resp.status_code, "body": payload}

        return payload if isinstance(payload, dict) else {"result": payload}


def dumps_if_needed(value: Any) -> Any:
    """Zulip expects some complex params as JSON-encoded strings (e.g. narrow, subscriptions)."""
    if value is None:
        return None
    if isinstance(value, (dict, list)):
        return json.dumps(value)
    return value
