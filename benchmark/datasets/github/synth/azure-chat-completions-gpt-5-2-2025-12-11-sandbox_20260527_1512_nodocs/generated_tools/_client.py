import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        user_agent: str = "mcp-github-rest",
        timeout: int = 30,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.user_agent = user_agent
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
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
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        expected: Tuple[int, ...] = (200, 201, 202, 204),
    ) -> Any:
        url = f"{self.base_url}{path}"
        h = self._headers()
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json,
                data=data,
                headers=h,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code == 204:
            return {"ok": True, "status": 204}

        # Handle rate limit politely
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            reset = resp.headers.get("X-RateLimit-Reset")
            return {
                "error": "rate_limited",
                "status": resp.status_code,
                "reset_epoch": int(reset) if reset and reset.isdigit() else None,
                "url": url,
            }

        content_type = resp.headers.get("Content-Type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = resp.json()
            except ValueError:
                body = resp.text
        else:
            body = resp.text

        if resp.status_code not in expected:
            msg = None
            if isinstance(body, dict):
                msg = body.get("message")
            return {
                "error": msg or "request_failed",
                "status": resp.status_code,
                "url": url,
                "body": body,
            }

        return body


def split_repo(repo: str) -> Tuple[str, str]:
    if not repo or "/" not in repo:
        raise ValueError("repo must be in 'owner/repo' format")
    owner, name = repo.split("/", 1)
    return owner, name
