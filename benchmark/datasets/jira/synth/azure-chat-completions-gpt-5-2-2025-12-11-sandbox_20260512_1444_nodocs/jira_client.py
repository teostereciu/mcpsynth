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
        timeout: int = 30,
    ):
        self.base_url = (base_url or os.environ.get("JIRA_BASE_URL", "")).rstrip("/")
        self.email = email or os.environ.get("JIRA_EMAIL", "")
        self.api_token = api_token or os.environ.get("JIRA_API_TOKEN", "")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError("JIRA_BASE_URL is required")
        if not self.email:
            raise ValueError("JIRA_EMAIL is required")
        if not self.api_token:
            raise ValueError("JIRA_API_TOKEN is required")

        self.api_root = f"{self.base_url}/rest/api/3"

    def _headers(self) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("utf-8")
        return {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        files: Any = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        url = f"{self.api_root}{path}"
        h = self._headers()
        if headers:
            h.update(headers)
        try:
            resp = requests.request(
                method=method,
                url=url,
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

        if resp.status_code >= 400:
            return {
                "error": "Jira API error",
                "status": resp.status_code,
                "body": body,
            }
        return body
