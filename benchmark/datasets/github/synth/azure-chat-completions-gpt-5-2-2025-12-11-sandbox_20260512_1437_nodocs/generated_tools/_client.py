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


def gh_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=60)
    except Exception as e:
        return {"error": str(e), "url": url}

    if resp.status_code >= 400:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return {"error": "GitHub API error", "status": resp.status_code, "url": url, "details": data}

    if resp.status_code == 204:
        return {"ok": True}

    ctype = resp.headers.get("content-type", "")
    if "application/json" in ctype:
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to parse JSON", "status": resp.status_code, "url": url, "text": resp.text}
    return resp.text
