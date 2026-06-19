import os
import requests
from typing import Any, Dict, Optional, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Confluence")

class ConfluenceClient:
    def __init__(self):
        self.base_url = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
        self.space_key = os.environ.get("CONFLUENCE_SPACE_KEY", "")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.api_token = os.environ.get("JIRA_API_TOKEN", "")
        
        if not self.base_url or not self.email or not self.api_token:
            raise ValueError("Missing required environment variables: CONFLUENCE_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN")

    def request(self, method: str, path: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None, data: Any = None, headers: Optional[Dict] = None, files: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        auth = (self.email, self.api_token)
        
        req_headers = {"Accept": "application/json"}
        if json_data is not None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update(headers)
            
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=auth,
                params=params,
                json=json_data,
                data=data,
                headers=req_headers,
                files=files
            )
            
            if response.status_code == 204:
                return {"success": True}
                
            if response.headers.get("Content-Type", "").startswith("application/json"):
                data = response.json()
                if not response.ok:
                    return {"error": f"HTTP {response.status_code}", "details": data}
                return data
            else:
                if not response.ok:
                    return {"error": f"HTTP {response.status_code}", "details": response.text}
                return {"success": True, "content": response.text}
                
        except Exception as e:
            return {"error": str(e)}

client = ConfluenceClient()

