from typing import Any, Dict, Optional

from .http_client import MastodonClient


def list_bookmarks(*, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/bookmarks"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/bookmarks", params=params)
