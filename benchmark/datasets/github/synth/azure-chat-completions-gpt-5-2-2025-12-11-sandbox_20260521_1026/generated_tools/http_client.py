import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


DEFAULT_API_BASE_URL = "https://api.github.com"
DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        accept: str = DEFAULT_ACCEPT,
        timeout_s: int = 60,
    ):
        self.token = token or _env("GITHUB_TOKEN")
        self.base_url = (base_url or _env("GITHUB_API_BASE_URL", DEFAULT_API_BASE_URL)).rstrip("/")
        self.api_version = api_version
        self.accept = accept
        self.timeout_s = timeout_s

    def _headers(self, accept: Optional[str] = None) -> Dict[str, str]:
        headers = {
            "Accept": accept or self.accept,
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
        extra_headers: Optional[Dict[str, str]] = None,
        retry: int = 2,
    ) -> Tuple[int, Any, Dict[str, str]]:
        url = f"{self.base_url}{path}"
        headers = self._headers(accept=accept)
        if extra_headers:
            headers.update(extra_headers)

        last_exc: Optional[Exception] = None
        for attempt in range(retry + 1):
            try:
                resp = requests.request(
                    method,
                    url,
                    headers=headers,
                    params=params,
                    json=json,
                    timeout=self.timeout_s,
                )
                content_type = resp.headers.get("Content-Type", "")
                if resp.status_code == 204:
                    data: Any = None
                elif "application/json" in content_type:
                    data = resp.json()
                else:
                    data = resp.text

                if resp.status_code in (429, 500, 502, 503, 504) and attempt < retry:
                    time.sleep(0.5 * (2**attempt))
                    continue

                return resp.status_code, data, dict(resp.headers)
            except Exception as e:
                last_exc = e
                if attempt < retry:
                    time.sleep(0.5 * (2**attempt))
                    continue
                raise
        raise last_exc  # pragma: no cover


def ok_or_error(status: int, data: Any, headers: Optional[Dict[str, str]] = None) -> Any:
    if 200 <= status <= 299:
        return data
    msg = None
    if isinstance(data, dict):
        msg = data.get("message") or data.get("error")
    return {
        "error": msg or "GitHub API error",
        "status": status,
        "details": data,
        "headers": headers or {},
    }
