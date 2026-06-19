from typing import Any, Optional

from generated_tools.common import mastodon_request


def get_home_timeline(limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", "/api/v1/timelines/home", params={"limit": limit})


def get_public_timeline(local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", "/api/v1/timelines/public", params={"local": local, "remote": remote, "only_media": only_media, "limit": limit})


def get_hashtag_timeline(hashtag: str, local: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", f"/api/v1/timelines/tag/{hashtag}", params={"local": local, "only_media": only_media, "limit": limit})


def get_list_timeline(list_id: str, limit: Optional[int] = None) -> Any:
    return mastodon_request("GET", f"/api/v1/timelines/list/{list_id}", params={"limit": limit})
