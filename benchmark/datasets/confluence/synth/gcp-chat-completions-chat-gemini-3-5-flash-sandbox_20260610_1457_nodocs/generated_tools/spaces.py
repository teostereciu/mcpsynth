from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def list_spaces(client: ConfluenceClient, limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
    """
    List all spaces in Confluence.
    
    Args:
        limit: Maximum number of spaces to return (default 20).
        cursor: Cursor for pagination.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.get("/api/v2/spaces", params=params)

def get_space(client: ConfluenceClient, space_id_or_key: str) -> Dict[str, Any]:
    """
    Get details of a specific space by its ID or key.
    
    Args:
        space_id_or_key: The numeric ID of the space or its key (e.g., 'SYNTH').
    """
    if space_id_or_key.isdigit():
        res = client.get(f"/api/v2/spaces/{space_id_or_key}")
        if "error" not in res:
            return res
    
    res = client.get("/api/v2/spaces", params={"keys": space_id_or_key})
    if "error" in res:
        return res
    
    results = res.get("results", [])
    if not results:
        return {"error": f"Space '{space_id_or_key}' not found."}
    return results[0]

def create_space(client: ConfluenceClient, key: str, name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new space.
    
    Args:
        key: Unique key for the space (e.g., 'SYNTH').
        name: Name of the space.
        description: Optional description of the space.
    """
    body = {
        "key": key,
        "name": name
    }
    if description:
        body["description"] = {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
    return client.post("/api/v2/spaces", json_data=body)

def delete_space(client: ConfluenceClient, space_id: str) -> Dict[str, Any]:
    """
    Delete a space by its numeric ID.
    
    Args:
        space_id: The numeric ID of the space to delete.
    """
    return client.delete(f"/api/v2/spaces/{space_id}")
