#!/usr/bin/env python3
"""
MCP Server for Mastodon API
Provides tools for interacting with Mastodon instances via the REST API.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("mastodon")

# Configuration from environment
MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN", "")
MASTODON_BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
API_BASE_URL = f"{MASTODON_BASE_URL}/api/v1"

# Helper function to make authenticated requests
def make_request(
    method: str,
    endpoint: str,
    data: Optional[dict] = None,
    params: Optional[dict] = None,
    files: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the Mastodon API."""
    url = f"{API_BASE_URL}{endpoint}"
    headers = {}
    
    if MASTODON_ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {MASTODON_ACCESS_TOKEN}"
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=10)
        elif method == "POST":
            if files:
                response = requests.post(url, headers=headers, data=data, files=files, timeout=10)
            else:
                response.headers["Content-Type"] = "application/json"
                response = requests.post(url, headers=headers, json=data, params=params, timeout=10)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data, params=params, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=10)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
        
        return response.json() if response.text else {}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from server"}


# ============================================================================
# STATUSES
# ============================================================================

@server.tool()
def post_status(
    status: str,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[list] = None,
    sensitive: bool = False,
    spoiler_text: Optional[str] = None,
    visibility: str = "public",
) -> dict:
    """
    Post a new status (toot) to Mastodon.
    
    Args:
        status: The text content of the status
        in_reply_to_id: ID of the status this is replying to
        media_ids: List of media attachment IDs to attach
        sensitive: Mark the status as sensitive/NSFW
        spoiler_text: Text to show before the status content
        visibility: One of "public", "unlisted", "private", "direct"
    
    Returns:
        The created status object
    """
    data = {
        "status": status,
        "sensitive": sensitive,
        "visibility": visibility,
    }
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        data["media_ids"] = media_ids
    if spoiler_text:
        data["spoiler_text"] = spoiler_text
    
    return make_request("POST", "/statuses", data=data)


@server.tool()
def get_status(status_id: str) -> dict:
    """
    Get a single status by ID.
    
    Args:
        status_id: The ID of the status to retrieve
    
    Returns:
        The status object
    """
    return make_request("GET", f"/statuses/{status_id}")


@server.tool()
def delete_status(status_id: str) -> dict:
    """
    Delete a status (must be owned by the authenticated user).
    
    Args:
        status_id: The ID of the status to delete
    
    Returns:
        The deleted status object
    """
    return make_request("DELETE", f"/statuses/{status_id}")


@server.tool()
def get_status_context(status_id: str) -> dict:
    """
    Get the context (ancestors and descendants) of a status.
    
    Args:
        status_id: The ID of the status
    
    Returns:
        Object with "ancestors" and "descendants" arrays
    """
    return make_request("GET", f"/statuses/{status_id}/context")


@server.tool()
def boost_status(status_id: str) -> dict:
    """
    Boost (reblog) a status.
    
    Args:
        status_id: The ID of the status to boost
    
    Returns:
        The boosted status object
    """
    return make_request("POST", f"/statuses/{status_id}/reblog")


@server.tool()
def unboost_status(status_id: str) -> dict:
    """
    Remove a boost (reblog) from a status.
    
    Args:
        status_id: The ID of the status to unboost
    
    Returns:
        The status object
    """
    return make_request("POST", f"/statuses/{status_id}/unreblog")


@server.tool()
def favourite_status(status_id: str) -> dict:
    """
    Mark a status as favourite.
    
    Args:
        status_id: The ID of the status to favourite
    
    Returns:
        The status object
    """
    return make_request("POST", f"/statuses/{status_id}/favourite")


@server.tool()
def unfavourite_status(status_id: str) -> dict:
    """
    Remove a status from favourites.
    
    Args:
        status_id: The ID of the status to unfavourite
    
    Returns:
        The status object
    """
    return make_request("POST", f"/statuses/{status_id}/unfavourite")


