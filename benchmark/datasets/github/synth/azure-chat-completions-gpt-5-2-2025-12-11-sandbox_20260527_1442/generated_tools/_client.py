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


def gh_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 60,
) -> Any:
    url = f"{_base_url()}{path}"
    h = _headers()
    if headers:
        h.update(headers)

    try:
        resp = requests.request(
            method,
            url,
            params=params,
            json=json,
            data=data,
            headers=h,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"ok": True, "status": 204}

    content_type = resp.headers.get("content-type", "")
    body: Any
    if "application/json" in content_type:
        try:
            body = resp.json()
        except ValueError:
            body = resp.text
    else:
        body = resp.text

    if resp.status_code >= 400:
        return {
            "error": "GitHub API error",
            "status": resp.status_code,
            "url": url,
            "response": body,
        }

    return body
