import os
import time
from typing import Any, Dict, Optional

import requests

DEFAULT_API_VERSION = "2026-03-10"


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(accept: Optional[str] = None) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    hdrs = {
        "Accept": accept or "application/vnd.github+json",
        "X-GitHub-Api-Version": DEFAULT_API_VERSION,
    }
    if token:
        hdrs["Authorization"] = f"Bearer {token}"
    return hdrs


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None, accept: Optional[str] = None) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(accept), params=params, json=json, timeout=60)
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"ok": True, "status": 204}

    content_type = resp.headers.get("content-type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except ValueError:
            data = resp.text
    else:
        data = resp.text

    if 200 <= resp.status_code < 300:
        return data

    # Expected errors should be returned, not raised.
    return {
        "error": "GitHub API error",
        "status": resp.status_code,
        "url": url,
        "response": data,
    }
