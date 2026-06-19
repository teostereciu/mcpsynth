from typing import Any, Dict, Optional

from .notion_client import NotionClient


def get_block(block_id: str, *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    client = client or NotionClient()
    data, err = client.request("GET", f"/blocks/{block_id}")
    return err or data  # type: ignore[return-value]


def update_block(block_id: str, block: Dict[str, Any], *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    """Update a block. Provide the block-type payload under `block` (e.g. {"paragraph": {...}})."""
    client = client or NotionClient()
    data, err = client.request("PATCH", f"/blocks/{block_id}", json=block)
    return err or data  # type: ignore[return-value]


def delete_block(block_id: str, *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    client = client or NotionClient()
    data, err = client.request("DELETE", f"/blocks/{block_id}")
    return err or data  # type: ignore[return-value]


def list_block_children(
    block_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data, err = client.request("GET", f"/blocks/{block_id}/children", params=params)
    return err or data  # type: ignore[return-value]


def append_block_children(
    block_id: str,
    children: list,
    *,
    after: Optional[str] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    payload: Dict[str, Any] = {"children": children}
    if after is not None:
        payload["after"] = after
    data, err = client.request("PATCH", f"/blocks/{block_id}/children", json=payload)
    return err or data  # type: ignore[return-value]
