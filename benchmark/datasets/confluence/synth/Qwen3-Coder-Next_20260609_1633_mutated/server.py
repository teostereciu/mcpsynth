#!/usr/bin/env python3
"""
Confluence Cloud MCP Server
A server implementing the Model Context Protocol for Confluence Cloud REST API.
"""

import os
import json
import base64
import re
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP
import requests


# Initialize FastMCP server
mcp = FastMCP(
    name="confluence",
    version="1.0.0",
)

# Environment variables for authentication
BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://yoursite.atlassian.net/wiki")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "SYNTH")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

# Authentication header for Basic auth
AUTH_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_auth() -> tuple:
    """Return authentication tuple for HTTP Basic auth."""
    return (EMAIL, API_TOKEN)


def api_request(method: str, path: str, params: Dict = None, json_data: Dict = None) -> Dict:
    """Make an API request to Confluence Cloud."""
    url = f"{BASE_URL}{path}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=AUTH_HEADERS,
            auth=get_auth(),
            params=params,
            json=json_data,
            timeout=30
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            if response.status_code == 204:  # No content
                return {"status": "success", "message": "Operation completed successfully"}
            try:
                return response.json()
            except:
                return {"status": "success", "data": response.text}
        else:
            return {
                "error": f"API request failed with status {response.status_code}",
                "status_code": response.status_code,
                "response": response.text[:500]  # Limit error response size
            }
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# SPACE OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_list_spaces(
    space_type: str = None,
    content_status: str = None,
    labels: str = None,
    sort: str = "id",
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    List all spaces accessible to the current user.
    
    Args:
        space_type: Filter by space type (global, personal, etc.)
        content_status: Filter by content status
        labels: Filter by labels (comma-separated)
        sort: Sort order
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of spaces with details
    """
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    if space_type:
        params["type"] = space_type
    if content_status:
        params["content_status"] = content_status
    if labels:
        params["labels"] = labels
        
    result = api_request("GET", "/wiki/api/v2/spaces", params=params)
    return result


@mcp.tool()
def confluence_get_space(space_id: int) -> Dict:
    """
    Get details for a specific space by ID.
    
    Args:
        space_id: The ID of the space to retrieve
        
    Returns:
        Space details including name, key, description, etc.
    """
    result = api_request("GET", f"/wiki/api/v2/spaces/{space_id}")
    return result


@mcp.tool()
def confluence_get_space_by_key(space_key: str) -> Dict:
    """
    Get details for a specific space by key.
    
    Args:
        space_key: The key of the space (e.g., SYNTH)
        
    Returns:
        Space details including name, key, description, etc.
    """
    # First get space ID from key
    spaces = confluence_list_spaces(space_type="global")
    if "results" in spaces:
        for space in spaces["results"]:
            if space.get("key") == space_key:
                return confluence_get_space(space["id"])
    return {"error": f"Space with key '{space_key}' not found"}


@mcp.tool()
def confluence_create_space(
    name: str,
    space_key: str = None,
    description: str = None,
    template_key: str = "space-template"
) -> Dict:
    """
    Create a new space.
    
    Args:
        name: Name of the space (required)
        space_key: Space key (auto-generated if not provided)
        description: Description of the space
        template_key: Template to use for the space
        
    Returns:
        Created space details
    """
    payload = {
        "name": name,
        "templateKey": template_key
    }
    if space_key:
        payload["key"] = space_key
    if description:
        payload["description"] = {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
        
    result = api_request("POST", "/wiki/api/v2/spaces", json_data=payload)
    return result


# ============================================================================
# PAGE OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_list_pages(
    space_id: int = None,
    sort: str = "createdAt",
    content_status: str = None,
    title: str = None,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    List all pages in a space or across all spaces.
    
    Args:
        space_id: Space ID to filter by (optional)
        sort: Sort order (createdAt, title, etc.)
        content_status: Filter by content status (current, archived, etc.)
        title: Filter by title
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of pages with details
    """
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    if space_id:
        params["spaceId"] = str(space_id)
    if content_status:
        params["content_status"] = content_status
    if title:
        params["title"] = title
        
    result = api_request("GET", "/wiki/api/v2/pages", params=params)
    return result


