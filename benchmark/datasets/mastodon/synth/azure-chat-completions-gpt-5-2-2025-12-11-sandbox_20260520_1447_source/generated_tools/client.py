import os
import requests
from typing import Any, Dict, Optional


class MastodonClient:
    def __init__(self, base_url: Optional[str] = None, access_token: Optional[str] = None, timeout: int = 30):
        self.base_url = (base_url or os.getenv("MASTODON_BASE_URL") or "").rstrip("/")
        self.access_token = access_token or os.getenv("MASTODON_ACCESS_TOKEN")
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None,
                json: Optional[Dict[str, Any]] = None, data: Any = None, files: Any = None) -> Any:
        if not self.base_url:
            return {"error": "MASTODON_BASE_URL is not set"}
        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method,
                url,
                headers=self._headers(),
                params=params,
                json=json,
                data=data,
                files=files,
                timeout=self.timeout,
            )
        except Exception as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                err = resp.json()
            except Exception:
                err = resp.text
            return {"error": "HTTP error", "status_code": resp.status_code, "details": err}

        if resp.status_code == 204:
            return {"ok": True}

        try:
            return resp.json()
        except Exception:
            return resp.text
