#!/usr/bin/env python3
"""Confluence Cloud MCP Server"""

import os
import json
import requests
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("confluence")

# Get base URL from environment
BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://your-site.atlassian.net/wiki")

# Authentication credentials
EMAIL = os.environ.get("JIRA_EMAIL")
API_TOKEN = os.environ.get("JIRA_API_TOKEN")

def get_auth():
    """Return HTTP Basic auth tuple"""
    return (EMAIL, API_TOKEN)

def api_request(method, path, params=None, data=None, headers=None):
    """Make an API request to Confluence Cloud"""
    url = f"{BASE_URL}{path}"
    
    default_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if headers:
        default_headers.update(headers)
    
    try:
        response = requests.request(
            method=method,
            url=url,
            auth=get_auth(),
            params=params,
            json=data,
            headers=default_headers,
            timeout=60
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            if response.status_code == 204:
                return {"status": "success"}
            return response.json()
        else:
            return {"error": f"API request failed: {response.status_code} - {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================
# Spaces (v2)
# ============================================

@mcp.tool()
def list_spaces(limit: int = 50, cursor: str = None) -> dict:
    """
    List all spaces accessible to the current user.
    Returns a paginated list of spaces with their details.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", "/wiki/api/v2/spaces", params=params)

@mcp.tool()
def get_space(space_id: int) -> dict:
    """
    Get a specific space by its ID.
    """
    return api_request("GET", f"/wiki/api/v2/spaces/{space_id}")

@mcp.tool()
def create_space(name: str, key: str = None, description: str = None, type: str = "global") -> dict:
    """
    Create a new space.
    """
    data = {"name": name}
    if key:
        data["key"] = key
    if description:
        data["description"] = {"value": description, "representation": "plain"}
    if type:
        data["type"] = type
    return api_request("POST", "/wiki/api/v2/spaces", data=data)

# ============================================
# Pages (v2)
# ============================================

@mcp.tool()
def list_pages(space_id: int = None, limit: int = 25, cursor: str = None) -> dict:
    """
    List all pages accessible to the current user.
    Optionally filter by space ID.
    """
    params = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", "/wiki/api/v2/pages", params=params)

@mcp.tool()
def get_page(page_id: int) -> dict:
    """
    Get a specific page by its ID.
    """
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}")

@mcp.tool()
def create_page(space_id: int, title: str, body: str, parent_id: int = None) -> dict:
    """
    Create a new page in a space.
    """
    data = {
        "spaceId": str(space_id),
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    if parent_id:
        data["parentId"] = str(parent_id)
    return api_request("POST", "/wiki/api/v2/pages", data=data)

@mcp.tool()
def update_page(page_id: int, title: str, body: str, version_number: int, version_message: str = None) -> dict:
    """
    Update an existing page.
    """
    data = {
        "id": str(page_id),
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    if version_message:
        data["version"]["message"] = version_message
    return api_request("PUT", f"/wiki/api/v2/pages/{page_id}", data=data)

@mcp.tool()
def delete_page(page_id: int, purge: bool = False, draft: bool = False) -> dict:
    """
    Delete a page. By default, moves to trash.
    Use purge=True to permanently delete, or draft=True to delete a draft.
    """
    params = {}
    if purge:
        params["purge"] = "true"
    if draft:
        params["draft"] = "true"
    return api_request("DELETE", f"/wiki/api/v2/pages/{page_id}", params=params)

@mcp.tool()
def update_page_title(page_id: int, title: str, status: str = "current") -> dict:
    """
    Update only the title of a page.
    """
    data = {
        "status": status,
        "title": title
    }
    return api_request("PUT", f"/wiki/api/v2/pages/{page_id}/title", data=data)

# ============================================
# Search (v1)
# ============================================

@mcp.tool()
def search_confluence(cql: str, limit: int = 25, start: int = 0) -> dict:
    """
    Search Confluence content using CQL (Confluence Query Language).
    Example: cql="type=page space=SYNTH"
    """
    params = {
        "cql": cql,
        "limit": limit,
        "start": start
    }
    return api_request("GET", "/wiki/rest/api/search", params=params)

# ============================================
# Labels (v2)
# ============================================

@mcp.tool()
def list_labels_for_page(page_id: int, limit: int = 25, cursor: str = None) -> dict:
    """
    List labels on a page.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/labels", params=params)

@mcp.tool()
def add_labels_to_page(page_id: int, labels: list) -> dict:
    """
    Add labels to a page.
    labels: list of dicts with 'prefix' and 'name' keys
    """
    data = {"labels": labels}
    return api_request("POST", f"/wiki/api/v2/pages/{page_id}/labels", data=data)

@mcp.tool()
def remove_label_from_page(page_id: int, label_id: int) -> dict:
    """
    Remove a label from a page by label ID.
    """
    return api_request("DELETE", f"/wiki/api/v2/pages/{page_id}/labels/{label_id}")

# ============================================
# Attachments (v2)
# ============================================

@mcp.tool()
def list_attachments_for_page(page_id: int, limit: int = 25, cursor: str = None) -> dict:
    """
    List attachments for a page.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/attachments", params=params)

@mcp.tool()
def get_attachment(attachment_id: str) -> dict:
    """
    Get a specific attachment by ID.
    """
    return api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}")

@mcp.tool()
def delete_attachment(attachment_id: int, purge: bool = False) -> dict:
    """
    Delete an attachment. By default, moves to trash.
    Use purge=True to permanently delete.
    """
    params = {}
    if purge:
        params["purge"] = "true"
    return api_request("DELETE", f"/wiki/api/v2/attachments/{attachment_id}", params=params)

# ============================================
# Comments (v2)
# ============================================

@mcp.tool()
def list_footer_comments_for_page(page_id: int, limit: int = 25, cursor: str = None) -> dict:
    """
    List footer comments for a page.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/footer-comments", params=params)

@mcp.tool()
def create_footer_comment(page_id: int, body: str) -> dict:
    """
    Create a footer comment on a page.
    """
    data = {
        "pageId": str(page_id),
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    return api_request("POST", "/wiki/api/v2/footer-comments", data=data)

@mcp.tool()
def list_inline_comments_for_page(page_id: int, limit: int = 25, cursor: str = None) -> dict:
    """
    List inline comments for a page.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/inline-comments", params=params)

# ============================================
# Versions (v2)
# ============================================

@mcp.tool()
def list_page_versions(page_id: int, limit: int = 25, cursor: str = None) -> dict:
    """
    List versions of a page.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/versions", params=params)

@mcp.tool()
def get_page_version(page_id: int, version_number: int) -> dict:
    """
    Get a specific version of a page.
    """
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/versions/{version_number}")

# ============================================
# Blog Posts (v2)
# ============================================

@mcp.tool()
def list_blog_posts(space_id: int = None, limit: int = 25, cursor: str = None) -> dict:
    """
    List blog posts accessible to the current user.
    Optionally filter by space ID.
    """
    params = {"limit": limit}
    if space_id:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return api_request("GET", "/wiki/api/v2/blogposts", params=params)

@mcp.tool()
def get_blog_post(blog_post_id: int) -> dict:
    """
    Get a specific blog post by ID.
    """
    return api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}")

@mcp.tool()
def create_blog_post(space_id: int, title: str, body: str) -> dict:
    """
    Create a new blog post in a space.
    """
    data = {
        "spaceId": str(space_id),
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        }
    }
    return api_request("POST", "/wiki/api/v2/blogposts", data=data)

@mcp.tool()
def update_blog_post(blog_post_id: int, title: str, body: str, version_number: int, version_message: str = None) -> dict:
    """
    Update an existing blog post.
    """
    data = {
        "id": str(blog_post_id),
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body
        },
        "version": {
            "number": version_number
        }
    }
    if version_message:
        data["version"]["message"] = version_message
    return api_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}", data=data)

