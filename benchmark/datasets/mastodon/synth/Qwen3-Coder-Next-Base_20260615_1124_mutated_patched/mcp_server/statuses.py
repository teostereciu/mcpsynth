from mcp.server.fastmcp import FastMCP
import requests
import os
from typing import Dict, Any, Optional

mcp = FastMCP("mastodon")

# Load authentication from environment variables
BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")

# Helper functions
def _get_auth_headers() -> Dict[str, str]:
    """Get authorization headers for Mastodon API."""
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}

def _api_request(method: str, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make an API request to Mastodon."""
    url = f"{BASE_URL}/api/v1{path}"
    headers = _get_auth_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# ==================== Statuses ====================

@mcp.tool()
def post_status(text: str, visibility: str = "public", in_reply_to_id: Optional[str] = None, media_ids: Optional[list] = None) -> Dict[str, Any]:
    """Post a new status to Mastodon.
    
    Args:
        text: The text content of the status
        visibility: Post visibility ("public", "unlisted", "private", "direct")
        in_reply_to_id: ID of status being replied to
        media_ids: List of media attachment IDs
        
    Returns:
        Dict containing status information
    """
    data = {"status": text, "visibility": visibility}
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        data["media_ids"] = media_ids
        
    return _api_request("POST", "/statuses", data=data)

@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """Get a single status by ID.
    
    Args:
        status_id: The ID of the status to retrieve
        
    Returns:
        Dict containing status information
    """
    return _api_request("GET", f"/statuses/{status_id}")

@mcp.tool()
def get_statuses(status_ids: list) -> list:
    """Get multiple statuses by IDs.
    
    Args:
        status_ids: List of status IDs to retrieve
        
    Returns:
        List of status dictionaries
    """
    return _api_request("GET", "/statuses", params={"id[]": status_ids})

@mcp.tool()
def delete_status(status_id: str, delete_media: bool = False) -> Dict[str, Any]:
    """Delete a status.
    
    Args:
        status_id: The ID of the status to delete
        delete_media: Whether to immediately delete media attachments
        
    Returns:
        Dict containing deleted status information
    """
    params = {"delete_media": delete_media}
    return _api_request("DELETE", f"/statuses/{status_id}", params=params)

@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    """Get parent and child statuses in context (thread).
    
    Args:
        status_id: The ID of the status to get context for
        
    Returns:
        Dict containing ancestors and descendants
    """
    return _api_request("GET", f"/statuses/{status_id}/context")

@mcp.tool()
def boost_status(status_id: str) -> Dict[str, Any]:
    """Boost (reblog) a status.
    
    Args:
        status_id: The ID of the status to boost
        
    Returns:
        Dict containing boosted status information
    """
    return _api_request("POST", f"/statuses/{status_id}/reblog")

@mcp.tool()
def unboost_status(status_id: str) -> Dict[str, Any]:
    """Unboost (unreblog) a status.
    
    Args:
        status_id: The ID of the status to unboost
        
    Returns:
        Dict containing unboosted status information
    """
    return _api_request("POST", f"/statuses/{status_id}/unreblog")

@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    """Favourite a status.
    
    Args:
        status_id: The ID of the status to favourite
        
    Returns:
        Dict containing favourited status information
    """
    return _api_request("POST", f"/statuses/{status_id}/favourite")

@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """Unfavourite a status.
    
    Args:
        status_id: The ID of the status to unfavourite
        
    Returns:
        Dict containing unfavourited status information
    """
    return _api_request("POST", f"/statuses/{status_id}/unfavourite")

@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    """Bookmark a status.
    
    Args:
        status_id: The ID of the status to bookmark
        
    Returns:
        Dict containing bookmarked status information
    """
    return _api_request("POST", f"/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """Unbookmark a status.
    
    Args:
        status_id: The ID of the status to unbookmark
        
    Returns:
        Dict containing unbookmarked status information
    """
    return _api_request("POST", f"/statuses/{status_id}/unbookmark")

@mcp.tool()
def list_favourites(limit: int = 20, max_id: Optional[str] = None) -> list:
    """List favourited statuses.
    
    Args:
        limit: Maximum number of results
        max_id: Return results older than this ID
        
    Returns:
        List of favourited status dictionaries
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    return _api_request("GET", "/favourites", params=params)

@mcp.tool()
def list_bookmarks(limit: int = 20, max_id: Optional[str] = None) -> list:
    """List bookmarked statuses.
    
    Args:
        limit: Maximum number of results
        max_id: Return results older than this ID
        
    Returns:
        List of bookmarked status dictionaries
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    return _api_request("GET", "/bookmarks", params=params)
