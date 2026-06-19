"""Shared HTTP utilities for Notion API."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests

NOTION_BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.environ.get("NOTION_VERSION", "2022-06-28")


def notion_headers(notion_version: str | None = None) -> Dict[str, str]:
    api_key = os.environ.get("NOTION_API_KEY")
    if not api_key:
        raise RuntimeError("NOTION_API_KEY environment variable is required")
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": notion_version or DEFAULT_NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    notion_version: str | None = None,
    timeout: float = 60.0,
) -> Dict[str, Any]:
    url = f"{NOTION_BASE_URL}{path}"
    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=notion_headers(notion_version),
            params=params,
            json=json,
            timeout=timeout,
        )
        if resp.status_code >= 400:
            try:
                err = resp.json()
            except Exception:
                err = {"message": resp.text}
            return {"error": True, "status": resp.status_code, "details": err}
        if resp.status_code == 204:
            return {"ok": True}
        return resp.json()
    except Exception as e:
        return {"error": True, "message": str(e)}
