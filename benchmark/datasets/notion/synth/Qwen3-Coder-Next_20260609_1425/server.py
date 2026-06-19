#!/usr/bin/env python3
"""MCP server for Notion API."""

import os
import json
import requests
from typing import Any

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("notion")

# Base URL for Notion API
NOTION_API_BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

# Authentication header
AUTH_HEADERS = {
    "Authorization": f"Bearer {os.getenv('NOTION_API_KEY')}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}


def make_request(method: str, endpoint: str, params: dict = None, data: dict = None) -> dict:
    """Make a request to the Notion API."""
    url = f"{NOTION_API_BASE_URL}{endpoint}"
    headers = AUTH_HEADERS.copy()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=30
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            return {"error": f"API error: {response.status_code} - {response.text}"}
            
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


# ==================== Page Endpoints ====================

@mcp.tool()
def create_page(parent_id: str, parent_type: str, properties: dict, content: str = None) -> dict:
    """
    Create a new page in Notion.
    
    Args:
        parent_id: ID of the parent page or database
        parent_type: Type of parent ('page_id' or 'data_source_id')
        properties: Page property values
        content: Optional page content as Markdown
    
    Returns:
        Created page object
    """
    data = {
        "parent": {
            "type": parent_type,
            parent_type: parent_id
        },
        "properties": properties
    }
    
    if content:
        data["content"] = content
    
    return make_request("POST", "/pages", data=data)


@mcp.tool()
def retrieve_page(page_id: str) -> dict:
    """
    Retrieve a page by ID.
    
    Args:
        page_id: ID of the page to retrieve
    
    Returns:
        Page object
    """
    return make_request("GET", f"/pages/{page_id}")


@mcp.tool()
def update_page(page_id: str, properties: dict = None, icon: dict = None, cover: dict = None, 
                in_trash: bool = None, locked: bool = None) -> dict:
    """
    Update a page's properties, icon, cover, or trash status.
    
    Args:
        page_id: ID of the page to update
        properties: Updated property values
        icon: Updated icon object
        cover: Updated cover object
        in_trash: Whether to move to trash (True) or restore (False)
        locked: Whether to lock the page from editing
    
    Returns:
        Updated page object
    """
    data = {}
    
    if properties is not None:
        data["properties"] = properties
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
    if in_trash is not None:
        data["in_trash"] = in_trash
    if locked is not None:
        data["is_locked"] = locked
    
    return make_request("PATCH", f"/pages/{page_id}", data=data)


@mcp.tool()
def trash_page(page_id: str) -> dict:
    """
    Move a page to the trash.
    
    Args:
        page_id: ID of the page to trash
    
    Returns:
        Updated page object
    """
    return update_page(page_id, in_trash=True)


@mcp.tool()
def restore_page(page_id: str) -> dict:
    """
    Restore a trashed page.
    
    Args:
        page_id: ID of the page to restore
    
    Returns:
        Updated page object
    """
    return update_page(page_id, in_trash=False)


@mcp.tool()
def move_page(page_id: str, new_parent_id: str, new_parent_type: str = "page_id") -> dict:
    """
    Move a page to a new parent.
    
    Args:
        page_id: ID of the page to move
        new_parent_id: ID of the new parent
        new_parent_type: Type of new parent ('page_id' or 'data_source_id')
    
    Returns:
        Updated page object
    """
    data = {
        "parent": {
            "type": new_parent_type,
            new_parent_type: new_parent_id
        }
    }
    
    return make_request("POST", f"/pages/{page_id}/move", data=data)


@mcp.tool()
def retrieve_page_markdown(page_id: str, include_transcripts: bool = False) -> dict:
    """
    Retrieve a page's content as Markdown.
    
    Args:
        page_id: ID of the page
        include_transcripts: Whether to include meeting note transcripts
    
    Returns:
        Page content as Markdown
    """
    params = {"include_transcripts": str(include_transcripts).lower()}
    return make_request("GET", f"/pages/{page_id}/markdown", params=params)


@mcp.tool()
def update_page_markdown(page_id: str, update_type: str = "update_content", 
                         content_updates: list = None) -> dict:
    """
    Update a page's content using Markdown operations.
    
    Args:
        page_id: ID of the page
        update_type: Type of update ('insert_content', 'update_content')
        content_updates: List of content update operations
    
    Returns:
        Updated page content
    """
    data = {
        "type": update_type
    }
    
    if content_updates:
        data["content_updates"] = content_updates
    
    return make_request("PATCH", f"/pages/{page_id}/markdown", data=data)


@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str) -> dict:
    """
    Retrieve a specific property from a page.
    
    Args:
        page_id: ID of the page
        property_id: ID of the property
    
    Returns:
        Property item object
    """
    return make_request("GET", f"/pages/{page_id}/properties/{property_id}")


