#!/usr/bin/env python3
"""
MCP Server for Confluence Cloud REST API
Provides tools for managing pages, spaces, blog posts, comments, labels, attachments, and more.
"""

import os
import json
import base64
from typing import Any, Optional
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("confluence-cloud")

# Configuration from environment variables
CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

# Validate required environment variables
if not all([CONFLUENCE_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
    raise ValueError(
        "Missing required environment variables: "
        "CONFLUENCE_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN"
    )

# Setup authentication
def get_auth_header():
    """Generate Basic Auth header for Confluence API"""
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
    """Make HTTP request to Confluence API"""
    url = f"{CONFLUENCE_BASE_URL}{endpoint}"
    req_headers = get_auth_header()
    req_headers["Accept"] = "application/json"
    if data:
        req_headers["Content-Type"] = "application/json"
    if headers:
        req_headers.update(headers)
    
    try:
        if method == "GET":
            response = requests.get(url, headers=req_headers, params=params, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=req_headers, json=data, params=params, timeout=30)
        elif method == "PUT":
            response = requests.put(url, headers=req_headers, json=data, params=params, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=req_headers, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        # Handle 204 No Content
        if response.status_code == 204:
            return {"success": True, "status_code": 204}
        
        # Handle 302 redirects (for downloads)
        if response.status_code == 302:
            return {"redirect_url": response.headers.get("Location"), "status_code": 302}
        
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return {"error": f"HTTP {response.status_code}", "details": error_data}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
        
        try:
            return response.json()
        except:
            return {"success": True, "status_code": response.status_code}
    
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ============================================================================
# PAGES (v2)
# ============================================================================

@server.tool()
def list_pages(
    space_id: Optional[str] = None,
    max_results: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """List all pages or pages in a specific space"""
    params = {"max_results": max_results}
    if space_id:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/wiki/api/v2/pages", params=params)

@server.tool()
def get_page(page_id: str) -> dict:
    """Get a specific page by ID"""
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}")

@server.tool()
def create_page(
    space_id: str,
    title: str,
    body: str,
    parent_id: Optional[str] = None,
    content_status: str = "current",
) -> dict:
    """Create a new page in a space"""
    data = {
        "spaceId": space_id,
        "title": title,
        "content_status": content_status,
        "body": {
            "representation": "storage",
            "value": body,
        },
    }
    if parent_id:
        data["parentId"] = parent_id
    return make_request("POST", "/wiki/api/v2/pages", data=data)

@server.tool()
def update_page(
    page_id: str,
    title: str,
    body: str,
    version_number: int,
    content_status: str = "current",
) -> dict:
    """Update an existing page"""
    data = {
        "id": page_id,
        "title": title,
        "content_status": content_status,
        "body": {
            "representation": "storage",
            "value": body,
        },
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/pages/{page_id}", data=data)

@server.tool()
def delete_page(page_id: str, purge: bool = False) -> dict:
    """Delete a page"""
    params = {}
    if purge:
        params["purge"] = "true"
    return make_request("DELETE", f"/wiki/api/v2/pages/{page_id}", params=params)

@server.tool()
def get_page_children(page_id: str, max_results: int = 25) -> dict:
    """Get child pages of a specific page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/children", params=params)

@server.tool()
def get_pages_in_space(space_id: str, max_results: int = 25) -> dict:
    """Get all pages in a specific space"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/pages", params=params)


# ============================================================================
# SPACES (v2)
# ============================================================================

@server.tool()
def list_spaces(max_results: int = 25, cursor: Optional[str] = None) -> dict:
    """List all spaces"""
    params = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/wiki/api/v2/spaces", params=params)

@server.tool()
def get_space(space_id: str) -> dict:
    """Get a specific space by ID"""
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}")

@server.tool()
def create_space(
    name: str,
    key: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Create a new space"""
    data = {"name": name}
    if key:
        data["key"] = key
    if description:
        data["description"] = {
            "value": description,
            "representation": "plain",
        }
    return make_request("POST", "/wiki/api/v2/spaces", data=data)


# ============================================================================
# BLOG POSTS (v2)
# ============================================================================

@server.tool()
def list_blog_posts(
    space_id: Optional[str] = None,
    max_results: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """List all blog posts or blog posts in a specific space"""
    params = {"max_results": max_results}
    if space_id:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/wiki/api/v2/blogposts", params=params)

@server.tool()
def get_blog_post(blog_post_id: str) -> dict:
    """Get a specific blog post by ID"""
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}")

@server.tool()
def create_blog_post(
    space_id: str,
    title: str,
    body: str,
    content_status: str = "current",
) -> dict:
    """Create a new blog post"""
    data = {
        "spaceId": space_id,
        "title": title,
        "content_status": content_status,
        "body": {
            "representation": "storage",
            "value": body,
        },
    }
    return make_request("POST", "/wiki/api/v2/blogposts", data=data)

@server.tool()
def update_blog_post(
    blog_post_id: str,
    title: str,
    body: str,
    version_number: int,
    space_id: str,
    content_status: str = "current",
) -> dict:
    """Update an existing blog post"""
    data = {
        "id": blog_post_id,
        "title": title,
        "content_status": content_status,
        "spaceId": space_id,
        "body": {
            "representation": "storage",
            "value": body,
        },
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}", data=data)

@server.tool()
def delete_blog_post(blog_post_id: str, purge: bool = False) -> dict:
    """Delete a blog post"""
    params = {}
    if purge:
        params["purge"] = "true"
    return make_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}", params=params)

@server.tool()
def get_blog_posts_in_space(space_id: str, max_results: int = 25) -> dict:
    """Get all blog posts in a specific space"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/blogposts", params=params)


# ============================================================================
# COMMENTS (v2)
# ============================================================================

@server.tool()
def get_page_footer_comments(page_id: str, max_results: int = 25) -> dict:
    """Get footer comments on a page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/footer-comments", params=params)

@server.tool()
def get_page_inline_comments(page_id: str, max_results: int = 25) -> dict:
    """Get inline comments on a page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/inline-comments", params=params)

@server.tool()
def get_blog_post_footer_comments(blog_post_id: str, max_results: int = 25) -> dict:
    """Get footer comments on a blog post"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/footer-comments", params=params)

@server.tool()
def get_blog_post_inline_comments(blog_post_id: str, max_results: int = 25) -> dict:
    """Get inline comments on a blog post"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/inline-comments", params=params)

@server.tool()
def create_footer_comment(
    body: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
) -> dict:
    """Create a footer comment on a page or blog post"""
    data = {
        "body": {
            "representation": "storage",
            "value": body,
        },
    }
    if page_id:
        data["pageId"] = page_id
    if blog_post_id:
        data["blogPostId"] = blog_post_id
    if parent_comment_id:
        data["parentCommentId"] = parent_comment_id
    return make_request("POST", "/wiki/api/v2/footer-comments", data=data)

@server.tool()
def get_footer_comment(comment_id: str) -> dict:
    """Get a specific footer comment"""
    return make_request("GET", f"/wiki/api/v2/footer-comments/{comment_id}")

@server.tool()
def update_footer_comment(
    comment_id: str,
    body: str,
    version_number: int,
) -> dict:
    """Update a footer comment"""
    data = {
        "body": {
            "representation": "storage",
            "value": body,
        },
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/footer-comments/{comment_id}", data=data)

@server.tool()
def delete_footer_comment(comment_id: str) -> dict:
    """Delete a footer comment"""
    return make_request("DELETE", f"/wiki/api/v2/footer-comments/{comment_id}")

@server.tool()
def create_inline_comment(
    body: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    marker_ref: Optional[str] = None,
) -> dict:
    """Create an inline comment on a page or blog post"""
    data = {
        "body": {
            "representation": "storage",
            "value": body,
        },
    }
    if page_id:
        data["pageId"] = page_id
    if blog_post_id:
        data["blogPostId"] = blog_post_id
    if parent_comment_id:
        data["parentCommentId"] = parent_comment_id
    if marker_ref:
        data["properties"] = {"inlineMarkerRef": marker_ref}
    return make_request("POST", "/wiki/api/v2/inline-comments", data=data)

@server.tool()
def get_inline_comment(comment_id: str) -> dict:
    """Get a specific inline comment"""
    return make_request("GET", f"/wiki/api/v2/inline-comments/{comment_id}")

@server.tool()
def update_inline_comment(
    comment_id: str,
    body: str,
    version_number: int,
) -> dict:
    """Update an inline comment"""
    data = {
        "body": {
            "representation": "storage",
            "value": body,
        },
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/inline-comments/{comment_id}", data=data)

@server.tool()
def delete_inline_comment(comment_id: str) -> dict:
    """Delete an inline comment"""
    return make_request("DELETE", f"/wiki/api/v2/inline-comments/{comment_id}")


# ============================================================================
# LABELS (v2)
# ============================================================================

@server.tool()
def list_labels(max_results: int = 25, cursor: Optional[str] = None) -> dict:
    """List all labels"""
    params = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/wiki/api/v2/labels", params=params)

@server.tool()
def get_page_labels(page_id: str, max_results: int = 25) -> dict:
    """Get labels on a page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/labels", params=params)

@server.tool()
def get_blog_post_labels(blog_post_id: str, max_results: int = 25) -> dict:
    """Get labels on a blog post"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/labels", params=params)

@server.tool()
def get_space_labels(space_id: str, max_results: int = 25) -> dict:
    """Get labels in a space"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/labels", params=params)

@server.tool()
def get_pages_for_label(label_id: str, max_results: int = 25) -> dict:
    """Get pages with a specific label"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/labels/{label_id}/pages", params=params)

@server.tool()
def get_blog_posts_for_label(label_id: str, max_results: int = 25) -> dict:
    """Get blog posts with a specific label"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/labels/{label_id}/blogposts", params=params)


# ============================================================================
# ATTACHMENTS (v2)
# ============================================================================

@server.tool()
def list_attachments(max_results: int = 25, cursor: Optional[str] = None) -> dict:
    """List all attachments"""
    params = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/wiki/api/v2/attachments", params=params)

@server.tool()
def get_attachment(attachment_id: str) -> dict:
    """Get a specific attachment by ID"""
    return make_request("GET", f"/wiki/api/v2/attachments/{attachment_id}")

@server.tool()
def delete_attachment(attachment_id: str, purge: bool = False) -> dict:
    """Delete an attachment"""
    params = {}
    if purge:
        params["purge"] = "true"
    return make_request("DELETE", f"/wiki/api/v2/attachments/{attachment_id}", params=params)

@server.tool()
def get_page_attachments(page_id: str, max_results: int = 25) -> dict:
    """Get attachments on a page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/attachments", params=params)

@server.tool()
def get_blog_post_attachments(blog_post_id: str, max_results: int = 25) -> dict:
    """Get attachments on a blog post"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/attachments", params=params)

@server.tool()
def get_attachment_labels(attachment_id: str, max_results: int = 25) -> dict:
    """Get labels on an attachment"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/labels", params=params)

