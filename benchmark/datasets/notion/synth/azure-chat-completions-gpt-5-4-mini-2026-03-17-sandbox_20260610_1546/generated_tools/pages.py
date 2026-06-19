from typing import Any, Dict, Optional

from .notion_client import NotionClient


client = NotionClient()


def create_page(body: Dict[str, Any]) -> Any:
    return client.request("POST", "/pages", json=body)


def retrieve_page(page_id: str, filter_properties: Optional[str] = None) -> Any:
    params = {"filter_properties": filter_properties} if filter_properties else None
    return client.request("GET", f"/pages/{page_id}", params=params)


def update_page(page_id: str, body: Dict[str, Any]) -> Any:
    return client.request("PATCH", f"/pages/{page_id}", json=body)


def trash_page(page_id: str, in_trash: bool = True) -> Any:
    return update_page(page_id, {"in_trash": in_trash})


def move_page(page_id: str, body: Dict[str, Any]) -> Any:
    return client.request("POST", f"/pages/{page_id}/move", json=body)
