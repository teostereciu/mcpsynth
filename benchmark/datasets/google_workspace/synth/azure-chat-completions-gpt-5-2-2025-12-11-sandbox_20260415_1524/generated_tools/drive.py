from typing import Any, Dict, Optional

from .http import request_bytes, request_json

DRIVE_BASE = "https://www.googleapis.com/drive/v3"


def drive_files_list(*, q: Optional[str] = None, pageSize: Optional[int] = None, pageToken: Optional[str] = None, corpora: Optional[str] = None, driveId: Optional[str] = None, includeItemsFromAllDrives: Optional[bool] = None, supportsAllDrives: Optional[bool] = None, orderBy: Optional[str] = None, spaces: Optional[str] = None, fields: Optional[str] = None) -> Any:
    url = f"{DRIVE_BASE}/files"
    params: Dict[str, Any] = {}
    for k, v in {
        "q": q,
        "pageSize": pageSize,
        "pageToken": pageToken,
        "corpora": corpora,
        "driveId": driveId,
        "includeItemsFromAllDrives": includeItemsFromAllDrives,
        "supportsAllDrives": supportsAllDrives,
        "orderBy": orderBy,
        "spaces": spaces,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", url, params=params)