# ==================== Database Endpoints ====================

@mcp.tool()
def create_database(parent_id: str, parent_type: str, title: list = None, 
                   description: list = None, icon: dict = None, cover: dict = None,
                   properties: dict = None, is_inline: bool = None) -> dict:
    """
    Create a new database in Notion.
    
    Args:
        parent_id: ID of the parent page
        parent_type: Type of parent ('page_id' or 'workspace')
        title: Database title
        description: Database description
        icon: Database icon
        cover: Database cover
        properties: Initial property schema
        is_inline: Whether to display inline
    
    Returns:
        Created database object
    """
    data = {
        "parent": {
            "type": parent_type,
            parent_type: parent_id
        }
    }
    
    if title:
        data["title"] = title
    if description:
        data["description"] = description
    if icon:
        data["icon"] = icon
    if cover:
        data["cover"] = cover
    if properties:
        data["properties"] = properties
    if is_inline is not None:
        data["is_inline"] = is_inline
    
    return make_request("POST", "/databases", data=data)


@mcp.tool()
def retrieve_database(database_id: str) -> dict:
    """
    Retrieve a database by ID.
    
    Args:
        database_id: ID of the database
    
    Returns:
        Database object
    """
    return make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def update_database(database_id: str, title: list = None, description: list = None,
                   icon: dict = None, cover: dict = None, in_trash: bool = None,
                   locked: bool = None, parent_id: str = None, parent_type: str = None) -> dict:
    """
    Update a database's properties.
    
    Args:
        database_id: ID of the database
        title: Updated title
        description: Updated description
        icon: Updated icon
        cover: Updated cover
        in_trash: Whether to move to trash
        locked: Whether to lock the database
        parent_id: New parent ID (for moving)
        parent_type: New parent type
    
    Returns:
        Updated database object
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
    
    if parent_id is not None and parent_type is not None:
        data["parent"] = {
            "type": parent_type,
            parent_type: parent_id
        }
    
    return make_request("PATCH", f"/databases/{database_id}", data=data)


@mcp.tool()
def query_database(database_id: str, filter_conditions: dict = None, sorts: list = None,
                  start_cursor: str = None, page_size: int = 100) -> dict:
    """
    Query a database with filters and sorts.
    
    Args:
        database_id: ID of the database
        filter_conditions: Filter conditions
        sorts: Sort configurations
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    data = {}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", f"/databases/{database_id}/query", data=data)


@mcp.tool()
def list_databases(start_cursor: str = None, page_size: int = 100) -> dict:
    """
    List databases accessible to the integration.
    
    Args:
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of databases
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/databases", params=params)


# ==================== Block Endpoints ====================

@mcp.tool()
def retrieve_block(block_id: str) -> dict:
    """
    Retrieve a block by ID.
    
    Args:
        block_id: ID of the block
    
    Returns:
        Block object
    """
    return make_request("GET", f"/blocks/{block_id}")


@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: str = None, 
                           page_size: int = 100) -> dict:
    """
    Retrieve a block's children.
    
    Args:
        block_id: ID of the parent block
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of child blocks
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def append_block_children(parent_block_id: str, children: list, 
                         position: dict = None) -> dict:
    """
    Append new blocks as children of an existing block.
    
    Args:
        parent_block_id: ID of the parent block
        children: List of child block objects
        position: Position object for insertion (start, end, or after_block)
    
    Returns:
        Updated block children
    """
    data = {"children": children}
    
    if position:
        data["position"] = position
    
    return make_request("PATCH", f"/blocks/{parent_block_id}/children", data=data)


