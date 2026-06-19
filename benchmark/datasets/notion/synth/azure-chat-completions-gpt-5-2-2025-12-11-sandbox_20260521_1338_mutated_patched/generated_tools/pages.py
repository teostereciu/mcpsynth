from typing import Any, Dict, List, Optional

from .notion_client import request_json


def pages_retrieve_property_item(page_id: str, property_id: str, *, page_cursor: str | None = None,
                                results_per_page: int | None = None) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}/properties/{property_id}

    Doc: docs/retrieve-a-page-property.md
    """
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["start_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return request_json("GET", f"/pages/{page_id}/properties/{property_id}", params=params)


def pages_move(page_id: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/pages/{page_id}/move

    Doc: docs/move-page.md
    """
    return request_json("POST", f"/pages/{page_id}/move", json={"parent": parent})


def pages_create(parent: Dict[str, Any], properties: Dict[str, Any], *, children: Optional[List[Dict[str, Any]]] = None,
                content_markdown: Optional[str] = None, icon: Optional[Dict[str, Any]] = None,
                cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/pages

    Doc: docs/post-page.md
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
    return request_json("POST", "/pages", json=body)


def pages_retrieve(page_id: str, *, filter_properties: Optional[List[str]] = None) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}

    Doc: docs/retrieve-a-page.md
    """
    params: Dict[str, Any] = {}
    if filter_properties:
        # Notion expects repeated query param: filter_properties[]=...
        params["filter_properties[]"] = filter_properties
    return request_json("GET", f"/pages/{page_id}", params=params)


def pages_update(page_id: str, *, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None,
                cover: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None,
                is_locked: Optional[bool] = None, erase_content: Optional[bool] = None,
                children: Optional[List[Dict[str, Any]]] = None, content_markdown: Optional[str] = None,
                template: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id}

    Doc: docs/patch-page.md (also see docs/archive-a-page.md for in_trash examples)
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
    if is_locked is not None:
        body["is_locked"] = is_locked
    if erase_content is not None:
        body["erase_content"] = erase_content
    if children is not None:
        body["children"] = children
    if content_markdown is not None:
        body["content_markdown"] = content_markdown
    if template is not None:
        body["template"] = template
    return request_json("PATCH", f"/pages/{page_id}", json=body)
