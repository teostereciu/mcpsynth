#!/usr/bin/env python3
"""
Notion API MCP Server

A comprehensive MCP server implementation for the Notion API, providing tools
for managing pages, databases, blocks, comments, users, and search operations.
"""

import os
import json
import httpx
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("notion-api")

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

# HTTP client helper
def get_headers() -> dict:
    """Get standard headers for Notion API requests."""
    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

def make_request(method: str, endpoint: str, data: Optional[dict] = None, params: Optional[dict] = None) -> dict:
    """Make an HTTP request to the Notion API."""
    url = f"{NOTION_BASE_URL}{endpoint}"
    headers = get_headers()
    
    try:
        with httpx.Client() as client:
            if method.upper() == "GET":
                response = client.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                response = client.post(url, headers=headers, json=data, params=params)
            elif method.upper() == "PATCH":
                response = client.patch(url, headers=headers, json=data, params=params)
            elif method.upper() == "DELETE":
                response = client.delete(url, headers=headers, params=params)
            else:
                return {"error": f"Unsupported HTTP method: {method}"}
            
            if response.status_code >= 400:
                try:
                    error_data = response.json()
                    return {"error": error_data.get("message", f"HTTP {response.status_code}")}
                except:
                    return {"error": f"HTTP {response.status_code}: {response.text}"}
            
            return response.json()
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# PAGES
# ============================================================================

@mcp.tool()
def create_page(parent: dict, properties: dict, children: Optional[list] = None, markdown_content: Optional[str] = None) -> dict:
    """Create a new page in Notion."""
    data = {"parent": parent, "properties": properties}
    if children:
        data["children"] = children
    if markdown_content:
        data["markdown_content"] = markdown_content
    return make_request("POST", "/pages", data)

@mcp.tool()
def retrieve_page(page_id: str, filter_properties: Optional[list] = None) -> dict:
    """Retrieve a page by ID."""
    params = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    return make_request("GET", f"/pages/{page_id}", params=params)

@mcp.tool()
def update_page(page_id: str, properties: Optional[dict] = None, icon: Optional[dict] = None, 
                cover: Optional[dict] = None, in_trash: Optional[bool] = None, 
                is_locked: Optional[bool] = None, erase_content: Optional[bool] = None) -> dict:
    """Update a page's properties, icon, cover, or trash status."""
    data = {}
    if properties is not None:
        data["properties"] = properties
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
    if in_trash is not None:
        data["in_trash"] = in_trash
    if is_locked is not None:
        data["is_locked"] = is_locked
    if erase_content is not None:
        data["erase_content"] = erase_content
    return make_request("PATCH", f"/pages/{page_id}", data)

@mcp.tool()
def trash_page(page_id: str) -> dict:
    """Move a page to trash."""
    return update_page(page_id, in_trash=True)

@mcp.tool()
def restore_page(page_id: str) -> dict:
    """Restore a page from trash."""
    return update_page(page_id, in_trash=False)

@mcp.tool()
def move_page(page_id: str, parent: dict) -> dict:
    """Move a page to a new parent location."""
    data = {"parent": parent}
    return make_request("POST", f"/pages/{page_id}/move", data)

@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str) -> dict:
    """Retrieve a specific property of a page."""
    return make_request("GET", f"/pages/{page_id}/properties/{property_id}")

@mcp.tool()
def retrieve_page_markdown(page_id: str, include_transcripts: Optional[bool] = None) -> dict:
    """Retrieve a page's content as Notion-flavored Markdown."""
    params = {}
    if include_transcripts is not None:
        params["include_transcripts"] = include_transcripts
    return make_request("GET", f"/pages/{page_id}/markdown", params=params)

@mcp.tool()
def update_page_markdown(page_id: str, update_type: str, content_updates: Optional[list] = None,
                        insert_content: Optional[str] = None, allow_deleting_content: Optional[bool] = None) -> dict:
    """Update a page's content using Notion-flavored Markdown."""
    data = {"type": update_type}
    if update_type == "update_content" and content_updates:
        data["update_content"] = {"content_updates": content_updates}
    elif update_type == "insert_content" and insert_content:
        data["insert_content"] = {"content": insert_content}
    if allow_deleting_content is not None:
        data["allow_deleting_content"] = allow_deleting_content
    return make_request("PATCH", f"/pages/{page_id}/markdown", data)

# ============================================================================
# DATABASES
# ============================================================================

@mcp.tool()
def create_database(parent: dict, title: list, description: Optional[list] = None, 
                   is_inline: Optional[bool] = None, icon: Optional[dict] = None,
                   cover: Optional[dict] = None) -> dict:
    """Create a new database."""
    data = {"parent": parent, "title": title}
    if description is not None:
        data["description"] = description
    if is_inline is not None:
        data["is_inline"] = is_inline
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
    return make_request("POST", "/databases", data)

