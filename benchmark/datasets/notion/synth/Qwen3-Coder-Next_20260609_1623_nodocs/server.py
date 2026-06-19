#!/usr/bin/env python3
"""
Notion API MCP Server

An MCP server with comprehensive coverage of the Notion API,
suitable for use by an autonomous agent completing real-world tasks.
"""

import os
import requests
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="Notion", inherit_authz=False)

# Base URL for Notion API
NOTION_BASE_URL = "https://api.notion.com/v1"

# Headers for authentication
NOTION_VERSION = "2022-06-22"

def get_headers() -> Dict[str, str]:
    """Get the authentication headers for Notion API requests."""
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        raise ValueError("NOTION_API_KEY environment variable is not set")
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }

def make_request(method: str, endpoint: str, params: Dict[str, Any] = None, 
                 data: Dict[str, Any] = None) -> Dict[str, Any]:
    """Make a request to the Notion API and return the response."""
    url = f"{NOTION_BASE_URL}{endpoint}"
    headers = get_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"error": f"Not found: {endpoint}"}
        elif response.status_code == 401:
            return {"error": "Unauthorized. Check your NOTION_API_KEY."}
        elif response.status_code == 403:
            return {"error": f"Forbidden: {e}"}
        elif response.status_code == 400:
            return {"error": f"Bad request: {e}"}
        elif response.status_code == 429:
            return {"error": "Rate limit exceeded. Please try again later."}
        else:
            return {"error": f"Request failed: {e}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request error: {e}"}

def list_paginated_results(endpoint: str, page_size: int = 100) -> List[Dict[str, Any]]:
    """List paginated results from an endpoint."""
    results = []
    start_cursor = None
    
    while True:
        params = {"page_size": page_size}
        if start_cursor:
            params["start_cursor"] = start_cursor
            
        response = make_request("GET", endpoint, params=params)
        if "error" in response:
            return [response]
            
        results.extend(response.get("results", response.get("results", [])))
        
        if not response.get("has_more"):
            break
        start_cursor = response.get("next_cursor")
        
    return results


# ==================== USERS ====================

@mcp.tool()
def list_users() -> List[Dict[str, Any]]:
    """List all users in the workspace.
    
    Returns a list of users with their details.
    """
    return make_request("GET", "/users")


@mcp.tool()
def get_user(user_id: str) -> Dict[str, Any]:
    """Get a user by ID.
    
    Args:
        user_id: The ID of the user to retrieve.
        
    Returns:
        User details including name, type, and avatar URL.
    """
    return make_request("GET", f"/users/{user_id}")


@mcp.tool()
def me() -> Dict[str, Any]:
    """Get the current authenticated user (bot) details.
    
    Returns:
        Details of the bot user associated with the integration.
    """
    return make_request("GET", "/users/me")


# ==================== PAGES ====================

