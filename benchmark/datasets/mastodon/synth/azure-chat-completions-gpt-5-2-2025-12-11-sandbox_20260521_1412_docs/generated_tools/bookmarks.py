from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import request_json


def list_bookmarks(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return request_json("GET", "/api/v1/bookmarks", params=params or None, require_auth=True)
