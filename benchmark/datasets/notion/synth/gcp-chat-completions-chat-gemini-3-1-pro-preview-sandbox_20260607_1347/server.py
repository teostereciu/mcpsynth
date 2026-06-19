import os
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("notion")

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
BASE_URL = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def make_request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, headers=HEADERS, **kwargs)
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
def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[List[Dict[str, Any]]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a new page in a database or as a child of an existing page."""
    payload = {
        "parent": parent,
        "properties": properties
    }
    if children:
        payload["children"] = children
    if icon:
        payload["icon"] = icon
    if cover:
        payload["cover"] = cover
    return make_request("POST", "/pages", json=payload)

@mcp.tool()
def retrieve_page(page_id: str) -> Dict[str, Any]:
    """Retrieve a page by ID."""
    return make_request("GET", f"/pages/{page_id}")

@mcp.tool()
def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update page properties, icon, cover, or archive status."""
    payload = {}
    if properties is not None:
        payload["properties"] = properties
    if archived is not None:
        payload["archived"] = archived
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    return make_request("PATCH", f"/pages/{page_id}", json=payload)

@mcp.tool()
def archive_page(page_id: str) -> Dict[str, Any]:
    """Archive a page by ID."""
    return make_request("PATCH", f"/pages/{page_id}", json={"archived": True})

@mcp.tool()
def create_database(parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new database as a child of an existing page."""
    payload = {
        "parent": parent,
        "title": title,
        "properties": properties
    }
    return make_request("POST", "/databases", json=payload)

@mcp.tool()
def query_database(database_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[List[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """Query a database for pages."""
    payload = {}
    if filter:
        payload["filter"] = filter
    if sorts:
        payload["sorts"] = sorts
    if start_cursor:
        payload["start_cursor"] = start_cursor
    if page_size:
        payload["page_size"] = page_size
    return make_request("POST", f"/databases/{database_id}/query", json=payload)

@mcp.tool()
def retrieve_database(database_id: str) -> Dict[str, Any]:
    """Retrieve a database by ID."""
    return make_request("GET", f"/databases/{database_id}")

@mcp.tool()
def update_database(database_id: str, title: Optional[List[Dict[str, Any]]] = None, description: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update a database's title, description, or properties."""
    payload = {}
    if title is not None:
        payload["title"] = title
    if description is not None:
        payload["description"] = description
    if properties is not None:
        payload["properties"] = properties
    return make_request("PATCH", f"/databases/{database_id}", json=payload)

@mcp.tool()
def retrieve_block(block_id: str) -> Dict[str, Any]:
    """Retrieve a block by ID."""
    return make_request("GET", f"/blocks/{block_id}")

@mcp.tool()
def update_block(block_id: str, block_type: str, block_data: Dict[str, Any]) -> Dict[str, Any]:
    """Update a block's content."""
    payload = {block_type: block_data}
    return make_request("PATCH", f"/blocks/{block_id}", json=payload)

@mcp.tool()
def retrieve_block_children(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """Retrieve children of a block."""
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    return make_request("GET", f"/blocks/{block_id}/children", params=params)

@mcp.tool()
def append_block_children(block_id: str, children: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Append children to a block."""
    return make_request("PATCH", f"/blocks/{block_id}/children", json={"children": children})

@mcp.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    """Delete (archive) a block."""
    return make_request("DELETE", f"/blocks/{block_id}")

@mcp.tool()
def create_comment(rich_text: List[Dict[str, Any]], parent: Optional[Dict[str, Any]] = None, discussion_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a comment on a page or existing discussion."""
    payload = {
        "rich_text": rich_text
    }
    if parent:
        payload["parent"] = parent
    if discussion_id:
        payload["discussion_id"] = discussion_id
    return make_request("POST", "/comments", json=payload)

@mcp.tool()
def list_comments(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """List comments on a block."""
    params = {"block_id": block_id}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    return make_request("GET", "/comments", params=params)

@mcp.tool()
def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """List all users."""
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size
    return make_request("GET", "/users", params=params)

@mcp.tool()
def get_user(user_id: str) -> Dict[str, Any]:
    """Retrieve a user by ID."""
    return make_request("GET", f"/users/{user_id}")

@mcp.tool()
def get_self() -> Dict[str, Any]:
    """Retrieve the bot user associated with the API token."""
    return make_request("GET", "/users/me")

@mcp.tool()
def search(query: Optional[str] = None, sort: Optional[Dict[str, Any]] = None, filter: Optional[Dict[str, Any]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """Search all pages and databases."""
    payload = {}
    if query is not None:
        payload["query"] = query
    if sort is not None:
        payload["sort"] = sort
    if filter is not None:
        payload["filter"] = filter
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    if page_size is not None:
        payload["page_size"] = page_size
    return make_request("POST", "/search", json=payload)

if __name__ == "__main__":
    mcp.run()