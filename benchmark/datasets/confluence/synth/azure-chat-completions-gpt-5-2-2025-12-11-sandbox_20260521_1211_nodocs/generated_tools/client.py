import base64
import os
from typing import Any, Dict, Optional

import requests


class ConfluenceClient:
    def __init__(self):
        self.base_url = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.api_token = os.environ.get("JIRA_API_TOKEN", "")
        self.default_space_key = os.environ.get("CONFLUENCE_SPACE_KEY", "")

        if not self.base_url:
            raise ValueError("CONFLUENCE_BASE_URL is required")

        self.session = requests.Session()
        auth = f"{self.email}:{self.api_token}".encode("utf-8")
        self.session.headers.update(
            {
                "Authorization": "Basic " + base64.b64encode(auth).decode("ascii"),
                "Accept": "application/json",
            }
        )

    def _url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return self.base_url + path

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
        data: Any = None,
        expected: tuple = (200, 201, 202, 204),
    ) -> Any:
        try:
            resp = self.session.request(
                method,
                self._url(path),
                params=params,
                json=json,
                headers=headers,
                files=files,
                data=data,
                timeout=60,
            )
        except Exception as e:
            return {"error": str(e)}

        if resp.status_code not in expected:
            try:
                return {"error": f"HTTP {resp.status_code}", "details": resp.json()}
            except Exception:
                return {"error": f"HTTP {resp.status_code}", "details": resp.text}

        if resp.status_code == 204:
            return {"ok": True}

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "details": resp.text}
        return resp.text
