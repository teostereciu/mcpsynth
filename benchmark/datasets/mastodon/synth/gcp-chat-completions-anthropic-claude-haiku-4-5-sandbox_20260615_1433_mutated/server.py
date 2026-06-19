#!/usr/bin/env python3
"""MCP Server for Mastodon API"""
import os, json, requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mastodon")
MASTODON_BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN", "")
API_BASE_URL = f"{MASTODON_BASE_URL}/api/v1"

def get_headers() -> dict:
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if MASTODON_ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {MASTODON_ACCESS_TOKEN}"
    return headers

def make_request(method: str, endpoint: str, **kwargs) -> dict:
    try:
        url = f"{API_BASE_URL}{endpoint}"
        response = requests.request(method, url, headers=get_headers(), **kwargs)
        response.raise_for_status()
        return response.json() if response.text else {}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_account_credentials() -> dict:
    """Get authenticated user's account credentials."""
    return make_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def update_account_credentials(display_name: Optional[str] = None, note: Optional[str] = None, locked: Optional[bool] = None, bot: Optional[bool] = None, discoverable: Optional[bool] = None) -> dict:
    """Update account credentials."""
    data = {}
    if display_name is not None: data["display_name"] = display_name
    if note is not None: data["note"] = note
    if locked is not None: data["locked"] = locked
    if bot is not None: data["bot"] = bot
    if discoverable is not None: data["discoverable"] = discoverable
    return make_request("PATCH", "/accounts/update_credentials", json=data)