@mcp.tool()
def confluence_get_page(page_id: int) -> Dict:
    """
    Get details for a specific page by ID.
    
    Args:
        page_id: The ID of the page to retrieve
        
    Returns:
        Page details including title, space, body, etc.
    """
    result = api_request("GET", f"/wiki/api/v2/pages/{page_id}")
    return result


@mcp.tool()
def confluence_create_page(
    space_id: int,
    title: str,
    body: str,
    parent_id: int = None,
    content_status: str = "current",
    subtype: str = None
) -> Dict:
    """
    Create a new page in a space.
    
    Args:
        space_id: ID of the space to create the page in (required)
        title: Page title (required)
        body: Page body content in storage format
        parent_id: ID of parent page (optional, for nested pages)
        content_status: Page status (current or draft)
        subtype: Page subtype (live, blogpost, etc.)
        
    Returns:
        Created page details
    """
    payload = {
        "spaceId": str(space_id),
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        },
        "content_status": content_status
    }
    if parent_id:
        payload["parentId"] = str(parent_id)
    if subtype:
        payload["subtype"] = subtype
        
    result = api_request("POST", "/wiki/api/v2/pages", json_data=payload)
    return result


@mcp.tool()
def confluence_update_page(
    page_id: int,
    title: str = None,
    body: str = None,
    content_status: str = None,
    version_message: str = None
) -> Dict:
    """
    Update an existing page.
    
    Args:
        page_id: The ID of the page to update (required)
        title: New title (optional)
        body: New body content in storage format (optional)
        content_status: New content status (optional)
        version_message: Version message for the update
        
    Returns:
        Updated page details
    """
    # First get current page to preserve existing data
    current_page = confluence_get_page(page_id)
    if "error" in current_page:
        return current_page
    
    payload = {
        "id": str(page_id),
        "type": current_page.get("type", "page"),
    }
    
    # Preserve existing values if not provided
    if title:
        payload["title"] = title
    else:
        payload["title"] = current_page.get("title")
        
    if content_status:
        payload["content_status"] = content_status
    else:
        payload["content_status"] = current_page.get("content_status", "current")
        
    if body:
        payload["body"] = {
            "representation": "storage",
            "value": body
        }
    elif "body" in current_page:
        payload["body"] = current_page["body"]
        
    # Get current version info
    version = current_page.get("version", {})
    if version:
        payload["version"] = {
            "number": version.get("number", 1) + 1,
        }
        if version_message:
            payload["version"]["message"] = version_message
    else:
        payload["version"] = {"number": 1}
        
    result = api_request("PUT", f"/wiki/api/v2/pages/{page_id}", json_data=payload)
    return result


@mcp.tool()
def confluence_delete_page(page_id: int, purge: bool = False, draft: bool = False) -> Dict:
    """
    Delete a page.
    
    Args:
        page_id: The ID of the page to delete
        purge: Permanently delete (purge) the page
        draft: Delete a draft page
        
    Returns:
        Deletion status
    """
    params = {}
    if purge:
        params["purge"] = "true"
    if draft:
        params["draft"] = "true"
        
    result = api_request("DELETE", f"/wiki/api/v2/pages/{page_id}", params=params)
    return result


@mcp.tool()
def confluence_list_page_versions(page_id: int, max_results: int = 25, start: int = 0) -> Dict:
    """
    List all versions of a page.
    
    Args:
        page_id: The ID of the page
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of page versions
    """
    params = {
        "start": start,
        "limit": max_results
    }
    result = api_request("GET", f"/wiki/api/v2/pages/{page_id}/versions", params=params)
    return result


