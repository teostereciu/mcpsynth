import os
import json
from typing import Any, Dict, Optional

import requests


NOTION_BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    token = os.getenv("NOTION_API_KEY")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Notion-Version": DEFAULT_NOTION_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if extra:
        headers.update({k: v for k, v in extra.items() if v is not None})
    return headers


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    """Internal helper. Returns JSON-serializable dict/list or {error,...}."""
    url = NOTION_BASE_URL + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json_body, timeout=60)
    except requests.RequestException as e:
        return {"error": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        try:
            data = resp.json() if "application/json" in content_type else {"message": resp.text}
        except Exception:
            data = {"message": resp.text}
        return {
            "error": "notion_api_error",
            "status": resp.status_code,
            "details": data,
        }

    if resp.status_code == 204:
        return {"ok": True}

    if "application/json" in content_type:
        try:
            return resp.json()
        except Exception:
            return {"error": "invalid_json", "status": resp.status_code, "text": resp.text}

    # Fallback for unexpected content types
    return {"ok": True, "status": resp.status_code, "text": resp.text}