@server.tool()
def bookmark_status(status_id: str) -> dict:
    """
    Bookmark a status.
    
    Args:
        status_id: The ID of the status to bookmark
    
    Returns:
        The status object
    """
    return make_request("POST", f"/statuses/{status_id}/bookmark")


@server.tool()
def unbookmark_status(status_id: str) -> dict:
    """
    Remove a status from bookmarks.
    
    Args:
        status_id: The ID of the status to unbookmark
    
    Returns:
        The status object
    """
    return make_request("POST", f"/statuses/{status_id}/unbookmark")


# ============================================================================
# ACCOUNTS
# ============================================================================

@server.tool()
def get_authenticated_account() -> dict:
    """
    Get the authenticated user's account information.
    
    Returns:
        The authenticated account object
    """
    return make_request("GET", "/accounts/verify_credentials")


@server.tool()
def get_account(account_id: str) -> dict:
    """
    Get an account by ID.
    
    Args:
        account_id: The ID of the account to retrieve
    
    Returns:
        The account object
    """
    return make_request("GET", f"/accounts/{account_id}")


@server.tool()
def get_account_statuses(
    account_id: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> list:
    """
    Get statuses posted by an account.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", f"/accounts/{account_id}/statuses", params=params)


@server.tool()
def follow_account(account_id: str) -> dict:
    """
    Follow an account.
    
    Args:
        account_id: The ID of the account to follow
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/follow")


@server.tool()
def unfollow_account(account_id: str) -> dict:
    """
    Unfollow an account.
    
    Args:
        account_id: The ID of the account to unfollow
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/unfollow")


@server.tool()
def get_account_followers(
    account_id: str,
    limit: int = 40,
    max_id: Optional[str] = None,
) -> list:
    """
    Get followers of an account.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of followers to return (default 40)
        max_id: Return followers older than this ID
    
    Returns:
        List of account objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    
    return make_request("GET", f"/accounts/{account_id}/followers", params=params)


@server.tool()
def get_account_following(
    account_id: str,
    limit: int = 40,
    max_id: Optional[str] = None,
) -> list:
    """
    Get accounts that an account is following.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of accounts to return (default 40)
        max_id: Return accounts older than this ID
    
    Returns:
        List of account objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    
    return make_request("GET", f"/accounts/{account_id}/following", params=params)


@server.tool()
def get_account_relationship(account_id: str) -> dict:
    """
    Get the relationship between the authenticated user and another account.
    
    Args:
        account_id: The ID of the account
    
    Returns:
        The relationship object
    """
    return make_request("GET", f"/accounts/relationships", params={"id": account_id})


@server.tool()
def block_account(account_id: str) -> dict:
    """
    Block an account.
    
    Args:
        account_id: The ID of the account to block
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/block")


@server.tool()
def unblock_account(account_id: str) -> dict:
    """
    Unblock an account.
    
    Args:
        account_id: The ID of the account to unblock
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/unblock")


@server.tool()
def mute_account(account_id: str, notifications: bool = True) -> dict:
    """
    Mute an account.
    
    Args:
        account_id: The ID of the account to mute
        notifications: Whether to mute notifications from this account
    
    Returns:
        The relationship object
    """
    data = {"notifications": notifications}
    return make_request("POST", f"/accounts/{account_id}/mute", data=data)


@server.tool()
def unmute_account(account_id: str) -> dict:
    """
    Unmute an account.
    
    Args:
        account_id: The ID of the account to unmute
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/unmute")


# ============================================================================
# TIMELINES
# ============================================================================

@server.tool()
def get_home_timeline(
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> list:
    """
    Get the authenticated user's home timeline.
    
    Args:
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/timelines/home", params=params)


@server.tool()
def get_public_timeline(
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    local: bool = False,
) -> list:
    """
    Get the public timeline.
    
    Args:
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
        local: Only return statuses from the local instance
    
    Returns:
        List of status objects
    """
    params = {"limit": limit, "local": local}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/timelines/public", params=params)


@server.tool()
def get_hashtag_timeline(
    hashtag: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    local: bool = False,
) -> list:
    """
    Get statuses with a specific hashtag.
    
    Args:
        hashtag: The hashtag to search for (without the # symbol)
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
        local: Only return statuses from the local instance
    
    Returns:
        List of status objects
    """
    params = {"limit": limit, "local": local}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", f"/timelines/tag/{hashtag}", params=params)


@server.tool()
def get_list_timeline(
    list_id: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> list:
    """
    Get statuses from a specific list.
    
    Args:
        list_id: The ID of the list
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", f"/timelines/list/{list_id}", params=params)


# ============================================================================
# NOTIFICATIONS
# ============================================================================

@server.tool()
def get_notifications(
    limit: int = 15,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    types: Optional[list] = None,
) -> list:
    """
    Get notifications for the authenticated user.
    
    Args:
        limit: Maximum number of notifications to return (default 15)
        max_id: Return notifications older than this ID
        min_id: Return notifications newer than this ID
        types: Filter by notification types (e.g., ["mention", "favourite", "reblog", "follow"])
    
    Returns:
        List of notification objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if types:
        params["types[]"] = types
    
    return make_request("GET", "/notifications", params=params)


@server.tool()
def get_notification(notification_id: str) -> dict:
    """
    Get a single notification by ID.
    
    Args:
        notification_id: The ID of the notification
    
    Returns:
        The notification object
    """
    return make_request("GET", f"/notifications/{notification_id}")


@server.tool()
def dismiss_notification(notification_id: str) -> dict:
    """
    Dismiss a single notification.
    
    Args:
        notification_id: The ID of the notification to dismiss
    
    Returns:
        Empty object on success
    """
    return make_request("POST", f"/notifications/{notification_id}/dismiss")


@server.tool()
def clear_notifications() -> dict:
    """
    Clear all notifications for the authenticated user.
    
    Returns:
        Empty object on success
    """
    return make_request("POST", "/notifications/clear")


# ============================================================================
# SEARCH
# ============================================================================

@server.tool()
def search(
    q: str,
    type: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Search for accounts, statuses, and hashtags.
    
    Args:
        q: The search query
        type: Filter by type ("accounts", "statuses", "hashtags")
        limit: Maximum number of results to return (default 20)
        offset: Offset for pagination (default 0)
    
    Returns:
        Object with "accounts", "statuses", and "hashtags" arrays
    """
    params = {"q": q, "limit": limit, "offset": offset}
    if type:
        params["type"] = type
    
    return make_request("GET", "/search", params=params)


@server.tool()
def search_accounts(q: str, limit: int = 20, offset: int = 0) -> list:
    """
    Search for accounts.
    
    Args:
        q: The search query
        limit: Maximum number of results to return (default 20)
        offset: Offset for pagination (default 0)
    
    Returns:
        List of account objects
    """
    result = search(q=q, type="accounts", limit=limit, offset=offset)
    return result.get("accounts", []) if isinstance(result, dict) else []


@server.tool()
def search_statuses(q: str, limit: int = 20, offset: int = 0) -> list:
    """
    Search for statuses.
    
    Args:
        q: The search query
        limit: Maximum number of results to return (default 20)
        offset: Offset for pagination (default 0)
    
    Returns:
        List of status objects
    """
    result = search(q=q, type="statuses", limit=limit, offset=offset)
    return result.get("statuses", []) if isinstance(result, dict) else []


@server.tool()
def search_hashtags(q: str, limit: int = 20, offset: int = 0) -> list:
    """
    Search for hashtags.
    
    Args:
        q: The search query
        limit: Maximum number of results to return (default 20)
        offset: Offset for pagination (default 0)
    
    Returns:
        List of hashtag objects
    """
    result = search(q=q, type="hashtags", limit=limit, offset=offset)
    return result.get("hashtags", []) if isinstance(result, dict) else []


# ============================================================================
# LISTS
# ============================================================================

@server.tool()
def get_lists() -> list:
    """
    Get all lists owned by the authenticated user.
    
    Returns:
        List of list objects
    """
    return make_request("GET", "/lists")


@server.tool()
def get_list(list_id: str) -> dict:
    """
    Get a single list by ID.
    
    Args:
        list_id: The ID of the list
    
    Returns:
        The list object
    """
    return make_request("GET", f"/lists/{list_id}")


@server.tool()
def create_list(title: str, replies_policy: str = "list") -> dict:
    """
    Create a new list.
    
    Args:
        title: The title of the list
        replies_policy: Policy for replies ("followed", "list", "none")
    
    Returns:
        The created list object
    """
    data = {"title": title, "replies_policy": replies_policy}
    return make_request("POST", "/lists", data=data)


@server.tool()
def update_list(list_id: str, title: Optional[str] = None, replies_policy: Optional[str] = None) -> dict:
    """
    Update a list.
    
    Args:
        list_id: The ID of the list to update
        title: The new title for the list
        replies_policy: New policy for replies ("followed", "list", "none")
    
    Returns:
        The updated list object
    """
    data = {}
    if title is not None:
        data["title"] = title
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    
    return make_request("PUT", f"/lists/{list_id}", data=data)


@server.tool()
def delete_list(list_id: str) -> dict:
    """
    Delete a list.
    
    Args:
        list_id: The ID of the list to delete
    
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/lists/{list_id}")


@server.tool()
def get_list_accounts(list_id: str, limit: int = 40, max_id: Optional[str] = None) -> list:
    """
    Get accounts in a list.
    
    Args:
        list_id: The ID of the list
        limit: Maximum number of accounts to return (default 40)
        max_id: Return accounts older than this ID
    
    Returns:
        List of account objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    
    return make_request("GET", f"/lists/{list_id}/accounts", params=params)


@server.tool()
def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
    """
    Add accounts to a list.
    
    Args:
        list_id: The ID of the list
        account_ids: List of account IDs to add
    
    Returns:
        Empty object on success
    """
    data = {"account_ids": account_ids}
    return make_request("POST", f"/lists/{list_id}/accounts", data=data)


@server.tool()
def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
    """
    Remove accounts from a list.
    
    Args:
        list_id: The ID of the list
        account_ids: List of account IDs to remove
    
    Returns:
        Empty object on success
    """
    data = {"account_ids": account_ids}
    return make_request("DELETE", f"/lists/{list_id}/accounts", data=data)


# ============================================================================
# BOOKMARKS
# ============================================================================

@server.tool()
def get_bookmarks(
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> list:
    """
    Get the authenticated user's bookmarked statuses.
    
    Args:
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/bookmarks", params=params)


# ============================================================================
# FAVOURITES
# ============================================================================

@server.tool()
def get_favourites(
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> list:
    """
    Get the authenticated user's favourited statuses.
    
    Args:
        limit: Maximum number of statuses to return (default 20)
        max_id: Return statuses older than this ID
        min_id: Return statuses newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/favourites", params=params)


# ============================================================================
# MEDIA
# ============================================================================

@server.tool()
def upload_media(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
) -> dict:
    """
    Upload a media attachment.
    
    Args:
        file_path: Path to the media file to upload
        description: Alt text description for the media
        focus: Focus coordinates for the media (e.g., "-0.5,0.5")
    
    Returns:
        The media attachment object
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            
            return make_request("POST", "/media", data=data, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Failed to upload media: {str(e)}"}


@server.tool()
def get_media(media_id: str) -> dict:
    """
    Get information about a media attachment.
    
    Args:
        media_id: The ID of the media attachment
    
    Returns:
        The media attachment object
    """
    return make_request("GET", f"/media/{media_id}")


@server.tool()
def update_media(
    media_id: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
) -> dict:
    """
    Update a media attachment's metadata.
    
    Args:
        media_id: The ID of the media attachment
        description: Alt text description for the media
        focus: Focus coordinates for the media (e.g., "-0.5,0.5")
    
    Returns:
        The updated media attachment object
    """
    data = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus
    
    return make_request("PUT", f"/media/{media_id}", data=data)


# ============================================================================
# INSTANCE
# ============================================================================

@server.tool()
def get_instance_info() -> dict:
    """
    Get information about the Mastodon instance.
    
    Returns:
        The instance information object
    """
    return make_request("GET", "/instance")


@server.tool()
def get_instance_peers() -> list:
    """
    Get a list of peer instances known to this instance.
    
    Returns:
        List of instance domain names
    """
    return make_request("GET", "/instance/peers")


@server.tool()
def get_instance_activity() -> list:
    """
    Get activity statistics for the instance.
    
    Returns:
        List of activity objects with weekly statistics
    """
    return make_request("GET", "/instance/activity")


# ============================================================================
# HASHTAGS
# ============================================================================

@server.tool()
def get_hashtag(hashtag: str) -> dict:
    """
    Get information about a hashtag.
    
    Args:
        hashtag: The hashtag to look up (without the # symbol)
    
    Returns:
        The hashtag object
    """
    return make_request("GET", f"/tags/{hashtag}")


@server.tool()
def follow_hashtag(hashtag: str) -> dict:
    """
    Follow a hashtag.
    
    Args:
        hashtag: The hashtag to follow (without the # symbol)
    
    Returns:
        The hashtag object
    """
    return make_request("POST", f"/tags/{hashtag}/follow")


@server.tool()
def unfollow_hashtag(hashtag: str) -> dict:
    """
    Unfollow a hashtag.
    
    Args:
        hashtag: The hashtag to unfollow (without the # symbol)
    
    Returns:
        The hashtag object
    """
    return make_request("POST", f"/tags/{hashtag}/unfollow")


# ============================================================================
# FILTERS
# ============================================================================

@server.tool()
def get_filters() -> list:
    """
    Get all filters owned by the authenticated user.
    
    Returns:
        List of filter objects
    """
    return make_request("GET", "/filters")


@server.tool()
def get_filter(filter_id: str) -> dict:
    """
    Get a single filter by ID.
    
    Args:
        filter_id: The ID of the filter
    
    Returns:
        The filter object
    """
    return make_request("GET", f"/filters/{filter_id}")


@server.tool()
def create_filter(
    phrase: str,
    context: list,
    irreversible: bool = False,
    whole_word: bool = False,
    expires_in: Optional[int] = None,
) -> dict:
    """
    Create a new filter.
    
    Args:
        phrase: The text to filter
        context: Array of contexts where the filter applies (e.g., ["home", "public"])
        irreversible: Whether the filter is irreversible
        whole_word: Whether the filter should only match whole words
        expires_in: Number of seconds until the filter expires
    
    Returns:
        The created filter object
    """
    data = {
        "phrase": phrase,
        "context": context,
        "irreversible": irreversible,
        "whole_word": whole_word,
    }
    if expires_in is not None:
        data["expires_in"] = expires_in
    
    return make_request("POST", "/filters", data=data)


@server.tool()
def update_filter(
    filter_id: str,
    phrase: Optional[str] = None,
    context: Optional[list] = None,
    irreversible: Optional[bool] = None,
    whole_word: Optional[bool] = None,
    expires_in: Optional[int] = None,
) -> dict:
    """
    Update a filter.
    
    Args:
        filter_id: The ID of the filter to update
        phrase: The text to filter
        context: Array of contexts where the filter applies
        irreversible: Whether the filter is irreversible
        whole_word: Whether the filter should only match whole words
        expires_in: Number of seconds until the filter expires
    
    Returns:
        The updated filter object
    """
    data = {}
    if phrase is not None:
        data["phrase"] = phrase
    if context is not None:
        data["context"] = context
    if irreversible is not None:
        data["irreversible"] = irreversible
    if whole_word is not None:
        data["whole_word"] = whole_word
    if expires_in is not None:
        data["expires_in"] = expires_in
    
    return make_request("PUT", f"/filters/{filter_id}", data=data)


@server.tool()
def delete_filter(filter_id: str) -> dict:
    """
    Delete a filter.
    
    Args:
        filter_id: The ID of the filter to delete
    
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/filters/{filter_id}")


# ============================================================================
# PREFERENCES
# ============================================================================

@server.tool()
def get_preferences() -> dict:
    """
    Get the authenticated user's preferences.
    
    Returns:
        The preferences object
    """
    return make_request("GET", "/preferences")


# ============================================================================
# ENDORSEMENTS
# ============================================================================

@server.tool()
def get_endorsements() -> list:
    """
    Get the authenticated user's endorsed accounts.
    
    Returns:
        List of account objects
    """
    return make_request("GET", "/endorsements")


@server.tool()
def endorse_account(account_id: str) -> dict:
    """
    Endorse an account.
    
    Args:
        account_id: The ID of the account to endorse
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/pin")


@server.tool()
def unendorse_account(account_id: str) -> dict:
    """
    Unendorse an account.
    
    Args:
        account_id: The ID of the account to unendorse
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/unpin")


# ============================================================================
# TRENDS
# ============================================================================

@server.tool()
def get_trending_statuses(limit: int = 20) -> list:
    """
    Get trending statuses.
    
    Args:
        limit: Maximum number of statuses to return (default 20)
    
    Returns:
        List of status objects
    """
    return make_request("GET", "/trends/statuses", params={"limit": limit})


@server.tool()
def get_trending_tags(limit: int = 20) -> list:
    """
    Get trending hashtags.
    
    Args:
        limit: Maximum number of hashtags to return (default 20)
    
    Returns:
        List of hashtag objects
    """
    return make_request("GET", "/trends/tags", params={"limit": limit})


@server.tool()
def get_trending_accounts(limit: int = 20) -> list:
    """
    Get trending accounts.
    
    Args:
        limit: Maximum number of accounts to return (default 20)
    
    Returns:
        List of account objects
    """
    return make_request("GET", "/trends/accounts", params={"limit": limit})


# ============================================================================
# SUGGESTIONS
# ============================================================================

@server.tool()
def get_suggestions(limit: int = 40) -> list:
    """
    Get account suggestions for the authenticated user.
    
    Args:
        limit: Maximum number of suggestions to return (default 40)
    
    Returns:
        List of account objects
    """
    return make_request("GET", "/suggestions", params={"limit": limit})


@server.tool()
def remove_suggestion(account_id: str) -> dict:
    """
    Remove an account from suggestions.
    
    Args:
        account_id: The ID of the account to remove from suggestions
    
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/suggestions/{account_id}")


# ============================================================================
# CONVERSATIONS
# ============================================================================

@server.tool()
def get_conversations(
    limit: int = 20,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> list:
    """
    Get the authenticated user's conversations.
    
    Args:
        limit: Maximum number of conversations to return (default 20)
        max_id: Return conversations older than this ID
        min_id: Return conversations newer than this ID
    
    Returns:
        List of conversation objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/conversations", params=params)


@server.tool()
def delete_conversation(conversation_id: str) -> dict:
    """
    Delete a conversation.
    
    Args:
        conversation_id: The ID of the conversation to delete
    
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/conversations/{conversation_id}")


# ============================================================================
# REPORTS
# ============================================================================

@server.tool()
def report_account(
    account_id: str,
    comment: Optional[str] = None,
    status_ids: Optional[list] = None,
) -> dict:
    """
    Report an account to the instance moderators.
    
    Args:
        account_id: The ID of the account to report
        comment: Optional comment explaining the report
        status_ids: Optional list of status IDs to include in the report
    
    Returns:
        The report object
    """
    data = {"account_id": account_id}
    if comment:
        data["comment"] = comment
    if status_ids:
        data["status_ids"] = status_ids
    
    return make_request("POST", "/reports", data=data)


if __name__ == "__main__":
    server.run()
