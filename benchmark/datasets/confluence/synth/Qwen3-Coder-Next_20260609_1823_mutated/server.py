"""Confluence Cloud MCP Server

This server provides comprehensive coverage of the Confluence Cloud REST API,
suitable for use by an autonomous agent completing real-world tasks.

Authentication: Uses HTTP Basic auth with:
- Username: JIRA_EMAIL
- Password: JIRA_API_TOKEN

Environment Variables:
- CONFLUENCE_BASE_URL: Base URL including /wiki (e.g. https://yoursite.atlassian.net/wiki)
- CONFLUENCE_SPACE_KEY: Default space key for operations
- JIRA_EMAIL: Atlassian account email
- JIRA_API_TOKEN: Atlassian API token
"""

import os
import json
import requests
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

# Initialize MCP server
mcp = FastMCP(
    name="Confluence Cloud",
    version="1.0.0",
    description="MCP server for Confluence Cloud REST API"
)

# Setup logging
logger = get_logger(__name__)

# Environment configuration
CONFLUENCE_BASE_URL = os.environ.get("CONFLUENCE_BASE_URL")
CONFLUENCE_SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

# Authentication setup
AUTH = (JIRA_EMAIL, JIRA_API_TOKEN) if JIRA_EMAIL and JIRA_API_TOKEN else None

# Base URL for API calls
BASE_URL = CONFLUENCE_BASE_URL.rstrip('/') if CONFLUENCE_BASE_URL else None


def _api_request(method: str, path: str, params: dict = None, data: dict = None, timeout: int = 60):
    """Make an authenticated API request to Confluence Cloud."""
    if not BASE_URL:
        return {"error": "CONFLUENCE_BASE_URL environment variable is not set"}
    
    if not AUTH:
        return {"error": "JIRA_EMAIL and JIRA_API_TOKEN environment variables are required"}
    
    url = f"{BASE_URL}{path}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            auth=AUTH,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            timeout=timeout
        )
        
        response.raise_for_status()
        
        # Try to parse JSON response
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"raw_response": response.text}
            
    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP {e.response.status_code}: {e.response.text}"
        return {"error": error_msg}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


# ============================================================================
# SPACE OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def list_spaces(
    ids: list[int] = None,
    keys: list[str] = None,
    type: str = None,
    content_status: str = None,
    labels: list[str] = None,
    favorited_by: str = None,
    not_favorited_by: str = None,
    sort: str = None,
    description_format: str = None,
    include_icon: bool = None,
    max_results: int = 25,
    cursor: str = None
) -> dict:
    """List all spaces.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    Only spaces that the user has permission to view will be returned.
    
    Returns spaces sorted by id ascending.
    """
    params = {
        "max_results": max_results
    }
    if ids:
        params["ids"] = ids
    if keys:
        params["keys"] = keys
    if type:
        params["type"] = type
    if content_status:
        params["content_status"] = content_status
    if labels:
        params["labels"] = labels
    if favorited_by:
        params["favorited-by"] = favorited_by
    if not_favorited_by:
        params["not-favorited-by"] = not_favorited_by
    if sort:
        params["sort"] = sort
    if description_format:
        params["description-format"] = description_format
    if include_icon is not None:
        params["include-icon"] = include_icon
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", "/wiki/api/v2/spaces", params=params)


@mcp.tool()
def get_space(space_id: int, description_format: str = None, include_icon: bool = None,
              include_operations: bool = None, include_properties: bool = None,
              include_permissions: bool = None, include_role_assignments: bool = None,
              include_labels: bool = None) -> dict:
    """Get a specific space by ID.
    
    Permissions required: Permission to view the space.
    """
    params = {}
    if description_format:
        params["description-format"] = description_format
    if include_icon is not None:
        params["include-icon"] = include_icon
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_permissions is not None:
        params["include-permissions"] = include_permissions
    if include_role_assignments is not None:
        params["include-role-assignments"] = include_role_assignments
    if include_labels is not None:
        params["include-labels"] = include_labels
    
    return _api_request("GET", f"/wiki/api/v2/spaces/{space_id}", params=params)


@mcp.tool()
def create_space(name: str, key: str = None, alias: str = None, description: dict = None,
                 role_assignments: list = None, copy_space_access_configuration: int = None,
                 create_private_space: bool = None, template_key: str = None) -> dict:
    """Create a new space.
    
    Available on tenants with Role-Based Access Control.
    
    Permissions required: Permission to create spaces.
    """
    data = {"name": name}
    if key:
        data["key"] = key
    if alias:
        data["alias"] = alias
    if description:
        data["description"] = description
    if role_assignments:
        data["roleAssignments"] = role_assignments
    if copy_space_access_configuration:
        data["copySpaceAccessConfiguration"] = copy_space_access_configuration
    if create_private_space is not None:
        data["createPrivateSpace"] = create_private_space
    if template_key:
        data["templateKey"] = template_key
    
    return _api_request("POST", "/wiki/api/v2/spaces", data=data)


