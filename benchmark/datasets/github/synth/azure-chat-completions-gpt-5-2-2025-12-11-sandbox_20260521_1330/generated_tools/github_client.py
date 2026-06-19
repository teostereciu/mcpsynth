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
        user_agent: str = "mcp-github-rest/1.0",
        timeout_s: int = 60,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.api_version = api_version
        self.user_agent = user_agent
        self.timeout_s = timeout_s

    def _headers(self, accept: Optional[str] = None) -> Dict[str, str]:
        headers = {
            "Accept": accept or DEFAULT_ACCEPT,
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
        allow_redirects: bool = True,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        try:
            resp = requests.request(
                method.upper(),
                url,
                headers=self._headers(accept=accept),
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                timeout=self.timeout_s,
                allow_redirects=allow_redirects,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        # Handle rate limit info if present
        rate = {
            "limit": resp.headers.get("X-RateLimit-Limit"),
            "remaining": resp.headers.get("X-RateLimit-Remaining"),
            "reset": resp.headers.get("X-RateLimit-Reset"),
        }

        if resp.status_code == 204:
            return {"status": 204, "ok": True, "rate": rate}

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type or content_type.endswith("+json"):
            try:
                data = resp.json()
            except ValueError:
                data = resp.text
        else:
            data = resp.text

        if 200 <= resp.status_code < 300:
            return {"status": resp.status_code, "ok": True, "data": data, "rate": rate}

        # Expected errors should be returned, not raised
        err = {
            "status": resp.status_code,
            "ok": False,
            "error": data,
            "url": url,
            "rate": rate,
        }
        return err


def parse_owner_repo(owner_repo: Optional[str]) -> Tuple[Optional[str], Optional[str], Optional[Dict[str, str]]]:
    if not owner_repo:
        owner_repo = os.getenv("GITHUB_TEST_REPO")
    if not owner_repo or "/" not in owner_repo:
        return None, None, {"error": "owner_repo must be provided as 'owner/repo' (or set GITHUB_TEST_REPO)"}
    owner, repo = owner_repo.split("/", 1)
    return owner, repo, None
