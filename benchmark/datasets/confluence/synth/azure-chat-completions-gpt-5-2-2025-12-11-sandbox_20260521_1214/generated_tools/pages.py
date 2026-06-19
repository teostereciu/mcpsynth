from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_pages(
    *,
    space_id: Optional[int] = None,
    title: Optional[str] = None,
    status: Optional[list[str]] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if title:
        params["title"] = title
    if sort:
        params["sort"] = sort
    if body_format:
        params["body-format"] = body_format
    if space_id is not None:
        params["space-id"] = [space_id]
    if status:
        params["status"] = status
    return client.request("GET", "/api/v2/pages", params=params)


def get_page(
    *,
    page_id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
    version: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if body_format:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = get_draft
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
    if version is not None:
        params["version"] = version
    return client.request("GET", f"/api/v2/pages/{page_id}", params=params)


def create_page(
    *,
    space_id: int,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    parent_id: Optional[int] = None,
    status: str = "current",
    subtype: Optional[str] = None,
    embedded: Optional[bool] = None,
    private: Optional[bool] = None,
    root_level: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/pages"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if embedded is not None:
        params["embedded"] = embedded
    if private is not None:
        params["private"] = private
    if root_level is not None:
        params["root-level"] = root_level

    body: Dict[str, Any] = {
        "spaceId": str(space_id),
        "status": status,
        "title": title,
        "body": {"representation": body_representation, "value": body_value},
    }
    if parent_id is not None:
        body["parentId"] = str(parent_id)
    if subtype is not None:
        body["subtype"] = subtype

    return client.request(
        "POST",
        "/api/v2/pages",
        params=params or None,
        json_body=body,
        content_type="application/json",
    )


def update_page(
    *,
    page_id: int,
    title: str,
    body_value: str,
    version_number: int,
    status: str = "current",
    body_representation: str = "storage",
    version_message: Optional[str] = None,
) -> Dict[str, Any]:
    """PUT /wiki/api/v2/pages/{id}"""
    client = ConfluenceClient.from_env()
    body: Dict[str, Any] = {
        "id": str(page_id),
        "status": status,
        "title": title,
        "body": {"representation": body_representation, "value": body_value},
        "version": {"number": version_number},
    }
    if version_message is not None:
        body["version"]["message"] = version_message

    return client.request(
        "PUT",
        f"/api/v2/pages/{page_id}",
        json_body=body,
        content_type="application/json",
    )


def delete_page(*, page_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    """DEL /wiki/api/v2/pages/{id}"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    if draft is not None:
        params["draft"] = draft
    return client.request("DELETE", f"/api/v2/pages/{page_id}", params=params or None, accept="application/json")
