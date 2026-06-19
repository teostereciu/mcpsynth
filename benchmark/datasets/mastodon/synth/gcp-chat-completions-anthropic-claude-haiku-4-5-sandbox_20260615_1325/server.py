#!/usr/bin/env python3
"""
Mastodon API MCP Server

An MCP server providing comprehensive access to the Mastodon REST API.
Requires MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL environment variables.
"""

import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("mastodon")

# Configuration from environment
MASTODON_BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN", "")
API_BASE = f"{MASTODON_BASE_URL}/api/v1"

# Helper function to make authenticated requests
def make_request(method: str, endpoint: str, params=None, data=None, files=None):
    """Make an authenticated request to the Mastodon API."""
    url = f"{API_BASE}{endpoint}"
    headers = {}
    if MASTODON_ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {MASTODON_ACCESS_TOKEN}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method.upper() == "POST":
            if files:
                response = requests.post(url, headers=headers, data=data, files=files, timeout=30)
            else:
                response = requests.post(url, headers=headers, json=data, timeout=30)
        elif method.upper() == "PATCH":
            response = requests.patch(url, headers=headers, json=data, timeout=30)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data, timeout=30)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
        
        return response.json() if response.text else {}
    except Exception as e:
        return {"error": str(e)}


# STATUSES
@mcp.tool()
def post_status(status: str, in_reply_to_id: Optional[str] = None, media_ids: Optional[list] = None, 
                sensitive: bool = False, spoiler_text: Optional[str] = None, visibility: str = "public",
                language: Optional[str] = None, scheduled_at: Optional[str] = None):
    """Post a new status to Mastodon."""
    data = {"status": status, "sensitive": sensitive, "visibility": visibility}
    if in_reply_to_id: data["in_reply_to_id"] = in_reply_to_id
    if media_ids: data["media_ids"] = media_ids
    if spoiler_text: data["spoiler_text"] = spoiler_text
    if language: data["language"] = language
    if scheduled_at: data["scheduled_at"] = scheduled_at
    return make_request("POST", "/statuses", data=data)

@mcp.tool()
def get_status(status_id: str):
    """Get a single status by ID."""
    return make_request("GET", f"/statuses/{status_id}")

@mcp.tool()
def get_statuses(status_ids: list):
    """Get multiple statuses by their IDs."""
    return make_request("GET", "/statuses", params={"id[]": status_ids})

@mcp.tool()
def delete_status(status_id: str, delete_media: bool = False):
    """Delete a status."""
    params = {"delete_media": "true"} if delete_media else {}
    return make_request("DELETE", f"/statuses/{status_id}", params=params)

@mcp.tool()
def get_status_context(status_id: str):
    """Get parent and child statuses in context (thread)."""
    return make_request("GET", f"/statuses/{status_id}/context")

@mcp.tool()
def favourite_status(status_id: str):
    """Favourite a status."""
    return make_request("POST", f"/statuses/{status_id}/favourite")

@mcp.tool()
def unfavourite_status(status_id: str):
    """Undo favourite of a status."""
    return make_request("POST", f"/statuses/{status_id}/unfavourite")

@mcp.tool()
def boost_status(status_id: str):
    """Boost (reblog) a status."""
    return make_request("POST", f"/statuses/{status_id}/reblog")

@mcp.tool()
def unboost_status(status_id: str):
    """Undo boost of a status."""
    return make_request("POST", f"/statuses/{status_id}/unreblog")

@mcp.tool()
def bookmark_status(status_id: str):
    """Bookmark a status."""
    return make_request("POST", f"/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str):
    """Undo bookmark of a status."""
    return make_request("POST", f"/statuses/{status_id}/unbookmark")

@mcp.tool()
def translate_status(status_id: str, language: Optional[str] = None):
    """Translate a status content into another language."""
    data = {}
    if language: data["language"] = language
    return make_request("POST", f"/statuses/{status_id}/translate", data=data)

@mcp.tool()
def get_status_boosters(status_id: str, limit: int = 40, max_id: Optional[str] = None):
    """Get accounts that have boosted a status."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/statuses/{status_id}/reblogged_by", params=params)

@mcp.tool()
def get_status_favouriters(status_id: str, limit: int = 40, max_id: Optional[str] = None):
    """Get accounts that have favourited a status."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/statuses/{status_id}/favourited_by", params=params)

@mcp.tool()
def pin_status(status_id: str):
    """Pin a status to your profile."""
    return make_request("POST", f"/statuses/{status_id}/pin")