@mcp.tool()
def update_block(block_id: str, **kwargs) -> dict:
    """
    Update a block's properties.
    
    Args:
        block_id: ID of the block
        **kwargs: Block type-specific properties to update
    
    Returns:
        Updated block object
    """
    return make_request("PATCH", f"/blocks/{block_id}", data=kwargs)


@mcp.tool()
def delete_block(block_id: str) -> dict:
    """
    Delete a block.
    
    Args:
        block_id: ID of the block to delete
    
    Returns:
        Deleted block object
    """
    # Notion doesn't have a direct DELETE endpoint for blocks
    # Use the update endpoint to set in_trash=true
    return update_block(block_id, in_trash=True)


# ==================== Comment Endpoints ====================

@mcp.tool()
def create_comment(parent_id: str, parent_type: str, rich_text: list, 
                  attachments: list = None, display_name: str = None) -> dict:
    """
    Create a comment on a page or block.
    
    Args:
        parent_id: ID of the parent page or block
        parent_type: Type of parent ('page_id' or 'block_id')
        rich_text: Comment content as rich text
        attachments: Optional file attachments
        display_name: Optional display name for the comment
    
    Returns:
        Created comment object
    """
    data = {
        "parent": {
            "type": parent_type,
            parent_type: parent_id
        },
        "rich_text": rich_text
    }
    
    if attachments:
        data["attachments"] = attachments
    if display_name:
        data["display_name"] = display_name
    
    return make_request("POST", "/comments", data=data)


@mcp.tool()
def retrieve_comment(comment_id: str) -> dict:
    """
    Retrieve a comment by ID.
    
    Args:
        comment_id: ID of the comment
    
    Returns:
        Comment object
    """
    return make_request("GET", f"/comments/{comment_id}")


@mcp.tool()
def list_comments(block_id: str, start_cursor: str = None, page_size: int = 100) -> dict:
    """
    List comments on a block.
    
    Args:
        block_id: ID of the block
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of comments
    """
    params = {"block_id": block_id}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/comments", params=params)


# ==================== User Endpoints ====================

