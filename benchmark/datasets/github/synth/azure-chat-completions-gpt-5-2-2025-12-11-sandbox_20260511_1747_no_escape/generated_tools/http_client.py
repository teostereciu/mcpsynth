import os
import time
from typing import Any, Dict, Optional, Tuple, Union

import requests


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: str = "2026-03-10",
        user_agent: str = "mcp-github-rest/1.0",
        timeout: int = 60,
    ):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = (base_url or os.getenv("GITHUB_API_BASE_URL") or "https://api.github.com").rstrip("/")
        self.api_version = api_version
        self.user_agent = user_agent
        self.timeout = timeout

    def _headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        headers = {
            "Accept": accept,
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
        accept: str = "application/vnd.github+json",
        extra_headers: Optional[Dict[str, str]] = None,
        allow_redirects: bool = True,
        retry: int = 2,
    ) -> Union[Dict[str, Any], list, str]:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        headers = self._headers(accept=accept)
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[Dict[str, Any]] = None
        for attempt in range(retry + 1):
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
                last_err = {"error": str(e), "url": url, "method": method}
                if attempt < retry:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return last_err

            if resp.status_code == 204:
                return {"status": 204}

            content_type = resp.headers.get("Content-Type", "")
            try:
                if "application/json" in content_type or content_type.endswith("+json"):
                    payload = resp.json()
                else:
                    payload = resp.text
            except ValueError:
                payload = resp.text

            if 200 <= resp.status_code < 300:
                return payload

            err = {
                "error": "GitHub API error",
                "status": resp.status_code,
                "url": url,
                "method": method.upper(),
                "response": payload,
            }

            # Basic retry for secondary rate limits / transient errors
            if resp.status_code in (429, 500, 502, 503, 504) and attempt < retry:
                time.sleep(0.75 * (attempt + 1))
                last_err = err
                continue

            return err

        return last_err or {"error": "Unknown error"}


def parse_owner_repo(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Tuple[str, str]:
    if owner_repo and (not owner or not repo):
        if "/" not in owner_repo:
            raise ValueError("owner_repo must be in 'owner/repo' format")
        o, r = owner_repo.split("/", 1)
        return o, r
    if not owner or not repo:
        test_repo = os.getenv("GITHUB_TEST_REPO")
        if test_repo and "/" in test_repo:
            o, r = test_repo.split("/", 1)
            return o, r
        raise ValueError("owner and repo are required (or set GITHUB_TEST_REPO)")
    return owner, repo
