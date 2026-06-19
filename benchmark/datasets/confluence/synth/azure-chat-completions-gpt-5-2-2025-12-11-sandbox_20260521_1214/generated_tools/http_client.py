import base64
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


@dataclass
class ConfluenceClient:
    base_url: str
    email: str
    api_token: str

    @staticmethod
    def from_env() -> "ConfluenceClient":
        base_url = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
        email = os.environ.get("JIRA_EMAIL", "")
        api_token = os.environ.get("JIRA_API_TOKEN", "")
        return ConfluenceClient(base_url=base_url, email=email, api_token=api_token)

    def _headers(self, accept: str = "application/json", content_type: Optional[str] = None) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("ascii")
        headers = {
            "Authorization": f"Basic {token}",
            "Accept": accept,
        }
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        data: Any = None,
        files: Any = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: int = 60,
    ) -> Any:
        if not self.base_url:
            return {"error": "CONFLUENCE_BASE_URL is not set"}
        if not self.email or not self.api_token:
            return {"error": "JIRA_EMAIL and/or JIRA_API_TOKEN not set"}

        url = f"{self.base_url}{path}"
        headers = self._headers(accept=accept, content_type=content_type)
        if extra_headers:
            headers.update(extra_headers)

        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_body,
                data=data,
                files=files,
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            # Try to parse JSON error
            try:
                err = resp.json()
            except Exception:
                err = resp.text
            return {"error": "HTTP error", "status": resp.status_code, "details": err}

        if resp.status_code == 204:
            return {"ok": True}

        if accept != "application/json":
            return resp.text

        if not resp.content:
            return {"ok": True}

        try:
            return resp.json()
        except json.JSONDecodeError:
            return resp.text