# ============================================================================
# BLOG POST OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_list_blog_posts(
    space_id: int,
    sort: str = "createdAt",
    content_status: str = None,
    title: str = None,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    List all blog posts in a space.
    
    Args:
        space_id: Space ID to filter by (required)
        sort: Sort order
        content_status: Filter by content status
        title: Filter by title
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of blog posts
    """
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    if content_status:
        params["content_status"] = content_status
    if title:
        params["title"] = title
        
    result = api_request("GET", f"/wiki/api/v2/spaces/{space_id}/blogposts", params=params)
    return result


@mcp.tool()
def confluence_get_blog_post(blog_post_id: int) -> Dict:
    """
    Get details for a specific blog post by ID.
    
    Args:
        blog_post_id: The ID of the blog post to retrieve
        
    Returns:
        Blog post details
    """
    result = api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}")
    return result


@mcp.tool()
def confluence_create_blog_post(
    space_id: int,
    title: str,
    body: str,
    content_status: str = "current"
) -> Dict:
    """
    Create a new blog post in a space.
    
    Args:
        space_id: ID of the space to create the blog post in (required)
        title: Blog post title (required)
        body: Blog post body content in storage format
        content_status: Blog post status (current or draft)
        
    Returns:
        Created blog post details
    """
    payload = {
        "spaceId": str(space_id),
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        },
        "content_status": content_status
    }
    
    result = api_request("POST", "/wiki/api/v2/blogposts", json_data=payload)
    return result


@mcp.tool()
def confluence_update_blog_post(
    blog_post_id: int,
    title: str = None,
    body: str = None,
    content_status: str = None,
    version_message: str = None
) -> Dict:
    """
    Update an existing blog post.
    
    Args:
        blog_post_id: The ID of the blog post to update (required)
        title: New title (optional)
        body: New body content (optional)
        content_status: New content status (optional)
        version_message: Version message (optional)
        
    Returns:
        Updated blog post details
    """
    current = confluence_get_blog_post(blog_post_id)
    if "error" in current:
        return current
    
    payload = {
        "id": str(blog_post_id),
        "type": current.get("type", "blogpost"),
    }
    
    if title:
        payload["title"] = title
    else:
        payload["title"] = current.get("title")
        
    if content_status:
        payload["content_status"] = content_status
    else:
        payload["content_status"] = current.get("content_status", "current")
        
    if body:
        payload["body"] = {
            "representation": "storage",
            "value": body
        }
    elif "body" in current:
        payload["body"] = current["body"]
        
    version = current.get("version", {})
    if version:
        payload["version"] = {
            "number": version.get("number", 1) + 1,
        }
        if version_message:
            payload["version"]["message"] = version_message
    else:
        payload["version"] = {"number": 1}
        
    result = api_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}", json_data=payload)
    return result


@mcp.tool()
def confluence_delete_blog_post(blog_post_id: int, purge: bool = False, draft: bool = False) -> Dict:
    """
    Delete a blog post.
    
    Args:
        blog_post_id: The ID of the blog post to delete
        purge: Permanently delete the blog post
        draft: Delete a draft blog post
        
    Returns:
        Deletion status
    """
    params = {}
    if purge:
        params["purge"] = "true"
    if draft:
        params["draft"] = "true"
        
    result = api_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}", params=params)
    return result


# ============================================================================
# SEARCH OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_search(
    cql: str,
    cql_context: str = None,
    max_results: int = 25,
    start: int = 0,
    include_archived_spaces: bool = False,
    exclude_current_spaces: bool = False
) -> Dict:
    """
    Search content using Confluence Query Language (CQL).
    
    Args:
        cql: CQL query string (required)
        cql_context: Context for the CQL query
        max_results: Maximum number of results
        start: Pagination offset
        include_archived_spaces: Include archived spaces in search
        exclude_current_spaces: Exclude current spaces from search
        
    Returns:
        Search results
    """
    params = {
        "cql": cql,
        "start": start,
        "limit": max_results,
        "includeArchivedSpaces": str(include_archived_spaces).lower()
    }
    if cql_context:
        params["cqlcontext"] = cql_context
    if exclude_current_spaces:
        params["excludeCurrentSpaces"] = str(exclude_current_spaces).lower()
        
    result = api_request("GET", "/wiki/rest/api/search", params=params)
    return result


@mcp.tool()
def confluence_search_users(
    cql: str,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    Search users using CQL.
    
    Args:
        cql: CQL query string for user search
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        User search results
    """
    params = {
        "cql": cql,
        "start": start,
        "limit": max_results
    }
    
    result = api_request("GET", "/wiki/rest/api/search/user", params=params)
    return result