# Pages
@mcp.tool()
def create_page(title: str, content: str, space_id: str, parent_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a new page."""
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
    return client.request("POST", "/api/v2/pages", json_data=payload)

@mcp.tool()
def get_page(page_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """Get a page by ID."""
    return client.request("GET", f"/api/v2/pages/{page_id}", params={"body-format": body_format})

@mcp.tool()
def update_page(page_id: str, title: str, content: str, version_number: int, space_id: str) -> Dict[str, Any]:
    """Update an existing page."""
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "spaceId": space_id,
        "body": {
            "representation": "storage",
            "value": content
        },
        "version": {
            "number": version_number
        }
    }
    return client.request("PUT", f"/api/v2/pages/{page_id}", json_data=payload)

@mcp.tool()
def delete_page(page_id: str) -> Dict[str, Any]:
    """Delete a page."""
    return client.request("DELETE", f"/api/v2/pages/{page_id}")

@mcp.tool()
def get_page_children(page_id: str) -> Dict[str, Any]:
    """Get children of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/children")

@mcp.tool()
def get_page_ancestors(page_id: str) -> Dict[str, Any]:
    """Get ancestors of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/ancestors")

@mcp.tool()
def move_page(page_id: str, parent_id: str, title: str, version_number: int, space_id: str) -> Dict[str, Any]:
    """Move a page to a new parent."""
    payload = {
        "id": page_id,
        "status": "current",
        "title": title,
        "spaceId": space_id,
        "parentId": parent_id,
        "version": {
            "number": version_number
        }
    }
    return client.request("PUT", f"/api/v2/pages/{page_id}", json_data=payload)

# Spaces
@mcp.tool()
def list_spaces() -> Dict[str, Any]:
    """List spaces."""
    return client.request("GET", "/api/v2/spaces")

@mcp.tool()
def get_space(space_id: str) -> Dict[str, Any]:
    """Get a space by ID."""
    return client.request("GET", f"/api/v2/spaces/{space_id}")

@mcp.tool()
def create_space(key: str, name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a new space."""
    payload = {
        "key": key,
        "name": name
    }
    if description:
        payload["description"] = {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        }
    return client.request("POST", "/rest/api/space", json_data=payload)

@mcp.tool()
def delete_space(space_key: str) -> Dict[str, Any]:
    """Delete a space."""
    return client.request("DELETE", f"/rest/api/space/{space_key}")

# Search
@mcp.tool()
def search_content(cql: str, limit: int = 25) -> Dict[str, Any]:
    """Search content using CQL."""
    return client.request("GET", "/rest/api/search", params={"cql": cql, "limit": limit})

# Labels
@mcp.tool()
def add_labels(content_id: str, labels: List[str]) -> Dict[str, Any]:
    """Add labels to content."""
    payload = [{"prefix": "global", "name": label} for label in labels]
    return client.request("POST", f"/rest/api/content/{content_id}/label", json_data=payload)

@mcp.tool()
def list_labels(page_id: str) -> Dict[str, Any]:
    """List labels on a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/labels")

@mcp.tool()
def remove_label(content_id: str, label_name: str) -> Dict[str, Any]:
    """Remove a label from content."""
    return client.request("DELETE", f"/rest/api/content/{content_id}/label/{label_name}")

# Attachments
@mcp.tool()
def list_attachments(page_id: str) -> Dict[str, Any]:
    """List attachments on a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/attachments")

@mcp.tool()
def upload_attachment(content_id: str, filename: str, file_content: str, comment: Optional[str] = None) -> Dict[str, Any]:
    """Upload an attachment to content."""
    headers = {"X-Atlassian-Token": "nocheck"}
    files = {"file": (filename, file_content)}
    data = {"comment": comment} if comment else None
    return client.request("POST", f"/rest/api/content/{content_id}/child/attachment", headers=headers, files=files, data=data)

@mcp.tool()
def download_attachment(content_id: str, attachment_id: str) -> Dict[str, Any]:
    """Download an attachment."""
    return client.request("GET", f"/rest/api/content/{content_id}/child/attachment/{attachment_id}/download")

# Comments
@mcp.tool()
def create_footer_comment(page_id: str, content: str) -> Dict[str, Any]:
    """Create a footer comment on a page."""
    payload = {
        "pageId": page_id,
        "body": {
            "representation": "storage",
            "value": content
        }
    }
    return client.request("POST", "/api/v2/footer-comments", json_data=payload)

@mcp.tool()
def list_footer_comments(page_id: str) -> Dict[str, Any]:
    """List footer comments on a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/footer-comments")

@mcp.tool()
def create_inline_comment(page_id: str, content: str, inline_marker_ref: str) -> Dict[str, Any]:
    """Create an inline comment on a page."""
    payload = {
        "pageId": page_id,
        "body": {
            "representation": "storage",
            "value": content
        },
        "inlineMarkerRef": inline_marker_ref
    }
    return client.request("POST", "/api/v2/inline-comments", json_data=payload)

@mcp.tool()
def list_inline_comments(page_id: str) -> Dict[str, Any]:
    """List inline comments on a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/inline-comments")

# Versions
@mcp.tool()
def list_page_versions(page_id: str) -> Dict[str, Any]:
    """List versions of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/versions")

@mcp.tool()
def get_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    """Get a specific version of a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")

@mcp.tool()
def restore_page_version(content_id: str, version_number: int, message: str = "") -> Dict[str, Any]:
    """Restore a page to a previous version."""
    payload = {
        "version": {
            "number": version_number,
            "message": message
        }
    }
    return client.request("POST", f"/rest/api/content/{content_id}/version", json_data=payload)

# Content Properties
@mcp.tool()
def get_content_properties(page_id: str) -> Dict[str, Any]:
    """Get content properties for a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/properties")

@mcp.tool()
def set_content_property(page_id: str, key: str, value: Any) -> Dict[str, Any]:
    """Set a content property on a page."""
    payload = {
        "key": key,
        "value": value
    }
    return client.request("POST", f"/api/v2/pages/{page_id}/properties", json_data=payload)

# Blog Posts
@mcp.tool()
def create_blog_post(title: str, content: str, space_id: str) -> Dict[str, Any]:
    """Create a new blog post."""
    payload = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": content
        }
    }
    return client.request("POST", "/api/v2/blogposts", json_data=payload)

@mcp.tool()
def get_blog_post(blog_post_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """Get a blog post by ID."""
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}", params={"body-format": body_format})

@mcp.tool()
def update_blog_post(blog_post_id: str, title: str, content: str, version_number: int, space_id: str) -> Dict[str, Any]:
    """Update an existing blog post."""
    payload = {
        "id": blog_post_id,
        "status": "current",
        "title": title,
        "spaceId": space_id,
        "body": {
            "representation": "storage",
            "value": content
        },
        "version": {
            "number": version_number
        }
    }
    return client.request("PUT", f"/api/v2/blogposts/{blog_post_id}", json_data=payload)

@mcp.tool()
def delete_blog_post(blog_post_id: str) -> Dict[str, Any]:
    """Delete a blog post."""
    return client.request("DELETE", f"/api/v2/blogposts/{blog_post_id}")

# Users
@mcp.tool()
def get_current_user() -> Dict[str, Any]:
    """Get the current user."""
    return client.request("GET", "/rest/api/user/current")

@mcp.tool()
def get_user_by_account_id(account_id: str) -> Dict[str, Any]:
    """Get a user by account ID."""
    return client.request("GET", "/rest/api/user", params={"accountId": account_id})

if __name__ == "__main__":
    mcp.run()
