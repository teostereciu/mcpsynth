from typing import Any, Dict, Optional
from server import mcp
from confluence_client import client

@mcp.tool()
def get_spaces(keys: Optional[str] = None, type: Optional[str] = None, limit: int = 25) -> Dict[str, Any]:
    """Get spaces."""
    params = {"limit": limit}
    if keys:
        params["keys"] = keys
    if type:
        params["type"] = type
    return client.request("GET", "/api/v2/spaces", params=params)

@mcp.tool()
def get_space_by_id(space_id: str) -> Dict[str, Any]:
    """Get a space by its ID."""
    return client.request("GET", f"/api/v2/spaces/{space_id}")

@mcp.tool()
def create_space(key: str, name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a new space."""
    payload = {
        "key": key,
        "name": name
    }
    if description:
        payload["description"] = {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
    return client.request("POST", "/rest/api/space", json=payload)

@mcp.tool()
def delete_space(space_key: str) -> Dict[str, Any]:
    """Delete a space."""
    return client.request("DELETE", f"/rest/api/space/{space_key}")
