from typing import Any, Dict, Optional

from .notion_client import NotionClient


def get_page(page_id: str, *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    """Retrieve a page."""
    client = client or NotionClient()
    data, err = client.request("GET", f"/pages/{page_id}")
    return err or data  # type: ignore[return-value]


def create_page(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    *,
    children: Optional[list] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    """Create a page."""
    client = client or NotionClient()
    payload: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        payload["children"] = children
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    data, err = client.request("POST", "/pages", json=payload)
    return err or data  # type: ignore[return-value]


def update_page(
    page_id: str,
    *,
    properties: Optional[Dict[str, Any]] = None,
    archived: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    """Update page properties / archive state."""
    client = client or NotionClient()
    payload: Dict[str, Any] = {}
    if properties is not None:
        payload["properties"] = properties
    if archived is not None:
        payload["archived"] = archived
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    data, err = client.request("PATCH", f"/pages/{page_id}", json=payload)
    return err or data  # type: ignore[return-value]


def archive_page(page_id: str, *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    """Archive a page (sets archived=true)."""
    return update_page(page_id, archived=True, client=client)
