#!/usr/bin/env python3
"""
Mastodon MCP Server
A Model Context Protocol server for Mastodon API
"""

import os
import sys
import time
import json
import requests
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("mastodon")

# Configuration from environment
MASTODON_ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")
MASTODON_BASE_URL = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social")

def get_base_url() -> str:
    """Get the base Mastodon instance URL."""
    return MASTODON_BASE_URL.rstrip('/')

def get_auth_headers() -> Dict[str, str]:
    """Get authorization headers for Mastodon API."""
    return {
        "Authorization": f"Bearer {MASTODON_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

def api_request(method: str, endpoint: str, params: Dict[str, Any] = None, 
                data: Dict[str, Any] = None, files: Dict[str, Any] = None) -> Dict[str, Any]:
    """Make a request to the Mastodon API."""
    base_url = get_base_url()
    url = f"{base_url}/api/v1{endpoint}"
    
    headers = get_auth_headers()
    if files:
        headers.pop("Content-Type", None)
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            files=files,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Statuses endpoints

@mcp.tool()
def post_status(status: str, media_ids: List[str] = None, 
                poll_options: List[str] = None, poll_expires_in: int = None,
                poll_multiple: bool = False, poll_hide_totals: bool = False,
                in_reply_to_id: str = None, sensitive: bool = False,
                spoiler_text: str = None, visibility: str = "public",
                language: str = None, scheduled_at: str = None,
                quoted_status_id: str = None, 
                quote_approval_policy: str = None) -> Dict[str, Any]:
    """
    Publish a new status to Mastodon.
    
    Args:
        status: The text content of the status
        media_ids: List of media attachment IDs to attach
        poll_options: List of poll options if creating a poll
        poll_expires_in: Duration in seconds for poll to be open
        poll_multiple: Allow multiple choices
        poll_hide_totals: Hide vote counts until poll ends
        in_reply_to_id: ID of status being replied to
        sensitive: Mark content as sensitive
        spoiler_text: Warning text before content
        visibility: public, unlisted, private, or direct
        language: ISO 639-1 language code
        scheduled_at: Datetime to schedule the post
        quoted_status_id: ID of status being quoted
        quote_approval_policy: Who can quote: public, followers, or nobody
    
    Returns:
        Status object if posted immediately, ScheduledStatus if scheduled
    """
    data = {"status": status}
    if media_ids:
        data["media_ids"] = media_ids
    if poll_options:
        data["poll"] = {"options": poll_options, "expires_in": poll_expires_in or 86400}
        data["poll"]["multiple"] = poll_multiple
        data["poll"]["hide_totals"] = poll_hide_totals
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    data["sensitive"] = sensitive
    if spoiler_text:
        data["spoiler_text"] = spoiler_text
    data["visibility"] = visibility
    if language:
        data["language"] = language
    if scheduled_at:
        data["scheduled_at"] = scheduled_at
    if quoted_status_id:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy:
        data["quote_approval_policy"] = quote_approval_policy
    
    return api_request("POST", "/statuses", data=data)

@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """
    Get information about a status.
    
    Args:
        status_id: The ID of the Status in the database
    
    Returns:
        Status object with details
    """
    return api_request("GET", f"/statuses/{status_id}")

@mcp.tool()
def delete_status(status_id: str, delete_media: bool = False) -> Dict[str, Any]:
    """
    Delete one of your own statuses.
    
    Args:
        status_id: The ID of the Status to delete
        delete_media: Whether to immediately delete media attachments
    
    Returns:
        Status object with source text and poll/media_attachments
    """
    params = {"delete_media": delete_media}
    return api_request("DELETE", f"/statuses/{status_id}", params=params)

@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    """
    Get parent and child statuses in a thread context.
    
    Args:
        status_id: The ID of the Status
    
    Returns:
        Context object with ancestors and descendants arrays
    """
    return api_request("GET", f"/statuses/{status_id}/context")

@mcp.tool()
def boost_status(status_id: str) -> Dict[str, Any]:
    """
    Boost (reblog) a status.
    
    Args:
        status_id: The ID of the Status to boost
    
    Returns:
        The boosted Status object
    """
    return api_request("POST", f"/statuses/{status_id}/reblog")

@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    """
    Favourite a status.
    
    Args:
        status_id: The ID of the Status to favourite
    
    Returns:
        The favourited Status object
    """
    return api_request("POST", f"/statuses/{status_id}/favourite")

@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """
    Unfavourite a status.
    
    Args:
        status_id: The ID of the Status to unfavourite
    
    Returns:
        The unfavourited Status object
    """
    return api_request("POST", f"/statuses/{status_id}/unfavourite")

@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    """
    Bookmark a status.
    
    Args:
        status_id: The ID of the Status to bookmark
    
    Returns:
        The bookmarked Status object
    """
    return api_request("POST", f"/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """
    Remove a bookmark from a status.
    
    Args:
        status_id: The ID of the Status to unbookmark
    
    Returns:
        The unbookmarked Status object
    """
    return api_request("POST", f"/statuses/{status_id}/unbookmark")

@mcp.tool()
def get_bookmarked_statuses(limit: int = 20) -> List[Dict[str, Any]]:
    """
    Get statuses the user has bookmarked.
    
    Args:
        limit: Maximum number of results (max 40)
    
    Returns:
        Array of bookmarked Status objects
    """
    params = {"limit": min(limit, 40)}
    return api_request("GET", "/bookmarks", params=params)

@mcp.tool()
def get_favourited_statuses(limit: int = 20) -> List[Dict[str, Any]]:
    """
    Get statuses the user has favourited.
    
    Args:
        limit: Maximum number of results (max 40)
    
    Returns:
        Array of favourited Status objects
    """
    params = {"limit": min(limit, 40)}
    return api_request("GET", "/favourites", params=params)

@mcp.tool()
def translate_status(status_id: str) -> Dict[str, Any]:
    """
    Translate a status content.
    
    Args:
        status_id: The ID of the Status to translate
    
    Returns:
        Translation object with translated content
    """
    return api_request("POST", f"/statuses/{status_id}/translate")

# Accounts endpoints

@mcp.tool()
def verify_credentials() -> Dict[str, Any]:
    """
    Verify account credentials and get current user info.
    
    Returns:
        CredentialAccount object with user details
    """
    return api_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def update_credentials(display_name: str = None, note: str = None,
                      avatar: str = None, header: str = None,
                      locked: bool = None, bot: bool = None,
                      discoverable: bool = None, hide_collections: bool = None,
                      indexable: bool = None, fields_attributes: Dict[str, Dict] = None,
                      source_privacy: str = None, source_sensitive: bool = None,
                      source_language: str = None, quote_policy: str = None) -> Dict[str, Any]:
    """
    Update account credentials and profile.
    
    Args:
        display_name: The display name for the profile
        note: The account bio
        avatar: Avatar image (base64 encoded)
        header: Header image (base64 encoded)
        locked: Whether manual approval of follow requests is required
        bot: Whether the account has a bot flag
        discoverable: Whether the account should be shown in directory
        hide_collections: Whether to hide followers and followed accounts
        indexable: Whether public posts should be searchable
        fields_attributes: Profile fields to set
        source_privacy: Default post privacy (public, unlisted, private)
        source_sensitive: Whether to mark posts as sensitive by default
        source_language: Default language for posts
        quote_policy: Default quote policy (public, followers, nobody)
    
    Returns:
        Updated CredentialAccount object
    """
    data = {}
    if display_name is not None:
        data["display_name"] = display_name
    if note is not None:
        data["note"] = note
    if locked is not None:
        data["locked"] = locked
    if bot is not None:
        data["bot"] = bot
    if discoverable is not None:
        data["discoverable"] = discoverable
    if hide_collections is not None:
        data["hide_collections"] = hide_collections
    if indexable is not None:
        data["indexable"] = indexable
    if fields_attributes:
        data["fields_attributes"] = fields_attributes
    if source_privacy:
        data["source[privacy]"] = source_privacy
    if source_sensitive is not None:
        data["source[sensitive]"] = source_sensitive
    if source_language:
        data["source[language]"] = source_language
    if quote_policy:
        data["source[quote_policy]"] = quote_policy
    
    files = {}
    if avatar:
        files["avatar"] = ("avatar.jpg", avatar, "image/jpeg")
    if header:
        files["header"] = ("header.jpg", header, "image/jpeg")
    
    return api_request("PATCH", "/accounts/update_credentials", 
                      data=data, files=files if files else None)

@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """
    Get account information by ID.
    
    Args:
        account_id: The ID of the Account
    
    Returns:
        Account object with details
    """
    return api_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def get_account_statuses(account_id: str, only_media: bool = False,
                         pinned: bool = False, exclude_replies: bool = False,
                         limit: int = 20) -> List[Dict[str, Any]]:
    """
    Get statuses for a specific account.
    
    Args:
        account_id: The ID of the Account
        only_media: Show only statuses with media
        pinned: Show only pinned statuses
        exclude_replies: Exclude replies
        limit: Maximum number of results (max 40)
    
    Returns:
        Array of Status objects
    """
    params = {"limit": min(limit, 40)}
    if only_media:
        params["only_media"] = True
    if pinned:
        params["pinned"] = True
    if exclude_replies:
        params["exclude_replies"] = True
    
    return api_request("GET", f"/accounts/{account_id}/statuses", params=params)

@mcp.tool()
def follow_account(account_id: str, reblogs: bool = True) -> Dict[str, Any]:
    """
    Follow an account.
    
    Args:
        account_id: The ID of the Account to follow
        reblogs: Whether to receive reblogs in feed
    
    Returns:
        Relationship object
    """
    data = {"id": account_id}
    if reblogs is not None:
        data["reblogs"] = reblogs
    return api_request("POST", f"/accounts/{account_id}/follow", data=data)

@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    """
    Unfollow an account.
    
    Args:
        account_id: The ID of the Account to unfollow
    
    Returns:
        Relationship object
    """
    return api_request("POST", f"/accounts/{account_id}/unfollow")

@mcp.tool()
def get_followers(account_id: str, limit: int = 20) -> List[Dict[str, Any]]:
    """
    Get followers for an account.
    
    Args:
        account_id: The ID of the Account
        limit: Maximum number of results (max 80)
    
    Returns:
        Array of Account objects
    """
    params = {"limit": min(limit, 80)}
    return api_request("GET", f"/accounts/{account_id}/followers", params=params)

@mcp.tool()
def get_following(account_id: str, limit: int = 20) -> List[Dict[str, Any]]:
    """
    Get accounts followed by an account.
    
    Args:
        account_id: The ID of the Account
        limit: Maximum number of results (max 80)
    
    Returns:
        Array of Account objects
    """
    params = {"limit": min(limit, 80)}
    return api_request("GET", f"/accounts/{account_id}/following", params=params)

@mcp.tool()
def block_account(account_id: str) -> Dict[str, Any]:
    """
    Block an account.
    
    Args:
        account_id: The ID of the Account to block
    
    Returns:
        Relationship object
    """
    return api_request("POST", f"/accounts/{account_id}/block")

@mcp.tool()
def unblock_account(account_id: str) -> Dict[str, Any]:
    """
    Unblock an account.
    
    Args:
        account_id: The ID of the Account to unblock
    
    Returns:
        Relationship object
    """
    return api_request("POST", f"/accounts/{account_id}/unblock")

@mcp.tool()
def mute_account(account_id: str, notifications: bool = True) -> Dict[str, Any]:
    """
    Mute an account.
    
    Args:
        account_id: The ID of the Account to mute
        notifications: Whether to mute notifications
    
    Returns:
        Relationship object
    """
    data = {"id": account_id, "notifications": notifications}
    return api_request("POST", f"/accounts/{account_id}/mute", data=data)

@mcp.tool()
def unmute_account(account_id: str) -> Dict[str, Any]:
    """
    Unmute an account.
    
    Args:
        account_id: The ID of the Account to unmute
    
    Returns:
        Relationship object
    """
    return api_request("POST", f"/accounts/{account_id}/unmute")

@mcp.tool()
def pin_account(account_id: str) -> Dict[str, Any]:
    """
    Pin an account (shows in profile).
    
    Args:
        account_id: The ID of the Account to pin
    
    Returns:
        Relationship object
    """
    return api_request("POST", f"/accounts/{account_id}/pin")

@mcp.tool()
def unpin_account(account_id: str) -> Dict[str, Any]:
    """
    Unpin an account.
    
    Args:
        account_id: The ID of the Account to unpin
    
    Returns:
        Relationship object
    """
    return api_request("POST", f"/accounts/{account_id}/unpin")

@mcp.tool()
def search_accounts(q: str, resolve: bool = False, limit: int = 20,
                   following: bool = False) -> List[Dict[str, Any]]:
    """
    Search for accounts.
    
    Args:
        q: Search query
        resolve: Attempt WebFinger lookup for remote accounts
        limit: Maximum number of results (max 40)
        following: Only include accounts user is following
    
    Returns:
        Array of Account objects
    """
    params = {"q": q, "limit": min(limit, 40)}
    if resolve:
        params["resolve"] = True
    if following:
        params["following"] = True
    
    results = api_request("GET", "/accounts/search", params=params)
    return results if isinstance(results, list) else []

# Timelines endpoints

@mcp.tool()
def get_home_timeline(limit: int = 20, max_id: str = None, min_id: str = None,
                     since_id: str = None) -> List[Dict[str, Any]]:
    """
    Get statuses from followed users and hashtags.
    
    Args:
        limit: Maximum number of results (max 40)
        max_id: Upper bound on results
        min_id: Lower bound on results
        since_id: Results newer than this ID
    
    Returns:
        Array of Status objects
    """
    params = {"limit": min(limit, 40)}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if since_id:
        params["since_id"] = since_id
    
    return api_request("GET", "/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(local: bool = False, remote: bool = False,
                       only_media: bool = False, limit: int = 20,
                       max_id: str = None, min_id: str = None,
                       since_id: str = None) -> List[Dict[str, Any]]:
    """
    Get public statuses.
    
    Args:
        local: Show only local statuses
        remote: Show only remote statuses
        only_media: Show only statuses with media
        limit: Maximum number of results (max 40)
        max_id: Upper bound on results
        min_id: Lower bound on results
        since_id: Results newer than this ID
    
    Returns:
        Array of Status objects
    """
    params = {"limit": min(limit, 40), "local": local, "remote": remote, 
              "only_media": only_media}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if since_id:
        params["since_id"] = since_id
    
    return api_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: bool = False, remote: bool = False,
                        only_media: bool = False, limit: int = 20,
                        max_id: str = None, min_id: str = None,
                        since_id: str = None) -> List[Dict[str, Any]]:
    """
    Get public statuses containing a hashtag.
    
    Args:
        hashtag: The hashtag name (without #)
        local: Return only local statuses
        remote: Return only remote statuses
        only_media: Return only statuses with media
        limit: Maximum number of results (max 40)
        max_id: Upper bound on results
        min_id: Lower bound on results
        since_id: Results newer than this ID
    
    Returns:
        Array of Status objects
    """
    params = {"limit": min(limit, 40), "local": local, "remote": remote,
              "only_media": only_media}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if since_id:
        params["since_id"] = since_id
    
    return api_request("GET", f"/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20, max_id: str = None,
                     min_id: str = None, since_id: str = None) -> List[Dict[str, Any]]:
    """
    Get statuses from a list timeline.
    
    Args:
        list_id: The ID of the List
        limit: Maximum number of results (max 40)
        max_id: Upper bound on results
        min_id: Lower bound on results
        since_id: Results newer than this ID
    
    Returns:
        Array of Status objects
    """
    params = {"limit": min(limit, 40)}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if since_id:
        params["since_id"] = since_id
    
    return api_request("GET", f"/timelines/list/{list_id}", params=params)

# Notifications endpoints

@mcp.tool()
def get_notifications(limit: int = 40, max_id: str = None, min_id: str = None,
                     since_id: str = None, types: List[str] = None,
                     exclude_types: List[str] = None, account_id: str = None,
                     include_filtered: bool = False) -> List[Dict[str, Any]]:
    """
    Get notifications for the current user.
    
    Args:
        limit: Maximum number of results (max 80)
        max_id: Upper bound on results
        min_id: Lower bound on results
        since_id: Results newer than this ID
        types: Types to include (mention, status, reblog, follow, etc.)
        exclude_types: Types to exclude
        account_id: Return only notifications from this account
        include_filtered: Include filtered notifications
    
    Returns:
        Array of Notification objects
    """
    params = {"limit": min(limit, 80)}
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if since_id:
        params["since_id"] = since_id
    if types:
        params["types[]"] = types
    if exclude_types:
        params["exclude_types[]"] = exclude_types
    if account_id:
        params["account_id"] = account_id
    if include_filtered:
        params["include_filtered"] = True
    
    return api_request("GET", "/notifications", params=params)

@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    """
    Get a single notification by ID.
    
    Args:
        notification_id: The ID of the Notification
    
    Returns:
        Notification object
    """
    return api_request("GET", f"/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """
    Dismiss a single notification.
    
    Args:
        notification_id: The ID of the Notification to dismiss
    
    Returns:
        Empty object
    """
    return api_request("POST", f"/notifications/{notification_id}/dismiss")

@mcp.tool()
def clear_notifications() -> Dict[str, Any]:
    """
    Clear all notifications.
    
    Returns:
        Empty object
    """
    return api_request("POST", "/notifications/clear")

@mcp.tool()
def get_unread_notification_count(limit: int = 100, types: List[str] = None,
                                  exclude_types: List[str] = None,
                                  account_id: str = None) -> Dict[str, int]:
    """
    Get count of unread notifications.
    
    Args:
        limit: Maximum number of results (max 1000)
        types: Types to count
        exclude_types: Types to exclude from count
        account_id: Only count from this account
    
    Returns:
        Dict with 'count' key
    """
    params = {"limit": min(limit, 1000)}
    if types:
        params["types[]"] = types
    if exclude_types:
        params["exclude_types[]"] = exclude_types
    if account_id:
        params["account_id"] = account_id
    
    return api_request("GET", "/notifications/unread_count", params=params)

# Search endpoints

@mcp.tool()
def search(q: str, type: str = None, resolve: bool = False, 
           limit: int = 20, offset: int = 0, account_id: str = None,
           max_id: str = None, min_id: str = None,
           exclude_unreviewed: bool = False) -> Dict[str, Any]:
    """
    Perform a search for accounts, statuses, and hashtags.
    
    Args:
        q: Search query
        type: Type to search (accounts, hashtags, statuses)
        resolve: Attempt WebFinger lookup
        limit: Max results per category (max 40)
        offset: Skip first n results
        account_id: Only search statuses by this account
        max_id: Upper bound on results
        min_id: Lower bound on results
        exclude_unreviewed: Filter out unreviewed tags
    
    Returns:
        Search object with accounts, statuses, and hashtags arrays
    """
    params = {"q": q, "limit": min(limit, 40)}
    if type:
        params["type"] = type
    if resolve:
        params["resolve"] = True
    if offset:
        params["offset"] = offset
    if account_id:
        params["account_id"] = account_id
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if exclude_unreviewed:
        params["exclude_unreviewed"] = True
    
    return api_request("GET", "/search", params=params)

# Lists endpoints

@mcp.tool()
def get_lists() -> List[Dict[str, Any]]:
    """
    Get all lists owned by the user.
    
    Returns:
        Array of List objects
    """
    return api_request("GET", "/lists")

@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    """
    Get a single list by ID.
    
    Args:
        list_id: The ID of the List
    
    Returns:
        List object
    """
    return api_request("GET", f"/lists/{list_id}")

@mcp.tool()
def create_list(title: str, replies_policy: str = "list",
               exclusive: bool = False) -> Dict[str, Any]:
    """
    Create a new list.
    
    Args:
        title: The title of the list
        replies_policy: One of followed, list, or none
        exclusive: Whether list members should be removed from home feed
    
    Returns:
        Created List object
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": exclusive
    }
    return api_request("POST", "/lists", data=data)

@mcp.tool()
def update_list(list_id: str, title: str, replies_policy: str = None,
               exclusive: bool = None) -> Dict[str, Any]:
    """
    Update a list.
    
    Args:
        list_id: The ID of the List
        title: The new title
        replies_policy: One of followed, list, or none
        exclusive: Whether list members should be removed from home feed
    
    Returns:
        Updated List object
    """
    data = {"title": title}
    if replies_policy:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = exclusive
    
    return api_request("PUT", f"/lists/{list_id}", data=data)

@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    """
    Delete a list.
    
    Args:
        list_id: The ID of the List to delete
    
    Returns:
        Empty object
    """
    return api_request("DELETE", f"/lists/{list_id}")

@mcp.tool()
def get_list_accounts(list_id: str, limit: int = 40) -> List[Dict[str, Any]]:
    """
    Get accounts in a list.
    
    Args:
        list_id: The ID of the List
        limit: Maximum number of results (max 80)
    
    Returns:
        Array of Account objects
    """
    params = {"limit": min(limit, 80)}
    return api_request("GET", f"/lists/{list_id}/accounts", params=params)

@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """
    Add accounts to a list.
    
    Args:
        list_id: The ID of the List
        account_ids: Array of account IDs to add
    
    Returns:
        Empty object
    """
    data = {"account_ids[]": account_ids}
    return api_request("POST", f"/lists/{list_id}/accounts", data=data)

@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """
    Remove accounts from a list.
    
    Args:
        list_id: The ID of the List
        account_ids: Array of account IDs to remove
    
    Returns:
        Empty object
    """
    data = {"account_ids[]": account_ids}
    return api_request("DELETE", f"/lists/{list_id}/accounts", data=data)

# Media endpoints

@mcp.tool()
def upload_media(file_path: str, description: str = None, 
                focus: str = None) -> Dict[str, Any]:
    """
    Upload a media file to attach to a status.
    
    Args:
        file_path: Path to the file to upload
        description: Accessibility description
        focus: Focal point as comma-separated x,y coordinates
    
    Returns:
        MediaAttachment object with id for use in status creation
    """
    files = {"file": open(file_path, "rb")}
    data = {}
    if description:
        data["description"] = description
    if focus:
        data["focus"] = focus
    
    try:
        return api_request("POST", "/v2/media", data=data, files=files)
    finally:
        files["file"].close()

@mcp.tool()
def get_media(media_id: str) -> Dict[str, Any]:
    """
    Get information about a media attachment.
    
    Args:
        media_id: The ID of the MediaAttachment
    
    Returns:
        MediaAttachment object
    """
    return api_request("GET", f"/media/{media_id}")

@mcp.tool()
def update_media(media_id: str, description: str = None, focus: str = None,
                thumbnail: str = None) -> Dict[str, Any]:
    """
    Update a media attachment before posting.
    
    Args:
        media_id: The ID of the MediaAttachment
        description: Accessibility description
        focus: Focal point as comma-separated x,y coordinates
        thumbnail: Custom thumbnail file path
    
    Returns:
        Updated MediaAttachment object
    """
    data = {}
    if description:
        data["description"] = description
    if focus:
        data["focus"] = focus
    
    files = {}
    if thumbnail:
        files["thumbnail"] = open(thumbnail, "rb")
    
    try:
        return api_request("PUT", f"/media/{media_id}", data=data, 
                          files=files if files else None)
    finally:
        if files:
            files["thumbnail"].close()

@mcp.tool()
def delete_media(media_id: str) -> Dict[str, Any]:
    """
    Delete a media attachment before posting.
    
    Args:
        media_id: The ID of the MediaAttachment
    
    Returns:
        Empty object
    """
    return api_request("DELETE", f"/media/{media_id}")

# Instance endpoints

@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    """
    Get information about the Mastodon server.
    
    Returns:
        Instance object with server configuration and statistics
    """
    return api_request("GET", "/v2/instance")

@mcp.tool()
def get_instance_rules() -> List[Dict[str, Any]]:
    """
    Get server rules.
    
    Returns:
        Array of Rule objects
    """
    return api_request("GET", "/instance/rules")

# Main entry point
if __name__ == "__main__":
    mcp.run()