@mcp.tool()
def get_account(account_id: str) -> dict:
    """Get account by ID."""
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def get_account_statuses(account_id: str, limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get account's statuses."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", f"/accounts/{account_id}/statuses", params=params)

@mcp.tool()
def get_account_followers(account_id: str, limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get account's followers."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", f"/accounts/{account_id}/followers", params=params)

@mcp.tool()
def get_account_following(account_id: str, limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get accounts that account is following."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", f"/accounts/{account_id}/following", params=params)

@mcp.tool()
def follow_account(account_id: str) -> dict:
    """Follow an account."""
    return make_request("POST", f"/accounts/{account_id}/follow")

@mcp.tool()
def unfollow_account(account_id: str) -> dict:
    """Unfollow an account."""
    return make_request("POST", f"/accounts/{account_id}/unfollow")

@mcp.tool()
def block_account(account_id: str) -> dict:
    """Block an account."""
    return make_request("POST", f"/accounts/{account_id}/block")

@mcp.tool()
def unblock_account(account_id: str) -> dict:
    """Unblock an account."""
    return make_request("POST", f"/accounts/{account_id}/unblock")

@mcp.tool()
def mute_account(account_id: str, notifications: bool = True) -> dict:
    """Mute an account."""
    return make_request("POST", f"/accounts/{account_id}/mute", json={"notifications": notifications})

@mcp.tool()
def unmute_account(account_id: str) -> dict:
    """Unmute an account."""
    return make_request("POST", f"/accounts/{account_id}/unmute")

@mcp.tool()
def get_account_relationships(account_ids: list) -> dict:
    """Check relationships to accounts."""
    return make_request("GET", "/accounts/relationships", params={"id[]": account_ids})

@mcp.tool()
def search_accounts(q: str, limit: int = 40, resolve: bool = False) -> dict:
    """Search for accounts."""
    return make_request("GET", "/accounts/search", params={"q": q, "limit": limit, "resolve": resolve})

@mcp.tool()
def post_status(status: str, in_reply_to_id: Optional[str] = None, media_ids: Optional[list] = None, sensitive: bool = False, spoiler_text: Optional[str] = None, visibility: str = "public", scheduled_at: Optional[str] = None) -> dict:
    """Post a new status."""
    data = {"status": status, "sensitive": sensitive, "visibility": visibility}
    if in_reply_to_id: data["in_reply_to_id"] = in_reply_to_id
    if media_ids: data["media_ids"] = media_ids
    if spoiler_text: data["spoiler_text"] = spoiler_text
    if scheduled_at: data["scheduled_at"] = scheduled_at
    return make_request("POST", "/statuses", json=data)

@mcp.tool()
def get_status(status_id: str) -> dict:
    """Get a status."""
    return make_request("GET", f"/statuses/{status_id}")

@mcp.tool()
def delete_status(status_id: str) -> dict:
    """Delete a status."""
    return make_request("DELETE", f"/statuses/{status_id}")

@mcp.tool()
def get_status_context(status_id: str) -> dict:
    """Get status context."""
    return make_request("GET", f"/statuses/{status_id}/context")

@mcp.tool()
def favourite_status(status_id: str) -> dict:
    """Favourite a status."""
    return make_request("POST", f"/statuses/{status_id}/favourite")

@mcp.tool()
def unfavourite_status(status_id: str) -> dict:
    """Unfavourite a status."""
    return make_request("POST", f"/statuses/{status_id}/unfavourite")

@mcp.tool()
def boost_status(status_id: str) -> dict:
    """Boost a status."""
    return make_request("POST", f"/statuses/{status_id}/reblog")

@mcp.tool()
def unboost_status(status_id: str) -> dict:
    """Unboost a status."""
    return make_request("POST", f"/statuses/{status_id}/unreblog")

@mcp.tool()
def bookmark_status(status_id: str) -> dict:
    """Bookmark a status."""
    return make_request("POST", f"/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str) -> dict:
    """Unbookmark a status."""
    return make_request("POST", f"/statuses/{status_id}/unbookmark")

@mcp.tool()
def pin_status(status_id: str) -> dict:
    """Pin a status."""
    return make_request("POST", f"/statuses/{status_id}/pin")

@mcp.tool()
def unpin_status(status_id: str) -> dict:
    """Unpin a status."""
    return make_request("POST", f"/statuses/{status_id}/unpin")

@mcp.tool()
def edit_status(status_id: str, status: str, spoiler_text: Optional[str] = None, sensitive: Optional[bool] = None) -> dict:
    """Edit a status."""
    data = {"status": status}
    if spoiler_text is not None: data["spoiler_text"] = spoiler_text
    if sensitive is not None: data["sensitive"] = sensitive
    return make_request("PUT", f"/statuses/{status_id}", json=data)

@mcp.tool()
def get_home_timeline(limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get home timeline."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(local: bool = False, remote: bool = False, only_media: bool = False, limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get public timeline."""
    params = {"local": local, "remote": remote, "only_media": only_media, "limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: bool = False, remote: bool = False, only_media: bool = False, limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get hashtag timeline."""
    params = {"local": local, "remote": remote, "only_media": only_media, "limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", f"/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get list timeline."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", f"/timelines/list/{list_id}", params=params)

@mcp.tool()
def get_notifications(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[list] = None, exclude_types: Optional[list] = None) -> dict:
    """Get notifications."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    if types: params["types[]"] = types
    if exclude_types: params["exclude_types[]"] = exclude_types
    return make_request("GET", "/notifications", params=params)

@mcp.tool()
def get_notification(notification_id: str) -> dict:
    """Get a notification."""
    return make_request("GET", f"/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str) -> dict:
    """Dismiss a notification."""
    return make_request("POST", f"/notifications/{notification_id}/dismiss")

@mcp.tool()
def clear_notifications() -> dict:
    """Clear all notifications."""
    return make_request("POST", "/notifications/clear")

@mcp.tool()
def get_unread_notification_count(limit: int = 100) -> dict:
    """Get unread notification count."""
    return make_request("GET", "/notifications/unread_count", params={"limit": limit})

@mcp.tool()
def search(q: str, type: Optional[str] = None, limit: int = 20, offset: int = 0, resolve: bool = False) -> dict:
    """Search."""
    params = {"q": q, "limit": limit, "offset": offset, "resolve": resolve}
    if type: params["type"] = type
    return make_request("GET", "/search", params=params)

@mcp.tool()
def get_lists() -> dict:
    """Get all lists."""
    return make_request("GET", "/lists")

@mcp.tool()
def get_list(list_id: str) -> dict:
    """Get a list."""
    return make_request("GET", f"/lists/{list_id}")

@mcp.tool()
def create_list(title: str, replies_policy: str = "list") -> dict:
    """Create a list."""
    return make_request("POST", "/lists", json={"title": title, "replies_policy": replies_policy})

@mcp.tool()
def update_list(list_id: str, title: str) -> dict:
    """Update a list."""
    return make_request("PUT", f"/lists/{list_id}", json={"title": title})

@mcp.tool()
def delete_list(list_id: str) -> dict:
    """Delete a list."""
    return make_request("DELETE", f"/lists/{list_id}")

@mcp.tool()
def get_list_accounts(list_id: str, limit: int = 40) -> dict:
    """Get list accounts."""
    return make_request("GET", f"/lists/{list_id}/accounts", params={"limit": limit})

@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
    """Add accounts to list."""
    return make_request("POST", f"/lists/{list_id}/accounts", json={"account_ids": account_ids})

@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
    """Remove accounts from list."""
    return make_request("DELETE", f"/lists/{list_id}/accounts", json={"account_ids": account_ids})

@mcp.tool()
def get_bookmarks(limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get bookmarks."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/bookmarks", params=params)

@mcp.tool()
def get_favourites(limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get favourites."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/favourites", params=params)

@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None) -> dict:
    """Upload media."""
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description: data["description"] = description
            headers = get_headers()
            if "Content-Type" in headers: del headers["Content-Type"]
            url = f"{API_BASE_URL}/media"
            response = requests.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_media(media_id: str) -> dict:
    """Get media."""
    return make_request("GET", f"/media/{media_id}")

@mcp.tool()
def update_media(media_id: str, description: Optional[str] = None) -> dict:
    """Update media."""
    data = {}
    if description is not None: data["description"] = description
    return make_request("PUT", f"/media/{media_id}", json=data)

@mcp.tool()
def delete_media(media_id: str) -> dict:
    """Delete media."""
    return make_request("DELETE", f"/media/{media_id}")

@mcp.tool()
def get_instance_info() -> dict:
    """Get instance info."""
    return make_request("GET", "/instance")

@mcp.tool()
def get_instance_peers() -> dict:
    """Get instance peers."""
    return make_request("GET", "/instance/peers")

@mcp.tool()
def get_instance_activity() -> dict:
    """Get instance activity."""
    return make_request("GET", "/instance/activity")

@mcp.tool()
def get_tag(tag_name: str) -> dict:
    """Get tag."""
    return make_request("GET", f"/tags/{tag_name}")

@mcp.tool()
def follow_tag(tag_name: str) -> dict:
    """Follow tag."""
    return make_request("POST", f"/tags/{tag_name}/follow")

@mcp.tool()
def unfollow_tag(tag_name: str) -> dict:
    """Unfollow tag."""
    return make_request("POST", f"/tags/{tag_name}/unfollow")

@mcp.tool()
def get_poll(poll_id: str) -> dict:
    """Get poll."""
    return make_request("GET", f"/polls/{poll_id}")

@mcp.tool()
def vote_on_poll(poll_id: str, choices: list) -> dict:
    """Vote on poll."""
    return make_request("POST", f"/polls/{poll_id}/votes", json={"choices": choices})

@mcp.tool()
def get_conversations(limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get conversations."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/conversations", params=params)

@mcp.tool()
def delete_conversation(conversation_id: str) -> dict:
    """Delete conversation."""
    return make_request("DELETE", f"/conversations/{conversation_id}")

@mcp.tool()
def mark_conversation_as_read(conversation_id: str) -> dict:
    """Mark conversation as read."""
    return make_request("POST", f"/conversations/{conversation_id}/read")

@mcp.tool()
def get_follow_requests(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get follow requests."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/follow_requests", params=params)

@mcp.tool()
def accept_follow_request(account_id: str) -> dict:
    """Accept follow request."""
    return make_request("POST", f"/follow_requests/{account_id}/authorize")

@mcp.tool()
def reject_follow_request(account_id: str) -> dict:
    """Reject follow request."""
    return make_request("POST", f"/follow_requests/{account_id}/reject")

@mcp.tool()
def get_blocks(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get blocks."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/blocks", params=params)

@mcp.tool()
def get_mutes(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get mutes."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/mutes", params=params)

@mcp.tool()
def get_domain_blocks(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get domain blocks."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/domain_blocks", params=params)

@mcp.tool()
def block_domain(domain: str) -> dict:
    """Block domain."""
    return make_request("POST", "/domain_blocks", json={"domain": domain})

@mcp.tool()
def unblock_domain(domain: str) -> dict:
    """Unblock domain."""
    return make_request("DELETE", "/domain_blocks", params={"domain": domain})

@mcp.tool()
def get_filters() -> dict:
    """Get filters."""
    return make_request("GET", "/filters")

@mcp.tool()
def get_filter(filter_id: str) -> dict:
    """Get filter."""
    return make_request("GET", f"/filters/{filter_id}")

@mcp.tool()
def create_filter(title: str, context: list, filter_action: str = "warn", expires_in: Optional[int] = None, keywords: Optional[list] = None) -> dict:
    """Create filter."""
    data = {"title": title, "context": context, "filter_action": filter_action}
    if expires_in is not None: data["expires_in"] = expires_in
    if keywords: data["keywords_attributes"] = [{"keyword": k} for k in keywords]
    return make_request("POST", "/filters", json=data)

@mcp.tool()
def update_filter(filter_id: str, title: Optional[str] = None, context: Optional[list] = None, filter_action: Optional[str] = None) -> dict:
    """Update filter."""
    data = {}
    if title is not None: data["title"] = title
    if context is not None: data["context"] = context
    if filter_action is not None: data["filter_action"] = filter_action
    return make_request("PUT", f"/filters/{filter_id}", json=data)

@mcp.tool()
def delete_filter(filter_id: str) -> dict:
    """Delete filter."""
    return make_request("DELETE", f"/filters/{filter_id}")

@mcp.tool()
def get_preferences() -> dict:
    """Get preferences."""
    return make_request("GET", "/preferences")

@mcp.tool()
def get_endorsements(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get endorsements."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/endorsements", params=params)

@mcp.tool()
def feature_account(account_id: str) -> dict:
    """Feature account."""
    return make_request("POST", f"/accounts/{account_id}/pin")

@mcp.tool()
def unfeature_account(account_id: str) -> dict:
    """Unfeature account."""
    return make_request("POST", f"/accounts/{account_id}/unpin")

@mcp.tool()
def get_announcements() -> dict:
    """Get announcements."""
    return make_request("GET", "/announcements")

@mcp.tool()
def dismiss_announcement(announcement_id: str) -> dict:
    """Dismiss announcement."""
    return make_request("POST", f"/announcements/{announcement_id}/dismiss")

@mcp.tool()
def file_report(account_id: str, comment: Optional[str] = None, status_ids: Optional[list] = None, rule_ids: Optional[list] = None) -> dict:
    """File report."""
    data = {"account_id": account_id}
    if comment: data["comment"] = comment
    if status_ids: data["status_ids"] = status_ids
    if rule_ids: data["rule_ids"] = rule_ids
    return make_request("POST", "/reports", json=data)

@mcp.tool()
def get_scheduled_statuses(limit: int = 20, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get scheduled statuses."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/scheduled_statuses", params=params)

@mcp.tool()
def get_scheduled_status(scheduled_status_id: str) -> dict:
    """Get scheduled status."""
    return make_request("GET", f"/scheduled_statuses/{scheduled_status_id}")

@mcp.tool()
def update_scheduled_status(scheduled_status_id: str, scheduled_at: str) -> dict:
    """Update scheduled status."""
    return make_request("PUT", f"/scheduled_statuses/{scheduled_status_id}", json={"scheduled_at": scheduled_at})

@mcp.tool()
def cancel_scheduled_status(scheduled_status_id: str) -> dict:
    """Cancel scheduled status."""
    return make_request("DELETE", f"/scheduled_statuses/{scheduled_status_id}")

@mcp.tool()
def get_custom_emojis() -> dict:
    """Get custom emojis."""
    return make_request("GET", "/custom_emojis")

@mcp.tool()
def get_directory(limit: int = 40, offset: int = 0, order: str = "active", local: bool = False) -> dict:
    """Get directory."""
    return make_request("GET", "/directory", params={"limit": limit, "offset": offset, "order": order, "local": local})

@mcp.tool()
def get_followed_tags(limit: int = 40, max_id: Optional[str] = None, min_id: Optional[str] = None) -> dict:
    """Get followed tags."""
    params = {"limit": limit}
    if max_id: params["max_id"] = max_id
    if min_id: params["min_id"] = min_id
    return make_request("GET", "/followed_tags", params=params)

@mcp.tool()
def get_featured_tags() -> dict:
    """Get featured tags."""
    return make_request("GET", "/featured_tags")

@mcp.tool()
def feature_tag(name: str) -> dict:
    """Feature tag."""
    return make_request("POST", "/featured_tags", json={"name": name})

@mcp.tool()
def unfeature_tag(featured_tag_id: str) -> dict:
    """Unfeature tag."""
    return make_request("DELETE", f"/featured_tags/{featured_tag_id}")

@mcp.tool()
def get_trending_tags(limit: int = 10) -> dict:
    """Get trending tags."""
    return make_request("GET", "/trends/tags", params={"limit": limit})

@mcp.tool()
def get_trending_statuses(limit: int = 10) -> dict:
    """Get trending statuses."""
    return make_request("GET", "/trends/statuses", params={"limit": limit})

@mcp.tool()
def get_trending_links(limit: int = 10) -> dict:
    """Get trending links."""
    return make_request("GET", "/trends/links", params={"limit": limit})

@mcp.tool()
def get_suggestions(limit: int = 40) -> dict:
    """Get suggestions."""
    return make_request("GET", "/suggestions", params={"limit": limit})

@mcp.tool()
def remove_suggestion(account_id: str) -> dict:
    """Remove suggestion."""
    return make_request("DELETE", f"/suggestions/{account_id}")

if __name__ == "__main__":
    mcp.run()

if __name__ == "__main__":
    mcp.run()
