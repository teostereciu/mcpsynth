"""
Mastodon API — Favourites domain tools.
Covers: list favourited statuses.
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
# List favourited statuses
# ---------------------------------------------------------------------------
def get_favourites(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses favourited by the authenticated account.

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
        r = _session().get(f"{_base()}/favourites", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}
