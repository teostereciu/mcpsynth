from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_properties(
    *,
    page_id: int,
    key: Optional[str] = None,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{page-id}/properties"""
    params: Dict[str, Any] = {}
    if key is not None:
        params["key"] = key
    if sort is not None:
        params["sort"] = sort
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}/properties", params=params)  # type: ignore[return-value]


def create_page_property(*, page_id: int, key: str, value: Any) -> Dict[str, Any]:
    """POST /wiki/api/v2/pages/{page-id}/properties"""
    payload = {"key": key, "value": value}
    return ConfluenceClient().request("POST", f"/api/v2/pages/{page_id}/properties", json=payload)  # type: ignore[return-value]


def get_page_property(*, page_id: int, property_id: int) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{page-id}/properties/{property-id}"""
    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}/properties/{property_id}")  # type: ignore[return-value]


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
    payload: Dict[str, Any] = {
        "key": key,
        "value": value,
        "version": {"number": version_number},
    }
    if version_message is not None:
        payload["version"]["message"] = version_message

    return ConfluenceClient().request(
        "PUT",
        f"/api/v2/pages/{page_id}/properties/{property_id}",
        json=payload,
    )  # type: ignore[return-value]


def delete_page_property(*, page_id: int, property_id: int) -> Dict[str, Any]:
    """DELETE /wiki/api/v2/pages/{page-id}/properties/{property-id}"""
    return ConfluenceClient().request("DELETE", f"/api/v2/pages/{page_id}/properties/{property_id}")  # type: ignore[return-value]
