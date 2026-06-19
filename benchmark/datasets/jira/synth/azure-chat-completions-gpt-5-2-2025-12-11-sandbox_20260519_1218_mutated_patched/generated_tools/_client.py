import os
import base64
from typing import Any, Dict, Optional

import requests


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

        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("ascii")
        self._headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
        }

    @property
    def api_root(self) -> str:
        return f"{self.base_url}/rest/api/3"

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
        url = f"{self.api_root}{path}"
        h = dict(self._headers)
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=h,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code == 204:
            return {"ok": True}

        content_type = resp.headers.get("Content-Type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = resp.json()
            except ValueError:
                body = resp.text
        else:
            body = resp.text

        if 200 <= resp.status_code < 300:
            return body

        return {
            "error": "Jira API error",
            "status": resp.status_code,
            "body": body,
        }
