from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_page_versions(page_id: int, *, cursor: Optional[str] = None, max_results: int = 25) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/versions"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if cursor:
        params["cursor"] = cursor
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/versions", params=params)
    return ok_or_error(status, body, headers)


def get_page_version_details(page_id: int, version_number: int) -> Dict[str, Any]:
    """GET /api/v2/pages/{page-id}/versions/{version-number}"""
    c = ConfluenceClient()
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")
    return ok_or_error(status, body, headers)
