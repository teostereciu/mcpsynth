from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_attachment_settings() -> Any:
    """GET /attachment/meta"""
    return JiraClient().request("GET", "/attachment/meta")


def get_attachment_metadata(attachment_id: str) -> Any:
    """GET /attachment/{id}"""
    return JiraClient().request("GET", f"/attachment/{attachment_id}")


def delete_attachment(attachment_id: str) -> Any:
    """DELETE /attachment/{id}"""
    return JiraClient().request("DELETE", f"/attachment/{attachment_id}")


def get_attachment_content(attachment_id: str, redirect: Optional[bool] = None) -> Any:
    """GET /attachment/content/{id}

    Note: this tool returns raw text if not JSON.
    """
    params: Dict[str, Any] = {}
    if redirect is not None:
        params["redirect"] = str(redirect).lower()
    return JiraClient().request("GET", f"/attachment/content/{attachment_id}", params=params or None)


def get_attachment_thumbnail(attachment_id: str, redirect: Optional[bool] = None,
                             fallback_to_default: Optional[bool] = None,
                             width: Optional[int] = None, height: Optional[int] = None) -> Any:
    """GET /attachment/thumbnail/{id}"""
    params: Dict[str, Any] = {}
    if redirect is not None:
        params["redirect"] = str(redirect).lower()
    if fallback_to_default is not None:
        params["fallbackToDefault"] = str(fallback_to_default).lower()
    if width is not None:
        params["width"] = width
    if height is not None:
        params["height"] = height
    return JiraClient().request("GET", f"/attachment/thumbnail/{attachment_id}", params=params or None)


def add_attachment(issue_id_or_key: str, file_path: str) -> Any:
    """POST /issue/{issueIdOrKey}/attachments

    Uploads a single file from local path.
    """
    client = JiraClient()
    try:
        with open(file_path, "rb") as f:
            files = {"file": (file_path.split("/")[-1], f)}
            return client.request(
                "POST",
                f"/issue/{issue_id_or_key}/attachments",
                files=files,
                headers={"X-Atlassian-Token": "no-check"},
            )
    except OSError as e:
        return {"error": str(e)}


def get_attachment_expand_human(attachment_id: str) -> Any:
    """GET /attachment/{id}/expand/human"""
    return JiraClient().request("GET", f"/attachment/{attachment_id}/expand/human")


def get_attachment_expand_raw(attachment_id: str) -> Any:
    """GET /attachment/{id}/expand/raw"""
    return JiraClient().request("GET", f"/attachment/{attachment_id}/expand/raw")
