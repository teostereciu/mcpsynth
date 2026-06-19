from typing import Any, Dict, Optional

from ._client import request_json


def blocks_retrieve(block_id: str) -> Any:
    return request_json("GET", f"/blocks/{block_id}")


def blocks_children_list(
    block_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/blocks/{block_id}/children", params=params or None)


def blocks_children_append(block_id: str, children: list, *, after: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return request_json("PATCH", f"/blocks/{block_id}/children", json=body)


def blocks_update(block_id: str, payload: Dict[str, Any]) -> Any:
    # payload should include type-specific fields (e.g., {"paragraph": {...}})
    return request_json("PATCH", f"/blocks/{block_id}", json=payload)


def blocks_delete(block_id: str) -> Any:
    return request_json("DELETE", f"/blocks/{block_id}")
