"""
Mastodon API — Favourites domain tools.
Covers: list favourited statuses.
"""

import requests
from config import BASE_URL, HEADERS


def get_favourites(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Retrieve statuses favourited by the authenticated account.

    Args:
        max_id: Return results older than this status ID.
        since_id: Return results newer than this status ID.
        min_id: Return results immediately newer than this status ID.
        limit: Maximum number of results (default 20, max 40).

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/favourites"
    params: dict = {"limit": limit}
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
