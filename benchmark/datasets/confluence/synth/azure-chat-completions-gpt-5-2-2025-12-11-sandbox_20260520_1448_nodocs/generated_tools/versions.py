from typing import Any, Dict

from .http import confluence_request


def list_page_versions(page_id: int, limit: int = 25, start: int = 0) -> Dict[str, Any]:
    return confluence_request(
        "GET",
        f"/rest/api/content/{page_id}/version",
        params={"limit": limit, "start": start},
    )


def get_page_version(page_id: int, version_number: int) -> Dict[str, Any]:
    return confluence_request("GET", f"/rest/api/content/{page_id}/version/{version_number}")


def restore_page_version(page_id: int, version_number: int) -> Dict[str, Any]:
    return confluence_request("POST", f"/rest/api/content/{page_id}/version/{version_number}/restore")
