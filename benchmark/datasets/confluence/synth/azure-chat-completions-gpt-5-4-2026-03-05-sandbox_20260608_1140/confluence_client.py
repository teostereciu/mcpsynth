import base64
import json
import os
from typing import Any, Dict, Optional

import requests


class ConfluenceClient:
    def __init__(self) -> None:
        self.base_url = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
        self.space_key = os.environ.get("CONFLUENCE_SPACE_KEY", "")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.api_token = os.environ.get("JIRA_API_TOKEN", "")

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode()).decode()
        headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Any] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
    ) -> Any:
        if not self.base_url or not self.email or not self.api_token:
            return {"error": "Missing required environment variables for Confluence authentication."}
        try:
            response = requests.request(
                method,
                self._url(path),
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                data=data,
                headers=self._headers(headers),
                files=files,
                timeout=60,
            )
            if response.status_code == 204:
                return {"ok": True, "status_code": 204}
            content_type = response.headers.get("Content-Type", "")
            payload: Any
            if "application/json" in content_type:
                payload = response.json()
            else:
                payload = {"text": response.text}
            if response.ok:
                return payload
            return {
                "error": f"HTTP {response.status_code}",
                "status_code": response.status_code,
                "details": payload,
            }
        except requests.RequestException as exc:
            return {"error": str(exc)}


client = ConfluenceClient()


def parse_json_if_needed(value: Any) -> Any:
    if isinstance(value, str):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value
