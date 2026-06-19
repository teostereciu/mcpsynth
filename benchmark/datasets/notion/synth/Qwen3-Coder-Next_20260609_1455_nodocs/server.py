#!/usr/bin/env python3
"""
Notion MCP Server

An MCP server for interacting with the Notion API.
"""

import os
import requests
from typing import Any
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP(name="notion", log_level="INFO")

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_VERSION = "2022-06-22"
BASE_URL = "https://api.notion.com/v1"


def _get_headers() -> dict:
    """Get authentication headers."""
    if not NOTION_API_KEY:
        raise ValueError("NOTION_API_KEY environment variable is not set")
    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, endpoint: str, params: dict = None, json: dict = None) -> dict:
    """Make a request to the Notion API."""
    url = f"{BASE_URL}{endpoint}"
    headers = _get_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {"error": "Resource not found"}
        elif e.response.status_code == 401:
            return {"error": "Unauthorized - check API key"}
        elif e.response.status_code == 400:
            return {"error": f"Bad request: {e.response.text}"}
        return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ==================== User Tools ====================

@mcp.tool()
def get_user(user_id: str) -> dict:
    """Get information about a specific user by ID.
    
    Args:
        user_id: The ID of the user to retrieve
        
    Returns:
        User object with details
    """
    return _request("GET", f"/users/{user_id}")


@mcp.tool()
def list_users() -> dict:
    """List all users in the workspace.
    
    Returns:
        Object with 'results' array of users and pagination info
    """
    return _request("GET", "/users")


@mcp.tool()
def get_current_bot() -> dict:
    """Get information about the current bot/user associated with the API token.
    
    Returns:
        User object for the current bot
    """
    return _request("GET", "/users/me")


# ==================== Search Tools ====================

@mcp.tool()
def search_pages(
    query: str = None,
    sort: dict = None,
    start_cursor: str = None,
    page_size: int = 10,
) -> dict:
    """Search for pages in the workspace.
    
    Args:
        query: Search query to filter pages
        sort: Optional sort configuration with 'direction' and 'timestamp'
        start_cursor: Pagination cursor for next page
        page_size: Number of results per page (1-100)
        
    Returns:
        Object with 'results' array of pages and pagination info
    """
    payload = {"filter": {"value": "page"}, "page_size": page_size}
    
    if query:
        payload["query"] = query
        
    if sort:
        payload["sort"] = sort
        
    if start_cursor:
        payload["start_cursor"] = start_cursor
        
    return _request("POST", "/search", json=payload)


@mcp.tool()
def search_databases(
    query: str = None,
    sort: dict = None,
    start_cursor: str = None,
    page_size: int = 10,
) -> dict:
    """Search for databases in the workspace.
    
    Args:
        query: Search query to filter databases
        sort: Optional sort configuration with 'direction' and 'timestamp'
        start_cursor: Pagination cursor for next page
        page_size: Number of results per page (1-100)
        
    Returns:
        Object with 'results' array of databases and pagination info
    """
    payload = {"filter": {"value": "database"}, "page_size": page_size}
    
    if query:
        payload["query"] = query
        
    if sort:
        payload["sort"] = sort
        
    if start_cursor:
        payload["start_cursor"] = start_cursor
        
    return _request("POST", "/search", json=payload)


# ==================== Page Tools ====================

@mcp.tool()
def get_page(page_id: str) -> dict:
    """Retrieve a page by ID.
    
    Args:
        page_id: The ID of the page to retrieve
        
    Returns:
        Page object with all properties
    """
    return _request("GET", f"/pages/{page_id}")


@mcp.tool()
def create_page(
    parent_page_id: str,
    title: str,
    properties: dict = None,
    children: list = None,
) -> dict:
    """Create a new page as a child of another page.
    
    Args:
        parent_page_id: The ID of the parent page
        title: The title for the new page
        properties: Additional page properties (name-value pairs)
        children: Optional list of block children to add to the page
        
    Returns:
        The created page object
    """
    payload = {
        "parent": {"page_id": parent_page_id},
        "properties": {"title": [{"text": {"content": title}}]},
    }
    
    if properties:
        payload["properties"].update(properties)
        
    if children:
        payload["children"] = children
        
    return _request("POST", "/pages", json=payload)