@server.tool()
def get_attachments_for_label(label_id: str, max_results: int = 25) -> dict:
    """Get attachments with a specific label"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/labels/{label_id}/attachments", params=params)


# ============================================================================
# USERS (v2)
# ============================================================================

@server.tool()
def get_users_by_account_ids(account_ids: list) -> dict:
    """Get user details by account IDs"""
    data = {"accountIds": account_ids}
    return make_request("POST", "/wiki/api/v2/users-bulk", data=data)

@server.tool()
def check_user_access_by_email(emails: list) -> dict:
    """Check which emails don't have access to the site"""
    data = {"emails": emails}
    return make_request("POST", "/wiki/api/v2/user/access/check-access-by-email", data=data)

@server.tool()
def invite_users_by_email(emails: list) -> dict:
    """Invite users to the site by email"""
    data = {"emails": emails}
    return make_request("POST", "/wiki/api/v2/user/access/invite-by-email", data=data)


# ============================================================================
# VERSIONS (v2)
# ============================================================================

@server.tool()
def get_page_versions(page_id: str, max_results: int = 25) -> dict:
    """Get version history of a page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/versions", params=params)

@server.tool()
def get_page_version(page_id: str, version_number: int) -> dict:
    """Get a specific version of a page"""
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/versions/{version_number}")

@server.tool()
def get_blog_post_versions(blog_post_id: str, max_results: int = 25) -> dict:
    """Get version history of a blog post"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/versions", params=params)

