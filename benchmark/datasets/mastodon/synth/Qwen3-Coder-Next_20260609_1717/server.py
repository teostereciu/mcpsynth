#!/usr/bin/env python3
"""
Mastodon MCP Server

An MCP server with comprehensive coverage of the Mastodon REST API.
"""

import os
import requests
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("mastodon")

# Base URL configuration
BASE_URL = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social")
API_BASE = f"{BASE_URL}/api/v1"

# Authentication headers
def get_auth_headers() -> Dict[str, str]:
    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    if not token:
        raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")
    return {"Authorization": f"Bearer {token}"}

# =============================================================================
# Media API
# =============================================================================

@mcp.tool()
def upload_media(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail_path: Optional[str] = None,
) -> Dict[str, Any]:
    """Upload a media file to Mastodon."""
    try:
        headers = get_auth_headers()
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            if thumbnail_path:
                with open(thumbnail_path, "rb") as tf:
                    files["thumbnail"] = (os.path.basename(thumbnail_path), tf)
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            response = requests.post(f"{API_BASE}/v2/media", headers=headers, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_media(media_id: str) -> Dict[str, Any]:
    """Get a media attachment."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/media/{media_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def update_media(media_id: str, description: Optional[str] = None, focus: Optional[str] = None) -> Dict[str, Any]:
    """Update a media attachment's parameters."""
    try:
        headers = get_auth_headers()
        data = {}
        if description:
            data["description"] = description
        if focus:
            data["focus"] = focus
        response = requests.put(f"{API_BASE}/media/{media_id}", headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def delete_media(media_id: str) -> Dict[str, Any]:
    """Delete a media attachment."""
    try:
        headers = get_auth_headers()
        response = requests.delete(f"{API_BASE}/media/{media_id}", headers=headers)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Statuses API
# =============================================================================

@mcp.tool()
def post_status(
    status: str,
    media_ids: Optional[List[str]] = None,
    visibility: str = "public",
    sensitive: bool = False,
    spoiler_text: Optional[str] = None,
    language: Optional[str] = None,
    in_reply_to_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Post a new status."""
    try:
        headers = get_auth_headers()
        data = {"status": status, "visibility": visibility, "sensitive": str(sensitive).lower()}
        if media_ids:
            for i, mid in enumerate(media_ids):
                data[f"media_ids[{i}]"] = mid
        if spoiler_text:
            data["spoiler_text"] = spoiler_text
        if language:
            data["language"] = language
        if in_reply_to_id:
            data["in_reply_to_id"] = in_reply_to_id
        response = requests.post(f"{API_BASE}/statuses", headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """Get a status by ID."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/statuses/{status_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def delete_status(status_id: str) -> Dict[str, Any]:
    """Delete a status."""
    try:
        headers = get_auth_headers()
        response = requests.delete(f"{API_BASE}/statuses/{status_id}", headers=headers)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def boost_status(status_id: str) -> Dict[str, Any]:
    """Boost a status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/reblog", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unboost_status(status_id: str) -> Dict[str, Any]:
    """Undo a boost of a status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/unreblog", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    """Favourite a status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/favourite", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """Undo a favourite of a status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/unfavourite", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    """Get the context of a status (ancestors and descendants)."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/statuses/{status_id}/context", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    """Bookmark a status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/bookmark", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """Undo a bookmark of a status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/unbookmark", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pin_status(status_id: str) -> Dict[str, Any]:
    """Pin a status on your profile."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/pin", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unpin_status(status_id: str) -> Dict[str, Any]:
    """Undo a pin of a status on your profile."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/unpin", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def mute_status(status_id: str) -> Dict[str, Any]:
    """Mute conversations including this status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/mute", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unmute_status(status_id: str) -> Dict[str, Any]:
    """Undo a mute of conversations including this status."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/unmute", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_status_history(status_id: str) -> List[Dict[str, Any]]:
    """Get edit history of a status."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/statuses/{status_id}/history", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_status_source(status_id: str) -> Dict[str, Any]:
    """Get source of a status."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/statuses/{status_id}/source", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_status_card(status_id: str) -> Dict[str, Any]:
    """Get card associated with a status."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/statuses/{status_id}/card", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_status_quotes(status_id: str) -> List[Dict[str, Any]]:
    """Get statuses that quote this status."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/statuses/{status_id}/quotes", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def translate_status(status_id: str, language: str) -> Dict[str, Any]:
    """Translate a status into a specific language."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/statuses/{status_id}/translate", headers=headers, data={"language": language})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_statuses(status_ids: List[str]) -> List[Dict[str, Any]]:
    """Get multiple statuses by ID."""
    try:
        headers = get_auth_headers()
        params = []
        for i, sid in enumerate(status_ids):
            params.append(("id[]", sid))
        response = requests.get(f"{API_BASE}/statuses", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Timelines API
# =============================================================================

@mcp.tool()
def get_home_timeline(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get home timeline (personalized feed)."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/timelines/home", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_public_timeline(
    local: bool = False,
    remote: bool = False,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get public timeline."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit, "local": str(local).lower(), "remote": str(remote).lower()}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/timelines/public", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get timeline for a specific hashtag."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit, "local": str(local).lower()}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/timelines/tag/{hashtag}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_list_timeline(
    list_id: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get timeline for a specific list."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/timelines/list/{list_id}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_direct_timeline(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get direct messages timeline."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/timelines/direct", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Accounts API
# =============================================================================

@mcp.tool()
def get_authenticated_account() -> Dict[str, Any]:
    """Get the authenticated account."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/accounts/verify_credentials", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """Get an account by ID."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/accounts/{account_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_account_statuses(
    account_id: str,
    only_media: bool = False,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get statuses for an account."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit, "only_media": str(only_media).lower()}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/accounts/{account_id}/statuses", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def follow_account(account_id: str) -> Dict[str, Any]:
    """Follow an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/follow", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    """Unfollow an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/unfollow", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_account_relationships(account_ids: List[str]) -> List[Dict[str, Any]]:
    """Get relationships to accounts."""
    try:
        headers = get_auth_headers()
        params = []
        for i, aid in enumerate(account_ids):
            params.append(("id[]", aid))
        response = requests.get(f"{API_BASE}/accounts/relationships", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_account_followers(
    account_id: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get followers of an account."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        response = requests.get(f"{API_BASE}/accounts/{account_id}/followers", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_account_following(
    account_id: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get accounts followed by an account."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        response = requests.get(f"{API_BASE}/accounts/{account_id}/following", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def block_account(account_id: str) -> Dict[str, Any]:
    """Block an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/block", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unblock_account(account_id: str) -> Dict[str, Any]:
    """Unblock an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/unblock", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def mute_account(account_id: str, notifications: bool = True) -> Dict[str, Any]:
    """Mute an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/mute", headers=headers, data={"notifications": str(notifications).lower()})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unmute_account(account_id: str) -> Dict[str, Any]:
    """Unmute an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/unmute", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pin_account(account_id: str) -> Dict[str, Any]:
    """Pin an account (add to featured accounts)."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/pin", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def unpin_account(account_id: str) -> Dict[str, Any]:
    """Unpin an account (remove from featured accounts)."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/unpin", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def update_account_note(account_id: str, note: str) -> Dict[str, Any]:
    """Update the note (private message) for an account."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/accounts/{account_id}/note", headers=headers, data={"comment": note})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_accounts(
    q: str,
    resolve: bool = False,
    limit: int = 10,
    following: bool = False,
) -> List[Dict[str, Any]]:
    """Search for accounts by username or display name."""
    try:
        headers = get_auth_headers()
        params = {"q": q, "resolve": str(resolve).lower(), "limit": limit, "following": str(following).lower()}
        response = requests.get(f"{API_BASE}/accounts/search", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def lookup_account(acct: str) -> Dict[str, Any]:
    """Get an account by username (acct)."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/accounts/lookup", headers=headers, params={"acct": acct})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Notifications API
# =============================================================================

@mcp.tool()
def list_notifications(
    types: Optional[List[str]] = None,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """List notifications."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if types:
            for i, t in enumerate(types):
                params[f"types[{i}]"] = t
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/notifications", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    """Get a notification by ID."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/notifications/{notification_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """Dismiss a single notification."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/notifications/{notification_id}/dismiss", headers=headers)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def dismiss_all_notifications() -> Dict[str, Any]:
    """Dismiss all notifications for the authenticated user."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/notifications/clear", headers=headers)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def dismiss_notifications_by_type(types: List[str]) -> Dict[str, Any]:
    """Dismiss all notifications of specified types."""
    try:
        headers = get_auth_headers()
        data = {}
        for i, t in enumerate(types):
            data[f"types[{i}]"] = t
        response = requests.post(f"{API_BASE}/notifications/dismiss", headers=headers, data=data)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_unread_notification_count(types: Optional[List[str]] = None) -> Dict[str, int]:
    """Get count of unread notifications."""
    try:
        headers = get_auth_headers()
        params = {}
        if types:
            for i, t in enumerate(types):
                params[f"types[{i}]"] = t
        response = requests.get(f"{API_BASE}/notifications/unread_count", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Search API
# =============================================================================

@mcp.tool()
def search(
    q: str,
    type: Optional[str] = None,
    resolve: bool = False,
    offset: int = 0,
    limit: int = 20,
) -> Dict[str, Any]:
    """Search for content."""
    try:
        headers = get_auth_headers()
        params = {"q": q, "resolve": str(resolve).lower(), "offset": offset, "limit": limit}
        if type:
            params["type"] = type
        response = requests.get(f"{API_BASE}/search", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Lists API
# =============================================================================

@mcp.tool()
def create_list(title: str) -> Dict[str, Any]:
    """Create a new list."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/lists", headers=headers, data={"title": title})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_lists() -> List[Dict[str, Any]]:
    """Get all lists for the authenticated user."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/lists", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    """Get a list by ID."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/lists/{list_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def update_list(list_id: str, title: str) -> Dict[str, Any]:
    """Update a list's title."""
    try:
        headers = get_auth_headers()
        response = requests.put(f"{API_BASE}/lists/{list_id}", headers=headers, data={"title": title})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    """Delete a list."""
    try:
        headers = get_auth_headers()
        response = requests.delete(f"{API_BASE}/lists/{list_id}", headers=headers)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """Add accounts to a list."""
    try:
        headers = get_auth_headers()
        data = {}
        for i, aid in enumerate(account_ids):
            data[f"account_ids[{i}]"] = aid
        response = requests.post(f"{API_BASE}/lists/{list_id}/accounts", headers=headers, data=data)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """Remove accounts from a list."""
    try:
        headers = get_auth_headers()
        data = {}
        for i, aid in enumerate(account_ids):
            data[f"account_ids[{i}]"] = aid
        response = requests.delete(f"{API_BASE}/lists/{list_id}/accounts", headers=headers, data=data)
        response.raise_for_status()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_list_accounts(list_id: str) -> List[Dict[str, Any]]:
    """Get accounts in a list."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/lists/{list_id}/accounts", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Bookmarks API
# =============================================================================

@mcp.tool()
def get_bookmarks(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get bookmarked statuses."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        response = requests.get(f"{API_BASE}/bookmarks", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Favourites API
# =============================================================================

@mcp.tool()
def get_favourites(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get favourited statuses."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        response = requests.get(f"{API_BASE}/favourites", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Instance API
# =============================================================================

@mcp.tool()
def get_instance() -> Dict[str, Any]:
    """Get instance information."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/instance", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_activity() -> Dict[str, Any]:
    """Get instance activity statistics."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/instance/activity", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_peers() -> List[str]:
    """Get list of federated instances."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/instance/peers", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_instance_rules() -> List[Dict[str, Any]]:
    """Get instance rules."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/instance/rules", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_domain_blocks() -> List[Dict[str, Any]]:
    """Get domain blocks for the authenticated user."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/instance/domain_blocks", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_extended_description() -> str:
    """Get extended description of the instance."""
    try:
        headers = get_auth_headers()
        response = requests.get(f"{API_BASE}/instance/extended_description", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Follow Requests API
# =============================================================================

@mcp.tool()
def list_follow_requests(
    limit: int = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """List pending follow requests."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/follow_requests", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def authorize_follow_request(account_id: str) -> Dict[str, Any]:
    """Accept a follow request."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/follow_requests/{account_id}/authorize", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def reject_follow_request(account_id: str) -> Dict[str, Any]:
    """Reject a follow request."""
    try:
        headers = get_auth_headers()
        response = requests.post(f"{API_BASE}/follow_requests/{account_id}/reject", headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Blocks API
# =============================================================================

@mcp.tool()
def get_blocked_accounts(
    limit: int = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get accounts blocked by the authenticated user."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        if min_id:
            params["min_id"] = min_id
        response = requests.get(f"{API_BASE}/blocks", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Mutes API
# =============================================================================

@mcp.tool()
def get_muted_accounts(
    limit: int = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Get accounts muted by the authenticated user."""
    try:
        headers = get_auth_headers()
        params = {"limit": limit}
        if max_id:
            params["max_id"] = max_id
        if since_id:
            params["since_id"] = since_id
        response = requests.get(f"{API_BASE}/mutes", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Run the server
# =============================================================================

if __name__ == "__main__":
    mcp.run()
