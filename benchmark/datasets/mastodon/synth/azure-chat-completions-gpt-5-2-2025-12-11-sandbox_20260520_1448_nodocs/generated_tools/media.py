import os
from typing import Any, Dict, Optional

from .client import MastodonClient


def upload_media(file_path: str, *, description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    """POST /api/v2/media"""
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    client = MastodonClient()
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus

    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            # Use multipart form; include optional fields as query params (works for Mastodon)
            params = data if data else None
            return client.request("POST", "/api/v2/media", params=params, json=None, files=files)
    except Exception as e:
        return {"error": str(e)}
