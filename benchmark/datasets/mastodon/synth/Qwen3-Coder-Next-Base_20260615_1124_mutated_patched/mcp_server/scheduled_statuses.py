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

# ==================== Scheduled Statuses ====================

@mcp.tool()
def list_scheduled_statuses(limit: int = 40, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> list:
    """Get all scheduled statuses.
    
    Args:
        limit: Maximum number of results
        max_id: All results returned will be lesser than this ID
        since_id: All results returned will be greater than this ID
        min_id: Returns results immediately newer than this ID
        
    Returns:
        List of scheduled status dictionaries
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return _api_request("GET", "/scheduled_statuses", params=params)

@mcp.tool()
def get_scheduled_status(status_id: str) -> Dict[str, Any]:
    """Get a single scheduled status.
    
    Args:
        status_id: The ID of the scheduled status
        
    Returns:
        Dict containing scheduled status information
    """
    return _api_request("GET", f"/scheduled_statuses/{status_id}")

@mcp.tool()
def update_scheduled_status(status_id: str, scheduled_at: str) -> Dict[str, Any]:
    """Update a scheduled status's publishing date.
    
    Args:
        status_id: The ID of the scheduled status
        scheduled_at: New datetime for publishing (at least 5 minutes in the future)
        
    Returns:
        Dict containing updated scheduled status information
    """
    data = {"scheduled_at": scheduled_at}
    return _api_request("PUT", f"/scheduled_statuses/{status_id}", data=data)

@mcp.tool()
def cancel_scheduled_status(status_id: str) -> Dict[str, Any]:
    """Cancel a scheduled status.
    
    Args:
        status_id: The ID of the scheduled status to cancel
        
    Returns:
        Dict with success information
    """
    return _api_request("DELETE", f"/scheduled_statuses/{status_id}")
