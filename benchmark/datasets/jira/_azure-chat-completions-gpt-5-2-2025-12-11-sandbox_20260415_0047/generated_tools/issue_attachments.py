from __future__ import annotations

import os
from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_attachment_metadata(attachment_id: str) -> Dict[str, Any]:
    """Get attachment metadata.

    GET /rest/api/3/attachment/{id}
    """

    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}")


@mcp.tool()
def jira_delete_attachment(attachment_id: str) -> Dict[str, Any]:
    """Delete an attachment.

    DEL /rest/api/3/attachment/{id}
    """

    client = JiraClient()
    return client.request("DELETE", f"/attachment/{attachment_id}")


@mcp.tool()
def jira_get_attachment_settings() -> Dict[str, Any]:
    """Get Jira attachment settings.

    GET /rest/api/3/attachment/meta
    """

    client = JiraClient()
    return client.request("GET", "/attachment/meta")


@mcp.tool()
def jira_add_attachments(issue_id_or_key: str, file_paths: list[str]) -> Dict[str, Any]:
    """Add one or more attachments to an issue.

    POST /rest/api/3/issue/{issueIdOrKey}/attachments

    Args:
        file_paths: Local file paths accessible to the server.

    Returns:
        List of attachment metadata objects.
    """

    client = JiraClient()

    files = []
    opened = []
    try:
        for p in file_paths:
            f = open(p, "rb")
            opened.append(f)
            files.append(("file", (os.path.basename(p), f)))

        return client.request(
            "POST",
            f"/issue/{issue_id_or_key}/attachments",
            headers={"X-Atlassian-Token": "no-check"},
            files=files,
        )
    finally:
        for f in opened:
            try:
                f.close()
            except Exception:
                pass
