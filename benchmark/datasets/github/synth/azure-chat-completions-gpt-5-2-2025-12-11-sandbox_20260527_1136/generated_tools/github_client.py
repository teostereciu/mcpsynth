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
        timeout: int = 30,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.api_version = api_version
        self.timeout = timeout

    def _headers(self, accept: Optional[str] = None) -> Dict[str, str]:
        headers = {
            "Accept": accept or DEFAULT_ACCEPT,
            "X-GitHub-Api-Version": self.api_version,
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
                method.upper(),
                url,
                headers=self._headers(accept=accept),
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code == 204:
            return {"status": 204}

        # Handle rate limiting politely
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            reset = resp.headers.get("X-RateLimit-Reset")
            return {
                "error": "rate_limited",
                "status": resp.status_code,
                "reset": int(reset) if reset and reset.isdigit() else reset,
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
            "message": (data.get("message") if isinstance(data, dict) else str(data))[:2000],
            "response": data,
        }


def split_owner_repo(owner_repo: Optional[str]) -> Dict[str, str]:
    if not owner_repo or "/" not in owner_repo:
        return {"error": "owner_repo must be in 'owner/repo' format"}
    owner, repo = owner_repo.split("/", 1)
    if not owner or not repo:
        return {"error": "owner_repo must be in 'owner/repo' format"}
    return {"owner": owner, "repo": repo}
