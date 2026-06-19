from typing import Any, Dict, Optional

from ._client import request_json


def upload_media(
    file_path: str,
    *,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail_path: Optional[str] = None,
) -> Any:
    files: Dict[str, Any] = {}
    try:
        files["file"] = open(file_path, "rb")
        if thumbnail_path:
            files["thumbnail"] = open(thumbnail_path, "rb")
        data: Dict[str, Any] = {}
        if description is not None:
            data["description"] = description
        if focus is not None:
            data["focus"] = focus
        return request_json("POST", "/api/v2/media", data=data, files=files)
    finally:
        for f in files.values():
            try:
                f.close()
            except Exception:
                pass


def get_media(media_id: str) -> Any:
    return request_json("GET", f"/api/v1/media/{media_id}")


def update_media(
    media_id: str,
    *,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail_path: Optional[str] = None,
) -> Any:
    files: Dict[str, Any] = {}
    try:
        if thumbnail_path:
            files["thumbnail"] = open(thumbnail_path, "rb")
        data: Dict[str, Any] = {}
        if description is not None:
            data["description"] = description
        if focus is not None:
            data["focus"] = focus
        return request_json("PUT", f"/api/v1/media/{media_id}", data=data, files=files if files else None)
    finally:
        for f in files.values():
            try:
                f.close()
            except Exception:
                pass


def delete_media(media_id: str) -> Any:
    return request_json("DELETE", f"/api/v1/media/{media_id}")
