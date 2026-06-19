import os
import logging
import requests
from typing import List, Optional, Dict, Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Mastodon API")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mastodon_mcp")

# Get environment variables
BASE_URL = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")

def make_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Helper function to make HTTP requests to the Mastodon API.
    """
    if not ACCESS_TOKEN:
        return {"error": "MASTODON_ACCESS_TOKEN environment variable is not set."}
    if not BASE_URL:
        return {"error": "MASTODON_BASE_URL environment variable is not set."}
    
    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    # Clean up params (remove None values)
    if params:
        params = {k: v for k, v in params.items() if v is not None}
    if json_data:
        json_data = {k: v for k, v in json_data.items() if v is not None}
    if data:
        data = {k: v for k, v in data.items() if v is not None}
        
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data,
            data=data,
            files=files,
            timeout=30
        )
        
        if response.status_code == 204:
            return {"success": True}
            
        try:
            res_data = response.json()
        except ValueError:
            return {
                "error": f"Invalid JSON response from server: {response.text[:200]}",
                "status_code": response.status_code
            }
            
        if not response.ok:
            return {
                "error": res_data.get("error", "Unknown API error"),
                "status_code": response.status_code,
                "details": res_data
            }
            
        return res_data
    except requests.exceptions.RequestException as e:
        return {"error": f"HTTP request failed: {str(e)}"}

# --- Statuses ---

@mcp.tool()
def post_status(
    status: str,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    sensitive: bool = False,
    spoiler_text: Optional[str] = None,
    visibility: str = "public",
    language: Optional[str] = None
) -> Dict[str, Any]:
    """
    Post a new status update (toot) to Mastodon.
    
    Args:
        status: The text content of the status.
        in_reply_to_id: ID of the status being replied to, if any.
        media_ids: Array of attachment IDs to attach to the status.
        sensitive: Mark status as sensitive (NSFW).
        spoiler_text: Content warning text to be shown before the status content.
        visibility: Visibility of the status ("public", "unlisted", "private", "direct").
        language: ISO 639 language code for the status.
    """
    payload = {
        "status": status,
        "in_reply_to_id": in_reply_to_id,
        "media_ids": media_ids,
        "sensitive": sensitive,
        "spoiler_text": spoiler_text,
        "visibility": visibility,
        "language": language
    }
    return make_request("POST", "/api/v1/statuses", json_data=payload)

@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific status by its ID.
    
    Args:
        status_id: The ID of the status to retrieve.
    """
    return make_request("GET", f"/api/v1/statuses/{status_id}")

@mcp.tool()
def delete_status(status_id: str) -> Dict[str, Any]:
    """
    Delete a status by its ID.
    
    Args:
        status_id: The ID of the status to delete.
    """
    return make_request("DELETE", f"/api/v1/statuses/{status_id}")

@mcp.tool()
def boost_status(status_id: str) -> Dict[str, Any]:
    """
    Boost (reblog) a status by its ID.
    
    Args:
        status_id: The ID of the status to boost.
    """
    return make_request("POST", f"/api/v1/statuses/{status_id}/reblog")

@mcp.tool()
def unboost_status(status_id: str) -> Dict[str, Any]:
    """
    Undo a boost (reblog) of a status by its ID.
    
    Args:
        status_id: The ID of the status to unboost.
    """
    return make_request("POST", f"/api/v1/statuses/{status_id}/unreblog")

@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    """
    Favourite a status by its ID.
    
    Args:
        status_id: The ID of the status to favourite.
    """
    return make_request("POST", f"/api/v1/statuses/{status_id}/favourite")

@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    """
    Undo a favourite of a status by its ID.
    
    Args:
        status_id: The ID of the status to unfavourite.
    """
    return make_request("POST", f"/api/v1/statuses/{status_id}/unfavourite")

@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    """
    Get the context/thread of a status (ancestors and descendants).
    
    Args:
        status_id: The ID of the status to get context for.
    """
    return make_request("GET", f"/api/v1/statuses/{status_id}/context")

