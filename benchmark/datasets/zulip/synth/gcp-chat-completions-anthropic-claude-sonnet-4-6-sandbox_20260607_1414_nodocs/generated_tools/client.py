"""
Shared HTTP client for Zulip API calls.
Reads credentials from environment variables:
  ZULIP_EMAIL   — bot/user email
  ZULIP_API_KEY — API key
  ZULIP_SITE    — base URL, e.g. https://your-org.zulipchat.com
"""

import os
import requests
from typing import Any, Optional

_EMAIL = os.environ.get("ZULIP_EMAIL", "")
_API_KEY = os.environ.get("ZULIP_API_KEY", "")
_SITE = os.environ.get("ZULIP_SITE", "").rstrip("/")
_BASE_URL = f"{_SITE}/api/v1"


def _auth() -> tuple[str, str]:
    return (_EMAIL, _API_KEY)


def _url(path: str) -> str:
    return f"{_BASE_URL}{path}"


def zulip_get(path: str, params: Optional[dict] = None) -> dict:
    """Perform an authenticated GET request to the Zulip API."""
    try:
        resp = requests.get(_url(path), params=params or {}, auth=_auth(), timeout=30)
        return resp.json()
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}


def zulip_post(path: str, data: Optional[dict] = None) -> dict:
    """Perform an authenticated POST request to the Zulip API."""
    try:
        resp = requests.post(_url(path), data=data or {}, auth=_auth(), timeout=30)
        return resp.json()
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}


def zulip_patch(path: str, data: Optional[dict] = None) -> dict:
    """Perform an authenticated PATCH request to the Zulip API."""
    try:
        resp = requests.patch(_url(path), data=data or {}, auth=_auth(), timeout=30)
        return resp.json()
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}


def zulip_delete(path: str, params: Optional[dict] = None) -> dict:
    """Perform an authenticated DELETE request to the Zulip API."""
    try:
        resp = requests.delete(_url(path), params=params or {}, auth=_auth(), timeout=30)
        return resp.json()
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}


def zulip_post_file(path: str, files: dict, data: Optional[dict] = None) -> dict:
    """Perform an authenticated multipart POST request (file upload)."""
    try:
        resp = requests.post(
            _url(path), files=files, data=data or {}, auth=_auth(), timeout=60
        )
        return resp.json()
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}
