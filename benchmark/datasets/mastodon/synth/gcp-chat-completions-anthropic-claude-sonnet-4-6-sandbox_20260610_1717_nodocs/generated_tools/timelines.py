"""
Mastodon API — Timelines domain tools.
Covers: home, public, hashtag, list timelines.
"""

import os
import requests


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {"Authorization": f"Bearer {os.environ.get('MASTODON_ACCESS_TOKEN', '')}"}
    )
    return s


def _base() -> str:
    return os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"


# ---------------------------------------------------------------------------
# Home timeline
# ---------------------------------------------------------------------------
def get_home_timeline(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses from accounts the authenticated user follows.

    Args:
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects or an error dict.
    """
    params: dict = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = _session().get(f"{_base()}/timelines/home", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Public timeline
# ---------------------------------------------------------------------------
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
    Return statuses from the public (federated) timeline.

    Args:
        local: Only return statuses from the local instance.
        remote: Only return statuses from remote instances.
        only_media: Only return statuses with media attachments.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects or an error dict.
    """
    params: dict = {
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
        r = _session().get(f"{_base()}/timelines/public", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Hashtag timeline
# ---------------------------------------------------------------------------
def get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses containing the given hashtag.

    Args:
        hashtag: The hashtag to search (without the '#' prefix).
        local: Only return statuses from the local instance.
        remote: Only return statuses from remote instances.
        only_media: Only return statuses with media attachments.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects or an error dict.
    """
    params: dict = {
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
        r = _session().get(f"{_base()}/timelines/tag/{hashtag}", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# List timeline
# ---------------------------------------------------------------------------
def get_list_timeline(
    list_id: str,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses from accounts in the given list.

    Args:
        list_id: The ID of the list.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects or an error dict.
    """
    params: dict = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = _session().get(f"{_base()}/timelines/list/{list_id}", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}