@mcp.tool()
def update_page(page_id: str, properties: dict = None, archived: bool = None) -> dict:
    """Update properties of an existing page.
    
    Args:
        page_id: The ID of the page to update
        properties: Page properties to update
        archived: Whether to archive the page (True) or unarchive (False)
        
    Returns:
        The updated page object
    """
    payload = {}
    
    if properties:
        payload["properties"] = properties
        
    if archived is not None:
        payload["archived"] = archived
        
    return _request("PATCH", f"/pages/{page_id}", json=payload)


@mcp.tool()
def archive_page(page_id: str) -> dict:
    """Archive a page.
    
    Args:
        page_id: The ID of the page to archive
        
    Returns:
        The archived page object
    """
    return _request("PATCH", f"/pages/{page_id}", json={"archived": True})


@mcp.tool()
def unarchive_page(page_id: str) -> dict:
    """Unarchive a page.
    
    Args:
        page_id: The ID of the page to unarchive
        
    Returns:
        The unarchived page object
    """
    return _request("PATCH", f"/pages/{page_id}", json={"archived": False})


# ==================== Database Tools ====================

@mcp.tool()
def get_database(database_id: str) -> dict:
    """Retrieve a database by ID.
    
    Args:
        database_id: The ID of the database to retrieve
        
    Returns:
        Database object with schema and metadata
    """
    return _request("GET", f"/databases/{database_id}")


@mcp.tool()
def query_database(
    database_id: str,
    filter: dict = None,
    sort: dict = None,
    start_cursor: str = None,
    page_size: int = 10,
) -> dict:
    """Query a database for rows matching specified criteria.
    
    Args:
        database_id: The ID of the database to query
        filter: Filter conditions for rows
        sort: Sort configuration
        start_cursor: Pagination cursor for next page
        page_size: Number of results per page (1-100)
        
    Returns:
        Object with 'results' array of rows and pagination info
    """
    payload = {"page_size": page_size}
    
    if filter:
        payload["filter"] = filter
        
    if sort:
        payload["sorts"] = [sort] if isinstance(sort, dict) else sort
        
    if start_cursor:
        payload["start_cursor"] = start_cursor
        
    return _request("POST", f"/databases/{database_id}/query", json=payload)


@mcp.tool()
def create_database(
    parent_page_id: str,
    title: str,
    properties: dict = None,
) -> dict:
    """Create a new database as a child of a page.
    
    Args:
        parent_page_id: The ID of the parent page
        title: The title for the database
        properties: Database properties schema (column definitions)
        
    Returns:
        The created database object
    """
    payload = {
        "parent": {"page_id": parent_page_id},
        "title": [{"text": {"content": title}}],
        "properties": properties or {},
    }
    
    return _request("POST", "/databases", json=payload)


@mcp.tool()
def update_database(
    database_id: str,
    properties: dict = None,
    cover: str = None,
    icon: str = None,
) -> dict:
    """Update properties of an existing database.
    
    Args:
        database_id: The ID of the database to update
        properties: Database properties schema to update
        cover: URL of the cover image
        icon: URL or emoji for the database icon
        
    Returns:
        The updated database object
    """
    payload = {}
    
    if properties:
        payload["properties"] = properties
        
    if cover:
        payload["cover"] = {"type": "external", "external": {"url": cover}}
        
    if icon:
        if icon.startswith(":") and icon.endswith(":"):
            payload["icon"] = {"type": "emoji", "emoji": icon.strip(":")}
        else:
            payload["icon"] = {"type": "external", "external": {"url": icon}}
            
    return _request("PATCH", f"/databases/{database_id}", json=payload)


# ==================== Block (Page Children) Tools ====================

@mcp.tool()
def get_block(block_id: str) -> dict:
    """Retrieve a block by ID.
    
    Args:
        block_id: The ID of the block to retrieve
        
    Returns:
        Block object with type-specific properties
    """
    return _request("GET", f"/blocks/{block_id}")


