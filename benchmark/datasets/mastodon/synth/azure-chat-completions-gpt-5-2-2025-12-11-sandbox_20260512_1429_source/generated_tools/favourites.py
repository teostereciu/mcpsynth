from typing import Any, Dict, Optional

from .http_client import MastodonClient


def list_favourites(*, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/favourites"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/favourites", params=params)
