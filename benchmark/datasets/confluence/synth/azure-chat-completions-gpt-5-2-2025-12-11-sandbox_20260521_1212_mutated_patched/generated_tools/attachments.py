from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_attachments(
    cursor: Optional[str] = None,
    max_results: int = 25,
    filename: Optional[str] = None,
    media_type: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/attachments"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if cursor is not None:
        params["cursor"] = cursor
    if filename is not None:
        params["filename"] = filename
    if media_type is not None:
        params["mediaType"] = media_type
    if content_status is not None:
        params["status"] = content_status
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", "/api/v2/attachments", params=params)


def get_attachment(
    attachment_id: str,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_versions: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /api/v2/attachments/{id}"""
    client = ConfluenceClient()
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
    return client.request("GET", f"/api/v2/attachments/{attachment_id}", params=params)


def list_page_attachments(
    page_id: int,
    cursor: Optional[str] = None,
    max_results: int = 25,
    filename: Optional[str] = None,
    media_type: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/attachments"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if cursor is not None:
        params["cursor"] = cursor
    if filename is not None:
        params["filename"] = filename
    if media_type is not None:
        params["mediaType"] = media_type
    if content_status is not None:
        params["status"] = content_status
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/attachments", params=params)


def delete_attachment(attachment_id: int, purge: Optional[bool] = None) -> Dict[str, Any]:
    """DEL /api/v2/attachments/{id}"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    return client.request("DELETE", f"/api/v2/attachments/{attachment_id}", params=params)
