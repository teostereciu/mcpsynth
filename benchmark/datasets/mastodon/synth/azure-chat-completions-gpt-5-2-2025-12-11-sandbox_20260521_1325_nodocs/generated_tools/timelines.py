from typing import Any, Dict, Optional

from .client import MastodonClient


def get_home_timeline(client: MastodonClient, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/api/v1/timelines/home", params=params or None)


def get_public_timeline(client: MastodonClient, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/api/v1/timelines/public", params=params or None)


def get_hashtag_timeline(client: MastodonClient, hashtag: str, local: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {
        "local": local,
        "only_media": only_media,
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/api/v1/timelines/tag/{hashtag}", params=params or None)


def get_list_timeline(client: MastodonClient, list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/api/v1/timelines/list/{list_id}", params=params or None)
