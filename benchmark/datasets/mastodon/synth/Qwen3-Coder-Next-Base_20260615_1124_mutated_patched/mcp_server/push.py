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

# ==================== Push Notifications ====================

@mcp.tool()
def get_push_subscription() -> Dict[str, Any]:
    """Get the current user's push subscription.
    
    Returns:
        Dict containing push subscription information
    """
    return _api_request("GET", "/push/subscription")

@mcp.tool()
def update_push_subscription(alerts: Dict[str, Any]) -> Dict[str, Any]:
    """Update the current user's push subscription alerts.
    
    Args:
        alerts: Dictionary specifying which alerts to enable
        
    Returns:
        Dict containing updated push subscription information
    """
    data = {"alerts": alerts}
    return _api_request("PUT", "/push/subscription", data=data)

@mcp.tool()
def delete_push_subscription() -> Dict[str, Any]:
    """Unsubscribe from push notifications.
    
    Returns:
        Dict with success information
    """
    return _api_request("DELETE", "/push/subscription")
