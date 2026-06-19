from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import request_json


def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None, thumbnail_path: Optional[str] = None) -> Dict[str, Any]:
    files: Dict[str, Any] = {}
    try:
        files["file"] = open(file_path, "rb")
    except Exception as e:
        return {"error": f"Failed to open file: {e}"}

    thumb_fh = None
    if thumbnail_path:
        try:
            thumb_fh = open(thumbnail_path, "rb")
            files["thumbnail"] = thumb_fh
        except Exception as e:
            files["file"].close()
            return {"error": f"Failed to open thumbnail: {e}"}

    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus

    try:
        return request_json("POST", "/api/v2/media", data=data or None, files=files, require_auth=True)
    finally:
        try:
            files["file"].close()
        except Exception:
            pass
        if thumb_fh:
            try:
                thumb_fh.close()
            except Exception:
                pass


def get_media(media_id: str) -> Dict[str, Any]:
    return request_json("GET", f"/api/v1/media/{media_id}", require_auth=True)
