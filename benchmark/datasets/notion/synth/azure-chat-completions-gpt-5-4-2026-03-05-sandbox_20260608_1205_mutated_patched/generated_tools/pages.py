import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"


def _headers() -> Dict[str, str]:
    token = os.getenv("NOTION_API_KEY")
    if not token:
        return {}
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Any:
    headers = _headers()
    if not headers:
        return {"error": "NOTION_API_KEY is not set"}
    try:
        response = requests.request(method, f"{BASE_URL}{path}", headers=headers, params=params, json=json_body, timeout=60)
        if response.status_code >= 400:
            try:
                return {"error": response.json()}
            except Exception:
                return {"error": response.text}
        if not response.text:
            return {"ok": True}
        return response.json()
    except requests.RequestException as exc:
        return {"error": str(exc)}


def retrieve_page(page_id: str, filter_properties: Optional[list[str]] = None) -> Any:
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    return _request("GET", f"/pages/{page_id}", params=params or None)


def create_page(parent: Dict[str, Any], properties: Optional[Dict[str, Any]] = None, children: Optional[list[Dict[str, Any]]] = None, content: Optional[str] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, template: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent}
    if properties is not None:
        body["properties"] = properties
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
    return _request("POST", "/pages", json_body=body)


def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None, is_locked: Optional[bool] = None, template: Optional[Dict[str, Any]] = None, erase_content: Optional[bool] = None, children: Optional[list[Dict[str, Any]]] = None) -> Any:
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    if template is not None:
        body["template"] = template
    if erase_content is not None:
        body["erase_content"] = erase_content
    if children is not None:
        body["children"] = children
    return _request("PATCH", f"/pages/{page_id}", json_body=body)


def trash_page(page_id: str) -> Any:
    return update_page(page_id=page_id, in_trash=True)


def restore_page(page_id: str) -> Any:
    return update_page(page_id=page_id, in_trash=False)


def retrieve_page_property(page_id: str, property_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", f"/pages/{page_id}/properties/{property_id}", params=params or None)


def move_page(page_id: str, parent: Dict[str, Any]) -> Any:
    return _request("POST", f"/pages/{page_id}/move", json_body={"parent": parent})
