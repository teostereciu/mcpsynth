from typing import Any, Optional

from .client import MastodonClient


def bookmarks_list(client: MastodonClient, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        "/api/v1/bookmarks",
        params={"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id},
    )


def statuses_bookmark(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/bookmark")


def statuses_unbookmark(client: MastodonClient, status_id: str) -> Any:
    return client.request("POST", f"/api/v1/statuses/{status_id}/unbookmark")