@mcp.tool()
def unpin_status(status_id: str):
    """Unpin a status from your profile."""
    return make_request("POST", f"/statuses/{status_id}/unpin")

@mcp.tool()
def mute_conversation(status_id: str):
    """Mute a conversation."""
    return make_request("POST", f"/statuses/{status_id}/mute")

@mcp.tool()
def unmute_conversation(status_id: str):
    """Unmute a conversation."""
    return make_request("POST", f"/statuses/{status_id}/unmute")

@mcp.tool()
def edit_status(status_id: str, status: str, spoiler_text: Optional[str] = None, 
                sensitive: Optional[bool] = None, media_ids: Optional[list] = None):
    """Edit a status."""
    data = {"status": status}
    if spoiler_text is not None: data["spoiler_text"] = spoiler_text
    if sensitive is not None: data["sensitive"] = sensitive
    if media_ids: data["media_ids"] = media_ids
    return make_request("PUT", f"/statuses/{status_id}", data=data)

@mcp.tool()
def get_status_edit_history(status_id: str):
    """Get the edit history of a status."""
    return make_request("GET", f"/statuses/{status_id}/history")

# ACCOUNTS
@mcp.tool()
def verify_credentials():
    """Verify the user token and get authenticated account info."""
    return make_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def get_account(account_id: str):
    """Get account information by ID."""
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def get_account_statuses(account_id: str, limit: int = 20, max_id: Optional[str] = None,
                        exclude_replies: bool = False, exclude_reblogs: bool = False):
    """Get statuses posted by an account."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if exclude_replies: params["exclude_replies"] = "true"
    if exclude_reblogs: params["exclude_reblogs"] = "true"
    return make_request("GET", f"/accounts/{account_id}/statuses", params=params)

@mcp.tool()
def get_account_followers(account_id: str, limit: int = 40, max_id: Optional[str] = None):
    """Get followers of an account."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/accounts/{account_id}/followers", params=params)

@mcp.tool()
def get_account_following(account_id: str, limit: int = 40, max_id: Optional[str] = None):
    """Get accounts that an account is following."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/accounts/{account_id}/following", params=params)

@mcp.tool()
def follow_account(account_id: str):
    """Follow an account."""
    return make_request("POST", f"/accounts/{account_id}/follow")

@mcp.tool()
def unfollow_account(account_id: str):
    """Unfollow an account."""
    return make_request("POST", f"/accounts/{account_id}/unfollow")

@mcp.tool()
def block_account(account_id: str):
    """Block an account."""
    return make_request("POST", f"/accounts/{account_id}/block")

@mcp.tool()
def unblock_account(account_id: str):
    """Unblock an account."""
    return make_request("POST", f"/accounts/{account_id}/unblock")

@mcp.tool()
def mute_account(account_id: str, notifications: bool = True):
    """Mute an account."""
    return make_request("POST", f"/accounts/{account_id}/mute", data={"notifications": notifications})

@mcp.tool()
def unmute_account(account_id: str):
    """Unmute an account."""
    return make_request("POST", f"/accounts/{account_id}/unmute")

@mcp.tool()
def get_account_relationships(account_ids: list):
    """Check relationships to other accounts."""
    return make_request("GET", "/accounts/relationships", params={"id[]": account_ids})

@mcp.tool()
def search_accounts(q: str, limit: int = 40, resolve: bool = False):
    """Search for accounts."""
    params = {"q": q, "limit": limit}
    if resolve: params["resolve"] = "true"
    return make_request("GET", "/accounts/search", params=params)

@mcp.tool()
def update_credentials(display_name: Optional[str] = None, note: Optional[str] = None,
                      locked: Optional[bool] = None, bot: Optional[bool] = None,
                      discoverable: Optional[bool] = None):
    """Update account credentials."""
    data = {}
    if display_name is not None: data["display_name"] = display_name
    if note is not None: data["note"] = note
    if locked is not None: data["locked"] = locked
    if bot is not None: data["bot"] = bot
    if discoverable is not None: data["discoverable"] = discoverable
    return make_request("PATCH", "/accounts/update_credentials", data=data)

# TIMELINES
@mcp.tool()
def get_home_timeline(limit: int = 20, max_id: Optional[str] = None):
    """Get the authenticated user's home timeline."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(local: bool = False, limit: int = 20, max_id: Optional[str] = None):
    """Get the public timeline."""
    params = {"limit": limit}
    if local: params["local"] = "true"
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: bool = False, limit: int = 20, max_id: Optional[str] = None):
    """Get statuses for a hashtag."""
    params = {"limit": limit}
    if local: params["local"] = "true"
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20, max_id: Optional[str] = None):
    """Get statuses in a list."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/timelines/list/{list_id}", params=params)

# NOTIFICATIONS
@mcp.tool()
def get_notifications(limit: int = 20, max_id: Optional[str] = None):
    """Get all notifications."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/notifications", params=params)

