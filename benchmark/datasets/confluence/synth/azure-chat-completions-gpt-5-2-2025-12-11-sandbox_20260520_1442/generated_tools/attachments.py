from typing import Any, Dict, Optional, List

from .http_client import ConfluenceClient


def list_attachments(
    *,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    status: Optional[List[str]] = None,
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/attachments"""
    params: Dict[str, Any] = {}
    if sort is not None:
        params["sort"] = sort
    if cursor is not None:
        params["cursor"] = cursor
    if status:
        params["status"] = status
    if media_type is not None:
        params["mediaType"] = media_type
    if filename is not None:
        params["filename"] = filename
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", "/api/v2/attachments", params=params)  # type: ignore[return-value]


def get_attachment(
    *,
    attachment_id: str,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_versions: Optional[bool] = None,
    include_version: Optional[bool] = None,
    include_collaborators: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/attachments/{id}"""
    params: Dict[str, Any] = {}
    if version is not None:
        params["version"] = version
    if include_labels is not None:
        params["include-labels"] = include_labels
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_versions is not None:
        params["include-versions"] = include_versions
    if include_version is not None:
        params["include-version"] = include_version
    if include_collaborators is not None:
        params["include-collaborators"] = include_collaborators

    return ConfluenceClient().request("GET", f"/api/v2/attachments/{attachment_id}", params=params)  # type: ignore[return-value]


def delete_attachment(*, attachment_id: int, purge: Optional[bool] = None) -> Dict[str, Any]:
    """DELETE /wiki/api/v2/attachments/{id}"""
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    return ConfluenceClient().request("DELETE", f"/api/v2/attachments/{attachment_id}", params=params)  # type: ignore[return-value]


def list_page_attachments(
    *,
    page_id: int,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    status: Optional[List[str]] = None,
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/attachments"""
    params: Dict[str, Any] = {}
    if sort is not None:
        params["sort"] = sort
    if cursor is not None:
        params["cursor"] = cursor
    if status:
        params["status"] = status
    if media_type is not None:
        params["mediaType"] = media_type
    if filename is not None:
        params["filename"] = filename
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}/attachments", params=params)  # type: ignore[return-value]