@server.tool()
def get_blog_post_version(blog_post_id: str, version_number: int) -> dict:
    """Get a specific version of a blog post"""
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/versions/{version_number}")

@server.tool()
def get_attachment_versions(attachment_id: str, max_results: int = 25) -> dict:
    """Get version history of an attachment"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/versions", params=params)

@server.tool()
def get_attachment_version(attachment_id: str, version_number: int) -> dict:
    """Get a specific version of an attachment"""
    return make_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/versions/{version_number}")


# ============================================================================
# CONTENT PROPERTIES (v2)
# ============================================================================

@server.tool()
def get_page_properties(page_id: str, max_results: int = 25) -> dict:
    """Get content properties on a page"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/properties", params=params)

@server.tool()
def create_page_property(page_id: str, key: str, value: dict) -> dict:
    """Create a content property on a page"""
    data = {
        "key": key,
        "value": value,
    }
    return make_request("POST", f"/wiki/api/v2/pages/{page_id}/properties", data=data)

@server.tool()
def get_page_property(page_id: str, property_id: str) -> dict:
    """Get a specific content property on a page"""
    return make_request("GET", f"/wiki/api/v2/pages/{page_id}/properties/{property_id}")

@server.tool()
def update_page_property(
    page_id: str,
    property_id: str,
    value: dict,
    version_number: int,
) -> dict:
    """Update a content property on a page"""
    data = {
        "value": value,
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/pages/{page_id}/properties/{property_id}", data=data)

@server.tool()
def delete_page_property(page_id: str, property_id: str) -> dict:
    """Delete a content property on a page"""
    return make_request("DELETE", f"/wiki/api/v2/pages/{page_id}/properties/{property_id}")

@server.tool()
def get_blog_post_properties(blog_post_id: str, max_results: int = 25) -> dict:
    """Get content properties on a blog post"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/properties", params=params)

@server.tool()
def create_blog_post_property(blog_post_id: str, key: str, value: dict) -> dict:
    """Create a content property on a blog post"""
    data = {
        "key": key,
        "value": value,
    }
    return make_request("POST", f"/wiki/api/v2/blogposts/{blog_post_id}/properties", data=data)

@server.tool()
def get_blog_post_property(blog_post_id: str, property_id: str) -> dict:
    """Get a specific content property on a blog post"""
    return make_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/properties/{property_id}")

@server.tool()
def update_blog_post_property(
    blog_post_id: str,
    property_id: str,
    value: dict,
    version_number: int,
) -> dict:
    """Update a content property on a blog post"""
    data = {
        "value": value,
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}/properties/{property_id}", data=data)

@server.tool()
def delete_blog_post_property(blog_post_id: str, property_id: str) -> dict:
    """Delete a content property on a blog post"""
    return make_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}/properties/{property_id}")


# ============================================================================
# SEARCH (v1)
# ============================================================================

@server.tool()
def search_content(cql: str, max_results: int = 25, start: int = 0) -> dict:
    """Search content using CQL (Confluence Query Language)"""
    params = {
        "cql": cql,
        "limit": max_results,
        "start": start,
    }
    return make_request("GET", "/wiki/rest/api/search", params=params)

@server.tool()
def search_users(query: str, max_results: int = 25, start: int = 0) -> dict:
    """Search for users"""
    params = {
        "query": query,
        "limit": max_results,
        "start": start,
    }
    return make_request("GET", "/wiki/rest/api/user/search", params=params)


# ============================================================================
# CONTENT (v1) - Additional operations
# ============================================================================

@server.tool()
def get_content_by_id(content_id: str, expand: Optional[str] = None) -> dict:
    """Get content by ID (v1)"""
    params = {}
    if expand:
        params["expand"] = expand
    return make_request("GET", f"/wiki/rest/api/content/{content_id}", params=params)

@server.tool()
def get_content_children(content_id: str, expand: Optional[str] = None) -> dict:
    """Get child content (v1)"""
    params = {}
    if expand:
        params["expand"] = expand
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/child", params=params)

@server.tool()
def get_content_ancestors(content_id: str) -> dict:
    """Get ancestor content (v1)"""
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/ancestor")


# ============================================================================
# SPACE OPERATIONS (v1)
# ============================================================================

@server.tool()
def get_space_by_key(space_key: str) -> dict:
    """Get space by key (v1)"""
    return make_request("GET", f"/wiki/rest/api/space/{space_key}")

@server.tool()
def get_space_content(space_key: str, max_results: int = 25, start: int = 0) -> dict:
    """Get content in a space (v1)"""
    params = {
        "limit": max_results,
        "start": start,
    }
    return make_request("GET", f"/wiki/rest/api/space/{space_key}/content", params=params)


# ============================================================================
# LABELS (v1)
# ============================================================================

@server.tool()
def add_labels_to_content(content_id: str, labels: list) -> dict:
    """Add labels to content (v1)"""
    data = {"labels": [{"name": label} for label in labels]}
    return make_request("POST", f"/wiki/rest/api/content/{content_id}/label", data=data)

@server.tool()
def remove_label_from_content(content_id: str, label_name: str) -> dict:
    """Remove a label from content (v1)"""
    return make_request("DELETE", f"/wiki/rest/api/content/{content_id}/label/{label_name}")

@server.tool()
def get_content_labels(content_id: str, max_results: int = 25, start: int = 0) -> dict:
    """Get labels on content (v1)"""
    params = {
        "limit": max_results,
        "start": start,
    }
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/label", params=params)


# ============================================================================
# RESTRICTIONS (v1)
# ============================================================================

@server.tool()
def get_content_restrictions(content_id: str) -> dict:
    """Get restrictions on content (v1)"""
    return make_request("GET", f"/wiki/rest/api/content/{content_id}/restriction")

@server.tool()
def update_content_restrictions(content_id: str, restrictions: dict) -> dict:
    """Update restrictions on content (v1)"""
    return make_request("PUT", f"/wiki/rest/api/content/{content_id}/restriction", data=restrictions)

@server.tool()
def add_content_restrictions(content_id: str, restrictions: dict) -> dict:
    """Add restrictions to content (v1)"""
    return make_request("POST", f"/wiki/rest/api/content/{content_id}/restriction", data=restrictions)


# ============================================================================
# SYSTEM INFO
# ============================================================================

@server.tool()
def get_system_info() -> dict:
    """Get Confluence system information"""
    return make_request("GET", "/wiki/rest/api/settings/systemInfo")


# ============================================================================
# CUSTOM CONTENT (v2)
# ============================================================================

@server.tool()
def list_custom_content(max_results: int = 25, cursor: Optional[str] = None) -> dict:
    """List all custom content"""
    params = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    return make_request("GET", "/wiki/api/v2/custom-content", params=params)

@server.tool()
def get_custom_content(custom_content_id: str) -> dict:
    """Get a specific custom content by ID"""
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}")

@server.tool()
def create_custom_content(
    space_id: str,
    type_name: str,
    body: str,
    title: Optional[str] = None,
) -> dict:
    """Create custom content"""
    data = {
        "spaceId": space_id,
        "type": type_name,
        "body": {
            "representation": "storage",
            "value": body,
        },
    }
    if title:
        data["title"] = title
    return make_request("POST", "/wiki/api/v2/custom-content", data=data)

@server.tool()
def update_custom_content(
    custom_content_id: str,
    body: str,
    version_number: int,
    title: Optional[str] = None,
) -> dict:
    """Update custom content"""
    data = {
        "id": custom_content_id,
        "body": {
            "representation": "storage",
            "value": body,
        },
        "version": {
            "number": version_number,
        },
    }
    if title:
        data["title"] = title
    return make_request("PUT", f"/wiki/api/v2/custom-content/{custom_content_id}", data=data)

@server.tool()
def delete_custom_content(custom_content_id: str) -> dict:
    """Delete custom content"""
    return make_request("DELETE", f"/wiki/api/v2/custom-content/{custom_content_id}")

@server.tool()
def get_custom_content_labels(custom_content_id: str, max_results: int = 25) -> dict:
    """Get labels on custom content"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/labels", params=params)

