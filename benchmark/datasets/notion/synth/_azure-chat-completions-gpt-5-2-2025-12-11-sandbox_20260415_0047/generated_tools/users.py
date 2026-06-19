"""Tools for Notion Users API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import notion_request


def list_users(
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """GET /v1/users"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", "/users", params=params or None, notion_version=notion_version)


def retrieve_user(*, user_id: str, notion_version: str | None = None) -> Dict[str, Any]:
    """GET /v1/users/{user_id}"""
    return notion_request("GET", f"/users/{user_id}", notion_version=notion_version)


def retrieve_me(*, notion_version: str | None = None) -> Dict[str, Any]:
    """GET /v1/users/me"""
    return notion_request("GET", "/users/me", notion_version=notion_version)
