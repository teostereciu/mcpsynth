import os
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

from confluence_client import ConfluenceClient
import generated_tools.spaces as spaces_tool
import generated_tools.pages as pages_tool
import generated_tools.search as search_tool
import generated_tools.labels as labels_tool
import generated_tools.attachments as attachments_tool
import generated_tools.comments as comments_tool
import generated_tools.versions as versions_tool
import generated_tools.properties as properties_tool
import generated_tools.blogposts as blogposts_tool
import generated_tools.users as users_tool

# Initialize FastMCP server
mcp = FastMCP("Confluence Cloud")

# Initialize Confluence Client lazily or at startup
_client = None

def get_client() -> ConfluenceClient:
    global _client
    if _client is None:
        _client = ConfluenceClient()
    return _client

# --- Spaces ---

@mcp.tool()
def list_spaces(limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
    """
    List all spaces in Confluence.
    
    Args:
        limit: Maximum number of spaces to return (default 20).
        cursor: Cursor for pagination.
    """
    return spaces_tool.list_spaces(get_client(), limit=limit, cursor=cursor)

@mcp.tool()
def get_space(space_id_or_key: str) -> Dict[str, Any]:
    """
    Get details of a specific space by its ID or key.
    
    Args:
        space_id_or_key: The numeric ID of the space or its key (e.g., 'SYNTH').
    """
    return spaces_tool.get_space(get_client(), space_id_or_key=space_id_or_key)

@mcp.tool()
def create_space(key: str, name: str, description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new space.
    
    Args:
        key: Unique key for the space (e.g., 'SYNTH').
        name: Name of the space.
        description: Optional description of the space.
    """
    return spaces_tool.create_space(get_client(), key=key, name=name, description=description)

@mcp.tool()
def delete_space(space_id: str) -> Dict[str, Any]:
    """
    Delete a space by its numeric ID.
    
    Args:
        space_id: The numeric ID of the space to delete.
    """
    return spaces_tool.delete_space(get_client(), space_id=space_id)

# --- Pages ---

@mcp.tool()
def create_page(
    title: str,
    space_key: Optional[str] = None,
    parent_id: Optional[str] = None,
    body: str = "",
    representation: str = "storage"
) -> Dict[str, Any]:
    """
    Create a new page in Confluence.
    
    Args:
        title: Title of the page.
        space_key: Key of the space (defaults to CONFLUENCE_SPACE_KEY env var).
        parent_id: Optional ID of the parent page.
        body: HTML/Storage or ADF content of the page.
        representation: Format of the body ('storage' for HTML, 'atlas_doc_format' for ADF).
    """
    return pages_tool.create_page(
        get_client(),
        title=title,
        space_key=space_key,
        parent_id=parent_id,
        body=body,
        representation=representation
    )

@mcp.tool()
def get_page(page_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """
    Get details of a specific page.
    
    Args:
        page_id: Numeric ID of the page.
        body_format: Format of the body to return ('storage', 'atlas_doc_format', 'view', etc.).
    """
    return pages_tool.get_page(get_client(), page_id=page_id, body_format=body_format)

@mcp.tool()
def update_page(
    page_id: str,
    title: str,
    body: str,
    representation: str = "storage",
    version_number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Update an existing page.
    
    Args:
        page_id: Numeric ID of the page.
        title: New title of the page.
        body: New content of the page.
        representation: Format of the body ('storage' or 'atlas_doc_format').
        version_number: Optional version number. If not provided, the current version is fetched and incremented.
    """
    return pages_tool.update_page(
        get_client(),
        page_id=page_id,
        title=title,
        body=body,
        representation=representation,
        version_number=version_number
    )

@mcp.tool()
def delete_page(page_id: str) -> Dict[str, Any]:
    """
    Delete a page.
    
    Args:
        page_id: Numeric ID of the page to delete.
    """
    return pages_tool.delete_page(get_client(), page_id=page_id)

@mcp.tool()
def get_page_children(page_id: str, limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
    """
    Get child pages of a page.
    
    Args:
        page_id: Numeric ID of the parent page.
        limit: Maximum number of children to return.
        cursor: Cursor for pagination.
    """
    return pages_tool.get_page_children(get_client(), page_id=page_id, limit=limit, cursor=cursor)

@mcp.tool()
def get_page_ancestors(page_id: str) -> Dict[str, Any]:
    """
    Get ancestors of a page (ordered from root down to parent).
    
    Args:
        page_id: Numeric ID of the page.
    """
    return pages_tool.get_page_ancestors(get_client(), page_id=page_id)

@mcp.tool()
def move_page(page_id: str, parent_id: str) -> Dict[str, Any]:
    """
    Move a page to be a child of another page.
    
    Args:
        page_id: Numeric ID of the page to move.
        parent_id: Numeric ID of the new parent page.
    """
    return pages_tool.move_page(get_client(), page_id=page_id, parent_id=parent_id)

# --- Search ---

@mcp.tool()
def search_content(cql: str, limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
    """
    Search for content using Confluence Query Language (CQL).
    
    Args:
        cql: The CQL query string (e.g., 'type = page and text ~ "mcp"').
        limit: Maximum number of results to return.
        cursor: Cursor for pagination.
    """
    return search_tool.search_content(get_client(), cql=cql, limit=limit, cursor=cursor)

# --- Labels ---

@mcp.tool()
def get_labels(content_id: str, content_type: str = "page") -> Dict[str, Any]:
    """
    Get labels for a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        content_type: Type of content ('page' or 'blogpost').
    """
    return labels_tool.get_labels(get_client(), content_id=content_id, content_type=content_type)

@mcp.tool()
def add_labels(content_id: str, labels: List[str], content_type: str = "page") -> Dict[str, Any]:
    """
    Add labels to a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        labels: List of label names to add.
        content_type: Type of content ('page' or 'blogpost').
    """
    return labels_tool.add_labels(get_client(), content_id=content_id, labels=labels, content_type=content_type)

@mcp.tool()
def remove_label(content_id: str, label_name: str, content_type: str = "page") -> Dict[str, Any]:
    """
    Remove a label from a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        label_name: Name of the label to remove.
        content_type: Type of content ('page' or 'blogpost').
    """
    return labels_tool.remove_label(get_client(), content_id=content_id, label_name=label_name, content_type=content_type)

# --- Attachments ---

@mcp.tool()
def list_attachments(
    content_id: str,
    content_type: str = "page",
    limit: int = 20,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List attachments for a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        content_type: Type of content ('page' or 'blogpost').
        limit: Maximum number of attachments to return.
        cursor: Cursor for pagination.
    """
    return attachments_tool.list_attachments(
        get_client(),
        content_id=content_id,
        content_type=content_type,
        limit=limit,
        cursor=cursor
    )

@mcp.tool()
def upload_attachment(
    content_id: str,
    filename: str,
    file_content_base64: str,
    comment: Optional[str] = None,
    content_type: str = "page"
) -> Dict[str, Any]:
    """
    Upload an attachment to a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        filename: Name of the file to upload.
        file_content_base64: Base64 encoded content of the file.
        comment: Optional comment about the attachment.
        content_type: Type of content ('page' or 'blogpost').
    """
    return attachments_tool.upload_attachment(
        get_client(),
        content_id=content_id,
        filename=filename,
        file_content_base64=file_content_base64,
        comment=comment,
        content_type=content_type
    )

@mcp.tool()
def download_attachment(attachment_id: str) -> Dict[str, Any]:
    """
    Download an attachment by its ID.
    Returns the attachment metadata and base64-encoded content.
    
    Args:
        attachment_id: Numeric ID of the attachment.
    """
    return attachments_tool.download_attachment(get_client(), attachment_id=attachment_id)

# --- Comments ---

@mcp.tool()
def list_comments(
    page_id: str,
    comment_type: str = "footer",
    limit: int = 20,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List comments on a page.
    
    Args:
        page_id: Numeric ID of the page.
        comment_type: Type of comments to list ('footer' or 'inline').
        limit: Maximum number of comments to return.
        cursor: Cursor for pagination.
    """
    return comments_tool.list_comments(
        get_client(),
        page_id=page_id,
        comment_type=comment_type,
        limit=limit,
        cursor=cursor
    )

@mcp.tool()
def create_footer_comment(
    page_id: str,
    body: str,
    parent_comment_id: Optional[str] = None,
    representation: str = "storage"
) -> Dict[str, Any]:
    """
    Create a footer comment on a page.
    
    Args:
        page_id: Numeric ID of the page.
        body: Content of the comment (HTML/Storage or ADF).
        parent_comment_id: Optional ID of the parent comment (for replies).
        representation: Format of the body ('storage' or 'atlas_doc_format').
    """
    return comments_tool.create_footer_comment(
        get_client(),
        page_id=page_id,
        body=body,
        parent_comment_id=parent_comment_id,
        representation=representation
    )

# --- Versions ---

@mcp.tool()
def list_versions(page_id: str, limit: int = 20, cursor: Optional[str] = None) -> Dict[str, Any]:
    """
    List all versions of a page.
    
    Args:
        page_id: Numeric ID of the page.
        limit: Maximum number of versions to return.
        cursor: Cursor for pagination.
    """
    return versions_tool.list_versions(get_client(), page_id=page_id, limit=limit, cursor=cursor)

@mcp.tool()
def get_version(page_id: str, version_number: int) -> Dict[str, Any]:
    """
    Get details of a specific page version.
    
    Args:
        page_id: Numeric ID of the page.
        version_number: Version number to retrieve.
    """
    return versions_tool.get_version(get_client(), page_id=page_id, version_number=version_number)

@mcp.tool()
def restore_version(page_id: str, version_number: int, message: Optional[str] = None) -> Dict[str, Any]:
    """
    Restore a page to a specific version.
    
    Args:
        page_id: Numeric ID of the page.
        version_number: Version number to restore to.
        message: Optional description/message for the restore operation.
    """
    return versions_tool.restore_version(
        get_client(),
        page_id=page_id,
        version_number=version_number,
        message=message
    )

# --- Content Properties ---

@mcp.tool()
def get_content_property(page_id: str, key: str) -> Dict[str, Any]:
    """
    Get a content property value for a page.
    
    Args:
        page_id: Numeric ID of the page.
        key: Key of the property.
    """
    return properties_tool.get_content_property(get_client(), page_id=page_id, key=key)

@mcp.tool()
def set_content_property(page_id: str, key: str, value: Any) -> Dict[str, Any]:
    """
    Set a content property value for a page.
    If the property already exists, it will be updated.
    
    Args:
        page_id: Numeric ID of the page.
        key: Key of the property.
        value: JSON-serializable value of the property.
    """
    return properties_tool.set_content_property(get_client(), page_id=page_id, key=key, value=value)

# --- Blog Posts ---

@mcp.tool()
def create_blogpost(
    title: str,
    space_key: Optional[str] = None,
    body: str = "",
    representation: str = "storage"
) -> Dict[str, Any]:
    """
    Create a new blog post.
    
    Args:
        title: Title of the blog post.
        space_key: Key of the space (defaults to CONFLUENCE_SPACE_KEY env var).
        body: Content of the blog post.
        representation: Format of the body ('storage' or 'atlas_doc_format').
    """
    return blogposts_tool.create_blogpost(
        get_client(),
        title=title,
        space_key=space_key,
        body=body,
        representation=representation
    )

@mcp.tool()
def get_blogpost(blogpost_id: str, body_format: str = "storage") -> Dict[str, Any]:
    """
    Get details of a specific blog post.
    
    Args:
        blogpost_id: Numeric ID of the blog post.
        body_format: Format of the body to return ('storage', 'atlas_doc_format', 'view', etc.).
    """
    return blogposts_tool.get_blogpost(get_client(), blogpost_id=blogpost_id, body_format=body_format)

@mcp.tool()
def update_blogpost(
    blogpost_id: str,
    title: str,
    body: str,
    representation: str = "storage",
    version_number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Update an existing blog post.
    
    Args:
        blogpost_id: Numeric ID of the blog post.
        title: New title of the blog post.
        body: New content of the blog post.
        representation: Format of the body ('storage' or 'atlas_doc_format').
        version_number: Optional version number. If not provided, the current version is fetched and incremented.
    """
    return blogposts_tool.update_blogpost(
        get_client(),
        blogpost_id=blogpost_id,
        title=title,
        body=body,
        representation=representation,
        version_number=version_number
    )

@mcp.tool()
def delete_blogpost(blogpost_id: str) -> Dict[str, Any]:
    """
    Delete a blog post.
    
    Args:
        blogpost_id: Numeric ID of the blog post to delete.
    """
    return blogposts_tool.delete_blogpost(get_client(), blogpost_id=blogpost_id)

# --- Users ---

@mcp.tool()
def get_current_user() -> Dict[str, Any]:
    """
    Get details of the currently authenticated user.
    """
    return users_tool.get_current_user(get_client())

@mcp.tool()
def get_user(account_id: str) -> Dict[str, Any]:
    """
    Get details of a user by their account ID.
    
    Args:
        account_id: The unique Atlassian account ID of the user.
    """
    return users_tool.get_user(get_client(), account_id=account_id)

if __name__ == "__main__":
    mcp.run()
