import os
import time
from typing import Any, Dict, Optional

import requests

DEFAULT_API_VERSION = "2026-03-10"


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(accept: Optional[str] = None, api_version: str = DEFAULT_API_VERSION) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    h = {
        "Accept": accept or "application/vnd.github+json",
        "X-GitHub-Api-Version": api_version,
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def gh_request(
    method: str,
    path: str,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
    api_version: str = DEFAULT_API_VERSION,
    timeout: int = 60,
) -> Any:
    url_path = path
    if path_params:
        for k, v in path_params.items():
            url_path = url_path.replace("{" + k + "}", requests.utils.quote(str(v), safe=""))
            url_path = url_path.replace("{+" + k + "}", requests.utils.quote(str(v), safe="/"))
    url = f"{_base_url()}{url_path}"

    params = {k: v for k, v in (query or {}).items() if v is not None}

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=_headers(accept=accept, api_version=api_version),
            params=params,
            json=json,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"status": 204}

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
        "rate_limit_remaining": resp.headers.get("x-ratelimit-remaining"),
        "rate_limit_reset": resp.headers.get("x-ratelimit-reset"),
    }
