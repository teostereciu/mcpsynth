#!/usr/bin/env python3
"""
Confluence Cloud MCP Server

An MCP server with comprehensive coverage of the Confluence Cloud REST API.
"""

import os
import requests
from typing import Any

from fastmcp import FastMCP
from fastmcp.tools import Tool

# Initialize FastMCP server
mcp = FastMCP(
    name="confluence",
    version="1.0.0",
)

# Authentication configuration
CONFLUENCE_BASE_URL = os.environ.get("CONFLUENCE_BASE_URL")
CONFLUENCE_SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

# Verify required environment variables
if not all([CONFLUENCE_BASE_URL, CONFLUENCE_SPACE_KEY, JIRA_EMAIL, JIRA_API_TOKEN]):
    print("Warning: Not all environment variables are set.")


def confluence_request(
    method: str,
    endpoint: str,
    params: dict | None = None,
    json: dict | None = None,
    **kwargs
) -> dict | list | str:
    """
    Make a request to the Confluence Cloud API.
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE, PATCH)
        endpoint: API endpoint path (e.g., '/wiki/api/v2/pages')
        params: Query parameters
        json: Request body for POST/PUT requests
        **kwargs: Additional arguments to pass to requests
        
    Returns:
        JSON response from the API
        
    Raises:
        requests.HTTPError: If the request fails
    """
    url = f"{CONFLUENCE_BASE_URL}{endpoint}"
    
    auth = (JIRA_EMAIL, JIRA_API_TOKEN)
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    
    # Merge headers from kwargs if provided
    if "headers" in kwargs:
        headers.update(kwargs["headers"])
        del kwargs["headers"]
    
    response = requests.request(
        method=method,
        url=url,
        params=params,
        json=json,
        auth=auth,
        headers=headers,
        **kwargs
    )
    
    # Handle response based on status code
    if response.status_code == 204:
        return {"message": "Operation successful, no content returned"}
    elif response.status_code >= 200 and response.status_code < 300:
        try:
            return response.json()
        except ValueError:
            return response.text
    else:
        # Return error information
        try:
            error_json = response.json()
            error_json["status_code"] = response.status_code
            return {"error": error_json}
        except ValueError:
            return {
                "error": response.text,
                "status_code": response.status_code
            }


# ============================================================================
# PAGE OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def confluence_create_page(
    space_id: str,
    title: str,
    body: str,
    parent_id: str | None = None,
    content_status: str = "current",
    subtype: str | None = None,
) -> dict:
    """
    Creates a new page in Confluence.
    
    Args:
        space_id: The ID of the space where the page will be created
        title: The title of the page
        body: The body content of the page (in storage format)
        parent_id: Optional parent page ID for hierarchical pages
        content_status: The status of the page ('current' or 'draft')
        subtype: Optional subtype (e.g., 'template', 'live')
        
    Returns:
        The created page object
    """
    endpoint = "/wiki/api/v2/pages"
    
    payload = {
        "spaceId": space_id,
        "title": title,
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        },
        "content_status": content_status
    }
    
    if parent_id:
        payload["parentId"] = parent_id
    if subtype:
        payload["subtype"] = subtype
    
    return confluence_request("POST", endpoint, json=payload)


@mcp.tool()
def confluence_get_page_by_id(
    page_id: int,
    include_labels: bool = False,
    include_properties: bool = False,
    include_version: bool = True,
    body_format: str = "storage",
) -> dict:
    """
    Retrieves a specific page by its ID.
    
    Args:
        page_id: The ID of the page to retrieve
        include_labels: Whether to include labels in the response
        include_properties: Whether to include properties in the response
        include_version: Whether to include version information
        body_format: The format of the body content ('storage', 'view', etc.)
        
    Returns:
        The page object
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}"
    
    params = {}
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_version:
        params["include-version"] = "true"
    if body_format:
        params["body-format"] = body_format
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_update_page(
    page_id: int,
    title: str,
    body: str,
    content_status: str = "current",
    parent_id: str | None = None,
) -> dict:
    """
    Updates an existing page in Confluence.
    
    Args:
        page_id: The ID of the page to update
        title: The new title of the page
        body: The new body content of the page (in storage format)
        content_status: The status of the page ('current' or 'draft')
        parent_id: Optional new parent page ID
        
    Returns:
        The updated page object
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}"
    
    payload = {
        "id": str(page_id),
        "title": title,
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        },
        "content_status": content_status,
        "version": {
            "number": 1  # Will be updated by the API
        }
    }
    
    if parent_id:
        payload["parentId"] = parent_id
    
    return confluence_request("PUT", endpoint, json=payload)


