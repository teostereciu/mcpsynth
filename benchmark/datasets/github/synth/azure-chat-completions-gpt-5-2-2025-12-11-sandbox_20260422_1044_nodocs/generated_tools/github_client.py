import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


DEFAULT_BASE_URL = "https://api.github.com"
DEFAULT_ACCEPT = "application/vnd.github+json"
DEFAULT_API_VERSION = "2022-11-28"


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout_s: int = 30,
        user_agent: str = "mcp-github-rest/1.0",
    ):
        self.token = token or _env("GITHUB_TOKEN")
        self.base_url = (base_url or _env("GITHUB_API_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout_s = timeout_s
        self.user_agent = user_agent

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Accept": DEFAULT_ACCEPT,
            "X-GitHub-Api-Version": DEFAULT_API_VERSION,
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
        raw: bool = False,
        allow_redirects: bool = True,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        try:
            resp = requests.request(
                method.upper(),
                url,
                params=params,
                json=json,
                data=data,
                headers=self._headers(headers),
                timeout=self.timeout_s,
                allow_redirects=allow_redirects,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        # Handle rate limit hints
        rate = {
            "limit": resp.headers.get("X-RateLimit-Limit"),
            "remaining": resp.headers.get("X-RateLimit-Remaining"),
            "reset": resp.headers.get("X-RateLimit-Reset"),
        }

        if raw:
            body: Any = resp.text
        else:
            if resp.status_code == 204:
                body = None
            else:
                ctype = resp.headers.get("Content-Type", "")
                if "application/json" in ctype:
                    try:
                        body = resp.json()
                    except ValueError:
                        body = resp.text
                else:
                    body = resp.text

        if 200 <= resp.status_code < 300:
            return {"ok": True, "status": resp.status_code, "data": body, "rate": rate}

        # Expected errors should not raise
        msg = None
        if isinstance(body, dict):
            msg = body.get("message")
        return {
            "ok": False,
            "status": resp.status_code,
            "error": msg or resp.reason or "Request failed",
            "data": body,
            "url": url,
            "rate": rate,
        }

    def paginate(
        self,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        per_page: int = 100,
        max_pages: int = 10,
    ) -> Dict[str, Any]:
        params = dict(params or {})
        params.setdefault("per_page", per_page)
        items = []
        page = 1
        last_resp: Optional[Dict[str, Any]] = None
        while page <= max_pages:
            params["page"] = page
            r = self.request("GET", path, params=params)
            last_resp = r
            if not r.get("ok"):
                return r
            data = r.get("data")
            if isinstance(data, list):
                items.extend(data)
                if len(data) < per_page:
                    break
            else:
                # Not a list; return as-is
                return r
            page += 1
            time.sleep(0.0)
        return {"ok": True, "status": 200, "data": items, "pages": page - 1, "rate": (last_resp or {}).get("rate")}


def parse_owner_repo(owner_repo: str) -> Tuple[str, str]:
    if not owner_repo or "/" not in owner_repo:
        raise ValueError("owner_repo must be in 'owner/repo' format")
    owner, repo = owner_repo.split("/", 1)
    if not owner or not repo:
        raise ValueError("owner_repo must be in 'owner/repo' format")
    return owner, repo
