import os
import json
from typing import Any, Dict, Optional, Tuple

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

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        url = self.base_url + path
        try:
            resp = requests.request(
                method=method,
                url=url,
                auth=(self.email, self.api_key),
                params=params if method.upper() == "GET" else None,
                data=params if method.upper() != "GET" and files is None and json_body is None else None,
                json=json_body,
                files=files,
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"result": "error", "error": str(e)}

        try:
            data = resp.json()
        except ValueError:
            return {"result": "error", "error": f"Non-JSON response ({resp.status_code})", "text": resp.text}

        if resp.status_code >= 400 and data.get("result") != "error":
            data = {"result": "error", "error": data, "status_code": resp.status_code}
        return data


def _maybe_json_loads(value: Any) -> Any:
    if isinstance(value, str):
        v = value.strip()
        if (v.startswith("[") and v.endswith("]")) or (v.startswith("{") and v.endswith("}")):
            try:
                return json.loads(v)
            except Exception:
                return value
    return value
