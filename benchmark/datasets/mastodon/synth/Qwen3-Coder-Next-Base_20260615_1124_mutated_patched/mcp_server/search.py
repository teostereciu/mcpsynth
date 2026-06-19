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

# ==================== Search ====================

@mcp.tool()
def search_accounts(query: str, limit: int = 40, resolve: bool = False, following: bool = False, following_id: Optional[str] = None) -> list:
    """Search for accounts.
    
    Args:
        query: Search query
        limit: Maximum number of results
        resolve: Attempt WebFinger lookup
        following: Limit to accounts being followed
        following_id: Limit to accounts that a specific account is following
        
    Returns:
        List of account dictionaries
    """
    params = {"q": query, "limit": limit, "resolve": resolve, "following": following}
    if following_id:
        params["following_id"] = following_id
    return _api_request("GET", "/search", params=params)

@mcp.tool()
def search_statuses(query: str, resolve: bool = False, account_id: Optional[str] = None, offset: int = 0) -> list:
    """Search for statuses.
    
    Args:
        query: Search query
        resolve: Attempt WebFinger lookup
        account_id: Limit to statuses by a specific account
        offset: Offset into search results
        
    Returns:
        List of status dictionaries
    """
    params = {"q": query, "resolve": resolve, "offset": offset}
    if account_id:
        params["account_id"] = account_id
    return _api_request("GET", "/search", params=params)

@mcp.tool()
def search_hashtags(query: str, resolve: bool = False) -> list:
    """Search for hashtags.
    
    Args:
        query: Search query
        resolve: Attempt WebFinger lookup
        
    Returns:
        List of hashtag dictionaries
    """
    params = {"q": query, "resolve": resolve}
    return _api_request("GET", "/search", params=params)