@mcp.tool()
def list_users(start_cursor: str = None, page_size: int = 100) -> dict:
    """
    List all users in the workspace.
    
    Args:
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of users
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/users", params=params)


@mcp.tool()
def retrieve_user(user_id: str) -> dict:
    """
    Retrieve a user by ID.
    
    Args:
        user_id: ID of the user
    
    Returns:
        User object
    """
    return make_request("GET", f"/users/{user_id}")


@mcp.tool()
def retrieve_my_user() -> dict:
    """
    Retrieve the user associated with the current token.
    
    Returns:
        User object for the bot
    """
    return make_request("GET", "/users/me")


# ==================== Search Endpoints ====================

@mcp.tool()
def search(query: str = None, filter_property: str = "object", 
          filter_value: str = None, sort_direction: str = "descending",
          sort_timestamp: str = "last_edited_time", start_cursor: str = None,
          page_size: int = 100) -> dict:
    """
    Search for pages, databases, and other items in the workspace.
    
    Args:
        query: Search query string
        filter_property: Property to filter on (default: 'object')
        filter_value: Value to filter for
        sort_direction: Sort direction ('ascending' or 'descending')
        sort_timestamp: Timestamp to sort by ('created_time' or 'last_edited_time')
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Search results
    """
    data = {
        "sort": {
            "direction": sort_direction,
            "timestamp": sort_timestamp
        }
    }
    
    if query:
        data["query"] = query
    
    if filter_property and filter_value:
        data["filter"] = {
            "property": filter_property,
            "value": filter_value
        }
    
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", "/search", data=data)


# ==================== View Endpoints ====================

@mcp.tool()
def create_view(database_id: str = None, data_source_id: str = None, name: str = None,
               view_type: str = None, filter_conditions: dict = None, sorts: list = None,
               quick_filters: dict = None, view_id: str = None, create_database: bool = False,
               presentation_config: dict = None, position: str = "end",
               insert_at: str = None) -> dict:
    """
    Create a new view in a database or dashboard.
    
    Args:
        database_id: ID of the database to create the view in
        data_source_id: ID of the data source
        name: Name of the view
        view_type: Type of view ('table', 'board', 'calendar', etc.)
        filter_conditions: Initial filter conditions
        sorts: Initial sort configurations
        quick_filters: Quick filter configurations
        view_id: ID of an existing dashboard to add the view to
        create_database: Whether to create a linked database
        presentation_config: View presentation settings
        position: Position in view tab bar ('start' or 'end')
        insert_at: Position in dashboard row
    
    Returns:
        Created view object
    """
    data = {}
    
    if name:
        data["name"] = name
    if view_type:
        data["type"] = view_type
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if quick_filters:
        data["quick_filters"] = quick_filters
    
    if presentation_config:
        data["presentation"] = presentation_config
    
    if position:
        data["position"] = position
    
    if insert_at:
        data["insert_at"] = insert_at
    
    endpoint = "/views"
    params = {}
    
    if database_id:
        params["database_id"] = database_id
    elif data_source_id:
        params["data_source_id"] = data_source_id
    
    if view_id:
        params["view_id"] = view_id
    
    return make_request("POST", endpoint, params=params, data=data)


@mcp.tool()
def retrieve_view(view_id: str) -> dict:
    """
    Retrieve a view by ID.
    
    Args:
        view_id: ID of the view
    
    Returns:
        View object
    """
    return make_request("GET", f"/views/{view_id}")


@mcp.tool()
def update_view(view_id: str, name: str = None, filter_conditions: dict = None,
               sorts: list = None, quick_filters: dict = None,
               presentation_config: dict = None) -> dict:
    """
    Update a view's properties.
    
    Args:
        view_id: ID of the view
        name: New name for the view
        filter_conditions: New filter conditions (null to clear)
        sorts: New sort configurations (null to clear)
        quick_filters: New quick filters (null to clear)
        presentation_config: New presentation config (null to clear)
    
    Returns:
        Updated view object
    """
    data = {}
    
    if name is not None:
        data["name"] = name
    if filter_conditions is not None:
        data["filter"] = filter_conditions
    if sorts is not None:
        data["sorts"] = sorts
    if quick_filters is not None:
        data["quick_filters"] = quick_filters
    if presentation_config is not None:
        data["presentation"] = presentation_config
    
    return make_request("PATCH", f"/views/{view_id}", data=data)


@mcp.tool()
def delete_view(view_id: str) -> dict:
    """
    Delete a view.
    
    Args:
        view_id: ID of the view to delete
    
    Returns:
        Deleted view object
    """
    return make_request("DELETE", f"/views/{view_id}")


@mcp.tool()
def list_views(database_id: str = None, data_source_id: str = None,
              start_cursor: str = None, page_size: int = 100) -> dict:
    """
    List views for a database or data source.
    
    Args:
        database_id: ID of the database
        data_source_id: ID of the data source
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of views
    """
    params = {}
    if database_id:
        params["database_id"] = database_id
    if data_source_id:
        params["data_source_id"] = data_source_id
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/views", params=params)


# ==================== View Query Endpoints ====================

@mcp.tool()
def create_view_query(view_id: str, page_size: int = 100) -> dict:
    """
    Create a view query.
    
    Args:
        view_id: ID of the view
        page_size: Number of results per page (max 100)
    
    Returns:
        Created query object
    """
    data = {"page_size": page_size}
    return make_request("POST", f"/views/{view_id}/queries", data=data)


@mcp.tool()
def get_view_query_results(view_id: str, query_id: str, start_cursor: str = None,
                          page_size: int = 100) -> dict:
    """
    Get results for a view query.
    
    Args:
        view_id: ID of the view
        query_id: ID of the query
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", f"/views/{view_id}/queries/{query_id}/results", params=params)