# ============================================================================
# PAGE OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def create_page(space_id: str, title: str = None, content_status: str = "current",
                parent_id: str = None, body: dict = None, subtype: str = None,
                embedded: bool = None, private: bool = None, root_level: bool = None) -> dict:
    """Create a new page.
    
    Pages are created as published by default unless specified as a draft.
    If creating a published page, the title must be specified.
    
    Permissions required: Permission to view the corresponding space. Permission to create a page in the space.
    """
    data = {
        "spaceId": space_id,
        "content_status": content_status
    }
    if title:
        data["title"] = title
    if parent_id:
        data["parentId"] = parent_id
    if body:
        data["body"] = body
    if subtype:
        data["subtype"] = subtype
    
    params = {}
    if embedded is not None:
        params["embedded"] = embedded
    if private is not None:
        params["private"] = private
    if root_level is not None:
        params["root-level"] = root_level
    
    return _api_request("POST", "/wiki/api/v2/pages", params=params, data=data)


@mcp.tool()
def get_page(page_id: int, body_format: str = None, get_draft: bool = None,
             content_status: list[str] = None, version: int = None,
             include_labels: bool = None, include_properties: bool = None,
             include_operations: bool = None, include_likes: bool = None,
             include_versions: bool = None) -> dict:
    """Get a specific page by ID.
    
    Permissions required: Permission to view the page and its corresponding space.
    """
    params = {}
    if body_format:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = get_draft
    if content_status:
        params["content_status"] = content_status
    if version:
        params["version"] = version
    if include_labels is not None:
        params["include-labels"] = include_labels
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_likes is not None:
        params["include-likes"] = include_likes
    if include_versions is not None:
        params["include-versions"] = include_versions
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}", params=params)


@mcp.tool()
def update_page(page_id: int, content_status: str, title: str, space_id: str = None,
                parent_id: str = None, owner_id: str = None, body: dict = None,
                version: dict = None) -> dict:
    """Update a page by ID.
    
    When the "current" version is updated, the provided body content is considered as the latest version.
    
    Permissions required: Permission to view the page and its corresponding space. Permission to update pages in the space.
    """
    data = {
        "id": str(page_id),
        "content_status": content_status,
        "title": title
    }
    if space_id:
        data["spaceId"] = space_id
    if parent_id:
        data["parentId"] = parent_id
    if owner_id:
        data["ownerId"] = owner_id
    if body:
        data["body"] = body
    if version:
        data["version"] = version
    
    return _api_request("PUT", f"/wiki/api/v2/pages/{page_id}", data=data)


@mcp.tool()
def delete_page(page_id: int, purge: bool = None, draft: bool = None) -> dict:
    """Delete a page by ID.
    
    By default this will delete pages that are non-drafts.
    To delete a page that is a draft, set draft=true.
    To permanently delete (purge) a trashed page, set purge=true.
    
    Permissions required: Permission to view the page and its corresponding space. 
    Permission to delete pages in the space. Permission to administer the space (if purging).
    """
    params = {}
    if purge is not None:
        params["purge"] = purge
    if draft is not None:
        params["draft"] = draft
    
    return _api_request("DELETE", f"/wiki/api/v2/pages/{page_id}", params=params)


@mcp.tool()
def update_page_title(page_id: int, content_status: str, title: str) -> dict:
    """Update the title of a page.
    
    Permissions required: Permission to view the page and its corresponding space. 
    Permission to update pages in the space.
    """
    data = {
        "content_status": content_status,
        "title": title
    }
    
    return _api_request("PUT", f"/wiki/api/v2/pages/{page_id}/title", data=data)


@mcp.tool()
def get_pages_for_label(label_id: int, space_id: list[int] = None, body_format: str = None,
                        sort: str = None, cursor: str = None, max_results: int = 25) -> dict:
    """Get pages for a specific label.
    
    Permissions required: Permission to view the content of the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if space_id:
        params["space-id"] = space_id
    if body_format:
        params["body-format"] = body_format
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/labels/{label_id}/pages", params=params)


@mcp.tool()
def get_pages(space_id: list[int] = None, sort: str = None, content_status: list[str] = None,
              title: str = None, body_format: str = None, subtype: str = None,
              cursor: str = None, max_results: int = 25) -> dict:
    """Get all pages with optional filtering.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    Only pages that the user has permission to view will be returned.
    """
    params = {
        "max_results": max_results
    }
    if space_id:
        params["space-id"] = space_id
    if sort:
        params["sort"] = sort
    if content_status:
        params["content_status"] = content_status
    if title:
        params["title"] = title
    if body_format:
        params["body-format"] = body_format
    if subtype:
        params["subtype"] = subtype
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", "/wiki/api/v2/pages", params=params)


@mcp.tool()
def get_pages_for_space(space_id: int, sort: str = None, content_status: list[str] = None,
                        title: str = None, body_format: str = None,
                        cursor: str = None, max_results: int = 25) -> dict:
    """Get all pages in a specific space.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission) 
    and view the space.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if content_status:
        params["content_status"] = content_status
    if title:
        params["title"] = title
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/spaces/{space_id}/pages", params=params)


