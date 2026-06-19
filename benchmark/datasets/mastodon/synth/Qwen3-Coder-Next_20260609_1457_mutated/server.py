#!/usr/bin/env python3
"""
Mastodon MCP Server

An MCP server with comprehensive coverage of the Mastodon REST API.
"""

import os
import requests
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("mastodon")

# Configuration
BASE_URL = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")


def _make_request(method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make a request to the Mastodon API."""
    url = f"{BASE_URL}/api/v1{endpoint}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"} if ACCESS_TOKEN else {}
    
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# Statuses
# ============================================================================

@mcp.tool()
def post_status(
    status: str,
    media_ids: Optional[List[str]] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: bool = False,
    poll_hide_totals: bool = False,
    reply_to_id: Optional[str] = None,
    is_sensitive: bool = False,
    content_warning: Optional[str] = None,
    post_visibility: str = "public",
    lang: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None
) -> Dict[str, Any]:
    """
    Post a new status to the user's timeline.
    
    Args:
        status: The text content of the status
        media_ids: List of media IDs to attach
        poll_options: Options for a poll
        poll_expires_in: Duration in seconds for poll
        poll_multiple: Allow multiple choices
        poll_hide_totals: Hide vote counts until poll ends
        reply_to_id: ID of status being replied to
        is_sensitive: Mark as sensitive
        content_warning: Text to show before content
        post_visibility: public, unlisted, private, or direct
        lang: ISO 639-1 language code
        scheduled_at: Schedule timestamp
        quoted_status_id: ID of status being quoted
        quote_approval_policy: Who can quote this post
        
    Returns:
        The created status or scheduled status
    """
    data = {
        "status": status,
        "media_ids": media_ids,
        "poll[options][]": poll_options,
        "poll[expires_in]": poll_expires_in,
        "poll[multiple]": poll_multiple,
        "poll[hide_totals]": poll_hide_totals,
        "reply_to_id": reply_to_id,
        "is_sensitive": is_sensitive,
        "content_warning": content_warning,
        "post_visibility": post_visibility,
        "lang": lang,
        "scheduled_at": scheduled_at,
        "quoted_status_id": quoted_status_id,
        "quote_approval_policy": quote_approval_policy,
    }
    # Filter out None values
    data = {k: v for k, v in data.items() if v is not None}
    return _make_request("POST", "/statuses", data=data)


@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """
    Get information about a specific status.
    
    Args:
        status_id: The ID of the status
        
    Returns:
        Status information
    """
    return _make_request("GET", f"/statuses/{status_id}")


@mcp.tool()
def delete_status(status_id: str, delete_media: bool = False) -> Dict[str, Any]:
    """
    Delete one of your own statuses.
    
    Args:
        status_id: The ID of the status to delete
        delete_media: Whether to immediately delete media attachments
        
    Returns:
        Deleted status information
    """
    params = {"delete_media": delete_media}
    return _make_request("DELETE", f"/statuses/{status_id}", params=params)


@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    """
    Get parent and child statuses in context.
    
    Args:
        status_id: The ID of the status
        
    Returns:
        Context with ancestors and descendants
    """
    return _make_request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def get_statuses(status_ids: List[str]) -> List[Dict[str, Any]]:
    """
    Get information about multiple statuses.
    
    Args:
        status_ids: List of status IDs
        
    Returns:
        List of status information
    """
    params = {"id[]": status_ids}
    return _make_request("GET", "/statuses", params=params)


@mcp.tool()
def reblog_status(status_id: str) -> Dict[str, Any]:
    """
    Boost (reblog) a status.
    
    Args:
        status_id: The ID of the status to reblog
        
    Returns:
        The reblogged status
    """
    return _make_request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    """
    Favourite a status.
    
    Args:
        status_id: The ID of the status to favourite
        
    Returns:
        The favourited status
    """
    return _make_request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """
    Unfavourite a status.
    
    Args:
        status_id: The ID of the status to unfavourite
        
    Returns:
        The unfavourited status
    """
    return _make_request("POST", f"/statuses/{status_id}/unfavourite")


@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    """
    Bookmark a status.
    
    Args:
        status_id: The ID of the status to bookmark
        
    Returns:
        The bookmarked status
    """
    return _make_request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """
    Remove a status from bookmarks.
    
    Args:
        status_id: The ID of the status to unbookmark
        
    Returns:
        The unbookmarked status
    """
    return _make_request("POST", f"/statuses/{status_id}/unbookmark")


# ============================================================================
# Timelines
# ============================================================================

@mcp.tool()
def get_home_timeline(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    View statuses from followed users and hashtags.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of status information
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", "/timelines/home", params=params)


@mcp.tool()
def get_public_timeline(
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    View public statuses.
    
    Args:
        local: Show only local statuses
        remote: Show only remote statuses
        only_media: Show only statuses with media
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of status information
    """
    params = {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", "/timelines/public", params=params)


@mcp.tool()
def get_hashtag_timeline(
    hashtag: str,
    any_tags: Optional[List[str]] = None,
    all_tags: Optional[List[str]] = None,
    none_tags: Optional[List[str]] = None,
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    View public statuses containing a specific hashtag.
    
    Args:
        hashtag: The hashtag (without #)
        any_tags: Any of these additional tags
        all_tags: All of these additional tags
        none_tags: None of these additional tags
        local: Show only local statuses
        remote: Show only remote statuses
        only_media: Show only statuses with media
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of status information
    """
    params = {
        "any[]": any_tags,
        "all[]": all_tags,
        "none[]": none_tags,
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", f"/timelines/tag/{hashtag}", params=params)


@mcp.tool()
def get_list_timeline(
    list_id: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    View statuses in a list timeline.
    
    Args:
        list_id: The ID of the list
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of status information
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", f"/timelines/list/{list_id}", params=params)


@mcp.tool()
def get_link_timeline(
    url: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    View public statuses containing a link to a trending article.
    
    Args:
        url: The URL of the trending article
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of status information
    """
    params = {
        "url": url,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", "/timelines/link", params=params)


# ============================================================================
# Accounts
# ============================================================================

@mcp.tool()
def get_current_account() -> Dict[str, Any]:
    """
    Verify account credentials and get current user information.
    
    Returns:
        Current account information
    """
    return _make_request("GET", "/accounts/verify_credentials")


@mcp.tool()
def update_account(
    display_name: Optional[str] = None,
    note: Optional[str] = None,
    avatar: Optional[str] = None,
    header: Optional[str] = None,
    locked: Optional[bool] = None,
    bot: Optional[bool] = None,
    discoverable: Optional[bool] = None,
    hide_collections: Optional[bool] = None,
    indexable: Optional[bool] = None,
    attribution_domains: Optional[List[str]] = None,
    fields_attributes: Optional[Dict[str, Dict[str, str]]] = None,
    source_privacy: Optional[str] = None,
    source_is_sensitive: Optional[bool] = None,
    source_lang: Optional[str] = None,
    source_quote_policy: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update account credentials and preferences.
    
    Args:
        display_name: Display name for profile
        note: Account bio
        avatar: Avatar image (multipart)
        header: Header image (multipart)
        locked: Require manual approval of follow requests
        bot: Set bot flag
        discoverable: Show in profile directory
        hide_collections: Hide followers/followed accounts
        indexable: Make public posts searchable
        attribution_domains: Allowed domains for credit
        fields_attributes: Profile fields to set
        source_privacy: Default post privacy
        source_is_sensitive: Mark posts as sensitive by default
        source_lang: Default language
        source_quote_policy: Default quote policy
        
    Returns:
        Updated account information
    """
    data = {
        "display_name": display_name,
        "note": note,
        "avatar": avatar,
        "header": header,
        "locked": locked,
        "bot": bot,
        "discoverable": discoverable,
        "hide_collections": hide_collections,
        "indexable": indexable,
        "attribution_domains[]": attribution_domains,
        "fields_attributes": fields_attributes,
        "source[privacy]": source_privacy,
        "source[is_sensitive]": source_is_sensitive,
        "source[lang]": source_lang,
        "source[quote_policy]": source_quote_policy,
    }
    # Filter out None values
    data = {k: v for k, v in data.items() if v is not None}
    return _make_request("PATCH", "/accounts/update_credentials", data=data)


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """
    Get account information by ID.
    
    Args:
        account_id: The account ID
        
    Returns:
        Account information
    """
    return _make_request("GET", f"/accounts/{account_id}")


@mcp.tool()
def follow_account(account_id: str, reblog: bool = True) -> Dict[str, Any]:
    """
    Follow an account.
    
    Args:
        account_id: The account ID to follow
        reblog: Show reblogs in timeline (default: True)
        
    Returns:
        Relationship information
    """
    data = {"reblog": reblog}
    return _make_request("POST", f"/accounts/{account_id}/follow", data=data)


@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    """
    Unfollow an account.
    
    Args:
        account_id: The account ID to unfollow
        
    Returns:
        Relationship information
    """
    return _make_request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool()
def block_account(account_id: str) -> Dict[str, Any]:
    """
    Block an account.
    
    Args:
        account_id: The account ID to block
        
    Returns:
        Account information
    """
    return _make_request("POST", f"/accounts/{account_id}/block")


@mcp.tool()
def unblock_account(account_id: str) -> Dict[str, Any]:
    """
    Unblock an account.
    
    Args:
        account_id: The account ID to unblock
        
    Returns:
        Account information
    """
    return _make_request("POST", f"/accounts/{account_id}/unblock")


@mcp.tool()
def mute_account(account_id: str, notifications: bool = True) -> Dict[str, Any]:
    """
    Mute an account.
    
    Args:
        account_id: The account ID to mute
        notifications: Mute notifications (default: True)
        
    Returns:
        Account information
    """
    data = {"notifications": notifications}
    return _make_request("POST", f"/accounts/{account_id}/mute", data=data)


@mcp.tool()
def unmute_account(account_id: str) -> Dict[str, Any]:
    """
    Unmute an account.
    
    Args:
        account_id: The account ID to unmute
        
    Returns:
        Account information
    """
    return _make_request("POST", f"/accounts/{account_id}/unmute")


@mcp.tool()
def get_account_followers(
    account_id: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 40
) -> List[Dict[str, Any]]:
    """
    Get followers for an account.
    
    Args:
        account_id: The account ID
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 80)
        
    Returns:
        List of follower accounts
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", f"/accounts/{account_id}/followers", params=params)


@mcp.tool()
def get_account_following(
    account_id: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 40
) -> List[Dict[str, Any]]:
    """
    Get accounts followed by an account.
    
    Args:
        account_id: The account ID
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 80)
        
    Returns:
        List of following accounts
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", f"/accounts/{account_id}/following", params=params)


@mcp.tool()
def get_account_status(
    account_id: str,
    status_id: str
) -> Dict[str, Any]:
    """
    Get a specific status from an account.
    
    Args:
        account_id: The account ID
        status_id: The status ID
        
    Returns:
        Status information
    """
    return _make_request("GET", f"/accounts/{account_id}/statuses/{status_id}")


@mcp.tool()
def get_account_statuses(
    account_id: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20,
    only_media: bool = False,
    pinned: bool = False
) -> List[Dict[str, Any]]:
    """
    Get statuses from an account.
    
    Args:
        account_id: The account ID
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        only_media: Show only statuses with media
        pinned: Show only pinned statuses
        
    Returns:
        List of status information
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit,
        "only_media": only_media,
        "pinned": pinned
    }
    return _make_request("GET", f"/accounts/{account_id}/statuses", params=params)


@mcp.tool()
def get_account_lists(account_id: str) -> List[Dict[str, Any]]:
    """
    Get lists that include an account.
    
    Args:
        account_id: The account ID
        
    Returns:
        List of lists
    """
    return _make_request("GET", f"/accounts/{account_id}/lists")


@mcp.tool()
def get_account_identity_proofs(account_id: str) -> List[Dict[str, Any]]:
    """
    Get identity proofs for an account.
    
    Args:
        account_id: The account ID
        
    Returns:
        List of identity proofs
    """
    return _make_request("GET", f"/accounts/{account_id}/identity_proofs")


# ============================================================================
# Notifications
# ============================================================================

@mcp.tool()
def get_notifications(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 40,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: bool = False
) -> List[Dict[str, Any]]:
    """
    Get notifications for the current user.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 80)
        types: Types to include (mention, status, reblog, follow, follow_request, favourite, poll, update, admin.sign_up, admin.report)
        exclude_types: Types to exclude
        account_id: Filter by account
        include_filtered: Include filtered notifications
        
    Returns:
        List of notification information
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit,
        "types[]": types,
        "exclude_types[]": exclude_types,
        "account_id": account_id,
        "include_filtered": include_filtered
    }
    return _make_request("GET", "/notifications", params=params)


@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    """
    Get information about a specific notification.
    
    Args:
        notification_id: The notification ID
        
    Returns:
        Notification information
    """
    return _make_request("GET", f"/notifications/{notification_id}")


@mcp.tool()
def clear_notifications() -> Dict[str, Any]:
    """
    Clear all notifications.
    
    Returns:
        Empty response
    """
    return _make_request("POST", "/notifications/clear")


@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """
    Dismiss a specific notification.
    
    Args:
        notification_id: The notification ID to dismiss
        
    Returns:
        Empty response
    """
    return _make_request("POST", f"/notifications/{notification_id}/dismiss")


@mcp.tool()
def get_unread_count(
    limit: int = 100,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None,
    account_id: Optional[str] = None
) -> Dict[str, int]:
    """
    Get the number of unread notifications.
    
    Args:
        limit: Maximum number of results (max 1000)
        types: Types of notifications to count
        exclude_types: Types of notifications to exclude
        account_id: Filter by account
        
    Returns:
        Count of unread notifications
    """
    params = {
        "limit": limit,
        "types[]": types,
        "exclude_types[]": exclude_types,
        "account_id": account_id
    }
    return _make_request("GET", "/notifications/unread_count", params=params)


# ============================================================================
# Lists
# ============================================================================

@mcp.tool()
def get_lists() -> List[Dict[str, Any]]:
    """
    Get all lists owned by the current user.
    
    Returns:
        List of lists
    """
    return _make_request("GET", "/lists")


@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    """
    Get information about a specific list.
    
    Args:
        list_id: The list ID
        
    Returns:
        List information
    """
    return _make_request("GET", f"/lists/{list_id}")


@mcp.tool()
def create_list(
    title: str,
    replies_policy: str = "list",
    exclusive: bool = False
) -> Dict[str, Any]:
    """
    Create a new list.
    
    Args:
        title: The title of the list
        replies_policy: One of followed, list, or none
        exclusive: Whether members need to be removed from Home feed
        
    Returns:
        Created list information
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": exclusive
    }
    return _make_request("POST", "/lists", data=data)


@mcp.tool()
def update_list(
    list_id: str,
    title: str,
    replies_policy: str = "list",
    exclusive: bool = False
) -> Dict[str, Any]:
    """
    Update a list.
    
    Args:
        list_id: The list ID
        title: The new title
        replies_policy: One of followed, list, or none
        exclusive: Whether members need to be removed from Home feed
        
    Returns:
        Updated list information
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": exclusive
    }
    return _make_request("PUT", f"/lists/{list_id}", data=data)


@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    """
    Delete a list.
    
    Args:
        list_id: The list ID
        
    Returns:
        Empty response
    """
    return _make_request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def get_list_accounts(
    list_id: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 40
) -> List[Dict[str, Any]]:
    """
    Get accounts in a list.
    
    Args:
        list_id: The list ID
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 80)
        
    Returns:
        List of accounts
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", f"/lists/{list_id}/accounts", params=params)


@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """
    Add accounts to a list.
    
    Args:
        list_id: The list ID
        account_ids: List of account IDs to add
        
    Returns:
        Empty response
    """
    data = {"account_ids[]": account_ids}
    return _make_request("POST", f"/lists/{list_id}/accounts", data=data)


@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """
    Remove accounts from a list.
    
    Args:
        list_id: The list ID
        account_ids: List of account IDs to remove
        
    Returns:
        Empty response
    """
    params = {"account_ids[]": account_ids}
    return _make_request("DELETE", f"/lists/{list_id}/accounts", params=params)


# ============================================================================
# Bookmarks
# ============================================================================

@mcp.tool()
def get_bookmarks(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    Get bookmarked statuses.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of bookmarked status information
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", "/bookmarks", params=params)


# ============================================================================
# Favourites
# ============================================================================

@mcp.tool()
def get_favourites(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """
    Get favourited statuses.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 40)
        
    Returns:
        List of favourited status information
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", "/favourites", params=params)


# ============================================================================
# Media
# ============================================================================

@mcp.tool()
def upload_media(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail: Optional[str] = None
) -> Dict[str, Any]:
    """
    Upload a media file for use in a status.
    
    Args:
        file_path: Path to the file to upload
        description: Accessibility description
        focus: Focal point as x,y coordinates
        thumbnail: Path to custom thumbnail
        
    Returns:
        Media attachment information
    """
    url = f"{BASE_URL}/api/v2/media"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            if thumbnail:
                files["thumbnail"] = open(thumbnail, "rb")
            
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
                
            response = requests.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_media(media_id: str) -> Dict[str, Any]:
    """
    Get information about a media attachment.
    
    Args:
        media_id: The media ID
        
    Returns:
        Media attachment information
    """
    return _make_request("GET", f"/media/{media_id}")


@mcp.tool()
def update_media(
    media_id: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update a media attachment.
    
    Args:
        media_id: The media ID
        description: Accessibility description
        focus: Focal point as x,y coordinates
        thumbnail: Path to custom thumbnail
        
    Returns:
        Updated media attachment information
    """
    data = {}
    if description:
        data["description"] = description
    if focus:
        data["focus"] = focus
        
    return _make_request("PUT", f"/media/{media_id}", data=data)


@mcp.tool()
def delete_media(media_id: str) -> Dict[str, Any]:
    """
    Delete a media attachment.
    
    Args:
        media_id: The media ID
        
    Returns:
        Empty response
    """
    return _make_request("DELETE", f"/media/{media_id}")


# ============================================================================
# Instance
# ============================================================================

@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    """
    Get information about the Mastodon instance.
    
    Returns:
        Instance information
    """
    return _make_request("GET", "/instance")


# ============================================================================
# Search
# ============================================================================

@mcp.tool()
def search(
    query: str,
    type: Optional[str] = None,
    resolve: bool = False,
    following: bool = False,
    account_id: Optional[str] = None,
    exclude_unreviewed: bool = False,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Search for accounts, statuses, or hashtags.
    
    Args:
        query: The search query
        type: Type to search for (accounts, hashtags, statuses)
        resolve: Attempt WebFinger lookup for remote accounts
        following: Only include accounts user is following
        account_id: Filter by account ID
        exclude_unreviewed: Filter out unreviewed tags
        max_id: Upper bound on results
        min_id: Cursor for forward pagination
        limit: Maximum results per category (max 40)
        offset: Skip first n results
        
    Returns:
        Search results with accounts, statuses, and hashtags
    """
    params = {
        "q": query,
        "type": type,
        "resolve": resolve,
        "following": following,
        "account_id": account_id,
        "exclude_unreviewed": exclude_unreviewed,
        "max_id": max_id,
        "min_id": min_id,
        "limit": limit,
        "offset": offset
    }
    return _make_request("GET", "/search", params=params)


# ============================================================================
# Blocks
# ============================================================================

@mcp.tool()
def get_blocked_accounts(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 40
) -> List[Dict[str, Any]]:
    """
    Get blocked accounts.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for forward pagination
        limit: Maximum number of results (max 80)
        
    Returns:
        List of blocked accounts
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit
    }
    return _make_request("GET", "/blocks", params=params)


# ============================================================================
# Mutes
# ============================================================================

@mcp.tool()
def get_muted_accounts(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    limit: int = 40
) -> List[Dict[str, Any]]:
    """
    Get muted accounts.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        limit: Maximum number of results (max 80)
        
    Returns:
        List of muted accounts
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "limit": limit
    }
    return _make_request("GET", "/mutes", params=params)


# ============================================================================
# Follow Requests
# ============================================================================

@mcp.tool()
def get_follow_requests(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    limit: int = 40
) -> List[Dict[str, Any]]:
    """
    Get pending follow requests.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        limit: Maximum number of results (max 80)
        
    Returns:
        List of accounts with pending follow requests
    """
    params = {
        "max_id": max_id,
        "since_id": since_id,
        "limit": limit
    }
    return _make_request("GET", "/follow_requests", params=params)


@mcp.tool()
def authorize_follow_request(account_id: str) -> Dict[str, Any]:
    """
    Accept a follow request.
    
    Args:
        account_id: The account ID to authorize
        
    Returns:
        Relationship information
    """
    return _make_request("POST", f"/follow_requests/{account_id}/authorize")


@mcp.tool()
def reject_follow_request(account_id: str) -> Dict[str, Any]:
    """
    Reject a follow request.
    
    Args:
        account_id: The account ID to reject
        
    Returns:
        Relationship information
    """
    return _make_request("POST", f"/follow_requests/{account_id}/reject")


# ============================================================================
# Main entry point
# ============================================================================

if __name__ == "__main__":
    mcp.run()
