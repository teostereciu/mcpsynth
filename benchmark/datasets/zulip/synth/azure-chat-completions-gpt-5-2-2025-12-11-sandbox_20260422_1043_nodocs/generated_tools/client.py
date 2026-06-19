import os
import requests
from typing import Any, Dict, Optional


class ZulipClient:
    def __init__(
        self,
        site: Optional[str] = None,
        email: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self.site = (site or os.getenv("ZULIP_SITE") or "").rstrip("/")
        self.email = email or os.getenv("ZULIP_EMAIL")
        self.api_key = api_key or os.getenv("ZULIP_API_KEY")
        self.timeout = timeout

    def _base_url(self) -> str:
        if not self.site:
            raise ValueError("ZULIP_SITE is not set")
        return f"{self.site}/api/v1"

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        files: Any = None,
    ) -> Dict[str, Any]:
        if not self.email or not self.api_key:
            return {"error": "Missing auth: set ZULIP_EMAIL and ZULIP_API_KEY"}
        try:
            url = self._base_url() + path
        except Exception as e:
            return {"error": str(e)}

        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                auth=(self.email, self.api_key),
                params=params,
                data=data,
                json=json,
                files=files,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

        content_type = resp.headers.get("content-type", "")
        try:
            if "application/json" in content_type:
                payload = resp.json()
            else:
                payload = {"raw": resp.text}
        except Exception:
            payload = {"raw": resp.text}

        if resp.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("http_status", resp.status_code)
                payload.setdefault("error", payload.get("msg") or payload.get("message") or resp.reason)
                return payload
            return {"http_status": resp.status_code, "error": resp.reason, "raw": resp.text}

        if isinstance(payload, dict):
            payload.setdefault("http_status", resp.status_code)
        return payload
