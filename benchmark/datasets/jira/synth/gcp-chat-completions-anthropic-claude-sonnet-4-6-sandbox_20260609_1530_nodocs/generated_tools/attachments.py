"""
MCP tools for Jira Issue Attachments.
"""

import os
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_delete, jira_multipart_post

mcp = FastMCP("jira-attachments")


@mcp.tool()
def get_attachment_metadata(attachment_id: str) -> Dict[str, Any]:
    """
    Get metadata for a specific attachment.

    Args:
        attachment_id: The attachment ID.
    """
    return jira_get(f"/attachment/{attachment_id}")


@mcp.tool()
def delete_attachment(attachment_id: str) -> Dict[str, Any]:
    """
    Delete an attachment from a Jira issue.

    Args:
        attachment_id: The attachment ID.
    """
    return jira_delete(f"/attachment/{attachment_id}")


@mcp.tool()
def get_attachment_settings() -> Dict[str, Any]:
    """
    Get global attachment settings (max size, whether attachments are enabled).
    """
    return jira_get("/attachment/meta")


@mcp.tool()
def upload_attachment(issue_id_or_key: str, file_path: str) -> Dict[str, Any]:
    """
    Upload a file as an attachment to a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        file_path: Absolute or relative path to the file to upload.
    """
    if not os.path.isfile(file_path):
        return {"error": f"File not found: {file_path}"}
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, "rb") as f:
            files = [("file", (file_name, f, "application/octet-stream"))]
            return jira_multipart_post(f"/issue/{issue_id_or_key}/attachments", files=files)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_issue_attachments(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get all attachments for a Jira issue (via issue fields).

    Args:
        issue_id_or_key: The issue ID or key.
    """
    result = jira_get(f"/issue/{issue_id_or_key}", params={"fields": "attachment"})
    if "error" in result:
        return result
    return result.get("fields", {}).get("attachment", [])


@mcp.tool()
def get_attachment_thumbnail(attachment_id: str) -> Dict[str, Any]:
    """
    Get metadata about an attachment's thumbnail (if available).

    Args:
        attachment_id: The attachment ID.
    """
    return jira_get(f"/attachment/{attachment_id}/expand/human")
