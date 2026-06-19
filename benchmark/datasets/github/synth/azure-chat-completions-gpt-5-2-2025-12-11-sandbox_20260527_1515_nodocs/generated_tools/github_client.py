import os
import time
from typing import Any, Dict, Optional

import requests


class GitHubClient:
    def __init__(self):
        self.base_url = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
        self.token = os.getenv("GITHUB_TOKEN", "").strip()

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: float = 30.0,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        h = self._headers()
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=h,
                params=params,
                json=json,
                data=data,
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e), "method": method, "url": url}

        # Handle rate limiting gently
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            reset = resp.headers.get("X-RateLimit-Reset")
            return {
                "error": "rate_limited",
                "status": resp.status_code,
                "reset": reset,
                "method": method,
                "url": url,
                "body": self._safe_json(resp),
            }

        if resp.status_code >= 400:
            return {
                "error": "http_error",
                "status": resp.status_code,
                "method": method,
                "url": url,
                "body": self._safe_json(resp),
            }

        # 204 No Content
        if resp.status_code == 204:
            return {"ok": True, "status": 204}

        return self._safe_json(resp)

    @staticmethod
    def _safe_json(resp: requests.Response) -> Dict[str, Any]:
        try:
            return resp.json()
        except ValueError:
            return {"raw": resp.text, "status": resp.status_code}
