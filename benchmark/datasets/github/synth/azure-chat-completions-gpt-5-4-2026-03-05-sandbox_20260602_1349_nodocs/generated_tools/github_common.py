import os
from typing import Any, Dict, Optional

import requests

DEFAULT_API_BASE_URL = "https://api.github.com"
DEFAULT_ACCEPT = "application/vnd.github+json"
API_VERSION = "2022-11-28"


def get_base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")


def get_headers() -> Dict[str, str]:
    headers = {
        "Accept": DEFAULT_ACCEPT,
        "X-GitHub-Api-Version": API_VERSION,
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def github_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Any:
    url = f"{get_base_url()}{path}"
    try:
        response = requests.request(method=method, url=url, headers=get_headers(), params=params, json=json_body, timeout=60)
    except requests.RequestException as exc:
        return {"error": str(exc), "path": path, "method": method}

    if response.status_code == 204:
        return {"success": True, "status_code": 204}

    try:
        data = response.json()
    except ValueError:
        data = {"text": response.text}

    if response.ok:
        return data

    if isinstance(data, dict):
        data.setdefault("status_code", response.status_code)
        data.setdefault("path", path)
        data.setdefault("method", method)
        return data

    return {
        "error": "GitHub API request failed",
        "status_code": response.status_code,
        "details": data,
        "path": path,
        "method": method,
    }


def clean_params(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
