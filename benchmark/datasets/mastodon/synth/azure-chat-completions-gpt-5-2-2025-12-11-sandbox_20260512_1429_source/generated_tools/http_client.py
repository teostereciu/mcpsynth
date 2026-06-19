import os
from typing import Any, Dict, Optional

import requests


class MastodonClient:
    def __init__(self, base_url: Optional[str] = None, access_token: Optional[str] = None, timeout: int = 30):
        self.base_url = (base_url or os.getenv("MASTODON_BASE_URL") or "").rstrip("/")
        self.access_token = access_token or os.getenv("MASTODON_ACCESS_TOKEN") or ""
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        data: Any = None,
        files: Any = None,
    ) -> Any:
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
            return {"error": f"Request failed: {e}"}

        try:
            data = resp.json() if resp.content else None
        except Exception:
            data = resp.text

        if resp.status_code >= 400:
            return {"error": f"HTTP {resp.status_code}", "details": data}
        return data
