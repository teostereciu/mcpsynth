import os
import requests
from typing import Any, Dict, Optional


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
        }

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        if not self.api_key:
            return {"error": "NOTION_API_KEY is not set"}
        url = self.base_url + path
        try:
            resp = requests.request(method, url, headers=self._headers(), params=params, json=json, timeout=60)
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = {"message": resp.text}
            return {"error": "Notion API error", "status": resp.status_code, "details": data}

        if resp.status_code == 204:
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return {"ok": True, "text": resp.text}
