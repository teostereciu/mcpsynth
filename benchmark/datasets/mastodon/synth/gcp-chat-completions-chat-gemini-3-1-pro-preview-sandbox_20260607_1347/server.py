import os
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mastodon")

def get_base_url() -> str:
    return os.environ.get("MASTODON_BASE_URL", "").rstrip("/")

def get_headers() -> Dict[str, str]:
    token = os.environ.get("MASTODON_ACCESS_TOKEN", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

def make_request(method: str, endpoint: str, params: dict = None, json: dict = None, data: dict = None, files: dict = None) -> Any:
    url = f"{get_base_url()}/api/v1{endpoint}"
    if endpoint.startswith("/api/v2"):
        url = f"{get_base_url()}{endpoint}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=get_headers(),
            params=params,
            json=json,
            data=data,
            files=files
        )
        response.raise_for_status()
        if response.content:
            return response.json()
        return {}
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

# Statuses
@mcp.tool()
def post_status(status: str, media_ids: List[str] = None, in_reply_to_id: str = None, sensitive: bool = False, spoiler_text: str = None, visibility: str = "public") -> Any:
    """Post a new status."""
    data = {"status": status, "visibility": visibility}
    if media_ids: data["media_ids[]"] = media_ids
    if in_reply_to_id: data["in_reply_to_id"] = in_reply_to_id
    if sensitive: data["sensitive"] = "true"
    if spoiler_text: data["spoiler_text"] = spoiler_text
    return make_request("POST", "/statuses", data=data)

@mcp.tool()
def get_status(id: str) -> Any:
    """Get a status by ID."""
    return make_request("GET", f"/statuses/{id}")

@mcp.tool()
def delete_status(id: str) -> Any:
    """Delete a status by ID."""
    return make_request("DELETE", f"/statuses/{id}")

@mcp.tool()
def boost_status(id: str) -> Any:
    """Boost (reblog) a status."""
    return make_request("POST", f"/statuses/{id}/reblog")

@mcp.tool()
def favourite_status(id: str) -> Any:
    """Favourite a status."""
    return make_request("POST", f"/statuses/{id}/favourite")

@mcp.tool()
def get_status_context(id: str) -> Any:
    """Get context (ancestors and descendants) of a status."""
    return make_request("GET", f"/statuses/{id}/context")

# Accounts
@mcp.tool()
def get_authenticated_account() -> Any:
    """Get the authenticated account."""
    return make_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def get_account(id: str) -> Any:
    """Get an account by ID."""
    return make_request("GET", f"/accounts/{id}")

@mcp.tool()
def follow_account(id: str) -> Any:
    """Follow an account."""
    return make_request("POST", f"/accounts/{id}/follow")

@mcp.tool()
def unfollow_account(id: str) -> Any:
    """Unfollow an account."""
    return make_request("POST", f"/accounts/{id}/unfollow")

@mcp.tool()
def get_account_followers(id: str, limit: int = 40) -> Any:
    """Get followers of an account."""
    return make_request("GET", f"/accounts/{id}/followers", params={"limit": limit})

@mcp.tool()
def get_account_following(id: str, limit: int = 40) -> Any:
    """Get accounts followed by an account."""
    return make_request("GET", f"/accounts/{id}/following", params={"limit": limit})

# Timelines
@mcp.tool()
def get_home_timeline(limit: int = 20) -> Any:
    """Get the home timeline."""
    return make_request("GET", "/timelines/home", params={"limit": limit})

@mcp.tool()
def get_public_timeline(local: bool = False, limit: int = 20) -> Any:
    """Get the public timeline."""
    params = {"limit": limit}
    if local: params["local"] = "true"
    return make_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: bool = False, limit: int = 20) -> Any:
    """Get a hashtag timeline."""
    params = {"limit": limit}
    if local: params["local"] = "true"
    return make_request("GET", f"/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20) -> Any:
    """Get a list timeline."""
    return make_request("GET", f"/timelines/list/{list_id}", params={"limit": limit})

# Notifications
@mcp.tool()
def list_notifications(limit: int = 20) -> Any:
    """List notifications."""
    return make_request("GET", "/notifications", params={"limit": limit})

@mcp.tool()
def get_notification(id: str) -> Any:
    """Get a single notification."""
    return make_request("GET", f"/notifications/{id}")

@mcp.tool()
def dismiss_notification(id: str) -> Any:
    """Dismiss a single notification."""
    return make_request("POST", f"/notifications/{id}/dismiss")

@mcp.tool()
def clear_notifications() -> Any:
    """Clear all notifications."""
    return make_request("POST", "/notifications/clear")

# Search
@mcp.tool()
def search(query: str, type: str = None, limit: int = 20) -> Any:
    """Search for accounts, statuses, or hashtags. Type can be 'accounts', 'hashtags', or 'statuses'."""
    params = {"q": query, "limit": limit}
    if type: params["type"] = type
    return make_request("GET", "/api/v2/search", params=params)

# Lists
@mcp.tool()
def create_list(title: str) -> Any:
    """Create a new list."""
    return make_request("POST", "/lists", data={"title": title})

@mcp.tool()
def get_lists() -> Any:
    """Get all lists."""
    return make_request("GET", "/lists")

@mcp.tool()
def get_list(id: str) -> Any:
    """Get a list by ID."""
    return make_request("GET", f"/lists/{id}")

@mcp.tool()
def update_list(id: str, title: str) -> Any:
    """Update a list."""
    return make_request("PUT", f"/lists/{id}", data={"title": title})

@mcp.tool()
def delete_list(id: str) -> Any:
    """Delete a list."""
    return make_request("DELETE", f"/lists/{id}")

@mcp.tool()
def add_accounts_to_list(id: str, account_ids: List[str]) -> Any:
    """Add accounts to a list."""
    return make_request("POST", f"/lists/{id}/accounts", data={"account_ids[]": account_ids})

@mcp.tool()
def remove_accounts_from_list(id: str, account_ids: List[str]) -> Any:
    """Remove accounts from a list."""
    return make_request("DELETE", f"/lists/{id}/accounts", data={"account_ids[]": account_ids})

# Bookmarks
@mcp.tool()
def list_bookmarks(limit: int = 20) -> Any:
    """List bookmarked statuses."""
    return make_request("GET", "/bookmarks", params={"limit": limit})

@mcp.tool()
def add_bookmark(id: str) -> Any:
    """Bookmark a status."""
    return make_request("POST", f"/statuses/{id}/bookmark")

@mcp.tool()
def remove_bookmark(id: str) -> Any:
    """Remove a bookmark from a status."""
    return make_request("POST", f"/statuses/{id}/unbookmark")

# Favourites
@mcp.tool()
def list_favourites(limit: int = 20) -> Any:
    """List favourited statuses."""
    return make_request("GET", "/favourites", params={"limit": limit})

# Media
@mcp.tool()
def upload_media(file_path: str, description: str = None) -> Any:
    """Upload a media attachment."""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {}
            if description:
                data['description'] = description
            return make_request("POST", "/api/v2/media", data=data, files=files)
    except Exception as e:
        return {"error": str(e)}

# Instance
@mcp.tool()
def get_instance_info() -> Any:
    """Get instance info and statistics."""
    return make_request("GET", "/api/v2/instance")

if __name__ == "__main__":
    mcp.run()
