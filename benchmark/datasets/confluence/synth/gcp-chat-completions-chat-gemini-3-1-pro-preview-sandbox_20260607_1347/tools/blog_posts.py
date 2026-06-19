from typing import Any, Dict, Optional
from server import mcp
from confluence_client import client

@mcp.tool()
def get_blog_posts(space_id: Optional[str] = None, limit: int = 25) -> Dict[str, Any]:
    """Get blog posts."""
    params = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    return client.request("GET", "/api/v2/blogposts", params=params)

@mcp.tool()
def get_blog_post_by_id(blog_post_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """Get a blog post by its ID."""
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}", params={"body-format": body_format})

@mcp.tool()
def create_blog_post(space_id: str, title: str, body: str) -> Dict[str, Any]:
    """Create a new blog post."""
    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    return client.request("POST", "/api/v2/blogposts", json=payload)

@mcp.tool()
def update_blog_post(blog_post_id: str, space_id: str, title: str, body: str, version_number: int) -> Dict[str, Any]:
    """Update an existing blog post."""
    payload = {
        "id": blog_post_id,
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
    return client.request("PUT", f"/api/v2/blogposts/{blog_post_id}", json=payload)

@mcp.tool()
def delete_blog_post(blog_post_id: str) -> Dict[str, Any]:
    """Delete a blog post."""
    return client.request("DELETE", f"/api/v2/blogposts/{blog_post_id}")
