from typing import Any, Dict, List, Optional

from .common import mastodon_request


def _clean(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


def get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return mastodon_request("GET", "/timelines/home", params=_clean({"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}))


def get_public_timeline(local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return mastodon_request("GET", "/timelines/public", params=_clean({"local": local, "remote": remote, "only_media": only_media, "limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}))


def get_hashtag_timeline(hashtag: str, any_tags: Optional[List[str]] = None, all_tags: Optional[List[str]] = None, none_tags: Optional[List[str]] = None, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"local": local, "remote": remote, "only_media": only_media, "limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}
    if any_tags is not None:
        for idx, value in enumerate(any_tags):
            params[f"any[{idx}]"] = value
    if all_tags is not None:
        for idx, value in enumerate(all_tags):
            params[f"all[{idx}]"] = value
    if none_tags is not None:
        for idx, value in enumerate(none_tags):
            params[f"none[{idx}]"] = value
    return mastodon_request("GET", f"/timelines/tag/{hashtag}", params=_clean(params))


def get_list_timeline(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return mastodon_request("GET", f"/timelines/list/{list_id}", params=_clean({"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}))