@mcp.tool()
def get_notification(notification_id: str):
    """Get a single notification."""
    return make_request("GET", f"/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str):
    """Dismiss a single notification."""
    return make_request("POST", f"/notifications/{notification_id}/dismiss")

@mcp.tool()
def dismiss_all_notifications():
    """Dismiss all notifications."""
    return make_request("POST", "/notifications/clear")

@mcp.tool()
def get_unread_notification_count():
    """Get the number of unread notifications."""
    return make_request("GET", "/notifications/unread_count")

# SEARCH
@mcp.tool()
def search(q: str, type: Optional[str] = None, limit: int = 20, offset: int = 0, resolve: bool = False):
    """Perform a search for statuses, accounts, or hashtags."""
    params = {"q": q, "limit": limit, "offset": offset}
    if type: params["type"] = type
    if resolve: params["resolve"] = "true"
    return make_request("GET", "/search", params=params)

# LISTS
@mcp.tool()
def get_lists():
    """Get all lists owned by the authenticated user."""
    return make_request("GET", "/lists")

@mcp.tool()
def get_list(list_id: str):
    """Get a single list."""
    return make_request("GET", f"/lists/{list_id}")

@mcp.tool()
def create_list(title: str, replies_policy: Optional[str] = None):
    """Create a new list."""
    data = {"title": title}
    if replies_policy: data["replies_policy"] = replies_policy
    return make_request("POST", "/lists", data=data)

@mcp.tool()
def update_list(list_id: str, title: str):
    """Update a list."""
    return make_request("PUT", f"/lists/{list_id}", data={"title": title})

@mcp.tool()
def delete_list(list_id: str):
    """Delete a list."""
    return make_request("DELETE", f"/lists/{list_id}")

@mcp.tool()
def get_list_accounts(list_id: str, limit: int = 40, max_id: Optional[str] = None):
    """Get accounts in a list."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", f"/lists/{list_id}/accounts", params=params)

@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: list):
    """Add accounts to a list."""
    return make_request("POST", f"/lists/{list_id}/accounts", data={"account_ids": account_ids})

@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: list):
    """Remove accounts from a list."""
    return make_request("DELETE", f"/lists/{list_id}/accounts", data={"account_ids": account_ids})

# BOOKMARKS
@mcp.tool()
def get_bookmarks(limit: int = 20, max_id: Optional[str] = None):
    """Get bookmarked statuses."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/bookmarks", params=params)

