#!/usr/bin/env python3
"""Mastodon MCP Server - Provides tools for interacting with the Mastodon API."""

import os
import requests
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(name="mastodon")

# Configuration from environment
BASE_URL = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")


def _make_request(method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make a request to the Mastodon API."""
    if not ACCESS_TOKEN:
        return {"error": "MASTODON_ACCESS_TOKEN environment variable not set"}
    
    url = f"{BASE_URL}/api/v1{endpoint}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, json=data, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def post_status(
    status: str,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    visibility: str = "public",
    sensitive: bool = False,
    spoiler_text: Optional[str] = None
) -> Dict[str, Any]:
    """Post a new status (toot) to the user's timeline."""
    data = {
        "status": status,
        "visibility": visibility,
        "sensitive": sensitive
    }
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        data["media_ids"] = media_ids
    if spoiler_text:
        data["spoiler_text"] = spoiler_text
    
    return _make_request("POST", "/statuses", data=data)


@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """Get a status by its ID."""
    return _make_request("GET", f"/statuses/{status_id}")


@mcp.tool()
def delete_status(status_id: str) -> Dict[str, Any]:
    """Delete a status by its ID."""
    return _make_request("DELETE", f"/statuses/{status_id}")


@mcp.tool()
def reblog_status(status_id: str) -> Dict[str, Any]:
    """Boost (reblog) a status."""
    return _make_request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def unreblog_status(status_id: str) -> Dict[str, Any]:
    """Undo a boost (unreblog) of a status."""
    return _make_request("DELETE", f"/statuses/{status_id}/reblog")


@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    """Favourite a status."""
    return _make_request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """Undo a favourite of a status."""
    return _make_request("DELETE", f"/statuses/{status_id}/favourite")


@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    """Get context (ancestors and descendants) for a status."""
    return _make_request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """Get account information by ID."""
    return _make_request("GET", f"/accounts/{account_id}")


@mcp.tool()
def get_authenticated_account() -> Dict[str, Any]:
    """Get the authenticated user's account information."""
    return _make_request("GET", "/accounts/verify_credentials")


@mcp.tool()
def follow_account(account_id: str) -> Dict[str, Any]:
    """Follow an account by ID."""
    return _make_request("POST", f"/accounts/{account_id}/follow")


@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    """Unfollow an account by ID."""
    return _make_request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool()
def get_account_followers(account_id: str, limit: int = 40) -> Dict[str, Any]:
    """Get followers for an account."""
    return _make_request("GET", f"/accounts/{account_id}/followers", params={"limit": limit})


@mcp.tool()
def get_account_following(account_id: str, limit: int = 40) -> Dict[str, Any]:
    """Get accounts followed by an account."""
    return _make_request("GET", f"/accounts/{account_id}/following", params={"limit": limit})


@mcp.tool()
def get_home_timeline(limit: int = 20, since_id: Optional[str] = None, max_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """Get the home timeline (statuses from followed accounts)."""
    params = {"limit": limit}
    if since_id:
        params["since_id"] = since_id
    if max_id:
        params["max_id"] = max_id
    return _make_request("GET", "/timelines/home", params=params)


@mcp.tool()
def get_public_timeline(local: bool = False, limit: int = 20) -> List[Dict[str, Any]]:
    """Get the public timeline (statuses from all accounts on the instance)."""
    params = {"limit": limit, "local": local}
    return _make_request("GET", "/timelines/public", params=params)


@mcp.tool()
def get_hashtag_timeline(tag: str, local: bool = False, limit: int = 20) -> List[Dict[str, Any]]:
    """Get statuses containing a specific hashtag."""
    params = {"limit": limit, "local": local}
    return _make_request("GET", f"/timelines/tag/{tag}", params=params)


@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Get statuses from a specific list."""
    return _make_request("GET", f"/timelines/list/{list_id}", params={"limit": limit})


@mcp.tool()
def list_notifications(limit: int = 20, since_id: Optional[str] = None, max_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """List notifications for the authenticated user."""
    params = {"limit": limit}
    if since_id:
        params["since_id"] = since_id
    if max_id:
        params["max_id"] = max_id
    return _make_request("GET", "/notifications", params=params)


@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    """Get a specific notification by ID."""
    return _make_request("GET", f"/notifications/{notification_id}")


@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """Dismiss (mark as read) a specific notification."""
    return _make_request("POST", f"/notifications/{notification_id}/dismiss")


@mcp.tool()
def clear_notifications() -> Dict[str, Any]:
    """Clear all notifications for the authenticated user."""
    return _make_request("POST", "/notifications/clear")


@mcp.tool()
def search_accounts(query: str, limit: int = 40, resolve: bool = False) -> List[Dict[str, Any]]:
    """Search for accounts by username or display name."""
    params = {"q": query, "limit": limit, "resolve": resolve}
    return _make_request("GET", "/accounts/search", params=params)


@mcp.tool()
def search_statuses(query: str, resolve: bool = False, offset: int = 0) -> List[Dict[str, Any]]:
    """Search for statuses by content."""
    params = {"q": query, "resolve": resolve}
    if offset:
        params["offset"] = offset
    return _make_request("GET", "/search", params=params)


@mcp.tool()
def search(query: str, resolve: bool = False, exclude_unreviewed: bool = False) -> Dict[str, Any]:
    """Search for accounts, statuses, and hashtags."""
    params = {"q": query, "resolve": resolve, "exclude_unreviewed": exclude_unreviewed}
    return _make_request("GET", "/search", params=params)


@mcp.tool()
def create_list(title: str) -> Dict[str, Any]:
    """Create a new list."""
    return _make_request("POST", "/lists", data={"title": title})


@mcp.tool()
def get_lists() -> List[Dict[str, Any]]:
    """Get all lists for the authenticated user."""
    return _make_request("GET", "/lists")


@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    """Get a specific list by ID."""
    return _make_request("GET", f"/lists/{list_id}")


@mcp.tool()
def update_list(list_id: str, title: str) -> Dict[str, Any]:
    """Update a list's title."""
    return _make_request("PUT", f"/lists/{list_id}", data={"title": title})


@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    """Delete a list."""
    return _make_request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """Add accounts to a list."""
    return _make_request("POST", f"/lists/{list_id}/accounts", data={"account_ids": account_ids})


@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """Remove accounts from a list."""
    return _make_request("DELETE", f"/lists/{list_id}/accounts", data={"account_ids": account_ids})


@mcp.tool()
def get_list_accounts(list_id: str) -> List[Dict[str, Any]]:
    """Get accounts in a list."""
    return _make_request("GET", f"/lists/{list_id}/accounts")


@mcp.tool()
def get_bookmarks(limit: int = 20) -> List[Dict[str, Any]]:
    """Get bookmarked statuses."""
    return _make_request("GET", "/bookmarks", params={"limit": limit})


@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    """Bookmark a status."""
    return _make_request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """Remove a status from bookmarks."""
    return _make_request("DELETE", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def get_favourites(limit: int = 20) -> List[Dict[str, Any]]:
    """Get favourite statuses."""
    return _make_request("GET", "/favourites", params={"limit": limit})


@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None, focus_x: float = 0, focus_y: float = 0) -> Dict[str, Any]:
    """Upload a media file for use in a status."""
    if not ACCESS_TOKEN:
        return {"error": "MASTODON_ACCESS_TOKEN environment variable not set"}
    
    url = f"{BASE_URL}/api/v1/media"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            data["focus_x"] = str(focus_x)
            data["focus_y"] = str(focus_y)
            
            response = requests.post(url, headers=headers, files=files, data=data, timeout=30)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    """Get information about the Mastodon instance."""
    return _make_request("GET", "/instance")


@mcp.tool()
def get_instance_activity() -> Dict[str, Any]:
    """Get activity metrics for the instance."""
    return _make_request("GET", "/instance/activity")


if __name__ == "__main__":
    mcp.run()
