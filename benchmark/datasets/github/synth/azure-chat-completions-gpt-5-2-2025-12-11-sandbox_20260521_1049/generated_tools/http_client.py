import os
import time
from typing import Any, Dict, Optional, Tuple

import requests

DEFAULT_API_VERSION = "2026-03-10"


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(accept: Optional[str] = None, api_version: str = DEFAULT_API_VERSION) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": accept or "application/vnd.github+json",
        "X-GitHub-Api-Version": api_version,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
    api_version: str = DEFAULT_API_VERSION,
    timeout: int = 60,
) -> Tuple[int, Any, Dict[str, Any]]:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(accept=accept, api_version=api_version),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return 0, {"error": str(e)}, {}

    # Handle rate limiting gently
    if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
        reset = resp.headers.get("X-RateLimit-Reset")
        return resp.status_code, {"error": "rate_limited", "reset": reset}, dict(resp.headers)

    if resp.status_code == 204:
        return resp.status_code, None, dict(resp.headers)

    content_type = resp.headers.get("Content-Type", "")
    if "application/json" in content_type or content_type.endswith("+json"):
        try:
            data = resp.json()
        except ValueError:
            data = {"error": "invalid_json", "text": resp.text}
    else:
        data = resp.text

    if resp.status_code >= 400:
        # Normalize error payload
        if isinstance(data, dict):
            msg = data.get("message") or data.get("error") or "request_failed"
            return resp.status_code, {"error": msg, "status": resp.status_code, "details": data}, dict(resp.headers)
        return resp.status_code, {"error": "request_failed", "status": resp.status_code, "details": data}, dict(resp.headers)

    return resp.status_code, data, dict(resp.headers)
