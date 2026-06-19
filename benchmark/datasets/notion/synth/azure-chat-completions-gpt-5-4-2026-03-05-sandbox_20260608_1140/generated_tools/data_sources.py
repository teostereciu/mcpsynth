from typing import Any, Dict, List, Optional

from generated_tools.common import notion_request


def create_data_source(parent: Dict[str, Any], properties: Dict[str, Any], title: Optional[List[Dict[str, Any]]] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if title is not None:
        body["title"] = title
    return notion_request("POST", "/data_sources", json_body=body)


def retrieve_data_source(data_source_id: str) -> Any:
    return notion_request("GET", f"/data_sources/{data_source_id}")


def update_data_source(data_source_id: str, title: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None, parent: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    if in_trash is not None:
        body["in_trash"] = in_trash
    if parent is not None:
        body["parent"] = parent
    return notion_request("PATCH", f"/data_sources/{data_source_id}", json_body=body)


def list_data_source_templates(data_source_id: str, name: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if name is not None:
        params["name"] = name
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", f"/data_sources/{data_source_id}/templates", params=params or None)
