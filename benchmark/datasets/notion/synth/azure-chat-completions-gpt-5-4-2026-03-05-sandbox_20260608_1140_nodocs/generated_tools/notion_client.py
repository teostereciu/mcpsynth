import os
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


class NotionClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("NOTION_API_KEY", "")

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }
        return headers

    def request(
        self,
        method: str,
        path: str,
        json_body: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if not self.api_key:
            return {"error": "NOTION_API_KEY environment variable is not set"}

        url = f"{BASE_URL}{path}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self._headers(),
                json=json_body,
                params=params,
                timeout=60,
            )
        except requests.RequestException as exc:
            return {"error": str(exc)}

        try:
            data = response.json()
        except ValueError:
            data = {"status_code": response.status_code, "text": response.text}

        if response.ok:
            return data

        if isinstance(data, dict):
            data.setdefault("status_code", response.status_code)
            return data
        return {"error": "Request failed", "status_code": response.status_code, "details": data}


client = NotionClient()
