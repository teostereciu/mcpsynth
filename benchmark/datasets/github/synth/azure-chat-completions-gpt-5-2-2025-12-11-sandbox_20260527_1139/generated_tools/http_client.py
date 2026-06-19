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
        allow_redirects: bool = True,
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
                allow_redirects=allow_redirects,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code == 204:
            return {"status": 204}

        # Some endpoints return redirects for downloads; keep JSON for others.
        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = {"message": resp.text}
            return {"error": data, "status": resp.status_code, "url": url}

        if "application/json" in content_type or content_type.endswith("+json"):
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "status": resp.status_code, "url": url, "text": resp.text}

        return {
            "status": resp.status_code,
            "content_type": content_type,
            "text": resp.text,
        }
