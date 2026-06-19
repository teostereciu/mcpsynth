import os
import json
from typing import Any, Dict, Optional

import requests
from requests.auth import HTTPBasicAuth


class JiraClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 60,
    ):
        self.base_url = (base_url or os.getenv("JIRA_BASE_URL") or "").rstrip("/")
        self.email = email or os.getenv("JIRA_EMAIL")
        self.api_token = api_token or os.getenv("JIRA_API_TOKEN")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError("JIRA_BASE_URL is required")
        if not self.email or not self.api_token:
            raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN are required")

        self.api_root = f"{self.base_url}/rest/api/3"
        self._session = requests.Session()
        self._session.auth = HTTPBasicAuth(self.email, self.api_token)
        self._session.headers.update({"Accept": "application/json"})

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
        data: Any = None,
        allow_redirects: bool = True,
    ) -> Any:
        url = self.api_root + (path if path.startswith("/") else f"/{path}")
        req_headers = dict(self._session.headers)
        if headers:
            req_headers.update(headers)

        try:
            resp = self._session.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                headers=req_headers,
                files=files,
                data=data,
                timeout=self.timeout,
                allow_redirects=allow_redirects,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            # Jira often returns JSON error bodies
            try:
                err = resp.json()
            except Exception:
                err = resp.text
            return {"error": "HTTP error", "status": resp.status_code, "details": err}

        if resp.status_code == 204:
            return {"ok": True}

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "status": resp.status_code, "text": resp.text}

        return resp.text


_client: Optional[JiraClient] = None


def get_client() -> JiraClient:
    global _client
    if _client is None:
        _client = JiraClient()
    return _client
