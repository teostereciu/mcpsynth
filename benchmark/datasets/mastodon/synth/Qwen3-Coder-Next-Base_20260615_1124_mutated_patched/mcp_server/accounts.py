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

# ==================== Accounts ====================

@mcp.tool()
def get_authenticated_account() -> Dict[str, Any]:
    """Get authenticated account information.
    
    Returns:
        Dict containing authenticated account credentials
    """
    return _api_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def update_account_profile(display_name: Optional[str] = None, note: Optional[str] = None, locked: bool = False, bot: bool = False, discoverable: bool = False, visibility: str = "public", sensitive: bool = False, lang: str = "", 
                           account_fields: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Update account profile and preferences.
    
    Args:
        display_name: Display name for the profile
        note: Account bio
        locked: Whether manual approval of follow requests is required
        bot: Whether the account has a bot flag
        discoverable: Whether the account should be shown in the profile directory
        visibility: Default post privacy ("public", "unlisted", "private")
        sensitive: Whether to mark authored statuses as sensitive by default
        lang: Default language for authored statuses (ISO 639-1)
        account_fields: List of field dictionaries with 'name' and 'value'
        
    Returns:
        Dict containing updated account credentials
    """
    data = {}
    if display_name is not None:
        data["display_name"] = display_name
    if note is not None:
        data["note"] = note
    data["locked"] = locked
    data["bot"] = bot
    data["discoverable"] = discoverable
    
    source = {"privacy": visibility, "is_sensitive": sensitive, "lang": lang}
    data["source"] = source
    
    if account_fields:
        fields_attrs = {}
        for i, field in enumerate(account_fields):
            fields_attrs[str(i)] = {"name": field["name"], "value": field["value"]}
        data["fields_attributes"] = fields_attrs
        
    return _api_request("PATCH", "/accounts/update_credentials", data=data)

@mcp.tool()
def get_account_by_id(account_id: str) -> Dict[str, Any]:
    """Get account information by ID.
    
    Args:
        account_id: The ID of the account to retrieve
        
    Returns:
        Dict containing account information
    """
    return _api_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def get_account_statuses(account_id: str, pinned: bool = False, limit: int = 20, exclude_replies: bool = False, max_id: Optional[str] = None) -> list:
    """Get account's statuses.
    
    Args:
        account_id: The ID of the account
        pinned: Filter for pinned statuses only
        limit: Maximum number of results
        exclude_replies: Filter out replies to other accounts
        max_id: Return results older than this ID
        
    Returns:
        List of status dictionaries
    """
    params = {"limit": limit, "pinned": pinned, "exclude_replies": exclude_replies}
    if max_id:
        params["max_id"] = max_id
    return _api_request("GET", f"/accounts/{account_id}/statuses", params=params)

@mcp.tool()
def follow_account(account_id: str) -> Dict[str, Any]:
    """Follow an account.
    
    Args:
        account_id: The ID of the account to follow
        
    Returns:
        Dict containing relationship information
    """
    return _api_request("POST", f"/accounts/{account_id}/follow")

@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    """Unfollow an account.
    
    Args:
        account_id: The ID of the account to unfollow
        
    Returns:
        Dict containing relationship information
    """
    return _api_request("POST", f"/accounts/{account_id}/unfollow")

@mcp.tool()
def get_followers(account_id: str, limit: int = 20) -> list:
    """Get account's followers.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of results
        
    Returns:
        List of follower account dictionaries
    """
    params = {"limit": limit}
    return _api_request("GET", f"/accounts/{account_id}/followers", params=params)

@mcp.tool()
def get_following(account_id: str, limit: int = 20) -> list:
    """Get accounts that this account is following.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of results
        
    Returns:
        List of following account dictionaries
    """
    params = {"limit": limit}
    return _api_request("GET", f"/accounts/{account_id}/following", params=params)

@mcp.tool()
def block_account(account_id: str) -> Dict[str, Any]:
    """Block an account.
    
    Args:
        account_id: The ID of the account to block
        
    Returns:
        Dict containing relationship information
    """
    return _api_request("POST", f"/accounts/{account_id}/block")

@mcp.tool()
def unblock_account(account_id: str) -> Dict[str, Any]:
    """Unblock an account.
    
    Args:
        account_id: The ID of the account to unblock
        
    Returns:
        Dict containing relationship information
    """
    return _api_request("POST", f"/accounts/{account_id}/unblock")

@mcp.tool()
def mute_account(account_id: str, notifications: bool = True) -> Dict[str, Any]:
    """Mute an account.
    
    Args:
        account_id: The ID of the account to mute
        notifications: Whether to mute notifications in addition to statuses
        
    Returns:
        Dict containing relationship information
    """
    params = {"notifications": notifications}
    return _api_request("POST", f"/accounts/{account_id}/mute", params=params)

@mcp.tool()
def unmute_account(account_id: str) -> Dict[str, Any]:
    """Unmute an account.
    
    Args:
        account_id: The ID of the account to unmute
        
    Returns:
        Dict containing relationship information
    """
    return _api_request("POST", f"/accounts/{account_id}/unmute")
