from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_attachments(
    *,
    limit: int = 25,
    cursor: Optional[str] = None,
    filename: Optional[str] = None,
    media_type: Optional[str] = None,
    status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/attachments"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if filename:
        params["filename"] = filename
    if media_type:
        params["mediaType"] = media_type
    if status:
        params["status"] = status
    if sort:
        params["sort"] = sort
    return client.request("GET", "/api/v2/attachments", params=params)


def list_page_attachments(
    *,
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    filename: Optional[str] = None,
    media_type: Optional[str] = None,
    status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/attachments"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if filename:
        params["filename"] = filename
    if media_type:
        params["mediaType"] = media_type
    if status:
        params["status"] = status
    if sort:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/attachments", params=params)


def get_attachment(
    *,
    attachment_id: str,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_versions: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/attachments/{id}"""
    client = ConfluenceClient.from_env()
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
    return client.request("GET", f"/api/v2/attachments/{attachment_id}", params=params or None)


def delete_attachment(*, attachment_id: int, purge: Optional[bool] = None) -> Dict[str, Any]:
    """DEL /wiki/api/v2/attachments/{id}"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    return client.request("DELETE", f"/api/v2/attachments/{attachment_id}", params=params or None)
