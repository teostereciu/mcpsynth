from typing import Any, Dict
from server import mcp
from confluence_client import client

@mcp.tool()
def get_labels(page_id: str) -> Dict[str, Any]:
    """Get labels for a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/labels")

@mcp.tool()
def add_labels(page_id: str, labels: list[str]) -> Dict[str, Any]:
    """Add labels to a page."""
    payload = [{"prefix": "global", "name": label} for label in labels]
    return client.request("POST", f"/rest/api/content/{page_id}/label", json=payload)

@mcp.tool()
def remove_label(page_id: str, label: str) -> Dict[str, Any]:
    """Remove a label from a page."""
    return client.request("DELETE", f"/rest/api/content/{page_id}/label/{label}")
