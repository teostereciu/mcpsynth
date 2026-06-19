from typing import Any, Dict, Optional

from .client import MastodonClient


def timelines_home(client: MastodonClient, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if local is not None:
        params["local"] = "true" if local else "false"
    return client.request("GET", "/api/v1/timelines/home", params=params or None)


def timelines_public(client: MastodonClient, *, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if local is not None:
        params["local"] = "true" if local else "false"
    if remote is not None:
        params["remote"] = "true" if remote else "false"
    if only_media is not None:
        params["only_media"] = "true" if only_media else "false"
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return client.request("GET", "/api/v1/timelines/public", params=params or None)


def timelines_tag(client: MastodonClient, hashtag: str, *, local: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if local is not None:
        params["local"] = "true" if local else "false"
    if only_media is not None:
        params["only_media"] = "true" if only_media else "false"
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return client.request("GET", f"/api/v1/timelines/tag/{hashtag}", params=params or None)


def timelines_list(client: MastodonClient, list_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return client.request("GET", f"/api/v1/timelines/list/{list_id}", params=params or None)
