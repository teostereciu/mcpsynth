from __future__ import annotations

from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def attachment_settings_get() -> Dict[str, Any]:
    """GET /attachment/meta - Get Jira attachment settings."""
    client = JiraClient()
    return client.request("GET", "/attachment/meta")  # type: ignore[return-value]


def attachment_get(attachment_id: str) -> Dict[str, Any]:
    """GET /attachment/{id} - Get attachment metadata."""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}")  # type: ignore[return-value]


def attachment_delete(attachment_id: str) -> Dict[str, Any]:
    """DELETE /attachment/{id} - Delete attachment."""
    client = JiraClient()
    return client.request("DELETE", f"/attachment/{attachment_id}")  # type: ignore[return-value]


def attachment_content_get(attachment_id: str, redirect: Optional[bool] = None, range_header: Optional[str] = None) -> Any:
    """GET /attachment/content/{id} - Get attachment content.

    Returns text/binary as string (requests will decode). For large/binary content, prefer redirect=True.
    """
    client = JiraClient()
    params = clean_params({"redirect": redirect})
    headers = {}
    if range_header:
        headers["Range"] = range_header
    return client.request("GET", f"/attachment/content/{attachment_id}", params=params, headers=headers, accept="*/*")


def attachment_thumbnail_get(
    attachment_id: str,
    redirect: Optional[bool] = None,
    fallback_to_default: Optional[bool] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
) -> Any:
    """GET /attachment/thumbnail/{id} - Get attachment thumbnail."""
    client = JiraClient()
    params = clean_params({"redirect": redirect, "fallbackToDefault": fallback_to_default, "width": width, "height": height})
    return client.request("GET", f"/attachment/thumbnail/{attachment_id}", params=params, accept="*/*")


def attachment_expand_human(attachment_id: str) -> Dict[str, Any]:
    """GET /attachment/{id}/expand/human - Get expanded attachment metadata (human)."""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}/expand/human")  # type: ignore[return-value]


def attachment_expand_raw(attachment_id: str) -> Dict[str, Any]:
    """GET /attachment/{id}/expand/raw - Get expanded attachment metadata (raw)."""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}/expand/raw")  # type: ignore[return-value]


def issue_attachments_add(issue_id_or_key: str, file_paths: List[str]) -> Dict[str, Any]:
    """POST /issue/{issueIdOrKey}/attachments - Add attachments.

    file_paths: local paths to upload.
    """
    client = JiraClient()
    files = []
    handles = []
    try:
        for p in file_paths:
            f = open(p, "rb")
            handles.append(f)
            files.append(("file", (p.split("/")[-1], f)))
        headers = {"X-Atlassian-Token": "no-check"}
        # requests will set multipart content-type.
        return client.request("POST", f"/issue/{issue_id_or_key}/attachments", headers=headers, files=files, accept="application/json")  # type: ignore[return-value]
    finally:
        for h in handles:
            try:
                h.close()
            except Exception:
                pass
