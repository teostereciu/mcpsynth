from typing import Any, Optional

from .mastodon_client import MastodonClient

client = MastodonClient()


def get_public_timeline(local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"local": local, "remote": remote, "only_media": only_media, "max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}.items() if v is not None}
    return client.request("GET", "/timelines/public", params=params)


def get_home_timeline(max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}.items() if v is not None}
    return client.request("GET", "/timelines/home", params=params)


def get_hashtag_timeline(hashtag: str, any_tags: Optional[list[str]] = None, all_tags: Optional[list[str]] = None, none_tags: Optional[list[str]] = None, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params: dict[str, Any] = {"local": local, "remote": remote, "only_media": only_media, "max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}
    for i, v in enumerate(any_tags or []): params[f"any[{i}]"] = v
    for i, v in enumerate(all_tags or []): params[f"all[{i}]"] = v
    for i, v in enumerate(none_tags or []): params[f"none[{i}]"] = v
    return client.request("GET", f"/timelines/tag/{hashtag}", params={k: v for k, v in params.items() if v is not None})
