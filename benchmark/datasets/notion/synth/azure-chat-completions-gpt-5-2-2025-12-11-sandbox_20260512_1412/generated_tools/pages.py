from typing import Any, Dict, List, Optional

from ._client import request_json


def pages_create(parent: Dict[str, Any], properties: Dict[str, Any], *, children: Optional[List[Dict[str, Any]]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """POST /v1/pages"""
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return request_json("POST", "/pages", json_body=body)


def pages_retrieve(page_id: str, *, filter_properties: Optional[List[str]] = None) -> Any:
    """GET /v1/pages/{page_id}"""
    params: Dict[str, Any] = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties
    return request_json("GET", f"/pages/{page_id}", params=params)


def pages_update(page_id: str, *, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """PATCH /v1/pages/{page_id}"""
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return request_json("PATCH", f"/pages/{page_id}", json_body=body)


def pages_archive(page_id: str) -> Any:
    """Convenience: archive a page (PATCH /v1/pages/{page_id} with archived=true)."""
    return pages_update(page_id, archived=True)


def pages_restore(page_id: str) -> Any:
    """Convenience: restore a page (PATCH /v1/pages/{page_id} with archived=false)."""
    return pages_update(page_id, archived=False)


def pages_retrieve_property_item(page_id: str, property_id: str, *, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """GET /v1/pages/{page_id}/properties/{property_id}"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/pages/{page_id}/properties/{property_id}", params=params)


def pages_move(page_id: str, parent: Dict[str, Any]) -> Any:
    """POST /v1/pages/{page_id}/move"""
    return request_json("POST", f"/pages/{page_id}/move", json_body={"parent": parent})
