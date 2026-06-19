#!/usr/bin/env python3
"""
MCP Server for Mastodon API
Provides tools for interacting with Mastodon instances
"""

import os
import requests
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("mastodon")

# Get base URL and access token from environment
BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")

def make_request(method: str, endpoint: str, params: Optional[dict] = None, 
                 data: Optional[dict] = None, files: Optional[dict] = None) -> dict | list | str:
    """Make authenticated request to Mastodon API"""
    url = f"{BASE_URL}/api/v1{endpoint}"
    headers = {}
    if ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    
    try:
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=data, files=files, headers=headers)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers)
        elif method == "PATCH":
            response = requests.patch(url, data=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, params=params, headers=headers)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        
        # Handle empty responses
        if not response.content:
            return {}
        
        return response.json()
    
    except requests.exceptions.HTTPError as e:
        if e.response is not None:
            try:
                return {"error": e.response.json()}
            except:
                return {"error": e.response.text}
        return {"error": str(e)}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_account_by_id(account_id: str) -> dict:
    """
    Get information about a specific account by ID.
    
    Args:
        account_id: The ID of the account to retrieve
        
    Returns:
        Account information including username, display name, followers, etc.
    """
    return make_request("GET", f"/accounts/{account_id}")


@mcp.tool()
def get_authenticated_account() -> dict:
    """
    Get the authenticated user's account information.
    
    Returns:
        The current user's account details including profile info, stats, etc.
    """
    return make_request("GET", "/accounts/verify_credentials")


@mcp.tool()
def follow_account(account_id: str) -> dict:
    """
    Follow an account.
    
    Args:
        account_id: The ID of the account to follow
        
    Returns:
        Account information after following
    """
    return make_request("POST", f"/accounts/{account_id}/follow")


@mcp.tool()
def unfollow_account(account_id: str) -> dict:
    """
    Unfollow an account.
    
    Args:
        account_id: The ID of the account to unfollow
        
    Returns:
        Account information after unfollowing
    """
    return make_request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool()
def get_account_followers(account_id: str, limit: int = 40) -> list:
    """
    Get followers of an account.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of results to return (default 40, max 80)
        
    Returns:
        List of follower accounts
    """
    return make_request("GET", f"/accounts/{account_id}/followers", params={"limit": limit})


@mcp.tool()
def get_account_following(account_id: str, limit: int = 40) -> list:
    """
    Get accounts followed by an account.
    
    Args:
        account_id: The ID of the account
        limit: Maximum number of results to return (default 40, max 80)
        
    Returns:
        List of followed accounts
    """
    return make_request("GET", f"/accounts/{account_id}/following", params={"limit": limit})


