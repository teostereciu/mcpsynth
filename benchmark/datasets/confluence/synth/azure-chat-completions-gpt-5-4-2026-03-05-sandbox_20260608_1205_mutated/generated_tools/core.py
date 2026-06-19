import base64
import os
from typing import Any, Dict, Optional

import requests


class ConfluenceClient:
    def __init__(self) -> None:
        self.base_url = os.environ["CONFLUENCE_BASE_URL"].rstrip("/")
        email = os.environ["JIRA_EMAIL"]
        token = os.environ["JIRA_API_TOKEN"]
        auth = base64.b64encode(f"{email}:{token}".encode()).decode()
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Basic {auth}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        response = self.session.request(method, url, params=_clean(params), json=json, headers=headers)
        if response.status_code >= 400:
            raise RuntimeError(f"Confluence API error {response.status_code}: {response.text}")
        if response.status_code == 204 or not response.text:
            return {"status": response.status_code}
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            data = response.json()
            link = response.headers.get("Link")
            if link:
                return {"data": data, "link": link}
            return data
        return {"status": response.status_code, "text": response.text}


def _clean(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _clean(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [_clean(v) for v in value if v is not None]
    return value


client = ConfluenceClient()
