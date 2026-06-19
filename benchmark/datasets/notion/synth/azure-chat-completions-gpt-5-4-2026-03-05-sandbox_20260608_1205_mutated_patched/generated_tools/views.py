from typing import Any, Dict, Optional

from generated_tools.pages import _request


def create_view(data_source_id: str, name: str, view_type: str, database_id: Optional[str] = None, view_id: Optional[str] = None, create_database: Optional[Dict[str, Any]] = None, filter_obj: Optional[Dict[str, Any]] = None, sorts: Optional[list[Dict[str, Any]]] = None, quick_filters: Optional[Dict[str, Any]] = None, config: Optional[Dict[str, Any]] = None, position: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"data_source_id": data_source_id, "name": name, "type": view_type}
    if database_id is not None:
        body["database_id"] = database_id
    if view_id is not None:
        body["view_id"] = view_id
    if create_database is not None:
        body["create_database"] = create_database
    if filter_obj is not None:
        body["filter"] = filter_obj
    if sorts is not None:
        body["sorts"] = sorts
    if quick_filters is not None:
        body["quick_filters"] = quick_filters
    if config is not None:
        body["config"] = config
    if position is not None:
        body["position"] = position
    return _request("POST", "/views", json_body=body)


def retrieve_view(view_id: str) -> Any:
    return _request("GET", f"/views/{view_id}")


def update_view(view_id: str, name: Optional[str] = None, filter_obj: Optional[Dict[str, Any]] = None, sorts: Optional[list[Dict[str, Any]]] = None, quick_filters: Optional[Dict[str, Any]] = None, config: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if filter_obj is not None:
        body["filter"] = filter_obj
    if sorts is not None:
        body["sorts"] = sorts
    if quick_filters is not None:
        body["quick_filters"] = quick_filters
    if config is not None:
        body["config"] = config
    return _request("PATCH", f"/views/{view_id}", json_body=body)


def delete_view(view_id: str) -> Any:
    return _request("DELETE", f"/views/{view_id}")