@mcp.tool()
def delete_view_query(view_id: str, query_id: str) -> dict:
    """
    Delete a view query.
    
    Args:
        view_id: ID of the view
        query_id: ID of the query
    
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/views/{view_id}/queries/{query_id}")


# ==================== Data Source Endpoints ====================

@mcp.tool()
def create_data_source(parent_id: str, parent_type: str = "database_id",
                      title: list = None, properties: dict = None,
                      icon: dict = None, cover: dict = None) -> dict:
    """
    Create a new data source.
    
    Args:
        parent_id: ID of the parent database
        parent_type: Type of parent ('database_id')
        title: Title of the data source
        properties: Initial property schema
        icon: Data source icon
        cover: Data source cover
    
    Returns:
        Created data source object
    """
    data = {
        "parent": {
            "type": parent_type,
            parent_type: parent_id
        }
    }
    
    if title:
        data["title"] = title
    if properties:
        data["properties"] = properties
    if icon:
        data["icon"] = icon
    if cover:
        data["cover"] = cover
    
    return make_request("POST", "/data_sources", data=data)


@mcp.tool()
def retrieve_data_source(data_source_id: str) -> dict:
    """
    Retrieve a data source by ID.
    
    Args:
        data_source_id: ID of the data source
    
    Returns:
        Data source object
    """
    return make_request("GET", f"/data_sources/{data_source_id}")


@mcp.tool()
def update_data_source(data_source_id: str, title: list = None, 
                      properties: dict = None, in_trash: bool = None,
                      parent_id: str = None, parent_type: str = None) -> dict:
    """
    Update a data source's properties.
    
    Args:
        data_source_id: ID of the data source
        title: Updated title
        properties: Updated property schema (null to remove)
        in_trash: Whether to move to trash
        parent_id: New parent ID (for moving)
        parent_type: New parent type
    
    Returns:
        Updated data source object
    """
    data = {}
    
    if title is not None:
        data["title"] = title
    if properties is not None:
        data["properties"] = properties
    if in_trash is not None:
        data["in_trash"] = in_trash
    
    if parent_id is not None and parent_type is not None:
        data["parent"] = {
            "type": parent_type,
            parent_type: parent_id
        }
    
    return make_request("PATCH", f"/data_sources/{data_source_id}", data=data)


@mcp.tool()
def query_data_source(data_source_id: str, filter_conditions: dict = None,
                     sorts: list = None, start_cursor: str = None,
                     page_size: int = 100) -> dict:
    """
    Query a data source with filters and sorts.
    
    Args:
        data_source_id: ID of the data source
        filter_conditions: Filter conditions
        sorts: Sort configurations
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    data = {}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", f"/data_sources/{data_source_id}/query", data=data)


@mcp.tool()
def list_data_source_templates(data_source_id: str, name_filter: str = None,
                               start_cursor: str = None, page_size: int = 100) -> dict:
    """
    List templates for a data source.
    
    Args:
        data_source_id: ID of the data source
        name_filter: Filter templates by name
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of templates
    """
    params = {}
    if name_filter:
        params["name"] = name_filter
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", f"/data_sources/{data_source_id}/templates", params=params)


@mcp.tool()
def update_data_source_properties(data_source_id: str, properties: dict) -> dict:
    """
    Update data source property schema.
    
    Args:
        data_source_id: ID of the data source
        properties: Property schema updates (null to remove properties)
    
    Returns:
        Updated data source object
    """
    data = {"properties": properties}
    return make_request("PATCH", f"/data_sources/{data_source_id}/properties", data=data)


# ==================== File Upload Endpoints ====================

