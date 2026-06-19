import os
from typing import Any, Dict, Optional

import httpx


NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"


class NotionClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        if not self.api_key:
            raise RuntimeError("NOTION_API_KEY is required")
        self._client = httpx.Client(
            base_url=NOTION_BASE_URL,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            },
            timeout=60.0,
        )

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> Any:
        resp = self._client.request(method, path, params=params, json=json)
        resp.raise_for_status()
        return resp.json()

    def close(self):
        self._client.close()
