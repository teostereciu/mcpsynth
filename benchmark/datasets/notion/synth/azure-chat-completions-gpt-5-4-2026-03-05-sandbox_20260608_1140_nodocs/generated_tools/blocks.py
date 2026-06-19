from typing import Any, Dict, List, Optional

from generated_tools.notion_client import client


def retrieve_block(block_id: str) -> Any:
    return client.request("GET", f"/blocks/{block_id}")


def retrieve_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", f"/blocks/{block_id}/children", params=params or None)


def append_block_children(block_id: str, children: List[Dict[str, Any]], after: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return client.request("PATCH", f"/blocks/{block_id}/children", json_body=body)


def update_block(block_id: str, block_type: str, block_data: Dict[str, Any], archived: Optional[bool] = None, in_trash: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {block_type: block_data}
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    return client.request("PATCH", f"/blocks/{block_id}", json_body=body)


def delete_block(block_id: str) -> Any:
    return client.request("DELETE", f"/blocks/{block_id}")
