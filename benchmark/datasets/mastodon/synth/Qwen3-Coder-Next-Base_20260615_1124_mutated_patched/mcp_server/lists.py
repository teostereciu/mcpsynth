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

# ==================== Lists ====================

@mcp.tool()
def create_list(title: str, exclusive: bool = False) -> Dict[str, Any]:
    """Create a new list.
    
    Args:
        title: Title for the list
        exclusive: Whether to hide accounts in this list from the public timeline
        
    Returns:
        Dict containing list information
    """
    data = {"title": title, "exclusive": exclusive}
    return _api_request("POST", "/lists", data=data)

@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    """Get a single list by ID.
    
    Args:
        list_id: The ID of the list to retrieve
        
    Returns:
        Dict containing list information
    """
    return _api_request("GET", f"/lists/{list_id}")

@mcp.tool()
def update_list(list_id: str, title: str, exclusive: bool = False) -> Dict[str, Any]:
    """Update a list.
    
    Args:
        list_id: The ID of the list
        title: New title for the list
        exclusive: Whether to hide accounts in this list from the public timeline
        
    Returns:
        Dict containing list information
    """
    data = {"title": title, "exclusive": exclusive}
    return _api_request("PUT", f"/lists/{list_id}", data=data)

@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    """Delete a list.
    
    Args:
        list_id: The ID of the list to delete
        
    Returns:
        Dict with success information
    """
    return _api_request("DELETE", f"/lists/{list_id}")

@mcp.tool()
def list_lists() -> list:
    """Get all lists for the current user.
    
    Returns:
        List of list dictionaries
    """
    return _api_request("GET", "/lists")

@mcp.tool()
def get_accounts_in_list(list_id: str) -> list:
    """Get accounts in a specific list.
    
    Args:
        list_id: The ID of the list
        
    Returns:
        List of account dictionaries
    """
    return _api_request("GET", f"/lists/{list_id}/accounts")

@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """Add accounts to a list.
    
    Args:
        list_id: The ID of the list
        account_ids: List of account IDs to add
        
    Returns:
        Dict with success information
    """
    data = {"account_ids": account_ids}
    return _api_request("POST", f"/lists/{list_id}/accounts", data=data)

@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """Remove accounts from a list.
    
    Args:
        list_id: The ID of the list
        account_ids: List of account IDs to remove
        
    Returns:
        Dict with success information
    """
    data = {"account_ids": account_ids}
    return _api_request("DELETE", f"/lists/{list_id}/accounts", data=data)
