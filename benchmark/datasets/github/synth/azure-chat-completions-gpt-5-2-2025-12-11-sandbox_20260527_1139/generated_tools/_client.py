import os
import time
from typing import Any, Dict, Optional

import requests

DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(accept: Optional[str] = None) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    headers = {
        "Accept": accept or DEFAULT_ACCEPT,
        "X-GitHub-Api-Version": DEFAULT_API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None,
                 accept: Optional[str] = None, timeout: int = 30) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(accept), params=params, json=json, timeout=timeout)
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"status": 204}

    # Handle rate limit politely if agent loops
    if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
        reset = resp.headers.get("X-RateLimit-Reset")
        return {"error": "rate_limited", "status": 403, "reset": reset}

    try:
        data = resp.json()
    except ValueError:
        data = resp.text

    if 200 <= resp.status_code < 300:
        return data

    return {
        "error": "github_api_error",
        "status": resp.status_code,
        "url": url,
        "response": data,
    }


def split_owner_repo(owner_repo: Optional[str]) -> Dict[str, str]:
    if not owner_repo:
        owner_repo = os.getenv("GITHUB_TEST_REPO", "")
    if "/" not in owner_repo:
        raise ValueError("owner_repo must be in 'owner/repo' format (or set GITHUB_TEST_REPO)")
    owner, repo = owner_repo.split("/", 1)
    return {"owner": owner, "repo": repo}
