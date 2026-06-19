import os
import time
from typing import Any, Dict, Optional, Tuple

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
        timeout: int = 60,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.api_version = api_version
        self.accept = accept
        self.user_agent = user_agent
        self.timeout = timeout

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
        data: Any = None,
        accept: Optional[str] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        allow_redirects: bool = True,
    ) -> Any:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        headers = self._headers(accept=accept)
        if extra_headers:
            headers.update(extra_headers)

        try:
            resp = requests.request(
                method.upper(),
                url,
                headers=headers,
                params=params,
                json=json,
                data=data,
                timeout=self.timeout,
                allow_redirects=allow_redirects,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        # Handle empty responses
        if resp.status_code == 204:
            return {"status": 204}

        # Try to parse JSON; fall back to text
        content_type = resp.headers.get("Content-Type", "")
        parsed: Any
        if "application/json" in content_type or content_type.endswith("+json"):
            try:
                parsed = resp.json()
            except ValueError:
                parsed = resp.text
        else:
            parsed = resp.text

        if 200 <= resp.status_code < 300:
            return parsed

        # Expected errors should be returned as dicts
        err: Dict[str, Any] = {
            "error": "GitHub API error",
            "status": resp.status_code,
            "url": url,
        }
        if isinstance(parsed, dict):
            err.update(parsed)
        else:
            err["message"] = parsed
        return err


def split_owner_repo(owner_repo: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
    if not owner_repo:
        return None, None
    if "/" not in owner_repo:
        return owner_repo, None
    owner, repo = owner_repo.split("/", 1)
    return owner, repo
