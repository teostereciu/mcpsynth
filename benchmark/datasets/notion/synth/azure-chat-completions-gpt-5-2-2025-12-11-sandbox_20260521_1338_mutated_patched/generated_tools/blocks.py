from typing import Any, Dict, List, Optional

from .notion_client import request_json


def blocks_retrieve(block_id: str) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}

    Doc: docs/retrieve-a-block.md
    """
    return request_json("GET", f"/blocks/{block_id}")


def blocks_children_list(block_id: str, *, page_cursor: Optional[str] = None,
                         results_per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /v1/blocks/{block_id}/children

    Doc: docs/get-block-children.md
    """
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["start_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return request_json("GET", f"/blocks/{block_id}/children", params=params)


def blocks_children_append(block_id: str, children: List[Dict[str, Any]], *, position: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}/children

    Doc: docs/patch-block-children.md
    """
    body: Dict[str, Any] = {"children": children}
    if position is not None:
        body["position"] = position
    return request_json("PATCH", f"/blocks/{block_id}/children", json=body)


def blocks_update(block_id: str, block: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /v1/blocks/{block_id}

    Doc: docs/update-a-block.md

    Note: Notion expects type-specific fields at top-level (e.g. {"paragraph": {...}}).
    Pass them via `block`.
    """
    return request_json("PATCH", f"/blocks/{block_id}", json=block)


def blocks_delete(block_id: str) -> Dict[str, Any]:
    """DELETE /v1/blocks/{block_id}

    Doc: docs/delete-a-block.md
    """
    return request_json("DELETE", f"/blocks/{block_id}")