# ============================================================================
# COMMENT OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_get_page_comments(
    page_id: int,
    body_format: str = "storage",
    sort: str = "creation",
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    Get footer comments for a page.
    
    Args:
        page_id: The ID of the page
        body_format: Format of the comment body
        sort: Sort order
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of comments
    """
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    if body_format:
        params["body-format"] = body_format
        
    result = api_request("GET", f"/wiki/api/v2/pages/{page_id}/footer-comments", params=params)
    return result


@mcp.tool()
def confluence_create_comment(
    page_id: int = None,
    blog_post_id: int = None,
    body: str = None,
    parent_comment_id: int = None
) -> Dict:
    """
    Create a comment on a page or blog post, or as a reply to another comment.
    
    Args:
        page_id: Page ID to comment on (required if blog_post_id not provided)
        blog_post_id: Blog post ID to comment on (required if page_id not provided)
        body: Comment body content in storage format (required)
        parent_comment_id: ID of parent comment for replies (optional)
        
    Returns:
        Created comment details
    """
    if not body:
        return {"error": "Comment body is required"}
        
    payload = {
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    
    if page_id:
        payload["pageId"] = str(page_id)
    elif blog_post_id:
        payload["blogPostId"] = str(blog_post_id)
        
    if parent_comment_id:
        payload["parentCommentId"] = str(parent_comment_id)
        
    result = api_request("POST", "/wiki/api/v2/footer-comments", json_data=payload)
    return result


@mcp.tool()
def confluence_update_comment(comment_id: int, body: str, version_message: str = None) -> Dict:
    """
    Update an existing comment.
    
    Args:
        comment_id: The ID of the comment to update
        body: New comment body content
        version_message: Version message (optional)
        
    Returns:
        Updated comment details
    """
    current = api_request("GET", f"/wiki/api/v2/footer-comments/{comment_id}")
    if "error" in current:
        return current
        
    payload = {
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": current.get("version", {}).get("number", 1) + 1,
        }
    }
    if version_message:
        payload["version"]["message"] = version_message
        
    result = api_request("PUT", f"/wiki/api/v2/footer-comments/{comment_id}", json_data=payload)
    return result


@mcp.tool()
def confluence_delete_comment(comment_id: int) -> Dict:
    """
    Delete a comment.
    
    Args:
        comment_id: The ID of the comment to delete
        
    Returns:
        Deletion status
    """
    result = api_request("DELETE", f"/wiki/api/v2/footer-comments/{comment_id}")
    return result


@mcp.tool()
def confluence_get_inline_comments(
    page_id: int,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    Get inline comments for a page.
    
    Args:
        page_id: The ID of the page
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of inline comments
    """
    params = {
        "start": start,
        "limit": max_results
    }
    
    result = api_request("GET", f"/wiki/api/v2/pages/{page_id}/inline-comments", params=params)
    return result


