from typing import Any, Dict, Optional

from .notion_client import NotionClient


def get_database(database_id: str, *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    client = client or NotionClient()
    data, err = client.request("GET", f"/databases/{database_id}")
    return err or data  # type: ignore[return-value]


def query_database(
    database_id: str,
    *,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[list] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    payload: Dict[str, Any] = {}
    if filter is not None:
        payload["filter"] = filter
    if sorts is not None:
        payload["sorts"] = sorts
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    if page_size is not None:
        payload["page_size"] = page_size
    data, err = client.request("POST", f"/databases/{database_id}/query", json=payload)
    return err or data  # type: ignore[return-value]


def create_database(
    parent: Dict[str, Any],
    title: list,
    properties: Dict[str, Any],
    *,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    description: Optional[list] = None,
    is_inline: Optional[bool] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    payload: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    if description is not None:
        payload["description"] = description
    if is_inline is not None:
        payload["is_inline"] = is_inline
    data, err = client.request("POST", "/databases", json=payload)
    return err or data  # type: ignore[return-value]


def update_database(
    database_id: str,
    *,
    title: Optional[list] = None,
    properties: Optional[Dict[str, Any]] = None,
    description: Optional[list] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if properties is not None:
        payload["properties"] = properties
    if description is not None:
        payload["description"] = description
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    if is_inline is not None:
        payload["is_inline"] = is_inline
    data, err = client.request("PATCH", f"/databases/{database_id}", json=payload)
    return err or data  # type: ignore[return-value]