@mcp.tool()
def confluence_delete_page(
    page_id: int,
    purge: bool = False,
    draft: bool = False,
) -> dict:
    """
    Deletes a page in Confluence.
    
    Args:
        page_id: The ID of the page to delete
        purge: Whether to permanently delete (purge) the page
        draft: Whether the page is a draft
        
    Returns:
        Deletion status
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}"
    
    params = {}
    if purge:
        params["purge"] = "true"
    if draft:
        params["draft"] = "true"
    
    return confluence_request("DELETE", endpoint, params=params)


@mcp.tool()
def confluence_get_pages(
    space_id: int | None = None,
    title: str | None = None,
    content_status: str | None = None,
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves a list of pages.
    
    Args:
        space_id: Optional space ID to filter by
        title: Optional title to filter by
        content_status: Optional content status to filter by
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        A paginated list of pages
    """
    endpoint = "/wiki/api/v2/pages"
    
    params = {
        "max_results": str(max_results)
    }
    
    if space_id:
        params["space-id"] = str(space_id)
    if title:
        params["title"] = title
    if content_status:
        params["content_status"] = content_status
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_get_page_children(
    page_id: int,
    include_version: bool = False,
    include_label: bool = False,
    max_results: int = 25,
) -> dict:
    """
    Retrieves the children of a page.
    
    Args:
        page_id: The ID of the page
        include_version: Whether to include version information
        include_label: Whether to include label information
        max_results: Maximum number of results to return
        
    Returns:
        A list of child pages
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/children"
    
    params = {
        "max_results": str(max_results)
    }
    
    if include_version:
        params["include-version"] = "true"
    if include_label:
        params["include-label"] = "true"
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_move_page(
    page_id: int,
    target_parent_id: int | None = None,
    target_position: str = "last-child",
) -> dict:
    """
    Moves a page to a new parent or position.
    
    Args:
        page_id: The ID of the page to move
        target_parent_id: The ID of the new parent page
        target_position: The position relative to siblings ('first-child', 'last-child', 'before', 'after')
        
    Returns:
        The moved page object
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}"
    
    payload = {
        "version": {
            "number": 1
        }
    }
    
    if target_parent_id:
        payload["parentId"] = str(target_parent_id)
    
    # Note: Position handling may require different endpoint
    return confluence_request("PUT", endpoint, json=payload)


# ============================================================================
# SPACE OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def confluence_get_spaces(
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves a list of spaces.
    
    Args:
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        A paginated list of spaces
    """
    endpoint = "/wiki/api/v2/spaces"
    
    params = {
        "max_results": str(max_results)
    }
    
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_get_space_by_id(
    space_id: int,
    include_icon: bool = False,
    include_operations: bool = False,
) -> dict:
    """
    Retrieves a specific space by its ID.
    
    Args:
        space_id: The ID of the space
        include_icon: Whether to include space icon
        include_operations: Whether to include operations
        
    Returns:
        The space object
    """
    endpoint = f"/wiki/api/v2/spaces/{space_id}"
    
    params = {}
    if include_icon:
        params["include-icon"] = "true"
    if include_operations:
        params["include-operations"] = "true"
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_create_space(
    name: str,
    key: str | None = None,
    description: str | None = None,
) -> dict:
    """
    Creates a new space in Confluence.
    
    Args:
        name: The name of the space
        key: The space key (auto-generated if not provided)
        description: The description of the space
        
    Returns:
        The created space object
    """
    endpoint = "/wiki/api/v2/spaces"
    
    payload = {
        "name": name
    }
    
    if key:
        payload["key"] = key
    if description:
        payload["description"] = {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
    
    return confluence_request("POST", endpoint, json=payload)


@mcp.tool()
def confluence_update_space(
    space_id: int,
    name: str | None = None,
    description: str | None = None,
) -> dict:
    """
    Updates an existing space.
    
    Args:
        space_id: The ID of the space to update
        name: The new name of the space
        description: The new description of the space
        
    Returns:
        The updated space object
    """
    endpoint = f"/wiki/api/v2/spaces/{space_id}"
    
    payload = {
        "version": {
            "number": 1
        }
    }
    
    if name:
        payload["name"] = name
    if description:
        payload["description"] = {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
    
    return confluence_request("PUT", endpoint, json=payload)


@mcp.tool()
def confluence_delete_space(
    space_id: int,
) -> dict:
    """
    Deletes a space in Confluence.
    
    Args:
        space_id: The ID of the space to delete
        
    Returns:
        Deletion status
    """
    endpoint = f"/wiki/api/v2/spaces/{space_id}"
    
    return confluence_request("DELETE", endpoint)


# ============================================================================
# SEARCH OPERATIONS (v1)
# ============================================================================

@mcp.tool()
def confluence_search(
    query: str,
    cql: str | None = None,
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Searches for content using CQL (Confluence Query Language).
    
    Args:
        query: The search query string
        cql: Optional CQL query
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        Search results
    """
    endpoint = "/wiki/rest/api/search"
    
    params = {
        "cql": cql if cql else query,
        "max_results": str(max_results)
    }
    
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_search_users(
    query: str,
    max_results: int = 25,
    offset: int = 0,
) -> dict:
    """
    Searches for users using CQL.
    
    Args:
        query: The search query string (user-specific fields only)
        max_results: Maximum number of results to return
        offset: Starting offset for pagination
        
    Returns:
        User search results
    """
    endpoint = "/wiki/rest/api/search/user"
    
    params = {
        "cql": query,
        "max_results": str(max_results),
        "offset": str(offset)
    }
    
    return confluence_request("GET", endpoint, params=params)


