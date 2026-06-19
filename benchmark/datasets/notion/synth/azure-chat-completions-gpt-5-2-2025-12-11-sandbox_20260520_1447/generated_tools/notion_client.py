import os
import json
from typing import Any, Dict, Optional

import requests


NOTION_BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


class NotionClient:
    def __init__(self, api_key: Optional[str] = None, notion_version: str = DEFAULT_NOTION_VERSION):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        self.notion_version = notion_version

    def _headers(self) -> Dict[str, str]:
        if not self.api_key:
            return {"error": "Missing NOTION_API_KEY"}  # type: ignore[return-value]
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        headers = self._headers()
        if "error" in headers:
            return headers  # type: ignore[return-value]

        url = NOTION_BASE_URL + path
        try:
            resp = requests.request(method, url, headers=headers, params=params, json=json_body, timeout=timeout)
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("Content-Type", "")
        data: Any
        if "application/json" in content_type:
            try:
                data = resp.json()
            except ValueError:
                data = {"raw": resp.text}
        else:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "Notion API error",
                "status": resp.status_code,
                "data": data,
            }
        if isinstance(data, dict):
            return data
        return {"data": data}


def _maybe_json_loads(s: Optional[str]) -> Optional[Dict[str, Any]]:
    if s is None:
        return None
    if isinstance(s, str):
        s = s.strip()
        if not s:
            return None
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return None
    return None
