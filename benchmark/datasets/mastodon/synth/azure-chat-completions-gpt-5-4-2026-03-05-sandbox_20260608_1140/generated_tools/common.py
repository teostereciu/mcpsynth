import os
from typing import Any, Dict, Optional

import requests


def _base_url() -> str:
    base = os.getenv("MASTODON_BASE_URL", "").strip().rstrip("/")
    if not base:
        raise ValueError("MASTODON_BASE_URL is not set")
    return base


def _headers() -> Dict[str, str]:
    token = os.getenv("MASTODON_ACCESS_TOKEN", "").strip()
    if not token:
        raise ValueError("MASTODON_ACCESS_TOKEN is not set")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }


def mastodon_request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, files: Any = None) -> Any:
    try:
        url = f"{_base_url()}{path}"
        headers = _headers()
        response = requests.request(method=method, url=url, headers=headers, params=params, data=data, files=files, timeout=60)
        if response.status_code >= 400:
            try:
                payload = response.json()
            except Exception:
                payload = response.text
            return {"error": f"HTTP {response.status_code}", "details": payload}
        if not response.text:
            return {"ok": True}
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return response.json()
        return {"text": response.text}
    except Exception as e:
        return {"error": str(e)}


def clean_params(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
