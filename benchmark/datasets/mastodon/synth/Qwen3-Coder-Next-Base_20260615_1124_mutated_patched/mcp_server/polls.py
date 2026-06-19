from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, List
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

def _api_request(method: str, path: str, params: Dict = None, data: Dict = None) -> Dict[str, Any]:
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

# ==================== Polls ====================

@mcp.tool()
def get_poll(poll_id: str) -> Dict[str, Any]:
    """Get a poll attached to a status.
    
    Args:
        poll_id: The ID of the poll
        
    Returns:
        Dict containing poll information
    """
    return _api_request("GET", f"/polls/{poll_id}")

@mcp.tool()
def vote_on_poll(poll_id: str, choices: List[int]) -> Dict[str, Any]:
    """Vote on a poll.
    
    Args:
        poll_id: The ID of the poll
        choices: List of indices for chosen options (starting from 0)
        
    Returns:
        Dict containing updated poll information
    """
    data = {"choices[]": choices}
    return _api_request("POST", f"/polls/{poll_id}/votes", data=data)
