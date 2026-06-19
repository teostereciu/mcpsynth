import json
import os
from typing import Any, Dict, Optional

import requests

BASE_API_PATH = "/rest/api/3"


class JiraClient:
    def __init__(self) -> None:
        base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        email = os.environ.get("JIRA_EMAIL")
        token = os.environ.get("JIRA_API_TOKEN")
        if not base_url:
            raise RuntimeError("JIRA_BASE_URL is required")
        if not email:
            raise RuntimeError("JIRA_EMAIL is required")
        if not token:
            raise RuntimeError("JIRA_API_TOKEN is required")
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = (email, token)
        self.session.headers.update({"Accept": "application/json"})

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Any = None,
        files: Any = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        request_headers = dict(headers or {})
        if json_body is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        response = self.session.request(
            method=method,
            url=url,
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            headers=request_headers,
            data=data,
            files=files,
        )
        if response.status_code >= 400:
            raise RuntimeError(f"Jira API error {response.status_code}: {response.text}")
        content_type = response.headers.get("Content-Type", "")
        if not response.content:
            return {"status": response.status_code}
        if "application/json" in content_type:
            return response.json()
        return {
            "status": response.status_code,
            "content_type": content_type,
            "text": response.text,
        }


def compact_dict(values: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in values.items() if v is not None}


def parse_json(value: Optional[str]) -> Any:
    if value is None:
        return None
    return json.loads(value)