# ============================================================================
# ATTACHMENT OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_list_attachments(
    page_id: int = None,
    blog_post_id: int = None,
    sort: str = "createdAt",
    media_type: str = None,
    filename: str = None,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    List attachments for a page or blog post.
    
    Args:
        page_id: Page ID to list attachments for
        blog_post_id: Blog post ID to list attachments for
        sort: Sort order
        media_type: Filter by media type
        filename: Filter by filename
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of attachments
    """
    if not page_id and not blog_post_id:
        return {"error": "Either page_id or blog_post_id must be provided"}
        
    path = f"/wiki/api/v2/pages/{page_id}/attachments" if page_id else f"/wiki/api/v2/blogposts/{blog_post_id}/attachments"
    
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
        
    result = api_request("GET", path, params=params)
    return result


@mcp.tool()
def confluence_get_attachment(attachment_id: int) -> Dict:
    """
    Get details for a specific attachment by ID.
    
    Args:
        attachment_id: The ID of the attachment to retrieve
        
    Returns:
        Attachment details
    """
    result = api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}")
    return result


@mcp.tool()
def confluence_upload_attachment(
    page_id: int,
    file_path: str,
    file_content: str = None,
    content_type: str = "application/octet-stream",
    comment: str = None
) -> Dict:
    """
    Upload an attachment to a page.
    
    Args:
        page_id: Page ID to upload the attachment to (required)
        file_path: Local path to the file (required)
        file_content: Base64-encoded file content (optional if file_path provided)
        content_type: MIME type of the file
        comment: Comment for the attachment
        
    Returns:
        Uploaded attachment details
    """
    # Read file content
    if file_content:
        # Already base64-encoded
        content = base64.b64decode(file_content)
    else:
        try:
            with open(file_path, "rb") as f:
                content = f.read()
        except Exception as e:
            return {"error": f"Failed to read file: {str(e)}"}
    
    # Prepare request
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/attachments"
    
    try:
        with open(file_path, "rb") as f:
            headers = {
                "Accept": "application/json",
                "X-Atlassian-Token": "no-check"
            }
            if comment:
                headers["X-Comment"] = comment
                
            response = requests.post(
                url=url,
                headers=headers,
                auth=get_auth(),
                files={"file": (os.path.basename(file_path), f, content_type)}
            )
            
            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                return {
                    "error": f"Upload failed with status {response.status_code}",
                    "status_code": response.status_code,
                    "response": response.text[:500]
                }
    except Exception as e:
        return {"error": f"Upload failed: {str(e)}"}


@mcp.tool()
def confluence_delete_attachment(attachment_id: int, purge: bool = False) -> Dict:
    """
    Delete an attachment.
    
    Args:
        attachment_id: The ID of the attachment to delete
        purge: Permanently delete the attachment
        
    Returns:
        Deletion status
    """
    params = {}
    if purge:
        params["purge"] = "true"
        
    result = api_request("DELETE", f"/wiki/api/v2/attachments/{attachment_id}", params=params)
    return result


# ============================================================================
# LABEL OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_get_labels(
    content_type: str,
    content_id: int
) -> Dict:
    """
    Get labels for a specific content item.
    
    Args:
        content_type: Type of content (page, blogpost, attachment, space)
        content_id: ID of the content
        
    Returns:
        List of labels
    """
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/labels",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/labels",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/labels",
        "space": f"/wiki/api/v2/spaces/{content_id}/labels",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
        
    result = api_request("GET", path)
    return result


@mcp.tool()
def confluence_add_label(
    content_type: str,
    content_id: int,
    label: str
) -> Dict:
    """
    Add a label to a content item.
    
    Args:
        content_type: Type of content (page, blogpost, attachment, space)
        content_id: ID of the content
        label: Label to add
        
    Returns:
        Updated labels
    """
    # First get existing labels
    existing = confluence_get_labels(content_type, content_id)
    if "error" in existing:
        return existing
    
    labels = existing.get("results", [])
    
    # Check if label already exists
    for existing_label in labels:
        if existing_label.get("name") == label:
            return {"warning": f"Label '{label}' already exists"}
    
    # Create label payload
    payload = {
        "name": label,
        "prefix": "global"
    }
    
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/labels",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/labels",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/labels",
        "space": f"/wiki/api/v2/spaces/{content_id}/labels",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
        
    result = api_request("POST", path, json_data=payload)
    return result


@mcp.tool()
def confluence_remove_label(
    content_type: str,
    content_id: int,
    label: str
) -> Dict:
    """
    Remove a label from a content item.
    
    Args:
        content_type: Type of content
        content_id: ID of the content
        label: Label to remove
        
    Returns:
        Status of removal
    """
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/labels",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/labels",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/labels",
        "space": f"/wiki/api/v2/spaces/{content_id}/labels",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
    
    # Get labels to find the label ID
    labels = confluence_get_labels(content_type, content_id)
    if "error" in labels:
        return labels
        
    label_id = None
    for l in labels.get("results", []):
        if l.get("name") == label:
            label_id = l.get("id")
            break
    
    if not label_id:
        return {"error": f"Label '{label}' not found"}
    
    # Remove the label
    result = api_request("DELETE", f"{path}/{label_id}")
    return result


# ============================================================================
# CONTENT PROPERTIES
# ============================================================================

@mcp.tool()
def confluence_get_content_properties(
    content_type: str,
    content_id: int,
    key: str = None,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    Get content properties for a content item.
    
    Args:
        content_type: Type of content (page, blogpost, attachment)
        content_id: ID of the content
        key: Filter by property key (optional)
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of content properties
    """
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/properties",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/properties",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/properties",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
    
    params = {
        "start": start,
        "limit": max_results
    }
    if key:
        params["key"] = key
        
    result = api_request("GET", path, params=params)
    return result


