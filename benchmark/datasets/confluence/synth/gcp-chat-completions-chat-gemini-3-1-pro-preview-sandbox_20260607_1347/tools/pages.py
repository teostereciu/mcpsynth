from typing import Any, Dict, Optional
from server import mcp
from confluence_client import client

@mcp.tool()
def get_pages(space_id: Optional[str] = None, title: Optional[str] = None, limit: int = 25) -> Dict[str, Any]:
    """Get pages, optionally filtered by space_id or title."""
    params = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    if title:
        params["title"] = title
    return client.request("GET", "/api/v2/pages", params=params)

@mcp.tool()
def get_page_by_id(page_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """Get a page by its ID."""
    return client.request("GET", f"/api/v2/pages/{page_id}", params={"body-format": body_format})

@mcp.tool()
def create_page(space_id: str, title: str, body: str, parent_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a new page."""
    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    if parent_id:
        payload["parentId"] = parent_id
    return client.request("POST", "/api/v2/pages", json=payload)

@mcp.tool()
def update_page(page_id: str, space_id: str, title: str, body: str, version_number: int) -> Dict[str, Any]:
    """Update an existing page."""
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "spaceId": space_id,
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    return client.request("PUT", f"/api/v2/pages/{page_id}", json=payload)

@mcp.tool()
def delete_page(page_id: str) -> Dict[str, Any]:
    """Delete a page."""
    return client.request("DELETE", f"/api/v2/pages/{page_id}")

@mcp.tool()
def get_page_children(page_id: str, limit: int = 25) -> Dict[str, Any]:
    """Get children of a page."""
    return client.request("GET", f"/api/v1/content/{page_id}/child/page", params={"limit": limit})

@mcp.tool()
def get_page_ancestors(page_id: str) -> Dict[str, Any]:
    """Get ancestors of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/ancestors")

@mcp.tool()
def move_page(page_id: str, target_id: str, position: str = "append") -> Dict[str, Any]:
    """Move a page to a new parent or position."""
    # v1 API is typically used for moving pages
    payload = {
        "pageId": target_id,
        "position": position
    }
    return client.request("PUT", f"/api/v1/content/{page_id}/move/{position}/{target_id}")
