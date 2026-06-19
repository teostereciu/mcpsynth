from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def list_bookmarks(max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v1/bookmarks

    Docs: docs/api_bookmarks.md
    """
    client = MastodonClient()
    params = compact_params({"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit})
    result, meta = client.request("GET", "/api/v1/bookmarks", params=params)
    return {"result": result, "meta": meta}
