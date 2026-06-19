import os
import json
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


def _headers() -> Dict[str, str]:
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {}
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": DEFAULT_NOTION_VERSION,
        "Content-Type": "application/json",
    }


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Dict[str, Any]:
    """Internal helper. Returns JSON dict or {"error": ...}.

    No MCP tool should directly expose arbitrary method/path.
    """
    hdrs = _headers()
    if not hdrs:
        return {"error": "NOTION_API_KEY is not set"}

    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(method, url, headers=hdrs, params=params, json=json_body, timeout=60)
    except requests.RequestException as e:
        return {"error": f"request_failed: {e}"}

    content_type = resp.headers.get("content-type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except ValueError:
            data = {"raw": resp.text}
    else:
        data = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        if isinstance(data, dict):
            return data
        return {"result": data}

    # Notion errors are JSON with message/code
    if isinstance(data, dict):
        data.setdefault("status", resp.status_code)
        return {"error": data}

    return {"error": {"status": resp.status_code, "message": resp.text}}
