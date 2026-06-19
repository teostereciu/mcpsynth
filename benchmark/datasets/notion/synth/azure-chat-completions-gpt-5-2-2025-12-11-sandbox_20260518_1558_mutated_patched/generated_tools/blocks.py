from typing import Any, Dict, List, Optional

from .http_client import request_json


def blocks_retrieve(block_id: str) -> Dict[str, Any]:
    """GET /blocks/{block_id}"""
    return request_json("GET", f"/blocks/{block_id}")


def blocks_children_list(block_id: str, *, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /blocks/{block_id}/children"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/blocks/{block_id}/children", params=params or None)


def blocks_children_append(block_id: str, *, children: List[Dict[str, Any]], position: Optional[Dict[str, Any]] = None,
                         after: Optional[str] = None) -> Dict[str, Any]:
    """PATCH /blocks/{block_id}/children

    position is the newer API shape. after is legacy; if provided and position is None,
    it will be sent as {"after": after}.
    """
    body: Dict[str, Any] = {"children": children}
    if position is not None:
        body["position"] = position
    elif after is not None:
        body["after"] = after
    return request_json("PATCH", f"/blocks/{block_id}/children", json_body=body)


def blocks_update(block_id: str, *, block: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /blocks/{block_id}"""
    return request_json("PATCH", f"/blocks/{block_id}", json_body=block)


def blocks_delete(block_id: str) -> Dict[str, Any]:
    """DELETE /blocks/{block_id}"""
    return request_json("DELETE", f"/blocks/{block_id}")
