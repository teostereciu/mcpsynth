import os
import requests
from typing import Any, Dict, Optional


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers() -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=60)
    except requests.RequestException as e:
        return {"error": str(e)}

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

    return {
        "error": "GitHub API error",
        "status": resp.status_code,
        "message": (data.get("message") if isinstance(data, dict) else None) or resp.reason,
        "details": data,
    }
