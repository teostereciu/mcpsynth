from typing import Any, Dict, Optional

from .client import MastodonClient


def list_favourites(client: MastodonClient, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/api/v1/favourites", params=params or None)
