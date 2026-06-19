import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_BASE_URL = "https://api.github.com"


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        user_agent: str = "mcp-github-rest/1.0",
        timeout_s: int = 30,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.api_version = api_version
        self.user_agent = user_agent
        self.timeout_s = timeout_s

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
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
        allow_redirects: bool = True,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        try:
            resp = requests.request(
                method.upper(),
                url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                data=data,
                headers=self._headers(headers),
                timeout=self.timeout_s,
                allow_redirects=allow_redirects,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        # Handle rate limit secondary throttling politely if present
        if resp.status_code == 403 and resp.headers.get("Retry-After"):
            try:
                time.sleep(min(5, int(resp.headers["Retry-After"])))
            except Exception:
                pass

        content_type = resp.headers.get("Content-Type", "")
        parsed: Any
        if "application/json" in content_type:
            try:
                parsed = resp.json()
            except Exception:
                parsed = resp.text
        else:
            parsed = resp.text

        if 200 <= resp.status_code < 300:
            return {
                "ok": True,
                "status": resp.status_code,
                "url": url,
                "headers": {k: v for k, v in resp.headers.items()},
                "data": parsed,
            }

        return {
            "ok": False,
            "status": resp.status_code,
            "url": url,
            "headers": {k: v for k, v in resp.headers.items()},
            "error": parsed,
        }


def parse_owner_repo(owner_repo: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
    if not owner_repo:
        return None, None
    if "/" not in owner_repo:
        return owner_repo, None
    owner, repo = owner_repo.split("/", 1)
    return owner or None, repo or None
