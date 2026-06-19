#!/usr/bin/env python3
"""
Confluence Cloud MCP Server

An MCP server for working with Confluence Cloud REST API v1 and v2.
"""

import os
import base64
import json
from typing import Any

import requests
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    name="Confluence Cloud",
    version="1.0.0",
    description="MCP Server for Confluence Cloud REST API"
)

# Get configuration from environment
BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://example.atlassian.net/wiki")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "SYNTH")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

# Build authentication header for Basic Auth
if EMAIL and API_TOKEN:
    auth_header = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()
else:
    auth_header = None


def make_request(method: str, endpoint: str, params: dict | None = None, 
                 json_body: dict | None = None) -> dict[str, Any]:
    """
    Make a request to the Confluence REST API.
    
    Returns a dict with either 'result' key on success or 'error' key on failure.
    """
    url = f"{BASE_URL}/rest/api{endpoint}" if endpoint.startswith("/wiki/") else f"{BASE_URL}{endpoint}"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if auth_header:
        headers["Authorization"] = f"Basic {auth_header}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_body,
            headers=headers,
            timeout=30
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return {"result": response.json()}
            except ValueError:
                return {"result": response.text}
        else:
            try:
                error_data = response.json()
                return {"error": f"API error ({response.status_code}): {error_data}"}
            except ValueError:
                return {"error": f"API error ({response.status_code}): {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============== Pages ==============

@mcp.tool()
def create_page(
    title: str,
    content: str,
    space_key: str | None = None,
    parent_id: str | None = None,
    page_type: str = "page",
    body_storage_format: str = "storage"
) -> dict[str, Any]:
    """Create a new page in Confluence.
    
    Args:
        title: Page title
        content: Page content in storage format (HTML)
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY)
        parent_id: Parent page ID for hierarchical pages
        page_type: Type of page ('page' or 'blogpost')
        body_storage_format: Format of content ('storage' or 'view')
    """
    data = {
        "type": page_type,
        "title": title,
        "space": {"key": space_key or SPACE_KEY},
        "body": {
            "storage": {
                "format": body_storage_format,
                "value": content
            }
        }
    }
    
    if parent_id:
        data["ancestors"] = [{"id": parent_id}]
    
    return make_request("POST", "/content", json_body=data)


@mcp.tool()
def get_page(
    page_id: str,
    expand: str | None = None,
    version: int | None = None,
    status: str | None = None
) -> dict[str, Any]:
    """Get a page by ID.
    
    Args:
        page_id: Page ID
        expand: Fields to expand (e.g., 'body.storage,version,space')
        version: Specific version number
        status: Content status ('current', 'draft', 'historical')
    """
    params = {}
    if expand:
        params["expand"] = expand
    if version:
        params["version"] = version
    if status:
        params["status"] = status
    
    return make_request("GET", f"/content/{page_id}", params=params)


@mcp.tool()
def update_page(
    page_id: str,
    title: str,
    content: str,
    version_message: str | None = None,
    minor_edit: bool = False
) -> dict[str, Any]:
    """Update an existing page.
    
    Args:
        page_id: Page ID
        title: New page title
        content: New page content in storage format
        version_message: Version comment
        minor_edit: Whether this is a minor edit
    """
    # First get current page info to get the version
    result = get_page(page_id, expand="version")
    
    if "error" in result:
        return result
    
    page_data = result["result"]
    current_version = page_data["version"]["number"]
    
    data = {
        "id": page_id,
        "type": "page",
        "title": title,
        "version": {
            "number": current_version + 1,
            "minorEdit": minor_edit
        },
        "body": {
            "storage": {
                "format": "storage",
                "value": content
            }
        }
    }
    
    if version_message:
        data["version"]["message"] = version_message
    
    return make_request("PUT", f"/content/{page_id}", json_body=data)


@mcp.tool()
def delete_page(page_id: str) -> dict[str, Any]:
    """Delete a page.
    
    Args:
        page_id: Page ID
    """
    return make_request("DELETE", f"/content/{page_id}")


@mcp.tool()
def get_page_children(
    page_id: str,
    expand: str | None = None,
    limit: int = 25,
    start: int = 0,
    type: str | None = None,
    order: str | None = None
) -> dict[str, Any]:
    """Get children of a page.
    
    Args:
        page_id: Page ID
        expand: Fields to expand
        limit: Maximum results per page
        start: Pagination start
        type: Child type ('page', 'attachment', 'comment')
        order: Order direction ('asc' or 'desc')
    """
    params = {
        "start": start,
        "limit": limit
    }
    if expand:
        params["expand"] = expand
    if type:
        params["type"] = type
    if order:
        params["order"] = order
    
    return make_request("GET", f"/content/{page_id}/child", params=params)


@mcp.tool()
def get_page_ancestors(page_id: str) -> dict[str, Any]:
    """Get ancestor pages of a page.
    
    Args:
        page_id: Page ID
    """
    return make_request("GET", f"/content/{page_id}/ancestors")


@mcp.tool()
def move_page(page_id: str, target_id: str, position: str = "last-child") -> dict[str, Any]:
    """Move a page to a new parent.
    
    Args:
        page_id: Page ID to move
        target_id: Target parent page ID
        position: Position relative to target ('first-child', 'last-child', 'above', 'below')
    """
    data = {
        "contentId": page_id,
        "targetId": target_id,
        "position": position
    }
    
    return make_request("POST", "/content/move", json_body=data)


# ============== Search ==============

@mcp.tool()
def search_cql(
    cql: str,
    expand: str | None = None,
    start: int = 0,
    limit: int = 25,
    sort: str | None = None,
    include_archived_spaces: bool = False
) -> dict[str, Any]:
    """Search content using CQL (Confluence Query Language).
    
    Args:
        cql: CQL query string
        expand: Fields to expand
        start: Pagination start
        limit: Maximum results per page
        sort: Sort order
        include_archived_spaces: Whether to include archived spaces
    """
    params = {
        "cql": cql,
        "start": start,
        "limit": limit,
        "includeArchivedSpaces": str(include_archived_spaces).lower()
    }
    if expand:
        params["expand"] = expand
    if sort:
        params["sort"] = sort
    
    return make_request("GET", "/search", params=params)


# ============== Spaces ==============

@mcp.tool()
def list_spaces(
    type: str | None = None,
    status: str | None = None,
    expand: str | None = None,
    start: int = 0,
    limit: int = 25
) -> dict[str, Any]:
    """List spaces.
    
    Args:
        type: Space type ('global', 'personal')
        status: Space status ('current', 'archived')
        expand: Fields to expand
        start: Pagination start
        limit: Maximum results per page
    """
    params = {
        "start": start,
        "limit": limit
    }
    if type:
        params["type"] = type
    if status:
        params["status"] = status
    if expand:
        params["expand"] = expand
    
    return make_request("GET", "/space", params=params)


@mcp.tool()
def get_space(space_key: str, expand: str | None = None) -> dict[str, Any]:
    """Get a space by key.
    
    Args:
        space_key: Space key
        expand: Fields to expand
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/space/{space_key}", params=params)


@mcp.tool()
def create_space(
    key: str,
    name: str,
    description: str | None = None,
    permission: str | None = None
) -> dict[str, Any]:
    """Create a new space.
    
    Args:
        key: Space key
        name: Space name
        description: Space description
        permission: Permission template name
    """
    data = {
        "key": key,
        "name": name
    }
    
    if description:
        data["description"] = {"plain": {"value": description, "representation": "plain"}}
    
    if permission:
        data["permission"] = {"name": permission}
    
    return make_request("POST", "/space", json_body=data)


@mcp.tool()
def delete_space(space_key: str) -> dict[str, Any]:
    """Delete a space.
    
    Args:
        space_key: Space key
    """
    return make_request("DELETE", f"/space/{space_key}")


# ============== Labels ==============

@mcp.tool()
def add_label(
    content_id: str,
    label: str,
    prefix: str = "global"
) -> dict[str, Any]:
    """Add a label to content.
    
    Args:
        content_id: Content ID (page, blog post, etc.)
        label: Label name
        prefix: Label prefix ('global' or 'system')
    """
    data = {
        "prefix": prefix,
        "name": label
    }
    
    return make_request("POST", f"/content/{content_id}/label", json_body=data)


@mcp.tool()
def list_labels(
    content_id: str,
    start: int = 0,
    limit: int = 25
) -> dict[str, Any]:
    """List labels on content.
    
    Args:
        content_id: Content ID
        start: Pagination start
        limit: Maximum results per page
    """
    params = {
        "start": start,
        "limit": limit
    }
    
    return make_request("GET", f"/content/{content_id}/label", params=params)


@mcp.tool()
def delete_label(
    content_id: str,
    label: str
) -> dict[str, Any]:
    """Delete a label from content.
    
    Args:
        content_id: Content ID
        label: Label name to delete
    """
    # Labels are stored with a prefix, need to find the full label
    # For simplicity, we assume global prefix
    return make_request("DELETE", f"/content/{content_id}/label", params={"name": label})


# ============== Attachments ==============

@mcp.tool()
def list_attachments(
    content_id: str,
    expand: str | None = None,
    filename: str | None = None,
    media_type: str | None = None,
    start: int = 0,
    limit: int = 25
) -> dict[str, Any]:
    """List attachments on content.
    
    Args:
        content_id: Content ID
        expand: Fields to expand
        filename: Filter by filename
        media_type: Filter by media type
        start: Pagination start
        limit: Maximum results per page
    """
    params = {
        "start": start,
        "limit": limit
    }
    if expand:
        params["expand"] = expand
    if filename:
        params["filename"] = filename
    if media_type:
        params["mediaType"] = media_type
    
    return make_request("GET", f"/content/{content_id}/child/attachment", params=params)


@mcp.tool()
def upload_attachment(
    content_id: str,
    file_path: str,
    file_name: str | None = None,
    comment: str | None = None
) -> dict[str, Any]:
    """Upload an attachment to content.
    
    Args:
        content_id: Content ID
        file_path: Local file path
        file_name: Optional filename (defaults to basename of file_path)
        comment: Attachment comment
    """
    if file_name is None:
        file_name = os.path.basename(file_path)
    
    # Read file content
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()
    except Exception as e:
        return {"error": f"Failed to read file: {str(e)}"}
    
    # Determine content type
    content_type = "application/octet-stream"
    if file_name.endswith(".pdf"):
        content_type = "application/pdf"
    elif file_name.endswith((".png", ".jpg", ".jpeg")):
        content_type = "image/jpeg"
    elif file_name.endswith(".gif"):
        content_type = "image/gif"
    elif file_name.endswith(".svg"):
        content_type = "image/svg+xml"
    elif file_name.endswith((".doc", ".docx")):
        content_type = "application/msword"
    elif file_name.endswith(".xls"):
        content_type = "application/vnd.ms-excel"
    
    headers = {
        "Accept": "application/json",
        "X-Atlassian-Token": "no-check"
    }
    if auth_header:
        headers["Authorization"] = f"Basic {auth_header}"
    
    url = f"{BASE_URL}/rest/api/content/{content_id}/child/attachment"
    
    files = {"file": (file_name, file_content, content_type)}
    data = {}
    if comment:
        data["comment"] = comment
    
    try:
        response = requests.post(url, headers=headers, files=files, data=data, timeout=30)
        
        if response.status_code >= 200 and response.status_code < 300:
            return {"result": response.json()}
        else:
            try:
                error_data = response.json()
                return {"error": f"Upload failed ({response.status_code}): {error_data}"}
            except ValueError:
                return {"error": f"Upload failed ({response.status_code}): {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Upload failed: {str(e)}"}


@mcp.tool()
def download_attachment(attachment_id: str) -> dict[str, Any]:
    """Download an attachment.
    
    Args:
        attachment_id: Attachment ID
    """
    headers = {"Accept": "application/octet-stream"}
    if auth_header:
        headers["Authorization"] = f"Basic {auth_header}"
    
    url = f"{BASE_URL}/rest/api/content/{attachment_id}/data"
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code >= 200 and response.status_code < 300:
            # Return as base64 encoded content
            return {
                "result": {
                    "content": base64.b64encode(response.content).decode("utf-8"),
                    "content_type": response.headers.get("content-type", "application/octet-stream"),
                    "size": len(response.content)
                }
            }
        else:
            try:
                error_data = response.json()
                return {"error": f"Download failed ({response.status_code}): {error_data}"}
            except ValueError:
                return {"error": f"Download failed ({response.status_code}): {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Download failed: {str(e)}"}


# ============== Comments ==============

@mcp.tool()
def create_comment(
    content_id: str,
    body: str,
    parent_id: str | None = None,
    body_format: str = "storage"
) -> dict[str, Any]:
    """Create a comment on content (page or blog post).
    
    Args:
        content_id: Content ID (page or blog post)
        body: Comment body in storage format
        parent_id: Parent comment ID for nested comments
        body_format: Format of body ('storage' or 'view')
    """
    data = {
        "type": "comment",
        "container": {"id": content_id, "type": "page"},
        "body": {
            "storage": {
                "format": body_format,
                "value": body
            }
        }
    }
    
    if parent_id:
        data["parent"] = {"id": parent_id}
    
    return make_request("POST", "/content", json_body=data)


@mcp.tool()
def list_comments(
    content_id: str,
    expand: str | None = None,
    start: int = 0,
    limit: int = 25,
    depth: int | None = None
) -> dict[str, Any]:
    """List comments on content.
    
    Args:
        content_id: Content ID
        expand: Fields to expand
        start: Pagination start
        limit: Maximum results per page
        depth: Comment depth limit
    """
    params = {
        "start": start,
        "limit": limit
    }
    if expand:
        params["expand"] = expand
    if depth:
        params["depth"] = depth
    
    return make_request("GET", f"/content/{content_id}/child/comment", params=params)


@mcp.tool()
def get_comment(comment_id: str, expand: str | None = None) -> dict[str, Any]:
    """Get a comment by ID.
    
    Args:
        comment_id: Comment ID
        expand: Fields to expand
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/content/{comment_id}", params=params)


@mcp.tool()
def update_comment(
    comment_id: str,
    body: str,
    version_message: str | None = None,
    minor_edit: bool = False,
    body_format: str = "storage"
) -> dict[str, Any]:
    """Update a comment.
    
    Args:
        comment_id: Comment ID
        body: New comment body
        version_message: Version comment
        minor_edit: Whether this is a minor edit
        body_format: Format of body ('storage' or 'view')
    """
    # Get current comment info
    result = get_comment(comment_id, expand="version")
    
    if "error" in result:
        return result
    
    comment_data = result["result"]
    current_version = comment_data["version"]["number"]
    
    data = {
        "id": comment_id,
        "type": "comment",
        "version": {
            "number": current_version + 1,
            "minorEdit": minor_edit
        },
        "body": {
            "storage": {
                "format": body_format,
                "value": body
            }
        }
    }
    
    if version_message:
        data["version"]["message"] = version_message
    
    return make_request("PUT", f"/content/{comment_id}", json_body=data)


@mcp.tool()
def delete_comment(comment_id: str) -> dict[str, Any]:
    """Delete a comment.
    
    Args:
        comment_id: Comment ID
    """
    return make_request("DELETE", f"/content/{comment_id}")


# ============== Inline Comments ==============

@mcp.tool()
def create_inline_comment(
    content_id: str,
    body: str,
    start: int,
    end: int,
    start_format: str = "text",
    end_format: str = "text"
) -> dict[str, Any]:
    """Create an inline comment on a page.
    
    Args:
        content_id: Content ID
        body: Comment body
        start: Start position
        end: End position
        start_format: Start format ('text' or 'offset')
        end_format: End format ('text' or 'offset')
    """
    data = {
        "type": "comment",
        "container": {"id": content_id, "type": "page"},
        "body": {
            "storage": {
                "format": "storage",
                "value": body
            }
        },
        "metadata": {
            "editor": {
                "version": 2,
                "selection": {
                    "start": start,
                    "end": end,
                    "startFormat": start_format,
                    "endFormat": end_format
                }
            }
        }
    }
    
    return make_request("POST", "/content", json_body=data)


# ============== Versions ==============

@mcp.tool()
def list_versions(
    content_id: str,
    start: int = 0,
    limit: int = 25,
    order_by: str | None = None,
    direction: str = "asc"
) -> dict[str, Any]:
    """List versions of content.
    
    Args:
        content_id: Content ID
        start: Pagination start
        limit: Maximum results per page
        order_by: Sort field
        direction: Sort direction ('asc' or 'desc')
    """
    params = {
        "start": start,
        "limit": limit,
        "direction": direction
    }
    if order_by:
        params["orderBy"] = order_by
    
    return make_request("GET", f"/content/{content_id}/version", params=params)


@mcp.tool()
def get_version(content_id: str, version_number: int) -> dict[str, Any]:
    """Get a specific version of content.
    
    Args:
        content_id: Content ID
        version_number: Version number
    """
    return make_request("GET", f"/content/{content_id}/version/{version_number}")


@mcp.tool()
def restore_version(
    content_id: str,
    version_number: int,
    override_edit: bool = False
) -> dict[str, Any]:
    """Restore content to a previous version.
    
    Args:
        content_id: Content ID
        version_number: Version number to restore
        override_edit: Override current edit lock
    """
    params = {"overrideEditLock": str(override_edit).lower()}
    
    return make_request("POST", f"/content/{content_id}/version/{version_number}/restore", params=params)


# ============== Content Properties ==============

@mcp.tool()
def get_content_property(
    content_id: str,
    property_key: str
) -> dict[str, Any]:
    """Get a property of content.
    
    Args:
        content_id: Content ID
        property_key: Property key
    """
    return make_request("GET", f"/content/{content_id}/property/{property_key}")


@mcp.tool()
def set_content_property(
    content_id: str,
    property_key: str,
    value: dict | list | str | int | float,
    version: int | None = None
) -> dict[str, Any]:
    """Set a property on content.
    
    Args:
        content_id: Content ID
        property_key: Property key
        value: Property value (JSON-serializable)
        version: Optional version number for optimistic locking
    """
    data = {
        "key": property_key,
        "value": value
    }
    
    params = {}
    if version:
        params["version"] = version
    
    return make_request("PUT", f"/content/{content_id}/property", params=params, json_body=data)


@mcp.tool()
def delete_content_property(
    content_id: str,
    property_key: str
) -> dict[str, Any]:
    """Delete a property from content.
    
    Args:
        content_id: Content ID
        property_key: Property key
    """
    return make_request("DELETE", f"/content/{content_id}/property/{property_key}")


# ============== Blog Posts ==============

@mcp.tool()
def create_blog_post(
    title: str,
    content: str,
    space_key: str | None = None,
    category: str | None = None
) -> dict[str, Any]:
    """Create a new blog post.
    
    Args:
        title: Blog post title
        content: Blog post content in storage format
        space_key: Space key (defaults to CONFLUENCE_SPACE_KEY)
        category: Blog post category
    """
    data = {
        "type": "blogpost",
        "title": title,
        "space": {"key": space_key or SPACE_KEY},
        "body": {
            "storage": {
                "format": "storage",
                "value": content
            }
        }
    }
    
    if category:
        data["metadata"] = {"labels": [{"name": category}]}
    
    return make_request("POST", "/content", json_body=data)


@mcp.tool()
def get_blog_post(
    blog_post_id: str,
    expand: str | None = None
) -> dict[str, Any]:
    """Get a blog post by ID.
    
    Args:
        blog_post_id: Blog post ID
        expand: Fields to expand
    """
    params = {}
    if expand:
        params["expand"] = expand
    
    return make_request("GET", f"/content/{blog_post_id}", params=params)


@mcp.tool()
def update_blog_post(
    blog_post_id: str,
    title: str,
    content: str,
    version_message: str | None = None,
    minor_edit: bool = False
) -> dict[str, Any]:
    """Update an existing blog post.
    
    Args:
        blog_post_id: Blog post ID
        title: New blog post title
        content: New blog post content
        version_message: Version comment
        minor_edit: Whether this is a minor edit
    """
    # First get current blog post info
    result = get_blog_post(blog_post_id, expand="version")
    
    if "error" in result:
        return result
    
    post_data = result["result"]
    current_version = post_data["version"]["number"]
    
    data = {
        "id": blog_post_id,
        "type": "blogpost",
        "title": title,
        "version": {
            "number": current_version + 1,
            "minorEdit": minor_edit
        },
        "body": {
            "storage": {
                "format": "storage",
                "value": content
            }
        }
    }
    
    if version_message:
        data["version"]["message"] = version_message
    
    return make_request("PUT", f"/content/{blog_post_id}", json_body=data)


@mcp.tool()
def delete_blog_post(blog_post_id: str) -> dict[str, Any]:
    """Delete a blog post.
    
    Args:
        blog_post_id: Blog post ID
    """
    return make_request("DELETE", f"/content/{blog_post_id}")


# ============== Users ==============

@mcp.tool()
def get_current_user() -> dict[str, Any]:
    """Get the current authenticated user."""
    return make_request("GET", "/user/current")


@mcp.tool()
def get_user_by_account_id(account_id: str) -> dict[str, Any]:
    """Get a user by their account ID.
    
    Args:
        account_id: Atlassian account ID
    """
    return make_request("GET", "/user", params={"accountId": account_id})


@mcp.tool()
def get_user_by_username(username: str) -> dict[str, Any]:
    """Get a user by username.
    
    Args:
        username: Username
    """
    return make_request("GET", "/user", params={"username": username})


# ============== Restrictions ==============

@mcp.tool()
def get_restrictions(content_id: str) -> dict[str, Any]:
    """Get restrictions on content (permissions).
    
    Args:
        content_id: Content ID
    """
    return make_request("GET", f"/content/{content_id}/restriction")


# ============== Templates ==============

@mcp.tool()
def list_templates(
    space_key: str | None = None,
    type: str | None = None,
    start: int = 0,
    limit: int = 25
) -> dict[str, Any]:
    """List content templates.
    
    Args:
        space_key: Space key
        type: Template type ('global', 'personal', 'space')
        start: Pagination start
        limit: Maximum results per page
    """
    params = {
        "start": start,
        "limit": limit
    }
    if space_key:
        params["spaceKey"] = space_key
    if type:
        params["type"] = type
    
    return make_request("GET", "/template", params=params)


if __name__ == "__main__":
    # Run the MCP server over stdio
    mcp.run()
