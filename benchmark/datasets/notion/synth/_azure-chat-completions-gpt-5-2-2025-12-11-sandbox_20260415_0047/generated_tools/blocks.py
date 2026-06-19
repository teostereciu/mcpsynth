"""Tools for Notion Blocks API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import notion_request


def retrieve_block(*, block_id: str, notion_version: str | None = None) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}"""
    return notion_request("GET", f"/blocks/{block_id}", notion_version=notion_version)


def list_block_children(
    *,
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}/children"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request(
        "GET",
        f"/blocks/{block_id}/children",
        params=params or None,
        notion_version=notion_version,
    )


def append_block_children(
    *,
    block_id: str,
    children: List[Dict[str, Any]],
    after: Optional[str] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}/children"""
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return notion_request(
        "PATCH",
        f"/blocks/{block_id}/children",
        json=body,
        notion_version=notion_version,
    )


def update_block(
    *,
    block_id: str,
    block: Dict[str, Any],
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}

    block: partial block payload (e.g., {"paragraph": {"rich_text": [...]}})
    """
    return notion_request(
        "PATCH",
        f"/blocks/{block_id}",
        json=block,
        notion_version=notion_version,
    )


def delete_block(*, block_id: str, notion_version: str | None = None) -> Dict[str, Any]:
    """DELETE /v1/blocks/{block_id}"""
    return notion_request("DELETE", f"/blocks/{block_id}", notion_version=notion_version)
