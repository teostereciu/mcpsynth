import base64
import json
import os
from typing import Any, Dict, Optional

import requests


class JiraClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("JIRA_BASE_URL", "").rstrip("/")
        self.email = os.getenv("JIRA_EMAIL", "")
        self.api_token = os.getenv("JIRA_API_TOKEN", "")
        self.api_base = f"{self.base_url}/rest/api/3" if self.base_url else ""

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode()).decode()
        headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def _check_config(self) -> Optional[Dict[str, str]]:
        if not self.base_url or not self.email or not self.api_token:
            return {
                "error": "Missing Jira configuration. Set JIRA_BASE_URL, JIRA_EMAIL, and JIRA_API_TOKEN."
            }
        return None

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
        config_error = self._check_config()
        if config_error:
            return config_error
        url = f"{self.api_base}{path}"
        try:
            response = requests.request(
                method=method,
                url=url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                data=data,
                headers=self._headers(headers),
                files=files,
                timeout=60,
            )
        except requests.RequestException as exc:
            return {"error": str(exc)}

        if response.status_code == 204:
            return {"success": True, "status_code": 204}

        content_type = response.headers.get("Content-Type", "")
        body: Any
        if "application/json" in content_type:
            try:
                body = response.json()
            except ValueError:
                body = {"raw": response.text}
        else:
            body = response.text

        if response.ok:
            return body

        if isinstance(body, dict):
            body.setdefault("status_code", response.status_code)
            return body
        return {"error": str(body), "status_code": response.status_code}


jira_client = JiraClient()
