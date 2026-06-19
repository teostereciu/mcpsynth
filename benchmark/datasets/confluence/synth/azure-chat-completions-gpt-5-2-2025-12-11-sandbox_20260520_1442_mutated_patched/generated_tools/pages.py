from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_pages(
    *,
    space_ids: Optional[list[int]] = None,
    title: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: int = 25,
) -> Dict[str, Any]:
    """GET /api/v2/pages"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if space_ids:
        params["space-id"] = space_ids
    if title:
        params["title"] = title
    if content_status:
        params["status"] = content_status
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    status, body, headers = c.request("GET", "/api/v2/pages", params=params)
    return ok_or_error(status, body, headers)


def get_page(
    page_id: int,
    *,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_versions: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {}
    if body_format:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = str(get_draft).lower()
    if include_labels is not None:
        params["include-labels"] = str(include_labels).lower()
    if include_properties is not None:
        params["include-properties"] = str(include_properties).lower()
    if include_operations is not None:
        params["include-operations"] = str(include_operations).lower()
    if include_versions is not None:
        params["include-versions"] = str(include_versions).lower()
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}", params=params)
    return ok_or_error(status, body, headers)


def create_page(
    *,
    space_id: str,
    title: str,
    body_storage_value: str,
    parent_id: Optional[str] = None,
    content_status: str = "current",
    embedded: Optional[bool] = None,
    private: Optional[bool] = None,
    root_level: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /api/v2/pages"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {}
    if embedded is not None:
        params["embedded"] = str(embedded).lower()
    if private is not None:
        params["private"] = str(private).lower()
    if root_level is not None:
        params["root-level"] = str(root_level).lower()

    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "status": content_status,
        "title": title,
        "body": {"representation": "storage", "value": body_storage_value},
    }
    if parent_id:
        payload["parentId"] = parent_id

    status, body, headers = c.request("POST", "/api/v2/pages", params=params, json_body=payload)
    return ok_or_error(status, body, headers)


def update_page(
    page_id: int,
    *,
    title: str,
    body_storage_value: str,
    version_number: int,
    version_message: Optional[str] = None,
    content_status: str = "current",
) -> Dict[str, Any]:
    """PUT /api/v2/pages/{id}"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "id": str(page_id),
        "status": content_status,
        "title": title,
        "body": {"representation": "storage", "value": body_storage_value},
        "version": {"number": version_number},
    }
    if version_message:
        payload["version"]["message"] = version_message

    status, body, headers = c.request("PUT", f"/api/v2/pages/{page_id}", json_body=payload)
    return ok_or_error(status, body, headers)


def delete_page(page_id: int, *, purge: bool = False, draft: bool = False) -> Dict[str, Any]:
    """DELETE /api/v2/pages/{id}"""
    c = ConfluenceClient()
    params = {"purge": str(purge).lower(), "draft": str(draft).lower()}
    status, body, headers = c.request("DELETE", f"/api/v2/pages/{page_id}", params=params)
    return ok_or_error(status, body, headers)


def update_page_title(page_id: int, *, title: str, content_status: str = "current") -> Dict[str, Any]:
    """PUT /api/v2/pages/{id}/title"""
    c = ConfluenceClient()
    payload = {"status": content_status, "title": title}
    status, body, headers = c.request("PUT", f"/api/v2/pages/{page_id}/title", json_body=payload)
    return ok_or_error(status, body, headers)
