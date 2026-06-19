import os
import requests
from requests.auth import HTTPBasicAuth


class ZulipClient:
    def __init__(self, site: str | None = None, email: str | None = None, api_key: str | None = None, timeout: float = 30.0):
        self.site = (site or os.getenv("ZULIP_SITE") or "").rstrip("/")
        self.email = email or os.getenv("ZULIP_EMAIL")
        self.api_key = api_key or os.getenv("ZULIP_API_KEY")
        self.timeout = timeout

    def _base_url(self) -> str:
        if not self.site:
            raise ValueError("ZULIP_SITE is not set")
        return f"{self.site}/api/v1"

    def request(self, method: str, path: str, params: dict | None = None, data: dict | None = None, json: dict | None = None, files=None):
        if not self.email or not self.api_key:
            return {"error": "ZULIP_EMAIL/ZULIP_API_KEY not set"}
        url = self._base_url() + path
        try:
            resp = requests.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                files=files,
                auth=HTTPBasicAuth(self.email, self.api_key),
                timeout=self.timeout,
            )
        except Exception as e:
            return {"error": str(e)}

        try:
            payload = resp.json()
        except Exception:
            payload = {"raw": resp.text}

        if resp.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("http_status", resp.status_code)
            return {"error": "HTTP error", "http_status": resp.status_code, "response": payload}
        return payload
