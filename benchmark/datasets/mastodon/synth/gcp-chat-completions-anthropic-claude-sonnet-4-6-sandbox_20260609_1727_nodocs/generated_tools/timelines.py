"""Mastodon API — Timelines domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_home_timeline(
    limit: int = 20,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
) -> list:
    """Fetch the home timeline (statuses from followed accounts and self).

    Args:
        limit: Maximum number of statuses to return (default 20, max 40).
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = requests.get(f"{BASE_URL}/timelines/home", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_public_timeline(
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    limit: int = 20,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
) -> list:
    """Fetch the public (federated) timeline.

    Args:
        local: Show only local statuses (from this instance).
        remote: Show only remote statuses (from other instances).
        only_media: Show only statuses with media attachments.
        limit: Maximum number of statuses to return (default 20, max 40).
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
    """
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
        r = requests.get(f"{BASE_URL}/timelines/public", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    only_media: bool = False,
    limit: int = 20,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
) -> list:
    """Fetch statuses for a given hashtag.

    Args:
        hashtag: The hashtag to search (without the leading '#').
        local: Show only local statuses.
        only_media: Show only statuses with media attachments.
        limit: Maximum number of statuses to return (default 20, max 40).
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
    """
    params = {"local": local, "only_media": only_media, "limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = requests.get(
            f"{BASE_URL}/timelines/tag/{hashtag}", headers=_headers(), params=params
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_list_timeline(
    list_id: str,
    limit: int = 20,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
) -> list:
    """Fetch statuses from a specific list timeline.

    Args:
        list_id: The ID of the list whose timeline to fetch.
        limit: Maximum number of statuses to return (default 20, max 40).
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = requests.get(
            f"{BASE_URL}/timelines/list/{list_id}", headers=_headers(), params=params
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
