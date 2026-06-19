#!/usr/bin/env python3
"""
Confluence Cloud REST API MCP Server

This server provides tools for interacting with Confluence Cloud via the REST API.
"""

import os
import base64
import json
import requests
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("confluence")

# Configuration from environment variables
BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://your-site.atlassian.net/wiki")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "SYNTH")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

# Auth header for Basic auth
AUTH_HEADER = None
if EMAIL and API_TOKEN:
    auth_str = f"{EMAIL}:{API_TOKEN}"
    AUTH_HEADER = {
        "Authorization": f"Basic {base64.b64encode(auth_str.encode()).decode()}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }


def make_request(method: str, path: str, params: Optional[dict] = None, 
                 data: Optional[dict] = None, files: Optional[dict] = None) -> dict:
    """Make a request to the Confluence API."""
    url = f"{BASE_URL}{path}"
    headers = dict(AUTH_HEADER) if AUTH_HEADER else {}
    
    if files:
        headers.pop("Content-Type", None)  # Let requests set boundary for multipart
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            files=files,
            headers=headers,
            timeout=60
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except:
                return {"success": True, "content": response.text}
        else:
            return {
                "error": f"API error: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


# ========== SPACE OPERATIONS ==========

@mcp.tool()
def list_spaces(limit: int = 25, start: int = 0) -> dict:
    """
    List all spaces the user has permission to view.
    """
    return make_request(
        "GET",
        "/wiki/rest/api/space",
        params={"limit": limit, "start": start, "expand": "description.plain,homepage"}
    )


@mcp.tool()
def get_space(space_key: str) -> dict:
    """
    Get a space by its key.
    """
    return make_request(
        "GET",
        f"/wiki/rest/api/space/{space_key}",
        params={"expand": "description.plain,homepage"}
    )


@mcp.tool()
def create_space(name: str, key: str, description: str = "") -> dict:
    """
    Create a new space.
    
    Args:
        name: The name of the space
        key: The space key (must be unique, uppercase)
        description: Optional description of the space
    """
    data = {
        "key": key,
        "name": name,
        "_links": {}
    }
    if description:
        data["description"] = {"plain": {"value": description, "representation": "plain"}}
    
    return make_request("POST", "/wiki/rest/api/space", data=data)


@mcp.tool()
def delete_space(space_key: str) -> dict:
    """
    Delete a space.
    """
    return make_request("DELETE", f"/wiki/rest/api/space/{space_key}")


# ========== PAGE OPERATIONS ==========

@mcp.tool()
def create_page(
    space_key: str,
    title: str,
    body: str,
    parent_id: Optional[str] = None,
    page_type: str = "page"
) -> dict:
    """
    Create a new page in a space.
    
    Args:
        space_key: The space key to create the page in
        title: The page title
        body: The page body in storage format (HTML) or plain text
        parent_id: Optional parent page ID for hierarchy
        page_type: Type of content, 'page' or 'blogpost'
    """
    data = {
        "type": page_type,
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
        data["ancestors"] = [{"id": parent_id}]
    
    return make_request("POST", "/wiki/api/v2/pages", data=data)


@mcp.tool()
def get_page(page_id: str, expand: str = "body.storage,version,metadata.labels") -> dict:
    """
    Get a page by its ID.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/pages/{page_id}",
        params={"expand": expand}
    )


@mcp.tool()
def update_page(
    page_id: str,
    title: Optional[str] = None,
    body: Optional[str] = None,
    version_comment: str = ""
) -> dict:
    """
    Update an existing page.
    
    Args:
        page_id: The ID of the page to update
        title: New title (optional)
        body: New body in storage format (optional)
        version_comment: Comment for this version (optional)
    """
    # First get the current page to get the version number
    current = get_page(page_id)
    if "error" in current:
        return current
    
    version = current.get("version", {}).get("number", 1)
    
    data = {
        "id": page_id,
        "version": {"number": version + 1, "comment": version_comment},
        "type": "page"
    }
    
    if title:
        data["title"] = title
    
    if body:
        data["body"] = {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    
    return make_request("PUT", f"/wiki/api/v2/pages/{page_id}", data=data)


@mcp.tool()
def delete_page(page_id: str) -> dict:
    """
    Delete a page.
    """
    return make_request("DELETE", f"/wiki/api/v2/pages/{page_id}")


@mcp.tool()
def get_page_children(
    page_id: str,
    type: str = "page",
    expand: str = "body.storage,version",
    limit: int = 25,
    start: int = 0
) -> dict:
    """
    Get child pages of a page.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/pages/{page_id}/children/{type}",
        params={"expand": expand, "limit": limit, "start": start}
    )


@mcp.tool()
def move_page(page_id: str, target_id: str, position: str = "last-child") -> dict:
    """
    Move a page to a new parent.
    
    Args:
        page_id: The page to move
        target_id: The new parent page ID
        position: "first-child", "last-child", "above", or "below"
    """
    data = {
        "contentId": page_id,
        "destination": {"id": target_id, "type": "page"},
        "position": position
    }
    
    return make_request("POST", "/wiki/api/v2/pages/move", data=data)


@mcp.tool()
def get_page_by_title(
    space_key: str,
    title: str,
    expand: str = "body.storage"
) -> dict:
    """
    Get a page by its title within a space.
    """
    return make_request(
        "GET",
        "/wiki/api/v2/pages",
        params={"spaceKey": space_key, "title": title, "expand": expand}
    )


# ========== BLOG POST OPERATIONS ==========

@mcp.tool()
def create_blog_post(
    space_key: str,
    title: str,
    body: str
) -> dict:
    """
    Create a new blog post.
    """
    data = {
        "type": "blogpost",
        "title": title,
        "space": {"key": space_key},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    }
    
    return make_request("POST", "/wiki/api/v2/pages", data=data)


@mcp.tool()
def get_blog_post(blog_post_id: str) -> dict:
    """
    Get a blog post by its ID.
    """
    return make_request("GET", f"/wiki/api/v2/pages/{blog_post_id}")


@mcp.tool()
def update_blog_post(
    blog_post_id: str,
    title: Optional[str] = None,
    body: Optional[str] = None,
    version_comment: str = ""
) -> dict:
    """
    Update a blog post.
    """
    current = get_page(blog_post_id)
    if "error" in current:
        return current
    
    version = current.get("version", {}).get("number", 1)
    
    data = {
        "id": blog_post_id,
        "version": {"number": version + 1, "comment": version_comment},
        "type": "blogpost"
    }
    
    if title:
        data["title"] = title
    
    if body:
        data["body"] = {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    
    return make_request("PUT", f"/wiki/api/v2/pages/{blog_post_id}", data=data)


@mcp.tool()
def delete_blog_post(blog_post_id: str) -> dict:
    """
    Delete a blog post.
    """
    return make_request("DELETE", f"/wiki/api/v2/pages/{blog_post_id}")


# ========== COMMENT OPERATIONS ==========

@mcp.tool()
def add_comment(
    page_id: str,
    body: str,
    parent_id: Optional[str] = None
) -> dict:
    """
    Add a comment to a page.
    
    Args:
        page_id: The page to comment on
        body: Comment body in storage format
        parent_id: Optional parent comment ID for replies
    """
    data = {
        "content": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        },
        "subject": ""
    }
    
    if parent_id:
        data["parentId"] = parent_id
    
    return make_request("POST", f"/wiki/api/v2/pages/{page_id}/comments", data=data)


@mcp.tool()
def get_comments(
    page_id: str,
    expand: str = "body.storage,author",
    limit: int = 25,
    start: int = 0
) -> dict:
    """
    Get comments on a page.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/pages/{page_id}/comments",
        params={"expand": expand, "limit": limit, "start": start}
    )


@mcp.tool()
def get_inline_comments(
    page_id: str,
    expand: str = "body.storage,author,container"
) -> dict:
    """
    Get inline comments on a page.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/pages/{page_id}/comments/inline",
        params={"expand": expand}
    )


@mcp.tool()
def update_comment(comment_id: str, body: str, version_comment: str = "") -> dict:
    """
    Update a comment.
    """
    # Get current comment to get version
    current = make_request("GET", f"/wiki/api/v2/comments/{comment_id}")
    if "error" in current:
        return current
    
    version = current.get("version", {}).get("number", 1)
    
    data = {
        "id": comment_id,
        "version": {"number": version + 1, "comment": version_comment},
        "content": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        },
        "subject": ""
    }
    
    return make_request("PUT", f"/wiki/api/v2/comments/{comment_id}", data=data)


