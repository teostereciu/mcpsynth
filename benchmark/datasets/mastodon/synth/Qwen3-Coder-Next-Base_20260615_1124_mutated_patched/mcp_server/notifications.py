from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, Optional
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

# ==================== Notifications ====================

@mcp.tool()
def list_notifications(limit: int = 20, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, exclude_types: Optional[list] = None) -> list:
    """Get notifications for the current user.
    
    Args:
        limit: Maximum number of results
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
        min_id: Return results more recent than this ID
        exclude_types: List of notification types to exclude
        
    Returns:
        List of notification dictionaries
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if exclude_types:
        params["exclude_types[]"] = exclude_types
    return _api_request("GET", "/notifications", params=params)

@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    """Get a single notification by ID.
    
    Args:
        notification_id: The ID of the notification to retrieve
        
    Returns:
        Dict containing notification information
    """
    return _api_request("GET", f"/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """Dismiss a single notification.
    
    Args:
        notification_id: The ID of the notification to dismiss
        
    Returns:
        Dict with success information
    """
    return _api_request("POST", f"/notifications/{notification_id}/dismiss")

@mcp.tool()
def clear_all_notifications() -> Dict[str, Any]:
    """Dismiss all notifications for the current user.
    
    Returns:
        Dict with success information
    """
    return _api_request("POST", "/notifications/clear")
