from typing import Any, Dict, Optional

from notion_client import NotionClient


def pages_create(parent: Dict[str, Any], properties: Dict[str, Any], *, children: Optional[list] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """POST /pages"""
    client = NotionClient()
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return client.request("POST", "/pages", json=body)


def pages_retrieve(page_id: str) -> Any:
    """GET /pages/{page_id}"""
    client = NotionClient()
    return client.request("GET", f"/pages/{page_id}")


def pages_update(page_id: str, *, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """PATCH /pages/{page_id}"""
    client = NotionClient()
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return client.request("PATCH", f"/pages/{page_id}", json=body)
