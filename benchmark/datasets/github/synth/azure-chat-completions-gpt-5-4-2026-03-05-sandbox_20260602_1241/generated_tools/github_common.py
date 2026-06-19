import json
import os
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import requests

API_VERSION = "2026-03-10"
DEFAULT_BASE_URL = "https://api.github.com"


def get_base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def get_headers(accept: str = "application/vnd.github+json") -> Dict[str, str]:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": "github-rest-mcp-server",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def build_url(path: str, params: Optional[Dict[str, Any]] = None) -> str:
    url = f"{get_base_url()}{path}"
    if params:
        filtered = {k: v for k, v in params.items() if v is not None}
        if filtered:
            return f"{url}?{urlencode(filtered, doseq=True)}"
    return url


def github_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None, accept: str = "application/vnd.github+json") -> Dict[str, Any]:
    response = requests.request(
        method=method,
        url=build_url(path, params),
        headers=get_headers(accept),
        json=json_body,
        timeout=60,
    )
    content_type = response.headers.get("Content-Type", "")
    try:
        body: Any
        if "application/json" in content_type or response.text.startswith("{") or response.text.startswith("["):
            body = response.json() if response.text else None
        else:
            body = response.text
    except Exception:
        body = response.text
    return {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "body": body,
    }


def compact(result: Dict[str, Any]) -> str:
    return json.dumps(result, indent=2, ensure_ascii=False, default=str)
