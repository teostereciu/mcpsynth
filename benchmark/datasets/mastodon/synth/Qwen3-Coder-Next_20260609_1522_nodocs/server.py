#!/usr/bin/env python3
"""
Mastodon MCP Server
Implements comprehensive coverage of the Mastodon REST API
"""

import os
import requests
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="mastodon", include_in_builtin_tools=True)

# Configuration
def get_base_url() -> str:
    """Get the Mastodon instance base URL from environment"""
    return os.getenv("MASTODON_BASE_URL", "https://mastodon.social")

def get_access_token() -> str:
    """Get the OAuth access token from environment"""
    token = os.getenv("MASTODON_ACCESS_TOKEN")
    if not token:
        raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")
    return token

def make_request(method: str, endpoint: str, params: Optional[dict] = None, 
                 data: Optional[dict] = None, files: Optional[dict] = None) -> dict:
    """Make a request to the Mastodon API"""
    base_url = get_base_url()
    url = f"{base_url}/api/v1{endpoint}"
    headers = {
        "Authorization": f"Bearer {get_access_token()}"
    }
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            files=files
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Status endpoints

@mcp.tool()
def post_status(status: str, visibility: str = "public", 
                media_ids: Optional[list] = None,
                in_reply_to_id: Optional[str] = None,
                sensitive: bool = False,
                spoiler_text: Optional[str] = None) -> dict:
    """Post a new status (toot) to the user's timeline
    
    Args:
        status: The text content of the status
        visibility: One of 'public', 'unlisted', 'private', 'direct'
        media_ids: List of media IDs to attach to the status
        in_reply_to_id: ID of the status being replied to
        sensitive: Mark the status as sensitive (NSFW)
        spoiler_text: CW/sensitive text to show before expanding the status
    
    Returns:
        The created status object
    """
    data = {
        "status": status,
        "visibility": visibility,
        "sensitive": sensitive
    }
    if media_ids:
        data["media_ids"] = media_ids
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if spoiler_text:
        data["spoiler_text"] = spoiler_text
    
    return make_request("POST", "/statuses", data=data)

@mcp.tool()
def get_status(status_id: str) -> dict:
    """Get a single status by ID
    
    Args:
        status_id: The ID of the status to retrieve
    
    Returns:
        The status object
    """
    return make_request("GET", f"/statuses/{status_id}")

@mcp.tool()
def delete_status(status_id: str) -> dict:
    """Delete a status by ID
    
    Args:
        status_id: The ID of the status to delete
    
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/statuses/{status_id}")

@mcp.tool()
def boost_status(status_id: str) -> dict:
    """Boost (reblog) a status
    
    Args:
        status_id: The ID of the status to boost
    
    Returns:
        The boosted status object
    """
    return make_request("POST", f"/statuses/{status_id}/reblog")

@mcp.tool()
def favourite_status(status_id: str) -> dict:
    """Favourite a status
    
    Args:
        status_id: The ID of the status to favourite
    
    Returns:
        The favourited status object
    """
    return make_request("POST", f"/statuses/{status_id}/favourite")

@mcp.tool()
def unfavourite_status(status_id: str) -> dict:
    """Unfavourite a status
    
    Args:
        status_id: The ID of the status to unfavourite
    
    Returns:
        The un favourited status object
    """
    return make_request("POST", f"/statuses/{status_id}/unfavourite")

@mcp.tool()
def get_status_context(status_id: str) -> dict:
    """Get the conversation context for a status (thread)
    
    Args:
        status_id: The ID of the status
    
    Returns:
        Context object with ancestors and descendants
    """
    return make_request("GET", f"/statuses/{status_id}/context")

@mcp.tool()
def get_status_bookmarked(status_id: str) -> dict:
    """Check if the current user has bookmarked a status
    
    Args:
        status_id: The ID of the status
    
    Returns:
        Boolean indicating if bookmarked
    """
    return make_request("GET", f"/statuses/{status_id}/bookmarked")

@mcp.tool()
def bookmark_status(status_id: str) -> dict:
    """Bookmark a status
    
    Args:
        status_id: The ID of the status to bookmark
    
    Returns:
        The bookmarked status object
    """
    return make_request("POST", f"/statuses/{status_id}/bookmark")

@mcp.tool()
def unbookmark_status(status_id: str) -> dict:
    """Unbookmark a status
    
    Args:
        status_id: The ID of the status to unbookmark
    
    Returns:
        The unbookmarked status object
    """
    return make_request("POST", f"/statuses/{status_id}/unbookmark")

# Accounts endpoints

@mcp.tool()
def get_current_account() -> dict:
    """Get the authenticated user's account
    
    Returns:
        The account object for the current user
    """
    return make_request("GET", "/accounts/verify_credentials")

@mcp.tool()
def get_account(account_id: str) -> dict:
    """Get an account by ID
    
    Args:
        account_id: The ID of the account to retrieve
    
    Returns:
        The account object
    """
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def get_account_statuses(account_id: str, only_media: bool = False, 
                         exclude_replies: bool = False, 
                         exclude_reblogs: bool = False,
                         limit: int = 20) -> list:
    """Get statuses for an account
    
    Args:
        account_id: The ID of the account
        only_media: Only return statuses with media attachments
        exclude_replies: Omit replies
        exclude_reblogs: Omit reblogs
        limit: Number of results to return (max 40)
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if only_media:
        params["only_media"] = True
    if exclude_replies:
        params["exclude_replies"] = True
    if exclude_reblogs:
        params["exclude_reblogs"] = True
    
    return make_request("GET", f"/accounts/{account_id}/statuses", params=params)