# ============================================================================
# BLOG POST OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def create_blog_post(space_id: str, title: str, content_status: str = "current",
                     body: dict = None, created_at: str = None, private: bool = None) -> dict:
    """Create a new blog post.
    
    By default this will create the blog post as a non-draft.
    If creating a non-draft, the title must not be empty.
    Currently only supports the storage representation.
    
    Permissions required: Permission to view the corresponding space.
    """
    data = {
        "spaceId": space_id,
        "content_status": content_status,
        "title": title
    }
    if body:
        data["body"] = body
    if created_at:
        data["createdAt"] = created_at
    
    params = {}
    if private is not None:
        params["private"] = private
    
    return _api_request("POST", "/wiki/api/v2/blogposts", params=params, data=data)


@mcp.tool()
def get_blog_post(blog_post_id: int, body_format: str = None, get_draft: bool = None,
                  content_status: list[str] = None, version: int = None,
                  include_labels: bool = None, include_properties: bool = None,
                  include_operations: bool = None, include_likes: bool = None,
                  include_versions: bool = None) -> dict:
    """Get a specific blog post by ID.
    
    Permissions required: Permission to view the blog post and its corresponding space.
    """
    params = {}
    if body_format:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = get_draft
    if content_status:
        params["content_status"] = content_status
    if version:
        params["version"] = version
    if include_labels is not None:
        params["include-labels"] = include_labels
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_likes is not None:
        params["include-likes"] = include_likes
    if include_versions is not None:
        params["include-versions"] = include_versions
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}", params=params)


@mcp.tool()
def update_blog_post(blog_post_id: int, content_status: str, title: str, space_id: str,
                     body: dict = None, version: dict = None, created_at: str = None) -> dict:
    """Update a blog post by ID.
    
    Permissions required: Permission to view the blog post and its corresponding space. 
    Permission to update blog posts in the space.
    """
    data = {
        "id": str(blog_post_id),
        "content_status": content_status,
        "title": title,
        "spaceId": space_id
    }
    if body:
        data["body"] = body
    if version:
        data["version"] = version
    if created_at:
        data["createdAt"] = created_at
    
    return _api_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}", data=data)


@mcp.tool()
def delete_blog_post(blog_post_id: int, purge: bool = None, draft: bool = None) -> dict:
    """Delete a blog post by ID.
    
    By default this will delete blog posts that are non-drafts.
    To delete a draft blog post, set draft=true.
    To permanently delete (purge) a trashed blog post, set purge=true.
    
    Permissions required: Permission to view the blog post and its corresponding space. 
    Permission to delete blog posts in the space. Permission to administer the space (if purging).
    """
    params = {}
    if purge is not None:
        params["purge"] = purge
    if draft is not None:
        params["draft"] = draft
    
    return _api_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}", params=params)


@mcp.tool()
def get_blog_posts_for_label(label_id: int, space_id: list[int] = None, body_format: str = None,
                             sort: str = None, cursor: str = None, max_results: int = 25) -> dict:
    """Get blog posts for a specific label.
    
    Permissions required: Permission to view the content of the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if space_id:
        params["space-id"] = space_id
    if body_format:
        params["body-format"] = body_format
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/labels/{label_id}/blogposts", params=params)


@mcp.tool()
def get_blog_posts(space_id: list[int] = None, sort: str = None, content_status: list[str] = None,
                   title: str = None, body_format: str = None,
                   cursor: str = None, max_results: int = 25) -> dict:
    """Get all blog posts with optional filtering.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    Only blog posts that the user has permission to view will be returned.
    """
    params = {
        "max_results": max_results
    }
    if space_id:
        params["space-id"] = space_id
    if sort:
        params["sort"] = sort
    if content_status:
        params["content_status"] = content_status
    if title:
        params["title"] = title
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", "/wiki/api/v2/blogposts", params=params)


@mcp.tool()
def get_blog_posts_for_space(space_id: int, sort: str = None, content_status: list[str] = None,
                             title: str = None, body_format: str = None,
                             cursor: str = None, max_results: int = 25) -> dict:
    """Get all blog posts in a specific space.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission) 
    and view the space.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if content_status:
        params["content_status"] = content_status
    if title:
        params["title"] = title
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/spaces/{space_id}/blogposts", params=params)


