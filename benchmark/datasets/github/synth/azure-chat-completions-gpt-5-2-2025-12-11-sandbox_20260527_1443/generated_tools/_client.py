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


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
    api_version: str = DEFAULT_API_VERSION,
    timeout: float = 30.0,
) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=_headers(accept=accept, api_version=api_version),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"ok": True, "status": 204}

    # Handle redirects for download endpoints etc.
    if resp.is_redirect or resp.status_code in (301, 302, 303, 307, 308):
        return {"redirect": resp.headers.get("Location"), "status": resp.status_code}

    try:
        data = resp.json()
    except ValueError:
        data = resp.text

    if 200 <= resp.status_code < 300:
        return data

    # Expected errors should be returned as dicts
    err: Dict[str, Any] = {
        "error": "GitHub API error",
        "status": resp.status_code,
        "url": url,
    }
    if isinstance(data, dict):
        err.update({"message": data.get("message"), "documentation_url": data.get("documentation_url"), "details": data})
    else:
        err["message"] = str(data)
    # Rate limit hints
    if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
        reset = resp.headers.get("X-RateLimit-Reset")
        if reset:
            try:
                err["rate_limit_reset_unix"] = int(reset)
                err["rate_limit_reset_in_seconds"] = max(0, int(reset) - int(time.time()))
            except Exception:
                pass
    return err
