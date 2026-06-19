import base64
import json
import os
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
        self.base_url = (base_url or os.environ.get("JIRA_BASE_URL") or "").rstrip("/")
        self.email = email or os.environ.get("JIRA_EMAIL")
        self.api_token = api_token or os.environ.get("JIRA_API_TOKEN")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError("JIRA_BASE_URL is required")
        if not self.email or not self.api_token:
            raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN are required")

        self.api_root = f"{self.base_url}/rest/api/3"

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("ascii")
        headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
    ) -> Any:
        url = f"{self.api_root}{path}"
        h = self._headers(headers)
        if json_body is not None:
            h.setdefault("Content-Type", "application/json")
        try:
            resp = requests.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                data=data,
                headers=h,
                files=files,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            try:
                err = resp.json() if "application/json" in content_type else resp.text
            except Exception:
                err = resp.text
            return {"error": "Jira API error", "status": resp.status_code, "details": err}

        if resp.status_code == 204:
            return {"ok": True}

        if "application/json" in content_type:
            try:
                return resp.json()
            except json.JSONDecodeError:
                return {"ok": True, "raw": resp.text}
        return {"ok": True, "raw": resp.text}
