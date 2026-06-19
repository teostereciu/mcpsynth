import os
import requests
from typing import Any, Dict, Optional


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(accept: Optional[str] = None) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    hdrs = {
        "Accept": accept or "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if token:
        hdrs["Authorization"] = f"Bearer {token}"
    return hdrs


def gh_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None, accept: Optional[str] = None) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(accept), params=params, json=json, timeout=60)
    except Exception as e:
        return {"error": str(e)}

    if resp.status_code == 204:
        return {"status": 204}

    content_type = resp.headers.get("content-type", "")
    data: Any
    if "application/json" in content_type or content_type.endswith("+json"):
        try:
            data = resp.json()
        except Exception:
            data = resp.text
    else:
        data = resp.text

    if resp.ok:
        return data

    return {
        "error": "GitHub API error",
        "status": resp.status_code,
        "message": (data.get("message") if isinstance(data, dict) else str(data))[:1000],
        "response": data,
    }
