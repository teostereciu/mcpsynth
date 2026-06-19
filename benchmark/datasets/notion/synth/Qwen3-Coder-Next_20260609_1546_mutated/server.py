#!/usr/bin/env python3
"""
Notion MCP Server

An MCP server for interacting with the Notion API.
"""

import os
import requests
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(
    name="Notion",
    version="1.0.0",
    description="An MCP server for interacting with the Notion API",
)

# Base URL for Notion API
NOTION_API_BASE_URL = "https://api.notion.com/v1"

# Default Notion API version
NOTION_VERSION = "2026-03-11"


def get_headers() -> Dict[str, str]:
    """Get the headers required for Notion API requests."""
    api_key = os.environ.get("NOTION_API_KEY")
    if not api_key:
        raise ValueError("NOTION_API_KEY environment variable is not set")
    
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }


def make_request(
    method: str, 
    endpoint: str, 
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    raise_for_status: bool = True,
) -> Dict[str, Any]:
    """
    Make a request to the Notion API.
    
    Args:
        method: HTTP method (GET, POST, PATCH, DELETE)
        endpoint: API endpoint path (e.g., "/pages/{page_id}")
        params: Query parameters
        data: Request body
        raise_for_status: Whether to raise an exception on HTTP errors
        
    Returns:
        JSON response from the API
        
    Raises:
        requests.HTTPError: If raise_for_status is True and the request fails
    """
    url = f"{NOTION_API_BASE_URL}{endpoint}"
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=get_headers(),
            params=params,
            json=data,
            timeout=30,
        )
        
        if raise_for_status:
            response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.HTTPError as e:
        # Return error information instead of raising
        error_detail = {
            "error": str(e),
            "status_code": e.response.status_code,
        }
        
        # Try to include response details
        try:
            error_detail["response"] = e.response.json()
        except:
            error_detail["response_text"] = e.response.text
            
        return error_detail
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# =============================================================================
# PAGES
# =============================================================================

@mcp.tool()
def retrieve_page(page_id: str) -> Dict[str, Any]:
    """
    Retrieve a page by ID.
    
    Args:
        page_id: The ID of the page to retrieve.
        
    Returns:
        The page object.
    """
    return make_request("GET", f"/pages/{page_id}")


