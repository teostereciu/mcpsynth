from typing import Any, Dict, Optional

from .http import request_json
from .server import mcp

DRIVE_BASE = "https://www.googleapis.com/drive/v3"


@mcp.tool()
def drive_files_create(file: Optional[Dict[str, Any]] = None, supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files"
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", url, params=params, json_body=file or {})


@mcp.tool()
def drive_files_get(fileId: str = "", fields: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}"
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_files_list(
    q: Optional[str] = None,
    pageSize: int = 10,
    pageToken: Optional[str] = None,
    fields: Optional[str] = None,
    orderBy: Optional[str] = None,
    spaces: Optional[str] = None,
    corpora: Optional[str] = None,
    driveId: Optional[str] = None,
    includeItemsFromAllDrives: Optional[bool] = None,
    supportsAllDrives: Optional[bool] = None,
) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files"
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
    if corpora is not None:
        params["corpora"] = corpora
    if driveId is not None:
        params["driveId"] = driveId
    if includeItemsFromAllDrives is not None:
        params["includeItemsFromAllDrives"] = includeItemsFromAllDrives
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_files_update(fileId: str = "", file: Optional[Dict[str, Any]] = None, supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}"
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("PATCH", url, params=params, json_body=file or {})


@mcp.tool()
def drive_files_delete(fileId: str = "", supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}"
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("DELETE", url, params=params)


@mcp.tool()
def drive_files_copy(fileId: str = "", file: Optional[Dict[str, Any]] = None, supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/copy"
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", url, params=params, json_body=file or {})


@mcp.tool()
def drive_files_export(fileId: str = "", mimeType: str = "application/pdf") -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/export"
    params = {"mimeType": mimeType}
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_permissions_create(fileId: str = "", permission: Optional[Dict[str, Any]] = None, sendNotificationEmail: Optional[bool] = None, emailMessage: Optional[str] = None, transferOwnership: Optional[bool] = None, supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/permissions"
    params: Dict[str, Any] = {}
    if sendNotificationEmail is not None:
        params["sendNotificationEmail"] = sendNotificationEmail
    if emailMessage is not None:
        params["emailMessage"] = emailMessage
    if transferOwnership is not None:
        params["transferOwnership"] = transferOwnership
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("POST", url, params=params, json_body=permission or {})


@mcp.tool()
def drive_permissions_list(fileId: str = "", pageSize: int = 100, pageToken: Optional[str] = None, supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/permissions"
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_permissions_delete(fileId: str = "", permissionId: str = "", supportsAllDrives: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/permissions/{permissionId}"
    params: Dict[str, Any] = {}
    if supportsAllDrives is not None:
        params["supportsAllDrives"] = supportsAllDrives
    return request_json("DELETE", url, params=params)


@mcp.tool()
def drive_drives_list(pageSize: int = 10, pageToken: Optional[str] = None, q: Optional[str] = None, useDomainAdminAccess: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/drives"
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if q is not None:
        params["q"] = q
    if useDomainAdminAccess is not None:
        params["useDomainAdminAccess"] = useDomainAdminAccess
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_drives_get(driveId: str = "", useDomainAdminAccess: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/drives/{driveId}"
    params: Dict[str, Any] = {}
    if useDomainAdminAccess is not None:
        params["useDomainAdminAccess"] = useDomainAdminAccess
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_comments_list(fileId: str = "", pageSize: int = 20, pageToken: Optional[str] = None, includeDeleted: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/comments"
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if includeDeleted is not None:
        params["includeDeleted"] = includeDeleted
    return request_json("GET", url, params=params)


@mcp.tool()
def drive_replies_list(fileId: str = "", commentId: str = "", pageSize: int = 20, pageToken: Optional[str] = None, includeDeleted: Optional[bool] = None) -> Dict[str, Any]:
    url = f"{DRIVE_BASE}/files/{fileId}/comments/{commentId}/replies"
    params: Dict[str, Any] = {"pageSize": pageSize}
    if pageToken is not None:
        params["pageToken"] = pageToken
    if includeDeleted is not None:
        params["includeDeleted"] = includeDeleted
    return request_json("GET", url, params=params)
