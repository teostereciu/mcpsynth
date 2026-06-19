"""Mastodon API — Bookmarks domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_bookmarks(
    limit: int = 20,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
) -> list:
    """Fetch all statuses bookmarked by the authenticated account.

    Args:
        limit: Maximum number of results (default 20, max 40).
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
        r = requests.get(f"{BASE_URL}/bookmarks", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
