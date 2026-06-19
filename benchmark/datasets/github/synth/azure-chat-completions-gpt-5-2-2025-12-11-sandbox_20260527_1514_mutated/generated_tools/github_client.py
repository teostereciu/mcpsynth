import os
import time
from typing import Any, Dict, Optional

import requests


DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        accept: str = DEFAULT_ACCEPT,
        user_agent: str = "mcp-github-rest/1.0",
        timeout_s: int = 60,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.api_version = api_version
        self.accept = accept
        self.user_agent = user_agent
        self.timeout_s = timeout_s

    def _headers(self, accept: Optional[str] = None) -> Dict[str, str]:
        headers = {
            "Accept": accept or self.accept,
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
        accept: Optional[str] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=self._headers(accept=accept),
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                timeout=self.timeout_s,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code == 204:
            return {"ok": True, "status": 204}

        # Try JSON first
        data: Any
        try:
            data = resp.json()
        except ValueError:
            data = resp.text

        if 200 <= resp.status_code < 300:
            return data

        # Expected errors should be returned, not raised
        err = {
            "error": True,
            "status": resp.status_code,
            "url": url,
            "response": data,
        }
        # Rate limit hints
        for h in ["X-RateLimit-Limit", "X-RateLimit-Remaining", "X-RateLimit-Reset"]:
            if h in resp.headers:
                err[h.lower()] = resp.headers[h]
        if "X-RateLimit-Reset" in resp.headers:
            try:
                err["rate_limit_reset_utc"] = time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime(int(resp.headers["X-RateLimit-Reset"]))
                )
            except Exception:
                pass
        return err
