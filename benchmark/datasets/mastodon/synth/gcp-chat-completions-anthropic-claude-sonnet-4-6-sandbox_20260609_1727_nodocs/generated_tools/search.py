"""Mastodon API — Search domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def search(
    query: str,
    type: str = None,
    resolve: bool = False,
    following: bool = False,
    account_id: str = None,
    limit: int = 20,
    offset: int = 0,
    min_id: str = None,
    max_id: str = None,
) -> dict:
    """Perform a full-text search across accounts, statuses, and hashtags.

    Args:
        query: The search query string.
        type: Restrict results to a specific type: 'accounts', 'statuses', or 'hashtags'.
        resolve: Attempt to resolve non-local accounts and statuses via WebFinger.
        following: Only include accounts the authenticated user is following.
        account_id: If searching statuses, restrict to those from this account ID.
        limit: Maximum number of results per type (default 20, max 40).
        offset: Offset for pagination.
        min_id: Return results newer than this ID.
        max_id: Return results older than this ID.
    """
    params = {"q": query, "resolve": resolve, "following": following, "limit": limit, "offset": offset}
    if type:
        params["type"] = type
    if account_id:
        params["account_id"] = account_id
    if min_id:
        params["min_id"] = min_id
    if max_id:
        params["max_id"] = max_id
    try:
        r = requests.get(f"{BASE_URL}/search", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def search_accounts(query: str, limit: int = 20, resolve: bool = False, following: bool = False) -> list:
    """Search for accounts matching a query string.

    Args:
        query: The search query (username, display name, etc.).
        limit: Maximum number of results (default 20, max 80).
        resolve: Attempt to resolve non-local accounts via WebFinger.
        following: Only include accounts the authenticated user is following.
    """
    params = {"q": query, "limit": limit, "resolve": resolve, "following": following}
    try:
        r = requests.get(f"{BASE_URL}/accounts/search", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
