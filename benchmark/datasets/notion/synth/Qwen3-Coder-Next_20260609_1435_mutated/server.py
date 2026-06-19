import os
import requests
from typing import Any

from fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("notion")

# Base URL and headers for Notion API
BASE_URL = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
    "Notion-Version": "2026-03-11",
    "Content-Type": "application/json"
}


def _make_request(method: str, endpoint: str, params: dict = None, json: dict = None) -> dict:
    """Helper function to make HTTP requests to the Notion API."""
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=HEADERS,
            params=params,
            json=json
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e}", "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}


# Page endpoints
@mcp.tool()
def get_page(page_id: str) -> dict:
    """Retrieve a page by its ID."""
    return _make_request("GET", f"/pages/{page_id}")


@mcp.tool()
def create_page(parent: dict, properties: dict = None, children: list = None) -> dict:
    """Create a new page under a parent."""
    payload = {"parent": parent}
    if properties:
        payload["properties"] = properties
    if children:
        payload["children"] = children
    return _make_request("POST", "/pages", json=payload)


@mcp.tool()
def update_page(page_id: str, properties: dict = None, icon: dict = None, cover: dict = None, 
                in_trash: bool = None, locked: bool = None) -> dict:
    """Update an existing page."""
    payload = {}
    if properties:
        payload["properties"] = properties
    if icon:
        payload["icon"] = icon
    if cover:
        payload["cover"] = cover
    if in_trash is not None:
        payload["in_trash"] = in_trash
    if locked is not None:
        payload["locked"] = locked
    return _make_request("PATCH", f"/pages/{page_id}", json=payload)


@mcp.tool()
def trash_page(page_id: str, in_trash: bool = True) -> dict:
    """Move a page to or from the trash."""
    return _make_request("PATCH", f"/pages/{page_id}", json={"in_trash": in_trash})


@mcp.tool()
def move_page(page_id: str, parent: dict) -> dict:
    """Move a page to a new parent."""
    return _make_request("POST", f"/pages/{page_id}/move", json={"parent": parent})


# Database endpoints
@mcp.tool()
def retrieve_database(database_id: str) -> dict:
    """Retrieve a database by its ID."""
    return _make_request("GET", f"/databases/{database_id}")


@mcp.tool()
def list_databases(start_cursor: str = None, page_size: int = 100) -> dict:
    """List all databases accessible to the integration."""
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", "/databases", params=params)


@mcp.tool()
def create_database(parent: dict, title: list = None, properties: dict = None, 
                   is_inline: bool = None, icon: dict = None, cover: dict = None) -> dict:
    """Create a new database."""
    payload = {"parent": parent}
    if title:
        payload["title"] = title
    if properties:
        payload["properties"] = properties
    if is_inline is not None:
        payload["is_inline"] = is_inline
    if icon:
        payload["icon"] = icon
    if cover:
        payload["cover"] = cover
    return _make_request("POST", "/databases", json=payload)


@mcp.tool()
def update_database(database_id: str, title: list = None, icon: dict = None, cover: dict = None,
                   is_inline: bool = None, parent: dict = None, in_trash: bool = None) -> dict:
    """Update an existing database."""
    payload = {}
    if title:
        payload["title"] = title
    if icon:
        payload["icon"] = icon
    if cover:
        payload["cover"] = cover
    if is_inline is not None:
        payload["is_inline"] = is_inline
    if parent:
        payload["parent"] = parent
    if in_trash is not None:
        payload["in_trash"] = in_trash
    return _make_request("PATCH", f"/databases/{database_id}", json=payload)


@mcp.tool()
def query_database(database_id: str, filter_properties: list = None, filter_obj: dict = None, 
                  sort_rules: list = None, start_cursor: str = None, page_size: int = 100) -> dict:
    """Query a database with optional filters and sorting."""
    payload = {}
    if filter_properties:
        payload["filter_properties"] = filter_properties
    if filter_obj:
        payload["filter"] = filter_obj
    if sort_rules:
        payload["sorts"] = sort_rules
    if start_cursor:
        payload["start_cursor"] = start_cursor
    payload["page_size"] = page_size
    return _make_request("POST", f"/databases/{database_id}/query", json=payload)


# Block endpoints
@mcp.tool()
def retrieve_block(block_id: str) -> dict:
    """Retrieve a block by its ID."""
    return _make_request("GET", f"/blocks/{block_id}")


