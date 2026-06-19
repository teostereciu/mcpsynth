import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2022-06-28")


class NotionClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        notion_version: str = DEFAULT_NOTION_VERSION,
        base_url: str = BASE_URL,
        timeout_s: int = 60,
        max_retries: int = 3,
    ):
        self.api_key = api_key or os.getenv("NOTION_API_KEY")
        self.notion_version = notion_version
        self.base_url = base_url.rstrip("/")
        self.timeout_s = timeout_s
        self.max_retries = max_retries

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
    ) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
        if not self.api_key:
            return None, {"error": "Missing NOTION_API_KEY env var"}

        url = f"{self.base_url}{path}"
        headers = self._headers()

        last_err: Optional[Dict[str, Any]] = None
        for attempt in range(self.max_retries):
            try:
                resp = requests.request(
                    method,
                    url,
                    headers=headers,
                    params=params,
                    json=json,
                    timeout=self.timeout_s,
                )

                if resp.status_code == 429 and attempt < self.max_retries - 1:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (0.5 * (2**attempt))
                    time.sleep(min(10.0, sleep_s))
                    continue

                if 200 <= resp.status_code < 300:
                    if resp.content:
                        return resp.json(), None
                    return {}, None

                # Notion errors are JSON with {object:"error", status, code, message}
                try:
                    err_json = resp.json()
                except Exception:
                    err_json = {"error": resp.text or "Request failed", "status": resp.status_code}

                if isinstance(err_json, dict):
                    err_json.setdefault("status", resp.status_code)
                last_err = err_json if isinstance(err_json, dict) else {"error": err_json}
                return None, last_err

            except requests.RequestException as e:
                last_err = {"error": str(e)}
                if attempt < self.max_retries - 1:
                    time.sleep(0.5 * (2**attempt))
                    continue
                return None, last_err

        return None, last_err or {"error": "Unknown error"}
