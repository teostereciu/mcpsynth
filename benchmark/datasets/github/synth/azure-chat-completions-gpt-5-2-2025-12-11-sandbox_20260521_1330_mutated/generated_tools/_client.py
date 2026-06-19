import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


DEFAULT_API_BASE_URL = "https://api.github.com"
DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        user_agent: str = "mcp-github-rest/1.0",
        timeout_s: int = 60,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or DEFAULT_API_BASE_URL).rstrip("/")
        self.api_version = api_version
        self.user_agent = user_agent
        self.timeout_s = timeout_s

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Accept": DEFAULT_ACCEPT,
            "X-GitHub-Api-Version": self.api_version,
            "User-Agent": self.user_agent,
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if extra:
            headers.update({k: v for k, v in extra.items() if v is not None})
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
        expected: Tuple[int, ...] = (200, 201, 202, 204),
    ) -> Any:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                data=data,
                headers=self._headers(headers),
                timeout=self.timeout_s,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        # Handle rate limit secondary throttling politely if present
        if resp.status_code == 403 and resp.headers.get("Retry-After"):
            try:
                time.sleep(min(int(resp.headers["Retry-After"]), 5))
            except Exception:
                pass

        if resp.status_code not in expected:
            try:
                payload = resp.json()
            except Exception:
                payload = resp.text
            return {
                "error": "GitHub API request failed",
                "status": resp.status_code,
                "url": url,
                "response": payload,
            }

        if resp.status_code == 204:
            return {"ok": True}
        if resp.content is None or resp.content == b"":
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return resp.text


_client_singleton: Optional[GitHubClient] = None


def get_client() -> GitHubClient:
    global _client_singleton
    if _client_singleton is None:
        _client_singleton = GitHubClient()
    return _client_singleton
