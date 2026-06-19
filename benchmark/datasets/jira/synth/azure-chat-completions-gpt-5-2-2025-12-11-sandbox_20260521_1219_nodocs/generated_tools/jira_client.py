import os
import base64
from typing import Any, Dict, Optional

import requests


class JiraClient:
    def __init__(self):
        self.base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.api_token = os.environ.get("JIRA_API_TOKEN", "")
        if not self.base_url:
            raise RuntimeError("JIRA_BASE_URL is required")
        self.api_base = f"{self.base_url}/rest/api/3"

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("utf-8")
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
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        files: Any = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        url = f"{self.api_base}{path}"
        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=self._headers(headers),
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        if resp.status_code >= 400:
            # Try to parse Jira error payload
            try:
                err = resp.json() if "application/json" in content_type else {"message": resp.text}
            except Exception:
                err = {"message": resp.text}
            return {"error": "HTTP error", "status": resp.status_code, "details": err}

        if resp.status_code == 204:
            return {"ok": True}

        if "application/json" in content_type:
            try:
                return resp.json()
            except Exception:
                return {"ok": True, "raw": resp.text}

        return {"ok": True, "raw": resp.text}
