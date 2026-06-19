import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"


def notion_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Any:
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"error": "Missing NOTION_API_KEY environment variable"}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
    }
    if json_body is not None:
        headers["Content-Type"] = "application/json"

    try:
        response = requests.request(method, f"{BASE_URL}{path}", headers=headers, params=params, json=json_body, timeout=60)
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