@mcp.tool()
def create_file_upload(mode: str = "single_part", filename: str = None,
                      content_type: str = None, number_of_parts: int = None,
                      external_url: str = None) -> dict:
    """
    Create a file upload session.
    
    Args:
        mode: Upload mode ('single_part', 'multi_part', 'external_url')
        filename: Name of the file
        content_type: MIME type of the file
        number_of_parts: Number of parts for multi-part upload
        external_url: URL for external file import
    
    Returns:
        File upload object
    """
    data = {"mode": mode}
    
    if filename:
        data["filename"] = filename
    if content_type:
        data["content_type"] = content_type
    if number_of_parts:
        data["number_of_parts"] = number_of_parts
    if external_url:
        data["external_url"] = external_url
    
    return make_request("POST", "/file_upload", data=data)


@mcp.tool()
def send_file_upload(file_upload_id: str, file_data: bytes, part_number: int = None) -> dict:
    """
    Send file data for upload.
    
    Args:
        file_upload_id: ID of the file upload
        file_data: Raw binary file content
        part_number: Part number for multi-part upload
    
    Returns:
        Updated file upload object
    """
    # This would typically be implemented with a direct upload
    # For MCP, we'll handle the logic but actual file upload would need special handling
    return {"error": "File upload requires direct HTTP request with binary data"}

@mcp.tool()
def complete_file_upload(file_upload_id: str) -> dict:
    """
    Complete a file upload session.
    
    Args:
        file_upload_id: ID of the file upload
    
    Returns:
        Completed file upload object
    """
    return make_request("POST", f"/file_uploads/{file_upload_id}/complete")


@mcp.tool()
def retrieve_file_upload(file_upload_id: str) -> dict:
    """
    Retrieve a file upload by ID.
    
    Args:
        file_upload_id: ID of the file upload
    
    Returns:
        File upload object
    """
    return make_request("GET", f"/file_uploads/{file_upload_id}")


@mcp.tool()
def list_file_uploads(status_filter: str = None, start_cursor: str = None,
                     page_size: int = 100) -> dict:
    """
    List file uploads.
    
    Args:
        status_filter: Filter by status
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        List of file uploads
    """
    params = {}
    if status_filter:
        params["status"] = status_filter
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/file_uploads", params=params)


# ==================== Tool Metadata ====================

@mcp.tool()
def query_data_source_with_filters(data_source_id: str, filter_conditions: dict = None,
                                   sorts: list = None, start_cursor: str = None,
                                   page_size: int = 100) -> dict:
    """
    Query a data source with filters and sorts.
    
    Args:
        data_source_id: ID of the data source
        filter_conditions: Filter conditions
        sorts: Sort configurations
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    data = {}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", f"/data_sources/{data_source_id}/query", data=data)


@mcp.tool()
def query_data_source_with_sorts(data_source_id: str, filter_conditions: dict = None,
                                  sorts: list = None, start_cursor: str = None,
                                  page_size: int = 100) -> dict:
    """
    Query a data source with sorts.
    
    Args:
        data_source_id: ID of the data source
        filter_conditions: Filter conditions
        sorts: Sort configurations
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    data = {}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", f"/data_sources/{data_source_id}/query", data=data)