@mcp.tool()
def create_page(parent_page_id: str, title: str, 
                properties: Dict[str, Any] = None,
                children: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a new page as a child of an existing page.
    
    Args:
        parent_page_id: The ID of the parent page.
        title: The title of the new page.
        properties: Additional page properties (for database pages).
        children: List of block children to add to the page.
        
    Returns:
        The created page object.
    """
    data = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "title": [{"text": {"content": title}}]
            }
        }
    }
    
    if properties:
        data["properties"].update(properties)
        
    if children:
        data["children"] = children
        
    return make_request("POST", "/pages", data=data)


@mcp.tool()
def retrieve_page(page_id: str) -> Dict[str, Any]:
    """Retrieve a page by ID.
    
    Args:
        page_id: The ID of the page to retrieve.
        
    Returns:
        Page object with all its properties.
    """
    return make_request("GET", f"/pages/{page_id}")


@mcp.tool()
def update_page(page_id: str, properties: Dict[str, Any] = None,
                archived: bool = None) -> Dict[str, Any]:
    """Update a page's properties or archive it.
    
    Args:
        page_id: The ID of the page to update.
        properties: Page properties to update.
        archived: Whether to archive the page.
        
    Returns:
        The updated page object.
    """
    data = {}
    if properties:
        data["properties"] = properties
    if archived is not None:
        data["archived"] = archived
        
    return make_request("PATCH", f"/pages/{page_id}", data=data)


@mcp.tool()
def archive_page(page_id: str) -> Dict[str, Any]:
    """Archive (move to trash) a page.
    
    Args:
        page_id: The ID of the page to archive.
        
    Returns:
        The archived page object.
    """
    return update_page(page_id, archived=True)


@mcp.tool()
def get_page_properties(page_id: str) -> Dict[str, Any]:
    """Get only the properties of a page.
    
    Args:
        page_id: The ID of the page.
        
    Returns:
        Page properties object.
    """
    return make_request("GET", f"/pages/{page_id}/properties")


# ==================== DATABASES ====================

@mcp.tool()
def list_databases() -> List[Dict[str, Any]]:
    """List all databases the integration has access to.
    
    Returns:
        A list of database objects.
    """
    return make_request("GET", "/databases")


@mcp.tool()
def retrieve_database(database_id: str) -> Dict[str, Any]:
    """Retrieve a database by ID.
    
    Args:
        database_id: The ID of the database to retrieve.
        
    Returns:
        Database object with schema and properties.
    """
    return make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def query_database(database_id: str, filter: Dict[str, Any] = None,
                   sorts: List[Dict[str, Any]] = None,
                   start_cursor: str = None,
                   page_size: int = 100) -> Dict[str, Any]:
    """Query a database with filters and sorts.
    
    Args:
        database_id: The ID of the database to query.
        filter: Filter conditions for the query.
        sorts: Sort conditions for the results.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page (1-100).
        
    Returns:
        Query results with pagination info.
    """
    data = {"page_size": page_size}
    if filter:
        data["filter"] = filter
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
        
    return make_request("POST", f"/databases/{database_id}/query", data=data)


@mcp.tool()
def create_database_page(database_id: str, properties: Dict[str, Any],
                         children: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a new page in a database.
    
    Args:
        database_id: The ID of the database.
        properties: Page properties (required).
        children: Block children to add to the page.
        
    Returns:
        The created page object.
    """
    data = {
        "parent": {"database_id": database_id},
        "properties": properties
    }
    if children:
        data["children"] = children
        
    return make_request("POST", "/pages", data=data)


@mcp.tool()
def get_database_schema(database_id: str) -> Dict[str, Any]:
    """Get the schema/properties of a database.
    
    Args:
        database_id: The ID of the database.
        
    Returns:
        Database schema with all properties defined.
    """
    return make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def update_database(database_id: str, title: List[Dict[str, Any]] = None,
                    description: List[Dict[str, Any]] = None,
                    properties: Dict[str, Any] = None) -> Dict[str, Any]:
    """Update a database's title, description, or properties.
    
    Args:
        database_id: The ID of the database.
        title: New database title.
        description: New database description.
        properties: Database properties to update.
        
    Returns:
        The updated database object.
    """
    data = {}
    if title:
        data["title"] = title
    if description:
        data["description"] = description
    if properties:
        data["properties"] = properties
        
    return make_request("PATCH", f"/databases/{database_id}", data=data)


# ==================== BLOCKS (PARENT/CHILD) ====================

@mcp.tool()
def retrieve_block(block_id: str) -> Dict[str, Any]:
    """Retrieve a block by ID.
    
    Args:
        block_id: The ID of the block to retrieve.
        
    Returns:
        Block object with its content.
    """
    return make_request("GET", f"/blocks/{block_id}")


@mcp.tool()
def update_block(block_id: str, **kwargs) -> Dict[str, Any]:
    """Update a block's content.
    
    Args:
        block_id: The ID of the block to update.
        **kwargs: Block properties to update (e.g., rich_text, checked).
        
    Returns:
        The updated block object.
    """
    return make_request("PATCH", f"/blocks/{block_id}", data=kwargs)


@mcp.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    """Delete (archive) a block.
    
    Args:
        block_id: The ID of the block to delete.
        
    Returns:
        Deletion confirmation.
    """
    return make_request("PATCH", f"/blocks/{block_id}", data={"archived": True})


@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: str = None,
                            page_size: int = 100) -> Dict[str, Any]:
    """Retrieve all children of a block.
    
    Args:
        block_id: The ID of the parent block.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page (1-100).
        
    Returns:
        Block children with pagination info.
    """
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return make_request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def append_block_children(block_id: str, children: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Append new children to a block (e.g., add content to a page).
    
    Args:
        block_id: The ID of the parent block.
        children: List of block objects to append.
        
    Returns:
        The updated block with new children.
    """
    data = {"children": children}
    return make_request("PATCH", f"/blocks/{block_id}/children", data=data)


# ==================== BLOCK TYPES ====================

@mcp.tool()
def create_paragraph_block(text: str, color: str = "default", 
                           children: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a paragraph block.
    
    Args:
        text: The text content of the paragraph.
        color: Text color.
        children: Nested block children.
        
    Returns:
        Paragraph block object.
    """
    block = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }
    if children:
        block["paragraph"]["children"] = children
    return block


