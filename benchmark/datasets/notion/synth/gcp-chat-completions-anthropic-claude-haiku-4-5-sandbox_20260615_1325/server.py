#!/usr/bin/env python3
"""
MCP Server for Notion API
Provides comprehensive tools for interacting with the Notion API
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("notion-api")

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
BASE_URL = "https://api.notion.com/v1"
API_VERSION = "2026-03-11"

# Helper function to make API requests
def make_request(
    method: str,
    endpoint: str,
    data: Optional[dict] = None,
    params: Optional[dict] = None,
) -> dict:
    """Make a request to the Notion API"""
    if not NOTION_API_KEY:
        return {"error": "NOTION_API_KEY environment variable not set"}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": API_VERSION,
        "Content-Type": "application/json",
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data, params=params, timeout=30)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, json=data, params=params, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=30)
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
        return {"error": "Failed to parse response as JSON"}


# ============================================================================
# PAGES
# ============================================================================

@mcp.tool()
def create_page(
    parent_type: str,
    parent_id: str,
    properties: dict,
    children: Optional[list] = None,
    icon: Optional[dict] = None,
    cover: Optional[dict] = None,
) -> dict:
    """Create a new page in Notion.
    
    Args:
        parent_type: Type of parent - 'database_id', 'page_id', 'workspace', or 'data_source_id'
        parent_id: ID of the parent
        properties: Page properties (e.g., {"Name": {"title": [{"text": {"content": "Title"}}]}})
        children: Optional list of child blocks
        icon: Optional icon object (e.g., {"type": "emoji", "emoji": "📝"})
        cover: Optional cover image object
    """
    parent = {parent_type: parent_id}
    body = {
        "parent": parent,
        "properties": properties,
    }
    if children:
        body["children"] = children
    if icon:
        body["icon"] = icon
    if cover:
        body["cover"] = cover
    
    return make_request("POST", "/pages", data=body)


@mcp.tool()
def retrieve_page(page_id: str, filter_properties: Optional[list] = None) -> dict:
    """Retrieve a page by ID.
    
    Args:
        page_id: The ID of the page to retrieve
        filter_properties: Optional list of property IDs to filter
    """
    params = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    
    return make_request("GET", f"/pages/{page_id}", params=params)


@mcp.tool()
def update_page(
    page_id: str,
    properties: Optional[dict] = None,
    icon: Optional[dict] = None,
    cover: Optional[dict] = None,
    in_trash: Optional[bool] = None,
    is_locked: Optional[bool] = None,
) -> dict:
    """Update a page.
    
    Args:
        page_id: The ID of the page to update
        properties: Updated properties
        icon: Updated icon
        cover: Updated cover
        in_trash: Whether to move page to trash
        is_locked: Whether to lock the page
    """
    body = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    
    return make_request("PATCH", f"/pages/{page_id}", data=body)


@mcp.tool()
def archive_page(page_id: str) -> dict:
    """Archive a page (move to trash).
    
    Args:
        page_id: The ID of the page to archive
    """
    return make_request("PATCH", f"/pages/{page_id}", data={"in_trash": True})


@mcp.tool()
def restore_page(page_id: str) -> dict:
    """Restore a page from trash.
    
    Args:
        page_id: The ID of the page to restore
    """
    return make_request("PATCH", f"/pages/{page_id}", data={"in_trash": False})


@mcp.tool()
def move_page(page_id: str, parent_type: str, parent_id: str) -> dict:
    """Move a page to a new parent.
    
    Args:
        page_id: The ID of the page to move
        parent_type: Type of new parent - 'page_id' or 'database_id'
        parent_id: ID of the new parent
    """
    parent = {parent_type: parent_id}
    return make_request("POST", f"/pages/{page_id}/move", data={"parent": parent})


@mcp.tool()
def retrieve_page_property(
    page_id: str,
    property_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """Retrieve a specific property of a page.
    
    Args:
        page_id: The ID of the page
        property_id: The ID of the property to retrieve
        start_cursor: Pagination cursor
        page_size: Number of results per page
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", f"/pages/{page_id}/properties/{property_id}", params=params)


# ============================================================================
# DATABASES
# ============================================================================

