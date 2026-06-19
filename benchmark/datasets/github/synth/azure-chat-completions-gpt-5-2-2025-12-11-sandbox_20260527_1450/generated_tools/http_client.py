import os
import time
from typing import Any, Dict, Optional

import requests


DEFAULT_API_VERSION = "2026-03-10"


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
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.api_version = api_version
        self.user_agent = user_agent
        self.timeout_s = timeout_s

    def _headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        headers = {
            "Accept": accept,
            "X-GitHub-Api-Version": self.api_version,
            "User-Agent": self.user_agent,
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
        accept: str = "application/vnd.github+json",
    ) -> Any:
        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method,
                url,
                headers=self._headers(accept=accept),
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                timeout=self.timeout_s,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code == 204:
            return {"ok": True, "status": 204}

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except ValueError:
                data = resp.text
        else:
            data = resp.text

        if 200 <= resp.status_code < 300:
            return data

        # Expected errors should be returned as dicts
        return {
            "error": "GitHub API error",
            "status": resp.status_code,
            "url": url,
            "response": data,
        }
