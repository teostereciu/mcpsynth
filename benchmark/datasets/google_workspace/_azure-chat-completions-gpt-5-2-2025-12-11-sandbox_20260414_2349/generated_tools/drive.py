from typing import Any, Dict, Optional

from .http import request_json

DRIVE_BASE = "https://www.googleapis.com/drive/v3"


def drive_files_create(*, body: Dict[str, Any], fields: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", f"{DRIVE_BASE}/files", params=params, json_body=body)


def drive_files_get(fileId: str, *, fields: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("GET", f"{DRIVE_BASE}/files/{fileId}", params=params)


def drive_files_list(
    *,
    q: Optional[str] = None,
    pageSize: int = 100,
    pageToken: Optional[str] = None,
    fields: Optional[str] = None,
    orderBy: Optional[str] = None,
    spaces: Optional[str] = None,
    supportsAllDrives: Optional[bool] = None,
    includeItemsFromAllDrives: Optional[bool] = None,
    corpora: Optional[str] = None,
    driveId: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"pageSize": pageSize}
    if q is not None:
        params["q"] = q
    if pageToken is not None:
        params["pageToken"] = pageToken
    if fields is not None:
        params["fields"] = fields
    if orderBy is not None:
        params["orderBy"] = orderBy
    if spaces is not None:
        params["spaces"] = spaces
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    if includeItemsFromAllDrives is not None:
        params["includeItemsFromAllDrives"] = includeItemsFromAllDrives
    if corpora is not None:
        params["corpora"] = corpora
    if driveId is not None:
        params["driveId"] = driveId
    return request_json("GET", f"{DRIVE_BASE}/files", params=params)


def drive_files_update(fileId: str, *, body: Dict[str, Any], fields: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("PATCH", f"{DRIVE_BASE}/files/{fileId}", params=params, json_body=body)


def drive_files_delete(fileId: str, *, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("DELETE", f"{DRIVE_BASE}/files/{fileId}", params=params)


def drive_files_copy(fileId: str, *, body: Optional[Dict[str, Any]] = None, fields: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", f"{DRIVE_BASE}/files/{fileId}/copy", params=params, json_body=body or {})


def drive_files_export(fileId: str, mimeType: str) -> Any:
    return request_json("GET", f"{DRIVE_BASE}/files/{fileId}/export", params={"mimeType": mimeType})


def drive_permissions_create(fileId: str, *, body: Dict[str, Any], fields: Optional[str] = None, sendNotificationEmail: Optional[bool] = None, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if sendNotificationEmail is not None:
        params["sendNotificationEmail"] = sendNotificationEmail
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", f"{DRIVE_BASE}/files/{fileId}/permissions", params=params, json_body=body)


def drive_permissions_list(fileId: str, *, fields: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("GET", f"{DRIVE_BASE}/files/{fileId}/permissions", params=params)


def drive_permissions_delete(fileId: str, permissionId: str, *, supportsAllDrives: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("DELETE", f"{DRIVE_BASE}/files/{fileId}/permissions/{permissionId}", params=params)


def drive_drives_list(*, pageSize: int = 100, pageToken: Optional[str] = None, q: Optional[str] = None, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if q is not None:
        params["q"] = q
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"{DRIVE_BASE}/drives", params=params)


def drive_drives_get(driveId: str, *, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"{DRIVE_BASE}/drives/{driveId}", params=params)


def drive_comments_list(fileId: str, *, pageSize: int = 100, pageToken: Optional[str] = None, fields: Optional[str] = None, includeDeleted: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if fields is not None:
        params["fields"] = fields
    if includeDeleted is not None:
        params["includeDeleted"] = includeDeleted
    return request_json("GET", f"{DRIVE_BASE}/files/{fileId}/comments", params=params)


def drive_replies_list(fileId: str, commentId: str, *, pageSize: int = 100, pageToken: Optional[str] = None, fields: Optional[str] = None, includeDeleted: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if fields is not None:
        params["fields"] = fields
    if includeDeleted is not None:
        params["includeDeleted"] = includeDeleted
    return request_json("GET", f"{DRIVE_BASE}/files/{fileId}/comments/{commentId}/replies", params=params)
