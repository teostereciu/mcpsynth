from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_timelines.md


def get_home_timeline(
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    """GET /api/v1/timelines/home"""
    params: Dict[str, Any] = {}
    for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/api/v1/timelines/home", params=params)


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
    """GET /api/v1/timelines/public"""
    params: Dict[str, Any] = {}
    for k, v in {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/api/v1/timelines/public", params=params)


def get_hashtag_timeline(
    hashtag: str,
    *,
    any_tags: Optional[list[str]] = None,
    all_tags: Optional[list[str]] = None,
    none_tags: Optional[list[str]] = None,
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    """GET /api/v1/timelines/tag/:hashtag"""
    params: Dict[str, Any] = {}
    if any_tags is not None:
        for i, t in enumerate(any_tags):
            params[f"any[{i}]"] = t
    if all_tags is not None:
        for i, t in enumerate(all_tags):
            params[f"all[{i}]"] = t
    if none_tags is not None:
        for i, t in enumerate(none_tags):
            params[f"none[{i}]"] = t
    for k, v in {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/timelines/tag/{hashtag}", params=params)


def get_list_timeline(
    list_id: str,
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    """GET /api/v1/timelines/list/:list_id"""
    params: Dict[str, Any] = {}
    for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/timelines/list/{list_id}", params=params)
