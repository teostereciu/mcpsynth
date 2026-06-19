import os
import time
from typing import Any, Dict, Optional

import requests


DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


class GitHubClient:
    def __init__(self, token: Optional[str] = None, base_url: Optional[str] = None):
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.token = token or os.getenv("GITHUB_TOKEN")

    def _headers(self, accept: Optional[str] = None, api_version: str = DEFAULT_API_VERSION) -> Dict[str, str]:
        headers = {
            "Accept": accept or DEFAULT_ACCEPT,
            "X-GitHub-Api-Version": api_version,
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
        accept: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        timeout: int = 60,
    ) -> Any:
        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method,
                url,
                headers=self._headers(accept=accept, api_version=api_version),
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        # Handle rate limit secondary errors gracefully
        if resp.status_code == 403 and resp.headers.get("Retry-After"):
            return {
                "error": "rate_limited",
                "status": resp.status_code,
                "retry_after": resp.headers.get("Retry-After"),
                "url": url,
                "body": _safe_json(resp),
            }

        if resp.status_code >= 400:
            return {
                "error": "github_api_error",
                "status": resp.status_code,
                "url": url,
                "body": _safe_json(resp),
            }

        if resp.status_code == 204:
            return {"ok": True}

        return _safe_json(resp)


def _safe_json(resp: requests.Response) -> Any:
    try:
        if resp.text is None or resp.text == "":
            return None
        return resp.json()
    except ValueError:
        return resp.text
