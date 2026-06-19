import os
import requests
from typing import Any, Dict, Optional


class NotionClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        notion_version: str = "2022-06-28",
        base_url: str = "https://api.notion.com/v1",
        timeout: float = 30.0,
    ):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        self.notion_version = notion_version
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        if not self.api_key:
            return {}
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(self, method: str, path: str, json: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        if not self.api_key:
            return {"error": "NOTION_API_KEY is not set"}

        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                headers=self._headers(),
                json=json,
                params=params,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

        try:
            data = resp.json() if resp.content else None
        except ValueError:
            data = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return data

        # Notion error format: {"object":"error","status":...,"code":...,"message":...}
        if isinstance(data, dict):
            data.setdefault("status_code", resp.status_code)
            return {"error": data}
        return {"error": {"status_code": resp.status_code, "body": data}}
