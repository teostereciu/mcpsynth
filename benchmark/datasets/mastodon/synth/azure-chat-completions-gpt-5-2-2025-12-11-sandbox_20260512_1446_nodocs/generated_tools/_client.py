import os
import requests
from typing import Any, Dict, Optional


def _base_url() -> str:
    base = os.environ.get("MASTODON_BASE_URL", "").strip()
    if not base:
        raise RuntimeError("MASTODON_BASE_URL is not set")
    return base.rstrip("/")


def _token() -> str:
    tok = os.environ.get("MASTODON_ACCESS_TOKEN", "").strip()
    if not tok:
        raise RuntimeError("MASTODON_ACCESS_TOKEN is not set")
    return tok


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
    timeout: int = 30,
) -> Any:
    url = f"{_base_url()}{path}"
    headers = {
        "Authorization": f"Bearer {_token()}",
        "Accept": "application/json",
    }
    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            files=files,
            timeout=timeout,
        )
        if resp.status_code >= 400:
            try:
                err = resp.json()
            except Exception:
                err = {"message": resp.text}
            return {"error": "http_error", "status": resp.status_code, "details": err}
        if resp.status_code == 204:
            return {"ok": True}
        if not resp.content:
            return {"ok": True}
        return resp.json()
    except Exception as e:
        return {"error": "request_failed", "details": str(e)}
