from typing import Any, Dict, List, Optional

from ._client import request_json


def blocks_retrieve(block_id: str) -> Any:
    """GET /v1/blocks/{block_id}"""
    return request_json("GET", f"/blocks/{block_id}")


def blocks_children_list(block_id: str, *, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """GET /v1/blocks/{block_id}/children"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/blocks/{block_id}/children", params=params)


def blocks_children_append(block_id: str, children: List[Dict[str, Any]], *, after: Optional[str] = None) -> Any:
    """PATCH /v1/blocks/{block_id}/children"""
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return request_json("PATCH", f"/blocks/{block_id}/children", json_body=body)


def blocks_update(block_id: str, block: Dict[str, Any]) -> Any:
    """PATCH /v1/blocks/{block_id}"""
    return request_json("PATCH", f"/blocks/{block_id}", json_body=block)


def blocks_delete(block_id: str) -> Any:
    """DELETE /v1/blocks/{block_id}"""
    return request_json("DELETE", f"/blocks/{block_id}")