# ============================================================================
# ATTACHMENT OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def get_attachments(sort: str = None, cursor: str = None, content_status: list[str] = None,
                    media_type: str = None, filename: str = None, max_results: int = 25) -> dict:
    """Get all attachments with optional filtering.
    
    Permissions required: Permission to view the container of the attachment.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    if content_status:
        params["content_status"] = content_status
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    
    return _api_request("GET", "/wiki/api/v2/attachments", params=params)


@mcp.tool()
def get_attachment(attachment_id: str, version: int = None, include_labels: bool = None,
                   include_properties: bool = None, include_operations: bool = None,
                   include_versions: bool = None) -> dict:
    """Get a specific attachment by ID.
    
    Permissions required: Permission to view the attachment's container.
    """
    params = {}
    if version:
        params["version"] = version
    if include_labels is not None:
        params["include-labels"] = include_labels
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_versions is not None:
        params["include-versions"] = include_versions
    
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}", params=params)


@mcp.tool()
def delete_attachment(attachment_id: str, purge: bool = None) -> dict:
    """Delete an attachment by ID.
    
    Deleting an attachment moves it to the trash. To permanently delete (purge) a trashed attachment, set purge=true.
    
    Permissions required: Permission to view the container of the attachment. 
    Permission to delete attachments in the space. Permission to administer the space (if purging).
    """
    params = {}
    if purge is not None:
        params["purge"] = purge
    
    return _api_request("DELETE", f"/wiki/api/v2/attachments/{attachment_id}", params=params)


@mcp.tool()
def get_attachments_for_page(page_id: int, sort: str = None, cursor: str = None,
                             content_status: list[str] = None, media_type: str = None,
                             filename: str = None, max_results: int = 25) -> dict:
    """Get attachments for a specific page.
    
    Permissions required: Permission to view the content of the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    if content_status:
        params["content_status"] = content_status
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/attachments", params=params)


@mcp.tool()
def get_attachments_for_blog_post(blog_post_id: int, sort: str = None, cursor: str = None,
                                  content_status: list[str] = None, media_type: str = None,
                                  filename: str = None, max_results: int = 25) -> dict:
    """Get attachments for a specific blog post.
    
    Permissions required: Permission to view the content of the blog post and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    if content_status:
        params["content_status"] = content_status
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/attachments", params=params)


@mcp.tool()
def get_attachments_for_label(label_id: int, sort: str = None, cursor: str = None,
                              max_results: int = 25) -> dict:
    """Get attachments for a specific label.
    
    Permissions required: Permission to view the attachment and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/labels/{label_id}/attachments", params=params)


@mcp.tool()
def get_attachments_for_custom_content(custom_content_id: int, sort: str = None, cursor: str = None,
                                        content_status: list[str] = None, media_type: str = None,
                                        filename: str = None, max_results: int = 25) -> dict:
    """Get attachments for custom content.
    
    Permissions required: Permission to view the content of the custom content and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    if content_status:
        params["content_status"] = content_status
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    
    return _api_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/attachments", params=params)


# ============================================================================
# COMMENT OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def get_footer_comments_for_page(page_id: int, body_format: str = None, content_status: list[str] = None,
                                  sort: str = None, cursor: str = None, max_results: int = 25) -> dict:
    """Get footer comments for a specific page.
    
    Permissions required: Permission to view the content of the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if content_status:
        params["content_status"] = content_status
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/footer-comments", params=params)


@mcp.tool()
def get_inline_comments_for_page(page_id: int, body_format: str = None, content_status: list[str] = None,
                                  resolution_status: list[str] = None, sort: str = None,
                                  cursor: str = None, max_results: int = 25) -> dict:
    """Get inline comments for a specific page.
    
    Permissions required: Permission to view the content of the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if content_status:
        params["content_status"] = content_status
    if resolution_status:
        params["resolution-content_status"] = resolution_status
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/inline-comments", params=params)


@mcp.tool()
def get_footer_comments_for_blog_post(blog_post_id: int, body_format: str = None,
                                       content_status: list[str] = None, sort: str = None,
                                       cursor: str = None, max_results: int = 25) -> dict:
    """Get footer comments for a specific blog post.
    
    Permissions required: Permission to view the content of the blog post and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if content_status:
        params["content_status"] = content_status
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/footer-comments", params=params)


