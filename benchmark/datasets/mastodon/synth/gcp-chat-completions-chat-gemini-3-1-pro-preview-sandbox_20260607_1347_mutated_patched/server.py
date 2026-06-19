import os
import requests
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mastodon")

def get_auth_headers() -> dict:
    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    if not token:
        raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")
    return {"Authorization": f"Bearer {token}"}

def get_base_url() -> str:
    url = os.environ.get("MASTODON_BASE_URL")
    if not url:
        raise ValueError("MASTODON_BASE_URL environment variable is required")
    return url.rstrip("/")

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    url = f"{get_base_url()}/api/v1{endpoint}"
    if endpoint.startswith("/api/"):
        url = f"{get_base_url()}{endpoint}"
        
    headers = get_auth_headers()
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_msg = e.response.json()
            except ValueError:
                error_msg = e.response.text
        return {"error": error_msg}

@mcp.tool()
def post_status(status: str, visibility: str = "public", in_reply_to_id: Optional[str] = None, media_ids: Optional[List[str]] = None) -> Any:
    """Post a new status."""
    data = {"status": status, "visibility": visibility}
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        data["media_ids"] = media_ids
    return make_request("POST", "/statuses", json=data)

@mcp.tool()
def get_status(status_id: str) -> Any:
    """View a single status."""
    return make_request("GET", f"/statuses/{status_id}")

@mcp.tool()
def delete_status(status_id: str) -> Any:
    """Delete a status."""
    return make_request("DELETE", f"/statuses/{status_id}")

@mcp.tool()
def boost_status(status_id: str) -> Any:
    """Boost (reblog) a status."""
    return make_request("POST", f"/statuses/{status_id}/reblog")

@mcp.tool()
def favourite_status(status_id: str) -> Any:
    """Favourite a status."""
    return make_request("POST", f"/statuses/{status_id}/favourite")

@mcp.tool()
def get_status_context(status_id: str) -> Any:
    """Get parent and child statuses in context."""
    return make_request("GET", f"/statuses/{status_id}/context")

@mcp.tool()
def get_authenticated_account() -> Any:
    """Get authenticated account."""
    return make_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def get_account(account_id: str) -> Any:
    """Get account by ID."""
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def follow_account(account_id: str) -> Any:
    """Follow account."""
    return make_request("POST", f"/accounts/{account_id}/follow")

@mcp.tool()
def unfollow_account(account_id: str) -> Any:
    """Unfollow account."""
    return make_request("POST", f"/accounts/{account_id}/unfollow")

@mcp.tool()
def get_account_followers(account_id: str) -> Any:
    """Get account's followers."""
    return make_request("GET", f"/accounts/{account_id}/followers")

@mcp.tool()
def get_account_following(account_id: str) -> Any:
    """Get account's following."""
    return make_request("GET", f"/accounts/{account_id}/following")

@mcp.tool()
def get_home_timeline(limit: int = 20) -> Any:
    """Get home timeline."""
    return make_request("GET", "/timelines/home", params={"limit": limit})

@mcp.tool()
def get_public_timeline(local: bool = False, limit: int = 20) -> Any:
    """Get public timeline."""
    return make_request("GET", "/timelines/public", params={"local": local, "limit": limit})

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: bool = False, limit: int = 20) -> Any:
    """Get hashtag timeline."""
    return make_request("GET", f"/timelines/tag/{hashtag}", params={"local": local, "limit": limit})

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20) -> Any:
    """Get list timeline."""
    return make_request("GET", f"/timelines/list/{list_id}", params={"limit": limit})

@mcp.tool()
def list_notifications(limit: int = 20) -> Any:
    """Get all notifications."""
    return make_request("GET", "/notifications", params={"limit": limit})

@mcp.tool()
def get_notification(notification_id: str) -> Any:
    """Get a single notification."""
    return make_request("GET", f"/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str) -> Any:
    """Dismiss a single notification."""
    return make_request("POST", f"/notifications/{notification_id}/dismiss")

@mcp.tool()
def clear_notifications() -> Any:
    """Dismiss all notifications."""
    return make_request("POST", "/notifications/clear")

@mcp.tool()
def search(query: str, type: Optional[str] = None, limit: int = 20) -> Any:
    """Search accounts, statuses, hashtags. Type can be 'accounts', 'hashtags', or 'statuses'."""
    params = {"q": query, "limit": limit}
    if type:
        params["type"] = type
    return make_request("GET", "/api/v2/search", params=params)

@mcp.tool()
def create_list(title: str) -> Any:
    """Create a list."""
    return make_request("POST", "/lists", json={"title": title})

@mcp.tool()
def get_list(list_id: str) -> Any:
    """Show a single list."""
    return make_request("GET", f"/lists/{list_id}")

@mcp.tool()
def update_list(list_id: str, title: str) -> Any:
    """Update a list."""
    return make_request("PUT", f"/lists/{list_id}", json={"title": title})

@mcp.tool()
def delete_list(list_id: str) -> Any:
    """Delete a list."""
    return make_request("DELETE", f"/lists/{list_id}")

@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Any:
    """Add accounts to a list."""
    return make_request("POST", f"/lists/{list_id}/accounts", json={"account_ids": account_ids})

@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Any:
    """Remove accounts from list."""
    return make_request("DELETE", f"/lists/{list_id}/accounts", json={"account_ids": account_ids})

@mcp.tool()
def list_bookmarks(limit: int = 20) -> Any:
    """View bookmarked statuses."""
    return make_request("GET", "/bookmarks", params={"limit": limit})

@mcp.tool()
def bookmark_status(status_id: str) -> Any:
    """Bookmark a status."""
    return make_request("POST", f"/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str) -> Any:
    """Undo bookmark of a status."""
    return make_request("POST", f"/statuses/{status_id}/unbookmark")

@mcp.tool()
def list_favourites(limit: int = 20) -> Any:
    """View favourited statuses."""
    return make_request("GET", "/favourites", params={"limit": limit})

@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None) -> Any:
    """Upload media as an attachment."""
    with open(file_path, "rb") as f:
        files = {"file": f}
        data = {}
        if description:
            data["description"] = description
        return make_request("POST", "/api/v2/media", files=files, data=data)

@mcp.tool()
def get_instance_info() -> Any:
    """View server information."""
    return make_request("GET", "/api/v2/instance")

if __name__ == "__main__":
    mcp.run()
