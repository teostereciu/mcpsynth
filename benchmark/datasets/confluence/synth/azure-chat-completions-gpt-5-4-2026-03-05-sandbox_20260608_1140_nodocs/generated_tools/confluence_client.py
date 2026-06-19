import os
import json
from typing import Any, Dict, Optional

import requests
from requests.auth import HTTPBasicAuth


class ConfluenceClient:
    def __init__(self) -> None:
        self.base_url = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
        self.space_key = os.getenv("CONFLUENCE_SPACE_KEY", "")
        self.email = os.getenv("JIRA_EMAIL", "")
        self.api_token = os.getenv("JIRA_API_TOKEN", "")

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Accept": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def _auth(self) -> HTTPBasicAuth:
        return HTTPBasicAuth(self.email, self.api_token)

    def _url(self, path: str) -> str:
        if not self.base_url:
            return path
        return f"{self.base_url}{path}"

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
        stream: bool = False,
    ) -> Dict[str, Any]:
        if not self.base_url:
            return {"error": "Missing CONFLUENCE_BASE_URL"}
        if not self.email or not self.api_token:
            return {"error": "Missing JIRA_EMAIL or JIRA_API_TOKEN"}
        try:
            response = requests.request(
                method=method,
                url=self._url(path),
                params=params,
                json=json_body,
                data=data,
                headers=self._headers(headers),
                auth=self._auth(),
                files=files,
                stream=stream,
                timeout=60,
            )
            if response.status_code >= 400:
                try:
                    payload = response.json()
                except Exception:
                    payload = response.text
                return {
                    "error": f"HTTP {response.status_code}",
                    "status_code": response.status_code,
                    "details": payload,
                }
            if stream:
                return {"response": response}
            if not response.text:
                return {"ok": True, "status_code": response.status_code}
            content_type = response.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return response.json()
            return {"text": response.text, "status_code": response.status_code}
        except requests.RequestException as exc:
            return {"error": str(exc)}


client = ConfluenceClient()