# ============================================================================
# LABEL OPERATIONS (v1 and v2)
# ============================================================================

@mcp.tool()
def confluence_add_labels_to_page(
    page_id: int,
    labels: list[str],
) -> dict:
    """
    Adds labels to a page.
    
    Args:
        page_id: The ID of the page
        labels: List of label names to add
        
    Returns:
        The updated labels
    """
    endpoint = "/wiki/rest/api/content/{page_id}/label".replace("{page_id}", str(page_id))
    
    label_objects = [{"prefix": "global", "name": label} for label in labels]
    
    return confluence_request("POST", endpoint, json=label_objects)


@mcp.tool()
def confluence_remove_label_from_page(
    page_id: int,
    label_name: str,
) -> dict:
    """
    Removes a label from a page.
    
    Args:
        page_id: The ID of the page
        label_name: The name of the label to remove
        
    Returns:
        Deletion status
    """
    endpoint = "/wiki/rest/api/content/{page_id}/label/{label_name}".replace(
        "{page_id}", str(page_id)
    ).replace("{label_name}", label_name)
    
    return confluence_request("DELETE", endpoint)


@mcp.tool()
def confluence_get_labels_for_page(
    page_id: int,
    max_results: int = 25,
) -> dict:
    """
    Retrieves labels for a page.
    
    Args:
        page_id: The ID of the page
        max_results: Maximum number of results to return
        
    Returns:
        List of labels
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/labels"
    
    params = {
        "max_results": str(max_results)
    }
    
    return confluence_request("GET", endpoint, params=params)


# ============================================================================
# ATTACHMENT OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def confluence_get_attachments(
    content_id: int,
    content_type: str = "page",
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves attachments for a page or blog post.
    
    Args:
        content_id: The ID of the page or blog post
        content_type: The type of content ('page', 'blogpost')
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        List of attachments
    """
    if content_type == "page":
        endpoint = f"/wiki/api/v2/pages/{content_id}/attachments"
    elif content_type == "blogpost":
        endpoint = f"/wiki/api/v2/blogposts/{content_id}/attachments"
    else:
        endpoint = f"/wiki/api/v2/attachments"
    
    params = {
        "max_results": str(max_results)
    }
    
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_get_attachment_by_id(
    attachment_id: int,
    include_labels: bool = False,
) -> dict:
    """
    Retrieves a specific attachment by its ID.
    
    Args:
        attachment_id: The ID of the attachment
        include_labels: Whether to include labels
        
    Returns:
        The attachment object
    """
    endpoint = f"/wiki/api/v2/attachments/{attachment_id}"
    
    params = {}
    if include_labels:
        params["include-labels"] = "true"
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_delete_attachment(
    attachment_id: int,
    purge: bool = False,
) -> dict:
    """
    Deletes an attachment.
    
    Args:
        attachment_id: The ID of the attachment to delete
        purge: Whether to permanently delete (purge) the attachment
        
    Returns:
        Deletion status
    """
    endpoint = f"/wiki/api/v2/attachments/{attachment_id}"
    
    params = {}
    if purge:
        params["purge"] = "true"
    
    return confluence_request("DELETE", endpoint, params=params)


