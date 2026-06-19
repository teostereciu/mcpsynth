from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_properties(
    *,
    page_id: int,
    key: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{page-id}/properties"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if key is not None:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/properties", params=params)


def create_page_property(*, page_id: int, key: str, value: Any) -> Dict[str, Any]:
    """POST /wiki/api/v2/pages/{page-id}/properties"""
    client = ConfluenceClient.from_env()
    body: Dict[str, Any] = {"key": key, "value": value}
    return client.request(
        "POST",
        f"/api/v2/pages/{page_id}/properties",
        json_body=body,
        content_type="application/json",
    )


def get_page_property(*, page_id: int, property_id: int) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{page-id}/properties/{property-id}"""
    client = ConfluenceClient.from_env()
    return client.request("GET", f"/api/v2/pages/{page_id}/properties/{property_id}")


def update_page_property(
    *,
    page_id: int,
    property_id: int,
    key: str,
    value: Any,
    version_number: int,
    version_message: Optional[str] = None,
) -> Dict[str, Any]:
    """PUT /wiki/api/v2/pages/{page-id}/properties/{property-id}"""
    client = ConfluenceClient.from_env()
    body: Dict[str, Any] = {
        "key": key,
        "value": value,
        "version": {"number": version_number},
    }
    if version_message is not None:
        body["version"]["message"] = version_message
    return client.request(
        "PUT",
        f"/api/v2/pages/{page_id}/properties/{property_id}",
        json_body=body,
        content_type="application/json",
    )


def delete_page_property(*, page_id: int, property_id: int) -> Dict[str, Any]:
    """DEL /wiki/api/v2/pages/{page-id}/properties/{property-id}"""
    client = ConfluenceClient.from_env()
    return client.request("DELETE", f"/api/v2/pages/{page_id}/properties/{property_id}")
