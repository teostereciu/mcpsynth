from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", "/api/v1/timelines/home", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))


def get_public_timeline(local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", "/api/v1/timelines/public", params=clean_params(local=local, remote=remote, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))


def get_hashtag_timeline(hashtag: str, any_tags: Optional[list[str]] = None, all_tags: Optional[list[str]] = None, none_tags: Optional[list[str]] = None, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    params = clean_params(local=local, remote=remote, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)
    if any_tags is not None:
        params["any[]"] = any_tags
    if all_tags is not None:
        params["all[]"] = all_tags
    if none_tags is not None:
        params["none[]"] = none_tags
    return mastodon_request("GET", f"/api/v1/timelines/tag/{hashtag}", params=params)


def get_list_timeline(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", f"/api/v1/timelines/list/{list_id}", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))
