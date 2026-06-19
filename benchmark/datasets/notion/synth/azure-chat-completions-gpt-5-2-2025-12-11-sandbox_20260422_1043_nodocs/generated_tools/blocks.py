from typing import Any, Dict, Optional

from .notion_client import NotionClient


def blocks_retrieve(block_id: str, *, notion_version: str = "2022-06-28") -> Any:
    client = NotionClient(notion_version=notion_version)
    return client.request("GET", f"/blocks/{block_id}")


def blocks_update(block_id: str, block: Dict[str, Any], *, notion_version: str = "2022-06-28") -> Any:
    """Update a block. Provide the block-type payload under `block` (e.g. {"paragraph": {...}})."""
    client = NotionClient(notion_version=notion_version)
    return client.request("PATCH", f"/blocks/{block_id}", json=block)


def blocks_delete(block_id: str, *, notion_version: str = "2022-06-28") -> Any:
    client = NotionClient(notion_version=notion_version)
    return client.request("DELETE", f"/blocks/{block_id}")


def blocks_children_list(
    block_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str = "2022-06-28",
) -> Any:
    client = NotionClient(notion_version=notion_version)
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", f"/blocks/{block_id}/children", params=params)


def blocks_children_append(
    block_id: str,
    children: list,
    *,
    after: Optional[str] = None,
    notion_version: str = "2022-06-28",
) -> Any:
    client = NotionClient(notion_version=notion_version)
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return client.request("PATCH", f"/blocks/{block_id}/children", json=body)