@mcp.tool()
def get_inline_comments_for_blog_post(blog_post_id: int, body_format: str = None,
                                       content_status: list[str] = None,
                                       resolution_status: list[str] = None, sort: str = None,
                                       cursor: str = None, max_results: int = 25) -> dict:
    """Get inline comments for a specific blog post.
    
    Permissions required: Permission to view the content of the blog post and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if content_status:
        params["content_status"] = content_status
    if resolution_status:
        params["resolution-content_status"] = resolution_status
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/inline-comments", params=params)


@mcp.tool()
def get_attachment_comments(attachment_id: str, body_format: str = None, cursor: str = None,
                            sort: str = None, version: int = None, max_results: int = 25) -> dict:
    """Get comments for a specific attachment.
    
    Permissions required: Permission to view the attachment and its corresponding containers.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    if version:
        params["version"] = version
    
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/footer-comments", params=params)


@mcp.tool()
def get_custom_content_comments(custom_content_id: int, body_format: str = None, cursor: str = None,
                                 sort: str = None, max_results: int = 25) -> dict:
    """Get comments for custom content.
    
    Permissions required: Permission to view the custom content and its corresponding containers.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    
    return _api_request("GET", f"/wiki/api/v2/custom-content/{custom_content_id}/footer-comments", params=params)


@mcp.tool()
def create_footer_comment(page_id: int = None, blog_post_id: int = None, attachment_id: str = None,
                          custom_content_id: int = None, parent_comment_id: int = None,
                          body: dict = None, content_status: str = "current") -> dict:
    """Create a footer comment.
    
    Can be created at the top level (specifying pageId or blogPostId) or as a reply (specifying parentCommentId).
    
    Permissions required: Permission to view the content and its corresponding space. 
    Permission to create comments in the space.
    """
    data = {"content_status": content_status}
    if page_id:
        data["pageId"] = page_id
    if blog_post_id:
        data["blogPostId"] = blog_post_id
    if attachment_id:
        data["attachmentId"] = attachment_id
    if custom_content_id:
        data["customContentId"] = custom_content_id
    if parent_comment_id:
        data["parentCommentId"] = parent_comment_id
    if body:
        data["body"] = body
    
    return _api_request("POST", "/wiki/api/v2/footer-comments", data=data)


@mcp.tool()
def update_footer_comment(comment_id: int, content_status: str, title: str, body: dict = None,
                          version: dict = None) -> dict:
    """Update a footer comment by ID.
    
    Permissions required: Permission to view the content and its corresponding space. 
    Permission to update comments in the space.
    """
    data = {
        "content_status": content_status,
        "title": title
    }
    if body:
        data["body"] = body
    if version:
        data["version"] = version
    
    return _api_request("PUT", f"/wiki/api/v2/footer-comments/{comment_id}", data=data)


@mcp.tool()
def delete_footer_comment(comment_id: int) -> dict:
    """Delete a footer comment by ID.
    
    Permissions required: Permission to view the content and its corresponding space. 
    Permission to delete comments in the space.
    """
    return _api_request("DELETE", f"/wiki/api/v2/footer-comments/{comment_id}")


@mcp.tool()
def create_inline_comment(page_id: int = None, blog_post_id: int = None, body: dict = None,
                          content_status: str = "open", resolution_status: str = "open") -> dict:
    """Create an inline comment.
    
    Permissions required: Permission to view the content and its corresponding space. 
    Permission to create comments in the space.
    """
    data = {
        "content_status": content_status,
        "resolutionStatus": resolution_status
    }
    if page_id:
        data["pageId"] = page_id
    if blog_post_id:
        data["blogPostId"] = blog_post_id
    if body:
        data["body"] = body
    
    return _api_request("POST", "/wiki/api/v2/inline-comments", data=data)


@mcp.tool()
def update_inline_comment(comment_id: int, content_status: str, title: str, body: dict = None,
                          resolution_status: str = None, version: dict = None) -> dict:
    """Update an inline comment by ID.
    
    Permissions required: Permission to view the content and its corresponding space. 
    Permission to update comments in the space.
    """
    data = {
        "content_status": content_status,
        "title": title
    }
    if body:
        data["body"] = body
    if resolution_status:
        data["resolutionStatus"] = resolution_status
    if version:
        data["version"] = version
    
    return _api_request("PUT", f"/wiki/api/v2/inline-comments/{comment_id}", data=data)


@mcp.tool()
def delete_inline_comment(comment_id: int) -> dict:
    """Delete an inline comment by ID.
    
    Permissions required: Permission to view the content and its corresponding space. 
    Permission to delete comments in the space.
    """
    return _api_request("DELETE", f"/wiki/api/v2/inline-comments/{comment_id}")


# ============================================================================
# VERSION OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def get_page_versions(page_id: int, body_format: str = None, cursor: str = None,
                      sort: str = None, max_results: int = 25) -> dict:
    """Get versions for a specific page.
    
    Permissions required: Permission to view the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/versions", params=params)


