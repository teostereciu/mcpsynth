from typing import Any, Dict, List, Optional

from .notion_client import NotionClient


def blocks_children_list(
    block_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}/children

    Doc: docs/get-block-children.md
    """
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient()
    return client.request("GET", f"/blocks/{block_id}/children", params=params or None)


def blocks_children_append(
    block_id: str,
    children: List[Dict[str, Any]],
    *,
    position: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}/children

    Doc: docs/patch-block-children.md
    """
    body: Dict[str, Any] = {"children": children}
    if position is not None:
        body["position"] = position
    client = NotionClient()
    return client.request("PATCH", f"/blocks/{block_id}/children", json_body=body)


def blocks_update(block_id: str, **block_fields: Any) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}

    Doc: docs/update-a-block.md

    Pass block-type-specific fields as keyword args, e.g. paragraph={...}, to_do={...}
    """
    if not block_fields:
        return {"error": "No fields provided"}
    client = NotionClient()
    return client.request("PATCH", f"/blocks/{block_id}", json_body=block_fields)


def blocks_delete(block_id: str) -> Dict[str, Any]:
    """DELETE /v1/blocks/{block_id}

    Doc: docs/delete-a-block.md
    """
    client = NotionClient()
    return client.request("DELETE", f"/blocks/{block_id}")


def blocks_retrieve(block_id: str) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}

    Doc: docs/retrieve-a-block.md
    """
    client = NotionClient()
    return client.request("GET", f"/blocks/{block_id}")
