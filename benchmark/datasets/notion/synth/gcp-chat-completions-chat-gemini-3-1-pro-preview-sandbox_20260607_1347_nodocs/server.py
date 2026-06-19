import os
import requests
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP

mcp = FastMCP("Notion")

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"

def get_headers() -> Dict[str, str]:
    if not NOTION_API_KEY:
        raise ValueError("NOTION_API_KEY environment variable is not set")
    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, headers=get_headers(), **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

@mcp.tool()
def search(query: Optional[str] = None, filter: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """Search all pages and databases in the workspace."""
    payload = {}
    if query is not None: payload["query"] = query
    if filter is not None: payload["filter"] = filter
    if sort is not None: payload["sort"] = sort
    if start_cursor is not None: payload["start_cursor"] = start_cursor
    if page_size is not None: payload["page_size"] = page_size
    return make_request("POST", "/search", json=payload)

@mcp.tool()
def retrieve_page(page_id: str) -> Any:
    """Retrieve a page by ID."""
    return make_request("GET", f"/pages/{page_id}")

@mcp.tool()
def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[List[Dict[str, Any]]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """Create a new page."""
    payload = {"parent": parent, "properties": properties}
    if children is not None: payload["children"] = children
    if icon is not None: payload["icon"] = icon
    if cover is not None: payload["cover"] = cover
    return make_request("POST", "/pages", json=payload)

@mcp.tool()
def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """Update page properties, icon, cover, or archive status."""
    payload = {}
    if properties is not None: payload["properties"] = properties
    if archived is not None: payload["archived"] = archived
    if icon is not None: payload["icon"] = icon
    if cover is not None: payload["cover"] = cover
    return make_request("PATCH", f"/pages/{page_id}", json=payload)

@mcp.tool()
def retrieve_database(database_id: str) -> Any:
    """Retrieve a database by ID."""
    return make_request("GET", f"/databases/{database_id}")

@mcp.tool()
def query_database(database_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[List[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """Query a database."""
    payload = {}
    if filter is not None: payload["filter"] = filter
    if sorts is not None: payload["sorts"] = sorts
    if start_cursor is not None: payload["start_cursor"] = start_cursor
    if page_size is not None: payload["page_size"] = page_size
    return make_request("POST", f"/databases/{database_id}/query", json=payload)

@mcp.tool()
def create_database(parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any]) -> Any:
    """Create a new database."""
    payload = {"parent": parent, "title": title, "properties": properties}
    return make_request("POST", "/databases", json=payload)

@mcp.tool()
def update_database(database_id: str, title: Optional[List[Dict[str, Any]]] = None, description: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None) -> Any:
    """Update a database."""
    payload = {}
    if title is not None: payload["title"] = title
    if description is not None: payload["description"] = description
    if properties is not None: payload["properties"] = properties
    return make_request("PATCH", f"/databases/{database_id}", json=payload)

@mcp.tool()
def retrieve_block(block_id: str) -> Any:
    """Retrieve a block by ID."""
    return make_request("GET", f"/blocks/{block_id}")

@mcp.tool()
def update_block(block_id: str, block_type: str, block_data: Dict[str, Any], archived: Optional[bool] = None) -> Any:
    """Update a block."""
    payload = {block_type: block_data}
    if archived is not None: payload["archived"] = archived
    return make_request("PATCH", f"/blocks/{block_id}", json=payload)

@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """Retrieve block children."""
    params = {}
    if start_cursor is not None: params["start_cursor"] = start_cursor
    if page_size is not None: params["page_size"] = page_size
    return make_request("GET", f"/blocks/{block_id}/children", params=params)

@mcp.tool()
def append_block_children(block_id: str, children: List[Dict[str, Any]]) -> Any:
    """Append block children."""
    payload = {"children": children}
    return make_request("PATCH", f"/blocks/{block_id}/children", json=payload)

@mcp.tool()
def delete_block(block_id: str) -> Any:
    """Delete a block."""
    return make_request("DELETE", f"/blocks/{block_id}")

@mcp.tool()
def retrieve_user(user_id: str) -> Any:
    """Retrieve a user by ID."""
    return make_request("GET", f"/users/{user_id}")

@mcp.tool()
def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """List all users."""
    params = {}
    if start_cursor is not None: params["start_cursor"] = start_cursor
    if page_size is not None: params["page_size"] = page_size
    return make_request("GET", "/users", params=params)

@mcp.tool()
def retrieve_comments(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """Retrieve comments for a block."""
    params = {"block_id": block_id}
    if start_cursor is not None: params["start_cursor"] = start_cursor
    if page_size is not None: params["page_size"] = page_size
    return make_request("GET", "/comments", params=params)

@mcp.tool()
def create_comment(parent: Dict[str, Any], rich_text: List[Dict[str, Any]], discussion_id: Optional[str] = None) -> Any:
    """Create a comment."""
    payload = {"parent": parent, "rich_text": rich_text}
    if discussion_id is not None: payload["discussion_id"] = discussion_id
    return make_request("POST", "/comments", json=payload)

if __name__ == "__main__":
    mcp.run()