@mcp.tool()
def create_page(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Create a new page.
    
    Args:
        parent: The parent of the page (e.g., {"type": "database_id", "database_id": "..."})
        properties: The page properties
        icon: Optional icon for the page
        cover: Optional cover image for the page
        
    Returns:
        The created page object.
    """
    data = {"parent": parent, "properties": properties}
    
    if icon is not None:
        data["icon"] = icon
        
    if cover is not None:
        data["cover"] = cover
        
    return make_request("POST", "/pages", data=data)


@mcp.tool()
def update_page(
    page_id: str,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Update a page.
    
    Args:
        page_id: The ID of the page to update
        properties: Optional updated properties
        icon: Optional updated icon
        cover: Optional updated cover image
        in_trash: Optional trash status
        
    Returns:
        The updated page object.
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
        
    return make_request("PATCH", f"/pages/{page_id}", data=data)


@mcp.tool()
def trash_page(page_id: str, trash: bool = True) -> Dict[str, Any]:
    """
    Move a page to or from the trash.
    
    Args:
        page_id: The ID of the page to trash or restore
        trash: If True, move to trash; if False, restore from trash
        
    Returns:
        The updated page object.
    """
    return make_request(
        "PATCH",
        f"/pages/{page_id}",
        data={"in_trash": trash}
    )


@mcp.tool()
def move_page(page_id: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    """
    Move a page to a new parent.
    
    Args:
        page_id: The ID of the page to move
        parent: The new parent (e.g., {"type": "page_id", "page_id": "..."})
        
    Returns:
        The updated page object.
    """
    return make_request(
        "POST",
        f"/pages/{page_id}/move",
        data={"parent": parent}
    )


@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str) -> Dict[str, Any]:
    """
    Retrieve a specific page property.
    
    Args:
        page_id: The ID of the page
        property_id: The ID of the property to retrieve
        
    Returns:
        The property value object.
    """
    return make_request("GET", f"/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def list_page_properties(page_id: str) -> Dict[str, Any]:
    """
    List all properties of a page.
    
    Args:
        page_id: The ID of the page
        
    Returns:
        A dict containing the page properties.
    """
    return retrieve_page_property(page_id, "properties")


@mcp.tool()
def retrieve_page_markdown(page_id: str, include_transcripts: Optional[bool] = None) -> Dict[str, Any]:
    """
    Retrieve a page as markdown.
    
    Args:
        page_id: The ID of the page to retrieve as markdown
        include_transcripts: Whether to include meeting note transcripts
        
    Returns:
        The page content as markdown.
    """
    params = {}
    
    if include_transcripts is not None:
        params["include_transcripts"] = include_transcripts
        
    return make_request("GET", f"/pages/{page_id}/markdown", params=params)


@mcp.tool()
def update_page_markdown(page_id: str, markdown: str, child_page_titles: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Update a page's content as markdown.
    
    Args:
        page_id: The ID of the page to update
        markdown: The markdown content to set on the page
        child_page_titles: Optional list of child page titles to create
        
    Returns:
        The updated page object.
    """
    data = {"markdown": markdown}
    
    if child_page_titles is not None:
        data["child_page_titles"] = child_page_titles
        
    return make_request("PATCH", f"/pages/{page_id}/markdown", data=data)


# =============================================================================
# DATABASES
# =============================================================================

@mcp.tool()
def retrieve_database(database_id: str) -> Dict[str, Any]:
    """
    Retrieve a database by ID.
    
    Args:
        database_id: The ID of the database to retrieve.
        
    Returns:
        The database object.
    """
    return make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def create_database(
    parent: Dict[str, Any],
    title: List[Dict[str, Any]],
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Create a new database.
    
    Args:
        parent: The parent of the database (e.g., {"type": "page_id", "page_id": "..."})
        title: The title of the database
        properties: Optional initial property schema
        icon: Optional icon for the database
        cover: Optional cover image for the database
        is_inline: Whether the database should be displayed inline
        
    Returns:
        The created database object.
    """
    data = {"parent": parent, "title": title}
    
    if properties is not None:
        data["properties"] = properties
        
    if icon is not None:
        data["icon"] = icon
        
    if cover is not None:
        data["cover"] = cover
        
    if is_inline is not None:
        data["is_inline"] = is_inline
        
    return make_request("POST", "/databases", data=data)


@mcp.tool()
def update_database(
    database_id: str,
    title: Optional[List[Dict[str, Any]]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
    in_trash: Optional[bool] = None,
    parent: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Update a database.
    
    Args:
        database_id: The ID of the database to update
        title: Optional updated title
        description: Optional updated description
        icon: Optional updated icon
        cover: Optional updated cover image
        is_inline: Optional updated inline status
        in_trash: Optional trash status
        parent: Optional new parent
        
    Returns:
        The updated database object.
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
        
    if is_inline is not None:
        data["is_inline"] = is_inline
        
    if in_trash is not None:
        data["in_trash"] = in_trash
        
    if parent is not None:
        data["parent"] = parent
        
    return make_request("PATCH", f"/databases/{database_id}", data=data)


@mcp.tool()
def query_database(
    database_id: str,
    filter_condition: Optional[Dict[str, Any]] = None,
    sort_rules: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Query a database with optional filters and sorting.
    
    Args:
        database_id: The ID of the database to query
        filter_condition: Optional filter condition
        sort_rules: Optional sort rules
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        The query results.
    """
    data = {}
    
    if filter_condition is not None:
        data["filter"] = filter_condition
        
    if sort_rules is not None:
        data["sorts"] = sort_rules
        
    if start_cursor is not None:
        data["start_cursor"] = start_cursor
        
    if page_size is not None:
        data["page_size"] = page_size
        
    return make_request("POST", f"/databases/{database_id}/query", data=data)


@mcp.tool()
def list_databases(
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    List databases accessible to the integration.
    
    Args:
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        A list of databases.
    """
    params = {}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
        
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", "/databases", params=params)


# =============================================================================
# BLOCKS
# =============================================================================

@mcp.tool()
def retrieve_block(block_id: str) -> Dict[str, Any]:
    """
    Retrieve a block by ID.
    
    Args:
        block_id: The ID of the block to retrieve.
        
    Returns:
        The block object.
    """
    return make_request("GET", f"/blocks/{block_id}")


@mcp.tool()
def update_block(
    block_id: str,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Update a block.
    
    Args:
        block_id: The ID of the block to update
        kwargs: Block-specific properties to update
        
    Returns:
        The updated block object.
    """
    return make_request("PATCH", f"/blocks/{block_id}", data=kwargs)


@mcp.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    """
    Delete a block.
    
    Args:
        block_id: The ID of the block to delete.
        
    Returns:
        The deleted block object.
    """
    return make_request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def append_block_children(
    block_id: str,
    children: List[Dict[str, Any]],
    after: Optional[str] = None,
    children_position: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Append block children to a parent block.
    
    Args:
        block_id: The ID of the parent block
        children: List of block children to append
        after: Block ID to insert after
        children_position: Position for insertion ("start", "end", or "after_block")
        
    Returns:
        The response containing the appended blocks.
    """
    data = {"children": children}
    
    if after is not None:
        data["position"] = {"type": "after_block", "after_block": {"id": after}}
    elif children_position == "start":
        data["position"] = {"type": "start"}
    elif children_position == "end":
        # Default position
        pass
        
    return make_request("PATCH", f"/blocks/{block_id}/children", data=data)


@mcp.tool()
def get_block_children(block_id: str, page_size: Optional[int] = None) -> Dict[str, Any]:
    """
    Get the children of a block.
    
    Args:
        block_id: The ID of the parent block
        page_size: Optional page size (max 100)
        
    Returns:
        A list of child blocks.
    """
    params = {}
    
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", f"/blocks/{block_id}/children", params=params)


# =============================================================================
# COMMENTS
# =============================================================================

@mcp.tool()
def create_comment(
    parent: Dict[str, Any],
    rich_text: List[Dict[str, Any]],
    attachments: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Create a comment.
    
    Args:
        parent: The parent of the comment (page or block)
        rich_text: The content of the comment
        attachments: Optional file attachments (max 3)
        
    Returns:
        The created comment object.
    """
    data = {"parent": parent, "rich_text": rich_text}
    
    if attachments is not None:
        data["attachments"] = attachments
        
    return make_request("POST", "/comments", data=data)


@mcp.tool()
def retrieve_comment(comment_id: str) -> Dict[str, Any]:
    """
    Retrieve a comment by ID.
    
    Args:
        comment_id: The ID of the comment to retrieve.
        
    Returns:
        The comment object.
    """
    return make_request("GET", f"/comments/{comment_id}")


@mcp.tool()
def list_comments(
    block_id: Optional[str] = None,
    page_id: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    List comments on a block or page.
    
    Args:
        block_id: The ID of the block (one of block_id or page_id required)
        page_id: The ID of the page (one of block_id or page_id required)
        page_size: Optional page size (max 100)
        
    Returns:
        A list of comments.
    """
    if block_id is None and page_id is None:
        return {"error": "Either block_id or page_id must be provided"}
    
    params = {}
    
    if block_id is not None:
        params["block_id"] = block_id
    else:
        params["page_id"] = page_id
        
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", "/comments", params=params)


# =============================================================================
# USERS
# =============================================================================

@mcp.tool()
def retrieve_user(user_id: str) -> Dict[str, Any]:
    """
    Retrieve a user by ID.
    
    Args:
        user_id: The ID of the user to retrieve.
        
    Returns:
        The user object.
    """
    return make_request("GET", f"/users/{user_id}")


@mcp.tool()
def list_users(
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    List all users in the workspace.
    
    Args:
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        A list of users.
    """
    params = {}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
        
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", "/users", params=params)


@mcp.tool()
def get_bot_user() -> Dict[str, Any]:
    """
    Retrieve the bot user associated with the integration.
    
    Returns:
        The bot user object.
    """
    return make_request("GET", "/users/me")


# =============================================================================
# SEARCH
# =============================================================================

@mcp.tool()
def search(
    query: Optional[str] = None,
    filter_condition: Optional[Dict[str, Any]] = None,
    sort_rules: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Search for pages, databases, and other objects.
    
    Args:
        query: Optional search query
        filter_condition: Optional filter condition (e.g., filter by object type)
        sort_rules: Optional sort rules
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        The search results.
    """
    data = {}
    
    if query is not None:
        data["query"] = query
        
    if filter_condition is not None:
        data["filter"] = filter_condition
        
    if sort_rules is not None:
        data["sorts"] = sort_rules
        
    if start_cursor is not None:
        data["start_cursor"] = start_cursor
        
    if page_size is not None:
        data["page_size"] = page_size
        
    return make_request("POST", "/search", data=data)


# =============================================================================
# VIEWS
# =============================================================================

@mcp.tool()
def retrieve_view(view_id: str) -> Dict[str, Any]:
    """
    Retrieve a view by ID.
    
    Args:
        view_id: The ID of the view to retrieve.
        
    Returns:
        The view object.
    """
    return make_request("GET", f"/views/{view_id}")


@mcp.tool()
def update_view(
    view_id: str,
    name: Optional[str] = None,
    filter_condition: Optional[Dict[str, Any]] = None,
    sort_rules: Optional[List[Dict[str, Any]]] = None,
    query_filters: Optional[Dict[str, Any]] = None,
    display: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Update a view.
    
    Args:
        view_id: The ID of the view to update
        name: Optional new name
        filter_condition: Optional new filter condition
        sort_rules: Optional new sort rules
        query_filters: Optional quick filters for the view's query filter bar
        display: Optional view presentation configuration
        
    Returns:
        The updated view object.
    """
    data = {}
    
    if name is not None:
        data["name"] = name
        
    if filter_condition is not None:
        data["filter"] = filter_condition
        
    if sort_rules is not None:
        data["sorts"] = sort_rules
        
    if query_filters is not None:
        data["query_filters"] = query_filters
        
    if display is not None:
        data["display"] = display
        
    return make_request("PATCH", f"/views/{view_id}", data=data)


@mcp.tool()
def list_views(
    database_id: str,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    List all views in a database.
    
    Args:
        database_id: The ID of the database
        page_size: Optional page size (max 100)
        
    Returns:
        A list of views.
    """
    params = {}
    
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", f"/databases/{database_id}/views", params=params)


@mcp.tool()
def delete_view(view_id: str) -> Dict[str, Any]:
    """
    Delete a view.
    
    Args:
        view_id: The ID of the view to delete.
        
    Returns:
        The deleted view object.
    """
    return make_request("DELETE", f"/views/{view_id}")


@mcp.tool()
def delete_view_query(view_id: str, query_id: str) -> Dict[str, Any]:
    """
    Delete a view query.
    
    Args:
        view_id: The ID of the view
        query_id: The ID of the query
        
    Returns:
        The deleted view query object.
    """
    return make_request("DELETE", f"/views/{view_id}/queries/{query_id}")


# =============================================================================
# FILE UPLOADS
# =============================================================================

@mcp.tool()
def create_file_upload(
    mode: str = "single_part",
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a file upload.
    
    Args:
        mode: Upload mode ("single_part" or "multi_part")
        filename: Optional filename
        content_type: Optional MIME type
        
    Returns:
        The file upload object.
    """
    data = {"mode": mode}
    
    if filename is not None:
        data["filename"] = filename
        
    if content_type is not None:
        data["content_type"] = content_type
        
    return make_request("POST", "/file_uploads", data=data)


@mcp.tool()
def retrieve_file_upload(file_upload_id: str) -> Dict[str, Any]:
    """
    Retrieve a file upload by ID.
    
    Args:
        file_upload_id: The ID of the file upload to retrieve.
        
    Returns:
        The file upload object.
    """
    return make_request("GET", f"/file_uploads/{file_upload_id}")


@mcp.tool()
def complete_file_upload(file_upload_id: str) -> Dict[str, Any]:
    """
    Complete a file upload.
    
    Args:
        file_upload_id: The ID of the file upload to complete.
        
    Returns:
        The completed file upload object.
    """
    return make_request("POST", f"/file_uploads/{file_upload_id}/complete")


@mcp.tool()
def list_file_uploads(
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    List file uploads.
    
    Args:
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        A list of file uploads.
    """
    params = {}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
        
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", "/file_uploads", params=params)


# =============================================================================
# AUTHENTICATION
# =============================================================================

@mcp.tool()
def introspect_token(
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Introspect an OAuth token.
    
    Args:
        client_id: OAuth client ID
        client_secret: OAuth client secret
        token: Token to introspect
        
    Returns:
        The introspection result.
    """
    # For OAuth introspection, we need to use Basic auth
    # This is a simplified implementation - for full OAuth support,
    # the client would need to provide the credentials
    api_key = os.environ.get("NOTION_API_KEY")
    if not api_key:
        return {"error": "NOTION_API_KEY environment variable is not set"}
    
    # This is a placeholder - actual OAuth introspection requires
    # a different endpoint and auth method
    return {
        "error": "OAuth introspection requires proper client credentials. "
                 "Use the integration token from NOTION_API_KEY for standard API calls."
    }


@mcp.tool()
def refresh_token(
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    refresh_token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Refresh an OAuth token.
    
    Args:
        client_id: OAuth client ID
        client_secret: OAuth client secret
        refresh_token: Token to refresh
        
    Returns:
        The new access token.
    """
    return {
        "error": "Token refresh requires OAuth credentials. "
                 "Use the integration token from NOTION_API_KEY for standard API calls."
    }


@mcp.tool()
def revoke_token(
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Revoke an OAuth token.
    
    Args:
        client_id: OAuth client ID
        client_secret: OAuth client secret
        token: Token to revoke
        
    Returns:
        The revocation result.
    """
    return {
        "error": "Token revocation requires OAuth credentials. "
                 "Use the integration token from NOTION_API_KEY for standard API calls."
    }


# =============================================================================
# DATA SOURCES
# =============================================================================

@mcp.tool()
def retrieve_data_source(data_source_id: str) -> Dict[str, Any]:
    """
    Retrieve a data source by ID.
    
    Args:
        data_source_id: The ID of the data source to retrieve.
        
    Returns:
        The data source object.
    """
    return make_request("GET", f"/data_sources/{data_source_id}")


@mcp.tool()
def query_data_source(
    data_source_id: str,
    filter_condition: Optional[Dict[str, Any]] = None,
    sort_rules: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Query a data source.
    
    Args:
        data_source_id: The ID of the data source to query
        filter_condition: Optional filter condition
        sort_rules: Optional sort rules
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        The query results.
    """
    data = {}
    
    if filter_condition is not None:
        data["filter"] = filter_condition
        
    if sort_rules is not None:
        data["sorts"] = sort_rules
        
    if start_cursor is not None:
        data["start_cursor"] = start_cursor
        
    if page_size is not None:
        data["page_size"] = page_size
        
    return make_request("POST", f"/data_sources/{data_source_id}/query", data=data)


# =============================================================================
# DATA SOURCE PROPERTIES
# =============================================================================

@mcp.tool()
def update_data_source_properties(
    data_source_id: str,
    properties: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Update data source properties.
    
    Args:
        data_source_id: The ID of the data source
        properties: Properties to update or remove
        
    Returns:
        The updated data source object.
    """
    return make_request("PATCH", f"/data_sources/{data_source_id}/properties", data=properties)


# =============================================================================
# VIEW QUERIES
# =============================================================================

@mcp.tool()
def create_view_query(
    view_id: str,
    filter_condition: Optional[Dict[str, Any]] = None,
    sort_rules: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Create a view query.
    
    Args:
        view_id: The ID of the view
        filter_condition: Optional filter condition
        sort_rules: Optional sort rules
        
    Returns:
        The view query object.
    """
    data = {}
    
    if filter_condition is not None:
        data["filter"] = filter_condition
        
    if sort_rules is not None:
        data["sorts"] = sort_rules
        
    return make_request("POST", f"/views/{view_id}/query", data=data)


@mcp.tool()
def get_view_query_results(
    view_query_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Get view query results.
    
    Args:
        view_query_id: The ID of the view query
        start_cursor: Optional cursor for pagination
        page_size: Optional page size (max 100)
        
    Returns:
        The query results.
    """
    params = {}
    
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
        
    if page_size is not None:
        params["page_size"] = page_size
        
    return make_request("GET", f"/view_queries/{view_query_id}", params=params)


if __name__ == "__main__":
    mcp.run()
