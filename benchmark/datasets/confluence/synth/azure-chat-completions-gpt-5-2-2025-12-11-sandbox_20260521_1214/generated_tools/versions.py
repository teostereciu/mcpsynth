from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_versions(
    *,
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
    body_format: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/versions"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    if body_format:
        params["body-format"] = body_format
    return client.request("GET", f"/api/v2/pages/{page_id}/versions", params=params)


def get_page_version_details(*, page_id: int, version_number: int) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{page-id}/versions/{version-number}"""
    client = ConfluenceClient.from_env()
    return client.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")


def restore_content_version(
    *,
    content_id: str,
    version_number: int,
    message: Optional[str] = None,
    restore_title: bool = True,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """POST /wiki/rest/api/content/{id}/version"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand

    body: Dict[str, Any] = {
        "operationKey": "restore",
        "params": {"versionNumber": version_number, "restoreTitle": restore_title},
    }
    if message is not None:
        body["params"]["message"] = message

    return client.request(
        "POST",
        f"/rest/api/content/{content_id}/version",
        params=params or None,
        json_body=body,
        content_type="application/json",
    )
