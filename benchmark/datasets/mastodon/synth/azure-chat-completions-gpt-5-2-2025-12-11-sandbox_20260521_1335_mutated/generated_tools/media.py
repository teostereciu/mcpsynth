from __future__ import annotations

import os
from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def upload_media(
    file_path: str,
    description: Optional[str] = None,
    focus: Optional[str] = None,
    thumbnail_path: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /api/v2/media

    Docs: docs/api_media.md
    """
    if not os.path.exists(file_path):
        return {"error": f"file_path not found: {file_path}"}

    files: Dict[str, Any] = {"file": open(file_path, "rb")}
    if thumbnail_path:
        if not os.path.exists(thumbnail_path):
            return {"error": f"thumbnail_path not found: {thumbnail_path}"}
        files["thumbnail"] = open(thumbnail_path, "rb")

    data = compact_params({"description": description, "focus": focus})

    client = MastodonClient()
    try:
        result, meta = client.request("POST", "/api/v2/media", data=data, files=files)
        return {"result": result, "meta": meta}
    finally:
        for f in files.values():
            try:
                f.close()
            except Exception:
                pass


def get_media(media_id: str) -> Dict[str, Any]:
    """GET /api/v1/media/:id

    Docs: docs/api_media.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", f"/api/v1/media/{media_id}")
    return {"result": result, "meta": meta}
