#!/usr/bin/env python3
"""MCP Server for Notion API"""

import os
import sys
from typing import Any, Dict, List, Optional

import requests
from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("notion")

# Configuration
NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_VERSION = "2026-03-11"
BASE_URL = "https://api.notion.com/v1"


def _make_request(method: str, endpoint: str, params: Optional[Dict] = None, 
                  json_data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make a request to the Notion API with proper authentication."""
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_data,
            timeout=30
        )
        
        # Handle response
        if response.status_code >= 200 and response.status_code < 300:
            return response.json() if response.content else {"success": True}
        else:
            # Return error info as dict
            try:
                error_data = response.json()
                return {"error": error_data.get("message", "Unknown error"), 
                        "status_code": response.status_code}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}", 
                        "status_code": response.status_code}
                
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ========== Page Endpoints ==========

@mcp.tool()
def retrieve_page(page_id: str) -> Dict[str, Any]:
    """Retrieve a page by its ID.
    
    Args:
        page_id: The ID of the page to retrieve.
        
    Returns:
        Page object or error dict.
    """
    return _make_request("GET", f"/pages/{page_id}")


@mcp.tool()
def create_page(parent: Dict[str, Any], properties: Dict[str, Any], 
                children: Optional[List[Dict[str, Any]]] = None,
                cover: Optional[Dict[str, Any]] = None,
                icon: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a new page.
    
    Args:
        parent: Parent object with type and ID.
        properties: Page properties.
        children: Optional list of block children to create with the page.
        cover: Optional cover image.
        icon: Optional page icon.
        
    Returns:
        Created page object or error dict.
    """
    data = {
        "parent": parent,
        "properties": properties,
    }
    
    if children:
        data["children"] = children
    if cover:
        data["cover"] = cover
    if icon:
        data["icon"] = icon
        
    return _make_request("POST", "/pages", json_data=data)


@mcp.tool()
def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None,
                in_trash: Optional[bool] = None,
                locked: Optional[bool] = None,
                icon: Optional[Dict[str, Any]] = None,
                cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update a page.
    
    Args:
        page_id: The ID of the page to update.
        properties: Page properties to update.
        in_trash: Whether to move the page to trash.
        locked: Whether to lock the page from editing.
        icon: New icon for the page.
        cover: New cover image for the page.
        
    Returns:
        Updated page object or error dict.
    """
    data = {}
    
    if properties is not None:
        data["properties"] = properties
    if in_trash is not None:
        data["in_trash"] = in_trash
    if locked is not None:
        data["is_locked"] = locked
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
        
    return _make_request("PATCH", f"/pages/{page_id}", json_data=data)


@mcp.tool()
def move_page(page_id: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """Move a page to a new parent.
    
    Args:
        page_id: The ID of the page to move.
        parent: New parent object (page_id or data_source_id).
        
    Returns:
        Updated page object or error dict.
    """
    return _make_request("POST", f"/pages/{page_id}/move", 
                         json_data={"parent": parent})


@mcp.tool()
def archive_page(page_id: str) -> Dict[str, Any]:
    """Archive (move to trash) a page.
    
    Args:
        page_id: The ID of the page to archive.
        
    Returns:
        Updated page object or error dict.
    """
    return _make_request("PATCH", f"/pages/{page_id}", 
                         json_data={"in_trash": True})


@mcp.tool()
def restore_page(page_id: str) -> Dict[str, Any]:
    """Restore a page from trash.
    
    Args:
        page_id: The ID of the page to restore.
        
    Returns:
        Updated page object or error dict.
    """
    return _make_request("PATCH", f"/pages/{page_id}", 
                         json_data={"in_trash": False})


@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str) -> Dict[str, Any]:
    """Retrieve a specific page property.
    
    Args:
        page_id: The ID of the page.
        property_id: The ID of the property to retrieve.
        
    Returns:
        Property item object or error dict.
    """
    return _make_request("GET", f"/pages/{page_id}/properties/{property_id}")


# ========== Database Endpoints ==========

@mcp.tool()
def retrieve_database(database_id: str) -> Dict[str, Any]:
    """Retrieve a database by its ID.
    
    Args:
        database_id: The ID of the database to retrieve.
        
    Returns:
        Database object or error dict.
    """
    return _make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def query_database(database_id: str, filter_conditions: Optional[Dict[str, Any]] = None,
                   sorts: Optional[List[Dict[str, Any]]] = None,
                   start_cursor: Optional[str] = None,
                   page_size: int = 100) -> Dict[str, Any]:
    """Query a database with optional filters and sorts.
    
    Args:
        database_id: The ID of the database to query.
        filter_conditions: Filter conditions for the query.
        sorts: Sort order for the results.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page (max 100).
        
    Returns:
        Query results with pagination info or error dict.
    """
    data = {"page_size": page_size}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
        
    return _make_request("POST", f"/databases/{database_id}/query", json_data=data)


@mcp.tool()
def create_database(parent: Dict[str, Any], title: List[Dict[str, Any]], 
                    properties: Optional[Dict[str, Any]] = None,
                    icon: Optional[Dict[str, Any]] = None,
                    cover: Optional[Dict[str, Any]] = None,
                    is_inline: bool = False) -> Dict[str, Any]:
    """Create a new database.
    
    Args:
        parent: Parent object (page or workspace).
        title: Database title as rich text array.
        properties: Initial property schema.
        icon: Database icon.
        cover: Database cover image.
        is_inline: Whether to display inline.
        
    Returns:
        Created database object or error dict.
    """
    data = {
        "parent": parent,
        "title": title,
        "is_inline": is_inline,
    }
    
    if properties:
        data["properties"] = properties
    if icon:
        data["icon"] = icon
    if cover:
        data["cover"] = cover
        
    return _make_request("POST", "/databases", json_data=data)


@mcp.tool()
def update_database(database_id: str, title: Optional[List[Dict[str, Any]]] = None,
                    description: Optional[List[Dict[str, Any]]] = None,
                    icon: Optional[Dict[str, Any]] = None,
                    cover: Optional[Dict[str, Any]] = None,
                    in_trash: Optional[bool] = None,
                    locked: Optional[bool] = None,
                    properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update a database.
    
    Args:
        database_id: The ID of the database to update.
        title: Updated title.
        description: Updated description.
        icon: New icon.
        cover: New cover image.
        in_trash: Whether to move to trash.
        locked: Whether to lock the database.
        
    Returns:
        Updated database object or error dict.
    """
    data = {}
    
    if title is not None:
        data["title"] = title
    if description is not None:
        data["description"] = description
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
    if in_trash is not None:
        data["in_trash"] = in_trash
    if locked is not None:
        data["is_locked"] = locked
    if properties is not None:
        data["properties"] = properties
        
    return _make_request("PATCH", f"/databases/{database_id}", json_data=data)


# ========== Block Endpoints ==========

@mcp.tool()
def retrieve_block(block_id: str) -> Dict[str, Any]:
    """Retrieve a block by its ID.
    
    Args:
        block_id: The ID of the block to retrieve.
        
    Returns:
        Block object or error dict.
    """
    return _make_request("GET", f"/blocks/{block_id}")


@mcp.tool()
def update_block(block_id: str, **kwargs) -> Dict[str, Any]:
    """Update a block.
    
    Args:
        block_id: The ID of the block to update.
        **kwargs: Block type-specific fields to update.
        
    Returns:
        Updated block object or error dict.
    """
    # Extract supported update fields
    data = {}
    
    # Handle common fields
    if "in_trash" in kwargs:
        data["in_trash"] = kwargs["in_trash"]
    if "is_locked" in kwargs:
        data["is_locked"] = kwargs["is_locked"]
        
    # Handle block type-specific content
    for key, value in kwargs.items():
        if key not in ["in_trash", "is_locked"]:
            data[key] = value
            
    return _make_request("PATCH", f"/blocks/{block_id}", json_data=data)


@mcp.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    """Delete (archive) a block.
    
    Args:
        block_id: The ID of the block to delete.
        
    Returns:
        Deleted block object or error dict.
    """
    return _make_request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def append_block_children(block_id: str, children: List[Dict[str, Any]],
                          after: Optional[str] = None) -> Dict[str, Any]:
    """Append child blocks to a parent block.
    
    Args:
        block_id: The ID of the parent block.
        children: List of child blocks to append.
        after: Optional block ID to insert after.
        
    Returns:
        Append results or error dict.
    """
    data = {"children": children}
    
    if after:
        data["position"] = {"type": "after_block", "after_block": {"id": after}}
    else:
        data["position"] = {"type": "end"}
        
    return _make_request("PATCH", f"/blocks/{block_id}/children", json_data=data)


@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: Optional[str] = None,
                            page_size: int = 100) -> Dict[str, Any]:
    """Retrieve child blocks of a parent block.
    
    Args:
        block_id: The ID of the parent block.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page.
        
    Returns:
        Block children list or error dict.
    """
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _make_request("GET", f"/blocks/{block_id}/children", params=params)


