from typing import Any, Dict, List, Optional

from .http_client import request_json


def pages_create(*, parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[List[Dict[str, Any]]] = None,
                content: Optional[str] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                template: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /pages"""
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if content is not None:
        body["content"] = content
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if template is not None:
        body["template"] = template
    return request_json("POST", "/pages", json_body=body)


def pages_retrieve(page_id: str, *, filter_properties: Optional[list] = None) -> Dict[str, Any]:
    """GET /pages/{page_id}"""
    params: Dict[str, Any] = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties
    return request_json("GET", f"/pages/{page_id}", params=params or None)


def pages_update(page_id: str, *, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None,
                cover: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, in_trash: Optional[bool] = None) -> Dict[str, Any]:
    """PATCH /pages/{page_id}"""
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    return request_json("PATCH", f"/pages/{page_id}", json_body=body)


def pages_archive(page_id: str) -> Dict[str, Any]:
    """PATCH /pages/{page_id} (archive/trash)"""
    return pages_update(page_id, in_trash=True)


def pages_restore(page_id: str) -> Dict[str, Any]:
    """PATCH /pages/{page_id} (restore from trash)"""
    return pages_update(page_id, in_trash=False)


def pages_retrieve_property_item(page_id: str, property_id: str, *, start_cursor: Optional[str] = None,
                                page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /pages/{page_id}/properties/{property_id}"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/pages/{page_id}/properties/{property_id}", params=params or None)


def pages_move(page_id: str, *, parent: Dict[str, Any]) -> Dict[str, Any]:
    """POST /pages/{page_id}/move"""
    return request_json("POST", f"/pages/{page_id}/move", json_body={"parent": parent})


def pages_retrieve_markdown(page_id: str, *, include_transcripts: Optional[bool] = None) -> Dict[str, Any]:
    """GET /pages/{page_id}/markdown"""
    params: Dict[str, Any] = {}
    if include_transcripts is not None:
        params["include_transcripts"] = str(include_transcripts).lower()
    return request_json("GET", f"/pages/{page_id}/markdown", params=params or None)


def pages_update_markdown(page_id: str, *, update: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /pages/{page_id}/markdown"""
    return request_json("PATCH", f"/pages/{page_id}/markdown", json_body=update)
