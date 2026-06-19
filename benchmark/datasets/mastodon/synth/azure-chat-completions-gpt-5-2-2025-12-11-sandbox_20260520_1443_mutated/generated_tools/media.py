from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_media.md


def upload_media(
    file_path: str,
    *,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail_path: Optional[str] = None,
) -> Any:
    """POST /api/v2/media"""
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus

    files: Dict[str, Any] = {}
    try:
        files["file"] = open(file_path, "rb")
    except Exception as e:
        return {"error": f"cannot_open_file: {e}"}

    thumb_fh = None
    if thumbnail_path is not None:
        try:
            thumb_fh = open(thumbnail_path, "rb")
            files["thumbnail"] = thumb_fh
        except Exception as e:
            try:
                files["file"].close()
            except Exception:
                pass
            return {"error": f"cannot_open_thumbnail: {e}"}

    try:
        return request_json("POST", "/api/v2/media", data=data, files=files)
    finally:
        try:
            files["file"].close()
        except Exception:
            pass
        if thumb_fh is not None:
            try:
                thumb_fh.close()
            except Exception:
                pass


def get_media(media_id: str) -> Any:
    """GET /api/v1/media/:id"""
    return request_json("GET", f"/api/v1/media/{media_id}")


def update_media(
    media_id: str,
    *,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail_path: Optional[str] = None,
) -> Any:
    """PUT /api/v1/media/:id"""
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus

    files: Optional[Dict[str, Any]] = None
    thumb_fh = None
    if thumbnail_path is not None:
        files = {}
        try:
            thumb_fh = open(thumbnail_path, "rb")
            files["thumbnail"] = thumb_fh
        except Exception as e:
            return {"error": f"cannot_open_thumbnail: {e}"}

    try:
        return request_json("PUT", f"/api/v1/media/{media_id}", data=data, files=files)
    finally:
        if thumb_fh is not None:
            try:
                thumb_fh.close()
            except Exception:
                pass


def delete_media(media_id: str) -> Any:
    """DELETE /api/v1/media/:id"""
    return request_json("DELETE", f"/api/v1/media/{media_id}")