# --- Accounts ---

@mcp.tool()
def get_authenticated_account() -> Dict[str, Any]:
    """
    Get details of the currently authenticated user account.
    """
    return make_request("GET", "/api/v1/accounts/verify_credentials")

@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """
    Get details of a specific account by its ID.
    
    Args:
        account_id: The ID of the account to retrieve.
    """
    return make_request("GET", f"/api/v1/accounts/{account_id}")

@mcp.tool()
def follow_account(
    account_id: str,
    reblogs: bool = True,
    notify: bool = False
) -> Dict[str, Any]:
    """
    Follow an account by its ID.
    
    Args:
        account_id: The ID of the account to follow.
        reblogs: Receive reblogs from this user.
        notify: Receive notifications when this user posts.
    """
    payload = {
        "reblogs": reblogs,
        "notify": notify
    }
    return make_request("POST", f"/api/v1/accounts/{account_id}/follow", json_data=payload)

@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    """
    Unfollow an account by its ID.
    
    Args:
        account_id: The ID of the account to unfollow.
    """
    return make_request("POST", f"/api/v1/accounts/{account_id}/unfollow")

@mcp.tool()
def get_followers(
    account_id: str,
    limit: int = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get the list of accounts following the specified account.
    
    Args:
        account_id: The ID of the account.
        limit: Maximum number of results to return (default 40).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", f"/api/v1/accounts/{account_id}/followers", params=params)

@mcp.tool()
def get_following(
    account_id: str,
    limit: int = 40,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get the list of accounts followed by the specified account.
    
    Args:
        account_id: The ID of the account.
        limit: Maximum number of results to return (default 40).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", f"/api/v1/accounts/{account_id}/following", params=params)

# --- Timelines ---

@mcp.tool()
def get_home_timeline(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve the home timeline (statuses from followed accounts).
    
    Args:
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", "/api/v1/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve the public timeline (local, remote, or federated).
    
    Args:
        local: Only return local statuses.
        remote: Only return remote statuses.
        only_media: Only return statuses with media attachments.
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", "/api/v1/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve public statuses containing the specified hashtag.
    
    Args:
        hashtag: The hashtag to query (without the '#' symbol).
        local: Only return local statuses.
        remote: Only return remote statuses.
        only_media: Only return statuses with media attachments.
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", f"/api/v1/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(
    list_id: str,
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve the timeline of statuses from accounts in the specified list.
    
    Args:
        list_id: The ID of the list.
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", f"/api/v1/timelines/list/{list_id}", params=params)

# --- Notifications ---

@mcp.tool()
def list_notifications(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    List notifications for the authenticated user.
    
    Args:
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        types: Types of notifications to include (e.g., ["mention", "reblog", "follow"]).
        exclude_types: Types of notifications to exclude.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id,
        "types": types,
        "exclude_types": exclude_types
    }
    return make_request("GET", "/api/v1/notifications", params=params)

@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    """
    Get details of a single notification by its ID.
    
    Args:
        notification_id: The ID of the notification.
    """
    return make_request("GET", f"/api/v1/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    """
    Dismiss a single notification by its ID.
    
    Args:
        notification_id: The ID of the notification to dismiss.
    """
    return make_request("POST", f"/api/v1/notifications/{notification_id}/dismiss")

@mcp.tool()
def clear_notifications() -> Dict[str, Any]:
    """
    Clear all notifications for the authenticated user.
    """
    return make_request("POST", "/api/v1/notifications/clear")

# --- Search ---

@mcp.tool()
def search(
    q: str,
    type: Optional[str] = None,
    resolve: bool = False,
    following: bool = False,
    limit: int = 20
) -> Dict[str, Any]:
    """
    Search for accounts, statuses, or hashtags.
    
    Args:
        q: The search query.
        type: Limit search to "accounts", "statuses", or "hashtags".
        resolve: Attempt WebFinger lookup for accounts to find remote users.
        following: Limit search to followed accounts.
        limit: Maximum number of results to return (default 20).
    """
    params = {
        "q": q,
        "type": type,
        "resolve": resolve,
        "following": following,
        "limit": limit
    }
    return make_request("GET", "/api/v2/search", params=params)

# --- Lists ---

@mcp.tool()
def create_list(title: str, replies_policy: str = "followed") -> Dict[str, Any]:
    """
    Create a new list.
    
    Args:
        title: Title of the list.
        replies_policy: Policy for replies ("followed", "list", "none").
    """
    payload = {
        "title": title,
        "replies_policy": replies_policy
    }
    return make_request("POST", "/api/v1/lists", json_data=payload)

@mcp.tool()
def get_lists() -> Dict[str, Any]:
    """
    Get all lists owned by the authenticated user.
    """
    return make_request("GET", "/api/v1/lists")

@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    """
    Get details of a specific list by its ID.
    
    Args:
        list_id: The ID of the list.
    """
    return make_request("GET", f"/api/v1/lists/{list_id}")

@mcp.tool()
def update_list(
    list_id: str,
    title: str,
    replies_policy: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update a list's title or replies policy.
    
    Args:
        list_id: The ID of the list.
        title: New title of the list.
        replies_policy: Policy for replies ("followed", "list", "none").
    """
    payload = {
        "title": title,
        "replies_policy": replies_policy
    }
    return make_request("PUT", f"/api/v1/lists/{list_id}", json_data=payload)

@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    """
    Delete a list by its ID.
    
    Args:
        list_id: The ID of the list to delete.
    """
    return make_request("DELETE", f"/api/v1/lists/{list_id}")

@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """
    Add accounts to a list.
    
    Args:
        list_id: The ID of the list.
        account_ids: Array of account IDs to add.
    """
    payload = {
        "account_ids": account_ids
    }
    return make_request("POST", f"/api/v1/lists/{list_id}/accounts", json_data=payload)

@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    """
    Remove accounts from a list.
    
    Args:
        list_id: The ID of the list.
        account_ids: Array of account IDs to remove.
    """
    payload = {
        "account_ids": account_ids
    }
    return make_request("DELETE", f"/api/v1/lists/{list_id}/accounts", json_data=payload)

# --- Bookmarks ---

@mcp.tool()
def list_bookmarks(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get bookmarked statuses.
    
    Args:
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", "/api/v1/bookmarks", params=params)

@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    """
    Bookmark a status by its ID.
    
    Args:
        status_id: The ID of the status to bookmark.
    """
    return make_request("POST", f"/api/v1/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    """
    Remove bookmark from a status by its ID.
    
    Args:
        status_id: The ID of the status to unbookmark.
    """
    return make_request("POST", f"/api/v1/statuses/{status_id}/unbookmark")

# --- Favourites ---

@mcp.tool()
def list_favourites(
    limit: int = 20,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get favourited statuses.
    
    Args:
        limit: Maximum number of results to return (default 20).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id
    }
    return make_request("GET", "/api/v1/favourites", params=params)

# --- Media ---

@mcp.tool()
def upload_media_attachment(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None
) -> Dict[str, Any]:
    """
    Upload a media file as an attachment.
    
    Args:
        file_path: Path to the local file to upload.
        description: Alt text description for the media (optional).
        focus: Focal point of the image (two comma-separated floats between -1.0 and 1.0, e.g., "0.5,-0.2").
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
        
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
                
            return make_request("POST", "/api/v1/media", data=data, files=files)
    except Exception as e:
        return {"error": f"Failed to upload media: {str(e)}"}

# --- Instance ---

@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    """
    Get information and statistics about the Mastodon instance.
    """
    return make_request("GET", "/api/v1/instance")

if __name__ == "__main__":
    mcp.run()
