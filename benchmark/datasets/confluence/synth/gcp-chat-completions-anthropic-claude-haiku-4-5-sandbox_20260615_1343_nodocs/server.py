#!/usr/bin/env python3
"""
MCP Server for Confluence Cloud REST API

Implements tools for managing pages, spaces, comments, attachments, labels,
and other Confluence content via the REST API.
"""

import os
import json
import base64
from typing import Any, Optional
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("confluence-api")

# Configuration from environment
CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

# Validate required configuration
if not all([CONFLUENCE_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
    raise ValueError(
        "Missing required environment variables: "
        "CONFLUENCE_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN"
    )


def get_auth_header() -> dict:
    """Generate HTTP Basic Auth header for Confluence API."""
    credentials = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}


def make_request(
    method: str,
    endpoint: str,
    data: Optional[dict] = None,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> dict:
    """
    Make an HTTP request to Confluence API.
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE, etc.)
        endpoint: API endpoint path (e.g., "/wiki/rest/api/content")
        data: JSON body for POST/PUT requests
        params: Query parameters
        headers: Additional headers
    
    Returns:
        Response as dict, or error dict if request fails
    """
    url = CONFLUENCE_BASE_URL + endpoint
    req_headers = get_auth_header()
    req_headers["Content-Type"] = "application/json"
    if headers:
        req_headers.update(headers)
    
    try:
        response = requests.request(
            method=method,
            url=url,
            json=data,
            params=params,
            headers=req_headers,
            timeout=30,
        )
        
        # Handle different response codes
        if response.status_code in [200, 201, 202, 204]:
            if response.text:
                return response.json()
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Not found", "status": 404}
        elif response.status_code == 403:
            return {"error": "Forbidden", "status": 403}
        elif response.status_code == 400:
            try:
                return {"error": response.json(), "status": 400}
            except:
                return {"error": response.text, "status": 400}
        else:
            try:
                return {"error": response.json(), "status": response.status_code}
            except:
                return {"error": response.text, "status": response.status_code}
    except requests.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# PAGES (v2 API)
# ============================================================================


@server.tool()
def create_page(
    title: str,
    space_key: Optional[str] = None,
    body: Optional[str] = None,
    parent_id: Optional[str] = None,
) -> dict:
    """
    Create a new page in Confluence.
    
    Args:
        title: Page title
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY)
        body: Page body content (storage format)
        parent_id: Parent page ID for nested pages
    
    Returns:
        Created page object or error
    """
    space_key = space_key or CONFLUENCE_SPACE_KEY
    if not space_key:
        return {"error": "space_key required"}
    
    payload = {
        "spaceId": space_key,
        "title": title,
        "body": {"representation": "storage", "value": body or ""},
    }
    
    if parent_id:
        payload["parentId"] = parent_id
    
    return make_request("POST", "/wiki/api/v2/pages", data=payload)


@server.tool()
def get_page(page_id: str, expand: Optional[str] = None) -> dict:
    """
    Get a page by ID.
    
    Args:
        page_id: Page ID
        expand: Comma-separated list of properties to expand
    
    Returns:
        Page object or error
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}", params=params)


@server.tool()
def update_page(
    page_id: str,
    title: Optional[str] = None,
    body: Optional[str] = None,
    version_number: Optional[int] = None,
) -> dict:
    """
    Update an existing page.
    
    Args:
        page_id: Page ID
        title: New page title
        body: New page body (storage format)
        version_number: Current version number (required for optimistic locking)
    
    Returns:
        Updated page object or error
    """
    # First get current page to get version if not provided
    if version_number is None:
        current = make_request("GET", f"/wiki/api/v2/pages/{page_id}")
        if "error" in current:
            return current
        version_number = current.get("version", {}).get("number", 1)
    
    payload = {
        "version": {"number": version_number + 1},
    }
    
    if title:
        payload["title"] = title
    if body:
        payload["body"] = {"representation": "storage", "value": body}
    
    return make_request("PUT", f"/wiki/api/v2/pages/{page_id}", data=payload)


@server.tool()
def delete_page(page_id: str) -> dict:
    """
    Delete a page.
    
    Args:
        page_id: Page ID
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/api/v2/pages/{page_id}")


@server.tool()
def get_page_children(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """
    Get child pages of a page.
    
    Args:
        page_id: Parent page ID
        limit: Maximum results per page
        cursor: Pagination cursor
    
    Returns:
        List of child pages or error
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/children", params=params)


@server.tool()
def get_page_ancestors(page_id: str) -> dict:
    """
    Get ancestor pages of a page.
    
    Args:
        page_id: Page ID
    
    Returns:
        List of ancestor pages or error
    """
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/ancestors")


@server.tool()
def move_page(page_id: str, target_parent_id: Optional[str] = None, position: str = "append") -> dict:
    """
    Move a page to a new location.
    
    Args:
        page_id: Page ID to move
        target_parent_id: New parent page ID (None for top-level)
        position: "append" or "before"
    
    Returns:
        Updated page object or error
    """
    payload = {"position": position}
    if target_parent_id:
        payload["targetParentId"] = target_parent_id
    
    return make_request("PUT", f"/wiki/api/v2/pages/{page_id}/move", data=payload)


@server.tool()
def get_page_versions(page_id: str, limit: int = 25) -> dict:
    """
    Get version history of a page.
    
    Args:
        page_id: Page ID
        limit: Maximum results
    
    Returns:
        List of page versions or error
    """
    params = {"limit": limit}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/versions", params=params)


@server.tool()
def get_page_version(page_id: str, version_id: str) -> dict:
    """
    Get a specific version of a page.
    
    Args:
        page_id: Page ID
        version_id: Version ID
    
    Returns:
        Page version object or error
    """
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/versions/{version_id}")


@server.tool()
def restore_page_version(page_id: str, version_id: str) -> dict:
    """
    Restore a page to a previous version.
    
    Args:
        page_id: Page ID
        version_id: Version ID to restore
    
    Returns:
        Updated page object or error
    """
    payload = {"versionId": version_id}
    return make_request("POST", f"/wiki/api/v2/pages/{page_id}/restore-version", data=payload)


# ============================================================================
# SPACES (v2 API)
# ============================================================================


@server.tool()
def list_spaces(limit: int = 25, cursor: Optional[str] = None, type_filter: Optional[str] = None) -> dict:
    """
    List spaces in Confluence.
    
    Args:
        limit: Maximum results per page
        cursor: Pagination cursor
        type_filter: Filter by space type (e.g., "global", "personal")
    
    Returns:
        List of spaces or error
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if type_filter:
        params["type"] = type_filter
    
    return make_request("GET", "/wiki/api/v2/spaces", params=params)


@server.tool()
def get_space(space_id: str) -> dict:
    """
    Get a space by ID.
    
    Args:
        space_id: Space ID
    
    Returns:
        Space object or error
    """
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}")


@server.tool()
def create_space(
    key: str,
    name: str,
    description: Optional[str] = None,
) -> dict:
    """
    Create a new space.
    
    Args:
        key: Space key (unique identifier)
        name: Space name
        description: Space description
    
    Returns:
        Created space object or error
    """
    payload = {
        "key": key,
        "name": name,
    }
    if description:
        payload["description"] = description
    
    return make_request("POST", "/wiki/api/v2/spaces", data=payload)


@server.tool()
def delete_space(space_id: str) -> dict:
    """
    Delete a space.
    
    Args:
        space_id: Space ID
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/api/v2/spaces/{space_id}")


@server.tool()
def get_space_pages(space_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """
    Get pages in a space.
    
    Args:
        space_id: Space ID
        limit: Maximum results per page
        cursor: Pagination cursor
    
    Returns:
        List of pages or error
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/pages", params=params)


# ============================================================================
# COMMENTS (v2 API)
# ============================================================================


@server.tool()
def create_comment(
    page_id: str,
    body: str,
    parent_comment_id: Optional[str] = None,
) -> dict:
    """
    Create a comment on a page.
    
    Args:
        page_id: Page ID
        body: Comment body (storage format)
        parent_comment_id: Parent comment ID for nested comments
    
    Returns:
        Created comment object or error
    """
    payload = {
        "body": {"representation": "storage", "value": body},
    }
    
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    
    return make_request("POST", f"/wiki/api/v2/pages/{page_id}/comments", data=payload)


@server.tool()
def get_page_comments(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """
    Get comments on a page.
    
    Args:
        page_id: Page ID
        limit: Maximum results per page
        cursor: Pagination cursor
    
    Returns:
        List of comments or error
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/comments", params=params)


@server.tool()
def get_comment(comment_id: str) -> dict:
    """
    Get a specific comment.
    
    Args:
        comment_id: Comment ID
    
    Returns:
        Comment object or error
    """
    return make_request("GET", f"/wiki/api/v2/comments/{comment_id}")


@server.tool()
def update_comment(comment_id: str, body: str) -> dict:
    """
    Update a comment.
    
    Args:
        comment_id: Comment ID
        body: New comment body (storage format)
    
    Returns:
        Updated comment object or error
    """
    payload = {
        "body": {"representation": "storage", "value": body},
    }
    
    return make_request("PUT", f"/wiki/api/v2/comments/{comment_id}", data=payload)


@server.tool()
def delete_comment(comment_id: str) -> dict:
    """
    Delete a comment.
    
    Args:
        comment_id: Comment ID
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/api/v2/comments/{comment_id}")


# ============================================================================
# ATTACHMENTS (v2 API)
# ============================================================================


@server.tool()
def list_attachments(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """
    List attachments on a page.
    
    Args:
        page_id: Page ID
        limit: Maximum results per page
        cursor: Pagination cursor
    
    Returns:
        List of attachments or error
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/attachments", params=params)


@server.tool()
def get_attachment(attachment_id: str) -> dict:
    """
    Get attachment metadata.
    
    Args:
        attachment_id: Attachment ID
    
    Returns:
        Attachment object or error
    """
    return make_request("GET", f"/wiki/api/v2/attachments/{attachment_id}")


@server.tool()
def delete_attachment(attachment_id: str) -> dict:
    """
    Delete an attachment.
    
    Args:
        attachment_id: Attachment ID
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/api/v2/attachments/{attachment_id}")


# ============================================================================
# LABELS (v1 API)
# ============================================================================


@server.tool()
def add_labels(content_id: str, labels: list) -> dict:
    """
    Add labels to content.
    
    Args:
        content_id: Content ID (page, blog post, etc.)
        labels: List of label names to add
    
    Returns:
        Updated labels or error
    """
    payload = {"labels": [{"name": label} for label in labels]}
    
    return make_request("POST", f"/wiki/rest/api/content/{content_id}/label", data=payload)


@server.tool()
def get_labels(content_id: str, limit: int = 25, start: int = 0) -> dict:
    """
    Get labels on content.
    
    Args:
        content_id: Content ID
        limit: Maximum results
        start: Starting index for pagination
    
    Returns:
        List of labels or error
    """
    params = {"limit": limit, "start": start}
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/label", params=params)


@server.tool()
def remove_label(content_id: str, label_name: str) -> dict:
    """
    Remove a label from content.
    
    Args:
        content_id: Content ID
        label_name: Label name to remove
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/rest/api/content/{content_id}/label/{label_name}")


# ============================================================================
# SEARCH (v1 API)
# ============================================================================


@server.tool()
def search_content(
    cql: str,
    limit: int = 25,
    start: int = 0,
    expand: Optional[str] = None,
) -> dict:
    """
    Search content using CQL (Confluence Query Language).
    
    Args:
        cql: CQL query string
        limit: Maximum results
        start: Starting index for pagination
        expand: Comma-separated list of properties to expand
    
    Returns:
        Search results or error
    """
    params = {
        "cql": cql,
        "limit": limit,
        "start": start,
    }
    if expand:
        params["expand"] = expand
    
    return make_request("GET", "/wiki/rest/api/content/search", params=params)


# ============================================================================
# BLOG POSTS (v2 API)
# ============================================================================


@server.tool()
def create_blog_post(
    title: str,
    space_key: Optional[str] = None,
    body: Optional[str] = None,
) -> dict:
    """
    Create a blog post.
    
    Args:
        title: Blog post title
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY)
        body: Blog post body (storage format)
    
    Returns:
        Created blog post object or error
    """
    space_key = space_key or CONFLUENCE_SPACE_KEY
    if not space_key:
        return {"error": "space_key required"}
    
    payload = {
        "spaceId": space_key,
        "title": title,
        "body": {"representation": "storage", "value": body or ""},
    }
    
    return make_request("POST", "/wiki/api/v2/blogposts", data=payload)


@server.tool()
def get_blog_post(blog_post_id: str, expand: Optional[str] = None) -> dict:
    """
    Get a blog post by ID.
    
    Args:
        blog_post_id: Blog post ID
        expand: Comma-separated list of properties to expand
    
    Returns:
        Blog post object or error
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}", params=params)


@server.tool()
def update_blog_post(
    blog_post_id: str,
    title: Optional[str] = None,
    body: Optional[str] = None,
    version_number: Optional[int] = None,
) -> dict:
    """
    Update a blog post.
    
    Args:
        blog_post_id: Blog post ID
        title: New title
        body: New body (storage format)
        version_number: Current version number
    
    Returns:
        Updated blog post object or error
    """
    if version_number is None:
        current = make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}")
        if "error" in current:
            return current
        version_number = current.get("version", {}).get("number", 1)
    
    payload = {
        "version": {"number": version_number + 1},
    }
    
    if title:
        payload["title"] = title
    if body:
        payload["body"] = {"representation": "storage", "value": body}
    
    return make_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}", data=payload)


