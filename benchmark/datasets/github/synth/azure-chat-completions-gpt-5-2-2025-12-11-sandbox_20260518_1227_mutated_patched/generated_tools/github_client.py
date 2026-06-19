import os
import time
from typing import Any, Dict, Optional

import requests


DEFAULT_API_VERSION = "2026-03-10"


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
        accept: str = "application/vnd.github+json",
        extra_headers: Optional[Dict[str, str]] = None,
        retry: int = 2,
    ) -> Any:
        url = f"{self.base_url}{path}"
        headers = self._headers(accept=accept)
        if extra_headers:
            headers.update(extra_headers)

        for attempt in range(retry + 1):
            try:
                resp = requests.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=json,
                    timeout=self.timeout_s,
                )
            except requests.RequestException as e:
                if attempt >= retry:
                    return {"error": str(e)}
                time.sleep(0.5 * (attempt + 1))
                continue

            # Handle rate limiting / abuse detection with backoff
            if resp.status_code in (429, 403) and attempt < retry:
                retry_after = resp.headers.get("Retry-After")
                if retry_after:
                    try:
                        time.sleep(float(retry_after))
                        continue
                    except ValueError:
                        pass
                # Secondary rate limit often returns 403 with message
                time.sleep(1.0 * (attempt + 1))
                continue

            if 200 <= resp.status_code < 300:
                if resp.status_code == 204:
                    return {"ok": True}
                ctype = resp.headers.get("Content-Type", "")
                if "application/json" in ctype:
                    return resp.json()
                # Some endpoints return redirects or raw content
                return {
                    "status": resp.status_code,
                    "content_type": ctype,
                    "text": resp.text,
                    "headers": dict(resp.headers),
                }

            # Expected errors should be returned as dicts
            try:
                err_json = resp.json()
            except Exception:
                err_json = {"message": resp.text}
            return {
                "error": err_json.get("message") if isinstance(err_json, dict) else "Request failed",
                "status": resp.status_code,
                "details": err_json,
                "url": url,
            }

        return {"error": "Request failed"}
