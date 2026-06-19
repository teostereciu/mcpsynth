from typing import Any, Optional

from .common import mastodon_request


def get_bookmarks(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params = {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}
    return mastodon_request("GET", "/bookmarks", params={k: v for k, v in params.items() if v is not None})
