from typing import Any, Optional

from .client import MastodonClient


def timelines_home(client: MastodonClient, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None) -> Any:
    return client.request(
        "GET",
        "/api/v1/timelines/home",
        params={"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id, "local": local},
    )


def timelines_public(client: MastodonClient, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None) -> Any:
    return client.request(
        "GET",
        "/api/v1/timelines/public",
        params={
            "limit": limit,
            "max_id": max_id,
            "since_id": since_id,
            "min_id": min_id,
            "local": local,
            "remote": remote,
            "only_media": only_media,
        },
    )


def timelines_tag(client: MastodonClient, hashtag: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None, only_media: Optional[bool] = None) -> Any:
    return client.request(
        "GET",
        f"/api/v1/timelines/tag/{hashtag}",
        params={"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id, "local": local, "only_media": only_media},
    )


def timelines_list(client: MastodonClient, list_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        f"/api/v1/timelines/list/{list_id}",
        params={"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id},
    )
