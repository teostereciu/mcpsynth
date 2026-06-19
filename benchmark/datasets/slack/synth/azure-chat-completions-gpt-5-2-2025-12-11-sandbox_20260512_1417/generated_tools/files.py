from typing import Any, Dict, List, Optional

import requests

from .slack_client import get_client


def files_list(
    channel: Optional[str] = None,
    user: Optional[str] = None,
    types: Optional[str] = None,
    ts_from: Optional[str] = None,
    ts_to: Optional[str] = None,
    count: Optional[int] = None,
    page: Optional[int] = None,
    show_files_hidden_by_limit: Optional[bool] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if channel is not None:
        payload["channel"] = channel
    if user is not None:
        payload["user"] = user
    if types is not None:
        payload["types"] = types
    if ts_from is not None:
        payload["ts_from"] = ts_from
    if ts_to is not None:
        payload["ts_to"] = ts_to
    if count is not None:
        payload["count"] = count
    if page is not None:
        payload["page"] = page
    if show_files_hidden_by_limit is not None:
        payload["show_files_hidden_by_limit"] = show_files_hidden_by_limit
    if team_id is not None:
        payload["team_id"] = team_id
    return get_client().request("GET", "/files.list", json=payload)


def files_get_upload_url_external(
    filename: str,
    length: int,
    snippet_type: Optional[str] = None,
    alt_txt: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"filename": filename, "length": length}
    if snippet_type is not None:
        payload["snippet_type"] = snippet_type
    if alt_txt is not None:
        payload["alt_txt"] = alt_txt
    return get_client().request("POST", "/files.getUploadURLExternal", json=payload)


def files_complete_upload_external(
    files: List[Dict[str, Any]],
    channel_id: Optional[str] = None,
    channels: Optional[str] = None,
    thread_ts: Optional[str] = None,
    initial_comment: Optional[str] = None,
    blocks: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"files": files}
    if channel_id is not None:
        payload["channel_id"] = channel_id
    if channels is not None:
        payload["channels"] = channels
    if thread_ts is not None:
        payload["thread_ts"] = thread_ts
    if initial_comment is not None:
        payload["initial_comment"] = initial_comment
    if blocks is not None:
        payload["blocks"] = blocks
    return get_client().request("POST", "/files.completeUploadExternal", json=payload)


def files_upload_via_external_url(upload_url: str, file_bytes: bytes, filename: Optional[str] = None) -> Dict[str, Any]:
    """Uploads raw bytes to the upload_url returned by files.getUploadURLExternal.

    This is not a Slack Web API method; it is a helper and is NOT registered as an MCP tool.
    """
    try:
        # Slack accepts raw bytes or multipart. We'll send raw bytes.
        headers = {}
        if filename:
            headers["Content-Disposition"] = f'attachment; filename="{filename}"'
        resp = requests.post(upload_url, data=file_bytes, headers=headers, timeout=60)
        if resp.status_code != 200:
            return {"ok": False, "error": "upload_failed", "http_status": resp.status_code, "text": resp.text}
        return {"ok": True, "http_status": resp.status_code}
    except requests.RequestException as e:
        return {"ok": False, "error": str(e)}
