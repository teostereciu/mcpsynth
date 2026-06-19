from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_page_versions(
    page_id: int,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/versions"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if cursor is not None:
        params["cursor"] = cursor
    if body_format is not None:
        params["body-format"] = body_format
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", f"/api/v2/pages/{page_id}/versions", params=params)


def get_page_version_details(page_id: int, version_number: int) -> Dict[str, Any]:
    """GET /api/v2/pages/{page-id}/versions/{version-number}"""
    client = ConfluenceClient()
    return client.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")
