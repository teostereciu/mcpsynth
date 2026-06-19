#!/usr/bin/env python3
"""
Mastodon MCP Server
Comprehensive MCP server for the Mastodon API
"""

import os
from typing import Any
import requests
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="mastodon", log_level="INFO")

# Base URL for Mastodon API
BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/")


def get_auth_headers() -> dict:
    """Get authorization headers from environment variable."""
    token = os.getenv("MASTODON_ACCESS_TOKEN")
    if not token:
        raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")
    return {"Authorization": f"Bearer {token}"}


def mastodon_request(
    method: str,
    endpoint: str,
    params: dict | None = None,
    data: dict | None = None,
) -> dict | list:
    """Make a request to the Mastodon API."""
    headers = get_auth_headers()
    url = f"{BASE_URL}/api/v1{endpoint}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            return {"error": "The access token is invalid"}
        elif response.status_code == 404:
            return {"error": "Record not found"}
        elif response.status_code == 422:
            return {"error": response.json().get("error", "Validation failed")}
        else:
            return {"error": f"HTTP {response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ====================
# Statuses API
# ====================

@mcp.tool(
    description="Post a new status to the user's timeline.",
    annotations={
        "title": "Post Status",
        "readOnly": False,
    },
)
def post_status(
    status: str,
    media_ids: list[str] | None = None,
    poll_options: list[str] | None = None,
    poll_expires_in: int | None = None,
    poll_multiple: bool = False,
    poll_hide_totals: bool = False,
    reply_to_id: str | None = None,
    is_sensitive: bool = False,
    content_warning: str | None = None,
    post_visibility: str = "public",
    lang: str | None = None,
    scheduled_at: str | None = None,
    quoted_status_id: str | None = None,
    quote_approval_policy: str | None = None,
) -> dict:
    """
    POST /api/v1/statuses
    Publish a status with the given parameters.
    """
    data = {
        "status": status,
    }
    
    if media_ids:
        for i, mid in enumerate(media_ids):
            data[f"media_ids[{i}]"] = mid
    
    if poll_options:
        for i, opt in enumerate(poll_options):
            data[f"poll[options][]"] = opt
        if poll_expires_in:
            data["poll[expires_in]"] = poll_expires_in
        data["poll[multiple]"] = str(poll_multiple).lower()
        data["poll[hide_totals]"] = str(poll_hide_totals).lower()
    
    if reply_to_id:
        data["reply_to_id"] = reply_to_id
    
    data["is_sensitive"] = str(is_sensitive).lower()
    
    if content_warning:
        data["content_warning"] = content_warning
    
    data["post_visibility"] = post_visibility
    
    if lang:
        data["lang"] = lang
    
    if scheduled_at:
        data["scheduled_at"] = scheduled_at
    
    if quoted_status_id:
        data["quoted_status_id"] = quoted_status_id
    
    if quote_approval_policy:
        data["quote_approval_policy"] = quote_approval_policy
    
    return mastodon_request("POST", "/statuses", data=data)


@mcp.tool(
    description="Get information about a specific status.",
    annotations={
        "title": "Get Status",
        "readOnly": True,
    },
)
def get_status(status_id: str) -> dict:
    """
    GET /api/v1/statuses/:id
    Obtain information about a status.
    """
    return mastodon_request("GET", f"/statuses/{status_id}")


@mcp.tool(
    description="Delete a status.",
    annotations={
        "title": "Delete Status",
        "readOnly": False,
    },
)
def delete_status(status_id: str, delete_media: bool = False) -> dict:
    """
    DELETE /api/v1/statuses/:id
    Delete one of your own statuses.
    """
    params = {"delete_media": str(delete_media).lower()}
    return mastodon_request("DELETE", f"/statuses/{status_id}", params=params)


@mcp.tool(
    description="Boost (reblog) a status.",
    annotations={
        "title": "Boost Status",
        "readOnly": False,
    },
)
def reblog_status(status_id: str) -> dict:
    """
    POST /api/v1/statuses/:id/reblog
    Boost a status.
    """
    return mastodon_request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool(
    description="Unboost (unreblog) a status.",
    annotations={
        "title": "Unboost Status",
        "readOnly": False,
    },
)
def unreblog_status(status_id: str) -> dict:
    """
    POST /api/v1/statuses/:id/unreblog
    Unboost a status.
    """
    return mastodon_request("POST", f"/statuses/{status_id}/unreblog")


@mcp.tool(
    description="Favourite a status.",
    annotations={
        "title": "Favourite Status",
        "readOnly": False,
    },
)
def favourite_status(status_id: str) -> dict:
    """
    POST /api/v1/statuses/:id/favourite
    Favourite a status.
    """
    return mastodon_request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool(
    description="Unfavourite a status.",
    annotations={
        "title": "Unfavourite Status",
        "readOnly": False,
    },
)
def unfavourite_status(status_id: str) -> dict:
    """
    POST /api/v1/statuses/:id/unfavourite
    Unfavourite a status.
    """
    return mastodon_request("POST", f"/statuses/{status_id}/unfavourite")


@mcp.tool(
    description="Get context (parent and child statuses) for a status.",
    annotations={
        "title": "Get Status Context",
        "readOnly": True,
    },
)
def get_status_context(status_id: str) -> dict:
    """
    GET /api/v1/statuses/:id/context
    View statuses above and below this status in the thread.
    """
    return mastodon_request("GET", f"/statuses/{status_id}/context")


@mcp.tool(
    description="Bookmark a status.",
    annotations={
        "title": "Bookmark Status",
        "readOnly": False,
    },
)
def bookmark_status(status_id: str) -> dict:
    """
    POST /api/v1/statuses/:id/bookmark
    Bookmark a status.
    """
    return mastodon_request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool(
    description="Unbookmark a status.",
    annotations={
        "title": "Unbookmark Status",
        "readOnly": False,
    },
)
def unbookmark_status(status_id: str) -> dict:
    """
    POST /api/v1/statuses/:id/unbookmark
    Unbookmark a status.
    """
    return mastodon_request("POST", f"/statuses/{status_id}/unbookmark")


# ====================
# Accounts API
# ====================

@mcp.tool(
    description="Verify credentials for the authenticated user.",
    annotations={
        "title": "Verify Credentials",
        "readOnly": True,
    },
)
def verify_credentials() -> dict:
    """
    GET /api/v1/accounts/verify_credentials
    Test to make sure that the user token works.
    """
    return mastodon_request("GET", "/accounts/verify_credentials")


@mcp.tool(
    description="Get an account by ID.",
    annotations={
        "title": "Get Account",
        "readOnly": True,
    },
)
def get_account(account_id: str) -> dict:
    """
    GET /api/v1/accounts/:id
    Obtain information about an account.
    """
    return mastodon_request("GET", f"/accounts/{account_id}")


@mcp.tool(
    description="Follow an account.",
    annotations={
        "title": "Follow Account",
        "readOnly": False,
    },
)
def follow_account(account_id: str, reblogs: bool = True) -> dict:
    """
    POST /api/v1/accounts/:id/follow
    Follow an account.
    """
    data = {"reblog": str(reblogs).lower()}
    return mastodon_request("POST", f"/accounts/{account_id}/follow", data=data)


@mcp.tool(
    description="Unfollow an account.",
    annotations={
        "title": "Unfollow Account",
        "readOnly": False,
    },
)
def unfollow_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/unfollow
    Unfollow an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool(
    description="Get followers for an account.",
    annotations={
        "title": "Get Account Followers",
        "readOnly": True,
    },
)
def get_account_followers(account_id: str, limit: int = 40) -> dict:
    """
    GET /api/v1/accounts/:id/followers
    Get followers for an account.
    """
    params = {"limit": limit}
    return mastodon_request("GET", f"/accounts/{account_id}/followers", params=params)


@mcp.tool(
    description="Get accounts followed by an account.",
    annotations={
        "title": "Get Account Following",
        "readOnly": True,
    },
)
def get_account_following(account_id: str, limit: int = 40) -> dict:
    """
    GET /api/v1/accounts/:id/following
    Get accounts followed by an account.
    """
    params = {"limit": limit}
    return mastodon_request("GET", f"/accounts/{account_id}/following", params=params)


@mcp.tool(
    description="Block an account.",
    annotations={
        "title": "Block Account",
        "readOnly": False,
    },
)
def block_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/block
    Block an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/block")


@mcp.tool(
    description="Unblock an account.",
    annotations={
        "title": "Unblock Account",
        "readOnly": False,
    },
)
def unblock_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/unblock
    Unblock an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/unblock")


@mcp.tool(
    description="Mute an account.",
    annotations={
        "title": "Mute Account",
        "readOnly": False,
    },
)
def mute_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/mute
    Mute an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/mute")


@mcp.tool(
    description="Unmute an account.",
    annotations={
        "title": "Unmute Account",
        "readOnly": False,
    },
)
def unmute_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/unmute
    Unmute an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/unmute")


@mcp.tool(
    description="Pin an account (show their posts on profile).",
    annotations={
        "title": "Pin Account",
        "readOnly": False,
    },
)
def pin_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/pin
    Pin an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/pin")


@mcp.tool(
    description="Unpin an account.",
    annotations={
        "title": "Unpin Account",
        "readOnly": False,
    },
)
def unpin_account(account_id: str) -> dict:
    """
    POST /api/v1/accounts/:id/unpin
    Unpin an account.
    """
    return mastodon_request("POST", f"/accounts/{account_id}/unpin")


# ====================
# Timelines API
# ====================

@mcp.tool(
    description="View your home timeline.",
    annotations={
        "title": "Get Home Timeline",
        "readOnly": True,
    },
)
def get_home_timeline(limit: int = 20, max_id: str | None = None, since_id: str | None = None, min_id: str | None = None) -> dict:
    """
    GET /api/v1/timelines/home
    View statuses from followed users and hashtags.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return mastodon_request("GET", "/timelines/home", params=params)


@mcp.tool(
    description="View public timeline.",
    annotations={
        "title": "Get Public Timeline",
        "readOnly": True,
    },
)
def get_public_timeline(
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    limit: int = 20,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
) -> dict:
    """
    GET /api/v1/timelines/public
    View public statuses.
    """
    params = {
        "local": str(local).lower(),
        "remote": str(remote).lower(),
        "only_media": str(only_media).lower(),
        "limit": limit,
    }
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return mastodon_request("GET", "/timelines/public", params=params)


@mcp.tool(
    description="View timeline for a specific hashtag.",
    annotations={
        "title": "Get Hashtag Timeline",
        "readOnly": True,
    },
)
def get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    limit: int = 20,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
) -> dict:
    """
    GET /api/v1/timelines/tag/:hashtag
    View public statuses containing the given hashtag.
    """
    params = {
        "local": str(local).lower(),
        "remote": str(remote).lower(),
        "only_media": str(only_media).lower(),
        "limit": limit,
    }
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return mastodon_request("GET", f"/timelines/tag/{hashtag}", params=params)


@mcp.tool(
    description="View timeline for a specific list.",
    annotations={
        "title": "Get List Timeline",
        "readOnly": True,
    },
)
def get_list_timeline(
    list_id: str,
    limit: int = 20,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
) -> dict:
    """
    GET /api/v1/timelines/list/:list_id
    View statuses in the given list timeline.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return mastodon_request("GET", f"/timelines/list/{list_id}", params=params)


# ====================
# Notifications API
# ====================

@mcp.tool(
    description="Get all notifications.",
    annotations={
        "title": "Get Notifications",
        "readOnly": True,
    },
)
def get_notifications(
    limit: int = 40,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
    types: list[str] | None = None,
    exclude_types: list[str] | None = None,
    account_id: str | None = None,
    include_filtered: bool = False,
) -> dict:
    """
    GET /api/v1/notifications
    Get all notifications concerning the user.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if types:
        for i, t in enumerate(types):
            params[f"types[{i}]"] = t
    if exclude_types:
        for i, t in enumerate(exclude_types):
            params[f"exclude_types[{i}]"] = t
    if account_id:
        params["account_id"] = account_id
    params["include_filtered"] = str(include_filtered).lower()
    return mastodon_request("GET", "/notifications", params=params)


@mcp.tool(
    description="Get a single notification by ID.",
    annotations={
        "title": "Get Notification",
        "readOnly": True,
    },
)
def get_notification(notification_id: str) -> dict:
    """
    GET /api/v1/notifications/:id
    View information about a notification with a given ID.
    """
    return mastodon_request("GET", f"/notifications/{notification_id}")


@mcp.tool(
    description="Dismiss all notifications.",
    annotations={
        "title": "Dismiss All Notifications",
        "readOnly": False,
    },
)
def dismiss_all_notifications() -> dict:
    """
    POST /api/v1/notifications/clear
    Clear all notifications from the server.
    """
    return mastodon_request("POST", "/notifications/clear")


@mcp.tool(
    description="Dismiss a single notification.",
    annotations={
        "title": "Dismiss Notification",
        "readOnly": False,
    },
)
def dismiss_notification(notification_id: str) -> dict:
    """
    POST /api/v1/notifications/:id/dismiss
    Dismiss a single notification from the server.
    """
    return mastodon_request("POST", f"/notifications/{notification_id}/dismiss")


# ====================
# Search API
# ====================

@mcp.tool(
    description="Search for accounts, statuses, and hashtags.",
    annotations={
        "title": "Search",
        "readOnly": True,
    },
)
def search(
    q: str,
    type: str | None = None,
    resolve: bool = False,
    limit: int = 40,
    offset: int | None = None,
) -> dict:
    """
    GET /api/v2/search
    Search for accounts, statuses, and hashtags.
    """
    params = {"q": q, "limit": limit}
    if type:
        params["type"] = type
    params["resolve"] = str(resolve).lower()
    if offset is not None:
        params["offset"] = offset
    return mastodon_request("GET", "/search", params=params)


# ====================
# Lists API
# ====================

@mcp.tool(
    description="Get all lists.",
    annotations={
        "title": "Get Lists",
        "readOnly": True,
    },
)
def get_lists() -> dict:
    """
    GET /api/v1/lists
    Fetch all lists that the user owns.
    """
    return mastodon_request("GET", "/lists")


@mcp.tool(
    description="Get a single list by ID.",
    annotations={
        "title": "Get List",
        "readOnly": True,
    },
)
def get_list(list_id: str) -> dict:
    """
    GET /api/v1/lists/:id
    Fetch the list with the given ID.
    """
    return mastodon_request("GET", f"/lists/{list_id}")


@mcp.tool(
    description="Create a new list.",
    annotations={
        "title": "Create List",
        "readOnly": False,
    },
)
def create_list(
    title: str,
    replies_policy: str = "list",
    exclusive: bool = False,
) -> dict:
    """
    POST /api/v1/lists
    Create a new list.
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": str(exclusive).lower(),
    }
    return mastodon_request("POST", "/lists", data=data)