@mcp.tool()
def delete_blog_post(blog_post_id: int, purge: bool = False, draft: bool = False) -> dict:
    """
    Delete a blog post. By default, moves to trash.
    Use purge=True to permanently delete, or draft=True to delete a draft.
    """
    params = {}
    if purge:
        params["purge"] = "true"
    if draft:
        params["draft"] = "true"
    return api_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}", params=params)

# ============================================
# Users (v2)
# ============================================

@mcp.tool()
def get_user_by_account_id(account_id: str) -> dict:
    """
    Get user details by account ID.
    """
    return api_request("GET", f"/wiki/api/v2/users?accountId={account_id}")

@mcp.tool()
def get_current_user() -> dict:
    """
    Get details of the current authenticated user.
    """
    return api_request("GET", "/wiki/api/v2/users/current")

# ============================================
# Content Properties (v2)
# ============================================

@mcp.tool()
def get_content_properties(content_id: int, key: str = None) -> dict:
    """
    Get properties for a content item (page, blog post, etc.).
    Optionally filter by property key.
    """
    params = {}
    if key:
        params["key"] = key
    return api_request("GET", f"/wiki/api/v2/pages/{content_id}/properties", params=params)

@mcp.tool()
def set_content_property(content_id: int, key: str, value: dict) -> dict:
    """
    Set a property on a content item.
    """
    data = {
        "key": key,
        "value": value
    }
    return api_request("POST", f"/wiki/api/v2/pages/{content_id}/properties", data=data)

# ============================================
# Ancestors (v2)
# ============================================

@mcp.tool()
def get_page_ancestors(page_id: int) -> dict:
    """
    Get the ancestors of a page.
    """
    return api_request("GET", f"/wiki/api/v2/pages/{page_id}/ancestors")

# ============================================
# Space Operations (v1)
# ============================================

@mcp.tool()
def list_all_spaces_v1(limit: int = 25, start: int = 0) -> dict:
    """
    List all spaces (v1 API).
    """
    params = {
        "limit": limit,
        "start": start
    }
    return api_request("GET", "/wiki/rest/api/space", params=params)

