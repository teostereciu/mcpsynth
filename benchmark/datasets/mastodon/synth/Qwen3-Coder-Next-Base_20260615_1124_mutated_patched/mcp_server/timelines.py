from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, Optional, List
import os
import requests

mcp = FastMCP("mastodon")

# Load authentication from environment variables
BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")

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

# ==================== Timelines ====================

@mcp.tool()
def get_home_timeline(limit: int = 20, max_id: Optional[str] = None, since_id: Optional[str] = None) -> list:
    """Get home timeline statuses.
    
    Args:
        limit: Maximum number of results
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
        
    Returns:
        List of status dictionaries
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    return _api_request("GET", "/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(local: bool = False, remote: bool = False, only_media: bool = False, limit: int = 20, max_id: Optional[str] = None, since_id: Optional[str] = None) -> list:
    """Get public timeline statuses.
    
    Args:
        local: Show only local statuses
        remote: Show only remote statuses
        only_media: Show only statuses with media attachments
        limit: Maximum number of results
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
        
    Returns:
        List of status dictionaries
    """
    params = {"limit": limit, "local": local, "remote": remote, "only_media": only_media}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    return _api_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: bool = False, limit: int = 20, max_id: Optional[str] = None, since_id: Optional[str] = None) -> list:
    """Get public timeline for a specific hashtag.
    
    Args:
        hashtag: The hashtag to get statuses for (without #)
        local: Show only local statuses
        limit: Maximum number of results
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
        
    Returns:
        List of status dictionaries
    """
    params = {"limit": limit, "local": local}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    return _api_request("GET", f"/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20, max_id: Optional[str] = None, since_id: Optional[str] = None) -> list:
    """Get statuses from a specific list.
    
    Args:
        list_id: The ID of the list
        limit: Maximum number of results
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
        
    Returns:
        List of status dictionaries
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    return _api_request("GET", f"/timelines/list/{list_id}", params=params)
