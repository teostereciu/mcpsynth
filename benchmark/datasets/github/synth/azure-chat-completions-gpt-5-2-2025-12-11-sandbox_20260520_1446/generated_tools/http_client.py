import os
import time
from typing import Any, Dict, Optional, Tuple

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


def request_json(
    method: str,
    path: str,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
    timeout: float = 30.0,
) -> Any:
    """Internal helper. Not exposed as an MCP tool."""

    url_path = path
    if path_params:
        for k, v in path_params.items():
            url_path = url_path.replace("{" + k + "}", requests.utils.quote(str(v), safe=""))
            url_path = url_path.replace("{+" + k + "}", requests.utils.quote(str(v), safe="/"))

    url = f"{_base_url()}{url_path}"

    params = {k: v for k, v in (query or {}).items() if v is not None}

    for _ in range(2):
        resp = requests.request(
            method=method,
            url=url,
            headers=_headers(accept),
            params=params,
            json=body,
            timeout=timeout,
        )

        # Basic secondary rate limit / abuse detection backoff
        if resp.status_code in (429, 403) and resp.headers.get("Retry-After"):
            try:
                time.sleep(float(resp.headers["Retry-After"]))
                continue
            except Exception:
                pass
        break

    if resp.status_code >= 400:
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {
            "error": True,
            "status": resp.status_code,
            "message": err.get("message") if isinstance(err, dict) else str(err),
            "details": err,
            "url": url,
        }

    if resp.status_code == 204:
        return {"ok": True, "status": 204}

    ctype = resp.headers.get("Content-Type", "")
    if "application/json" in ctype or "+json" in ctype:
        return resp.json()

    return {"ok": True, "status": resp.status_code, "content": resp.text}