@server.tool()
def get_custom_content_attachments(custom_content_id: str, max_results: int = 25) -> dict:
    """Get attachments on custom content"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/attachments", params=params)

@server.tool()
def get_custom_content_properties(custom_content_id: str, max_results: int = 25) -> dict:
    """Get content properties on custom content"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/properties", params=params)

@server.tool()
def create_custom_content_property(custom_content_id: str, key: str, value: dict) -> dict:
    """Create a content property on custom content"""
    data = {
        "key": key,
        "value": value,
    }
    return make_request("POST", f"/wiki/api/v2/custom-content/{custom_content_id}/properties", data=data)

@server.tool()
def get_custom_content_property(custom_content_id: str, property_id: str) -> dict:
    """Get a specific content property on custom content"""
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/properties/{property_id}")

@server.tool()
def update_custom_content_property(
    custom_content_id: str,
    property_id: str,
    value: dict,
    version_number: int,
) -> dict:
    """Update a content property on custom content"""
    data = {
        "value": value,
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/custom-content/{custom_content_id}/properties/{property_id}", data=data)

@server.tool()
def delete_custom_content_property(custom_content_id: str, property_id: str) -> dict:
    """Delete a content property on custom content"""
    return make_request("DELETE", f"/wiki/api/v2/custom-content/{custom_content_id}/properties/{property_id}")

@server.tool()
def get_custom_content_versions(custom_content_id: str, max_results: int = 25) -> dict:
    """Get version history of custom content"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/versions", params=params)

@server.tool()
def get_custom_content_version(custom_content_id: str, version_number: int) -> dict:
    """Get a specific version of custom content"""
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/versions/{version_number}")


# ============================================================================
# SPACE PROPERTIES (v2)
# ============================================================================

@server.tool()
def get_space_properties(space_id: str, max_results: int = 25) -> dict:
    """Get properties on a space"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/properties", params=params)

