import os
import requests
from typing import Any, Dict, Optional


class GitHubClient:
    def __init__(self, token: Optional[str] = None, base_url: Optional[str] = None):
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.token = token or os.getenv("GITHUB_TOKEN")

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(method, url, headers=self._headers(), params=params, json=json, timeout=60)
        except Exception as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": "GitHub API error", "status": resp.status_code, "details": data}

        if resp.status_code == 204:
            return {"ok": True}
        if resp.content is None or resp.content == b"":
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return resp.text