@mcp.tool()
def confluence_create_content_property(
    content_type: str,
    content_id: int,
    key: str,
    value: Any
) -> Dict:
    """
    Create a content property.
    
    Args:
        content_type: Type of content (page, blogpost, attachment)
        content_id: ID of the content
        key: Property key
        value: Property value
        
    Returns:
        Created property
    """
    payload = {
        "key": key,
        "value": value
    }
    
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/properties",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/properties",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/properties",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
        
    result = api_request("POST", path, json_data=payload)
    return result


@mcp.tool()
def confluence_update_content_property(
    content_type: str,
    content_id: int,
    property_id: int,
    key: str,
    value: Any,
    version_message: str = None
) -> Dict:
    """
    Update a content property.
    
    Args:
        content_type: Type of content
        content_id: ID of the content
        property_id: ID of the property
        key: New property key
        value: New property value
        version_message: Version message (optional)
        
    Returns:
        Updated property
    """
    # First get current property
    current = api_request("GET", f"/wiki/api/v2/{content_type}s/{content_id}/properties/{property_id}")
    if "error" in current:
        # Try alternative path
        current = api_request("GET", f"/wiki/api/v2/{content_type}s/{content_id}/properties/{property_id}")
    
    payload = {
        "key": key,
        "value": value
    }
    
    if "version" in current:
        payload["version"] = {
            "number": current["version"].get("number", 1) + 1
        }
        if version_message:
            payload["version"]["message"] = version_message
    else:
        payload["version"] = {"number": 1}
        
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/properties/{property_id}",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/properties/{property_id}",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/properties/{property_id}",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
        
    result = api_request("PUT", path, json_data=payload)
    return result


@mcp.tool()
def confluence_delete_content_property(
    content_type: str,
    content_id: int,
    property_id: int
) -> Dict:
    """
    Delete a content property.
    
    Args:
        content_type: Type of content
        content_id: ID of the content
        property_id: ID of the property to delete
        
    Returns:
        Deletion status
    """
    paths = {
        "page": f"/wiki/api/v2/pages/{content_id}/properties/{property_id}",
        "blogpost": f"/wiki/api/v2/blogposts/{content_id}/properties/{property_id}",
        "attachment": f"/wiki/api/v2/attachments/{content_id}/properties/{property_id}",
    }
    
    path = paths.get(content_type)
    if not path:
        return {"error": f"Invalid content type: {content_type}"}
        
    result = api_request("DELETE", path)
    return result


# ============================================================================
# VERSION OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_get_page_version(page_id: int, version_number: int) -> Dict:
    """
    Get a specific version of a page.
    
    Args:
        page_id: The ID of the page
        version_number: Version number to retrieve
        
    Returns:
        Version details
    """
    result = api_request("GET", f"/wiki/api/v2/pages/{page_id}/versions/{version_number}")
    return result


@mcp.tool()
def confluence_restore_page_version(
    page_id: int,
    version_number: int,
    version_message: str = None
) -> Dict:
    """
    Restore a page to a previous version.
    
    Args:
        page_id: The ID of the page
        version_number: Version number to restore
        version_message: Message for the new version created by restoration
        
    Returns:
        Restored page details
    """
    # Get current page info
    current = confluence_get_page(page_id)
    if "error" in current:
        return current
    
    # Get version details
    version = confluence_get_page_version(page_id, version_number)
    if "error" in version:
        return version
    
    payload = {
        "id": str(page_id),
        "type": "page",
        "title": current.get("title"),
        "content_status": "current",
        "body": version.get("body", {}),
        "version": {
            "number": current.get("version", {}).get("number", 1) + 1
        }
    }
    
    if version_message:
        payload["version"]["message"] = version_message
        
    result = api_request("PUT", f"/wiki/api/v2/pages/{page_id}", json_data=payload)
    return result


