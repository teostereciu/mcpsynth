from typing import Any, Dict, Optional

from .notion_client import NotionClient


def databases_retrieve(database_id: str, *, notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """GET /databases/{database_id}"""
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("GET", f"/databases/{database_id}")


def databases_query(database_id: str, *, filter: Optional[Dict[str, Any]] = None,
                    sorts: Optional[list] = None, start_cursor: Optional[str] = None,
                    page_size: Optional[int] = None,
                    notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """POST /databases/{database_id}/query"""
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("POST", f"/databases/{database_id}/query", json_body=body)


def databases_create(parent: Dict[str, Any], title: list, properties: Dict[str, Any], *,
                     icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                     notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """POST /databases"""
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("POST", "/databases", json_body=body)


def databases_update(database_id: str, *, title: Optional[list] = None, properties: Optional[Dict[str, Any]] = None,
                     description: Optional[list] = None, icon: Optional[Dict[str, Any]] = None,
                     cover: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None,
                     notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """PATCH /databases/{database_id}"""
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    if description is not None:
        body["description"] = description
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if archived is not None:
        body["archived"] = archived
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("PATCH", f"/databases/{database_id}", json_body=body)
