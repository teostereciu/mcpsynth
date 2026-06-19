from typing import Any, Dict, List, Optional

from ._client import request_json


def get_public_timeline(
    *,
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if local is not None:
        params["local"] = "true" if local else "false"
    if remote is not None:
        params["remote"] = "true" if remote else "false"
    if only_media is not None:
        params["only_media"] = "true" if only_media else "false"
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", "/api/v1/timelines/public", params=params)


def get_hashtag_timeline(
    hashtag: str,
    *,
    any_tags: Optional[List[str]] = None,
    all_tags: Optional[List[str]] = None,
    none_tags: Optional[List[str]] = None,
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if any_tags:
        for i, t in enumerate(any_tags):
            params[f"any[{i}]"] = t
    if all_tags:
        for i, t in enumerate(all_tags):
            params[f"all[{i}]"] = t
    if none_tags:
        for i, t in enumerate(none_tags):
            params[f"none[{i}]"] = t
    if local is not None:
        params["local"] = "true" if local else "false"
    if remote is not None:
        params["remote"] = "true" if remote else "false"
    if only_media is not None:
        params["only_media"] = "true" if only_media else "false"
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", f"/api/v1/timelines/tag/{hashtag}", params=params)


def get_home_timeline(
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", "/api/v1/timelines/home", params=params)


def get_list_timeline(
    list_id: str,
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", f"/api/v1/timelines/list/{list_id}", params=params)
