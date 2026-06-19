from typing import Any, Dict, List, Optional

from .notion_client import NotionClient, omit_none


def blocks_retrieve(*, block_id: str) -> Dict[str, Any]:
    """GET /blocks/{block_id}

    Source: docs/retrieve-a-block.md
    """
    return NotionClient().request("GET", f"/blocks/{block_id}")


def blocks_children_list(
    *,
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /blocks/{block_id}/children

    Source: docs/get-block-children.md
    """
    params = omit_none({"start_cursor": start_cursor, "page_size": page_size})
    return NotionClient().request(
        "GET", f"/blocks/{block_id}/children", params=params or None
    )


def blocks_children_append(
    *,
    block_id: str,
    children: List[Dict[str, Any]],
    position: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """PATCH /blocks/{block_id}/children

    Source: docs/patch-block-children.md
    """
    body = omit_none({"children": children, "position": position})
    return NotionClient().request("PATCH", f"/blocks/{block_id}/children", json=body)


def blocks_update(*, block_id: str, **block_fields: Any) -> Dict[str, Any]:
    """PATCH /blocks/{block_id}

    Source: docs/update-a-block.md

    Pass block type payloads as keyword args, e.g. paragraph={...}, heading_1={...}
    """
    if not block_fields:
        return {"error": "no fields provided to update"}
    return NotionClient().request("PATCH", f"/blocks/{block_id}", json=block_fields)


def blocks_delete(*, block_id: str) -> Dict[str, Any]:
    """DELETE /blocks/{block_id}

    Source: docs/delete-a-block.md
    """
    return NotionClient().request("DELETE", f"/blocks/{block_id}")