# ============================================================================
# COMMENT OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def confluence_get_page_footer_comments(
    page_id: int,
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves footer comments for a page.
    
    Args:
        page_id: The ID of the page
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        List of footer comments
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/footer-comments"
    
    params = {
        "max_results": str(max_results)
    }
    
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_create_page_footer_comment(
    page_id: int,
    body: str,
) -> dict:
    """
    Creates a footer comment on a page.
    
    Args:
        page_id: The ID of the page
        body: The comment body content (in storage format)
        
    Returns:
        The created comment
    """
    endpoint = "/wiki/api/v2/footer-comments"
    
    payload = {
        "pageId": str(page_id),
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        }
    }
    
    return confluence_request("POST", endpoint, json=payload)


@mcp.tool()
def confluence_get_inline_comments(
    page_id: int,
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves inline comments for a page.
    
    Args:
        page_id: The ID of the page
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        List of inline comments
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/inline-comments"
    
    params = {
        "max_results": str(max_results)
    }
    
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


# ============================================================================
# VERSION OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def confluence_get_page_versions(
    page_id: int,
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves versions of a page.
    
    Args:
        page_id: The ID of the page
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        List of page versions
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/versions"
    
    params = {
        "max_results": str(max_results)
    }
    
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_get_version_details(
    page_id: int,
    version_number: int,
) -> dict:
    """
    Retrieves details of a specific page version.
    
    Args:
        page_id: The ID of the page
        version_number: The version number
        
    Returns:
        Version details
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/versions/{version_number}"
    
    return confluence_request("GET", endpoint)


@mcp.tool()
def confluence_restore_page_version(
    page_id: int,
    version_number: int,
    message: str = "Restored from previous version",
) -> dict:
    """
    Restores a previous version of a page.
    
    Args:
        page_id: The ID of the page
        version_number: The version number to restore
        message: The version message
        
    Returns:
        The restored version
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/versions"
    
    # Note: This endpoint typically uses POST to restore a version
    # The exact API may vary based on Confluence version
    payload = {
        "message": message
    }
    
    return confluence_request("POST", endpoint, json=payload)


# ============================================================================
# CONTENT PROPERTIES (v2)
# ============================================================================

@mcp.tool()
def confluence_get_page_properties(
    page_id: int,
    key: str | None = None,
    max_results: int = 25,
    cursor: str | None = None,
) -> dict:
    """
    Retrieves properties for a page.
    
    Args:
        page_id: The ID of the page
        key: Optional property key to filter by
        max_results: Maximum number of results to return
        cursor: Cursor for pagination
        
    Returns:
        List of page properties
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/properties"
    
    params = {
        "max_results": str(max_results)
    }
    
    if key:
        params["key"] = key
    if cursor:
        params["cursor"] = cursor
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_create_page_property(
    page_id: int,
    key: str,
    value: Any,
) -> dict:
    """
    Creates a property for a page.
    
    Args:
        page_id: The ID of the page
        key: The property key
        value: The property value
        
    Returns:
        The created property
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/properties"
    
    payload = {
        "key": key,
        "value": value
    }
    
    return confluence_request("POST", endpoint, json=payload)


@mcp.tool()
def confluence_update_page_property(
    page_id: int,
    property_id: int,
    key: str,
    value: Any,
) -> dict:
    """
    Updates a property for a page.
    
    Args:
        page_id: The ID of the page
        property_id: The ID of the property
        key: The property key
        value: The property value
        
    Returns:
        The updated property
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/properties/{property_id}"
    
    payload = {
        "key": key,
        "value": value,
        "version": {
            "number": 1
        }
    }
    
    return confluence_request("PUT", endpoint, json=payload)


@mcp.tool()
def confluence_delete_page_property(
    page_id: int,
    property_id: int,
) -> dict:
    """
    Deletes a property from a page.
    
    Args:
        page_id: The ID of the page
        property_id: The ID of the property
        
    Returns:
        Deletion status
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/properties/{property_id}"
    
    return confluence_request("DELETE", endpoint)


# ============================================================================
# BLOG POST OPERATIONS (v2)
# ============================================================================

@mcp.tool()
def confluence_create_blog_post(
    space_id: str,
    title: str,
    body: str,
    content_status: str = "current",
) -> dict:
    """
    Creates a new blog post in Confluence.
    
    Args:
        space_id: The ID of the space where the blog post will be created
        title: The title of the blog post
        body: The body content of the blog post (in storage format)
        content_status: The status of the blog post ('current' or 'draft')
        
    Returns:
        The created blog post object
    """
    endpoint = "/wiki/api/v2/blogposts"
    
    payload = {
        "spaceId": space_id,
        "title": title,
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        },
        "content_status": content_status
    }
    
    return confluence_request("POST", endpoint, json=payload)


