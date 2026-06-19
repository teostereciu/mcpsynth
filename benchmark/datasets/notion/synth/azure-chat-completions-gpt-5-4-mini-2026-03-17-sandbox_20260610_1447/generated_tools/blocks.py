from typing import Any, Dict
from .notion_client import NotionClient

client = NotionClient()


def retrieve_block(block_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/blocks/{block_id}")


def list_block_children(block_id: str, start_cursor: Any = None, page_size: Any = None) -> Dict[str, Any]:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", f"/blocks/{block_id}/children", params=params or None)


def append_block_children(block_id: str, children: Any) -> Dict[str, Any]:
    return client.request("PATCH", f"/blocks/{block_id}/children", json={"children": children})


def update_block(block_id: str, **kwargs) -> Dict[str, Any]:
    return client.request("PATCH", f"/blocks/{block_id}", json=kwargs)


def delete_block(block_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/blocks/{block_id}")
