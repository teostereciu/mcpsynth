import os
import requests
from fastmcp import FastMCP
from typing import Optional, Dict, Any, List

mcp = FastMCP("confluence")

def get_session():
    session = requests.Session()
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    if email and token:
        session.auth = (email, token)
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json"
    })
    return session

def get_base_url():
    return os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")

def get_default_space():
    return os.environ.get("CONFLUENCE_SPACE_KEY")

def make_request(method: str, path: str, **kwargs) -> Dict[str, Any]:
    session = get_session()
    base_url = get_base_url()
    url = f"{base_url}{path}"
    
    try:
        response = session.request(method, url, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_msg = e.response.json()
            except ValueError:
                error_msg = e.response.text
        return {"error": error_msg}

def get_space_id(space_key: str) -> Optional[str]:
    res = make_request("GET", f"/api/v2/spaces?keys={space_key}")
    if "error" in res:
        return None
    results = res.get("results", [])
    if results:
        return results[0]["id"]
    return None

# --- Pages ---

@mcp.tool()
def get_page(page_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """Get a Confluence page by ID."""
    return make_request("GET", f"/api/v2/pages/{page_id}?body-format={body_format}")

@mcp.tool()
def create_page(title: str, content: str, space_key: Optional[str] = None, parent_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a new Confluence page."""
    s_key = space_key or get_default_space()
    if not s_key:
        return {"error": "space_key is required or CONFLUENCE_SPACE_KEY must be set"}
    
    space_id = get_space_id(s_key)
    if not space_id:
        return {"error": f"Could not find space ID for key {s_key}"}
        
    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content
        }
    }
    if parent_id:
        payload["parentId"] = parent_id
        
    return make_request("POST", "/api/v2/pages", json=payload)

@mcp.tool()
def update_page(page_id: str, title: str, content: str, version_number: int) -> Dict[str, Any]:
    """Update an existing Confluence page."""
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content
        },
        "version": {
            "number": version_number,
            "message": "Updated via MCP"
        }
    }
    return make_request("PUT", f"/api/v2/pages/{page_id}", json=payload)

@mcp.tool()
def delete_page(page_id: str) -> Dict[str, Any]:
    """Delete a Confluence page."""
    return make_request("DELETE", f"/api/v2/pages/{page_id}")

@mcp.tool()
def get_page_children(page_id: str) -> Dict[str, Any]:
    """Get child pages of a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/children")

@mcp.tool()
def get_page_ancestors(page_id: str) -> Dict[str, Any]:
    """Get ancestors of a Confluence page."""
    return make_request("GET", f"/rest/api/content/{page_id}?expand=ancestors")

@mcp.tool()
def move_page(page_id: str, target_parent_id: str) -> Dict[str, Any]:
    """Move a Confluence page to a new parent."""
    page = make_request("GET", f"/api/v2/pages/{page_id}")
    if "error" in page:
        return page
        
    version = page.get("version", {}).get("number", 0) + 1
    
    payload = {
        "id": page_id,
        "status": "current",
        "title": page.get("title"),
        "parentId": target_parent_id,
        "version": {
            "number": version,
            "message": "Moved via MCP"
        }
    }
    return make_request("PUT", f"/api/v2/pages/{page_id}", json=payload)

# --- Spaces ---

@mcp.tool()
def list_spaces(limit: int = 25) -> Dict[str, Any]:
    """List Confluence spaces."""
    return make_request("GET", f"/api/v2/spaces?limit={limit}")

@mcp.tool()
def get_space(space_id: str) -> Dict[str, Any]:
    """Get a Confluence space by ID."""
    return make_request("GET", f"/api/v2/spaces/{space_id}")

@mcp.tool()
def create_space(key: str, name: str, description: str = "") -> Dict[str, Any]:
    """Create a new Confluence space."""
    payload = {
        "key": key,
        "name": name,
        "description": {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
    }
    return make_request("POST", "/rest/api/space", json=payload)

@mcp.tool()
def delete_space(space_key: str) -> Dict[str, Any]:
    """Delete a Confluence space."""
    return make_request("DELETE", f"/rest/api/space/{space_key}")

# --- Search ---

@mcp.tool()
def search_content(cql: str, limit: int = 25) -> Dict[str, Any]:
    """Search Confluence content using CQL."""
    return make_request("GET", f"/rest/api/search?cql={cql}&limit={limit}")

# --- Labels ---

@mcp.tool()
def get_labels(page_id: str) -> Dict[str, Any]:
    """Get labels for a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/labels")

@mcp.tool()
def add_label(page_id: str, label: str) -> Dict[str, Any]:
    """Add a label to a Confluence page."""
    payload = [{"prefix": "global", "name": label}]
    return make_request("POST", f"/rest/api/content/{page_id}/label", json=payload)

@mcp.tool()
def remove_label(page_id: str, label: str) -> Dict[str, Any]:
    """Remove a label from a Confluence page."""
    return make_request("DELETE", f"/rest/api/content/{page_id}/label/{label}")

# --- Attachments ---

@mcp.tool()
def list_attachments(page_id: str) -> Dict[str, Any]:
    """List attachments for a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/attachments")

@mcp.tool()
def upload_attachment(page_id: str, file_path: str, comment: str = "") -> Dict[str, Any]:
    """Upload an attachment to a Confluence page."""
    session = get_session()
    base_url = get_base_url()
    url = f"{base_url}/rest/api/content/{page_id}/child/attachment"
    
    session.headers.update({"X-Atlassian-Token": "nocheck"})
    session.headers.pop("Content-Type", None)
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            data = {"comment": comment}
            response = session.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def download_attachment(attachment_id: str, save_path: str) -> Dict[str, Any]:
    """Download an attachment by ID."""
    # First get attachment metadata to find download URL
    meta = make_request("GET", f"/api/v2/attachments/{attachment_id}")
    if "error" in meta:
        return meta
        
    download_path = meta.get("downloadLink")
    if not download_path:
        return {"error": "Could not find download link"}
        
    session = get_session()
    base_url = get_base_url()
    url = f"{base_url}{download_path}"
    
    try:
        response = session.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return {"status": "success", "saved_to": save_path}
    except Exception as e:
        return {"error": str(e)}

# --- Comments ---

@mcp.tool()
def get_comments(page_id: str) -> Dict[str, Any]:
    """Get comments for a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/footer-comments")

@mcp.tool()
def create_footer_comment(page_id: str, content: str) -> Dict[str, Any]:
    """Create a footer comment on a Confluence page."""
    payload = {
        "pageId": page_id,
        "body": {
            "representation": "storage",
            "value": content
        }
    }
    return make_request("POST", "/api/v2/footer-comments", json=payload)

@mcp.tool()
def create_inline_comment(page_id: str, content: str, inline_marker_ref: str) -> Dict[str, Any]:
    """Create an inline comment on a Confluence page."""
    payload = {
        "containerId": page_id,
        "containerType": "page",
        "body": {
            "representation": "storage",
            "value": content
        },
        "inlineMarkerRef": inline_marker_ref
    }
    return make_request("POST", "/rest/api/content", json=payload) # v1 for inline comments is complex, v2 might not support it fully. Let's use v1 content creation for comment.
    # Actually, v1 comment creation: POST /rest/api/content
    # {"type": "comment", "container": {"id": page_id, "type": "page"}, "body": {"storage": {"value": content, "representation": "storage"}}}

# Let's fix create_inline_comment
@mcp.tool()
def create_comment(page_id: str, content: str, parent_comment_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a comment on a Confluence page."""
    payload = {
        "type": "comment",
        "container": {
            "id": page_id,
            "type": "page"
        },
        "body": {
            "storage": {
                "value": content,
                "representation": "storage"
            }
        }
    }
    if parent_comment_id:
        payload["ancestors"] = [{"id": parent_comment_id}]
    return make_request("POST", "/rest/api/content", json=payload)

# --- Versions ---

@mcp.tool()
def get_page_versions(page_id: str) -> Dict[str, Any]:
    """Get versions of a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/versions")

@mcp.tool()
def get_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    """Get a specific version of a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")

@mcp.tool()
def restore_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    """Restore a Confluence page to a previous version."""
    payload = {
        "version": {
            "number": version_number
        },
        "message": f"Restored to version {version_number} via MCP"
    }
    return make_request("POST", f"/rest/api/content/{page_id}/version", json=payload)

# --- Content Properties ---

@mcp.tool()
def get_content_properties(page_id: str) -> Dict[str, Any]:
    """Get content properties for a Confluence page."""
    return make_request("GET", f"/api/v2/pages/{page_id}/properties")

@mcp.tool()
def set_content_property(page_id: str, key: str, value: Any) -> Dict[str, Any]:
    """Set a content property on a Confluence page."""
    payload = {
        "key": key,
        "value": value
    }
    return make_request("POST", f"/api/v2/pages/{page_id}/properties", json=payload)

# --- Blog Posts ---

@mcp.tool()
def get_blog_post(blog_id: str) -> Dict[str, Any]:
    """Get a Confluence blog post by ID."""
    return make_request("GET", f"/api/v2/blogposts/{blog_id}")

@mcp.tool()
def create_blog_post(title: str, content: str, space_key: Optional[str] = None) -> Dict[str, Any]:
    """Create a new Confluence blog post."""
    s_key = space_key or get_default_space()
    if not s_key:
        return {"error": "space_key is required or CONFLUENCE_SPACE_KEY must be set"}
    
    space_id = get_space_id(s_key)
    if not space_id:
        return {"error": f"Could not find space ID for key {s_key}"}
        
    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content
        }
    }
    return make_request("POST", "/api/v2/blogposts", json=payload)

@mcp.tool()
def update_blog_post(blog_id: str, title: str, content: str, version_number: int) -> Dict[str, Any]:
    """Update an existing Confluence blog post."""
    payload = {
        "id": blog_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content
        },
        "version": {
            "number": version_number,
            "message": "Updated via MCP"
        }
    }
    return make_request("PUT", f"/api/v2/blogposts/{blog_id}", json=payload)

@mcp.tool()
def delete_blog_post(blog_id: str) -> Dict[str, Any]:
    """Delete a Confluence blog post."""
    return make_request("DELETE", f"/api/v2/blogposts/{blog_id}")

# --- Users ---

@mcp.tool()
def get_current_user() -> Dict[str, Any]:
    """Get the current authenticated user."""
    return make_request("GET", "/rest/api/user/current")

@mcp.tool()
def get_user(account_id: str) -> Dict[str, Any]:
    """Get a user by account ID."""
    return make_request("GET", f"/rest/api/user?accountId={account_id}")

if __name__ == "__main__":
    mcp.run()