@mcp.tool()
def follow_account(account_id: str, reblogs: bool = True) -> dict:
    """Follow an account
    
    Args:
        account_id: The ID of the account to follow
        reblogs: Whether to receive reblogs in timeline (default: True)
    
    Returns:
        The relationship object
    """
    data = {"reblogs": reblogs}
    return make_request("POST", f"/accounts/{account_id}/follow", data=data)

@mcp.tool()
def unfollow_account(account_id: str) -> dict:
    """Unfollow an account
    
    Args:
        account_id: The ID of the account to unfollow
    
    Returns:
        The relationship object
    """
    return make_request("POST", f"/accounts/{account_id}/unfollow")

@mcp.tool()
def get_account_relationships(account_id: str) -> list:
    """Get relationship with an account
    
    Args:
        account_id: The ID of the account
    
    Returns:
        List of relationship objects
    """
    params = {"id[]": [account_id]}
    return make_request("GET", "/accounts/relationships", params=params)

@mcp.tool()
def get_account_followers(account_id: str, limit: int = 40) -> list:
    """Get followers for an account
    
    Args:
        account_id: The ID of the account
        limit: Number of results to return (max 80)
    
    Returns:
        List of account objects
    """
    params = {"limit": limit}
    return make_request("GET", f"/accounts/{account_id}/followers", params=params)

@mcp.tool()
def get_account_following(account_id: str, limit: int = 40) -> list:
    """Get accounts followed by an account
    
    Args:
        account_id: The ID of the account
        limit: Number of results to return (max 80)
    
    Returns:
        List of account objects
    """
    params = {"limit": limit}
    return make_request("GET", f"/accounts/{account_id}/following", params=params)

@mcp.tool()
def search_accounts(query: str, resolve: bool = False, 
                    following: bool = False, limit: int = 40) -> list:
    """Search for accounts by username or display name
    
    Args:
        query: The search query
        resolve: Whether to resolve remote accounts
        following: Only return accounts the current user follows
        limit: Number of results to return (max 40)
    
    Returns:
        List of account objects
    """
    params = {
        "q": query,
        "limit": limit
    }
    if resolve:
        params["resolve"] = True
    if following:
        params["following"] = True
    
    return make_request("GET", "/accounts/search", params=params)

# Timelines endpoints

@mcp.tool()
def get_home_timeline(limit: int = 20, max_id: Optional[str] = None,
                      since_id: Optional[str] = None) -> list:
    """Get the home timeline (statuses from followed accounts)
    
    Args:
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/timelines/home", params=params)

@mcp.tool()
def get_public_timeline(local: bool = False, remote: bool = False,
                        limit: int = 20, max_id: Optional[str] = None,
                        since_id: Optional[str] = None) -> list:
    """Get the public timeline
    
    Args:
        local: Only return local statuses
        remote: Only return remote statuses
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if local:
        params["local"] = True
    if remote:
        params["remote"] = True
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/timelines/public", params=params)

@mcp.tool()
def get_tag_timeline(tag: str, local: bool = False,
                     limit: int = 20, max_id: Optional[str] = None,
                     since_id: Optional[str] = None) -> list:
    """Get statuses for a hashtag
    
    Args:
        tag: The hashtag (without #)
        local: Only return local statuses with this hashtag
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if local:
        params["local"] = True
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", f"/timelines/tag/{tag}", params=params)

@mcp.tool()
def get_list_timeline(list_id: str, limit: int = 20,
                      max_id: Optional[str] = None,
                      since_id: Optional[str] = None) -> list:
    """Get statuses for a list
    
    Args:
        list_id: The ID of the list
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", f"/timelines/list/{list_id}", params=params)

