import os
from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_attachment_settings() -> Any:
    """GET /rest/api/3/attachment/meta"""
    client = JiraClient()
    return client.request("GET", "/attachment/meta")


def get_attachment_metadata(attachmentId: str) -> Any:
    """GET /rest/api/3/attachment/{id}"""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachmentId}")


def delete_attachment(attachmentId: str) -> Any:
    """DEL /rest/api/3/attachment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/attachment/{attachmentId}")


def add_attachment(issueIdOrKey: str, file_path: str, *, filename: Optional[str] = None) -> Any:
    """POST /rest/api/3/issue/{issueIdOrKey}/attachments

    Uploads a single file from local path.
    """
    if not os.path.exists(file_path):
        return {"error": f"file not found: {file_path}"}

    client = JiraClient()
    headers = {"X-Atlassian-Token": "no-check"}
    name = filename or os.path.basename(file_path)
    with open(file_path, "rb") as f:
        files = {"file": (name, f)}
        return client.request(
            "POST",
            f"/issue/{issueIdOrKey}/attachments",
            headers=headers,
            files=files,
        )