@mcp.tool()
def create_heading_1_block(text: str, color: str = "default") -> Dict[str, Any]:
    """Create a heading level 1 block.
    
    Args:
        text: The heading text.
        color: Text color.
        
    Returns:
        Heading 1 block object.
    """
    return {
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }


@mcp.tool()
def create_heading_2_block(text: str, color: str = "default") -> Dict[str, Any]:
    """Create a heading level 2 block.
    
    Args:
        text: The heading text.
        color: Text color.
        
    Returns:
        Heading 2 block object.
    """
    return {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }


@mcp.tool()
def create_heading_3_block(text: str, color: str = "default") -> Dict[str, Any]:
    """Create a heading level 3 block.
    
    Args:
        text: The heading text.
        color: Text color.
        
    Returns:
        Heading 3 block object.
    """
    return {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }


@mcp.tool()
def create_bullet_item_block(text: str, color: str = "default") -> Dict[str, Any]:
    """Create a bullet item block.
    
    Args:
        text: The item text.
        color: Text color.
        
    Returns:
        Bullet item block object.
    """
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }


@mcp.tool()
def create_numbered_item_block(text: str, color: str = "default") -> Dict[str, Any]:
    """Create a numbered list item block.
    
    Args:
        text: The item text.
        color: Text color.
        
    Returns:
        Numbered list item block object.
    """
    return {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }


@mcp.tool()
def create_to_do_block(text: str, checked: bool = False, color: str = "default") -> Dict[str, Any]:
    """Create a to-do block.
    
    Args:
        text: The to-do text.
        checked: Whether the to-do is completed.
        color: Text color.
        
    Returns:
        To-do block object.
    """
    return {
        "object": "block",
        "type": "to_do",
        "to_do": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "checked": checked,
            "color": color
        }
    }


@mcp.tool()
def create_toggle_block(text: str, color: str = "default",
                        children: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a toggle block.
    
    Args:
        text: The toggle summary text.
        color: Text color.
        children: Nested block children visible when toggled open.
        
    Returns:
        Toggle block object.
    """
    block = {
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }
    if children:
        block["toggle"]["children"] = children
    return block


@mcp.tool()
def create_quote_block(text: str, color: str = "default") -> Dict[str, Any]:
    """Create a quote block.
    
    Args:
        text: The quoted text.
        color: Text color.
        
    Returns:
        Quote block object.
    """
    return {
        "object": "block",
        "type": "quote",
        "quote": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }


@mcp.tool()
def create_callout_block(text: str, icon: str = None, color: str = "default") -> Dict[str, Any]:
    """Create a callout block.
    
    Args:
        text: The callout text.
        icon: Emoji or file URL for the icon.
        color: Text color.
        
    Returns:
        Callout block object.
    """
    block = {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }
    if icon:
        block["callout"]["icon"] = {"emoji": icon} if len(icon) == 1 else {"external": {"url": icon}}
    return block


@mcp.tool()
def create_code_block(text: str, language: str = "plain text",
                      caption: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a code block.
    
    Args:
        text: The code content.
        language: Programming language for syntax highlighting.
        caption: Optional caption for the code block.
        
    Returns:
        Code block object.
    """
    block = {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "language": language
        }
    }
    if caption:
        block["code"]["caption"] = caption
    return block


@mcp.tool()
def create_divider_block() -> Dict[str, Any]:
    """Create a divider block.
    
    Returns:
        Divider block object.
    """
    return {
        "object": "block",
        "type": "divider",
        "divider": {}
    }


