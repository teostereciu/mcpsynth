from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_versions(
    *,
    page_id: int,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = 25,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{id}/versions"""
    params: Dict[str, Any] = {}
    if body_format is not None:
        params["body-format"] = body_format
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit
    if sort is not None:
        params["sort"] = sort

    return ConfluenceClient().request("GET", f"/api/v2/pages/{page_id}/versions", params=params)  # type: ignore[return-value]


def get_page_version_details(*, page_id: int, version_number: int) -> Dict[str, Any]:
    """GET /wiki/api/v2/pages/{page-id}/versions/{version-number}"""
    return ConfluenceClient().request(
        "GET",
        f"/api/v2/pages/{page_id}/versions/{version_number}",
    )  # type: ignore[return-value]


def restore_content_version(
    *,
    content_id: str,
    version_number: int,
    message: Optional[str] = None,
    restore_title: Optional[bool] = None,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """POST /wiki/rest/api/content/{id}/version"""
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand

    payload: Dict[str, Any] = {
        "operationKey": "restore",
        "params": {"versionNumber": version_number},
    }
    if message is not None:
        payload["params"]["message"] = message
    if restore_title is not None:
        payload["params"]["restoreTitle"] = restore_title

    return ConfluenceClient().request(
        "POST",
        f"/rest/api/content/{content_id}/version",
        params=params,
        json=payload,
    )  # type: ignore[return-value]
