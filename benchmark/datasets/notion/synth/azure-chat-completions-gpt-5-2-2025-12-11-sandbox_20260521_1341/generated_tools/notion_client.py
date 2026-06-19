import os
import time
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


class NotionClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        notion_version: str = DEFAULT_NOTION_VERSION,
        base_url: str = BASE_URL,
        timeout_s: int = 60,
    ):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        self.notion_version = notion_version
        self.base_url = base_url.rstrip("/")
        self.timeout_s = timeout_s

    def _headers(self) -> Dict[str, str]:
        if not self.api_key:
            return {}
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "NOTION_API_KEY is not set"}

        url = f"{self.base_url}{path}"
        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=self._headers(),
                params=params,
                json=json,
                timeout=self.timeout_s,
            )
        except requests.RequestException as e:
            return {"error": f"request_failed: {e}"}

        # Notion returns JSON errors.
        try:
            data = resp.json() if resp.content else None
        except ValueError:
            data = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return data if data is not None else {"ok": True}

        err: Dict[str, Any] = {
            "error": "notion_api_error",
            "status": resp.status_code,
        }
        if isinstance(data, dict):
            err.update(data)
        else:
            err["details"] = data
        return err


def omit_none(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}