@mcp.tool()
def create_breadcrumb_block() -> Dict[str, Any]:
    """Create a breadcrumb block.
    
    Returns:
        Breadcrumb block object.
    """
    return {
        "object": "block",
        "type": "breadcrumb",
        "breadcrumb": {}
    }


# ==================== SEARCH ====================

@mcp.tool()
def search(query: str = None, filter: Dict[str, Any] = None,
           start_cursor: str = None, page_size: int = 100) -> Dict[str, Any]:
    """Search pages and databases.
    
    Args:
        query: Search query string.
        filter: Filter by object type ("page" or "database").
        start_cursor: Cursor for pagination.
        page_size: Number of results per page (1-100).
        
    Returns:
        Search results with pagination info.
    """
    data = {"page_size": page_size}
    if query:
        data["query"] = query
    if filter:
        data["filter"] = filter
    if start_cursor:
        data["start_cursor"] = start_cursor
        
    return make_request("POST", "/search", data=data)


# ==================== COMMENTS ====================

@mcp.tool()
def create_comment(page_id: str, rich_text: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create a comment on a page.
    
    Args:
        page_id: The ID of the page to comment on.
        rich_text: The comment text as rich text.
        
    Returns:
        The created comment.
    """
    data = {
        "parent": {"page_id": page_id},
        "rich_text": rich_text
    }
    return make_request("POST", "/comments", data=data)


@mcp.tool()
def list_comments(page_id: str, start_cursor: str = None,
                  page_size: int = 100) -> Dict[str, Any]:
    """List comments on a page.
    
    Args:
        page_id: The ID of the page.
        start_cursor: Cursor for pagination.
        page_size: Number of results per page (1-100).
        
    Returns:
        Comments with pagination info.
    """
    params = {"page_id": page_id, "page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
        
    return make_request("GET", "/comments", params=params)


# ==================== ICONS & FILES ====================

@mcp.tool()
def create_icon(emoji: str = None, external_url: str = None) -> Dict[str, Any]:
    """Create an icon object for pages or databases.
    
    Args:
        emoji: Emoji character for the icon.
        external_url: URL for an external icon image.
        
    Returns:
        Icon object.
    """
    if emoji:
        return {"type": "emoji", "emoji": emoji}
    elif external_url:
        return {"type": "external", "external": {"url": external_url}}
    return {}


@mcp.tool()
def create_database_icon(emoji: str = None, external_url: str = None) -> Dict[str, Any]:
    """Create an icon object for a database.
    
    Args:
        emoji: Emoji character for the icon.
        external_url: URL for an external icon image.
        
    Returns:
        Icon object.
    """
    return create_icon(emoji=emoji, external_url=external_url)


@mcp.tool()
def create_page_icon(emoji: str = None, external_url: str = None) -> Dict[str, Any]:
    """Create an icon object for a page.
    
    Args:
        emoji: Emoji character for the icon.
        external_url: URL for an external icon image.
        
    Returns:
        Icon object.
    """
    return create_icon(emoji=emoji, external_url=external_url)


@mcp.tool()
def create_cover_image(external_url: str) -> Dict[str, Any]:
    """Create a cover image object for a page.
    
    Args:
        external_url: URL for the cover image.
        
    Returns:
        Cover image object.
    """
    return {"type": "external", "external": {"url": external_url}}


# ==================== UTILITY ====================

@mcp.tool()
def get_block_url(block_id: str) -> str:
    """Get the public URL of a block.
    
    Args:
        block_id: The ID of the block.
        
    Returns:
        The public URL of the block.
    """
    # Notion doesn't have a direct API for this, but we can construct it
    # This is a helper for the agent to understand URL structure
    return f"https://notion.so/{block_id.replace('-', '')}"


@mcp.tool()
def get_page_url(page_id: str) -> str:
    """Get the public URL of a page.
    
    Args:
        page_id: The ID of the page.
        
    Returns:
        The public URL of the page.
    """
    return f"https://notion.so/{page_id.replace('-', '')}"


@mcp.tool()
def health_check() -> Dict[str, Any]:
    """Health check endpoint to verify integration access.
    
    Returns:
        Bot user info if authenticated successfully.
    """
    return me()


if __name__ == "__main__":
    mcp.run()
