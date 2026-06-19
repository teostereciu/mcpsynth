"""HTTP client utilities for the Zulip REST API.

All requests use HTTP Basic auth with credentials from environment:
- ZULIP_EMAIL
- ZULIP_API_KEY
- ZULIP_SITE

This module is intentionally small and reused by all tool modules.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from typing import Any, Dict, Mapping, Optional

import requests


@dataclass(frozen=True)
class ZulipConfig:
    site: str
    email: str
    api_key: str


def get_config() -> ZulipConfig:
    """Load Zulip credentials from environment variables."""
    return ZulipConfig(
        site=os.environ["ZULIP_SITE"].rstrip("/"),
        email=os.environ["ZULIP_EMAIL"],
        api_key=os.environ["ZULIP_API_KEY"],
    )


def _coerce_data(data: Optional[Mapping[str, Any]]) -> Optional[Dict[str, Any]]:
    if data is None:
        return None
    out: Dict[str, Any] = {}
    for k, v in data.items():
        if v is None:
            continue
        if isinstance(v, (dict, list)):
            out[k] = json.dumps(v)
        else:
            out[k] = v
    return out


def zulip_request(method: str, path: str, *, params: Mapping[str, Any] | None = None, data: Mapping[str, Any] | None = None) -> Dict[str, Any]:
    """Make an authenticated request to the Zulip API.

    Returns a JSON dict. Errors are returned as JSON dicts when possible.
    """
    cfg = get_config()
    url = f"{cfg.site}/api/v1{path}"

    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            auth=(cfg.email, cfg.api_key),
            params=_coerce_data(params),
            data=_coerce_data(data),
            timeout=30,
        )
        # Zulip returns JSON even for many errors; try to parse first.
        try:
            payload = resp.json()
        except Exception:
            payload = {"result": "error", "msg": resp.text, "http_status": resp.status_code}

        if resp.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("result", "error")
                payload.setdefault("http_status", resp.status_code)
            return payload if isinstance(payload, dict) else {"result": "error", "msg": str(payload), "http_status": resp.status_code}

        return payload if isinstance(payload, dict) else {"result": "success", "data": payload}
    except requests.RequestException as e:
        return {"result": "error", "msg": str(e)}
