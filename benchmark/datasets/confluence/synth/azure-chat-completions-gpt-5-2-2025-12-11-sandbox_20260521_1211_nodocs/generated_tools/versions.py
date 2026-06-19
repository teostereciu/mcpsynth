from typing import Any, Dict

from .client import ConfluenceClient


def v1_list_page_versions(page_id: str, *, limit: int = 25, start: int = 0) -> Any:
    """GET /rest/api/content/{id}/version"""
    c = ConfluenceClient()
    return c.request(
        "GET",
        f"/rest/api/content/{page_id}/version",
        params={"limit": limit, "start": start},
    )


def v1_get_page_version(page_id: str, version_number: int) -> Any:
    """GET /rest/api/content/{id}/version/{versionNumber}"""
    c = ConfluenceClient()
    return c.request("GET", f"/rest/api/content/{page_id}/version/{version_number}")


def v1_restore_page_version(page_id: str, version_number: int) -> Any:
    """POST /rest/api/content/{id}/version/{versionNumber}/restore"""
    c = ConfluenceClient()
    return c.request(
        "POST",
        f"/rest/api/content/{page_id}/version/{version_number}/restore",
        json={},
        expected=(200, 201, 202),
    )