@server.tool()
def delete_blog_post(blog_post_id: str) -> dict:
    """
    Delete a blog post.
    
    Args:
        blog_post_id: Blog post ID
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}")


# ============================================================================
# USERS (v1 API)
# ============================================================================


@server.tool()
def get_current_user() -> dict:
    """
    Get the current authenticated user.
    
    Returns:
        Current user object or error
    """
    return make_request("GET", "/wiki/rest/api/user/current")


@server.tool()
def get_user(account_id: str) -> dict:
    """
    Get a user by account ID.
    
    Args:
        account_id: User account ID
    
    Returns:
        User object or error
    """
    params = {"accountId": account_id}
    return make_request("GET", "/wiki/rest/api/user", params=params)


# ============================================================================
# CONTENT PROPERTIES (v1 API)
# ============================================================================


@server.tool()
def get_content_properties(content_id: str, limit: int = 25, start: int = 0) -> dict:
    """
    Get properties on content.
    
    Args:
        content_id: Content ID
        limit: Maximum results
        start: Starting index
    
    Returns:
        List of properties or error
    """
    params = {"limit": limit, "start": start}
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/property", params=params)


@server.tool()
def get_content_property(content_id: str, property_key: str) -> dict:
    """
    Get a specific property on content.
    
    Args:
        content_id: Content ID
        property_key: Property key
    
    Returns:
        Property object or error
    """
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/property/{property_key}")


@server.tool()
def set_content_property(content_id: str, property_key: str, value: Any) -> dict:
    """
    Set a property on content.
    
    Args:
        content_id: Content ID
        property_key: Property key
        value: Property value (any JSON-serializable object)
    
    Returns:
        Created/updated property or error
    """
    payload = {
        "key": property_key,
        "value": value,
    }
    
    return make_request("POST", f"/wiki/rest/api/content/{content_id}/property", data=payload)


@server.tool()
def delete_content_property(content_id: str, property_key: str) -> dict:
    """
    Delete a property from content.
    
    Args:
        content_id: Content ID
        property_key: Property key
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/rest/api/content/{content_id}/property/{property_key}")


