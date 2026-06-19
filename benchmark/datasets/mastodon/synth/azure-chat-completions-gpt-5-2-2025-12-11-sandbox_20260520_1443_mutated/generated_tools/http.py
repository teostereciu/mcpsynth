import os
import json
from typing import Any, Dict, Optional

import requests


def _base_url() -> str:
    base = os.environ.get("MASTODON_BASE_URL", "").strip()
    if not base:
        raise RuntimeError("MASTODON_BASE_URL is not set")
    return base.rstrip("/")


def _auth_headers() -> Dict[str, str]:
    token = os.environ.get("MASTODON_ACCESS_TOKEN", "").strip()
    if not token:
        raise RuntimeError("MASTODON_ACCESS_TOKEN is not set")
    return {"Authorization": f"Bearer {token}"}


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
    timeout: int = 30,
) -> Any:
    url = f"{_base_url()}{path}"
    headers = _auth_headers()

    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json_body,
            files=files,
            timeout=timeout,
        )
    except Exception as e:
        return {"error": f"request_failed: {e}"}

    content_type = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        try:
            err = resp.json() if "application/json" in content_type else {"error": resp.text}
        except Exception:
            err = {"error": resp.text}
        err.setdefault("status_code", resp.status_code)
        err.setdefault("url", url)
        return err

    if resp.status_code == 204:
        return {"ok": True}

    if "application/json" in content_type:
        try:
            return resp.json()
        except json.JSONDecodeError:
            return {"error": "invalid_json_response", "status_code": resp.status_code, "text": resp.text}

    return {"ok": True, "text": resp.text}
