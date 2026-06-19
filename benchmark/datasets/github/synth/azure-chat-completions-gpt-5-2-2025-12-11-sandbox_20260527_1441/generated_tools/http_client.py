import os
import requests
from typing import Any, Dict, Optional


DEFAULT_API_VERSION = "2026-03-10"


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

    def _headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        headers = {
            "Accept": accept,
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
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": "GitHub API error", "status": resp.status_code, "details": data}

        if resp.status_code == 204:
            return {"ok": True}

        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "status": resp.status_code, "details": resp.text}
        return resp.text
