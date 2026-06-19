from typing import Any, Dict, Optional
from server import mcp
from confluence_client import client

@mcp.tool()
def get_page_comments(page_id: str, limit: int = 25) -> Dict[str, Any]:
    """Get footer comments for a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/footer-comments", params={"limit": limit})

@mcp.tool()
def get_inline_comments(page_id: str, limit: int = 25) -> Dict[str, Any]:
    """Get inline comments for a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/inline-comments", params={"limit": limit})

@mcp.tool()
def create_footer_comment(page_id: str, body: str) -> Dict[str, Any]:
    """Create a footer comment on a page."""
    payload = {
        "pageId": page_id,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    return client.request("POST", "/api/v2/footer-comments", json=payload)

@mcp.tool()
def create_inline_comment(page_id: str, body: str, inline_marker_ref: str) -> Dict[str, Any]:
    """Create an inline comment on a page."""
    payload = {
        "pageId": page_id,
        "body": {
            "representation": "storage",
            "value": body
        },
        "inlineMarkerRef": inline_marker_ref
    }
    return client.request("POST", "/api/v2/inline-comments", json=payload)
