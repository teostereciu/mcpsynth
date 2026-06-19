from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def get_home_timeline(max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v1/timelines/home

    Docs: docs/api_timelines.md
    """
    client = MastodonClient()
    params = compact_params({"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit})
    result, meta = client.request("GET", "/api/v1/timelines/home", params=params)
    return {"result": result, "meta": meta}


def get_public_timeline(
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /api/v1/timelines/public

    Docs: docs/api_timelines.md
    """
    client = MastodonClient()
    params = compact_params(
        {
            "local": str(bool(local)).lower() if local is not None else None,
            "remote": str(bool(remote)).lower() if remote is not None else None,
            "only_media": str(bool(only_media)).lower() if only_media is not None else None,
            "max_id": max_id,
            "since_id": since_id,
            "min_id": min_id,
            "limit": limit,
        }
    )
    result, meta = client.request("GET", "/api/v1/timelines/public", params=params)
    return {"result": result, "meta": meta}


def get_hashtag_timeline(
    hashtag: str,
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
) -> Dict[str, Any]:
    """GET /api/v1/timelines/tag/:hashtag

    Docs: docs/api_timelines.md
    """
    client = MastodonClient()
    params: Dict[str, Any] = {
        "local": str(bool(local)).lower() if local is not None else None,
        "remote": str(bool(remote)).lower() if remote is not None else None,
        "only_media": str(bool(only_media)).lower() if only_media is not None else None,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "limit": limit,
    }
    if any_tags:
        for i, t in enumerate(any_tags):
            params[f"any[{i}]"] = t
    if all_tags:
        for i, t in enumerate(all_tags):
            params[f"all[{i}]"] = t
    if none_tags:
        for i, t in enumerate(none_tags):
            params[f"none[{i}]"] = t

    result, meta = client.request("GET", f"/api/v1/timelines/tag/{hashtag}", params=compact_params(params))
    return {"result": result, "meta": meta}


def get_list_timeline(list_id: str, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v1/timelines/list/:list_id

    Docs: docs/api_timelines.md
    """
    client = MastodonClient()
    params = compact_params({"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit})
    result, meta = client.request("GET", f"/api/v1/timelines/list/{list_id}", params=params)
    return {"result": result, "meta": meta}
