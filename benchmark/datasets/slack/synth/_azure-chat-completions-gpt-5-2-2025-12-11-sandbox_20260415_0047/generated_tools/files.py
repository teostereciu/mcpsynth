from __future__ import annotations

import base64
from typing import Any, Dict, List, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call, slack_upload_to_external_url


@mcp.tool(name="files_get_upload_url_external")
def files_get_upload_url_external(
    filename: str,
    length: int,
    snippet_type: Optional[str] = None,
    alt_txt: Optional[str] = None,
) -> Dict[str, Any]:
    """Gets a URL for an edge external file upload (files.getUploadURLExternal)."""

    payload: Dict[str, Any] = {"filename": filename, "length": length}
    if snippet_type is not None:
        payload["snippet_type"] = snippet_type
    if alt_txt is not None:
        payload["alt_txt"] = alt_txt

    try:
        return slack_api_call("files.getUploadURLExternal", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="files_complete_upload_external")
def files_complete_upload_external(
    files: List[Dict[str, Any]],
    channel_id: Optional[str] = None,
    channels: Optional[List[str]] = None,
    initial_comment: Optional[str] = None,
    thread_ts: Optional[str] = None,
) -> Dict[str, Any]:
    """Finishes an upload started with files.getUploadURLExternal (files.completeUploadExternal)."""

    payload: Dict[str, Any] = {"files": files}
    if channel_id is not None:
        payload["channel_id"] = channel_id
    if channels is not None:
        payload["channels"] = ",".join(channels)
    if initial_comment is not None:
        payload["initial_comment"] = initial_comment
    if thread_ts is not None:
        payload["thread_ts"] = thread_ts

    try:
        return slack_api_call("files.completeUploadExternal", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="files_upload_text_to_channel")
def files_upload_text_to_channel(
    channel: str,
    filename: str,
    content: str,
    initial_comment: Optional[str] = None,
    thread_ts: Optional[str] = None,
) -> Dict[str, Any]:
    """Convenience tool: uploads a text file to a channel using the modern two-step flow.

    Implements:
      1) files.getUploadURLExternal
      2) POST bytes to upload_url
      3) files.completeUploadExternal (sharing to channel)
    """

    data = content.encode("utf-8")
    step1 = files_get_upload_url_external(filename=filename, length=len(data))
    if not step1.get("ok"):
        return step1

    upload_url = step1.get("upload_url")
    file_id = step1.get("file_id")
    if not upload_url or not file_id:
        return {"ok": False, "error": "invalid_response", "detail": "Missing upload_url or file_id"}

    upload_res = slack_upload_to_external_url(upload_url, data)
    if not upload_res.get("ok"):
        return upload_res

    files_payload = [{"id": file_id, "title": filename}]
    return files_complete_upload_external(
        files=files_payload,
        channel_id=channel,
        initial_comment=initial_comment,
        thread_ts=thread_ts,
    )


@mcp.tool(name="files_info")
def files_info(file: str, count: Optional[int] = None, page: Optional[int] = None) -> Dict[str, Any]:
    """Gets information about a file (files.info)."""

    params: Dict[str, Any] = {"file": file}
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page

    try:
        return slack_api_call("files.info", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="files_list")
def files_list(
    channel: Optional[str] = None,
    user: Optional[str] = None,
    types: Optional[str] = None,
    ts_from: Optional[str] = None,
    ts_to: Optional[str] = None,
    count: Optional[int] = None,
    page: Optional[int] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """Lists files within the team (files.list)."""

    params: Dict[str, Any] = {}
    if channel is not None:
        params["channel"] = channel
    if user is not None:
        params["user"] = user
    if types is not None:
        params["types"] = types
    if ts_from is not None:
        params["ts_from"] = ts_from
    if ts_to is not None:
        params["ts_to"] = ts_to
    if count is not None:
        params["count"] = count
    if page is not None:
        params["page"] = page
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    try:
        return slack_api_call("files.list", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="files_delete")
def files_delete(file: str) -> Dict[str, Any]:
    """Deletes a file (files.delete)."""

    try:
        return slack_api_call("files.delete", http_method="POST", json={"file": file})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="files_shared_public_url")
def files_shared_public_url(file: str) -> Dict[str, Any]:
    """Enables a public URL for a file (files.sharedPublicURL)."""

    try:
        return slack_api_call("files.sharedPublicURL", http_method="POST", json={"file": file})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="files_revoke_public_url")
def files_revoke_public_url(file: str) -> Dict[str, Any]:
    """Revokes public URL for a file (files.revokePublicURL)."""

    try:
        return slack_api_call("files.revokePublicURL", http_method="POST", json={"file": file})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