@mcp.tool()
def get_page_version_details(page_id: int, version_number: int) -> dict:
    """Get version details for a specific page version.
    
    Permissions required: Permission to view the page.
    """
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/versions/{version_number}")


@mcp.tool()
def get_blog_post_versions(blog_post_id: int, body_format: str = None, cursor: str = None,
                            sort: str = None, max_results: int = 25) -> dict:
    """Get versions for a specific blog post.
    
    Permissions required: Permission to view the blog post and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if body_format:
        params["body-format"] = body_format
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/versions", params=params)


@mcp.tool()
def get_blog_post_version_details(blog_post_id: int, version_number: int) -> dict:
    """Get version details for a specific blog post version.
    
    Permissions required: Permission to view the blog post.
    """
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/versions/{version_number}")


@mcp.tool()
def get_attachment_versions(attachment_id: str, cursor: str = None, sort: str = None,
                            max_results: int = 25) -> dict:
    """Get versions for a specific attachment.
    
    Permissions required: Permission to view the attachment and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/versions", params=params)


@mcp.tool()
def get_attachment_version_details(attachment_id: str, version_number: int) -> dict:
    """Get version details for a specific attachment version.
    
    Permissions required: Permission to view the attachment.
    """
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/versions/{version_number}")


# ============================================================================
# CONTENT PROPERTIES OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def get_page_properties(page_id: int, key: str = None, sort: str = None,
                        cursor: str = None, max_results: int = 25) -> dict:
    """Get content properties for a page.
    
    Permissions required: Permission to view the page.
    """
    params = {
        "max_results": max_results
    }
    if key:
        params["key"] = key
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/properties", params=params)


@mcp.tool()
def create_page_property(page_id: int, key: str, value: any) -> dict:
    """Create a content property for a page.
    
    Permissions required: Permission to update the page.
    """
    data = {"key": key}
    if value is not None:
        data["value"] = value
    
    return _api_request("POST", f"/wiki/api/v2/pages/{page_id}/properties", data=data)


@mcp.tool()
def get_page_property_by_id(page_id: int, property_id: int) -> dict:
    """Get a specific content property for a page by ID.
    
    Permissions required: Permission to view the page.
    """
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def update_page_property(page_id: int, property_id: int, key: str, value: any,
                          version: dict = None) -> dict:
    """Update a content property for a page by ID.
    
    Permissions required: Permission to edit the page.
    """
    data = {"key": key}
    if value is not None:
        data["value"] = value
    if version:
        data["version"] = version
    
    return _api_request("PUT", f"/wiki/api/v2/pages/{page_id}/properties/{property_id}", data=data)


@mcp.tool()
def delete_page_property(page_id: int, property_id: int) -> dict:
    """Delete a content property for a page by ID.
    
    Permissions required: Permission to edit the page.
    """
    return _api_request("DELETE", f"/wiki/api/v2/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def get_blog_post_properties(blog_post_id: int, key: str = None, sort: str = None,
                              cursor: str = None, max_results: int = 25) -> dict:
    """Get content properties for a blog post.
    
    Permissions required: Permission to view the blog post.
    """
    params = {
        "max_results": max_results
    }
    if key:
        params["key"] = key
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/properties", params=params)


@mcp.tool()
def create_blog_post_property(blog_post_id: int, key: str, value: any) -> dict:
    """Create a content property for a blog post.
    
    Permissions required: Permission to update the blog post.
    """
    data = {"key": key}
    if value is not None:
        data["value"] = value
    
    return _api_request("POST", f"/wiki/api/v2/blogposts/{blog_post_id}/properties", data=data)


@mcp.tool()
def get_blog_post_property_by_id(blog_post_id: int, property_id: int) -> dict:
    """Get a specific content property for a blog post by ID.
    
    Permissions required: Permission to view the blog post.
    """
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/properties/{property_id}")


@mcp.tool()
def update_blog_post_property(blog_post_id: int, property_id: int, key: str, value: any,
                               version: dict = None) -> dict:
    """Update a content property for a blog post by ID.
    
    Permissions required: Permission to edit the blog post.
    """
    data = {"key": key}
    if value is not None:
        data["value"] = value
    if version:
        data["version"] = version
    
    return _api_request("PUT", f"/wiki/api/v2/blogposts/{blog_post_id}/properties/{property_id}", data=data)


