from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_pages(
    space_id: Optional[int] = None,
    title: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
    ids: Optional[list[int]] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if space_id is not None:
        params["space-id"] = [space_id]
    if title is not None:
        params["title"] = title
    if content_status is not None:
        params["content_status"] = content_status
    if cursor is not None:
        params["cursor"] = cursor
    if body_format is not None:
        params["body-format"] = body_format
    if sort is not None:
        params["sort"] = sort
    if ids is not None:
        params["id"] = ids
    return client.request("GET", "/api/v2/pages", params=params)


def get_page(
    page_id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    content_status: Optional[list[str]] = None,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if body_format is not None:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = get_draft
    if content_status is not None:
        params["content_status"] = content_status
    if version is not None:
        params["version"] = version
    if include_labels is not None:
        params["include-labels"] = include_labels
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_likes is not None:
        params["include-likes"] = include_likes
    if include_versions is not None:
        params["include-versions"] = include_versions
    return client.request("GET", f"/api/v2/pages/{page_id}", params=params)


def create_page(
    space_id: str,
    title: str,
    body_representation: str,
    body_value: str,
    parent_id: Optional[str] = None,
    content_status: str = "current",
    subtype: Optional[str] = None,
    embedded: Optional[bool] = None,
    private: Optional[bool] = None,
    root_level: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /api/v2/pages"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if embedded is not None:
        params["embedded"] = embedded
    if private is not None:
        params["private"] = private
    if root_level is not None:
        params["root-level"] = root_level

    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "content_status": content_status,
        "title": title,
        "body": {"representation": body_representation, "value": body_value},
    }
    if parent_id is not None:
        payload["parentId"] = parent_id
    if subtype is not None:
        payload["subtype"] = subtype

    return client.request("POST", "/api/v2/pages", params=params, json=payload)


def update_page(
    page_id: int,
    title: str,
    body_representation: str,
    body_value: str,
    version_number: int,
    version_message: Optional[str] = None,
    content_status: str = "current",
) -> Dict[str, Any]:
    """PUT /api/v2/pages/{id}"""
    client = ConfluenceClient()
    payload: Dict[str, Any] = {
        "id": str(page_id),
        "content_status": content_status,
        "title": title,
        "body": {"representation": body_representation, "value": body_value},
        "version": {"number": version_number},
    }
    if version_message is not None:
        payload["version"]["message"] = version_message
    return client.request("PUT", f"/api/v2/pages/{page_id}", json=payload)


def delete_page(page_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    """DEL /api/v2/pages/{id}"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    if draft is not None:
        params["draft"] = draft
    return client.request("DELETE", f"/api/v2/pages/{page_id}", params=params)


def update_page_title(page_id: int, title: str, content_status: str = "current") -> Dict[str, Any]:
    """PUT /api/v2/pages/{id}/title"""
    client = ConfluenceClient()
    payload = {"content_status": content_status, "title": title}
    return client.request("PUT", f"/api/v2/pages/{page_id}/title", json=payload)
