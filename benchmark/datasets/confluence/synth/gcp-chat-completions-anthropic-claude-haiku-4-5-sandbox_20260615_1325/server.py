#!/usr/bin/env python3
"""
MCP Server for Confluence Cloud REST API
Provides tools for managing pages, spaces, comments, attachments, labels, and more.
"""

import os
import json
import base64
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("confluence-cloud")

# Configuration from environment variables
CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

# Setup authentication
def get_auth_header():
    """Generate Basic Auth header for Confluence API"""
    credentials = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}

def make_request(method: str, endpoint: str, data: Optional[dict] = None, params: Optional[dict] = None, is_v2: bool = True) -> dict:
    """Make HTTP request to Confluence API"""
    if is_v2:
        url = f"{CONFLUENCE_BASE_URL}/api/v2{endpoint}"
    else:
        url = f"{CONFLUENCE_BASE_URL}/rest/api{endpoint}"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        **get_auth_header()
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data, params=params)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data, params=params)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code in [200, 201]:
            return response.json() if response.text else {"success": True}
        elif response.status_code == 204:
            return {"success": True}
        elif response.status_code == 404:
            return {"error": "Not found"}
        elif response.status_code == 400:
            return {"error": f"Bad request: {response.text}"}
        elif response.status_code == 401:
            return {"error": "Unauthorized - check credentials"}
        else:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# PAGES (v2)
# ============================================================================