@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: str = None, page_size: int = 100) -> dict:
    """Retrieve the children of a block."""
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str) -> dict:
    """Retrieve a specific property item from a page."""
    return _make_request("GET", f"/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def update_block(block_id: str, block_type: str, **kwargs) -> dict:
    """Update a block. block_type should be one of: paragraph, heading_1, heading_2, heading_3,
    bulleted_list_item, numbered_list_item, quote, to_do, toggle, template, callout, synced_block,
    child_page, child_database, equation, code, callout, divider, breadcrumb, table_of_contents,
    table, table_row, column_list, column, link_preview, bookmark, image, video, pdf, audio,
    embed, Unsupported, meeting_notes.
    """
    payload = {block_type: kwargs}
    return _make_request("PATCH", f"/blocks/{block_id}", json=payload)


@mcp.tool()
def delete_block(block_id: str) -> dict:
    """Delete a block."""
    return _make_request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def append_block_children(block_id: str, children: list, position: dict = None) -> dict:
    """Append children blocks to a block."""
    payload = {"children": children}
    if position:
        payload["position"] = position
    return _make_request("PATCH", f"/blocks/{block_id}/children", json=payload)


# Search endpoint
@mcp.tool()
def search(query: str = None, filter_obj: dict = None, sorts: list = None,
          start_cursor: str = None, page_size: int = 100) -> dict:
    """Search for pages and databases."""
    payload = {}
    if query:
        payload["query"] = query
    if filter_obj:
        payload["filter"] = filter_obj
    if sorts:
        payload["sorts"] = sorts
    if start_cursor:
        payload["start_cursor"] = start_cursor
    payload["page_size"] = page_size
    return _make_request("POST", "/search", json=payload)


# User endpoints
@mcp.tool()
def retrieve_user(user_id: str) -> dict:
    """Retrieve a user by their ID."""
    return _make_request("GET", f"/users/{user_id}")


@mcp.tool()
def list_users(start_cursor: str = None, page_size: int = 100) -> dict:
    """List all users accessible to the integration."""
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", "/users", params=params)


# Comment endpoints
@mcp.tool()
def create_comment(parent: dict, rich_text: list, attachments: list = None, 
                  display_name: dict = None) -> dict:
    """Create a new comment."""
    payload = {"parent": parent, "rich_text": rich_text}
    if attachments:
        payload["attachments"] = attachments
    if display_name:
        payload["display_name"] = display_name
    return _make_request("POST", "/comments", json=payload)


@mcp.tool()
def list_comments(block_id: str = None, page_id: str = None, start_cursor: str = None,
                 page_size: int = 100) -> dict:
    """List comments on a block or page."""
    if block_id:
        endpoint = f"/blocks/{block_id}/comments"
    elif page_id:
        endpoint = f"/pages/{page_id}/comments"
    else:
        endpoint = "/comments"
    
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", endpoint, params=params)


@mcp.tool()
def retrieve_comment(comment_id: str) -> dict:
    """Retrieve a comment by its ID."""
    return _make_request("GET", f"/comments/{comment_id}")


# View endpoints
@mcp.tool()
def retrieve_view(view_id: str) -> dict:
    """Retrieve a view by its ID."""
    return _make_request("GET", f"/views/{view_id}")


@mcp.tool()
def list_views(database_id: str = None, data_source_id: str = None, 
               start_cursor: str = None, page_size: int = 100) -> dict:
    """List views for a database or data source."""
    params = {"page_size": page_size}
    if database_id:
        params["database_id"] = database_id
    if data_source_id:
        params["data_source_id"] = data_source_id
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", "/views", params=params)


@mcp.tool()
def update_view(view_id: str, name: str = None, filter_obj: dict = None, 
                sorts: list = None, quick_filters: dict = None, 
                presentation: dict = None) -> dict:
    """Update a view."""
    payload = {}
    if name:
        payload["name"] = name
    if filter_obj:
        payload["filter"] = filter_obj
    if sorts:
        payload["sorts"] = sorts
    if quick_filters is not None:
        payload["quick_filters"] = quick_filters
    if presentation is not None:
        payload["presentation"] = presentation
    return _make_request("PATCH", f"/views/{view_id}", json=payload)


@mcp.tool()
def delete_view(view_id: str) -> dict:
    """Delete a view."""
    return _make_request("DELETE", f"/views/{view_id}")


# Data source endpoints
@mcp.tool()
def retrieve_data_source(data_source_id: str) -> dict:
    """Retrieve a data source by its ID."""
    return _make_request("GET", f"/data_sources/{data_source_id}")


@mcp.tool()
def create_data_source(parent: dict, properties: dict = None, title: list = None) -> dict:
    """Create a new data source."""
    payload = {"parent": parent}
    if properties:
        payload["properties"] = properties
    if title:
        payload["title"] = title
    return _make_request("POST", "/data_sources", json=payload)


@mcp.tool()
def update_data_source(data_source_id: str, title: list = None, 
                      properties: dict = None, in_trash: bool = None,
                      parent: dict = None) -> dict:
    """Update an existing data source."""
    payload = {}
    if title:
        payload["title"] = title
    if properties is not None:
        payload["properties"] = properties
    if in_trash is not None:
        payload["in_trash"] = in_trash
    if parent:
        payload["parent"] = parent
    return _make_request("PATCH", f"/data_sources/{data_source_id}", json=payload)


@mcp.tool()
def query_data_source(data_source_id: str, filter_obj: dict = None,
                     sort_rules: list = None, start_cursor: str = None,
                     page_size: int = 100) -> dict:
    """Query a data source with optional filters and sorting."""
    payload = {}
    if filter_obj:
        payload["filter"] = filter_obj
    if sort_rules:
        payload["sorts"] = sort_rules
    if start_cursor:
        payload["start_cursor"] = start_cursor
    payload["page_size"] = page_size
    return _make_request("POST", f"/data_sources/{data_source_id}/query", json=payload)


# Authentication endpoints
@mcp.tool()
def get_my_user() -> dict:
    """Retrieve the user associated with the current token."""
    return _make_request("GET", "/users/me")


@mcp.tool()
def introspect_token(client_id: str, client_secret: str, token: str) -> dict:
    """Introspect an OAuth token to check its validity and scope."""
    import base64
    auth_str = f"{client_id}:{client_secret}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Notion-Version": "2026-03-11",
        "Content-Type": "application/json"
    }
    url = f"{BASE_URL}/oauth/introspect"
    try:
        response = requests.post(url, headers=headers, json={"token": token})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e}", "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}


