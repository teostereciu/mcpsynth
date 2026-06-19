import os
import json
from typing import Any, Dict, Optional, Tuple

import requests


class MastodonClient:
    def __init__(self, base_url: Optional[str] = None, access_token: Optional[str] = None, timeout: int = 30):
        self.base_url = (base_url or os.getenv("MASTODON_BASE_URL") or "").rstrip("/")
        self.access_token = access_token or os.getenv("MASTODON_ACCESS_TOKEN")
        self.timeout = timeout

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {"Accept": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        if extra:
            headers.update({k: v for k, v in extra.items() if v is not None})
        return headers

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Tuple[Optional[Any], Dict[str, Any]]:
        if not self.base_url:
            return None, {"error": "MASTODON_BASE_URL is not set"}

        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                data=data,
                files=files,
                headers=self._headers(headers),
                timeout=self.timeout,
            )
        except Exception as e:
            return None, {"error": str(e)}

        meta: Dict[str, Any] = {
            "status_code": resp.status_code,
            "headers": {k: v for k, v in resp.headers.items()},
        }

        if resp.status_code >= 400:
            try:
                meta["body"] = resp.json()
            except Exception:
                meta["body"] = resp.text
            meta["error"] = f"HTTP {resp.status_code}"
            return None, meta

        if resp.status_code == 204 or not resp.content:
            return {}, meta

        try:
            return resp.json(), meta
        except Exception:
            return resp.text, meta


def compact_params(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}
