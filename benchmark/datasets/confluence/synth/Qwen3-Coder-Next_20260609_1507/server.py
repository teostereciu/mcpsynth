#!/usr/bin/env python3
"""
MCP Server for Confluence Cloud REST API

This server provides tools to interact with Confluence Cloud using the REST API.
It supports both v1 (/wiki/rest/api/) and v2 (/wiki/api/v2/) endpoints.
"""

import os
import json
import requests
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("confluence")

# Configuration from environment variables
BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://yoursite.atlassian.net/wiki")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "SYNTH")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

# Auth header for Basic Auth
AUTH = (EMAIL, API_TOKEN) if EMAIL and API_TOKEN else None

# Base API URLs
V1_API_URL = f"{BASE_URL}/rest/api"
V2_API_URL = f"{BASE_URL}/api/v2"


def _make_request(method: str, path: str, params: Dict[str, Any] = None, 
                  data: Dict[str, Any] = None, v2: bool = False) -> Dict[str, Any]:
    """Make an authenticated request to the Confluence API."""
    base_url = V2_API_URL if v2 else V1_API_URL
    url = f"{base_url}{path}"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=headers,
            auth=AUTH,
            timeout=60
        )
        
        if response.status_code >= 400:
            return {
                "error": f"API request failed with status {response.status_code}",
                "status_code": response.status_code,
                "response": response.text[:500]
            }
        
        if response.status_code == 204:  # No content
            return {"success": True}
            
        return response.json() if response.content else {"success": True}
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ==================== SPACE OPERATIONS ====================

@mcp.tool()
def list_spaces(
    limit: int = 25,
    start: int = 0,
    type: str = "global",
    status: str = "current",
    labels: str = None
) -> Dict[str, Any]:
    """List spaces in Confluence."""
    params = {
        "limit": limit,
        "start": start,
        "type": type,
        "status": status
    }
    if labels:
        params["labels"] = labels
    
    return _make_request("GET", "/space", params=params, v2=True)


@mcp.tool()
def get_space_by_key(space_key: str) -> Dict[str, Any]:
    """Get a space by its key."""
    return _make_request("GET", f"/space/{space_key}", v2=True)


@mcp.tool()
def create_space(name: str, key: str, description: str = None) -> Dict[str, Any]:
    """Create a new space."""
    data = {"name": name, "key": key}
    if description:
        data["description"] = {"plain": {"value": description, "representation": "plain"}}
    return _make_request("POST", "/space", data=data, v2=True)


@mcp.tool()
def delete_space(space_key: str) -> Dict[str, Any]:
    """Delete a space."""
    return _make_request("DELETE", f"/space/{space_key}", v2=True)


# ==================== PAGE OPERATIONS ====================

@mcp.tool()
def list_pages(
    space_id: str = None,
    limit: int = 25,
    start: int = 0,
    status: str = "current"
) -> Dict[str, Any]:
    """List pages in Confluence."""
    if space_id is None:
        space = get_space_by_key(SPACE_KEY)
        if "id" in space:
            space_id = space["id"]
        else:
            return {"error": "Could not determine space ID. Please specify space_id parameter."}
    
    params = {"space-id": space_id, "limit": limit, "start": start, "status": status}
    return _make_request("GET", "/pages", params=params, v2=True)


@mcp.tool()
def get_page_by_id(page_id: str) -> Dict[str, Any]:
    """Get a page by its ID."""
    return _make_request("GET", f"/pages/{page_id}", v2=True)


@mcp.tool()
def create_page(
    space_id: str,
    title: str,
    body: str,
    parent_id: str = None,
    status: str = "current"
) -> Dict[str, Any]:
    """Create a new page."""
    data = {
        "spaceId": space_id,
        "title": title,
        "body": {"storage": {"value": body, "representation": "storage"}},
        "status": status
    }
    if parent_id:
        data["parentId"] = parent_id
    return _make_request("POST", "/pages", data=data, v2=True)


