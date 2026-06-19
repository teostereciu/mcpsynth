from typing import Any, Dict, List, Optional

from .notion_client import NotionClient, omit_none


def pages_create(
    *,
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    children: Optional[List[Dict[str, Any]]] = None,
    content_markdown: Optional[str] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    template: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /pages

    Source: docs/post-page.md

    Notes:
      - content_markdown is mutually exclusive with children.
    """
    if content_markdown is not None and children is not None:
        return {"error": "content_markdown is mutually exclusive with children"}

    body: Dict[str, Any] = omit_none(
        {
            "parent": parent,
            "properties": properties,
            "children": children,
            "content_markdown": content_markdown,
            "icon": icon,
            "cover": cover,
            "template": template,
        }
    )
    return NotionClient().request("POST", "/pages", json=body)


def pages_retrieve(
    *,
    page_id: str,
    filter_properties: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """GET /pages/{page_id}

    Source: docs/retrieve-a-page.md
    """
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    return NotionClient().request("GET", f"/pages/{page_id}", params=params or None)


def pages_update(
    *,
    page_id: str,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
    archived: Optional[bool] = None,
    locked: Optional[bool] = None,
    erase_content: Optional[bool] = None,
    children: Optional[List[Dict[str, Any]]] = None,
    content_markdown: Optional[str] = None,
    template: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """PATCH /pages/{page_id}

    Source: docs/patch-page.md

    Notes:
      - content_markdown is mutually exclusive with children.
    """
    if content_markdown is not None and children is not None:
        return {"error": "content_markdown is mutually exclusive with children"}

    body: Dict[str, Any] = omit_none(
        {
            "properties": properties,
            "icon": icon,
            "cover": cover,
            "in_trash": in_trash,
            "archived": archived,
            "locked": locked,
            "erase_content": erase_content,
            "children": children,
            "content_markdown": content_markdown,
            "template": template,
        }
    )
    return NotionClient().request("PATCH", f"/pages/{page_id}", json=body)
