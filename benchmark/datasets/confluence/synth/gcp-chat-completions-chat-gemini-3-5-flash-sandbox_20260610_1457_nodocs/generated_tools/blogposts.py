from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def create_blogpost(
    client: ConfluenceClient,
    title: str,
    space_key: Optional[str] = None,
    body: str = "",
    representation: str = "storage"
) -> Dict[str, Any]:
    """
    Create a new blog post.
    
    Args:
        title: Title of the blog post.
        space_key: Key of the space (defaults to CONFLUENCE_SPACE_KEY env var).
        body: Content of the blog post.
        representation: Format of the body ('storage' or 'atlas_doc_format').
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
    return client.post("/api/v2/blogposts", json_data=payload)

def get_blogpost(client: ConfluenceClient, blogpost_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """
    Get details of a specific blog post.
    
    Args:
        blogpost_id: Numeric ID of the blog post.
        body_format: Format of the body to return ('storage', 'atlas_doc_format', 'view', etc.).
    """
    return client.get(f"/api/v2/blogposts/{blogpost_id}", params={"body-format": body_format})

def update_blogpost(
    client: ConfluenceClient,
    blogpost_id: str,
    title: str,
    body: str,
    representation: str = "storage",
    version_number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Update an existing blog post.
    
    Args:
        blogpost_id: Numeric ID of the blog post.
        title: New title of the blog post.
        body: New content of the blog post.
        representation: Format of the body ('storage' or 'atlas_doc_format').
        version_number: Optional version number. If not provided, the current version is fetched and incremented.
    """
    if version_number is None:
        current_blog = client.get(f"/api/v2/blogposts/{blogpost_id}")
        if "error" in current_blog:
            return {"error": f"Failed to fetch current blog post version: {current_blog['error']}"}
        version_number = current_blog.get("version", {}).get("number", 0) + 1
        
    payload = {
        "id": blogpost_id,
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
    return client.put(f"/api/v2/blogposts/{blogpost_id}", json_data=payload)

def delete_blogpost(client: ConfluenceClient, blogpost_id: str) -> Dict[str, Any]:
    """
    Delete a blog post.
    
    Args:
        blogpost_id: Numeric ID of the blog post to delete.
    """
    return client.delete(f"/api/v2/blogposts/{blogpost_id}")
