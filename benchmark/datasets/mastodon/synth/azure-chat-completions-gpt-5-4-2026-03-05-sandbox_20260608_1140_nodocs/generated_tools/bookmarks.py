from typing import Any, Optional

from generated_tools.common import mastodon_request


def list_bookmarks(limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", "/api/v1/bookmarks", params={"limit": limit})


def bookmark_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/bookmark")


def unbookmark_status(status_id: str) -> Any:
    return mastodon_request("POST", f"/api/v1/statuses/{status_id}/unbookmark")


def list_favourites(limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", "/api/v1/favourites", params={"limit": limit})
