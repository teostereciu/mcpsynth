from typing import Any, Dict
from server import mcp
from confluence_client import client

@mcp.tool()
def get_page_versions(page_id: str, limit: int = 25) -> Dict[str, Any]:
    """Get versions of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/versions", params={"limit": limit})

@mcp.tool()
def get_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    """Get a specific version of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")

@mcp.tool()
def restore_page_version(page_id: str, version_number: int, message: str = "") -> Dict[str, Any]:
    """Restore a page to a previous version."""
    payload = {
        "version": {
            "number": version_number,
            "message": message
        }
    }
    return client.request("POST", f"/rest/api/content/{page_id}/version", json=payload)
