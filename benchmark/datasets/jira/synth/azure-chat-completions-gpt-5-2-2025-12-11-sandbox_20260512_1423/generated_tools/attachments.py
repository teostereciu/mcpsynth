import os
from typing import Any, Dict, Optional

from ._client import get_client


def get_attachment_meta() -> Any:
    """GET /attachment/meta"""
    return get_client().request("GET", "/attachment/meta")


def get_attachment(attachment_id: str) -> Any:
    """GET /attachment/{id}"""
    return get_client().request("GET", f"/attachment/{attachment_id}")


def delete_attachment(attachment_id: str) -> Any:
    """DELETE /attachment/{id}"""
    return get_client().request("DELETE", f"/attachment/{attachment_id}")


def add_attachment(issue_id_or_key: str, file_path: str) -> Any:
    """POST /issue/{issueIdOrKey}/attachments

    Uploads a single file from local disk.
    """
    if not os.path.exists(file_path):
        return {"error": "File not found", "file_path": file_path}

    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        return get_client().request(
            "POST",
            f"/issue/{issue_id_or_key}/attachments",
            files=files,
            headers={"X-Atlassian-Token": "no-check"},
        )


def get_attachment_archive_metadata_human(attachment_id: str) -> Any:
    """GET /attachment/{id}/expand/human"""
    return get_client().request("GET", f"/attachment/{attachment_id}/expand/human")


def get_attachment_archive_metadata_raw(attachment_id: str) -> Any:
    """GET /attachment/{id}/expand/raw"""
    return get_client().request("GET", f"/attachment/{attachment_id}/expand/raw")