@mcp.tool()
def retrieve_database(database_id: str) -> dict:
    """Retrieve a database by ID."""
    return make_request("GET", f"/databases/{database_id}")

@mcp.tool()
def update_database(database_id: str, title: Optional[list] = None, 
                   description: Optional[list] = None, is_inline: Optional[bool] = None,
                   icon: Optional[dict] = None, cover: Optional[dict] = None,
                   in_trash: Optional[bool] = None, is_locked: Optional[bool] = None) -> dict:
    """Update a database's properties."""
    data = {}
    if title is not None:
        data["title"] = title
    if description is not None:
        data["description"] = description
    if is_inline is not None:
        data["is_inline"] = is_inline
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
    if in_trash is not None:
        data["in_trash"] = in_trash
    if is_locked is not None:
        data["is_locked"] = is_locked
    return make_request("PATCH", f"/databases/{database_id}", data)

@mcp.tool()
def query_database(database_id: str, filter: Optional[dict] = None, sorts: Optional[list] = None,
                  page_cursor: Optional[str] = None, results_per_page: Optional[int] = None,
                  filter_properties: Optional[list] = None) -> dict:
    """Query a database with optional filters and sorts."""
    data = {}
    if filter is not None:
        data["filter"] = filter
    if sorts is not None:
        data["sorts"] = sorts
    if page_cursor is not None:
        data["page_cursor"] = page_cursor
    if results_per_page is not None:
        data["page_size"] = results_per_page
    params = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties
    return make_request("POST", f"/databases/{database_id}/query", data, params)

# ============================================================================
# DATA SOURCES
# ============================================================================

@mcp.tool()
def create_data_source(parent: dict, title: list, properties: dict) -> dict:
    """Create a new data source."""
    data = {"parent": parent, "title": title, "properties": properties}
    return make_request("POST", "/data_sources", data)

@mcp.tool()
def retrieve_data_source(data_source_id: str) -> dict:
    """Retrieve a data source by ID."""
    return make_request("GET", f"/data_sources/{data_source_id}")

@mcp.tool()
def update_data_source(data_source_id: str, title: Optional[list] = None, 
                      properties: Optional[dict] = None, in_trash: Optional[bool] = None,
                      parent: Optional[dict] = None) -> dict:
    """Update a data source's properties."""
    data = {}
    if title is not None:
        data["title"] = title
    if properties is not None:
        data["properties"] = properties
    if in_trash is not None:
        data["in_trash"] = in_trash
    if parent is not None:
        data["parent"] = parent
    return make_request("PATCH", f"/data_sources/{data_source_id}", data)

@mcp.tool()
def query_data_source(data_source_id: str, query_filter: Optional[dict] = None, 
                     sort_rules: Optional[list] = None, page_cursor: Optional[str] = None,
                     results_per_page: Optional[int] = None, filter_properties: Optional[list] = None) -> dict:
    """Query a data source with optional filters and sorts."""
    data = {}
    if query_filter is not None:
        data["query_filter"] = query_filter
    if sort_rules is not None:
        data["sort_rules"] = sort_rules
    if page_cursor is not None:
        data["page_cursor"] = page_cursor
    if results_per_page is not None:
        data["page_size"] = results_per_page
    params = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties
    return make_request("POST", f"/data_sources/{data_source_id}/query", data, params)

# ============================================================================
# BLOCKS
# ============================================================================

@mcp.tool()
def retrieve_block(block_id: str) -> dict:
    """Retrieve a block by ID."""
    return make_request("GET", f"/blocks/{block_id}")

@mcp.tool()
def get_block_children(block_id: str, page_cursor: Optional[str] = None, 
                      results_per_page: Optional[int] = None) -> dict:
    """Retrieve the children of a block."""
    params = {}
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return make_request("GET", f"/blocks/{block_id}/children", params=params)

@mcp.tool()
def append_block_children(block_id: str, children: list, position: Optional[dict] = None) -> dict:
    """Append child blocks to a block."""
    data = {"children": children}
    if position is not None:
        data["position"] = position
    return make_request("PATCH", f"/blocks/{block_id}/children", data)

@mcp.tool()
def update_block(block_id: str, block_data: dict) -> dict:
    """Update a block's content."""
    return make_request("PATCH", f"/blocks/{block_id}", block_data)

@mcp.tool()
def delete_block(block_id: str) -> dict:
    """Delete a block."""
    return make_request("DELETE", f"/blocks/{block_id}")

# ============================================================================
# COMMENTS
# ============================================================================

@mcp.tool()
def create_comment(parent: dict, rich_text: list, display_name: Optional[dict] = None,
                  attachments: Optional[list] = None) -> dict:
    """Create a comment on a page or block."""
    data = {"parent": parent, "rich_text": rich_text}
    if display_name is not None:
        data["display_name"] = display_name
    if attachments is not None:
        data["attachments"] = attachments
    return make_request("POST", "/comments", data)