@mcp.tool(
    description="Update a list.",
    annotations={
        "title": "Update List",
        "readOnly": False,
    },
)
def update_list(
    list_id: str,
    title: str,
    replies_policy: str = "list",
    exclusive: bool = False,
) -> dict:
    """
    PUT /api/v1/lists/:id
    Change the properties of a list.
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": str(exclusive).lower(),
    }
    return mastodon_request("PUT", f"/lists/{list_id}", data=data)


@mcp.tool(
    description="Delete a list.",
    annotations={
        "title": "Delete List",
        "readOnly": False,
    },
)
def delete_list(list_id: str) -> dict:
    """
    DELETE /api/v1/lists/:id
    Delete a list.
    """
    return mastodon_request("DELETE", f"/lists/{list_id}")


@mcp.tool(
    description="Add accounts to a list.",
    annotations={
        "title": "Add Accounts to List",
        "readOnly": False,
    },
)
def add_accounts_to_list(list_id: str, account_ids: list[str]) -> dict:
    """
    POST /api/v1/lists/:id/accounts
    Add accounts to the given list.
    """
    data = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    return mastodon_request("POST", f"/lists/{list_id}/accounts", data=data)


@mcp.tool(
    description="Remove accounts from a list.",
    annotations={
        "title": "Remove Accounts from List",
        "readOnly": False,
    },
)
def remove_accounts_from_list(list_id: str, account_ids: list[str]) -> dict:
    """
    DELETE /api/v1/lists/:id/accounts
    Remove accounts from the given list.
    """
    data = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    return mastodon_request("DELETE", f"/lists/{list_id}/accounts", data=data)


# ====================
# Bookmarks API
# ====================

@mcp.tool(
    description="Get bookmarked statuses.",
    annotations={
        "title": "Get Bookmarks",
        "readOnly": True,
    },
)
def get_bookmarks(limit: int = 40, max_id: str | None = None, since_id: str | None = None, min_id: str | None = None) -> dict:
    """
    GET /api/v1/bookmarks
    Get bookmarked statuses.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return mastodon_request("GET", "/bookmarks", params=params)


