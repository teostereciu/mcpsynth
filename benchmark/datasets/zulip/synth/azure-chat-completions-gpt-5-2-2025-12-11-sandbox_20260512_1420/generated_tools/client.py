import os
import json
from typing import Any, Dict, Optional

import requests


class ZulipClient:
    def __init__(
        self,
        site: Optional[str] = None,
        email: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self.site = (site or os.getenv("ZULIP_SITE") or "").rstrip("/")
        self.email = email or os.getenv("ZULIP_EMAIL")
        self.api_key = api_key or os.getenv("ZULIP_API_KEY")
        self.timeout = timeout

    @property
    def base_url(self) -> str:
        return f"{self.site}/api/v1"

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Any = None,
    ) -> Dict[str, Any]:
        if not self.site:
            return {"error": "ZULIP_SITE is not set"}
        if not self.email or not self.api_key:
            return {"error": "ZULIP_EMAIL/ZULIP_API_KEY are not set"}

        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data,
                files=files,
                auth=(self.email, self.api_key),
                timeout=self.timeout,
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
            return {"error": "HTTP error", "http_status": resp.status_code, "response": payload}

        return payload if isinstance(payload, dict) else {"result": payload}


def dumps_narrow(narrow: Any) -> str:
    return json.dumps(narrow)