@mcp.tool()
def delete_blog_post_property(blog_post_id: int, property_id: int) -> dict:
    """Delete a content property for a blog post by ID.
    
    Permissions required: Permission to edit the blog post.
    """
    return _api_request("DELETE", f"/wiki/api/v2/blogposts/{blog_post_id}/properties/{property_id}")


@mcp.tool()
def get_attachment_properties(attachment_id: str, key: str = None, sort: str = None,
                               cursor: str = None, max_results: int = 25) -> dict:
    """Get content properties for an attachment.
    
    Permissions required: Permission to view the attachment.
    """
    params = {
        "max_results": max_results
    }
    if key:
        params["key"] = key
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/properties", params=params)


@mcp.tool()
def create_attachment_property(attachment_id: str, key: str, value: any) -> dict:
    """Create a content property for an attachment.
    
    Permissions required: Permission to update the attachment.
    """
    data = {"key": key}
    if value is not None:
        data["value"] = value
    
    return _api_request("POST", f"/wiki/api/v2/attachments/{attachment_id}/properties", data=data)


@mcp.tool()
def get_attachment_property_by_id(attachment_id: str, property_id: int) -> dict:
    """Get a specific content property for an attachment by ID.
    
    Permissions required: Permission to view the attachment.
    """
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/properties/{property_id}")


@mcp.tool()
def update_attachment_property(attachment_id: str, property_id: int, key: str, value: any,
                                version: dict = None) -> dict:
    """Update a content property for an attachment by ID.
    
    Permissions required: Permission to edit the attachment.
    """
    data = {"key": key}
    if value is not None:
        data["value"] = value
    if version:
        data["version"] = version
    
    return _api_request("PUT", f"/wiki/api/v2/attachments/{attachment_id}/properties/{property_id}", data=data)


@mcp.tool()
def delete_attachment_property(attachment_id: str, property_id: int) -> dict:
    """Delete a content property for an attachment by ID.
    
    Permissions required: Permission to edit the attachment.
    """
    return _api_request("DELETE", f"/wiki/api/v2/attachments/{attachment_id}/properties/{property_id}")


# ============================================================================
# LABEL OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def get_labels_for_page(page_id: int, prefix: str = None, sort: str = None,
                        cursor: str = None, max_results: int = 25) -> dict:
    """Get labels for a specific page.
    
    Permissions required: Permission to view the content of the page and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if prefix:
        params["prefix"] = prefix
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/pages/{page_id}/labels", params=params)


@mcp.tool()
def get_labels_for_blog_post(blog_post_id: int, prefix: str = None, sort: str = None,
                              cursor: str = None, max_results: int = 25) -> dict:
    """Get labels for a specific blog post.
    
    Permissions required: Permission to view the content of the blog post and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if prefix:
        params["prefix"] = prefix
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/blogposts/{blog_post_id}/labels", params=params)


@mcp.tool()
def get_labels_for_attachment(attachment_id: int, prefix: str = None, sort: str = None,
                               cursor: str = None, max_results: int = 25) -> dict:
    """Get labels for a specific attachment.
    
    Permissions required: Permission to view the parent content of the attachment and its corresponding space.
    """
    params = {
        "max_results": max_results
    }
    if prefix:
        params["prefix"] = prefix
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/attachments/{attachment_id}/labels", params=params)


@mcp.tool()
def get_labels_for_space(space_id: int, prefix: str = None, sort: str = None,
                          cursor: str = None, max_results: int = 25) -> dict:
    """Get labels for a specific space.
    
    Permissions required: Permission to view the space.
    """
    params = {
        "max_results": max_results
    }
    if prefix:
        params["prefix"] = prefix
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/spaces/{space_id}/labels", params=params)


@mcp.tool()
def get_labels_for_space_content(space_id: int, prefix: str = None, sort: str = None,
                                  cursor: str = None, max_results: int = 25) -> dict:
    """Get labels for space content (pages, blogposts, etc).
    
    Permissions required: Permission to view the space.
    """
    params = {
        "max_results": max_results
    }
    if prefix:
        params["prefix"] = prefix
    if sort:
        params["sort"] = sort
    if cursor:
        params["cursor"] = cursor
    
    return _api_request("GET", f"/wiki/api/v2/spaces/{space_id}/content/labels", params=params)


@mcp.tool()
def get_labels(prefix: list[str] = None, label_id: list[int] = None, cursor: str = None,
               sort: str = None, max_results: int = 25) -> dict:
    """Get all labels.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    """
    params = {
        "max_results": max_results
    }
    if prefix:
        params["prefix"] = prefix
    if label_id:
        params["label-id"] = label_id
    if cursor:
        params["cursor"] = cursor
    if sort:
        params["sort"] = sort
    
    return _api_request("GET", "/wiki/api/v2/labels", params=params)


