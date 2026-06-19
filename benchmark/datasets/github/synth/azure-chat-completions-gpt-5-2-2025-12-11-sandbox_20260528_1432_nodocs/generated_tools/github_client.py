import os
import time
from typing import Any, Dict, Optional

import requests


class GitHubClient:
    def __init__(self, token: Optional[str] = None, base_url: Optional[str] = None, user_agent: str = "mcp-github-rest"):
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.user_agent = user_agent

    def _headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        headers = {
            "Accept": accept,
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
        api_version: Optional[str] = "2022-11-28",
        timeout: float = 30.0,
    ) -> Any:
        url = f"{self.base_url}{path}"
        headers = self._headers(accept=accept)
        if api_version:
            headers["X-GitHub-Api-Version"] = api_version

        try:
            resp = requests.request(method, url, headers=headers, params=params, json=json, timeout=timeout)
        except requests.RequestException as e:
            return {"error": str(e)}

        # Handle rate limit hints
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            reset = resp.headers.get("X-RateLimit-Reset")
            return {
                "error": "rate_limited",
                "status": resp.status_code,
                "reset_epoch": int(reset) if reset and reset.isdigit() else None,
                "message": self._safe_json(resp).get("message") if resp.content else None,
            }

        if resp.status_code >= 400:
            body = self._safe_json(resp)
            return {
                "error": body.get("message") if isinstance(body, dict) else "request_failed",
                "status": resp.status_code,
                "details": body,
            }

        if resp.status_code == 204:
            return {"ok": True}

        # Some endpoints return empty body with 201/202
        if not resp.content:
            return {"ok": True, "status": resp.status_code}

        return self._safe_json(resp)

    @staticmethod
    def _safe_json(resp: requests.Response) -> Any:
        try:
            return resp.json()
        except ValueError:
            return {"raw": resp.text}


def get_default_repo() -> Optional[Dict[str, str]]:
    v = os.getenv("GITHUB_TEST_REPO")
    if not v or "/" not in v:
        return None
    owner, repo = v.split("/", 1)
    return {"owner": owner, "repo": repo}