@mcp.tool()
def create_database(
    parent_type: str,
    parent_id: str,
    title: list,
    properties: Optional[dict] = None,
    description: Optional[list] = None,
    icon: Optional[dict] = None,
    cover: Optional[dict] = None,
    is_inline: Optional[bool] = None,
) -> dict:
    """Create a new database.
    
    Args:
        parent_type: Type of parent - 'page_id' or 'workspace'
        parent_id: ID of the parent
        title: Title as rich text array (e.g., [{"text": {"content": "My Database"}}])
        properties: Database properties schema
        description: Optional description as rich text array
        icon: Optional icon object
        cover: Optional cover image object
        is_inline: Whether to display inline
    """
    body = {
        "parent": {parent_type: parent_id},
        "title": title,
    }
    if properties:
        body["properties"] = properties
    if description:
        body["description"] = description
    if icon:
        body["icon"] = icon
    if cover:
        body["cover"] = cover
    if is_inline is not None:
        body["is_inline"] = is_inline
    
    return make_request("POST", "/databases", data=body)


@mcp.tool()
def retrieve_database(database_id: str) -> dict:
    """Retrieve a database by ID.
    
    Args:
        database_id: The ID of the database to retrieve
    """
    return make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def update_database(
    database_id: str,
    title: Optional[list] = None,
    description: Optional[list] = None,
    icon: Optional[dict] = None,
    cover: Optional[dict] = None,
    properties: Optional[dict] = None,
) -> dict:
    """Update a database.
    
    Args:
        database_id: The ID of the database to update
        title: Updated title as rich text array
        description: Updated description as rich text array
        icon: Updated icon
        cover: Updated cover
        properties: Updated properties schema
    """
    body = {}
    if title is not None:
        body["title"] = title
    if description is not None:
        body["description"] = description
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if properties is not None:
        body["properties"] = properties
    
    return make_request("PATCH", f"/databases/{database_id}", data=body)


@mcp.tool()
def query_database(
    database_id: str,
    filter: Optional[dict] = None,
    sorts: Optional[list] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    filter_properties: Optional[list] = None,
) -> dict:
    """Query a database with filters and sorts.
    
    Args:
        database_id: The ID of the database to query
        filter: Filter object (e.g., {"property": "Status", "select": {"equals": "Done"}})
        sorts: List of sort objects (e.g., [{"property": "Name", "direction": "ascending"}])
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
        filter_properties: List of property IDs to include in response
    """
    body = {}
    if filter:
        body["filter"] = filter
    if sorts:
        body["sorts"] = sorts
    if start_cursor:
        body["start_cursor"] = start_cursor
    if page_size:
        body["page_size"] = page_size
    
    params = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    
    return make_request("POST", f"/databases/{database_id}/query", data=body, params=params)


# ============================================================================
# BLOCKS
# ============================================================================

@mcp.tool()
def retrieve_block(block_id: str) -> dict:
    """Retrieve a block by ID.
    
    Args:
        block_id: The ID of the block to retrieve
    """
    return make_request("GET", f"/blocks/{block_id}")


