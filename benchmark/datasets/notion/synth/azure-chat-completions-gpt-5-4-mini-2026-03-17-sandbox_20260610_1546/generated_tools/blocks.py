from typing import Any, Dict, Optional

from .notion_client import NotionClient


client = NotionClient()


def retrieve_block(block_id: str) -> Any:
    return client.request("GET", f"/blocks/{block_id}")


def list_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", f"/blocks/{block_id}/children", params=params or None)


def append_block_children(block_id: str, body: Dict[str, Any]) -> Any:
    return client.request("PATCH", f"/blocks/{block_id}/children", json=body)


def update_block(block_id: str, body: Dict[str, Any]) -> Any:
    return client.request("PATCH", f"/blocks/{block_id}", json=body)


def delete_block(block_id: str) -> Any:
    return client.request("DELETE", f"/blocks/{block_id}")