# ====================
# Favourites API
# ====================

@mcp.tool(
    description="Get favourited statuses.",
    annotations={
        "title": "Get Favourites",
        "readOnly": True,
    },
)
def get_favourites(limit: int = 40, max_id: str | None = None, since_id: str | None = None, min_id: str | None = None) -> dict:
    """
    GET /api/v1/favourites
    Get favourited statuses.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return mastodon_request("GET", "/favourites", params=params)


# ====================
# Media API
# ====================

@mcp.tool(
    description="Upload a media attachment.",
    annotations={
        "title": "Upload Media",
        "readOnly": False,
    },
)
def upload_media(
    file_path: str,
    description: str | None = None,
    focus: str | None = None,
) -> dict:
    """
    POST /api/v2/media
    Upload a media attachment.
    """
    headers = get_auth_headers()
    url = f"{BASE_URL}/api/v2/media"
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            
            response = requests.post(
                url=url,
                headers=headers,
                files=files,
                data=data,
                timeout=60,
            )
            response.raise_for_status()
            return response.json()
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ====================
# Instance API
# ====================

@mcp.tool(
    description="Get instance information.",
    annotations={
        "title": "Get Instance Info",
        "readOnly": True,
    },
)
def get_instance_info() -> dict:
    """
    GET /api/v1/instance
    Get instance info and statistics.
    """
    return mastodon_request("GET", "/instance")


@mcp.tool(
    description="Get instance activity statistics.",
    annotations={
        "title": "Get Instance Activity",
        "readOnly": True,
    },
)
def get_instance_activity() -> dict:
    """
    GET /api/v1/instance/activity
    Get instance activity statistics.
    """
    return mastodon_request("GET", "/instance/activity")


if __name__ == "__main__":
    mcp.run()
