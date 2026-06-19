import os
from typing import Any, Dict, Optional

import requests


def _base_url() -> str:
    base = os.getenv("MASTODON_BASE_URL", "").rstrip("/")
    if not base:
        raise ValueError("MASTODON_BASE_URL is not set")
    return base


def _headers() -> Dict[str, str]:
    token = os.getenv("MASTODON_ACCESS_TOKEN", "")
    if not token:
        raise ValueError("MASTODON_ACCESS_TOKEN is not set")
    return {"Authorization": f"Bearer {token}"}


def mastodon_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
) -> Any:
    try:
        url = f"{_base_url()}{path}"
        response = requests.request(
            method=method,
            url=url,
            headers=_headers(),
            params={k: v for k, v in (params or {}).items() if v is not None},
            data={k: v for k, v in (data or {}).items() if v is not None} if data else None,
            files=files,
            json=json_body,
            timeout=60,
        )
        response.raise_for_status()
        if not response.text:
            return {"ok": True}
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return response.json()
        return {"text": response.text}
    except Exception as e:
        return {"error": str(e)}
