import os
import json
from typing import Any, Dict, Optional

import requests


class NotionClient:
    def __init__(self, api_key: Optional[str] = None, notion_version: str = "2022-06-28"):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        self.notion_version = notion_version
        self.base_url = "https://api.notion.com/v1"

    def _headers(self) -> Dict[str, str]:
        if not self.api_key:
            return {}
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing NOTION_API_KEY environment variable"}

        url = self.base_url + path
        try:
            resp = requests.request(method, url, headers=self._headers(), params=params, json=json_body, timeout=60)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

        # Notion returns JSON for errors too
        try:
            data = resp.json() if resp.text else None
        except json.JSONDecodeError:
            data = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return data if data is not None else {"ok": True}

        # Normalize error
        if isinstance(data, dict):
            msg = data.get("message") or data.get("error") or data.get("code") or "Unknown error"
            return {"error": msg, "status": resp.status_code, "details": data}
        return {"error": "HTTP error", "status": resp.status_code, "details": data}
