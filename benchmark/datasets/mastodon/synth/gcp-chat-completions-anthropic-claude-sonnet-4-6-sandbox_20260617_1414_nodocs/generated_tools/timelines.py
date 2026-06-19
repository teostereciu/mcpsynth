"""
Mastodon API — Timelines domain tools.
Covers: home timeline, public timeline, hashtag timeline, list timeline.
"""

import requests
from config import BASE_URL, HEADERS


def get_home_timeline(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Retrieve the home timeline (statuses from followed accounts and self).

    Args:
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
        limit: Maximum number of results to return (default 20, max 40).

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/timelines/home"
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_public_timeline(
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Retrieve the public (federated or local) timeline.

    Args:
        local: Show only statuses from the local instance.
        remote: Show only statuses from remote instances.
        only_media: Show only statuses with media attachments.
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/timelines/public"
    params = {
        "local": local,
        "remote": remote,
        "only_media": only_media,
        "limit": limit,
    }
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    only_media: bool = False,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Retrieve a timeline of public statuses containing the given hashtag.

    Args:
        hashtag: The hashtag to search (without the leading '#').
        local: Show only statuses from the local instance.
        only_media: Show only statuses with media attachments.
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/timelines/tag/{hashtag}"
    params = {"local": local, "only_media": only_media, "limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_list_timeline(
    list_id: str,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Retrieve the timeline of statuses for a specific list.

    Args:
        list_id: The ID of the list.
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/timelines/list/{list_id}"
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}
