import os
import requests
from requests.auth import HTTPBasicAuth


class ZulipClient:
    def __init__(self, site: str | None = None, email: str | None = None, api_key: str | None = None, timeout: float = 30.0):
        self.site = (site or os.environ.get("ZULIP_SITE") or "").rstrip("/")
        self.email = email or os.environ.get("ZULIP_EMAIL")
        self.api_key = api_key or os.environ.get("ZULIP_API_KEY")
        self.timeout = timeout

        if not self.site:
            raise ValueError("ZULIP_SITE is required")
        if not self.email or not self.api_key:
            raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY are required")

        self.base_url = f"{self.site}/api/v1"
        self._auth = HTTPBasicAuth(self.email, self.api_key)

    def request(self, method: str, path: str, *, params=None, data=None, json=None, files=None):
        url = self.base_url + path
        try:
            resp = requests.request(
                method=method,
                url=url,
                auth=self._auth,
                params=params,
                data=data,
                json=json,
                files=files,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("content-type", "")
        parsed = None
        if "application/json" in content_type:
            try:
                parsed = resp.json()
            except Exception:
                parsed = None

        if resp.status_code >= 400:
            if isinstance(parsed, dict):
                parsed.setdefault("http_status", resp.status_code)
                return parsed
            return {"error": resp.text or "HTTP error", "http_status": resp.status_code}

        return parsed if parsed is not None else {"result": resp.text}