# ========== Comment Endpoints ==========

@mcp.tool()
def retrieve_comment(comment_id: str) -> Dict[str, Any]:
    """Retrieve a comment by its ID.
    
    Args:
        comment_id: The ID of the comment to retrieve.
        
    Returns:
        Comment object or error dict.
    """
    return _make_request("GET", f"/comments/{comment_id}")


@mcp.tool()
def create_comment(parent: Dict[str, Any], rich_text: List[Dict[str, Any]],
                   attachments: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Create a comment.
    
    Args:
        parent: Parent object (page or block).
        rich_text: Comment content as rich text.
        attachments: Optional file attachments.
        
    Returns:
        Created comment or error dict.
    """
    data = {
        "parent": parent,
        "rich_text": rich_text,
    }
    
    if attachments:
        data["attachments"] = attachments
        
    return _make_request("POST", "/comments", json_data=data)


@mcp.tool()
def list_comments(block_id: str, start_cursor: Optional[str] = None,
                  page_size: int = 100) -> Dict[str, Any]:
    """List comments on a block or page.
    
    Args:
        block_id: The ID of the block or page.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page.
        
    Returns:
        Comments list or error dict.
    """
    params = {"block_id": block_id, "page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _make_request("GET", "/comments", params=params)


# ========== User Endpoints ==========

@mcp.tool()
def list_users(start_cursor: Optional[str] = None,
               page_size: int = 100) -> Dict[str, Any]:
    """List all users in the workspace.
    
    Args:
        start_cursor: Cursor for pagination.
        page_size: Number of results per page.
        
    Returns:
        Users list or error dict.
    """
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _make_request("GET", "/users", params=params)


@mcp.tool()
def retrieve_user(user_id: str) -> Dict[str, Any]:
    """Retrieve a user by ID.
    
    Args:
        user_id: The ID of the user to retrieve.
        
    Returns:
        User object or error dict.
    """
    return _make_request("GET", f"/users/{user_id}")


@mcp.tool()
def retrieve_my_bot() -> Dict[str, Any]:
    """Retrieve the bot user associated with the current token.
    
    Returns:
        Bot user object or error dict.
    """
    return _make_request("GET", "/users/me")


# ========== View Endpoints ==========

@mcp.tool()
def retrieve_view(view_id: str) -> Dict[str, Any]:
    """Retrieve a view by its ID.
    
    Args:
        view_id: The ID of the view to retrieve.
        
    Returns:
        View object or error dict.
    """
    return _make_request("GET", f"/views/{view_id}")


@mcp.tool()
def list_views(database_id: Optional[str] = None, data_source_id: Optional[str] = None,
               start_cursor: Optional[str] = None,
               page_size: int = 100) -> Dict[str, Any]:
    """List views in a database or data source.
    
    Args:
        database_id: The ID of the database to list views for.
        data_source_id: The ID of the data source to list views for.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page.
        
    Returns:
        Views list or error dict.
    """
    params = {"page_size": page_size}
    
    if database_id:
        params["database_id"] = database_id
    if data_source_id:
        params["data_source_id"] = data_source_id
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _make_request("GET", "/views", params=params)


# ========== Search Endpoints ==========

@mcp.tool()
def search(query: Optional[str] = None, 
           filter_conditions: Optional[Dict[str, Any]] = None,
           sorts: Optional[List[Dict[str, Any]]] = None,
           start_cursor: Optional[str] = None,
           page_size: int = 100) -> Dict[str, Any]:
    """Search pages and databases.
    
    Args:
        query: Search query string.
        filter_conditions: Filter to narrow results.
        sorts: Sort order for results.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page.
        
    Returns:
        Search results or error dict.
    """
    data = {"page_size": page_size}
    
    if query is not None:
        data["query"] = query
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
        
    return _make_request("POST", "/search", json_data=data)


# ========== Utility Endpoints ==========

@mcp.tool()
def get_databases(start_cursor: Optional[str] = None,
                  page_size: int = 100) -> Dict[str, Any]:
    """List all databases.
    
    Args:
        start_cursor: Cursor for pagination.
        page_size: Number of results per page.
        
    Returns:
        Databases list or error dict.
    """
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return _make_request("GET", "/databases", params=params)


if __name__ == "__main__":
    mcp.run()
