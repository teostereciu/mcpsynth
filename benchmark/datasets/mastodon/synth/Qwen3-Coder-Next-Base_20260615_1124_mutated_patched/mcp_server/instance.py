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

# ==================== Instance ====================

@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    """Get information about the Mastodon instance.
    
    Returns:
        Dict containing instance information including version, title, description, etc.
    """
    return _api_request("GET", "/instance")

@mcp.tool()
def get_instance_peers() -> list:
    """Get a list of instances this instance knows about.
    
    Returns:
        List of instance domain strings
    """
    return _api_request("GET", "/instance/peers")

@mcp.tool()
def get_instance_activity() -> Dict[str, Any]:
    """Get weekly activity for the instance.
    
    Returns:
        Dict containing weekly activity statistics
    """
    return _api_request("GET", "/instance/activity")