@mcp.tool()
def query_database_with_filters(database_id: str, filter_conditions: dict = None,
                                sorts: list = None, start_cursor: str = None,
                                page_size: int = 100) -> dict:
    """
    Query a database with filters.
    
    Args:
        database_id: ID of the database
        filter_conditions: Filter conditions
        sorts: Sort configurations
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    data = {}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", f"/databases/{database_id}/query", data=data)


@mcp.tool()
def query_database_with_sorts(database_id: str, filter_conditions: dict = None,
                              sorts: list = None, start_cursor: str = None,
                              page_size: int = 100) -> dict:
    """
    Query a database with sorts.
    
    Args:
        database_id: ID of the database
        filter_conditions: Filter conditions
        sorts: Sort configurations
        start_cursor: Cursor for pagination
        page_size: Number of results per page (max 100)
    
    Returns:
        Query results
    """
    data = {}
    
    if filter_conditions:
        data["filter"] = filter_conditions
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    
    return make_request("POST", f"/databases/{database_id}/query", data=data)


@mcp.tool()
def get_tool_list() -> dict:
    """
    List all available tools in this MCP server.
    
    Returns:
        Dictionary of available tools with their documentation
    """
    tools = [
        {"name": "create_page", "description": "Create a new page in Notion"},
        {"name": "retrieve_page", "description": "Retrieve a page by ID"},
        {"name": "update_page", "description": "Update a page's properties"},
        {"name": "trash_page", "description": "Move a page to the trash"},
        {"name": "restore_page", "description": "Restore a trashed page"},
        {"name": "move_page", "description": "Move a page to a new parent"},
        {"name": "retrieve_page_markdown", "description": "Retrieve a page's content as Markdown"},
        {"name": "update_page_markdown", "description": "Update a page's content using Markdown operations"},
        {"name": "retrieve_page_property", "description": "Retrieve a specific property from a page"},
        {"name": "create_database", "description": "Create a new database"},
        {"name": "retrieve_database", "description": "Retrieve a database by ID"},
        {"name": "update_database", "description": "Update a database's properties"},
        {"name": "query_database", "description": "Query a database with filters and sorts"},
        {"name": "query_database_with_filters", "description": "Query a database with filters"},
        {"name": "query_database_with_sorts", "description": "Query a database with sorts"},
        {"name": "list_databases", "description": "List databases accessible to the integration"},
        {"name": "retrieve_block", "description": "Retrieve a block by ID"},
        {"name": "retrieve_block_children", "description": "Retrieve a block's children"},
        {"name": "append_block_children", "description": "Append new blocks as children of an existing block"},
        {"name": "update_block", "description": "Update a block's properties"},
        {"name": "delete_block", "description": "Delete a block (moves to trash)"},
        {"name": "create_comment", "description": "Create a comment on a page or block"},
        {"name": "retrieve_comment", "description": "Retrieve a comment by ID"},
        {"name": "list_comments", "description": "List comments on a block"},
        {"name": "list_users", "description": "List all users in the workspace"},
        {"name": "retrieve_user", "description": "Retrieve a user by ID"},
        {"name": "retrieve_my_user", "description": "Retrieve the user associated with the current token"},
        {"name": "search", "description": "Search for pages, databases, and other items"},
        {"name": "create_view", "description": "Create a new view in a database or dashboard"},
        {"name": "retrieve_view", "description": "Retrieve a view by ID"},
        {"name": "update_view", "description": "Update a view's properties"},
        {"name": "delete_view", "description": "Delete a view"},
        {"name": "list_views", "description": "List views for a database or data source"},
        {"name": "create_view_query", "description": "Create a view query"},
        {"name": "get_view_query_results", "description": "Get results for a view query"},
        {"name": "delete_view_query", "description": "Delete a view query"},
        {"name": "create_data_source", "description": "Create a new data source"},
        {"name": "retrieve_data_source", "description": "Retrieve a data source by ID"},
        {"name": "update_data_source", "description": "Update a data source's properties"},
        {"name": "query_data_source", "description": "Query a data source with filters and sorts"},
        {"name": "query_data_source_with_filters", "description": "Query a data source with filters"},
        {"name": "query_data_source_with_sorts", "description": "Query a data source with sorts"},
        {"name": "list_data_source_templates", "description": "List templates for a data source"},
        {"name": "update_data_source_properties", "description": "Update data source property schema"},
        {"name": "create_file_upload", "description": "Create a file upload session"},
        {"name": "send_file_upload", "description": "Send file data for upload"},
        {"name": "complete_file_upload", "description": "Complete a file upload session"},
        {"name": "retrieve_file_upload", "description": "Retrieve a file upload by ID"},
        {"name": "list_file_uploads", "description": "List file uploads"},
        {"name": "get_tool_list", "description": "List all available tools in this MCP server"}
    ]
    
    return {"tools": tools, "count": len(tools)}


# ==================== MCP Entry Point ====================

if __name__ == "__main__":
    mcp.run()
