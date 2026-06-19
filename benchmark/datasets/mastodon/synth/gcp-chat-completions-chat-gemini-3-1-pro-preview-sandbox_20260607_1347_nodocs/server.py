import os
import requests
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mastodon")

def get_session():
    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    base_url = os.environ.get("MASTODON_BASE_URL")
    if not token or not base_url:
        raise ValueError("MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL must be set")
    
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    })
    return session, base_url.rstrip("/") + "/api/v1"

def get_session_v2():
    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    base_url = os.environ.get("MASTODON_BASE_URL")
    if not token or not base_url:
        raise ValueError("MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL must be set")
    
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    })
    return session, base_url.rstrip("/") + "/api/v2"

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    try:
        session, base_url = get_session()
        url = f"{base_url}{endpoint}"
        response = session.request(method, url, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except Exception as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

def make_request_v2(method: str, endpoint: str, **kwargs) -> Any:
    try:
        session, base_url = get_session_v2()
        url = f"{base_url}{endpoint}"
        response = session.request(method, url, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except Exception as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

# Statuses
@mcp.tool()
def post_status(status: str, media_ids: Optional[List[str]] = None, in_reply_to_id: Optional[str] = None, sensitive: Optional[bool] = None, spoiler_text: Optional[str] = None, visibility: Optional[str] = None) -> Any:
    """Post a new status."""
    data = {"status": status}
    if media_ids: data["media_ids"] = media_ids
    if in_reply_to_id: data["in_reply_to_id"] = in_reply_to_id
    if sensitive is not None: data["sensitive"] = sensitive
    if spoiler_text: data["spoiler_text"] = spoiler_text
    if visibility: data["visibility"] = visibility
    return make_request("POST", "/statuses", json=data)

@mcp.tool()
def get_status(id: str) -> Any:
    """Get a status by ID."""
    return make_request("GET", f"/statuses/{id}")

@mcp.tool()
def delete_status(id: str) -> Any:
    """Delete a status."""
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
def get_account_followers(id: str, limit: Optional[int] = None) -> Any:
    """Get followers of an account."""
    params = {}
    if limit: params["limit"] = limit
    return make_request("GET", f"/accounts/{id}/followers", params=params)

@mcp.tool()
def get_account_following(id: str, limit: Optional[int] = None) -> Any:
    """Get accounts followed by an account."""
    params = {}
    if limit: params["limit"] = limit
    return make_request("GET", f"/accounts/{id}/following", params=params)

# Timelines
@mcp.tool()
def get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """Get the home timeline."""
    params = {}
    if limit: params["limit"] = limit
    if max_id: params["max_id"] = max_id
    if since_id: params["since_id"] = since_id
    return make_request("GET", "/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(local: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """Get the public timeline."""
    params = {}
    if local is not None: params["local"] = local
    if limit: params["limit"] = limit
    if max_id: params["max_id"] = max_id
    if since_id: params["since_id"] = since_id
    return make_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_hashtag_timeline(hashtag: str, local: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """Get a hashtag timeline."""
    params = {}
    if local is not None: params["local"] = local
    if limit: params["limit"] = limit
    if max_id: params["max_id"] = max_id
    if since_id: params["since_id"] = since_id
    return make_request("GET", f"/timelines/tag/{hashtag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """Get a list timeline."""
    params = {}
    if limit: params["limit"] = limit
    if max_id: params["max_id"] = max_id
    if since_id: params["since_id"] = since_id
    return make_request("GET", f"/timelines/list/{list_id}", params=params)

# Notifications
@mcp.tool()
def get_notifications(limit: Optional[int] = None, types: Optional[List[str]] = None, exclude_types: Optional[List[str]] = None) -> Any:
    """Get notifications."""
    params = {}
    if limit: params["limit"] = limit
    if types: params["types[]"] = types
    if exclude_types: params["exclude_types[]"] = exclude_types
    return make_request("GET", "/notifications", params=params)

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
def search(q: str, type: Optional[str] = None, limit: Optional[int] = None) -> Any:
    """Search for accounts, statuses, or hashtags."""
    params = {"q": q}
    if type: params["type"] = type
    if limit: params["limit"] = limit
    return make_request_v2("GET", "/search", params=params)

# Lists
@mcp.tool()
def get_lists() -> Any:
    """Get all lists."""
    return make_request("GET", "/lists")

@mcp.tool()
def create_list(title: str) -> Any:
    """Create a new list."""
    return make_request("POST", "/lists", json={"title": title})

@mcp.tool()
def get_list(id: str) -> Any:
    """Get a list by ID."""
    return make_request("GET", f"/lists/{id}")

@mcp.tool()
def update_list(id: str, title: str) -> Any:
    """Update a list."""
    return make_request("PUT", f"/lists/{id}", json={"title": title})

@mcp.tool()
def delete_list(id: str) -> Any:
    """Delete a list."""
    return make_request("DELETE", f"/lists/{id}")

@mcp.tool()
def get_list_accounts(id: str, limit: Optional[int] = None) -> Any:
    """Get accounts in a list."""
    params = {}
    if limit: params["limit"] = limit
    return make_request("GET", f"/lists/{id}/accounts", params=params)

@mcp.tool()
def add_accounts_to_list(id: str, account_ids: List[str]) -> Any:
    """Add accounts to a list."""
    return make_request("POST", f"/lists/{id}/accounts", json={"account_ids": account_ids})

@mcp.tool()
def remove_accounts_from_list(id: str, account_ids: List[str]) -> Any:
    """Remove accounts from a list."""
    return make_request("DELETE", f"/lists/{id}/accounts", json={"account_ids": account_ids})

# Bookmarks
@mcp.tool()
def get_bookmarks(limit: Optional[int] = None) -> Any:
    """Get bookmarked statuses."""
    params = {}
    if limit: params["limit"] = limit
    return make_request("GET", "/bookmarks", params=params)

@mcp.tool()
def bookmark_status(id: str) -> Any:
    """Bookmark a status."""
    return make_request("POST", f"/statuses/{id}/bookmark")

@mcp.tool()
def unbookmark_status(id: str) -> Any:
    """Unbookmark a status."""
    return make_request("POST", f"/statuses/{id}/unbookmark")

# Favourites
@mcp.tool()
def get_favourites(limit: Optional[int] = None) -> Any:
    """Get favourited statuses."""
    params = {}
    if limit: params["limit"] = limit
    return make_request("GET", "/favourites", params=params)

# Media
@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None) -> Any:
    """Upload a media attachment."""
    try:
        session, base_url = get_session_v2()
        url = f"{base_url}/media"
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            response = session.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}

# Instance
@mcp.tool()
def get_instance() -> Any:
    """Get instance information."""
    return make_request_v2("GET", "/instance")

if __name__ == "__main__":
    mcp.run()