@mcp.tool()
def list_pages(space_id: Optional[str] = None, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all pages or pages in a specific space"""
    params = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/pages", params=params)

@mcp.tool()
def get_page(page_id: str) -> dict:
    """Get a specific page by ID"""
    return make_request("GET", f"/pages/{page_id}")

@mcp.tool()
def create_page(space_id: str, title: str, body: str, parent_id: Optional[str] = None, status: str = "current") -> dict:
    """Create a new page"""
    data = {
        "spaceId": space_id,
        "title": title,
        "status": status,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    if parent_id:
        data["parentId"] = parent_id
    return make_request("POST", "/pages", data=data)

@mcp.tool()
def update_page(page_id: str, title: str, body: str, version_number: int, status: str = "current") -> dict:
    """Update an existing page"""
    data = {
        "id": page_id,
        "title": title,
        "status": status,
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/pages/{page_id}", data=data)

@mcp.tool()
def delete_page(page_id: str, purge: bool = False) -> dict:
    """Delete a page"""
    params = {}
    if purge:
        params["purge"] = "true"
    return make_request("DELETE", f"/pages/{page_id}", params=params)

@mcp.tool()
def update_page_title(page_id: str, title: str, status: str = "current") -> dict:
    """Update only the title of a page"""
    data = {
        "title": title,
        "status": status
    }
    return make_request("PUT", f"/pages/{page_id}/title", data=data)

# ============================================================================
# SPACES (v2)
# ============================================================================

@mcp.tool()
def list_spaces(limit: int = 25, cursor: Optional[str] = None, space_type: Optional[str] = None) -> dict:
    """List all spaces"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if space_type:
        params["type"] = space_type
    return make_request("GET", "/spaces", params=params)

@mcp.tool()
def get_space(space_id: str) -> dict:
    """Get a specific space by ID"""
    return make_request("GET", f"/spaces/{space_id}")

@mcp.tool()
def create_space(name: str, key: Optional[str] = None, description: Optional[str] = None) -> dict:
    """Create a new space"""
    data = {"name": name}
    if key:
        data["key"] = key
    if description:
        data["description"] = {
            "value": description,
            "representation": "plain"
        }
    return make_request("POST", "/spaces", data=data)

# ============================================================================
# BLOG POSTS (v2)
# ============================================================================

@mcp.tool()
def list_blog_posts(space_id: Optional[str] = None, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all blog posts or blog posts in a specific space"""
    params = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/blogposts", params=params)

@mcp.tool()
def get_blog_post(blog_post_id: str) -> dict:
    """Get a specific blog post by ID"""
    return make_request("GET", f"/blogposts/{blog_post_id}")

@mcp.tool()
def create_blog_post(space_id: str, title: str, body: str, status: str = "current") -> dict:
    """Create a new blog post"""
    data = {
        "spaceId": space_id,
        "title": title,
        "status": status,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    return make_request("POST", "/blogposts", data=data)

@mcp.tool()
def update_blog_post(blog_post_id: str, title: str, body: str, version_number: int, space_id: str, status: str = "current") -> dict:
    """Update an existing blog post"""
    data = {
        "id": blog_post_id,
        "title": title,
        "status": status,
        "spaceId": space_id,
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/blogposts/{blog_post_id}", data=data)

@mcp.tool()
def delete_blog_post(blog_post_id: str, purge: bool = False) -> dict:
    """Delete a blog post"""
    params = {}
    if purge:
        params["purge"] = "true"
    return make_request("DELETE", f"/blogposts/{blog_post_id}", params=params)

# ============================================================================
# COMMENTS (v2)
# ============================================================================

@mcp.tool()
def list_page_footer_comments(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List footer comments on a page"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/pages/{page_id}/footer-comments", params=params)

@mcp.tool()
def list_page_inline_comments(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List inline comments on a page"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/pages/{page_id}/inline-comments", params=params)

@mcp.tool()
def create_footer_comment(page_id: Optional[str] = None, blog_post_id: Optional[str] = None, body: str = "", parent_comment_id: Optional[str] = None) -> dict:
    """Create a footer comment on a page or blog post"""
    data = {
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    if page_id:
        data["pageId"] = page_id
    elif blog_post_id:
        data["blogPostId"] = blog_post_id
    if parent_comment_id:
        data["parentCommentId"] = parent_comment_id
    return make_request("POST", "/footer-comments", data=data)

@mcp.tool()
def get_footer_comment(comment_id: str) -> dict:
    """Get a specific footer comment"""
    return make_request("GET", f"/footer-comments/{comment_id}")

@mcp.tool()
def update_footer_comment(comment_id: str, body: str, version_number: int) -> dict:
    """Update a footer comment"""
    data = {
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/footer-comments/{comment_id}", data=data)

@mcp.tool()
def delete_footer_comment(comment_id: str) -> dict:
    """Delete a footer comment"""
    return make_request("DELETE", f"/footer-comments/{comment_id}")

# ============================================================================
# ATTACHMENTS (v2)
# ============================================================================

@mcp.tool()
def list_attachments(limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all attachments"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/attachments", params=params)

@mcp.tool()
def get_attachment(attachment_id: str) -> dict:
    """Get a specific attachment by ID"""
    return make_request("GET", f"/attachments/{attachment_id}")

@mcp.tool()
def list_page_attachments(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List attachments on a page"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/pages/{page_id}/attachments", params=params)

@mcp.tool()
def delete_attachment(attachment_id: str, purge: bool = False) -> dict:
    """Delete an attachment"""
    params = {}
    if purge:
        params["purge"] = "true"
    return make_request("DELETE", f"/attachments/{attachment_id}", params=params)

# ============================================================================
# LABELS (v2)
# ============================================================================

@mcp.tool()
def list_labels(limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all labels"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/labels", params=params)

@mcp.tool()
def list_page_labels(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List labels on a page"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/pages/{page_id}/labels", params=params)

@mcp.tool()
def list_space_labels(space_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List labels in a space"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/spaces/{space_id}/labels", params=params)

# ============================================================================
# VERSIONS (v2)
# ============================================================================

@mcp.tool()
def list_page_versions(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List versions of a page"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/pages/{page_id}/versions", params=params)

@mcp.tool()
def get_page_version(page_id: str, version_number: int) -> dict:
    """Get a specific version of a page"""
    return make_request("GET", f"/pages/{page_id}/versions/{version_number}")

@mcp.tool()
def list_blog_post_versions(blog_post_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List versions of a blog post"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/blogposts/{blog_post_id}/versions", params=params)

@mcp.tool()
def get_blog_post_version(blog_post_id: str, version_number: int) -> dict:
    """Get a specific version of a blog post"""
    return make_request("GET", f"/blogposts/{blog_post_id}/versions/{version_number}")

# ============================================================================
# CONTENT PROPERTIES (v2)
# ============================================================================

@mcp.tool()
def list_page_properties(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List properties on a page"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/pages/{page_id}/properties", params=params)

@mcp.tool()
def get_page_property(page_id: str, property_id: str) -> dict:
    """Get a specific property on a page"""
    return make_request("GET", f"/pages/{page_id}/properties/{property_id}")

@mcp.tool()
def create_page_property(page_id: str, key: str, value: Any) -> dict:
    """Create a property on a page"""
    data = {
        "key": key,
        "value": value
    }
    return make_request("POST", f"/pages/{page_id}/properties", data=data)

@mcp.tool()
def update_page_property(page_id: str, property_id: str, key: str, value: Any, version_number: int) -> dict:
    """Update a property on a page"""
    data = {
        "key": key,
        "value": value,
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/pages/{page_id}/properties/{property_id}", data=data)

@mcp.tool()
def delete_page_property(page_id: str, property_id: str) -> dict:
    """Delete a property on a page"""
    return make_request("DELETE", f"/pages/{page_id}/properties/{property_id}")

# ============================================================================
# USERS (v2)
# ============================================================================

@mcp.tool()
def get_users_by_account_ids(account_ids: list) -> dict:
    """Get user details by account IDs"""
    data = {"accountIds": account_ids}
    return make_request("POST", "/users-bulk", data=data)

@mcp.tool()
def check_user_access(emails: list) -> dict:
    """Check which emails don't have access to the site"""
    data = {"emails": emails}
    return make_request("POST", "/user/access/check-access-by-email", data=data)

@mcp.tool()
def invite_users_by_email(emails: list) -> dict:
    """Invite users to the site by email"""
    data = {"emails": emails}
    return make_request("POST", "/user/access/invite-by-email", data=data)

# ============================================================================
# SEARCH (v1)
# ============================================================================

@mcp.tool()
def search_content(cql: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """Search content using Confluence Query Language (CQL)"""
    params = {
        "cql": cql,
        "limit": limit
    }
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/search", params=params, is_v2=False)

@mcp.tool()
def search_users(cql: str, limit: int = 25, start: int = 0) -> dict:
    """Search users using CQL"""
    params = {
        "cql": cql,
        "limit": limit,
        "start": start
    }
    return make_request("GET", "/search/user", params=params, is_v2=False)

# ============================================================================
# SPACE PAGES (v2)
# ============================================================================

@mcp.tool()
def list_space_pages(space_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all pages in a space"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/spaces/{space_id}/pages", params=params)

@mcp.tool()
def list_space_blog_posts(space_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all blog posts in a space"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/spaces/{space_id}/blogposts", params=params)

# ============================================================================
# LABEL CONTENT (v2)
# ============================================================================

@mcp.tool()
def list_label_pages(label_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List pages with a specific label"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/labels/{label_id}/pages", params=params)

@mcp.tool()
def list_label_blog_posts(label_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List blog posts with a specific label"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/labels/{label_id}/blogposts", params=params)

@mcp.tool()
def list_label_attachments(label_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List attachments with a specific label"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/labels/{label_id}/attachments", params=params)

# ============================================================================
# BLOG POST COMMENTS (v2)
# ============================================================================

@mcp.tool()
def list_blog_post_footer_comments(blog_post_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List footer comments on a blog post"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/blogposts/{blog_post_id}/footer-comments", params=params)

@mcp.tool()
def list_blog_post_inline_comments(blog_post_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List inline comments on a blog post"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/blogposts/{blog_post_id}/inline-comments", params=params)

# ============================================================================
# BLOG POST ATTACHMENTS (v2)
# ============================================================================

@mcp.tool()
def list_blog_post_attachments(blog_post_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List attachments on a blog post"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/blogposts/{blog_post_id}/attachments", params=params)

# ============================================================================
# BLOG POST LABELS (v2)
# ============================================================================

@mcp.tool()
def list_blog_post_labels(blog_post_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List labels on a blog post"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/blogposts/{blog_post_id}/labels", params=params)

# ============================================================================
# BLOG POST PROPERTIES (v2)
# ============================================================================

@mcp.tool()
def list_blog_post_properties(blog_post_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List properties on a blog post"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/blogposts/{blog_post_id}/properties", params=params)

@mcp.tool()
def get_blog_post_property(blog_post_id: str, property_id: str) -> dict:
    """Get a specific property on a blog post"""
    return make_request("GET", f"/blogposts/{blog_post_id}/properties/{property_id}")

@mcp.tool()
def create_blog_post_property(blog_post_id: str, key: str, value: Any) -> dict:
    """Create a property on a blog post"""
    data = {
        "key": key,
        "value": value
    }
    return make_request("POST", f"/blogposts/{blog_post_id}/properties", data=data)

@mcp.tool()
def update_blog_post_property(blog_post_id: str, property_id: str, key: str, value: Any, version_number: int) -> dict:
    """Update a property on a blog post"""
    data = {
        "key": key,
        "value": value,
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/blogposts/{blog_post_id}/properties/{property_id}", data=data)

@mcp.tool()
def delete_blog_post_property(blog_post_id: str, property_id: str) -> dict:
    """Delete a property on a blog post"""
    return make_request("DELETE", f"/blogposts/{blog_post_id}/properties/{property_id}")

# ============================================================================
# ATTACHMENT LABELS (v2)
# ============================================================================

@mcp.tool()
def list_attachment_labels(attachment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List labels on an attachment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/attachments/{attachment_id}/labels", params=params)

# ============================================================================
# ATTACHMENT PROPERTIES (v2)
# ============================================================================

@mcp.tool()
def list_attachment_properties(attachment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List properties on an attachment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/attachments/{attachment_id}/properties", params=params)

@mcp.tool()
def get_attachment_property(attachment_id: str, property_id: str) -> dict:
    """Get a specific property on an attachment"""
    return make_request("GET", f"/attachments/{attachment_id}/properties/{property_id}")

@mcp.tool()
def create_attachment_property(attachment_id: str, key: str, value: Any) -> dict:
    """Create a property on an attachment"""
    data = {
        "key": key,
        "value": value
    }
    return make_request("POST", f"/attachments/{attachment_id}/properties", data=data)

@mcp.tool()
def update_attachment_property(attachment_id: str, property_id: str, key: str, value: Any, version_number: int) -> dict:
    """Update a property on an attachment"""
    data = {
        "key": key,
        "value": value,
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/attachments/{attachment_id}/properties/{property_id}", data=data)

@mcp.tool()
def delete_attachment_property(attachment_id: str, property_id: str) -> dict:
    """Delete a property on an attachment"""
    return make_request("DELETE", f"/attachments/{attachment_id}/properties/{property_id}")

# ============================================================================
# ATTACHMENT VERSIONS (v2)
# ============================================================================

@mcp.tool()
def list_attachment_versions(attachment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List versions of an attachment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/attachments/{attachment_id}/versions", params=params)

@mcp.tool()
def get_attachment_version(attachment_id: str, version_number: int) -> dict:
    """Get a specific version of an attachment"""
    return make_request("GET", f"/attachments/{attachment_id}/versions/{version_number}")

# ============================================================================
# ATTACHMENT COMMENTS (v2)
# ============================================================================

@mcp.tool()
def list_attachment_footer_comments(attachment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List footer comments on an attachment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/attachments/{attachment_id}/footer-comments", params=params)

# ============================================================================
# FOOTER COMMENTS (v2)
# ============================================================================

@mcp.tool()
def list_all_footer_comments(limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all footer comments"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/footer-comments", params=params)

@mcp.tool()
def list_footer_comment_children(comment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List child comments of a footer comment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/footer-comments/{comment_id}/children", params=params)

@mcp.tool()
def list_footer_comment_versions(comment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List versions of a footer comment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/footer-comments/{comment_id}/versions", params=params)

@mcp.tool()
def get_footer_comment_version(comment_id: str, version_number: int) -> dict:
    """Get a specific version of a footer comment"""
    return make_request("GET", f"/footer-comments/{comment_id}/versions/{version_number}")

# ============================================================================
# INLINE COMMENTS (v2)
# ============================================================================

@mcp.tool()
def list_all_inline_comments(limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List all inline comments"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/inline-comments", params=params)

@mcp.tool()
def create_inline_comment(page_id: Optional[str] = None, blog_post_id: Optional[str] = None, body: str = "", parent_comment_id: Optional[str] = None) -> dict:
    """Create an inline comment on a page or blog post"""
    data = {
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    if page_id:
        data["pageId"] = page_id
    elif blog_post_id:
        data["blogPostId"] = blog_post_id
    if parent_comment_id:
        data["parentCommentId"] = parent_comment_id
    return make_request("POST", "/inline-comments", data=data)

@mcp.tool()
def get_inline_comment(comment_id: str) -> dict:
    """Get a specific inline comment"""
    return make_request("GET", f"/inline-comments/{comment_id}")

@mcp.tool()
def update_inline_comment(comment_id: str, body: str, version_number: int) -> dict:
    """Update an inline comment"""
    data = {
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    return make_request("PUT", f"/inline-comments/{comment_id}", data=data)

@mcp.tool()
def delete_inline_comment(comment_id: str) -> dict:
    """Delete an inline comment"""
    return make_request("DELETE", f"/inline-comments/{comment_id}")

@mcp.tool()
def list_inline_comment_children(comment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List child comments of an inline comment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/inline-comments/{comment_id}/children", params=params)

@mcp.tool()
def list_inline_comment_versions(comment_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List versions of an inline comment"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/inline-comments/{comment_id}/versions", params=params)

@mcp.tool()
def get_inline_comment_version(comment_id: str, version_number: int) -> dict:
    """Get a specific version of an inline comment"""
    return make_request("GET", f"/inline-comments/{comment_id}/versions/{version_number}")

# ============================================================================
# SPACE LABELS (v2)
# ============================================================================

@mcp.tool()
def list_space_content_labels(space_id: str, limit: int = 25, cursor: Optional[str] = None) -> dict:
    """List labels used in space content"""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", f"/spaces/{space_id}/content/labels", params=params)

if __name__ == "__main__":
    mcp.run()
