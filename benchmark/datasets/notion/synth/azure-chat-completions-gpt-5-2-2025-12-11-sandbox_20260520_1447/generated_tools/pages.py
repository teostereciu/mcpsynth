from typing import Any, Dict, List, Optional

from .notion_client import NotionClient


def pages_retrieve(page_id: str, filter_properties: Optional[List[str]] = None) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}

    Doc: docs/retrieve-a-page.md
    """
    client = NotionClient()
    params: Dict[str, Any] = {}
    if filter_properties:
        # Notion expects repeated filter_properties[] query params.
        params["filter_properties"] = filter_properties
    return client.request("GET", f"/pages/{page_id}", params=params or None)


def pages_create(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    *,
    children: Optional[List[Dict[str, Any]]] = None,
    content_markdown: Optional[str] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/pages

    Doc: docs/post-page.md
    """
    if children is not None and content_markdown is not None:
        return {"error": "children and content_markdown are mutually exclusive"}

    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if content_markdown is not None:
        body["content_markdown"] = content_markdown
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover

    client = NotionClient()
    return client.request("POST", "/pages", json_body=body)


def pages_archive(page_id: str) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id} (trash/archive)

    Doc: docs/archive-a-page.md
    """
    client = NotionClient()
    return client.request("PATCH", f"/pages/{page_id}", json_body={"in_trash": True})


def pages_restore(page_id: str) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id} (restore from trash)

    Doc: docs/archive-a-page.md
    """
    client = NotionClient()
    return client.request("PATCH", f"/pages/{page_id}", json_body={"in_trash": False})


def pages_retrieve_property_item(
    page_id: str,
    property_id: str,
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}/properties/{property_id}

    Doc: docs/retrieve-a-page-property.md
    """
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient()
    return client.request("GET", f"/pages/{page_id}/properties/{property_id}", params=params or None)


def pages_move(page_id: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/pages/{page_id}/move

    Doc: docs/move-page.md
    """
    client = NotionClient()
    return client.request("POST", f"/pages/{page_id}/move", json_body={"parent": parent})


def pages_update(
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
    template: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id}

    Doc: docs/patch-page.md
    """
    if children is not None and content_markdown is not None:
        return {"error": "children and content_markdown are mutually exclusive"}

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
    if template is not None:
        body["template"] = template

    client = NotionClient()
    return client.request("PATCH", f"/pages/{page_id}", json_body=body)
