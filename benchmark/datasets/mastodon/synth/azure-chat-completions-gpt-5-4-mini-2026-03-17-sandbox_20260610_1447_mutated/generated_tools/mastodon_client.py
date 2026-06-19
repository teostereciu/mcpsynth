import os
from typing import Any, Dict, Optional

import httpx


class MastodonClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("MASTODON_BASE_URL", "").rstrip("/")
        self.access_token = os.getenv("MASTODON_ACCESS_TOKEN")
        if not self.base_url:
            raise ValueError("MASTODON_BASE_URL is required")

    def _headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}/api/v1{path}"
        with httpx.Client(timeout=60.0, headers=self._headers()) as client:
            resp = client.request(method, url, params=params, data=data, files=files)
            resp.raise_for_status()
            if resp.status_code == 204:
                return {}
            return resp.json()