@mcp.tool()
def retrieve_comment(comment_id: str) -> dict:
    """Retrieve a comment by ID."""
    return make_request("GET", f"/comments/{comment_id}")

@mcp.tool()
def list_comments(block_id: str, page_cursor: Optional[str] = None, 
                 results_per_page: Optional[int] = None) -> dict:
    """List comments on a block or page."""
    params = {"block_id": block_id}
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return make_request("GET", "/comments", params=params)

# ============================================================================
# USERS
# ============================================================================

@mcp.tool()
def list_users(page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> dict:
    """List all users in the workspace."""
    params = {}
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return make_request("GET", "/users", params=params)

@mcp.tool()
def retrieve_user(user_id: str) -> dict:
    """Retrieve a user by ID."""
    return make_request("GET", f"/users/{user_id}")

@mcp.tool()
def get_self() -> dict:
    """Retrieve the bot user associated with the API token."""
    return make_request("GET", "/users/me")

# ============================================================================
# VIEWS
# ============================================================================

@mcp.tool()
def create_view(data_source_id: str, name: str, view_type: str, database_id: Optional[str] = None,
               view_id: Optional[str] = None, query_filter: Optional[dict] = None,
               sort_rules: Optional[list] = None, quick_filters: Optional[dict] = None) -> dict:
    """Create a new view in a database or dashboard."""
    data = {"data_source_id": data_source_id, "name": name, "type": view_type}
    if database_id is not None:
        data["database_id"] = database_id
    if view_id is not None:
        data["view_id"] = view_id
    if query_filter is not None:
        data["query_filter"] = query_filter
    if sort_rules is not None:
        data["sort_rules"] = sort_rules
    if quick_filters is not None:
        data["quick_filters"] = quick_filters
    return make_request("POST", "/views", data)

@mcp.tool()
def retrieve_view(view_id: str) -> dict:
    """Retrieve a view by ID."""
    return make_request("GET", f"/views/{view_id}")

@mcp.tool()
def update_view(view_id: str, name: Optional[str] = None, query_filter: Optional[dict] = None,
               sort_rules: Optional[list] = None, quick_filters: Optional[dict] = None) -> dict:
    """Update a view's properties."""
    data = {}
    if name is not None:
        data["name"] = name
    if query_filter is not None:
        data["query_filter"] = query_filter
    if sort_rules is not None:
        data["sort_rules"] = sort_rules
    if quick_filters is not None:
        data["quick_filters"] = quick_filters
    return make_request("PATCH", f"/views/{view_id}", data)

@mcp.tool()
def delete_view(view_id: str) -> dict:
    """Delete a view."""
    return make_request("DELETE", f"/views/{view_id}")

@mcp.tool()
def list_views(database_id: str) -> dict:
    """List all views in a database."""
    params = {"database_id": database_id}
    return make_request("GET", "/views", params=params)

# ============================================================================
# FILE UPLOADS
# ============================================================================

@mcp.tool()
def create_file_upload(mode: str = "single_part", filename: Optional[str] = None,
                      content_type: Optional[str] = None, number_of_parts: Optional[int] = None,
                      external_url: Optional[str] = None) -> dict:
    """Create a file upload session."""
    data = {"mode": mode}
    if filename is not None:
        data["filename"] = filename
    if content_type is not None:
        data["content_type"] = content_type
    if number_of_parts is not None:
        data["number_of_parts"] = number_of_parts
    if external_url is not None:
        data["external_url"] = external_url
    return make_request("POST", "/file_uploads", data)

@mcp.tool()
def retrieve_file_upload(file_upload_id: str) -> dict:
    """Retrieve a file upload by ID."""
    return make_request("GET", f"/file_uploads/{file_upload_id}")

@mcp.tool()
def list_file_uploads(page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> dict:
    """List all file uploads."""
    params = {}
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return make_request("GET", "/file_uploads", params=params)

@mcp.tool()
def complete_file_upload(file_upload_id: str) -> dict:
    """Complete a file upload session."""
    return make_request("POST", f"/file_uploads/{file_upload_id}/complete", {})

# ============================================================================
# SEARCH
# ============================================================================

@mcp.tool()
def search(query: Optional[str] = None, query_filter: Optional[dict] = None, 
          sort: Optional[dict] = None, page_cursor: Optional[str] = None,
          results_per_page: Optional[int] = None) -> dict:
    """Search for pages and databases."""
    data = {}
    if query is not None:
        data["query"] = query
    if query_filter is not None:
        data["query_filter"] = query_filter
    if sort is not None:
        data["sort"] = sort
    if page_cursor is not None:
        data["page_cursor"] = page_cursor
    if results_per_page is not None:
        data["page_size"] = results_per_page
    return make_request("POST", "/search", data)

# ============================================================================
# SERVER STARTUP
# ============================================================================

if __name__ == "__main__":
    mcp.run()
