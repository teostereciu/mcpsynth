import os
import time
from typing import Any, Dict, Optional

import requests


BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2026-03-11")


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    token = os.getenv("NOTION_API_KEY")
    if not token:
        # Keep JSON-serializable error handling at call sites.
        return {}
    h = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": DEFAULT_NOTION_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra:
        h.update(extra)
    return h


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 60,
    max_retries: int = 3,
) -> Any:
    """Make a Notion API request and return JSON-serializable output.

    Returns:
      - dict/list on success
      - {"error": ..., "status": ..., "details": ...} on expected failures
    """

    if not os.getenv("NOTION_API_KEY"):
        return {"error": "NOTION_API_KEY is not set"}

    url = BASE_URL + (path if path.startswith("/") else f"/{path}")
    h = _headers(headers)
    if not h:
        return {"error": "NOTION_API_KEY is not set"}

    last_err: Optional[Dict[str, Any]] = None
    for attempt in range(max_retries):
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json,
                data=data,
                headers=h,
                timeout=timeout,
            )
        except requests.RequestException as e:
            last_err = {"error": "request_failed", "details": str(e)}
            time.sleep(0.5 * (attempt + 1))
            continue

        content_type = resp.headers.get("content-type", "")
        parsed: Any
        if "application/json" in content_type:
            try:
                parsed = resp.json()
            except Exception:
                parsed = {"raw": resp.text}
        else:
            parsed = {"raw": resp.text}

        if 200 <= resp.status_code < 300:
            return parsed

        # Notion error payloads are JSON with fields like: status, code, message
        last_err = {
            "error": "notion_api_error",
            "status": resp.status_code,
            "details": parsed,
        }

        # Retry on rate limit / transient server errors
        if resp.status_code in (429, 500, 502, 503, 504):
            time.sleep(0.75 * (attempt + 1))
            continue

        return last_err

    return last_err or {"error": "unknown_error"}