@mcp.tool()
def delete_comment(comment_id: str) -> dict:
    """
    Delete a comment.
    """
    return make_request("DELETE", f"/wiki/api/v2/comments/{comment_id}")


# ========== ATTACHMENT OPERATIONS ==========

@mcp.tool()
def list_attachments(
    content_id: str,
    expand: str = "file",
    limit: int = 25,
    start: int = 0
) -> dict:
    """
    List attachments on a page or blog post.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/{content_id}/attachments",
        params={"expand": expand, "limit": limit, "start": start}
    )


@mcp.tool()
def upload_attachment(
    content_id: str,
    file_path: str,
    file_name: str,
    file_content: str,
    comment: str = ""
) -> dict:
    """
    Upload an attachment to a page or blog post.
    
    Args:
        content_id: The page or blog post ID
        file_path: Full local path to the file
        file_name: Name for the attachment
        file_content: File content as base64-encoded string
        comment: Optional comment for the attachment
    """
    import base64
    from io import BytesIO
    
    # Decode base64 content
    file_bytes = base64.b64decode(file_content)
    
    files = {
        "file": (file_name, BytesIO(file_bytes)),
        "comment": (None, comment)
    }
    
    return make_request(
        "POST",
        f"/wiki/api/v2/{content_id}/attachments",
        files=files
    )


@mcp.tool()
def download_attachment(attachment_id: str) -> dict:
    """
    Download an attachment.
    Returns the file content as base64.
    """
    url = f"{BASE_URL}/wiki/api/v2/attachments/{attachment_id}/data"
    
    headers = dict(AUTH_HEADER) if AUTH_HEADER else {}
    headers["Accept"] = "*/*"  # Accept any content type
    
    try:
        response = requests.get(url, headers=headers, timeout=60)
        
        if response.status_code >= 200 and response.status_code < 300:
            import base64
            return {
                "success": True,
                "content_type": response.headers.get("content-type", "application/octet-stream"),
                "content_length": len(response.content),
                "content_base64": base64.b64encode(response.content).decode()
            }
        else:
            return {
                "error": f"Download failed: {response.status_code}",
                "status_code": response.status_code,
                "response": response.text
            }
    except Exception as e:
        return {"error": f"Download failed: {str(e)}"}


@mcp.tool()
def delete_attachment(attachment_id: str, version: int = 1) -> dict:
    """
    Delete an attachment.
    """
    return make_request(
        "DELETE",
        f"/wiki/api/v2/attachments/{attachment_id}",
        params={"version": version}
    )


# ========== LABEL OPERATIONS ==========

@mcp.tool()
def add_label(content_id: str, label: str) -> dict:
    """
    Add a label to content.
    """
    data = {
        "prefix": "global",
        "name": label
    }
    
    return make_request("POST", f"/wiki/api/v2/{content_id}/labels", data=data)


@mcp.tool()
def get_labels(content_id: str) -> dict:
    """
    Get all labels on content.
    """
    return make_request("GET", f"/wiki/api/v2/{content_id}/labels")


@mcp.tool()
def delete_label(content_id: str, label_id: str) -> dict:
    """
    Remove a label from content.
    """
    return make_request("DELETE", f"/wiki/api/v2/{content_id}/labels/{label_id}")


# ========== SEARCH OPERATIONS ==========

@mcp.tool()
def search(cql: str, limit: int = 25, start: int = 0, expand: str = "content") -> dict:
    """
    Search content using CQL (Confluence Query Language).
    
    Examples of CQL:
    - "space = SYNTH"
    - "text ~ 'meeting notes'"
    - "type = page"
    - "creator = currentUser()"
    - "label = todo"
    """
    return make_request(
        "GET",
        "/wiki/api/v2/search",
        params={"cql": cql, "limit": limit, "start": start, "expand": expand}
    )


# ========== VERSION OPERATIONS ==========

@mcp.tool()
def get_version(page_id: str, version_id: str) -> dict:
    """
    Get a specific version of a page.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/pages/{page_id}/versions/{version_id}"
    )


