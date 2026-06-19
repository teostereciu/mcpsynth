from typing import Any, Dict, List, Optional

from .client import notion_request


def retrieve_page(page_id: str, property_ids: Optional[List[str]] = None) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}

    Args:
        page_id: Notion page ID.
        property_ids: Optional list of property IDs to filter properties in the response.
    """
    params: Dict[str, Any] = {}
    if property_ids:
        params["property_ids"] = ",".join(property_ids)
    return notion_request("GET", f"/pages/{page_id}", params=params or None)


def create_page(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    *,
    children: Optional[List[Dict[str, Any]]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    content_markdown: Optional[str] = None,
    show_child_attributes: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /v1/pages

    Notes:
        - Provide either `children` (Notion block children) OR `content_markdown`.
        - `parent` is typically {"page_id": ...} or {"database_id": ...} or {"data_source_id": ...}.
    """
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if content_markdown is not None:
        body["content_markdown"] = content_markdown
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover

    params: Dict[str, Any] = {}
    if show_child_attributes is not None:
        params["show_child_attributes"] = str(show_child_attributes).lower()

    return notion_request("POST", "/pages", params=params or None, json_body=body)


def update_page(
    page_id: str,
    *,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
    archived: Optional[bool] = None,
    locked: Optional[bool] = None,
    erase_content: Optional[bool] = None,
    children: Optional[List[Dict[str, Any]]] = None,
    content_markdown: Optional[str] = None,
    show_child_attributes: Optional[bool] = None,
) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id}

    Notes:
        - Provide either `children` OR `content_markdown` when adding content.
        - `erase_content=True` clears existing content.
    """
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if archived is not None:
        body["archived"] = archived
    if locked is not None:
        body["locked"] = locked
    if erase_content is not None:
        body["erase_content"] = erase_content
    if children is not None:
        body["children"] = children
    if content_markdown is not None:
        body["content_markdown"] = content_markdown

    params: Dict[str, Any] = {}
    if show_child_attributes is not None:
        params["show_child_attributes"] = str(show_child_attributes).lower()

    return notion_request("PATCH", f"/pages/{page_id}", params=params or None, json_body=body)


def retrieve_page_property_item(
    page_id: str,
    property_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}/properties/{property_id}"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request(
        "GET",
        f"/pages/{page_id}/properties/{property_id}",
        params=params or None,
    )


def trash_page(page_id: str) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id} with {in_trash: true}."""
    return notion_request("PATCH", f"/pages/{page_id}", json_body={"in_trash": True})


def move_page(
    page_id: str,
    parent: Dict[str, Any],
    *,
    show_child_attributes: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /v1/pages/{page_id}/move"""
    params: Dict[str, Any] = {}
    if show_child_attributes is not None:
        params["show_child_attributes"] = str(show_child_attributes).lower()
    return notion_request("POST", f"/pages/{page_id}/move", params=params or None, json_body={"parent": parent})


def restore_page(page_id: str) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id} with {in_trash: false}."""
    return notion_request("PATCH", f"/pages/{page_id}", json_body={"in_trash": False})
