"""Shared HTTP client utilities for GitHub REST API.

All generated tools should use :func:`github_request`.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests

DEFAULT_API_BASE_URL = "https://api.github.com"
DEFAULT_API_VERSION = "2022-11-28"


def _headers(extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN")
    headers: Dict[str, str] = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": os.environ.get("GITHUB_API_VERSION", DEFAULT_API_VERSION),
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if extra_headers:
        headers.update({k: v for k, v in extra_headers.items() if v is not None})
    return headers


def github_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Perform an HTTP request to GitHub REST API.

    Returns a JSON-serializable dict:
      - On success: {"status": int, "data": parsed_json_or_text, "headers": {...}}
      - On error:   {"error": str, "status": int, "data": parsed_json_or_text}
    """

    base_url = os.environ.get("GITHUB_API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")
    url = f"{base_url}{path if path.startswith('/') else '/' + path}"

    try:
        resp = requests.request(
            method.upper(),
            url,
            headers=_headers(headers),
            params=params,
            json=json,
            data=data,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}

    content_type = resp.headers.get("Content-Type", "")
    parsed: Any
    if "application/json" in content_type:
        try:
            parsed = resp.json()
        except ValueError:
            parsed = resp.text
    else:
        parsed = resp.text

    out = {"status": resp.status_code, "headers": dict(resp.headers), "data": parsed}
    if resp.status_code >= 400:
        msg = None
        if isinstance(parsed, dict):
            msg = parsed.get("message")
        return {"error": msg or f"GitHub API error ({resp.status_code})", **out}
    return out


def split_repo(full_name: str) -> Dict[str, str]:
    """Split 'owner/repo' into components."""
    if not full_name or "/" not in full_name:
        raise ValueError("Repository must be in 'owner/repo' format")
    owner, repo = full_name.split("/", 1)
    return {"owner": owner, "repo": repo}