@mcp.tool()
def post_status(
    status: str,
    media_ids: Optional[list[str]] = None,
    poll_options: Optional[list[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    in_reply_to_id: Optional[str] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None
) -> dict:
    """
    Post a new status.
    
    Args:
        status: The text content of the status
        media_ids: Array of media attachment IDs to attach
        poll_options: Array of poll answer options
        poll_expires_in: Duration the poll should be open (seconds)
        poll_multiple: Allow multiple choices? (default false)
        poll_hide_totals: Hide vote counts until poll ends? (default false)
        in_reply_to_id: ID of status being replied to
        sensitive: Mark status and media as sensitive? (default false)
        spoiler_text: Text to be shown as warning before content
        visibility: Sets visibility to 'public', 'unlisted', 'private', 'direct'
        language: ISO 639-1 language code
        scheduled_at: Datetime at which to schedule status
        quoted_status_id: ID of status being quoted
        quote_approval_policy: Who can quote: 'public', 'followers', 'nobody'
        
    Returns:
        Created status or scheduled status information
    """
    data = {"status": status}
    
    if media_ids:
        data["media_ids[]"] = media_ids
    if poll_options:
        data["poll[options][]"] = poll_options
    if poll_expires_in is not None:
        data["poll[expires_in]"] = poll_expires_in
    if poll_multiple is not None:
        data["poll[multiple]"] = poll_multiple
    if poll_hide_totals is not None:
        data["poll[hide_totals]"] = poll_hide_totals
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if sensitive is not None:
        data["sensitive"] = sensitive
    if spoiler_text:
        data["spoiler_text"] = spoiler_text
    if visibility:
        data["visibility"] = visibility
    if language:
        data["language"] = language
    if scheduled_at:
        data["scheduled_at"] = scheduled_at
    if quoted_status_id:
        data["quoted_status_id"] = quoted_status_id
    if quote_approval_policy:
        data["quote_approval_policy"] = quote_approval_policy
    
    return make_request("POST", "/statuses", data=data)


@mcp.tool()
def get_status_by_id(status_id: str) -> dict:
    """
    Get information about a specific status by ID.
    
    Args:
        status_id: The ID of the status to retrieve
        
    Returns:
        Status information including content, account, stats, etc.
    """
    return make_request("GET", f"/statuses/{status_id}")


@mcp.tool()
def delete_status(status_id: str, delete_media: Optional[bool] = None) -> dict:
    """
    Delete one of your own statuses.
    
    Args:
        status_id: The ID of the status to delete
        delete_media: Whether to immediately delete media attachments
        
    Returns:
        Deleted status information with source properties
    """
    params = {}
    if delete_media is not None:
        params["delete_media"] = delete_media
    
    return make_request("DELETE", f"/statuses/{status_id}", params=params)


@mcp.tool()
def reblog_status(status_id: str) -> dict:
    """
    Boost (reblog) a status.
    
    Args:
        status_id: The ID of the status to reblog
        
    Returns:
        The reblogged status information
    """
    return make_request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def favourite_status(status_id: str) -> dict:
    """
    Favourite a status.
    
    Args:
        status_id: The ID of the status to favourite
        
    Returns:
        The favourited status information
    """
    return make_request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def unfavourite_status(status_id: str) -> dict:
    """
    Unfavourite a status.
    
    Args:
        status_id: The ID of the status to unfavourite
        
    Returns:
        The unfavourited status information
    """
    return make_request("POST", f"/statuses/{status_id}/unfavourite")


@mcp.tool()
def get_status_context(status_id: str) -> dict:
    """
    Get parent and child statuses in context (thread).
    
    Args:
        status_id: The ID of the status
        
    Returns:
        Context with ancestors and descendants arrays
    """
    return make_request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def bookmark_status(status_id: str) -> dict:
    """
    Bookmark a status.
    
    Args:
        status_id: The ID of the status to bookmark
        
    Returns:
        The bookmarked status information
    """
    return make_request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> dict:
    """
    Remove a status from bookmarks.
    
    Args:
        status_id: The ID of the status to unbookmark
        
    Returns:
        The unbookmarked status information
    """
    return make_request("POST", f"/statuses/{status_id}/unbookmark")


@mcp.tool()
def get_home_timeline(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> list:
    """
    Get home timeline (statuses from followed users and hashtags).
    
    Args:
        max_id: Upper bound on results (lesser than this ID)
        since_id: Lower bound on results (greater than this ID)
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of status objects in the home timeline
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/timelines/home", params=params)


@mcp.tool()
def get_public_timeline(
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> list:
    """
    Get public timeline statuses.
    
    Args:
        local: Show only local statuses? (default false)
        remote: Show only remote statuses? (default false)
        only_media: Show only statuses with media? (default false)
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of public status objects
    """
    params = {"limit": limit}
    if local is not None:
        params["local"] = local
    if remote is not None:
        params["remote"] = remote
    if only_media is not None:
        params["only_media"] = only_media
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/timelines/public", params=params)


@mcp.tool()
def get_hashtag_timeline(
    hashtag: str,
    any_tags: Optional[list[str]] = None,
    all_tags: Optional[list[str]] = None,
    none_tags: Optional[list[str]] = None,
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> list:
    """
    Get public statuses containing a specific hashtag.
    
    Args:
        hashtag: The hashtag name (without # symbol)
        any_tags: Return statuses with any of these additional tags
        all_tags: Return statuses with all of these additional tags
        none_tags: Return statuses without any of these additional tags
        local: Return only local statuses? (default false)
        remote: Return only remote statuses? (default false)
        only_media: Return only statuses with media? (default false)
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of status objects with the hashtag
    """
    params = {"limit": limit}
    
    if any_tags:
        params["any[]"] = any_tags
    if all_tags:
        params["all[]"] = all_tags
    if none_tags:
        params["none[]"] = none_tags
    if local is not None:
        params["local"] = local
    if remote is not None:
        params["remote"] = remote
    if only_media is not None:
        params["only_media"] = only_media
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", f"/timelines/tag/{hashtag}", params=params)


@mcp.tool()
def get_list_timeline(
    list_id: str,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> list:
    """
    Get statuses in a list timeline.
    
    Args:
        list_id: The ID of the list
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of status objects in the list timeline
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", f"/timelines/list/{list_id}", params=params)


@mcp.tool()
def list_notifications(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 40,
    types: Optional[list[str]] = None,
    exclude_types: Optional[list[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = None
) -> list:
    """
    Get all notifications for the user.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 40, max 80)
        types: Types to include in results
        exclude_types: Types to exclude from results
        account_id: Return only notifications from this account
        include_filtered: Include filtered notifications? (default false)
        
    Returns:
        List of notification objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if types:
        params["types[]"] = types
    if exclude_types:
        params["exclude_types[]"] = exclude_types
    if account_id:
        params["account_id"] = account_id
    if include_filtered is not None:
        params["include_filtered"] = include_filtered
    
    return make_request("GET", "/notifications", params=params)


@mcp.tool()
def get_notification_by_id(notification_id: str) -> dict:
    """
    Get information about a specific notification.
    
    Args:
        notification_id: The ID of the notification
        
    Returns:
        Notification information including account and status
    """
    return make_request("GET", f"/notifications/{notification_id}")


@mcp.tool()
def dismiss_notification(notification_id: str) -> dict:
    """
    Dismiss a single notification.
    
    Args:
        notification_id: The ID of the notification to dismiss
        
    Returns:
        Empty object on success
    """
    return make_request("POST", f"/notifications/{notification_id}/dismiss")


@mcp.tool()
def clear_all_notifications() -> dict:
    """
    Clear all notifications from the server.
    
    Returns:
        Empty object on success
    """
    return make_request("POST", "/notifications/clear")


@mcp.tool()
def search_accounts_statuses_hashtags(
    q: str,
    type: Optional[str] = None,
    resolve: Optional[bool] = None,
    following: Optional[bool] = None,
    account_id: Optional[str] = None,
    exclude_unreviewed: Optional[bool] = None,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20,
    offset: Optional[int] = None
) -> dict:
    """
    Search for accounts, statuses, and hashtags.
    
    Args:
        q: The search query
        type: Specify 'accounts', 'hashtags', 'statuses'
        resolve: Attempt WebFinger lookup for remote accounts? (default false)
        following: Only include accounts the user is following? (default false)
        account_id: If provided, only return statuses by this account
        exclude_unreviewed: Filter out unreviewed tags? (default false)
        max_id: Upper bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results per category (default 20, max 40)
        offset: Skip first n results
        
    Returns:
        Search results with accounts, statuses, and hashtags arrays
    """
    params = {
        "q": q,
        "limit": limit
    }
    if type:
        params["type"] = type
    if resolve is not None:
        params["resolve"] = resolve
    if following is not None:
        params["following"] = following
    if account_id:
        params["account_id"] = account_id
    if exclude_unreviewed is not None:
        params["exclude_unreviewed"] = exclude_unreviewed
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    if offset is not None:
        params["offset"] = offset
    
    return make_request("GET", "/search", params=params)


@mcp.tool()
def create_list(
    title: str,
    replies_policy: Optional[str] = None,
    exclusive: Optional[bool] = None
) -> dict:
    """
    Create a new list.
    
    Args:
        title: The title of the list
        replies_policy: One of 'followed', 'list', or 'none' (default 'list')
        exclusive: Whether members need to be removed from Home feed? (default false)
        
    Returns:
        The created list information
    """
    data = {"title": title}
    if replies_policy:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = exclusive
    
    return make_request("POST", "/lists", data=data)


@mcp.tool()
def get_list_by_id(list_id: str) -> dict:
    """
    Get information about a specific list.
    
    Args:
        list_id: The ID of the list
        
    Returns:
        List information including title, replies policy, etc.
    """
    return make_request("GET", f"/lists/{list_id}")


@mcp.tool()
def update_list(
    list_id: str,
    title: str,
    replies_policy: Optional[str] = None,
    exclusive: Optional[bool] = None
) -> dict:
    """
    Update a list's properties.
    
    Args:
        list_id: The ID of the list to update
        title: The new title for the list
        replies_policy: One of 'followed', 'list', or 'none'
        exclusive: Whether members need to be removed from Home feed?
        
    Returns:
        Updated list information
    """
    data = {"title": title}
    if replies_policy:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = exclusive
    
    return make_request("PUT", f"/lists/{list_id}", data=data)


@mcp.tool()
def delete_list(list_id: str) -> dict:
    """
    Delete a list.
    
    Args:
        list_id: The ID of the list to delete
        
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def get_accounts_in_list(list_id: str, limit: int = 40) -> list:
    """
    Get accounts in a list.
    
    Args:
        list_id: The ID of the list
        limit: Maximum results to return (default 40, max 80)
        
    Returns:
        List of account objects in the list
    """
    return make_request("GET", f"/lists/{list_id}/accounts", params={"limit": limit})


@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: list[str]) -> dict:
    """
    Add accounts to a list.
    
    Args:
        list_id: The ID of the list
        account_ids: Array of account IDs to add
        
    Returns:
        Empty object on success
    """
    data = {"account_ids[]": account_ids}
    return make_request("POST", f"/lists/{list_id}/accounts", data=data)


@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: list[str]) -> dict:
    """
    Remove accounts from a list.
    
    Args:
        list_id: The ID of the list
        account_ids: Array of account IDs to remove
        
    Returns:
        Empty object on success
    """
    data = {"account_ids[]": account_ids}
    return make_request("DELETE", f"/lists/{list_id}/accounts", data=data)


@mcp.tool()
def get_bookmarks(max_id: Optional[str] = None, since_id: Optional[str] = None,
                  min_id: Optional[str] = None, limit: int = 20) -> list:
    """
    Get statuses the user has bookmarked.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of bookmarked status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/bookmarks", params=params)


@mcp.tool()
def get_favourites(max_id: Optional[str] = None, since_id: Optional[str] = None,
                   min_id: Optional[str] = None, limit: int = 20) -> list:
    """
    Get statuses the user has favourited.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of favourited status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/favourites", params=params)


@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None,
                 focus: Optional[str] = None) -> dict:
    """
    Upload media as an attachment to be used with statuses.
    
    Args:
        file_path: Path to the file to upload
        description: Plain-text description for accessibility
        focus: Two floating points (x,y) comma-delimited, ranging from -1.0 to 1.0
        
    Returns:
        Media attachment information including ID for use with status posting
    """
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            
            return make_request("POST", "/media", files=files, data=data)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_info() -> dict:
    """
    Get server information about the Mastodon instance.
    
    Returns:
        Instance information including version, usage stats, configuration, etc.
    """
    return make_request("GET", "/instance")


@mcp.tool()
def get_account_by_username(username: str) -> dict:
    """
    Look up an account by username.
    
    Args:
        username: The username to look up (can be local or remote like user@domain)
        
    Returns:
        Account information if found
    """
    return make_request("GET", "/accounts/lookup", params={"acct": username})


@mcp.tool()
def mute_account(account_id: str, duration: Optional[int] = None) -> dict:
    """
    Mute an account.
    
    Args:
        account_id: The ID of the account to mute
        duration: Number of seconds to mute (default: permanent)
        
    Returns:
        Account information after muting
    """
    params = {}
    if duration is not None:
        params["duration"] = duration
    
    return make_request("POST", f"/accounts/{account_id}/mute", params=params)


@mcp.tool()
def unmute_account(account_id: str) -> dict:
    """
    Unmute an account.
    
    Args:
        account_id: The ID of the account to unmute
        
    Returns:
        Account information after unmuting
    """
    return make_request("POST", f"/accounts/{account_id}/unmute")


@mcp.tool()
def block_account(account_id: str) -> dict:
    """
    Block an account.
    
    Args:
        account_id: The ID of the account to block
        
    Returns:
        Account information after blocking
    """
    return make_request("POST", f"/accounts/{account_id}/block")


@mcp.tool()
def unblock_account(account_id: str) -> dict:
    """
    Unblock an account.
    
    Args:
        account_id: The ID of the account to unblock
        
    Returns:
        Account information after unblocking
    """
    return make_request("POST", f"/accounts/{account_id}/unblock")


@mcp.tool()
def pin_account(account_id: str) -> dict:
    """
    Pin an account (pin their posts to your profile).
    
    Args:
        account_id: The ID of the account to pin
        
    Returns:
        Account information after pinning
    """
    return make_request("POST", f"/accounts/{account_id}/pin")


@mcp.tool()
def unpin_account(account_id: str) -> dict:
    """
    Unpin an account.
    
    Args:
        account_id: The ID of the account to unpin
        
    Returns:
        Account information after unpinning
    """
    return make_request("POST", f"/accounts/{account_id}/unpin")


@mcp.tool()
def mute_status(status_id: str) -> dict:
    """
    Mute a status (hide from timeline).
    
    Args:
        status_id: The ID of the status to mute
        
    Returns:
        Status information after muting
    """
    return make_request("POST", f"/statuses/{status_id}/mute")


@mcp.tool()
def unmute_status(status_id: str) -> dict:
    """
    Unmute a status.
    
    Args:
        status_id: The ID of the status to unmute
        
    Returns:
        Status information after unmuting
    """
    return make_request("POST", f"/statuses/{status_id}/unmute")


@mcp.tool()
def pin_status(status_id: str) -> dict:
    """
    Pin a status to your profile.
    
    Args:
        status_id: The ID of the status to pin
        
    Returns:
        Status information after pinning
    """
    return make_request("POST", f"/statuses/{status_id}/pin")


@mcp.tool()
def unpin_status(status_id: str) -> dict:
    """
    Unpin a status from your profile.
    
    Args:
        status_id: The ID of the status to unpin
        
    Returns:
        Status information after unpinning
    """
    return make_request("POST", f"/statuses/{status_id}/unpin")


if __name__ == "__main__":
    mcp.run()
 Delete a list.
    
    Args:
        list_id: The ID of the list to delete
        
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def get_accounts_in_list(
    list_id: str,
    limit: int = 40
) -> list:
    """
    Get accounts in a list.
    
    Args:
        list_id: The ID of the list
        limit: Maximum results to return (default 40, max 80)
        
    Returns:
        List of account objects in the list
    """
    return make_request("GET", f"/lists/{list_id}/accounts", params={"limit": limit})


@mcp.tool()
def add_accounts_to_list(
    list_id: str,
    account_ids: list[str]
) -> dict:
    """
    Add accounts to a list.
    
    Args:
        list_id: The ID of the list
        account_ids: Array of account IDs to add
        
    Returns:
        Empty object on success
    """
    data = {"account_ids[]": account_ids}
    return make_request("POST", f"/lists/{list_id}/accounts", data=data)


@mcp.tool()
def remove_accounts_from_list(
    list_id: str,
    account_ids: list[str]
) -> dict:
    """
    Remove accounts from a list.
    
    Args:
        list_id: The ID of the list
        account_ids: Array of account IDs to remove
        
    Returns:
        Empty object on success
    """
    data = {"account_ids[]": account_ids}
    return make_request("DELETE", f"/lists/{list_id}/accounts", data=data)


@mcp.tool()
def get_bookmarks(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> list:
    """
    Get statuses the user has bookmarked.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of bookmarked status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/bookmarks", params=params)


@mcp.tool()
def get_favourites(
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: int = 20
) -> list:
    """
    Get statuses the user has favourited.
    
    Args:
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor for results newer than this ID
        limit: Maximum results to return (default 20, max 40)
        
    Returns:
        List of favourited status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    
    return make_request("GET", "/favourites", params=params)


@mcp.tool()
def upload_media(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None
) -> dict:
    """
    Upload media as an attachment to be used with statuses.
    
    Args:
        file_path: Path to the file to upload
        description: Plain-text description for accessibility
        focus: Two floating points (x,y) comma-delimited, ranging from -1.0 to 1.0
        
    Returns:
        Media attachment information including ID for use with status posting
    """
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            
            return make_request("POST", "/media", files=files, data=data)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_info() -> dict:
    """
    Get server information about the Mastodon instance.
    
    Returns:
        Instance information including version, usage stats, configuration, etc.
    """
    return make_request("GET", "/instance")


@mcp.tool()
def get_account_by_username(username: str) -> dict:
    """
    Look up an account by username.
    
    Args:
        username: The username to look up (can be local or remote like user@domain)
        
    Returns:
        Account information if found
    """
    return make_request("GET", f"/accounts/lookup", params={"acct": username})


@mcp.tool()
def update_account_credentials(
    display_name: Optional[str] = None,
    note: Optional[str] = None,
    locked: Optional[bool] = None,
    bot: Optional[bool] = None,
    discoverable: Optional[bool] = None,
    hide_collections: Optional[bool] = None,
    indexable: Optional[bool] = None,
    privacy: Optional[str] = None,
    sensitive: Optional[bool] = None,
    language: Optional[str] = None,
    quote_policy: Optional[str] = None,
    fields_attributes: Optional[dict] = None
) -> dict:
    """
    Update the authenticated user's account credentials.
    
    Args:
        display_name: The display name to use for the profile
        note: The account bio
        locked: Whether manual approval of follow requests is required
        bot: Whether the account has a bot flag
        discoverable: Whether the account should be shown in profile directory
        hide_collections: Whether to hide followers and followed accounts
        indexable: Whether public posts should be searchable
        privacy: Default post privacy ('public', 'unlisted', 'private')
        sensitive: Whether to mark posts as sensitive by default
        language: Default language for authored statuses
        quote_policy: Default quote policy ('public', 'followers', 'nobody')
        fields_attributes: Dictionary of profile fields to set
        
    Returns:
        Updated account information
    """
    data = {}
    if display_name:
        data["display_name"] = display_name
    if note:
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
    if privacy:
        data["source[privacy]"] = privacy
    if sensitive is not None:
        data["source[sensitive]"] = sensitive
    if language:
        data["source[language]"] = language
    if quote_policy:
        data["source[quote_policy]"] = quote_policy
    if fields_attributes:
        # Convert fields_attributes to the expected format
        for idx, field in fields_attributes.items():
            data[f"fields_attributes[{idx}][name]"] = field.get("name", "")
            data[f"fields_attributes[{idx}][value]"] = field.get("value", "")
    
    return make_request("PATCH", "/accounts/update_credentials", data=data)


@mcp.tool()
def mute_account(account_id: str, duration: Optional[int] = None) -> dict:
    """
    Mute an account.
    
    Args:
        account_id: The ID of the account to mute
        duration: Number of seconds to mute (default: permanent)
        
    Returns:
        Account information after muting
    """
    params = {}
    if duration is not None:
        params["duration"] = duration
    
    return make_request("POST", f"/accounts/{account_id}/mute", params=params)


@mcp.tool()
def unmute_account(account_id: str) -> dict:
    """
    Unmute an account.
    
    Args:
        account_id: The ID of the account to unmute
        
    Returns:
        Account information after unmuting
    """
    return make_request("POST", f"/accounts/{account_id}/unmute")


@mcp.tool()
def block_account(account_id: str) -> dict:
    """
    Block an account.
    
    Args:
        account_id: The ID of the account to block
        
    Returns:
        Account information after blocking
    """
    return make_request("POST", f"/accounts/{account_id}/block")


@mcp.tool()
def unblock_account(account_id: str) -> dict:
    """
    Unblock an account.
    
    Args:
        account_id: The ID of the account to unblock
        
    Returns:
        Account information after unblocking
    """
    return make_request("POST", f"/accounts/{account_id}/unblock")


@mcp.tool()
def pin_account(account_id: str) -> dict:
    """
    Pin an account (pin their posts to your profile).
    
    Args:
        account_id: The ID of the account to pin
        
    Returns:
        Account information after pinning
    """
    return make_request("POST", f"/accounts/{account_id}/pin")


@mcp.tool()
def unpin_account(account_id: str) -> dict:
    """
    Unpin an account.
    
    Args:
        account_id: The ID of the account to unpin
        
    Returns:
        Account information after unpinning
    """
    return make_request("POST", f"/accounts/{account_id}/unpin")


@mcp.tool()
def mute_status(status_id: str) -> dict:
    """
    Mute a status (hide from timeline).
    
    Args:
        status_id: The ID of the status to mute
        
    Returns:
        Status information after muting
    """
    return make_request("POST", f"/statuses/{status_id}/mute")


@mcp.tool()
def unmute_status(status_id: str) -> dict:
    """
    Unmute a status.
    
    Args:
        status_id: The ID of the status to unmute
        
    Returns:
        Status information after unmuting
    """
    return make_request("POST", f"/statuses/{status_id}/unmute")


@mcp.tool()
def pin_status(status_id: str) -> dict:
    """
    Pin a status to your profile.
    
    Args:
        status_id: The ID of the status to pin
        
    Returns:
        Status information after pinning
    """
    return make_request("POST", f"/statuses/{status_id}/pin")


@mcp.tool()
def unpin_status(status_id: str) -> dict:
    """
    Unpin a status from your profile.
    
    Args:
        status_id: The ID of the status to unpin
        
    Returns:
        Status information after unpinning
    """
    return make_request("POST", f"/statuses/{status_id}/unpin")


if __name__ == "__main__":
    mcp.run()
