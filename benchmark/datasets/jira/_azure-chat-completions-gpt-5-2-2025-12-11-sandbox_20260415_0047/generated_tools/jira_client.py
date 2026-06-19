"""Shared Jira REST API v3 client helpers.

Auth is via HTTP Basic (email + API token).
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests
from requests.auth import HTTPBasicAuth


class JiraClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout_s: int = 30,
    ) -> None:
        self.base_url = (base_url or os.environ.get("JIRA_BASE_URL", "")).rstrip("/")
        self.email = email or os.environ.get("JIRA_EMAIL", "")
        self.api_token = api_token or os.environ.get("JIRA_API_TOKEN", "")
        self.timeout_s = timeout_s

    def _auth(self) -> HTTPBasicAuth:
        if not self.email or not self.api_token:
            raise RuntimeError("Missing JIRA_EMAIL or JIRA_API_TOKEN")
        return HTTPBasicAuth(self.email, self.api_token)

    def _url(self, path: str) -> str:
        if not self.base_url:
            raise RuntimeError("Missing JIRA_BASE_URL")
        if not path.startswith("/"):
            path = "/" + path
        return f"{self.base_url}/rest/api/3{path}"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Any = None,
        files: Any = None,
    ) -> Any:
        h: Dict[str, str] = {"Accept": "application/json"}
        if headers:
            h.update(headers)
        if json is not None and "Content-Type" not in h:
            h["Content-Type"] = "application/json"

        resp = requests.request(
            method.upper(),
            self._url(path),
            auth=self._auth(),
            headers=h,
            params=params or {},
            json=json,
            data=data,
            files=files,
            timeout=self.timeout_s,
        )

        if resp.status_code == 204:
            return {"ok": True}

        content_type = resp.headers.get("Content-Type", "")
        try:
            body = resp.json() if "application/json" in content_type else resp.text
        except Exception:
            body = resp.text

        if resp.ok:
            return body

        # Jira error bodies often include: errorMessages, errors
        err: Dict[str, Any] = {
            "error": "Jira API request failed",
            "status": resp.status_code,
            "method": method.upper(),
            "path": path,
            "details": body,
        }
        return err


def adf_text(text: str) -> Dict[str, Any]:
    """Create a simple Atlassian Document Format (ADF) document with plain text."""

    return {
        "version": 1,
        "type": "doc",
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": text}]}
        ],
    }