@mcp.tool()
def update_page(
    page_id: str,
    title: str,
    body: str,
    version_number: int,
    version_message: str = None
) -> Dict[str, Any]:
    """Update an existing page."""
    data = {
        "id": page_id,
        "title": title,
        "body": {"storage": {"value": body, "representation": "storage"}},
        "version": {"number": version_number + 1}
    }
    if version_message:
        data["version"]["message"] = version_message
    return _make_request("PUT", f"/pages/{page_id}", data=data, v2=True)


@mcp.tool()
def delete_page(page_id: str, purge: bool = False, draft: bool = False) -> Dict[str, Any]:
    """Delete a page."""
    params = {}
    if purge:
        params["purge"] = True
    if draft:
        params["draft"] = True
    return _make_request("DELETE", f"/pages/{page_id}", params=params, v2=True)


@mcp.tool()
def get_page_by_title(space_key: str, title: str) -> Dict[str, Any]:
    """Get a page by its title within a space."""
    search_result = search_content(f'title="{title}" AND space="{space_key}"')
    if "results" in search_result and search_result["results"]:
        return search_result["results"][0]
    return {"error": f"Page '{title}' not found in space '{space_key}'"}


# ==================== SEARCH OPERATIONS ====================

@mcp.tool()
def search_content(
    cql: str,
    cql_context: str = None,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """Search content using Confluence Query Language (CQL)."""
    params = {"cql": cql, "limit": limit, "start": start}
    if cql_context:
        params["cqlcontext"] = cql_context
    return _make_request("GET", "/search", params=params, v2=False)


@mcp.tool()
def search_users(
    cql: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """Search users using CQL."""
    params = {"cql": cql, "limit": limit, "start": start}
    return _make_request("GET", "/search/user", params=params, v2=False)


# ==================== LABEL OPERATIONS ====================

@mcp.tool()
def add_label(
    content_id: str,
    label: str,
    prefix: str = "global"
) -> Dict[str, Any]:
    """Add a label to content."""
    labels = _make_request("GET", f"/labels/{content_id}/labels", v2=True)
    if "results" in labels:
        for existing_label in labels["results"]:
            if existing_label.get("name") == label and existing_label.get("prefix") == prefix:
                return {"error": f"Label '{label}' already exists"}
    
    data = {"name": label, "prefix": prefix}
    return _make_request("POST", f"/labels/{content_id}/labels", data=data, v2=True)


@mcp.tool()
def list_labels(
    content_id: str,
    prefix: str = None
) -> Dict[str, Any]:
    """List labels on content."""
    params = {}
    if prefix:
        params["prefix"] = prefix
    return _make_request("GET", f"/labels/{content_id}/labels", params=params, v2=True)


@mcp.tool()
def remove_label(
    content_id: str,
    label_name: str,
    prefix: str = "global"
) -> Dict[str, Any]:
    """Remove a label from content."""
    labels = list_labels(content_id, prefix)
    if "error" in labels:
        return labels
    
    label_id = None
    if "results" in labels:
        for label in labels["results"]:
            if label.get("name") == label_name and label.get("prefix") == prefix:
                label_id = label.get("id")
                break
    
    if not label_id:
        return {"error": f"Label '{label_name}' not found"}
    return _make_request("DELETE", f"/labels/{label_id}", v2=True)


# ==================== COMMENT OPERATIONS ====================

@mcp.tool()
def list_footer_comments(
    page_id: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List footer comments on a page."""
    params = {"limit": limit, "start": start}
    return _make_request("GET", f"/pages/{page_id}/footer-comments", params=params, v2=True)


@mcp.tool()
def create_footer_comment(
    page_id: str,
    body: str
) -> Dict[str, Any]:
    """Create a footer comment on a page."""
    data = {
        "pageId": page_id,
        "body": {"storage": {"value": body, "representation": "storage"}}
    }
    return _make_request("POST", "/footer-comments", data=data, v2=True)


@mcp.tool()
def list_inline_comments(
    page_id: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List inline comments on a page."""
    params = {"limit": limit, "start": start}
    return _make_request("GET", f"/pages/{page_id}/inline-comments", params=params, v2=True)


@mcp.tool()
def create_inline_comment(
    page_id: str,
    body: str,
    inline_marker_ref: str = None
) -> Dict[str, Any]:
    """Create an inline comment on a page."""
    data = {
        "pageId": page_id,
        "body": {"storage": {"value": body, "representation": "storage"}}
    }
    if inline_marker_ref:
        data["properties"] = {"inlineMarkerRef": inline_marker_ref}
    return _make_request("POST", "/inline-comments", data=data, v2=True)


# ==================== CONTENT PROPERTIES ====================

@mcp.tool()
def list_content_properties(
    content_id: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List properties for content."""
    if content_id.startswith("attachment:"):
        path = f"/attachments/{content_id}/properties"
    elif content_id.startswith("comment:"):
        path = f"/comments/{content_id}/properties"
    else:
        path = f"/pages/{content_id}/properties"
    
    params = {"limit": limit, "start": start}
    return _make_request("GET", path, params=params, v2=True)


@mcp.tool()
def get_content_property(
    content_id: str,
    property_key: str
) -> Dict[str, Any]:
    """Get a specific property for content."""
    if content_id.startswith("attachment:"):
        path = f"/attachments/{content_id}/properties/{property_key}"
    elif content_id.startswith("comment:"):
        path = f"/comments/{content_id}/properties/{property_key}"
    else:
        path = f"/pages/{content_id}/properties/{property_key}"
    
    return _make_request("GET", path, v2=True)


@mcp.tool()
def set_content_property(
    content_id: str,
    property_key: str,
    property_value: Any
) -> Dict[str, Any]:
    """Set a property for content."""
    if content_id.startswith("attachment:"):
        path = f"/attachments/{content_id}/properties"
    elif content_id.startswith("comment:"):
        path = f"/comments/{content_id}/properties"
    else:
        path = f"/pages/{content_id}/properties"
    
    data = {"key": property_key, "value": property_value}
    return _make_request("POST", path, data=data, v2=True)


@mcp.tool()
def delete_content_property(
    content_id: str,
    property_key: str
) -> Dict[str, Any]:
    """Delete a property from content."""
    prop = get_content_property(content_id, property_key)
    if "error" in prop:
        return prop
    
    prop_id = prop.get("id")
    if not prop_id:
        return {"error": "Property ID not found"}
    
    if content_id.startswith("attachment:"):
        path = f"/attachments/{content_id}/properties/{prop_id}"
    elif content_id.startswith("comment:"):
        path = f"/comments/{content_id}/properties/{prop_id}"
    else:
        path = f"/pages/{content_id}/properties/{prop_id}"
    
    return _make_request("DELETE", path, v2=True)


# ==================== ATTACHMENT OPERATIONS ====================

@mcp.tool()
def list_attachments(
    page_id: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List attachments on a page."""
    params = {"limit": limit, "start": start}
    return _make_request("GET", f"/pages/{page_id}/attachments", params=params, v2=True)


@mcp.tool()
def get_attachment_by_id(attachment_id: str) -> Dict[str, Any]:
    """Get an attachment by its ID."""
    return _make_request("GET", f"/attachments/{attachment_id}", v2=True)


@mcp.tool()
def create_attachment(
    page_id: str,
    file_path: str,
    file_name: str,
    content_type: str = "application/octet-stream"
) -> Dict[str, Any]:
    """Create an attachment by uploading a file."""
    return {"error": "File upload not yet implemented. Use multipart/form-data request."}


# ==================== USER OPERATIONS ====================

@mcp.tool()
def get_current_user() -> Dict[str, Any]:
    """Get the current authenticated user."""
    return _make_request("GET", "/user/current", v2=False)


@mcp.tool()
def get_user_by_account_id(account_id: str) -> Dict[str, Any]:
    """Get a user by their account ID."""
    params = {"accountId": account_id}
    return _make_request("GET", "/user", params=params, v2=False)


@mcp.tool()
def bulk_get_users(
    account_ids: List[str]
) -> Dict[str, Any]:
    """Get multiple users by their account IDs."""
    data = {"accountIds": account_ids}
    return _make_request("POST", "/users-bulk", data=data, v2=True)


# ==================== SPACE PROPERTIES ====================

@mcp.tool()
def list_space_properties(
    space_key: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List properties for a space."""
    space = get_space_by_key(space_key)
    if "error" in space:
        return space
    
    space_id = space.get("id")
    if not space_id:
        return {"error": "Space ID not found"}
    
    params = {"limit": limit, "start": start}
    return _make_request("GET", f"/spaces/{space_id}/properties", params=params, v2=True)


@mcp.tool()
def get_space_property(
    space_key: str,
    property_key: str
) -> Dict[str, Any]:
    """Get a specific property for a space."""
    space = get_space_by_key(space_key)
    if "error" in space:
        return space
    
    space_id = space.get("id")
    if not space_id:
        return {"error": "Space ID not found"}
    
    return _make_request("GET", f"/spaces/{space_id}/properties/{property_key}", v2=True)


@mcp.tool()
def set_space_property(
    space_key: str,
    property_key: str,
    property_value: Any
) -> Dict[str, Any]:
    """Set a property for a space."""
    space = get_space_by_key(space_key)
    if "error" in space:
        return space
    
    space_id = space.get("id")
    if not space_id:
        return {"error": "Space ID not found"}
    
    data = {"key": property_key, "value": property_value}
    return _make_request("POST", f"/spaces/{space_id}/properties", data=data, v2=True)


@mcp.tool()
def delete_space_property(
    space_key: str,
    property_key: str
) -> Dict[str, Any]:
    """Delete a property from a space."""
    space = get_space_by_key(space_key)
    if "error" in space:
        return space
    
    space_id = space.get("id")
    if not space_id:
        return {"error": "Space ID not found"}
    
    prop = get_space_property(space_key, property_key)
    if "error" in prop:
        return prop
    
    prop_id = prop.get("id")
    if not prop_id:
        return {"error": "Property ID not found"}
    
    return _make_request("DELETE", f"/spaces/{space_id}/properties/{prop_id}", v2=True)


# ==================== SPACE PERMISSIONS ====================

@mcp.tool()
def list_space_permissions(
    space_key: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List permissions for a space."""
    space = get_space_by_key(space_key)
    if "error" in space:
        return space
    
    space_id = space.get("id")
    if not space_id:
        return {"error": "Space ID not found"}
    
    params = {"limit": limit, "start": start}
    return _make_request("GET", f"/spaces/{space_id}/permissions", params=params, v2=True)


@mcp.tool()
def add_space_permission(
    space_key: str,
    principal_type: str,
    principal_id: str,
    operation: str = "use",
    target_type: str = "page"
) -> Dict[str, Any]:
    """Add a permission to a space."""
    space = get_space_by_key(space_key)
    if "error" in space:
        return space
    
    space_id = space.get("id")
    if not space_id:
        return {"error": "Space ID not found"}
    
    data = {
        "principal": {"principalType": principal_type, "principalId": principal_id},
        "permission": {"key": operation, "targetType": target_type}
    }
    return _make_request("POST", f"/spaces/{space_id}/permissions", data=data, v2=True)


# ==================== VERSION OPERATIONS ====================

@mcp.tool()
def list_page_versions(
    page_id: str,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """List versions of a page."""
    params = {"limit": limit, "start": start}
    return _make_request("GET", f"/pages/{page_id}/versions", params=params, v2=True)


@mcp.tool()
def get_page_version(
    page_id: str,
    version_number: int
) -> Dict[str, Any]:
    """Get a specific version of a page."""
    return _make_request("GET", f"/pages/{page_id}/versions/{version_number}", v2=True)


# ==================== LABEL SEARCH ====================

@mcp.tool()
def search_labels(
    prefix: str = None,
    label_id: str = None,
    limit: int = 25,
    start: int = 0
) -> Dict[str, Any]:
    """Search labels."""
    params = {"limit": limit, "start": start}
    if prefix:
        params["prefix"] = prefix
    if label_id:
        params["label-id"] = label_id
    return _make_request("GET", "/labels", params=params, v2=True)


# Run the server
if __name__ == "__main__":
    mcp.run()
