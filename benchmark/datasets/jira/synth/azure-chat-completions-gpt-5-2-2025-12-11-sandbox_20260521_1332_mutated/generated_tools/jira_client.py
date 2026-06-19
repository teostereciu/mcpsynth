import os
import json
from typing import Any, Dict, Optional, Union

import requests
from requests.auth import HTTPBasicAuth


class JiraClient:
    def __init__(self):
        base = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        if not base:
            raise RuntimeError("JIRA_BASE_URL is required")
        self.base_url = f"{base}/rest/api/3"
        email = os.environ.get("JIRA_EMAIL")
        token = os.environ.get("JIRA_API_TOKEN")
        if not email or not token:
            raise RuntimeError("JIRA_EMAIL and JIRA_API_TOKEN are required")
        self.auth = HTTPBasicAuth(email, token)
        self.session = requests.Session()
        self.session.auth = self.auth
        self.session.headers.update({"Accept": "application/json"})

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, Any], str, bytes]] = None,
        timeout: int = 60,
    ) -> Any:
        url = self.base_url + (path if path.startswith("/") else f"/{path}")
        req_headers = {}
        if headers:
            req_headers.update(headers)

        try:
            resp = self.session.request(
                method.upper(),
                url,
                params=params,
                json=json_body,
                headers=req_headers,
                files=files,
                data=data,
                timeout=timeout,
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
            except Exception:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return body

        return {
            "error": "Jira API error",
            "status": resp.status_code,
            "body": body,
        }


def adf_from_text(text: str) -> Dict[str, Any]:
    """Create a minimal Atlassian Document Format body from plain text."""
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": text}],
            }
        ],
    }