# ============================================================================
# RESTRICTIONS (v1 API)
# ============================================================================


@server.tool()
def get_content_restrictions(content_id: str, expand: Optional[str] = None) -> dict:
    """
    Get restrictions on content.
    
    Args:
        content_id: Content ID
        expand: Comma-separated list of properties to expand
    
    Returns:
        Restrictions object or error
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/restriction", params=params)


@server.tool()
def add_content_restriction(
    content_id: str,
    restriction_type: str,
    user_ids: Optional[list] = None,
    group_names: Optional[list] = None,
) -> dict:
    """
    Add restrictions to content.
    
    Args:
        content_id: Content ID
        restriction_type: "read" or "update"
        user_ids: List of user account IDs
        group_names: List of group names
    
    Returns:
        Updated restrictions or error
    """
    payload = {
        "restrictions": {
            restriction_type: {
                "user": [{"accountId": uid} for uid in (user_ids or [])],
                "group": [{"name": gname} for gname in (group_names or [])],
            }
        }
    }
    
    return make_request("POST", f"/wiki/rest/api/content/{content_id}/restriction", data=payload)


@server.tool()
def remove_content_restriction(
    content_id: str,
    restriction_type: str,
    user_id: Optional[str] = None,
    group_name: Optional[str] = None,
) -> dict:
    """
    Remove a restriction from content.
    
    Args:
        content_id: Content ID
        restriction_type: "read" or "update"
        user_id: User account ID to remove
        group_name: Group name to remove
    
    Returns:
        Success or error
    """
    if user_id:
        return make_request(
            "DELETE",
            f"/wiki/rest/api/content/{content_id}/restriction/{restriction_type}/user/{user_id}",
        )
    elif group_name:
        return make_request(
            "DELETE",
            f"/wiki/rest/api/content/{content_id}/restriction/{restriction_type}/group/{group_name}",
        )
    else:
        return {"error": "user_id or group_name required"}


# ============================================================================
# TEMPLATES (v1 API)
# ============================================================================


@server.tool()
def get_space_templates(space_key: str) -> dict:
    """
    Get templates in a space.
    
    Args:
        space_key: Space key
    
    Returns:
        List of templates or error
    """
    params = {"spaceKey": space_key}
    return make_request("GET", "/wiki/rest/api/template", params=params)


@server.tool()
def get_template(template_id: str) -> dict:
    """
    Get a template by ID.
    
    Args:
        template_id: Template ID
    
    Returns:
        Template object or error
    """
    return make_request("GET", f"/wiki/rest/api/template/{template_id}")


# ============================================================================
# CONTENT (v1 API - Generic)
# ============================================================================


@server.tool()
def get_content(content_id: str, expand: Optional[str] = None) -> dict:
    """
    Get content by ID (generic for pages, blog posts, etc.).
    
    Args:
        content_id: Content ID
        expand: Comma-separated list of properties to expand
    
    Returns:
        Content object or error
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/wiki/rest/api/content/{content_id}", params=params)


@server.tool()
def delete_content(content_id: str) -> dict:
    """
    Delete content by ID (generic for pages, blog posts, etc.).
    
    Args:
        content_id: Content ID
    
    Returns:
        Success or error
    """
    return make_request("DELETE", f"/wiki/rest/api/content/{content_id}")


if __name__ == "__main__":
    server.run()
