from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_bookmarks.md


def list_bookmarks(
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    """GET /api/v1/bookmarks"""
    params: Dict[str, Any] = {}
    for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/api/v1/bookmarks", params=params)
