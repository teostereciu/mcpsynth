from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

DRIVE_BASE = "https://www.googleapis.com/drive/v3"


def drive_files_create(
    *,
    name: str,
    mimeType: Optional[str] = None,
    parents: Optional[list[str]] = None,
    fields: str = "id,name,mimeType,modifiedTime",
    supportsAllDrives: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files"
    body: Dict[str, Any] = {"name": name}
    if mimeType is not None:
        body["mimeType"] = mimeType
    if parents is not None:
        body["parents"] = parents
    params: Dict[str, Any] = {"fields": fields}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", url, params=params, json_body=body)


def drive_files_list(
    *,
    pageSize: int = 10,
    q: Optional[str] = None,
    fields: str = "nextPageToken,files(id,name,mimeType,modifiedTime)",
    orderBy: Optional[str] = None,
    pageToken: Optional[str] = None,
    supportsAllDrives: Optional[bool] = None,
    includeItemsFromAllDrives: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files"
    params: Dict[str, Any] = {"pageSize": pageSize, "fields": fields}
    if q is not None:
        params["q"] = q
    if orderBy is not None:
        params["orderBy"] = orderBy
    if pageToken is not None:
        params["pageToken"] = pageToken
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    if includeItemsFromAllDrives is not None:
        params["includeItemsFromAllDrives"] = includeItemsFromAllDrives
    return request_json("GET", url, params=params)


def drive_files_get(
    fileId: str,
    *,
    fields: str = "id,name,mimeType,modifiedTime,parents,webViewLink,owners,permissions",
    supportsAllDrives: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}"
    params: Dict[str, Any] = {"fields": fields}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("GET", url, params=params)


def drive_permissions_create(
    fileId: str,
    *,
    permission: Dict[str, Any],
    fields: str = "id,type,role,emailAddress,domain,allowFileDiscovery",
    sendNotificationEmail: Optional[bool] = None,
    supportsAllDrives: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/permissions"
    params: Dict[str, Any] = {"fields": fields}
    if sendNotificationEmail is not None:
        params["sendNotificationEmail"] = sendNotificationEmail
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", url, params=params, json_body=permission)
