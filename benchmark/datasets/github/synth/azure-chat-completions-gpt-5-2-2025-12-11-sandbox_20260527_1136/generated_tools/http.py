import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


DEFAULT_API_BASE_URL = "https://api.github.com"
DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


def _get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        accept: str = DEFAULT_ACCEPT,
        timeout_s: int = 60,
        user_agent: str = "mcp-github-rest/1.0",
    ):
        self.token = token or _get_env("GITHUB_TOKEN")
        self.base_url = (base_url or _get_env("GITHUB_API_BASE_URL") or DEFAULT_API_BASE_URL).rstrip("/")
        self.api_version = api_version
        self.accept = accept
        self.timeout_s = timeout_s
        self.user_agent = user_agent

    def _headers(self, accept: Optional[str] = None) -> Dict[str, str]:
        h = {
            "Accept": accept or self.accept,
            "X-GitHub-Api-Version": self.api_version,
            "User-Agent": self.user_agent,
        }
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

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
            return {"status": 204}

        # Handle rate limiting gently
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            reset = resp.headers.get("X-RateLimit-Reset")
            return {
                "error": "rate_limited",
                "status": resp.status_code,
                "rate_limit_reset": int(reset) if reset and reset.isdigit() else reset,
                "url": url,
            }

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

        return {
            "error": "github_api_error",
            "status": resp.status_code,
            "url": url,
            "response": data,
        }


def split_owner_repo(owner_repo: str) -> Tuple[str, str]:
    if not owner_repo or "/" not in owner_repo:
        raise ValueError("Expected 'owner/repo'")
    owner, repo = owner_repo.split("/", 1)
    if not owner or not repo:
        raise ValueError("Expected 'owner/repo'")
    return owner, repo
