from typing import Any, Dict
from server import mcp
from confluence_client import client

@mcp.tool()
def get_content_properties(page_id: str, limit: int = 25) -> Dict[str, Any]:
    """Get content properties for a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/properties", params={"limit": limit})

@mcp.tool()
def get_content_property(page_id: str, property_id: str) -> Dict[str, Any]:
    """Get a specific content property."""
    return client.request("GET", f"/api/v2/pages/{page_id}/properties/{property_id}")

@mcp.tool()
def create_content_property(page_id: str, key: str, value: Any) -> Dict[str, Any]:
    """Create a content property."""
    payload = {
        "key": key,
        "value": value
    }
    return client.request("POST", f"/api/v2/pages/{page_id}/properties", json=payload)

@mcp.tool()
def update_content_property(page_id: str, property_id: str, key: str, value: Any, version_number: int) -> Dict[str, Any]:
    """Update a content property."""
    payload = {
        "key": key,
        "value": value,
        "version": {
            "number": version_number
        }
    }
    return client.request("PUT", f"/api/v2/pages/{page_id}/properties/{property_id}", json=payload)

@mcp.tool()
def delete_content_property(page_id: str, property_id: str) -> Dict[str, Any]:
    """Delete a content property."""
    return client.request("DELETE", f"/api/v2/pages/{page_id}/properties/{property_id}")