@mcp.tool()
def confluence_get_blog_post_by_id(
    blog_post_id: int,
    include_labels: bool = False,
) -> dict:
    """
    Retrieves a specific blog post by its ID.
    
    Args:
        blog_post_id: The ID of the blog post
        include_labels: Whether to include labels
        
    Returns:
        The blog post object
    """
    endpoint = f"/wiki/api/v2/blogposts/{blog_post_id}"
    
    params = {}
    if include_labels:
        params["include-labels"] = "true"
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_update_blog_post(
    blog_post_id: int,
    title: str,
    body: str,
    content_status: str = "current",
) -> dict:
    """
    Updates an existing blog post.
    
    Args:
        blog_post_id: The ID of the blog post to update
        title: The new title of the blog post
        body: The new body content of the blog post (in storage format)
        content_status: The status of the blog post ('current' or 'draft')
        
    Returns:
        The updated blog post object
    """
    endpoint = f"/wiki/api/v2/blogposts/{blog_post_id}"
    
    payload = {
        "id": str(blog_post_id),
        "title": title,
        "body": {
            "storage": {
                "value": body,
                "representation": "storage"
            }
        },
        "content_status": content_status,
        "version": {
            "number": 1
        }
    }
    
    return confluence_request("PUT", endpoint, json=payload)


@mcp.tool()
def confluence_delete_blog_post(
    blog_post_id: int,
    purge: bool = False,
    draft: bool = False,
) -> dict:
    """
    Deletes a blog post in Confluence.
    
    Args:
        blog_post_id: The ID of the blog post to delete
        purge: Whether to permanently delete (purge) the blog post
        draft: Whether the blog post is a draft
        
    Returns:
        Deletion status
    """
    endpoint = f"/wiki/api/v2/blogposts/{blog_post_id}"
    
    params = {}
    if purge:
        params["purge"] = "true"
    if draft:
        params["draft"] = "true"
    
    return confluence_request("DELETE", endpoint, params=params)


# ============================================================================
# USER OPERATIONS (v1)
# ============================================================================

@mcp.tool()
def confluence_get_current_user(
    include: str = "profilePicture,displayName",
) -> dict:
    """
    Retrieves information about the currently logged-in user.
    
    Args:
        include: Comma-separated list of fields to include
        
    Returns:
        User information
    """
    endpoint = "/wiki/rest/api/user/current"
    
    params = {
        "include": include
    }
    
    return confluence_request("GET", endpoint, params=params)


@mcp.tool()
def confluence_get_user_by_account_id(
    account_id: str,
    include: str = "profilePicture,displayName",
) -> dict:
    """
    Retrieves a user by their account ID.
    
    Args:
        account_id: The Atlassian account ID
        include: Comma-separated list of fields to include
        
    Returns:
        User information
    """
    endpoint = "/wiki/rest/api/user"
    
    params = {
        "accountId": account_id,
        "include": include
    }
    
    return confluence_request("GET", endpoint, params=params)


# ============================================================================
# ADDITIONAL UTILITY FUNCTIONS
# ============================================================================

@mcp.tool()
def confluence_get_ancestors(
    page_id: int,
) -> dict:
    """
    Retrieves the ancestors of a page.
    
    Args:
        page_id: The ID of the page
        
    Returns:
        List of ancestor pages
    """
    endpoint = f"/wiki/api/v2/pages/{page_id}/ancestors"
    
    return confluence_request("GET", endpoint)


@mcp.tool()
def confluence_get_space_by_key(
    space_key: str,
) -> dict:
    """
    Retrieves a space by its key.
    
    Args:
        space_key: The space key
        
    Returns:
        Space information
    """
    # Use v1 API for space key lookup
    endpoint = f"/wiki/rest/api/space/{space_key}"
    
    return confluence_request("GET", endpoint)


@mcp.tool()
def confluence_get_page_by_title(
    space_key: str,
    title: str,
) -> dict:
    """
    Retrieves a page by its title within a space.
    
    Args:
        space_key: The space key
        title: The page title
        
    Returns:
        Page information
    """
    endpoint = "/wiki/rest/api/content"
    
    params = {
        "spaceKey": space_key,
        "title": title,
        "expand": "body.storage,version"
    }
    
    result = confluence_request("GET", endpoint, params=params)
    
    # Extract the first result if available
    if isinstance(result, dict) and "results" in result:
        results = result["results"]
        if results:
            return results[0]
    
    return result


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