# ============================================================================
# USER OPERATIONS (v1)
# ============================================================================

@mcp.tool()
def get_current_user(include: list[str] = None) -> dict:
    """Get the currently logged-in user.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    """
    params = {}
    if include:
        params["include"] = include
    
    return _api_request("GET", "/wiki/rest/api/user/current", params=params)


@mcp.tool()
def get_user(account_id: str, include: list[str] = None) -> dict:
    """Get a specific user by account ID.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    """
    params = {"accountId": account_id}
    if include:
        params["include"] = include
    
    return _api_request("GET", "/wiki/rest/api/user", params=params)


@mcp.tool()
def get_anonymous_user(include: list[str] = None) -> dict:
    """Get information about how anonymous users are represented.
    
    Permissions required: Permission to access the Confluence site ('Can use' global permission).
    """
    params = {}
    if include:
        params["include"] = include
    
    return _api_request("GET", "/wiki/rest/api/user/anonymous", params=params)


# ============================================================================
# SEARCH OPERATIONS (v1)
# ============================================================================

@mcp.tool()
def search_content(query: str, cqlcontext: str = None, cursor: str = None, next: bool = None,
                   prev: bool = None, max_results: int = 25, offset: int = 0,
                   include_archived_spaces: bool = None, exclude_current_spaces: bool = None,
                   excerpt: str = None) -> dict:
    """Search for content using Confluence Query Language (CQL).
    
    Permissions required: Permission to view the entities.
    Note: Only entities that the user has permission to view will be returned.
    """
    params = {
        "query": query,
        "max_results": max_results
    }
    if cqlcontext:
        params["cqlcontext"] = cqlcontext
    if cursor:
        params["cursor"] = cursor
    if next is not None:
        params["next"] = next
    if prev is not None:
        params["prev"] = prev
    if offset:
        params["offset"] = offset
    if include_archived_spaces is not None:
        params["includeArchivedSpaces"] = include_archived_spaces
    if exclude_current_spaces is not None:
        params["excludeCurrentSpaces"] = exclude_current_spaces
    if excerpt:
        params["excerpt"] = excerpt
    
    return _api_request("GET", "/wiki/rest/api/search", params=params)


@mcp.tool()
def search_users(query: str, offset: int = 0, max_results: int = 25, include: list[str] = None,
                 site_permission_type_filter: str = None) -> dict:
    """Search for users using user-specific queries from CQL.
    
    Note: This endpoint only supports user-specific fields like user, user.fullname, user.accountid, and user.userkey.
    """
    params = {
        "query": query,
        "max_results": max_results
    }
    if offset:
        params["offset"] = offset
    if include:
        params["include"] = include
    if site_permission_type_filter:
        params["sitePermissionTypeFilter"] = site_permission_type_filter
    
    return _api_request("GET", "/wiki/rest/api/search/user", params=params)


# ============================================================================
# SPACE OPERATIONS (v1 - additional)
# ============================================================================

@mcp.tool()
def create_space_v1(name: str, key: str = None, alias: str = None, description: dict = None,
                    permissions: list = None) -> dict:
    """Create a new space (v1 API).
    
    Currently you cannot set space labels when creating a space.
    
    Permissions required: 'Create Space(s)' global permission.
    """
    data = {"name": name}
    if key:
        data["key"] = key
    if alias:
        data["alias"] = alias
    if description:
        data["description"] = description
    if permissions:
        data["permissions"] = permissions
    
    return _api_request("POST", "/wiki/rest/api/space", data=data)


@mcp.tool()
def update_space(space_key: str, name: str = None, description: dict = None,
                 permissions: list = None) -> dict:
    """Update a space by key (v1 API).
    
    Permissions required: Permission to administer the space.
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if permissions:
        data["permissions"] = permissions
    
    return _api_request("PUT", f"/wiki/rest/api/space/{space_key}", data=data)


@mcp.tool()
def delete_space(space_key: str) -> dict:
    """Delete a space by key (v1 API).
    
    Permissions required: Permission to administer the space.
    """
    return _api_request("DELETE", f"/wiki/rest/api/space/{space_key}")


# ============================================================================
# CONTENT OPERATIONS (v1 - additional)
# ============================================================================

@mcp.tool()
def archive_pages(pages: list[dict]) -> dict:
    """Archive pages (v1 API - Experimental).
    
    This API accepts the archival request and returns a task ID.
    The archival process happens asynchronously.
    
    Permissions required: 'Archive' permission for each of the pages in the corresponding space.
    """
    data = {"pages": pages}
    
    return _api_request("POST", "/wiki/rest/api/content/archive", data=data)


# Run the server if executed directly
if __name__ == "__main__":
    mcp.run(transport="stdio")
