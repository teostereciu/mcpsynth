import os
import requests
from typing import Any, Dict, Optional


NOTION_BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    api_key = os.getenv("NOTION_API_KEY")
    h = {
        "Authorization": f"Bearer {api_key}" if api_key else "",
        "Notion-Version": DEFAULT_NOTION_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra:
        h.update({k: v for k, v in extra.items() if v is not None})
    return h


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Dict[str, Any]:
    """Internal helper. Returns JSON dict; errors returned as {"error": ..., "status": ..., "details": ...}."""
    url = NOTION_BASE_URL + path
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "details": str(e)}

    try:
        data = resp.json() if resp.content else {}
    except Exception:
        data = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return data if isinstance(data, dict) else {"result": data}

    return {
        "error": "notion_api_error",
        "status": resp.status_code,
        "details": data,
    }
