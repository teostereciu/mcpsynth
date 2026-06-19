from typing import Any, Dict, Optional, List

from .http_client import ConfluenceClient


def list_pages(
    *,
    ids: Optional[List[int]] = None,
    space_ids: Optional[List[int]] = None,
    status: Optional[List[str]] = None,
    title: Optional[str] = None,
    sort: Optional[str] = None,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages"""
    params: Dict[str, Any] = {}
    if ids:
        params["id"] = ids
    if space_ids:
        params["space-id"] = space_ids
    if status:
        params["status"] = status
    if title is not None:
        params["title"] = title
    if sort is not None:
        params["sort"] = sort
    if body_format is not None:
        params["body-format"] = body_format
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", "/api/v2/pages", params=params)  # type: ignore[return-value]


def get_page(
    *,
    page_id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    status: Optional[List[str]] = None,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
    include_version: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}"""
    params: Dict[str, Any] = {}
    if body_format is not None:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = get_draft
    if status:
        params["status"] = status
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
    if include_version is not None:
        params["include-version"] = include_version

    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}", params=params)  # type: ignore[return-value]


def create_page(
    *,
    space_id: str,
    title: str,
    body_representation: str = "storage",
    body_value: str,
    parent_id: Optional[str] = None,
    status: str = "current",
    subtype: Optional[str] = None,
    embedded: Optional[bool] = None,
    private: Optional[bool] = None,
    root_level: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/pages"""
    params: Dict[str, Any] = {}
    if embedded is not None:
        params["embedded"] = embedded
    if private is not None:
        params["private"] = private
    if root_level is not None:
        params["root-level"] = root_level

    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "status": status,
        "title": title,
        "body": {"representation": body_representation, "value": body_value},
    }
    if parent_id is not None:
        payload["parentId"] = parent_id
    if subtype is not None:
        payload["subtype"] = subtype

    return ConfluenceClient().request("POST", "/api/v2/pages", params=params, json=payload)  # type: ignore[return-value]


def update_page(
    *,
    page_id: int,
    status: str,
    title: str,
    body_representation: str,
    body_value: str,
    version_number: int,
    version_message: Optional[str] = None,
    owner_id: Optional[str] = None,
    parent_id: Optional[str] = None,
) -> Dict[str, Any]:
    """PUT /wiki/api/v2/pages/{id}"""
    payload: Dict[str, Any] = {
        "id": str(page_id),
        "status": status,
        "title": title,
        "body": {"representation": body_representation, "value": body_value},
        "version": {"number": version_number},
    }
    if version_message is not None:
        payload["version"]["message"] = version_message
    if owner_id is not None:
        payload["ownerId"] = owner_id
    if parent_id is not None:
        payload["parentId"] = parent_id

    return ConfluenceClient().request("PUT", f"/api/v2/pages/{page_id}", json=payload)  # type: ignore[return-value]


def delete_page(*, page_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    """DELETE /wiki/api/v2/pages/{id}"""
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    if draft is not None:
        params["draft"] = draft
    return ConfluenceClient().request("DELETE", f"/api/v2/pages/{page_id}", params=params)  # type: ignore[return-value]