@mcp.tool()
def get_space_by_key_v1(space_key: str) -> dict:
    """
    Get a space by its key (v1 API).
    """
    return api_request("GET", f"/wiki/rest/api/space/{space_key}")

# ============================================
# Content Operations (v1)
# ============================================

@mcp.tool()
def get_content_by_id_v1(content_id: int, expand: str = None) -> dict:
    """
    Get content by ID (v1 API).
    """
    params = {}
    if expand:
        params["expand"] = expand
    return api_request("GET", f"/wiki/rest/api/content/{content_id}", params=params)

@mcp.tool()
def create_content_v1(type: str, title: str, body: str, space_key: str, parent_id: int = None) -> dict:
    """
    Create content (v1 API).
    type: 'page' or 'blogpost'
    """
    data = {
        "type": type,
        "title": title,
        "space": {"key": space_key},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    }
    if parent_id:
        data["ancestors"] = [{"id": str(parent_id)}]
    return api_request("POST", "/wiki/rest/api/content", data=data)

@mcp.tool()
def update_content_v1(content_id: int, title: str, body: str, version_number: int, version_message: str = None) -> dict:
    """
    Update content (v1 API).
    """
    data = {
        "id": content_id,
        "type": "page",
        "title": title,
        "version": {"number": version_number},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    }
    if version_message:
        data["version"]["message"] = version_message
    return api_request("PUT", f"/wiki/rest/api/content/{content_id}", data=data)

@mcp.tool()
def delete_content_v1(content_id: int, status: str = "current") -> dict:
    """
    Delete content (v1 API).
    """
    params = {"status": status}
    return api_request("DELETE", f"/wiki/rest/api/content/{content_id}", params=params)

# ============================================
# Labels (v1)
# ============================================

@mcp.tool()
def add_label_v1(content_id: int, label_name: str, label_prefix: str = "system") -> dict:
    """
    Add a label to content (v1 API).
    """
    data = [
        {
            "prefix": label_prefix,
            "name": label_name
        }
    ]
    return api_request("POST", f"/wiki/rest/api/content/{content_id}/label", data=data)

@mcp.tool()
def remove_label_v1(content_id: int, label_name: str) -> dict:
    """
    Remove a label from content (v1 API).
    """
    params = {"name": label_name}
    return api_request("DELETE", f"/wiki/rest/api/content/{content_id}/label", params=params)

# ============================================
# Attachments (v1)
# ============================================

@mcp.tool()
def upload_attachment_v1(content_id: int, file_path: str, file_name: str = None, comment: str = None) -> dict:
    """
    Upload an attachment to content (v1 API).
    file_path: local path to the file
    """
    # Read file content
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    
    # Determine filename
    filename = file_name or os.path.basename(file_path)
    
    # Build request
    url = f"{BASE_URL}/wiki/rest/api/content/{content_id}/child/attachment"
    headers = {
        "Accept": "application/json",
        "X-Atlassian-Token": "no-check"
    }
    
    files = {'file': (filename, file_content)}
    data = {}
    if comment:
        data["comment"] = comment
    
    try:
        response = requests.post(
            url=url,
            auth=get_auth(),
            headers=headers,
            files=files,
            data=data,
            timeout=120
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            return {"error": f"Upload failed: {response.status_code} - {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Upload failed: {str(e)}"}

@mcp.tool()
def list_attachments_v1(content_id: int, limit: int = 25, start: int = 0) -> dict:
    """
    List attachments for content (v1 API).
    """
    params = {
        "limit": limit,
        "start": start
    }
    return api_request("GET", f"/wiki/rest/api/content/{content_id}/child/attachment", params=params)

# ============================================
# Comments (v1)
# ============================================

@mcp.tool()
def add_comment_v1(content_id: int, body: str) -> dict:
    """
    Add a comment to content (v1 API).
    """
    data = {
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    }
    return api_request("POST", f"/wiki/rest/api/content/{content_id}/child/comment", data=data)

@mcp.tool()
def list_comments_v1(content_id: int, limit: int = 25, start: int = 0) -> dict:
    """
    List comments for content (v1 API).
    """
    params = {
        "limit": limit,
        "start": start
    }
    return api_request("GET", f"/wiki/rest/api/content/{content_id}/child/comment", params=params)

# ============================================
# Versions (v1)
# ============================================

@mcp.tool()
def restore_version_v1(content_id: int, version_number: int, message: str = None) -> dict:
    """
    Restore a previous version of content (v1 API).
    """
    data = {
        "operationKey": "restore",
        "params": {
            "versionNumber": version_number,
            "restoreTitle": True
        }
    }
    if message:
        data["params"]["message"] = message
    return api_request("POST", f"/wiki/rest/api/content/{content_id}/version", data=data)

# ============================================
# Main entry point
# ============================================

if __name__ == "__main__":
    mcp.run()
