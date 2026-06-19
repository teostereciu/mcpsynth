import os
import json
from typing import Any, Dict, Optional

import requests


NOTION_BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"_missing": "NOTION_API_KEY"}

    h = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": DEFAULT_NOTION_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra:
        h.update({k: v for k, v in extra.items() if v is not None})
    return h


def notion_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Dict[str, Any]:
    h = _headers()
    if "_missing" in h:
        return {"error": "Missing NOTION_API_KEY environment variable"}

    url = NOTION_BASE_URL + path
    try:
        resp = requests.request(method, url, headers=h, params=params, json=json_body, timeout=60)
    except requests.RequestException as e:
        return {"error": str(e)}

    content_type = resp.headers.get("Content-Type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception:
            data = {"raw": resp.text}
    else:
        data = {"raw": resp.text}

    if resp.status_code >= 400:
        if isinstance(data, dict):
            data.setdefault("status", resp.status_code)
            return {"error": data}
        return {"error": {"status": resp.status_code, "body": data}}

    return data if isinstance(data, (dict, list, str, int, float, bool)) else json.loads(json.dumps(data, default=str))