# FAVOURITES
@mcp.tool()
def get_favourites(limit: int = 20, max_id: Optional[str] = None):
    """Get favourited statuses."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/favourites", params=params)

# MEDIA
@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None):
    """Upload a media attachment."""
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description: data["description"] = description
            if focus: data["focus"] = focus
            return make_request("POST", "/media", data=data, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_media(media_id: str):
    """Get a media attachment."""
    return make_request("GET", f"/media/{media_id}")

@mcp.tool()
def update_media(media_id: str, description: Optional[str] = None, focus: Optional[str] = None):
    """Update a media attachment."""
    data = {}
    if description is not None: data["description"] = description
    if focus is not None: data["focus"] = focus
    return make_request("PATCH", f"/media/{media_id}", data=data)

@mcp.tool()
def delete_media(media_id: str):
    """Delete a media attachment."""
    return make_request("DELETE", f"/media/{media_id}")

# INSTANCE
@mcp.tool()
def get_instance_info():
    """Get instance information."""
    return make_request("GET", "/instance")

@mcp.tool()
def get_instance_peers():
    """Get list of connected domains."""
    return make_request("GET", "/instance/peers")

@mcp.tool()
def get_instance_activity():
    """Get weekly activity statistics."""
    return make_request("GET", "/instance/activity")

@mcp.tool()
def get_instance_rules():
    """Get instance rules."""
    return make_request("GET", "/instance/rules")

# POLLS
@mcp.tool()
def get_poll(poll_id: str):
    """Get a poll."""
    return make_request("GET", f"/polls/{poll_id}")

@mcp.tool()
def vote_on_poll(poll_id: str, choices: list):
    """Vote on a poll."""
    return make_request("POST", f"/polls/{poll_id}/votes", data={"choices": choices})

# TAGS
@mcp.tool()
def get_tag(tag_name: str):
    """Get information about a tag."""
    return make_request("GET", f"/tags/{tag_name}")

@mcp.tool()
def follow_tag(tag_name: str):
    """Follow a hashtag."""
    return make_request("POST", f"/tags/{tag_name}/follow")

@mcp.tool()
def unfollow_tag(tag_name: str):
    """Unfollow a hashtag."""
    return make_request("POST", f"/tags/{tag_name}/unfollow")

# FILTERS
@mcp.tool()
def get_filters():
    """Get all filters."""
    return make_request("GET", "/filters")

@mcp.tool()
def get_filter(filter_id: str):
    """Get a single filter."""
    return make_request("GET", f"/filters/{filter_id}")

@mcp.tool()
def create_filter(title: str, context: list, filter_action: str = "warn", expires_in: Optional[int] = None):
    """Create a filter."""
    data = {"title": title, "context": context, "filter_action": filter_action}
    if expires_in: data["expires_in"] = expires_in
    return make_request("POST", "/filters", data=data)

@mcp.tool()
def update_filter(filter_id: str, title: Optional[str] = None, context: Optional[list] = None,
                 filter_action: Optional[str] = None):
    """Update a filter."""
    data = {}
    if title is not None: data["title"] = title
    if context is not None: data["context"] = context
    if filter_action is not None: data["filter_action"] = filter_action
    return make_request("PUT", f"/filters/{filter_id}", data=data)

@mcp.tool()
def delete_filter(filter_id: str):
    """Delete a filter."""
    return make_request("DELETE", f"/filters/{filter_id}")

# MUTES AND BLOCKS
@mcp.tool()
def get_muted_accounts(limit: int = 40, max_id: Optional[str] = None):
    """Get muted accounts."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/mutes", params=params)

@mcp.tool()
def get_blocked_accounts(limit: int = 40, max_id: Optional[str] = None):
    """Get blocked accounts."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/blocks", params=params)

# FOLLOW REQUESTS
@mcp.tool()
def get_follow_requests(limit: int = 40, max_id: Optional[str] = None):
    """Get pending follow requests."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/follow_requests", params=params)

@mcp.tool()
def accept_follow_request(account_id: str):
    """Accept a follow request."""
    return make_request("POST", f"/follow_requests/{account_id}/authorize")

@mcp.tool()
def reject_follow_request(account_id: str):
    """Reject a follow request."""
    return make_request("POST", f"/follow_requests/{account_id}/reject")

# PREFERENCES
@mcp.tool()
def get_preferences():
    """Get user preferences."""
    return make_request("GET", "/preferences")

# ANNOUNCEMENTS
@mcp.tool()
def get_announcements(with_dismissed: bool = False):
    """Get all announcements."""
    params = {}
    if with_dismissed: params["with_dismissed"] = "true"
    return make_request("GET", "/announcements", params=params)

@mcp.tool()
def dismiss_announcement(announcement_id: str):
    """Dismiss an announcement."""
    return make_request("POST", f"/announcements/{announcement_id}/dismiss")

# DOMAIN BLOCKS
@mcp.tool()
def get_domain_blocks(limit: int = 40, max_id: Optional[str] = None):
    """Get domain blocks."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/domain_blocks", params=params)

@mcp.tool()
def block_domain(domain: str):
    """Block a domain."""
    return make_request("POST", "/domain_blocks", data={"domain": domain})

@mcp.tool()
def unblock_domain(domain: str):
    """Unblock a domain."""
    return make_request("DELETE", "/domain_blocks", params={"domain": domain})

# CONVERSATIONS
@mcp.tool()
def get_conversations(limit: int = 20, max_id: Optional[str] = None):
    """Get all conversations."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/conversations", params=params)

@mcp.tool()
def delete_conversation(conversation_id: str):
    """Delete a conversation."""
    return make_request("DELETE", f"/conversations/{conversation_id}")

@mcp.tool()
def mark_conversation_as_read(conversation_id: str):
    """Mark a conversation as read."""
    return make_request("POST", f"/conversations/{conversation_id}/read")

# CUSTOM EMOJIS
@mcp.tool()
def get_custom_emojis():
    """Get all custom emojis."""
    return make_request("GET", "/custom_emojis")

# FEATURED TAGS
@mcp.tool()
def get_featured_tags():
    """Get featured tags."""
    return make_request("GET", "/featured_tags")

