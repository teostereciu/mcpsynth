from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import request_json


def get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return request_json("GET", "/api/v1/timelines/home", params=params or None, require_auth=True)


def get_public_timeline(
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if local is not None:
        params["local"] = str(bool(local)).lower()
    if remote is not None:
        params["remote"] = str(bool(remote)).lower()
    if only_media is not None:
        params["only_media"] = str(bool(only_media)).lower()
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return request_json("GET", "/api/v1/timelines/public", params=params or None, require_auth=False)


def get_hashtag_timeline(
    hashtag: str,
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    any_tags: Optional[list[str]] = None,
    all_tags: Optional[list[str]] = None,
    none_tags: Optional[list[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if any_tags is not None:
        params["any[]"] = any_tags
    if all_tags is not None:
        params["all[]"] = all_tags
    if none_tags is not None:
        params["none[]"] = none_tags
    if local is not None:
        params["local"] = str(bool(local)).lower()
    if remote is not None:
        params["remote"] = str(bool(remote)).lower()
    if only_media is not None:
        params["only_media"] = str(bool(only_media)).lower()
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return request_json("GET", f"/api/v1/timelines/tag/{hashtag}", params=params or None, require_auth=False)


def get_list_timeline(
    list_id: str,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return request_json("GET", f"/api/v1/timelines/list/{list_id}", params=params or None, require_auth=True)
