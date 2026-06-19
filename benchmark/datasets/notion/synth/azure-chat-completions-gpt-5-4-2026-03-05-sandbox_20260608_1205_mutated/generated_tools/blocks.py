from typing import Any, Dict, Optional

from generated_tools.pages import _request


def retrieve_block(block_id: str) -> Any:
    return _request("GET", f"/blocks/{block_id}")


def list_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", f"/blocks/{block_id}/children", params=params or None)


def append_block_children(block_id: str, children: list[Dict[str, Any]], position: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"children": children}
    if position is not None:
        body["position"] = position
    return _request("PATCH", f"/blocks/{block_id}/children", json_body=body)


def update_block(block_id: str, block_type: str, block_payload: Dict[str, Any]) -> Any:
    return _request("PATCH", f"/blocks/{block_id}", json_body={block_type: block_payload})


def delete_block(block_id: str) -> Any:
    return _request("DELETE", f"/blocks/{block_id}")
