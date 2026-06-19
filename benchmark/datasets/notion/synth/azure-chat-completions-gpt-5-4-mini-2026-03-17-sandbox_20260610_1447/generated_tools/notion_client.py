import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"


class NotionClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        })

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "NOTION_API_KEY is not set"}
        try:
            resp = self.session.request(method, f"{BASE_URL}{path}", params=params, json=json, timeout=60)
            if resp.status_code >= 400:
                try:
                    return {"error": resp.json()}
                except Exception:
                    return {"error": resp.text}
            if resp.text:
                return resp.json()
            return {}
        except requests.RequestException as e:
            return {"error": str(e)}
