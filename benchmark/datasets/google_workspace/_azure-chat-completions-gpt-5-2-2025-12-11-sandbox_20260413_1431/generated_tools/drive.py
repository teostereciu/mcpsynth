"""Google Drive API v3 tools (metadata operations)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

DRIVE_BASE = "https://www.googleapis.com/drive/v3"


def drive_files_create(*, file: Dict[str, Any], fields: Optional[str] = None, supports_all_drives: bool = True) -> Any:
    params: Dict[str, Any] = {"supportsAllDrives": supports_all_drives}
    if fields:
        params["fields"] = fields
    return request_json("POST", f"{DRIVE_BASE}/files", params=params, json=file)


def drive_files_list(
    *,
    q: Optional[str] = None,
    page_size: int = 100,
    page_token: Optional[str] = None,
    fields: Optional[str] = None,
    supports_all_drives: bool = True,
    include_items_from_all_drives: bool = True,
    corpora: Optional[str] = None,
    drive_id: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {
        "pageSize": page_size,
        "supportsAllDrives": supports_all_drives,
        "includeItemsFromAllDrives": include_items_from_all_drives,
    }
    if q:
        params["q"] = q
    if page_token:
        params["pageToken"] = page_token
    if fields:
        params["fields"] = fields
    if corpora:
        params["corpora"] = corpora
    if drive_id:
        params["driveId"] = drive_id
    return request_json("GET", f"{DRIVE_BASE}/files", params=params)


def drive_files_get(file_id: str, *, fields: Optional[str] = None, supports_all_drives: bool = True) -> Any:
    params: Dict[str, Any] = {"supportsAllDrives": supports_all_drives}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"{DRIVE_BASE}/files/{file_id}", params=params)


def drive_permissions_create(
    file_id: str,
    *,
    permission: Dict[str, Any],
    fields: Optional[str] = None,
    send_notification_email: bool = False,
    supports_all_drives: bool = True,
) -> Any:
    params: Dict[str, Any] = {
        "supportsAllDrives": supports_all_drives,
        "sendNotificationEmail": send_notification_email,
    }
    if fields:
        params["fields"] = fields
    return request_json("POST", f"{DRIVE_BASE}/files/{file_id}/permissions", params=params, json=permission)


def drive_permissions_list(file_id: str, *, fields: Optional[str] = None, supports_all_drives: bool = True) -> Any:
    params: Dict[str, Any] = {"supportsAllDrives": supports_all_drives}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"{DRIVE_BASE}/files/{file_id}/permissions", params=params)


def drive_permissions_delete(file_id: str, permission_id: str, *, supports_all_drives: bool = True) -> Any:
    params: Dict[str, Any] = {"supportsAllDrives": supports_all_drives}
    return request_json("DELETE", f"{DRIVE_BASE}/files/{file_id}/permissions/{permission_id}", params=params)
