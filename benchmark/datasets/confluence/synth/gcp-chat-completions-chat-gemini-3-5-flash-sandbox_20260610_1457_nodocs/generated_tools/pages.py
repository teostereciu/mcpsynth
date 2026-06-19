from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def create_page(
    client: ConfluenceClient,
    title: str,
    space_key: Optional[str] = None,
    parent_id: Optional[str] = None,
    body: str = "",
    representation: str = "storage"
) -> Dict[str, Any]:
    """
    Create a new page in Confluence.
    
    Args:
        title: Title of the page.
        space_key: Key of the space (defaults to CONFLUENCE_SPACE_KEY env var).
        parent_id: Optional ID of the parent page.
        body: HTML/Storage or ADF content of the page.
        representation: Format of the body ('storage' for HTML, 'atlas_doc_format' for ADF).
    """
    key = space_key or client.default_space_key
    if not key:
        return {"error": "Space key is required (either space_key parameter or CONFLUENCE_SPACE_KEY env var)."}
    
    space_id = client.resolve_space_id(key)
    if isinstance(space_id, dict) and "error" in space_id:
        return space_id
    
    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": representation,
            "value": body
        }
    }
    if parent_id:
        payload["parentId"] = parent_id
        
    return client.post("/api/v2/pages", json_data=payload)

def get_page(client: ConfluenceClient, page_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """
    Get details of a specific page.
    
    Args:
        page_id: Numeric ID of the page.
        body_format: Format of the body to return ('storage', 'atlas_doc_format', 'view', etc.).
    """
    return client.get(f"/api/v2/pages/{page_id}", params={"body-format": body_format})

def update_page(
    client: ConfluenceClient,
    page_id: str,
    title: str,
    body: str,
    representation: str = "storage",
    version_number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Update an existing page.
    
    Args:
        page_id: Numeric ID of the page.
        title: New title of the page.
        body: New content of the page.
        representation: Format of the body ('storage' or 'atlas_doc_format').
        version_number: Optional version number. If not provided, the current version is fetched and incremented.
    """
    if version_number is None:
        current_page = client.get(f"/api/v2/pages/{page_id}")
        if "error" in current_page:
            return {"error": f"Failed to fetch current page version: {current_page['error']}"}
        version_number = current_page.get("version", {}).get("number", 0) + 1
        
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": representation,
            "value": body
        },
        "version": {
            "number": version_number,
            "message": "Updated via MCP"
        }
    }
    return client.put(f"/api/v2/pages/{page_id}", json_data=payload)

def delete_page(client: ConfluenceClient, page_id: str) -> Dict[str, Any]:
    """
    Delete a page.
    
    Args:
        page_id: Numeric ID of the page to delete.
    """
    return client.delete(f"/api/v2/pages/{page_id}")

def get_page_children(client: ConfluenceClient, page_id: str, limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
    """
    Get child pages of a page.
    
    Args:
        page_id: Numeric ID of the parent page.
        limit: Maximum number of children to return.
        cursor: Cursor for pagination.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.get(f"/api/v2/pages/{page_id}/children", params=params)

def get_page_ancestors(client: ConfluenceClient, page_id: str) -> Dict[str, Any]:
    """
    Get ancestors of a page (ordered from root down to parent).
    
    Args:
        page_id: Numeric ID of the page.
    """
    # Using v1 endpoint as it returns ancestors in a single call
    res = client.get(f"/rest/api/content/{page_id}", params={"expand": "ancestors"})
    if "error" in res:
        return res
    return {"ancestors": res.get("ancestors", [])}

def move_page(client: ConfluenceClient, page_id: str, parent_id: str) -> Dict[str, Any]:
    """
    Move a page to be a child of another page.
    
    Args:
        page_id: Numeric ID of the page to move.
        parent_id: Numeric ID of the new parent page.
    """
    # Fetch current page details to construct the update payload
    current_page = client.get(f"/api/v2/pages/{page_id}", params={"body-format": "storage"})
    if "error" in current_page:
        return {"error": f"Failed to fetch page details: {current_page['error']}"}
    
    version_number = current_page.get("version", {}).get("number", 0) + 1
    title = current_page.get("title", "")
    body_val = current_page.get("body", {}).get("storage", {}).get("value", "")
    
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "parentId": parent_id,
        "body": {
            "representation": "storage",
            "value": body_val
        },
        "version": {
            "number": version_number,
            "message": "Moved page via MCP"
        }
    }
    return client.put(f"/api/v2/pages/{page_id}", json_data=payload)
