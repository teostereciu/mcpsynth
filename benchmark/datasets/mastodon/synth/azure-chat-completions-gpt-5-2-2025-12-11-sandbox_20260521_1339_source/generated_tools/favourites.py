from typing import Any, Optional

from .client import MastodonClient


def favourites_list(client: MastodonClient, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        "/api/v1/favourites",
        params={"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id},
    )
