import os
import time
from typing import Any, Dict, Optional

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
        timeout_s: int = 60,
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
        raw: bool = False,
        paginate: bool = False,
    ) -> Any:
        url = f"{self.base_url}{path if path.startswith('/') else '/' + path}"
        try:
            if paginate and method.upper() == "GET":
                return self._paginate(url, params=params, headers=headers)

            resp = requests.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json,
                data=data,
                headers=self._headers(headers),
                timeout=self.timeout_s,
            )
            return self._handle_response(resp, raw=raw)
        except requests.RequestException as e:
            return {"error": str(e)}

    def _handle_response(self, resp: requests.Response, *, raw: bool = False) -> Any:
        if resp.status_code >= 400:
            try:
                payload = resp.json()
            except Exception:
                payload = {"message": resp.text}
            return {
                "error": payload.get("message") if isinstance(payload, dict) else "HTTP error",
                "status": resp.status_code,
                "response": payload,
            }

        if raw:
            return {
                "status": resp.status_code,
                "headers": dict(resp.headers),
                "body": resp.text,
            }

        if resp.status_code == 204:
            return {"status": 204}

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.text

    def _paginate(self, url: str, *, params: Optional[Dict[str, Any]], headers: Optional[Dict[str, str]]) -> Any:
        items = []
        page = 1
        per_page = None
        if params:
            per_page = params.get("per_page")
        while True:
            p = dict(params or {})
            p.setdefault("page", page)
            if per_page is not None:
                p.setdefault("per_page", per_page)
            resp = requests.get(url, params=p, headers=self._headers(headers), timeout=self.timeout_s)
            data = self._handle_response(resp)
            if isinstance(data, dict) and data.get("error"):
                return data
            if not isinstance(data, list):
                return data
            items.extend(data)
            link = resp.headers.get("Link", "")
            if 'rel="next"' not in link:
                break
            page += 1
            time.sleep(0.1)
        return items
