from typing import Any, Dict, Optional

from .client import MastodonClient


def list_bookmarks(*, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    """GET /api/v1/bookmarks"""
    client = MastodonClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/api/v1/bookmarks", params=params)


def bookmark_status(status_id: str) -> Any:
    """POST /api/v1/statuses/{id}/bookmark"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str) -> Any:
    """POST /api/v1/statuses/{id}/unbookmark"""
    client = MastodonClient()
    return client.request("POST", f"/api/v1/statuses/{status_id}/unbookmark")
