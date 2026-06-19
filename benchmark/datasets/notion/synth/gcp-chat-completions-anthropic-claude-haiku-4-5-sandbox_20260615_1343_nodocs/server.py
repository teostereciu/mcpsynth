#!/usr/bin/env python3
"""
Notion API MCP Server

Provides tools for interacting with the Notion API including:
- Pages (create, retrieve, update, archive)
- Databases (create, query, update)
- Blocks (retrieve, append, update, delete)
- Comments
- Users
- Search
"""

import os
import json
import requests
from typing import Any, Dict, Optional, List
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
server = FastMCP("notion-api")

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2024-02"

# Helper function to make API requests
def make_request(
    method: str,
    endpoint: str,
    data: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to the Notion API."""
    if not NOTION_API_KEY:
        return {"error": "NOTION_API_KEY environment variable not set"}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data, params=params, timeout=30)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, json=data, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {
                "error": f"API error {response.status_code}",
                "details": response.text
            }
        
        if response.status_code == 204:
            return {"success": True}
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}


# ============================================================================
# PAGES TOOLS
# ============================================================================

@server.tool()
def create_page(
    parent_id: str,
    title: str,
    properties: Optional[Dict[str, Any]] = None,
    children: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Create a new page in Notion.
    
    Args:
        parent_id: The ID of the parent page or database
        title: The title of the new page
        properties: Optional page properties (for database pages)
        children: Optional list of block children to add to the page
    
    Returns:
        The created page object
    """
    payload = {
        "parent": {"page_id": parent_id},
        "properties": properties or {
            "title": {
                "title": [{"text": {"content": title}}]
            }
        },
    }
    
    if children:
        payload["children"] = children
    
    return make_request("POST", "/pages", data=payload)


@server.tool()
def get_page(page_id: str) -> Dict[str, Any]:
    """
    Retrieve a page by ID.
    
    Args:
        page_id: The ID of the page to retrieve
    
    Returns:
        The page object
    """
    return make_request("GET", f"/pages/{page_id}")


@server.tool()
def update_page(
    page_id: str,
    properties: Dict[str, Any],
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Update a page's properties, icon, or cover.
    
    Args:
        page_id: The ID of the page to update
        properties: The properties to update
        icon: Optional icon object
        cover: Optional cover object
    
    Returns:
        The updated page object
    """
    payload = {"properties": properties}
    
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    
    return make_request("PATCH", f"/pages/{page_id}", data=payload)


@server.tool()
def archive_page(page_id: str) -> Dict[str, Any]:
    """
    Archive a page (soft delete).
    
    Args:
        page_id: The ID of the page to archive
    
    Returns:
        The archived page object
    """
    return make_request("PATCH", f"/pages/{page_id}", data={"archived": True})


@server.tool()
def restore_page(page_id: str) -> Dict[str, Any]:
    """
    Restore an archived page.
    
    Args:
        page_id: The ID of the page to restore
    
    Returns:
        The restored page object
    """
    return make_request("PATCH", f"/pages/{page_id}", data={"archived": False})


@server.tool()
def get_page_property(page_id: str, property_id: str) -> Dict[str, Any]:
    """
    Retrieve a specific property of a page.
    
    Args:
        page_id: The ID of the page
        property_id: The ID of the property to retrieve
    
    Returns:
        The property object
    """
    return make_request("GET", f"/pages/{page_id}/properties/{property_id}")


# ============================================================================
# DATABASES TOOLS
# ============================================================================

@server.tool()
def create_database(
    parent_id: str,
    title: str,
    properties: Dict[str, Any],
    is_inline: bool = False,
) -> Dict[str, Any]:
    """
    Create a new database.
    
    Args:
        parent_id: The ID of the parent page
        title: The title of the database
        properties: The database schema (property definitions)
        is_inline: Whether the database is inline (default: False)
    
    Returns:
        The created database object
    """
    payload = {
        "parent": {"page_id": parent_id},
        "title": [{"text": {"content": title}}],
        "properties": properties,
        "is_inline": is_inline,
    }
    
    return make_request("POST", "/databases", data=payload)


@server.tool()
def get_database(database_id: str) -> Dict[str, Any]:
    """
    Retrieve a database by ID.
    
    Args:
        database_id: The ID of the database to retrieve
    
    Returns:
        The database object
    """
    return make_request("GET", f"/databases/{database_id}")


@server.tool()
def update_database(
    database_id: str,
    title: Optional[str] = None,
    properties: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a database's title, properties, or description.
    
    Args:
        database_id: The ID of the database to update
        title: Optional new title
        properties: Optional property updates
        description: Optional description
    
    Returns:
        The updated database object
    """
    payload = {}
    
    if title is not None:
        payload["title"] = [{"text": {"content": title}}]
    if properties is not None:
        payload["properties"] = properties
    if description is not None:
        payload["description"] = [{"text": {"content": description}}]
    
    return make_request("PATCH", f"/databases/{database_id}", data=payload)


@server.tool()
def query_database(
    database_id: str,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> Dict[str, Any]:
    """
    Query a database with optional filters and sorts.
    
    Args:
        database_id: The ID of the database to query
        filter: Optional filter object
        sorts: Optional list of sort objects
        start_cursor: Optional cursor for pagination
        page_size: Number of results per page (1-100, default: 100)
    
    Returns:
        Query results with pages and pagination info
    """
    payload = {
        "page_size": min(page_size, 100),
    }
    
    if filter is not None:
        payload["filter"] = filter
    if sorts is not None:
        payload["sorts"] = sorts
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    
    return make_request("POST", f"/databases/{database_id}/query", data=payload)


# ============================================================================
# BLOCKS TOOLS
# ============================================================================

@server.tool()
def get_block(block_id: str) -> Dict[str, Any]:
    """
    Retrieve a block by ID.
    
    Args:
        block_id: The ID of the block to retrieve
    
    Returns:
        The block object
    """
    return make_request("GET", f"/blocks/{block_id}")


@server.tool()
def get_block_children(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> Dict[str, Any]:
    """
    Retrieve the children of a block (e.g., paragraphs in a page).
    
    Args:
        block_id: The ID of the block
        start_cursor: Optional cursor for pagination
        page_size: Number of results per page (1-100, default: 100)
    
    Returns:
        List of child blocks and pagination info
    """
    params = {"page_size": min(page_size, 100)}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    
    return make_request("GET", f"/blocks/{block_id}/children", params=params)


@server.tool()
def append_block_children(
    block_id: str,
    children: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Append blocks as children to a block.
    
    Args:
        block_id: The ID of the parent block
        children: List of block objects to append
    
    Returns:
        The appended blocks
    """
    payload = {"children": children}
    return make_request("PATCH", f"/blocks/{block_id}/children", data=payload)


@server.tool()
def update_block(
    block_id: str,
    block_data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Update a block's content.
    
    Args:
        block_id: The ID of the block to update
        block_data: The updated block data
    
    Returns:
        The updated block object
    """
    return make_request("PATCH", f"/blocks/{block_id}", data=block_data)


@server.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    """
    Delete a block.
    
    Args:
        block_id: The ID of the block to delete
    
    Returns:
        Confirmation of deletion
    """
    return make_request("DELETE", f"/blocks/{block_id}")


# ============================================================================
# COMMENTS TOOLS
# ============================================================================

@server.tool()
def create_comment(
    page_id: str,
    text: str,
) -> Dict[str, Any]:
    """
    Create a comment on a page.
    
    Args:
        page_id: The ID of the page to comment on
        text: The comment text
    
    Returns:
        The created comment object
    """
    payload = {
        "parent": {"page_id": page_id},
        "rich_text": [{"text": {"content": text}}],
    }
    
    return make_request("POST", "/comments", data=payload)


@server.tool()
def get_comments(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> Dict[str, Any]:
    """
    Retrieve comments on a block or page.
    
    Args:
        block_id: The ID of the block or page
        start_cursor: Optional cursor for pagination
        page_size: Number of results per page (1-100, default: 100)
    
    Returns:
        List of comments and pagination info
    """
    params = {"block_id": block_id, "page_size": min(page_size, 100)}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    
    return make_request("GET", "/comments", params=params)


# ============================================================================
# USERS TOOLS
# ============================================================================

@server.tool()
def get_user(user_id: str) -> Dict[str, Any]:
    """
    Retrieve a user by ID.
    
    Args:
        user_id: The ID of the user to retrieve
    
    Returns:
        The user object
    """
    return make_request("GET", f"/users/{user_id}")


@server.tool()
def list_users(
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> Dict[str, Any]:
    """
    List all users in the workspace.
    
    Args:
        start_cursor: Optional cursor for pagination
        page_size: Number of results per page (1-100, default: 100)
    
    Returns:
        List of users and pagination info
    """
    params = {"page_size": min(page_size, 100)}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    
    return make_request("GET", "/users", params=params)


@server.tool()
def get_current_user() -> Dict[str, Any]:
    """
    Get the current authenticated user.
    
    Returns:
        The current user object
    """
    return make_request("GET", "/users/me")


# ============================================================================
# SEARCH TOOLS
# ============================================================================

@server.tool()
def search(
    query: str,
    sort: Optional[Dict[str, Any]] = None,
    filter: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> Dict[str, Any]:
    """
    Search for pages and databases.
    
    Args:
        query: The search query string
        sort: Optional sort object
        filter: Optional filter object (e.g., {"property": "object", "value": "page"})
        start_cursor: Optional cursor for pagination
        page_size: Number of results per page (1-100, default: 100)
    
    Returns:
        Search results and pagination info
    """
    payload = {
        "query": query,
        "page_size": min(page_size, 100),
    }
    
    if sort is not None:
        payload["sort"] = sort
    if filter is not None:
        payload["filter"] = filter
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    
    return make_request("POST", "/search", data=payload)


# ============================================================================
# UTILITY TOOLS
# ============================================================================

@server.tool()
def create_paragraph_block(text: str) -> Dict[str, str]:
    """
    Create a paragraph block object for use with append_block_children.
    
    Args:
        text: The paragraph text
    
    Returns:
        A paragraph block object
    """
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": "default",
        },
    }


@server.tool()
def create_heading_block(text: str, level: int = 1) -> Dict[str, Any]:
    """
    Create a heading block object for use with append_block_children.
    
    Args:
        text: The heading text
        level: Heading level (1, 2, or 3)
    
    Returns:
        A heading block object
    """
    if level not in [1, 2, 3]:
        return {"error": "Heading level must be 1, 2, or 3"}
    
    heading_type = f"heading_{level}"
    return {
        "object": "block",
        "type": heading_type,
        heading_type: {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": "default",
        },
    }


@server.tool()
def create_bullet_list_block(text: str) -> Dict[str, str]:
    """
    Create a bullet list block object for use with append_block_children.
    
    Args:
        text: The list item text
    
    Returns:
        A bullet list block object
    """
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": "default",
        },
    }


@server.tool()
def create_numbered_list_block(text: str) -> Dict[str, str]:
    """
    Create a numbered list block object for use with append_block_children.
    
    Args:
        text: The list item text
    
    Returns:
        A numbered list block object
    """
    return {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": "default",
        },
    }


@server.tool()
def create_code_block(text: str, language: str = "python") -> Dict[str, Any]:
    """
    Create a code block object for use with append_block_children.
    
    Args:
        text: The code content
        language: The programming language (default: python)
    
    Returns:
        A code block object
    """
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "language": language,
            "caption": [],
        },
    }


@server.tool()
def create_divider_block() -> Dict[str, str]:
    """
    Create a divider block object for use with append_block_children.
    
    Returns:
        A divider block object
    """
    return {
        "object": "block",
        "type": "divider",
        "divider": {},
    }


if __name__ == "__main__":
    server.run()
