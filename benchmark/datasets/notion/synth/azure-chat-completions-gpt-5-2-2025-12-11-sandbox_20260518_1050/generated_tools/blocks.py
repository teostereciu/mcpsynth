from typing import Any, Dict, Optional

from .client import notion_request


def retrieve_block(block_id: str) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}"""
    return notion_request("GET", f"/blocks/{block_id}")


def retrieve_block_children(
    block_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}/children"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", f"/blocks/{block_id}/children", params=params or None)


def append_block_children(
    block_id: str,
    children: list,
    *,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}/children"""
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return notion_request("PATCH", f"/blocks/{block_id}/children", json_body=body)


def update_block(block_id: str, block: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}

    Args:
        block: Partial block object fields to update.
    """
    return notion_request("PATCH", f"/blocks/{block_id}", json_body=block)


def delete_block(block_id: str) -> Dict[str, Any]:
    """DELETE /v1/blocks/{block_id}"""
    return notion_request("DELETE", f"/blocks/{block_id}")