# ============================================================================
# USER OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_get_current_user() -> Dict:
    """
    Get details for the currently authenticated user.
    
    Returns:
        User details
    """
    result = api_request("GET", "/wiki/rest/api/user/current")
    return result


@mcp.tool()
def confluence_get_user_by_account_id(account_id: str) -> Dict:
    """
    Get user details by account ID.
    
    Args:
        account_id: The account ID of the user
        
    Returns:
        User details
    """
    params = {"accountId": account_id}
    result = api_request("GET", "/wiki/rest/api/user", params=params)
    return result


@mcp.tool()
def confluence_get_users_by_ids(account_ids: List[str]) -> Dict:
    """
    Get user details for multiple account IDs.
    
    Args:
        account_ids: List of account IDs
        
    Returns:
        List of user details
    """
    payload = {"accountIds": account_ids}
    result = api_request("POST", "/wiki/api/v2/users-bulk", json_data=payload)
    return result


# ============================================================================
# SPACE CONTENT OPERATIONS
# ============================================================================

@mcp.tool()
def confluence_list_space_pages(
    space_id: int,
    sort: str = "createdAt",
    content_status: str = None,
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    List pages in a specific space.
    
    Args:
        space_id: Space ID
        sort: Sort order
        content_status: Filter by content status
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of pages in the space
    """
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    if content_status:
        params["content_status"] = content_status
        
    result = api_request("GET", f"/wiki/api/v2/spaces/{space_id}/pages", params=params)
    return result


@mcp.tool()
def confluence_list_space_attachments(
    space_id: int,
    sort: str = "createdAt",
    max_results: int = 25,
    start: int = 0
) -> Dict:
    """
    List attachments in a space.
    
    Args:
        space_id: Space ID
        sort: Sort order
        max_results: Maximum number of results
        start: Pagination offset
        
    Returns:
        List of attachments
    """
    params = {
        "start": start,
        "limit": max_results,
        "sort": sort
    }
    
    result = api_request("GET", f"/wiki/api/v2/spaces/{space_id}/attachments", params=params)
    return result


# ============================================================================
# HELPER TOOLS
# ============================================================================

@mcp.tool()
def confluence_get_space_id(space_key: str) -> Dict:
    """
    Get space ID from space key.
    
    Args:
        space_key: The space key (e.g., SYNTH)
        
    Returns:
        Space details including ID
    """
    result = confluence_get_space_by_key(space_key)
    return result


@mcp.tool()
def confluence_list_default_space_pages() -> Dict:
    """
    List pages in the default space (from CONFLUENCE_SPACE_KEY env variable).
    
    Returns:
        List of pages in the default space
    """
    if not SPACE_KEY:
        return {"error": "CONFLUENCE_SPACE_KEY environment variable not set"}
    
    # Get space ID from key
    space_info = confluence_get_space_by_key(SPACE_KEY)
    if "error" in space_info:
        return space_info
        
    space_id = space_info.get("id")
    if not space_id:
        return {"error": "Could not determine space ID"}
    
    return confluence_list_space_pages(space_id)


@mcp.tool()
def confluence_create_page_in_default_space(
    title: str,
    body: str,
    parent_title: str = None
) -> Dict:
    """
    Create a page in the default space (from CONFLUENCE_SPACE_KEY env variable).
    
    Args:
        title: Page title (required)
        body: Page body content in storage format
        parent_title: Parent page title for nested pages (optional)
        
    Returns:
        Created page details
    """
    if not SPACE_KEY:
        return {"error": "CONFLUENCE_SPACE_KEY environment variable not set"}
    
    # Get space ID from key
    space_info = confluence_get_space_by_key(SPACE_KEY)
    if "error" in space_info:
        return space_info
        
    space_id = space_info.get("id")
    if not space_id:
        return {"error": "Could not determine space ID"}
    
    # Get parent ID if specified
    parent_id = None
    if parent_title:
        pages = confluence_list_space_pages(space_id)
        if "results" in pages:
            for page in pages["results"]:
                if page.get("title") == parent_title:
                    parent_id = page.get("id")
                    break
    
    return confluence_create_page(space_id, title, body, parent_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
