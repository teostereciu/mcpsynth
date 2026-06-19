import os
import json
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Notion")

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

def _request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    if not NOTION_API_KEY:
        return {"error": "NOTION_API_KEY environment variable is not set"}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
    }
    
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
        
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        if response.status_code == 204:
            return {"success": True}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[List[Dict[str, Any]]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a new page in a database or as a child of an existing page."""
    data = {"parent": parent, "properties": properties}
    if children:
        data["children"] = children
    if icon:
        data["icon"] = icon
    if cover:
        data["cover"] = cover
    return _request("POST", "/pages", json=data)

@mcp.tool()
def retrieve_page(page_id: str) -> Dict[str, Any]:
    """Retrieve a page object using its ID."""
    return _request("GET", f"/pages/{page_id}")

@mcp.tool()
def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update page properties, icon, cover, or archive status."""
    data = {}
    if properties is not None:
        data["properties"] = properties
    if archived is not None:
        data["archived"] = archived
    if icon is not None:
        data["icon"] = icon
    if cover is not None:
        data["cover"] = cover
    return _request("PATCH", f"/pages/{page_id}", json=data)

@mcp.tool()
def archive_page(page_id: str) -> Dict[str, Any]:
    """Archive a page (move it to trash)."""
    return _request("PATCH", f"/pages/{page_id}", json={"archived": True})

@mcp.tool()
def create_database(parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new database as a subpage of a given page."""
    data = {"parent": parent, "title": title, "properties": properties}
    return _request("POST", "/databases", json=data)

@mcp.tool()
def retrieve_database(database_id: str) -> Dict[str, Any]:
    """Retrieve a database object using its ID."""
    return _request("GET", f"/databases/{database_id}")

@mcp.tool()
def query_database(database_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[List[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = 100) -> Dict[str, Any]:
    """Query a database for pages, with optional filters and sorts."""
    data = {}
    if filter:
        data["filter"] = filter
    if sorts:
        data["sorts"] = sorts
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    return _request("POST", f"/databases/{database_id}/query", json=data)

@mcp.tool()
def update_database(database_id: str, title: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update a database's title or property schema."""
    data = {}
    if title is not None:
        data["title"] = title
    if properties is not None:
        data["properties"] = properties
    return _request("PATCH", f"/databases/{database_id}", json=data)

@mcp.tool()
def retrieve_block(block_id: str) -> Dict[str, Any]:
    """Retrieve a block object using its ID."""
    return _request("GET", f"/blocks/{block_id}")

@mcp.tool()
def update_block(block_id: str, block_type: str, block_data: Dict[str, Any]) -> Dict[str, Any]:
    """Update the content of a specific block."""
    data = {block_type: block_data}
    return _request("PATCH", f"/blocks/{block_id}", json=data)

@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = 100) -> Dict[str, Any]:
    """Retrieve the children blocks of a given block."""
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    return _request("GET", f"/blocks/{block_id}/children", params=params)

@mcp.tool()
def append_block_children(block_id: str, children: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Append new children blocks to a given block."""
    return _request("PATCH", f"/blocks/{block_id}/children", json={"children": children})

@mcp.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    """Delete (archive) a block."""
    return _request("DELETE", f"/blocks/{block_id}")

@mcp.tool()
def create_comment(parent: Dict[str, Any], rich_text: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create a new comment on a page or discussion."""
    data = {"parent": parent, "rich_text": rich_text}
    return _request("POST", "/comments", json=data)

@mcp.tool()
def retrieve_comments(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = 100) -> Dict[str, Any]:
    """Retrieve comments for a given block or page."""
    params = {"block_id": block_id}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    return _request("GET", "/comments", params=params)

@mcp.tool()
def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = 100) -> Dict[str, Any]:
    """List all users in the workspace."""
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    return _request("GET", "/users", params=params)

@mcp.tool()
def retrieve_user(user_id: str) -> Dict[str, Any]:
    """Retrieve a user object using their ID."""
    return _request("GET", f"/users/{user_id}")

@mcp.tool()
def get_bot_user() -> Dict[str, Any]:
    """Retrieve the bot user associated with the API token."""
    return _request("GET", "/users/me")

@mcp.tool()
def search(query: Optional[str] = None, sort: Optional[Dict[str, Any]] = None, filter: Optional[Dict[str, Any]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = 100) -> Dict[str, Any]:
    """Search for pages and databases in the workspace."""
    data = {}
    if query:
        data["query"] = query
    if sort:
        data["sort"] = sort
    if filter:
        data["filter"] = filter
    if start_cursor:
        data["start_cursor"] = start_cursor
    if page_size:
        data["page_size"] = page_size
    return _request("POST", "/search", json=data)

if __name__ == "__main__":
    mcp.run()
