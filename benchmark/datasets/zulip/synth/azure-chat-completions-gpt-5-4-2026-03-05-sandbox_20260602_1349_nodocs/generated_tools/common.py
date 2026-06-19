import os
from typing import Any, Dict, Optional

import requests


class ZulipClient:
    def __init__(self) -> None:
        self.site = (os.getenv("ZULIP_SITE") or "").rstrip("/")
        self.email = os.getenv("ZULIP_EMAIL") or ""
        self.api_key = os.getenv("ZULIP_API_KEY") or ""

    def configured(self) -> bool:
        return bool(self.site and self.email and self.api_key)

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not self.configured():
            return {
                "error": "Missing Zulip configuration. Set ZULIP_SITE, ZULIP_EMAIL, and ZULIP_API_KEY."
            }

        url = f"{self.site}/api/v1{path}"
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                auth=(self.email, self.api_key),
                params=params if method.upper() == "GET" else None,
                data=params if method.upper() != "GET" and files is None else params,
                files=files,
                timeout=60,
            )
        except requests.RequestException as exc:
            return {"error": str(exc), "endpoint": f"{method.upper()} {path}"}

        try:
            data = response.json()
        except ValueError:
            return {
                "error": "Non-JSON response from Zulip API",
                "status_code": response.status_code,
                "text": response.text,
            }

        if response.ok:
            return data
        if isinstance(data, dict):
            data.setdefault("status_code", response.status_code)
            return data
        return {"error": "Request failed", "status_code": response.status_code, "response": data}


client = ZulipClient()


def json_dumps(value: Any) -> str:
    import json

    return json.dumps(value)