@server.tool()
def create_space_property(space_id: str, key: str, value: dict) -> dict:
    """Create a property on a space"""
    data = {
        "key": key,
        "value": value,
    }
    return make_request("POST", f"/wiki/api/v2/spaces/{space_id}/properties", data=data)

@server.tool()
def get_space_property(space_id: str, property_id: str) -> dict:
    """Get a specific property on a space"""
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/properties/{property_id}")

@server.tool()
def update_space_property(
    space_id: str,
    property_id: str,
    value: dict,
    version_number: int,
) -> dict:
    """Update a property on a space"""
    data = {
        "value": value,
        "version": {
            "number": version_number,
        },
    }
    return make_request("PUT", f"/wiki/api/v2/spaces/{space_id}/properties/{property_id}", data=data)

@server.tool()
def delete_space_property(space_id: str, property_id: str) -> dict:
    """Delete a property on a space"""
    return make_request("DELETE", f"/wiki/api/v2/spaces/{space_id}/properties/{property_id}")


# ============================================================================
# SPACE PERMISSIONS (v2)
# ============================================================================

@server.tool()
def get_space_permissions(space_id: str, max_results: int = 25) -> dict:
    """Get permissions on a space"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/spaces/{space_id}/permissions", params=params)

@server.tool()
def add_space_permission(
    space_id: str,
    principal_type: str,
    principal_id: str,
    operation: str,
) -> dict:
    """Add a permission to a space"""
    data = {
        "principal": {
            "type": principal_type,
            "id": principal_id,
        },
        "operation": {
            "key": operation,
        },
    }
    return make_request("POST", f"/wiki/api/v2/spaces/{space_id}/permissions", data=data)

@server.tool()
def delete_space_permission(space_id: str, permission_id: str) -> dict:
    """Delete a permission from a space"""
    return make_request("DELETE", f"/wiki/api/v2/spaces/{space_id}/permissions/{permission_id}")


# ============================================================================
# INLINE COMMENTS (v2) - Additional operations
# ============================================================================

@server.tool()
def get_footer_comment_children(comment_id: str, max_results: int = 25) -> dict:
    """Get child comments of a footer comment"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/footer-comments/{comment_id}/children", params=params)

@server.tool()
def get_inline_comment_children(comment_id: str, max_results: int = 25) -> dict:
    """Get child comments of an inline comment"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/inline-comments/{comment_id}/children", params=params)


# ============================================================================
# ATTACHMENT COMMENTS (v2)
# ============================================================================

@server.tool()
def get_attachment_footer_comments(attachment_id: str, max_results: int = 25) -> dict:
    """Get footer comments on an attachment"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/footer-comments", params=params)

@server.tool()
def get_custom_content_footer_comments(custom_content_id: str, max_results: int = 25) -> dict:
    """Get footer comments on custom content"""
    params = {"max_results": max_results}
    return make_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/footer-comments", params=params)


if __name__ == "__main__":
    server.run()