@mcp.tool()
def feature_tag(name: str):
    """Feature a tag."""
    return make_request("POST", "/featured_tags", data={"name": name})

@mcp.tool()
def unfeature_tag(tag_id: str):
    """Unfeature a tag."""
    return make_request("DELETE", f"/featured_tags/{tag_id}")

# FOLLOWED TAGS
@mcp.tool()
def get_followed_tags(limit: int = 20, max_id: Optional[str] = None):
    """Get followed tags."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/followed_tags", params=params)

# SCHEDULED STATUSES
@mcp.tool()
def get_scheduled_statuses(limit: int = 20, max_id: Optional[str] = None):
    """Get scheduled statuses."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/scheduled_statuses", params=params)

@mcp.tool()
def get_scheduled_status(scheduled_status_id: str):
    """Get a scheduled status."""
    return make_request("GET", f"/scheduled_statuses/{scheduled_status_id}")

@mcp.tool()
def update_scheduled_status(scheduled_status_id: str, scheduled_at: str):
    """Update a scheduled status's publishing date."""
    return make_request("PUT", f"/scheduled_statuses/{scheduled_status_id}", data={"scheduled_at": scheduled_at})

@mcp.tool()
def cancel_scheduled_status(scheduled_status_id: str):
    """Cancel a scheduled status."""
    return make_request("DELETE", f"/scheduled_statuses/{scheduled_status_id}")

# MARKERS
@mcp.tool()
def get_markers(timelines: Optional[list] = None):
    """Get saved timeline positions."""
    params = {}
    if timelines: params["timeline[]"] = timelines
    return make_request("GET", "/markers", params=params)

@mcp.tool()
def save_markers(home: Optional[dict] = None, notifications: Optional[dict] = None):
    """Save timeline positions."""
    data = {}
    if home: data["home"] = home
    if notifications: data["notifications"] = notifications
    return make_request("POST", "/markers", data=data)

# TRENDS
@mcp.tool()
def get_trending_statuses(limit: int = 20, offset: int = 0):
    """Get trending statuses."""
    return make_request("GET", "/trends/statuses", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_trending_tags(limit: int = 20, offset: int = 0):
    """Get trending tags."""
    return make_request("GET", "/trends/tags", params={"limit": limit, "offset": offset})

@mcp.tool()
def get_trending_links(limit: int = 20, offset: int = 0):
    """Get trending links."""
    return make_request("GET", "/trends/links", params={"limit": limit, "offset": offset})

# SUGGESTIONS
@mcp.tool()
def get_suggestions(limit: int = 40):
    """Get follow suggestions."""
    return make_request("GET", "/suggestions", params={"limit": limit})

@mcp.tool()
def remove_suggestion(account_id: str):
    """Remove a suggestion."""
    return make_request("DELETE", f"/suggestions/{account_id}")

# ENDORSEMENTS
@mcp.tool()
def get_endorsements(limit: int = 40, max_id: Optional[str] = None):
    """Get featured accounts."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    return make_request("GET", "/endorsements", params=params)

@mcp.tool()
def endorse_account(account_id: str):
    """Feature an account on your profile."""
    return make_request("POST", f"/accounts/{account_id}/pin")

@mcp.tool()
def unendorse_account(account_id: str):
    """Unfeature an account from your profile."""
    return make_request("POST", f"/accounts/{account_id}/unpin")

# REPORTS
@mcp.tool()
def file_report(account_id: str, comment: Optional[str] = None, status_ids: Optional[list] = None,
               rule_ids: Optional[list] = None):
    """File a report."""
    data = {"account_id": account_id}
    if comment: data["comment"] = comment
    if status_ids: data["status_ids"] = status_ids
    if rule_ids: data["rule_ids"] = rule_ids
    return make_request("POST", "/reports", data=data)

# PROFILE
@mcp.tool()
def get_profile():
    """Get current user profile (alias for verify_credentials)."""
    return make_request("GET", "/accounts/verify_credentials")

# DIRECTORY
@mcp.tool()
def get_directory(limit: int = 20, offset: int = 0, order: str = "active", local: bool = False):
    """Get profile directory."""
    params = {"limit": limit, "offset": offset, "order": order}
    if local: params["local"] = "true"
    return make_request("GET", "/directory", params=params)

# APPS
@mcp.tool()
def verify_app_credentials():
    """Verify app credentials."""
    return make_request("GET", "/apps/verify_credentials")

if __name__ == "__main__":
    mcp.run()
