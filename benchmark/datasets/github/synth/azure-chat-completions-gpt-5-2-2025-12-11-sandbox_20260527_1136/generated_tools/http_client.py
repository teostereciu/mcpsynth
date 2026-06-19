import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

DEFAULT_API_VERSION = "2026-03-10"
DEFAULT_ACCEPT = "application/vnd.github+json"


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(accept: Optional[str] = None) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": accept or DEFAULT_ACCEPT,
        "X-GitHub-Api-Version": DEFAULT_API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def request_json(
    method: str,
    path: str,
    *,
    accept: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Any = None,
    timeout: int = 60,
) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(accept),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json,
            data=data,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"ok": True, "status": 204}

    content_type = resp.headers.get("Content-Type", "")
    body: Any
    if "application/json" in content_type:
        try:
            body = resp.json()
        except ValueError:
            body = resp.text
    else:
        body = resp.text

    if 200 <= resp.status_code < 300:
        return body

    # Expected errors should be returned as dicts
    return {
        "error": "GitHub API error",
        "status": resp.status_code,
        "url": url,
        "response": body,
    }


def parse_owner_repo(owner: Optional[str] = None, repo: Optional[str] = None, owner_repo: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
    if owner and repo:
        return owner, repo
    if owner_repo and "/" in owner_repo:
        o, r = owner_repo.split("/", 1)
        return o, r
    test_repo = os.getenv("GITHUB_TEST_REPO")
    if test_repo and "/" in test_repo:
        o, r = test_repo.split("/", 1)
        return o, r
    return owner, repo