@mcp.tool()
def get_block_children(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """Retrieve children of a block.
    
    Args:
        block_id: The ID of the parent block
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def append_block_children(
    block_id: str,
    children: list,
    position: Optional[dict] = None,
) -> dict:
    """Append child blocks to a block.
    
    Args:
        block_id: The ID of the parent block
        children: List of block objects to append
        position: Optional position object (e.g., {"type": "end"} or {"type": "start"})
    """
    body = {"children": children}
    if position:
        body["position"] = position
    
    return make_request("PATCH", f"/blocks/{block_id}/children", data=body)


@mcp.tool()
def update_block(block_id: str, block_data: dict) -> dict:
    """Update a block.
    
    Args:
        block_id: The ID of the block to update
        block_data: Block type and content (e.g., {"paragraph": {"rich_text": [...]}})
    """
    return make_request("PATCH", f"/blocks/{block_id}", data=block_data)


@mcp.tool()
def delete_block(block_id: str) -> dict:
    """Delete a block.
    
    Args:
        block_id: The ID of the block to delete
    """
    return make_request("DELETE", f"/blocks/{block_id}")


# ============================================================================
# COMMENTS
# ============================================================================

@mcp.tool()
def create_comment(
    parent_type: str,
    parent_id: str,
    rich_text: list,
    attachments: Optional[list] = None,
    display_name: Optional[dict] = None,
) -> dict:
    """Create a comment on a page or block.
    
    Args:
        parent_type: Type of parent - 'page_id' or 'block_id'
        parent_id: ID of the parent
        rich_text: Comment content as rich text array
        attachments: Optional list of file attachments
        display_name: Optional custom display name
    """
    body = {
        "parent": {parent_type: parent_id},
        "rich_text": rich_text,
    }
    if attachments:
        body["attachments"] = attachments
    if display_name:
        body["display_name"] = display_name
    
    return make_request("POST", "/comments", data=body)


@mcp.tool()
def retrieve_comment(comment_id: str) -> dict:
    """Retrieve a comment by ID.
    
    Args:
        comment_id: The ID of the comment to retrieve
    """
    return make_request("GET", f"/comments/{comment_id}")


@mcp.tool()
def list_comments(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """List comments on a block or page.
    
    Args:
        block_id: The ID of the block or page
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    params = {"block_id": block_id}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/comments", params=params)


# ============================================================================
# USERS
# ============================================================================

@mcp.tool()
def list_users(
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """List all users in the workspace.
    
    Args:
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/users", params=params)


@mcp.tool()
def retrieve_user(user_id: str) -> dict:
    """Retrieve a user by ID.
    
    Args:
        user_id: The ID of the user to retrieve
    """
    return make_request("GET", f"/users/{user_id}")


@mcp.tool()
def get_bot_user() -> dict:
    """Retrieve the bot user associated with the API token."""
    return make_request("GET", "/users/me")


# ============================================================================
# SEARCH
# ============================================================================

@mcp.tool()
def search(
    query: Optional[str] = None,
    filter: Optional[dict] = None,
    sort: Optional[dict] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """Search for pages and databases.
    
    Args:
        query: Search query string
        filter: Filter object (e.g., {"property": "object", "value": "page"})
        sort: Sort object (e.g., {"direction": "descending", "timestamp": "last_edited_time"})
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    body = {}
    if query:
        body["query"] = query
    if filter:
        body["filter"] = filter
    if sort:
        body["sort"] = sort
    if start_cursor:
        body["start_cursor"] = start_cursor
    if page_size:
        body["page_size"] = page_size
    
    return make_request("POST", "/search", data=body)


# ============================================================================
# DATA SOURCES
# ============================================================================

@mcp.tool()
def create_data_source(
    parent_type: str,
    parent_id: str,
    title: list,
    properties: Optional[dict] = None,
) -> dict:
    """Create a new data source.
    
    Args:
        parent_type: Type of parent - 'database_id' or 'page_id'
        parent_id: ID of the parent
        title: Title as rich text array
        properties: Data source properties schema
    """
    body = {
        "parent": {parent_type: parent_id},
        "title": title,
    }
    if properties:
        body["properties"] = properties
    
    return make_request("POST", "/data_sources", data=body)


@mcp.tool()
def retrieve_data_source(data_source_id: str) -> dict:
    """Retrieve a data source by ID.
    
    Args:
        data_source_id: The ID of the data source to retrieve
    """
    return make_request("GET", f"/data_sources/{data_source_id}")


@mcp.tool()
def query_data_source(
    data_source_id: str,
    filter: Optional[dict] = None,
    sorts: Optional[list] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """Query a data source with filters and sorts.
    
    Args:
        data_source_id: The ID of the data source to query
        filter: Filter object
        sorts: List of sort objects
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    body = {}
    if filter:
        body["filter"] = filter
    if sorts:
        body["sorts"] = sorts
    if start_cursor:
        body["start_cursor"] = start_cursor
    if page_size:
        body["page_size"] = page_size
    
    return make_request("POST", f"/data_sources/{data_source_id}/query", data=body)


@mcp.tool()
def update_data_source(
    data_source_id: str,
    title: Optional[list] = None,
    properties: Optional[dict] = None,
) -> dict:
    """Update a data source.
    
    Args:
        data_source_id: The ID of the data source to update
        title: Updated title as rich text array
        properties: Updated properties schema
    """
    body = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    
    return make_request("PATCH", f"/data_sources/{data_source_id}", data=body)


@mcp.tool()
def list_data_source_templates(data_source_id: str) -> dict:
    """List templates available for a data source.
    
    Args:
        data_source_id: The ID of the data source
    """
    return make_request("GET", f"/data_sources/{data_source_id}/templates")


# ============================================================================
# VIEWS
# ============================================================================

@mcp.tool()
def create_view(
    data_source_id: str,
    name: str,
    view_type: str,
    database_id: Optional[str] = None,
    view_id: Optional[str] = None,
    filter: Optional[dict] = None,
    sorts: Optional[list] = None,
    quick_filters: Optional[dict] = None,
    config: Optional[dict] = None,
    position: Optional[dict] = None,
) -> dict:
    """Create a new view.
    
    Args:
        data_source_id: The ID of the data source
        name: Name of the view
        view_type: Type of view (e.g., 'table', 'gallery', 'calendar')
        database_id: Optional database ID (for database views)
        view_id: Optional view ID (for dashboard widgets)
        filter: Optional filter object
        sorts: Optional list of sort objects
        quick_filters: Optional quick filters
        config: Optional view configuration
        position: Optional position object
    """
    body = {
        "data_source_id": data_source_id,
        "name": name,
        "type": view_type,
    }
    if database_id:
        body["database_id"] = database_id
    if view_id:
        body["view_id"] = view_id
    if filter:
        body["filter"] = filter
    if sorts:
        body["sorts"] = sorts
    if quick_filters:
        body["quick_filters"] = quick_filters
    if config:
        body["config"] = config
    if position:
        body["position"] = position
    
    return make_request("POST", "/views", data=body)


@mcp.tool()
def retrieve_view(view_id: str) -> dict:
    """Retrieve a view by ID.
    
    Args:
        view_id: The ID of the view to retrieve
    """
    return make_request("GET", f"/views/{view_id}")


@mcp.tool()
def update_view(
    view_id: str,
    name: Optional[str] = None,
    filter: Optional[dict] = None,
    sorts: Optional[list] = None,
    quick_filters: Optional[dict] = None,
    config: Optional[dict] = None,
) -> dict:
    """Update a view.
    
    Args:
        view_id: The ID of the view to update
        name: Updated name
        filter: Updated filter
        sorts: Updated sorts
        quick_filters: Updated quick filters
        config: Updated configuration
    """
    body = {}
    if name is not None:
        body["name"] = name
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if quick_filters is not None:
        body["quick_filters"] = quick_filters
    if config is not None:
        body["config"] = config
    
    return make_request("PATCH", f"/views/{view_id}", data=body)


@mcp.tool()
def delete_view(view_id: str) -> dict:
    """Delete a view.
    
    Args:
        view_id: The ID of the view to delete
    """
    return make_request("DELETE", f"/views/{view_id}")


@mcp.tool()
def list_views(
    data_source_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """List views for a data source.
    
    Args:
        data_source_id: The ID of the data source
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    params = {"data_source_id": data_source_id}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/views", params=params)


@mcp.tool()
def create_view_query(
    view_id: str,
    filter: Optional[dict] = None,
    sorts: Optional[list] = None,
) -> dict:
    """Create a query for a view.
    
    Args:
        view_id: The ID of the view
        filter: Optional filter object
        sorts: Optional list of sort objects
    """
    body = {}
    if filter:
        body["filter"] = filter
    if sorts:
        body["sorts"] = sorts
    
    return make_request("POST", f"/views/{view_id}/queries", data=body)


@mcp.tool()
def get_view_query_results(
    view_id: str,
    query_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """Get results for a view query.
    
    Args:
        view_id: The ID of the view
        query_id: The ID of the query
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", f"/views/{view_id}/queries/{query_id}/results", params=params)


@mcp.tool()
def delete_view_query(view_id: str, query_id: str) -> dict:
    """Delete a view query.
    
    Args:
        view_id: The ID of the view
        query_id: The ID of the query to delete
    """
    return make_request("DELETE", f"/views/{view_id}/queries/{query_id}")


# ============================================================================
# FILE UPLOADS
# ============================================================================

@mcp.tool()
def create_file_upload(
    filename: str,
    content_type: str,
    mode: str = "single_part",
    number_of_parts: Optional[int] = None,
    external_url: Optional[str] = None,
) -> dict:
    """Create a file upload session.
    
    Args:
        filename: Name of the file to upload
        content_type: MIME type of the file
        mode: Upload mode - 'single_part', 'multi_part', or 'external_url'
        number_of_parts: Required for multi_part mode
        external_url: Required for external_url mode
    """
    body = {
        "filename": filename,
        "content_type": content_type,
        "mode": mode,
    }
    if number_of_parts:
        body["number_of_parts"] = number_of_parts
    if external_url:
        body["external_url"] = external_url
    
    return make_request("POST", "/file_uploads", data=body)


@mcp.tool()
def retrieve_file_upload(file_upload_id: str) -> dict:
    """Retrieve a file upload by ID.
    
    Args:
        file_upload_id: The ID of the file upload to retrieve
    """
    return make_request("GET", f"/file_uploads/{file_upload_id}")


@mcp.tool()
def list_file_uploads(
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> dict:
    """List file uploads.
    
    Args:
        start_cursor: Pagination cursor
        page_size: Number of results per page (max 100)
    """
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    
    return make_request("GET", "/file_uploads", params=params)


@mcp.tool()
def complete_file_upload(file_upload_id: str) -> dict:
    """Complete a file upload.
    
    Args:
        file_upload_id: The ID of the file upload to complete
    """
    return make_request("POST", f"/file_uploads/{file_upload_id}/complete", data={})


if __name__ == "__main__":
    mcp.run()