# Notifications endpoints

@mcp.tool()
def list_notifications(limit: int = 20, max_id: Optional[str] = None,
                       since_id: Optional[str] = None,
                       types: Optional[list] = None) -> list:
    """List notifications
    
    Args:
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
        types: Filter by notification types (mention, status, reblog, follow, follow_request, favourite, poll, update)
    
    Returns:
        List of notification objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if types:
        params["types[]"] = types
    
    return make_request("GET", "/notifications", params=params)

@mcp.tool()
def get_notification(notification_id: str) -> dict:
    """Get a single notification by ID
    
    Args:
        notification_id: The ID of the notification
    
    Returns:
        The notification object
    """
    return make_request("GET", f"/notifications/{notification_id}")

@mcp.tool()
def dismiss_notification(notification_id: str) -> dict:
    """Dismiss a notification
    
    Args:
        notification_id: The ID of the notification to dismiss
    
    Returns:
        Empty object on success
    """
    return make_request("POST", f"/notifications/{notification_id}/dismiss")

@mcp.tool()
def clear_notifications() -> dict:
    """Clear all notifications
    
    Returns:
        Empty object on success
    """
    return make_request("POST", "/notifications/clear")

# Search endpoints

@mcp.tool()
def search(query: str, resolve: bool = False, 
           exclude_unreviewed: bool = True) -> dict:
    """Search for accounts, statuses, and hashtags
    
    Args:
        query: The search query
        resolve: For remote queries, try to resolve the query via WebFinger
        exclude_unreviewed: Exclude unreviewed tags
    
    Returns:
        Object with accounts, statuses, and hashtags arrays
    """
    params = {
        "q": query,
        "resolve": resolve,
        "exclude_unreviewed": exclude_unreviewed
    }
    return make_request("GET", "/search", params=params)

@mcp.tool()
def search_accounts(query: str, resolve: bool = False,
                    following: bool = False, limit: int = 40) -> list:
    """Search for accounts by username or display name
    
    Args:
        query: The search query
        resolve: Whether to resolve remote accounts
        following: Only return accounts the current user follows
        limit: Number of results to return (max 40)
    
    Returns:
        List of account objects
    """
    params = {
        "q": query,
        "resolve": resolve,
        "limit": limit
    }
    if following:
        params["following"] = True
    
    return make_request("GET", "/accounts/search", params=params)

@mcp.tool()
def search_hashtags(query: str, exclude_risky: bool = True) -> list:
    """Search for hashtags
    
    Args:
        query: The search query (without #)
        exclude_risky: Exclude risky tags
    
    Returns:
        List of hashtag objects
    """
    params = {
        "q": query,
        "exclude_risky": exclude_risky
    }
    return make_request("GET", "/tags/search", params=params)

# Lists endpoints

@mcp.tool()
def create_list(title: str) -> dict:
    """Create a new list
    
    Args:
        title: The title of the list
    
    Returns:
        The created list object
    """
    data = {"title": title}
    return make_request("POST", "/lists", data=data)

@mcp.tool()
def get_lists() -> list:
    """Get all lists for the current user
    
    Returns:
        List of list objects
    """
    return make_request("GET", "/lists")

@mcp.tool()
def get_list(list_id: str) -> dict:
    """Get a list by ID
    
    Args:
        list_id: The ID of the list
    
    Returns:
        The list object
    """
    return make_request("GET", f"/lists/{list_id}")

@mcp.tool()
def update_list(list_id: str, title: str) -> dict:
    """Update a list title
    
    Args:
        list_id: The ID of the list
        title: The new title
    
    Returns:
        The updated list object
    """
    data = {"title": title}
    return make_request("PUT", f"/lists/{list_id}", data=data)

@mcp.tool()
def delete_list(list_id: str) -> dict:
    """Delete a list
    
    Args:
        list_id: The ID of the list to delete
    
    Returns:
        Empty object on success
    """
    return make_request("DELETE", f"/lists/{list_id}")

@mcp.tool()
def get_list_accounts(list_id: str, limit: int = 40) -> list:
    """Get accounts in a list
    
    Args:
        list_id: The ID of the list
        limit: Number of results to return (max 80)
    
    Returns:
        List of account objects
    """
    params = {"limit": limit}
    return make_request("GET", f"/lists/{list_id}/accounts", params=params)

@mcp.tool()
def add_account_to_list(list_id: str, account_id: str) -> dict:
    """Add an account to a list
    
    Args:
        list_id: The ID of the list
        account_id: The ID of the account to add
    
    Returns:
        Empty object on success
    """
    data = {"account_ids": [account_id]}
    return make_request("POST", f"/lists/{list_id}/accounts", data=data)

@mcp.tool()
def remove_account_from_list(list_id: str, account_id: str) -> dict:
    """Remove an account from a list
    
    Args:
        list_id: The ID of the list
        account_id: The ID of the account to remove
    
    Returns:
        Empty object on success
    """
    data = {"account_ids": [account_id]}
    return make_request("DELETE", f"/lists/{list_id}/accounts", data=data)

# Bookmarks endpoints

@mcp.tool()
def get_bookmarks(limit: int = 20, max_id: Optional[str] = None,
                  since_id: Optional[str] = None) -> list:
    """Get bookmarked statuses
    
    Args:
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/bookmarks", params=params)

# Favourites endpoints

@mcp.tool()
def get_favourites(limit: int = 20, max_id: Optional[str] = None,
                   since_id: Optional[str] = None) -> list:
    """Get favourited statuses
    
    Args:
        limit: Number of results to return (max 40)
        max_id: Return results older than this ID
        since_id: Return results newer than this ID
    
    Returns:
        List of status objects
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/favourites", params=params)

# Media endpoints

@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None,
                 focus_x: Optional[float] = None, focus_y: Optional[float] = None,
                 thumbnail: Optional[str] = None) -> dict:
    """Upload a media attachment
    
    Args:
        file_path: Path to the local file to upload
        description: Description of the media for accessibility
        focus_x: Cropping focus X coordinate (-1 to 1)
        focus_y: Cropping focus Y coordinate (-1 to 1)
        thumbnail: Optional thumbnail file path
    
    Returns:
        The uploaded media object with ID for use in statuses
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    
    base_url = get_base_url()
    url = f"{base_url}/api/v1/media"
    headers = {
        "Authorization": f"Bearer {get_access_token()}"
    }
    
    files = {"file": open(file_path, "rb")}
    if thumbnail:
        files["thumbnail"] = open(thumbnail, "rb")
    
    data = {}
    if description:
        data["description"] = description
    if focus_x is not None:
        data["focus_x"] = str(focus_x)
    if focus_y is not None:
        data["focus_y"] = str(focus_y)
    
    try:
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    finally:
        files["file"].close()
        if thumbnail:
            files["thumbnail"].close()

# Instance endpoints

@mcp.tool()
def get_instance() -> dict:
    """Get instance information
    
    Returns:
        Instance object with configuration and contact info
    """
    return make_request("GET", "/instance")

@mcp.tool()
def get_instance_activity() -> list:
    """Get instance activity statistics
    
    Returns:
        List of activity statistics per week
    """
    return make_request("GET", "/instance/activity")

@mcp.tool()
def get_instance_peers() -> list:
    """Get federated instances this instance connects to
    
    Returns:
        List of federated instance domains
    """
    return make_request("GET", "/instance/peers")

@mcp.tool()
def get_instance_version() -> dict:
    """Get instance version information
    
    Returns:
        Object with version string and other metadata
    """
    return make_request("GET", "/instance/version")

# Account update endpoints

@mcp.tool()
def update_account(display_name: Optional[str] = None,
                   note: Optional[str] = None,
                   avatar: Optional[str] = None,
                   header: Optional[str] = None,
                   locked: Optional[bool] = None,
                   bot: Optional[bool] = None,
                   discoverable: Optional[bool] = None) -> dict:
    """Update the current user's account profile
    
    Args:
        display_name: New display name
        note: New bio/description
        avatar: Path to new avatar image
        header: Path to new header image
        locked: Whether to require follow requests
        bot: Whether account is a bot
        discoverable: Whether to show in profile directory
    
    Returns:
        The updated account object
    """
    data = {}
    if display_name is not None:
        data["display_name"] = display_name
    if note is not None:
        data["note"] = note
    if locked is not None:
        data["locked"] = locked
    if bot is not None:
        data["bot"] = bot
    if discoverable is not None:
        data["discoverable"] = discoverable
    
    base_url = get_base_url()
    url = f"{base_url}/api/v1/accounts/update_credentials"
    headers = {
        "Authorization": f"Bearer {get_access_token()}"
    }
    
    files = {}
    if avatar:
        files["avatar"] = open(avatar, "rb")
    if header:
        files["header"] = open(header, "rb")
    
    try:
        if files:
            # Multipart request for file uploads
            response = requests.patch(url, headers=headers, data=data, files=files)
        else:
            # Regular JSON request
            response = requests.patch(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    finally:
        for f in files.values():
            f.close()

# Run the server
if __name__ == "__main__":
    mcp.run()
