import os
import requests
from typing import Any, Dict, Optional


class NotionClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        notion_version: str = "2022-06-28",
        base_url: str = "https://api.notion.com/v1",
        timeout: int = 60,
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
        }

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
        if not self.api_key:
            return {"error": "Missing NOTION_API_KEY environment variable"}

        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=self._headers(),
                params=params,
                json=json,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

        try:
            data = resp.json() if resp.content else None
        except ValueError:
            data = resp.text

        if 200 <= resp.status_code < 300:
            return data

        # Notion error format: {"object":"error","status":...,"code":...,"message":...}
        if isinstance(data, dict):
            msg = data.get("message") or data.get("error") or str(data)
            code = data.get("code")
            return {"error": msg, "status": resp.status_code, "code": code, "details": data}
        return {"error": str(data), "status": resp.status_code}