@mcp.tool()
def get_block_children(block_id: str, start_cursor: str = None, page_size: int = 100) -> dict:
    """Get all child blocks of a parent block.
    
    Args:
        block_id: The ID of the parent block
        start_cursor: Pagination cursor for next page
        page_size: Number of results per page (1-100)
        
    Returns:
        Object with 'results' array of child blocks
    """
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def append_block_children(
    block_id: str,
    children: list,
) -> dict:
    """Append new child blocks to a parent block.
    
    Args:
        block_id: The ID of the parent block
        children: List of block objects to append
        
    Returns:
        Object with updated children array
    """
    payload = {"children": children}
    return _request("PATCH", f"/blocks/{block_id}/children", json=payload)


@mcp.tool()
def update_block(
    block_id: str,
    text: str = None,
    archived: bool = None,
    **kwargs,
) -> dict:
    """Update a block's properties.
    
    Args:
        block_id: The ID of the block to update
        text: New text content for the block
        archived: Whether to archive the block
        **kwargs: Additional block-specific properties
        
    Returns:
        The updated block object
    """
    payload = {}
    
    if text is not None:
        # For paragraph blocks, update the text property
        if "paragraph" not in kwargs:
            kwargs["paragraph"] = {"rich_text": [{"type": "text", "text": {"content": text}}]}
            
    if archived is not None:
        payload["archived"] = archived
        
    payload.update(kwargs)
    
    return _request("PATCH", f"/blocks/{block_id}", json=payload)


@mcp.tool()
def delete_block(block_id: str) -> dict:
    """Delete a block.
    
    Args:
        block_id: The ID of the block to delete
        
    Returns:
        Deletion confirmation
    """
    # Notion API marks blocks as archived rather than truly deleting
    return _request("PATCH", f"/blocks/{block_id}", json={"archived": True})


# ==================== Comment Tools ====================

@mcp.tool()
def create_comment(
    parent_id: str,
    text: str,
    property_name: str = None,
) -> dict:
    """Create a comment on a page or database.
    
    Args:
        parent_id: The ID of the page/database to comment on
        text: The comment text
        property_name: Optional property name for property comments
        
    Returns:
        The created comment object
    """
    payload = {
        "parent": {"page_id": parent_id},
        "rich_text": [{"type": "text", "text": {"content": text}}],
    }
    
    if property_name:
        payload["property"] = property_name
        
    return _request("POST", "/comments", json=payload)


@mcp.tool()
def list_comments(
    page_id: str,
    start_cursor: str = None,
    page_size: int = 10,
) -> dict:
    """List comments on a page.
    
    Args:
        page_id: The ID of the page to list comments for
        start_cursor: Pagination cursor for next page
        page_size: Number of results per page (1-100)
        
    Returns:
        Object with 'results' array of comments
    """
    params = {"page_id": page_id, "page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _request("GET", "/comments", params=params)


# ==================== Utility Tools ====================

@mcp.tool()
def list_blocks_recursive(
    block_id: str,
    max_depth: int = 3,
) -> dict:
    """Recursively list all blocks under a parent block up to a certain depth.
    
    Args:
        block_id: The ID of the parent block
        max_depth: Maximum recursion depth
        
    Returns:
        Nested structure of blocks
    """
    result = {"blocks": [], "depth": 0}
    
    def _fetch_blocks(current_id: str, current_depth: int, acc: dict):
        if current_depth >= max_depth:
            return
            
        response = get_block_children(current_id)
        if "error" in response:
            return
            
        blocks = response.get("results", [])
        acc["blocks"].extend(blocks)
        
        # Find collapsible/parent blocks for recursive fetch
        for block in blocks:
            block_type = block.get("type", "")
            has_children = block.get(f"{block_type}", {}).get("has_children", False)
            
            if has_children and current_depth < max_depth - 1:
                child_block_id = block.get("id")
                if child_block_id:
                    _fetch_blocks(child_block_id, current_depth + 1, acc)
    
    _fetch_blocks(block_id, 0, result)
    return result


if __name__ == "__main__":
    mcp.run()