@mcp.tool()
def list_versions(page_id: str, limit: int = 25, start: int = 0) -> dict:
    """
    List versions of a page.
    """
    return make_request(
        "GET",
        f"/wiki/api/v2/pages/{page_id}/versions",
        params={"limit": limit, "start": start}
    )


@mcp.tool()
def restore_version(page_id: str, version_id: str) -> dict:
    """
    Restore a page to a specific version.
    """
    data = {"id": version_id}
    
    return make_request(
        "POST",
        f"/wiki/api/v2/pages/{page_id}/restore",
        data=data
    )


# ========== CONTENT PROPERTIES ==========

@mcp.tool()
def get_content_properties(content_id: str) -> dict:
    """
    Get all properties of a content item.
    """
    return make_request("GET", f"/wiki/api/v2/{content_id}/properties")


@mcp.tool()
def set_content_property(
    content_id: str,
    key: str,
    value: dict
) -> dict:
    """
    Set a content property.
    """
    data = {
        "key": key,
        "value": value
    }
    
    return make_request("POST", f"/wiki/api/v2/{content_id}/properties", data=data)


@mcp.tool()
def update_content_property(
    content_id: str,
    key: str,
    version: int,
    value: dict
) -> dict:
    """
    Update a content property.
    """
    data = {
        "key": key,
        "value": value,
        "version": {"number": version}
    }
    
    return make_request("PUT", f"/wiki/api/v2/{content_id}/properties/{key}", data=data)


@mcp.tool()
def delete_content_property(content_id: str, key: str) -> dict:
    """
    Delete a content property.
    """
    return make_request("DELETE", f"/wiki/api/v2/{content_id}/properties/{key}")


# ========== USER OPERATIONS ==========

@mcp.tool()
def get_current_user() -> dict:
    """
    Get the current authenticated user.
    """
    return make_request("GET", "/wiki/api/v2/user")


@mcp.tool()
def get_user_by_account_id(account_id: str) -> dict:
    """
    Get a user by their account ID.
    """
    return make_request(
        "GET",
        "/wiki/api/v2/user",
        params={"accountId": account_id}
    )


# ========== RUN SERVER ==========

if __name__ == "__main__":
    mcp.run()
