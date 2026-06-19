#!/usr/bin/env python3
"""
Mastodon MCP Server

A Model Context Protocol server implementing the Mastodon REST API.
"""

import os
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    name="Mastodon",
    version="1.0.0",
    description="Mastodon API server for MCP"
)

# Configuration
BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")

def make_request(method: str, endpoint: str, params: dict = None, data: dict = None) -> dict:
    """Make a request to the Mastodon API."""
    url = f"{BASE_URL}/api/v1{endpoint}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, params=params, data=data)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, params=params, data=data)
        elif method.upper() == "PATCH":
            response = requests.patch(url, headers=headers, params=params, data=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            return {"error": "Unauthorized - Invalid or missing access token"}
        elif e.response.status_code == 404:
            return {"error": "Not found - Resource does not exist"}
        elif e.response.status_code == 422:
            return {"error": f"Validation failed: {e.response.text}"}
        else:
            return {"error": f"API error: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except ValueError as e:
        return {"error": f"Failed to parse response: {str(e)}"}


# ===== STATUS OPERATIONS =====

@mcp.tool()
def post_status(
    status: str,
    media_ids: Optional[str] = None,
    poll_options: Optional[str] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = False,
    poll_hide_totals: Optional[bool] = False,
    reply_to_id: Optional[str] = None,
    is_sensitive: Optional[bool] = False,
    content_warning: Optional[str] = None,
    post_visibility: Optional[str] = "public",
    lang: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
) -> dict:
    """Post a new status to Mastodon.
    
    Args:
        status: The text content of the status
        media_ids: Comma-separated list of attachment IDs to attach
        poll_options: Comma-separated list of poll options
        poll_expires_in: Duration the poll should be open, in seconds
        poll_multiple: Allow multiple choices? Defaults to false
        poll_hide_totals: Hide vote counts until the poll ends? Defaults to false
        reply_to_id: ID of the status being replied to
        is_sensitive: Mark status and attached media as sensitive? Defaults to false
        content_warning: Text to be shown as a warning before the actual content
        post_visibility: Sets the post_visibility to 'public', 'unlisted', 'private', 'direct'
        lang: ISO 639-1 language code for this status
        scheduled_at: Datetime at which to schedule a status
        quoted_status_id: ID of the status being quoted
        quote_approval_policy: Who is allowed to quote the status
    """
    data = {"status": status}
    
    if media_ids:
        data["media_ids[]"] = media_ids.split(",")
    if poll_options:
        options = poll_options.split(",")
        for i, option in enumerate(options):
            data[f"poll[options][]"] = option
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
    
    return make_request("POST", "/statuses", data=data)


@mcp.tool()
def get_status(status_id: str) -> dict:
    """View information about a status.
    
    Args:
        status_id: The ID of the Status in the database
    """
    return make_request("GET", f"/statuses/{status_id}")


@mcp.tool()
def delete_status(status_id: str, delete_media: Optional[bool] = False) -> dict:
    """Delete one of your own statuses.
    
    Args:
        status_id: The ID of the Status in the database
        delete_media: Whether to immediately delete the post's media attachments
    """
    params = {"delete_media": str(delete_media).lower()}
    return make_request("DELETE", f"/statuses/{status_id}", params=params)


@mcp.tool()
def reblog_status(status_id: str) -> dict:
    """Boost (reblog) a status.
    
    Args:
        status_id: The ID of the Status to reblog
    """
    return make_request("POST", f"/statuses/{status_id}/reblog")


@mcp.tool()
def unreblog_status(status_id: str) -> dict:
    """Undo a reblog of a status.
    
    Args:
        status_id: The ID of the Status to unreblog
    """
    return make_request("POST", f"/statuses/{status_id}/unreblog")


@mcp.tool()
def favourite_status(status_id: str) -> dict:
    """Favourite a status.
    
    Args:
        status_id: The ID of the Status to favourite
    """
    return make_request("POST", f"/statuses/{status_id}/favourite")


@mcp.tool()
def unfavourite_status(status_id: str) -> dict:
    """Undo favourite of a status.
    
    Args:
        status_id: The ID of the Status to unfavourite
    """
    return make_request("POST", f"/statuses/{status_id}/unfavourite")


@mcp.tool()
def bookmark_status(status_id: str) -> dict:
    """Bookmark a status.
    
    Args:
        status_id: The ID of the Status to bookmark
    """
    return make_request("POST", f"/statuses/{status_id}/bookmark")


@mcp.tool()
def unbookmark_status(status_id: str) -> dict:
    """Undo bookmark of a status.
    
    Args:
        status_id: The ID of the Status to unbookmark
    """
    return make_request("POST", f"/statuses/{status_id}/unbookmark")


@mcp.tool()
def get_status_context(status_id: str) -> dict:
    """Get parent and child statuses in context.
    
    Args:
        status_id: The ID of the Status to get context for
    """
    return make_request("GET", f"/statuses/{status_id}/context")


@mcp.tool()
def translate_status(status_id: str, lang: str) -> dict:
    """Translate a status into a specific language.
    
    Args:
        status_id: The ID of the Status to translate
        lang: Language code to translate to
    """
    data = {"lang": lang}
    return make_request("POST", f"/statuses/{status_id}/translate", data=data)


@mcp.tool()
def pin_status(status_id: str) -> dict:
    """Pin a status.
    
    Args:
        status_id: The ID of the Status to pin
    """
    return make_request("POST", f"/statuses/{status_id}/pin")


@mcp.tool()
def unpin_status(status_id: str) -> dict:
    """Unpin a status.
    
    Args:
        status_id: The ID of the Status to unpin
    """
    return make_request("POST", f"/statuses/{status_id}/unpin")


@mcp.tool()
def mute_status(status_id: str) -> dict:
    """Mute a status.
    
    Args:
        status_id: The ID of the Status to mute
    """
    return make_request("POST", f"/statuses/{status_id}/mute")


@mcp.tool()
def unmute_status(status_id: str) -> dict:
    """Unmute a status.
    
    Args:
        status_id: The ID of the Status to unmute
    """
    return make_request("POST", f"/statuses/{status_id}/unmute")


# ===== ACCOUNT OPERATIONS =====

@mcp.tool()
def verify_credentials() -> dict:
    """Verify account credentials."""
    return make_request("GET", "/accounts/verify_credentials")


@mcp.tool()
def update_credentials(
    display_name: Optional[str] = None,
    note: Optional[str] = None,
    locked: Optional[bool] = None,
    bot: Optional[bool] = None,
    discoverable: Optional[bool] = None,
    hide_collections: Optional[bool] = None,
    indexable: Optional[bool] = None,
    fields_attributes: Optional[str] = None,
    source_privacy: Optional[str] = None,
    source_is_sensitive: Optional[bool] = None,
    source_lang: Optional[str] = None,
    quote_policy: Optional[str] = None,
) -> dict:
    """Update account credentials.
    
    Args:
        display_name: The display name to use for the profile
        note: The account bio
        locked: Whether manual approval of follow requests is required
        bot: Whether the account has a bot flag
        discoverable: Whether the account should be shown in the profile directory
        hide_collections: Whether to hide followers and followed accounts
        indexable: Whether public posts should be searchable
        fields_attributes: JSON string of profile fields attributes
        source_privacy: Default post privacy for authored statuses
        source_is_sensitive: Whether to mark authored statuses as sensitive by default
        source_lang: Default lang to use for authored statuses
        quote_policy: Default quote policy for new posts
    """
    data = {}
    
    if display_name is not None:
        data["display_name"] = display_name
    if note is not None:
        data["note"] = note
    if locked is not None:
        data["locked"] = str(locked).lower()
    if bot is not None:
        data["bot"] = str(bot).lower()
    if discoverable is not None:
        data["discoverable"] = str(discoverable).lower()
    if hide_collections is not None:
        data["hide_collections"] = str(hide_collections).lower()
    if indexable is not None:
        data["indexable"] = str(indexable).lower()
    if fields_attributes is not None:
        data["fields_attributes"] = fields_attributes
    if source_privacy is not None:
        data["source[privacy]"] = source_privacy
    if source_is_sensitive is not None:
        data["source[is_sensitive]"] = str(source_is_sensitive).lower()
    if source_lang is not None:
        data["source[lang]"] = source_lang
    if quote_policy is not None:
        data["source[quote_policy]"] = quote_policy
    
    return make_request("PATCH", "/accounts/update_credentials", data=data)


@mcp.tool()
def get_account(account_id: str) -> dict:
    """View information about an account.
    
    Args:
        account_id: The ID of the Account in the database
    """
    return make_request("GET", f"/accounts/{account_id}")


@mcp.tool()
def get_account_statuses(
    account_id: str,
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View statuses for an account.
    
    Args:
        account_id: The ID of the Account
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", f"/accounts/{account_id}/statuses", params=params)


@mcp.tool()
def follow_account(account_id: str, reblog: Optional[bool] = True) -> dict:
    """Follow an account.
    
    Args:
        account_id: The ID of the Account to follow
        reblog: Whether to show reblogs in the home timeline
    """
    data = {"reblog": str(reblog).lower()}
    return make_request("POST", f"/accounts/{account_id}/follow", data=data)


@mcp.tool()
def unfollow_account(account_id: str) -> dict:
    """Unfollow an account.
    
    Args:
        account_id: The ID of the Account to unfollow
    """
    return make_request("POST", f"/accounts/{account_id}/unfollow")


@mcp.tool()
def block_account(account_id: str) -> dict:
    """Block an account.
    
    Args:
        account_id: The ID of the Account to block
    """
    return make_request("POST", f"/accounts/{account_id}/block")


@mcp.tool()
def unblock_account(account_id: str) -> dict:
    """Unblock an account.
    
    Args:
        account_id: The ID of the Account to unblock
    """
    return make_request("POST", f"/accounts/{account_id}/unblock")


@mcp.tool()
def mute_account(account_id: str) -> dict:
    """Mute an account.
    
    Args:
        account_id: The ID of the Account to mute
    """
    return make_request("POST", f"/accounts/{account_id}/mute")


@mcp.tool()
def unmute_account(account_id: str) -> dict:
    """Unmute an account.
    
    Args:
        account_id: The ID of the Account to unmute
    """
    return make_request("POST", f"/accounts/{account_id}/unmute")


@mcp.tool()
def pin_account(account_id: str) -> dict:
    """Pin an account.
    
    Args:
        account_id: The ID of the Account to pin
    """
    return make_request("POST", f"/accounts/{account_id}/pin")


@mcp.tool()
def unpin_account(account_id: str) -> dict:
    """Unpin an account.
    
    Args:
        account_id: The ID of the Account to unpin
    """
    return make_request("POST", f"/accounts/{account_id}/unpin")


@mcp.tool()
def endorse_account(account_id: str) -> dict:
    """Endorse an account.
    
    Args:
        account_id: The ID of the Account to endorse
    """
    return make_request("POST", f"/accounts/{account_id}/endorse")


@mcp.tool()
def unendorse_account(account_id: str) -> dict:
    """Unendorse an account.
    
    Args:
        account_id: The ID of the Account to unendorse
    """
    return make_request("POST", f"/accounts/{account_id}/unendorse")


@mcp.tool()
def add_account_to_note(account_id: str, comment: str) -> dict:
    """Add a note to an account.
    
    Args:
        account_id: The ID of the Account
        comment: The note content
    """
    data = {"comment": comment}
    return make_request("POST", f"/accounts/{account_id}/note", data=data)


@mcp.tool()
def get_account_relationships(account_ids: str) -> dict:
    """Get relationships with accounts.
    
    Args:
        account_ids: Comma-separated list of account IDs
    """
    params = {"id[]": account_ids.split(",")}
    return make_request("GET", "/accounts/relationships", params=params)


@mcp.tool()
def get_account_followers(
    account_id: str,
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """Get followers for an account.
    
    Args:
        account_id: The ID of the Account
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", f"/accounts/{account_id}/followers", params=params)


@mcp.tool()
def get_account_following(
    account_id: str,
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """Get accounts followed by an account.
    
    Args:
        account_id: The ID of the Account
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", f"/accounts/{account_id}/following", params=params)


@mcp.tool()
def search_accounts(
    q: str,
    limit: Optional[int] = 40,
    following: Optional[bool] = False,
) -> dict:
    """Search for accounts.
    
    Args:
        q: The search query
        limit: Maximum number of results to return
        following: Only include accounts that the user is following
    """
    params = {"q": q, "limit": limit, "following": str(following).lower()}
    return make_request("GET", "/accounts/search", params=params)


# ===== TIMELINE OPERATIONS =====

@mcp.tool()
def get_home_timeline(
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View statuses from followed users.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
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
    local: Optional[bool] = False,
    remote: Optional[bool] = False,
    only_media: Optional[bool] = False,
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View public statuses.
    
    Args:
        local: Show only local statuses? Defaults to false
        remote: Show only remote statuses? Defaults to false
        only_media: Show only statuses with media attached? Defaults to false
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
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
    return make_request("GET", "/timelines/public", params=params)


@mcp.tool()
def get_hashtag_timeline(
    hashtag: str,
    any_tags: Optional[str] = None,
    all_tags: Optional[str] = None,
    none_tags: Optional[str] = None,
    local: Optional[bool] = False,
    remote: Optional[bool] = False,
    only_media: Optional[bool] = False,
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View public statuses containing a hashtag.
    
    Args:
        hashtag: The name of the hashtag (not including #)
        any_tags: Comma-separated list of additional tags to match any of
        all_tags: Comma-separated list of additional tags to match all of
        none_tags: Comma-separated list of additional tags to match none of
        local: Return only local statuses? Defaults to false
        remote: Return only remote statuses? Defaults to false
        only_media: Return only statuses with media attachments? Defaults to false
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    
    if any_tags:
        for tag in any_tags.split(","):
            params["any[]"] = tag
    if all_tags:
        for tag in all_tags.split(","):
            params["all[]"] = tag
    if none_tags:
        for tag in none_tags.split(","):
            params["none[]"] = tag
    
    params["local"] = str(local).lower()
    params["remote"] = str(remote).lower()
    params["only_media"] = str(only_media).lower()
    
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
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View statuses in a list timeline.
    
    Args:
        list_id: Local ID of the List
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", f"/timelines/list/{list_id}", params=params)


# ===== NOTIFICATION OPERATIONS =====

@mcp.tool()
def get_notifications(
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    types: Optional[str] = None,
    exclude_types: Optional[str] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = False,
) -> dict:
    """Get all notifications.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
        types: Comma-separated list of types to include
        exclude_types: Comma-separated list of types to exclude
        account_id: Return only notifications from this account
        include_filtered: Whether to include filtered notifications
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if types:
        params["types[]"] = types.split(",")
    if exclude_types:
        params["exclude_types[]"] = exclude_types.split(",")
    if account_id:
        params["account_id"] = account_id
    params["include_filtered"] = str(include_filtered).lower()
    
    return make_request("GET", "/notifications", params=params)


@mcp.tool()
def get_notification(notification_id: str) -> dict:
    """Get a single notification.
    
    Args:
        notification_id: The ID of the Notification
    """
    return make_request("GET", f"/notifications/{notification_id}")


@mcp.tool()
def clear_notifications() -> dict:
    """Clear all notifications."""
    return make_request("POST", "/notifications/clear")


@mcp.tool()
def dismiss_notification(notification_id: str) -> dict:
    """Dismiss a single notification.
    
    Args:
        notification_id: The ID of the Notification
    """
    return make_request("POST", f"/notifications/{notification_id}/dismiss")


@mcp.tool()
def get_unread_notification_count(
    limit: Optional[int] = 100,
    types: Optional[str] = None,
    exclude_types: Optional[str] = None,
    account_id: Optional[str] = None,
) -> dict:
    """Get the number of unread notifications.
    
    Args:
        limit: Maximum number of results to count
        types: Comma-separated list of types to count
        exclude_types: Comma-separated list of types to exclude from count
        account_id: Only count notifications from this account
    """
    params = {"limit": limit}
    if types:
        params["types[]"] = types.split(",")
    if exclude_types:
        params["exclude_types[]"] = exclude_types.split(",")
    if account_id:
        params["account_id"] = account_id
    return make_request("GET", "/notifications/unread_count", params=params)


# ===== SEARCH OPERATIONS =====

@mcp.tool()
def search(
    q: str,
    type: Optional[str] = None,
    resolve: Optional[bool] = False,
    following: Optional[bool] = False,
    account_id: Optional[str] = None,
    exclude_unreviewed: Optional[bool] = False,
    limit: Optional[int] = 20,
) -> dict:
    """Search for content in accounts, statuses and hashtags.
    
    Args:
        q: The search query
        type: Specify whether to search for 'accounts', 'hashtags', 'statuses'
        resolve: Attempt WebFinger lookup?
        following: Only include accounts that the user is following
        account_id: If provided, will only return statuses from this account
        exclude_unreviewed: Filter out unreviewed tags?
        limit: Maximum number of results to return
    """
    params = {
        "q": q,
        "resolve": str(resolve).lower(),
        "following": str(following).lower(),
        "exclude_unreviewed": str(exclude_unreviewed).lower(),
        "limit": limit,
    }
    if type:
        params["type"] = type
    if account_id:
        params["account_id"] = account_id
    return make_request("GET", "/search", params=params)


# ===== LIST OPERATIONS =====

@mcp.tool()
def get_lists() -> dict:
    """View your lists."""
    return make_request("GET", "/lists")


@mcp.tool()
def get_list(list_id: str) -> dict:
    """Show a single list.
    
    Args:
        list_id: The ID of the list
    """
    return make_request("GET", f"/lists/{list_id}")


@mcp.tool()
def create_list(
    title: str,
    replies_policy: Optional[str] = "list",
    exclusive: Optional[bool] = False,
) -> dict:
    """Create a new list.
    
    Args:
        title: The title of the list
        replies_policy: One of 'followed', 'list', or 'none'
        exclusive: Whether members need to get removed from the Home feed
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": str(exclusive).lower(),
    }
    return make_request("POST", "/lists", data=data)


@mcp.tool()
def update_list(
    list_id: str,
    title: str,
    replies_policy: Optional[str] = "list",
    exclusive: Optional[bool] = False,
) -> dict:
    """Update a list.
    
    Args:
        list_id: The ID of the list
        title: The title of the list
        replies_policy: One of 'followed', 'list', or 'none'
        exclusive: Whether members need to get removed from the Home feed
    """
    data = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": str(exclusive).lower(),
    }
    return make_request("PUT", f"/lists/{list_id}", data=data)


@mcp.tool()
def delete_list(list_id: str) -> dict:
    """Delete a list.
    
    Args:
        list_id: The ID of the list
    """
    return make_request("DELETE", f"/lists/{list_id}")


@mcp.tool()
def get_list_accounts(
    list_id: str,
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View accounts in a list.
    
    Args:
        list_id: The ID of the list
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", f"/lists/{list_id}/accounts", params=params)


@mcp.tool()
def add_accounts_to_list(
    list_id: str,
    account_ids: str,
) -> dict:
    """Add accounts to a list.
    
    Args:
        list_id: The ID of the list
        account_ids: Comma-separated list of account IDs to add
    """
    data = {"account_ids[]": account_ids.split(",")}
    return make_request("POST", f"/lists/{list_id}/accounts", data=data)


@mcp.tool()
def remove_accounts_from_list(
    list_id: str,
    account_ids: str,
) -> dict:
    """Remove accounts from a list.
    
    Args:
        list_id: The ID of the list
        account_ids: Comma-separated list of account IDs to remove
    """
    data = {"account_ids[]": account_ids.split(",")}
    return make_request("DELETE", f"/lists/{list_id}/accounts", data=data)


# ===== BOOKMARK OPERATIONS =====

@mcp.tool()
def get_bookmarks(
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View your bookmarked statuses.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", "/bookmarks", params=params)


# ===== FAVOURITE OPERATIONS =====

@mcp.tool()
def get_favourites(
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View your favourited statuses.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", "/favourites", params=params)


# ===== MEDIA OPERATIONS =====

@mcp.tool()
def upload_media(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
) -> dict:
    """Upload media as an attachment.
    
    Args:
        file_path: Path to the file to upload
        description: A plain-text description of the media
        focus: Two floating points (x,y), comma-delimited, ranging from -1.0 to 1.0
    """
    url = f"{BASE_URL}/api/v2/media"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            
            response = requests.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Upload failed: {str(e)}"}


# ===== INSTANCE OPERATIONS =====

@mcp.tool()
def get_instance() -> dict:
    """View server information."""
    return make_request("GET", "/instance")


# ===== FOLLOW REQUEST OPERATIONS =====

@mcp.tool()
def get_follow_requests(
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
) -> dict:
    """View pending follow requests.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    return make_request("GET", "/follow_requests", params=params)


@mcp.tool()
def accept_follow_request(account_id: str) -> dict:
    """Accept a follow request.
    
    Args:
        account_id: The ID of the Account
    """
    return make_request("POST", f"/follow_requests/{account_id}/authorize")


@mcp.tool()
def reject_follow_request(account_id: str) -> dict:
    """Reject a follow request.
    
    Args:
        account_id: The ID of the Account
    """
    return make_request("POST", f"/follow_requests/{account_id}/reject")


# ===== CONVERSATION OPERATIONS =====

@mcp.tool()
def get_conversations(
    limit: Optional[int] = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View all conversations.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", "/conversations", params=params)


@mcp.tool()
def remove_conversation(conversation_id: str) -> dict:
    """Remove a conversation.
    
    Args:
        conversation_id: The ID of the Conversation
    """
    return make_request("DELETE", f"/conversations/{conversation_id}")


@mcp.tool()
def mark_conversation_read(conversation_id: str) -> dict:
    """Mark a conversation as read.
    
    Args:
        conversation_id: The ID of the Conversation
    """
    return make_request("POST", f"/conversations/{conversation_id}/read")


# ===== SUGGESTION OPERATIONS =====

@mcp.tool()
def get_suggestions(
    limit: Optional[int] = 40,
) -> dict:
    """View follow suggestions.
    
    Args:
        limit: Maximum number of results to return
    """
    params = {"limit": limit}
    return make_request("GET", "/suggestions", params=params)


@mcp.tool()
def remove_suggestion(account_id: str) -> dict:
    """Remove an account from follow suggestions.
    
    Args:
        account_id: The ID of the Account
    """
    return make_request("DELETE", f"/suggestions/{account_id}")


# ===== BLOCK OPERATIONS =====

@mcp.tool()
def get_blocked_accounts(
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View blocked accounts.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", "/blocks", params=params)


# ===== DOMAIN BLOCK OPERATIONS =====

@mcp.tool()
def get_domain_blocks(
    limit: Optional[int] = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> dict:
    """View domain blocks.
    
    Args:
        limit: Maximum number of results to return
        max_id: Upper bound on results
        since_id: Lower bound on results
        min_id: Cursor at this ID for forward pagination
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    return make_request("GET", "/domain_blocks", params=params)


@mcp.tool()
def block_domain(domain: str) -> dict:
    """Block a domain.
    
    Args:
        domain: The domain to block
    """
    data = {"domain": domain}
    return make_request("POST", "/domain_blocks", data=data)


@mcp.tool()
def unblock_domain(domain: str) -> dict:
    """Unblock a domain.
    
    Args:
        domain: The domain to unblock
    """
    data = {"domain": domain}
    return make_request("DELETE", "/domain_blocks", data=data)


if __name__ == "__main__":
    # Run the server over stdio
    mcp.run()
