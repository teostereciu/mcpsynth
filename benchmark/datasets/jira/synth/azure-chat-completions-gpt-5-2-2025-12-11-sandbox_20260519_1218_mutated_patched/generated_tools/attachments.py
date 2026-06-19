from __future__ import annotations

from typing import Any, Dict, Optional

from ._client import JiraClient


def get_attachment_meta(client: JiraClient) -> Any:
    return client.request("GET", "/attachment/meta")


def get_attachment(client: JiraClient, attachment_id: str) -> Any:
    return client.request("GET", f"/attachment/{attachment_id}")


def delete_attachment(client: JiraClient, attachment_id: str) -> Any:
    return client.request("DELETE", f"/attachment/{attachment_id}")


def get_attachment_archive_metadata_human(client: JiraClient, attachment_id: str) -> Any:
    return client.request("GET", f"/attachment/{attachment_id}/expand/human")


def get_attachment_archive_metadata_raw(client: JiraClient, attachment_id: str) -> Any:
    return client.request("GET", f"/attachment/{attachment_id}/expand/raw")


def add_attachment(
    client: JiraClient,
    issue_id_or_key: str,
    file_path: str,
    *,
    filename: Optional[str] = None,
) -> Any:
    # Jira requires multipart form field name 'file' and header X-Atlassian-Token: no-check
    try:
        f = open(file_path, "rb")
    except OSError as e:
        return {"error": str(e)}

    try:
        files = {"file": (filename or file_path.split("/")[-1], f)}
        headers = {"X-Atlassian-Token": "no-check"}
        return client.request(
            "POST",
            f"/issue/{issue_id_or_key}/attachments",
            headers=headers,
            files=files,
        )
    finally:
        try:
            f.close()
        except Exception:
            pass


def get_attachment_content(
    client: JiraClient,
    attachment_id: str,
    *,
    redirect: Optional[bool] = None,
    range_header: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if redirect is not None:
        params["redirect"] = str(redirect).lower()
    headers: Dict[str, str] = {}
    if range_header is not None:
        headers["Range"] = range_header
    return client.request(
        "GET",
        f"/attachment/content/{attachment_id}",
        params=params or None,
        headers=headers or None,
    )


def get_attachment_thumbnail(
    client: JiraClient,
    attachment_id: str,
    *,
    redirect: Optional[bool] = None,
    fallback_to_default: Optional[bool] = None,
    width: Optional[int] = None,
    height: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if redirect is not None:
        params["redirect"] = str(redirect).lower()
    if fallback_to_default is not None:
        params["fallbackToDefault"] = str(fallback_to_default).lower()
    if width is not None:
        params["width"] = width
    if height is not None:
        params["height"] = height
    return client.request("GET", f"/attachment/thumbnail/{attachment_id}", params=params or None)