# File upload endpoints
@mcp.tool()
def create_file_upload(mode: str = "single_part", filename: str = None,
                       content_type: str = None, content_length: int = None,
                       number_of_parts: int = None, external_url: str = None) -> dict:
    """Create a new file upload."""
    payload = {"mode": mode}
    if filename:
        payload["filename"] = filename
    if content_type:
        payload["content_type"] = content_type
    if content_length:
        payload["content_length"] = content_length
    if number_of_parts:
        payload["number_of_parts"] = number_of_parts
    if external_url:
        payload["external_url"] = external_url
    return _make_request("POST", "/file_upload", json=payload)


@mcp.tool()
def send_file_upload(file_upload_id: str, file_data: dict, part_number: int = None) -> dict:
    """Send file data for a file upload. For multipart uploads, specify part_number."""
    endpoint = f"/file_upload/{file_upload_id}"
    headers = HEADERS.copy()
    headers["Content-Type"] = "application/octet-stream"
    
    if part_number:
        headers["X-Notion-Part-Number"] = str(part_number)
    
    url = f"{BASE_URL}{endpoint}"
    try:
        # file_data should contain the binary file contents
        response = requests.post(url, headers=headers, data=file_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e}", "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}


@mcp.tool()
def complete_file_upload(file_upload_id: str) -> dict:
    """Complete a file upload and make it available for use."""
    return _make_request("POST", f"/file_upload/{file_upload_id}/complete")


@mcp.tool()
def retrieve_file_upload(file_upload_id: str) -> dict:
    """Retrieve a file upload by its ID."""
    return _make_request("GET", f"/file_upload/{file_upload_id}")


@mcp.tool()
def list_file_uploads(status: str = None, start_cursor: str = None,
                     page_size: int = 100) -> dict:
    """List file uploads accessible to the integration."""
    params = {"page_size": page_size}
    if status:
        params["status"] = status
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", "/file_upload", params=params)


# View query endpoints
@mcp.tool()
def create_view_query(view_id: str, page_size: int = 100) -> dict:
    """Create a new view query to execute a saved view."""
    payload = {"page_size": page_size}
    return _make_request("POST", f"/views/{view_id}/queries", json=payload)


@mcp.tool()
def get_view_query_results(view_id: str, query_id: str, start_cursor: str = None,
                          page_size: int = 100) -> dict:
    """Get results for a view query."""
    params = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", f"/views/{view_id}/queries/{query_id}/results", params=params)


@mcp.tool()
def delete_view_query(view_id: str, query_id: str) -> dict:
    """Delete a view query."""
    return _make_request("DELETE", f"/views/{view_id}/queries/{query_id}")


@mcp.tool()
def list_data_source_templates(data_source_id: str, name: str = None,
                               start_cursor: str = None, page_size: int = 100) -> dict:
    """List templates for a data source."""
    params = {"page_size": page_size}
    if name:
        params["name"] = name
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _make_request("GET", f"/data_sources/{data_source_id}/templates", params=params)


if __name__ == "__main__":
    # Run the MCP server over stdio
    mcp.run()
