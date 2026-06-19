from typing import Any, Dict
from .notion_client import NotionClient

client = NotionClient()


def create_database(parent: Dict[str, Any], title: Any, properties: Dict[str, Any], icon: Any = None, cover: Any = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return client.request("POST", "/databases", json=body)


def retrieve_database(database_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/databases/{database_id}")


def update_database(database_id: str, title: Any = None, description: Any = None, properties: Dict[str, Any] = None, icon: Any = None, cover: Any = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if description is not None:
        body["description"] = description
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return client.request("PATCH", f"/databases/{database_id}", json=body)


def query_database(database_id: str, filter: Any = None, sorts: Any = None, start_cursor: Any = None, page_size: Any = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return client.request("POST", f"/databases/{database_id}/query", json=body)
