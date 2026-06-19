from typing import Any, Dict, List, Optional

from generated_tools.common import notion_request


def get_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", f"/blocks/{block_id}/children", params=params or None)


def append_block_children(block_id: str, children: List[Dict[str, Any]], position: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"children": children}
    if position is not None:
        body["position"] = position
    return notion_request("PATCH", f"/blocks/{block_id}/children", json_body=body)


def retrieve_block(block_id: str) -> Any:
    return notion_request("GET", f"/blocks/{block_id}")


def update_block(block_id: str, block_fields: Dict[str, Any]) -> Any:
    return notion_request("PATCH", f"/blocks/{block_id}", json_body=block_fields)


def delete_block(block_id: str) -> Any:
    return notion_request("DELETE", f"/blocks/{block_id}")
