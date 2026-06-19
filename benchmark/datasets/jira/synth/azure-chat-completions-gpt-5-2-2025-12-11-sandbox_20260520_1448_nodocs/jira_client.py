import os
import base64
from typing import Any, Dict, Optional

import requests


class JiraClient:
    def __init__(self):
        base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        if not base_url:
            raise ValueError("JIRA_BASE_URL is required")
        self.base_url = base_url
        self.api_base = f"{self.base_url}/rest/api/3"

        email = os.environ.get("JIRA_EMAIL", "")
        token = os.environ.get("JIRA_API_TOKEN", "")
        if not email or not token:
            raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN are required")

        auth = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("ascii")
        self.headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
        data: Any = None,
    ) -> Any:
        url = f"{self.api_base}{path}"
        h = dict(self.headers)
        if headers:
            h.update(headers)
        try:
            resp = requests.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=h,
                files=files,
                data=data,
                timeout=60,
            )
        except Exception as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                return {"error": resp.json(), "status": resp.status_code}
            except Exception:
                return {"error": resp.text, "status": resp.status_code}

        if resp.status_code == 204:
            return {"ok": True}

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "status": resp.status_code, "text": resp.text}
        return resp.text
