from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_page_properties(page_id: int, *, key: Optional[str] = None, cursor: Optional[str] = None, max_results: int = 25) -> Dict[str, Any]:
    """GET /api/v2/pages/{page-id}/properties"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if key:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/properties", params=params)
    return ok_or_error(status, body, headers)


def create_page_property(page_id: int, *, key: str, value: Any) -> Dict[str, Any]:
    """POST /api/v2/pages/{page-id}/properties"""
    c = ConfluenceClient()
    payload = {"key": key, "value": value}
    status, body, headers = c.request("POST", f"/api/v2/pages/{page_id}/properties", json_body=payload)
    return ok_or_error(status, body, headers)


def get_page_property(page_id: int, property_id: int) -> Dict[str, Any]:
    """GET /api/v2/pages/{page-id}/properties/{property-id}"""
    c = ConfluenceClient()
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/properties/{property_id}")
    return ok_or_error(status, body, headers)


def update_page_property(page_id: int, property_id: int, *, key: str, value: Any, version_number: int, version_message: Optional[str] = None) -> Dict[str, Any]:
    """PUT /api/v2/pages/{page-id}/properties/{property-id}"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {"key": key, "value": value, "version": {"number": version_number}}
    if version_message:
        payload["version"]["message"] = version_message
    status, body, headers = c.request("PUT", f"/api/v2/pages/{page_id}/properties/{property_id}", json_body=payload)
    return ok_or_error(status, body, headers)


def delete_page_property(page_id: int, property_id: int) -> Dict[str, Any]:
    """DELETE /api/v2/pages/{page-id}/properties/{property-id}"""
    c = ConfluenceClient()
    status, body, headers = c.request("DELETE", f"/api/v2/pages/{page_id}/properties/{property_id}")
    return ok_or_error(status, body, headers)
