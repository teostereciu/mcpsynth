from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_properties(
    page_id: int,
    key: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: int = 25,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{page-id}/properties"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if key is not None:
        params["key"] = key
    if cursor is not None:
        params["cursor"] = cursor
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/properties", params=params)


def create_page_property(page_id: int, key: str, value: Any) -> Dict[str, Any]:
    """POST /api/v2/pages/{page-id}/properties"""
    client = ConfluenceClient()
    payload = {"key": key, "value": value}
    return client.request("POST", f"/api/v2/pages/{page_id}/properties", json=payload)


def update_page_property(page_id: int, property_id: int, key: str, value: Any, version_number: int, version_message: Optional[str] = None) -> Dict[str, Any]:
    """PUT /api/v2/pages/{page-id}/properties/{property-id}"""
    client = ConfluenceClient()
    payload: Dict[str, Any] = {"key": key, "value": value, "version": {"number": version_number}}
    if version_message is not None:
        payload["version"]["message"] = version_message
    return client.request("PUT", f"/api/v2/pages/{page_id}/properties/{property_id}", json=payload)


def get_page_property(page_id: int, property_id: int) -> Dict[str, Any]:
    """GET /api/v2/pages/{page-id}/properties/{property-id}"""
    client = ConfluenceClient()
    return client.request("GET", f"/api/v2/pages/{page_id}/properties/{property_id}")


def delete_page_property(page_id: int, property_id: int) -> Dict[str, Any]:
    """DEL /api/v2/pages/{page-id}/properties/{property-id}"""
    client = ConfluenceClient()
    return client.request("DELETE", f"/api/v2/pages/{page_id}/properties/{property_id}")
