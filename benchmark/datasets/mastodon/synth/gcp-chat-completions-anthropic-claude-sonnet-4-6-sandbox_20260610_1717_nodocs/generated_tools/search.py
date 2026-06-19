"""
Mastodon API — Search domain tools.
Covers: unified search (accounts, statuses, hashtags).
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
# Unified search
# ---------------------------------------------------------------------------
def search(
    query: str,
    search_type: str = None,
    resolve: bool = False,
    following: bool = False,
    account_id: str = None,
    max_id: str = None,
    min_id: str = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Search for accounts, statuses, and hashtags.

    Args:
        query: The search query string.
        search_type: Restrict results to 'accounts', 'statuses', or 'hashtags'.
        resolve: Attempt to resolve non-local accounts and statuses via WebFinger.
        following: Only include accounts the authenticated user follows.
        account_id: Restrict statuses to those from this account.
        max_id: Return results older than this ID (statuses only).
        min_id: Return results immediately newer than this ID (statuses only).
        limit: Maximum number of results per category (default 20, max 40).
        offset: Skip the first N results (for pagination).

    Returns:
        A dict with 'accounts', 'statuses', and 'hashtags' lists, or an error dict.
    """
    params: dict = {
        "q": query,
        "resolve": resolve,
        "following": following,
        "limit": limit,
        "offset": offset,
    }
    if search_type:
        params["type"] = search_type
    if account_id:
        params["account_id"] = account_id
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = _session().get(f"{_base()}/search", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search accounts (convenience wrapper)
# ---------------------------------------------------------------------------
def search_accounts(
    query: str,
    limit: int = 40,
    resolve: bool = False,
    following: bool = False,
) -> list:
    """
    Search for accounts matching the query string.

    Args:
        query: The search query (username, display name, or Webfinger address).
        limit: Maximum number of results (default 40, max 80).
        resolve: Attempt to resolve non-local accounts via WebFinger.
        following: Only include accounts the authenticated user follows.

    Returns:
        A list of Account objects or an error dict.
    """
    params: dict = {
        "q": query,
        "limit": limit,
        "resolve": resolve,
        "following": following,
    }
    try:
        r = _session().get(f"{_base()}/accounts/search", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search hashtags (convenience wrapper using unified search)
# ---------------------------------------------------------------------------
def search_hashtags(query: str, limit: int = 20) -> list:
    """
    Search for hashtags matching the query string.

    Args:
        query: The hashtag search query (without '#').
        limit: Maximum number of results (default 20).

    Returns:
        A list of Tag objects or an error dict.
    """
    params: dict = {"q": query, "type": "hashtags", "limit": limit}
    try:
        r = _session().get(f"{_base()}/search", params=params)
        r.raise_for_status()
        data = r.json()
        return data.get("hashtags", data)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search statuses (convenience wrapper using unified search)
# ---------------------------------------------------------------------------
def search_statuses(
    query: str,
    limit: int = 20,
    account_id: str = None,
    max_id: str = None,
    min_id: str = None,
    offset: int = 0,
) -> list:
    """
    Search for statuses matching the query string.

    Args:
        query: The search query.
        limit: Maximum number of results (default 20).
        account_id: Restrict results to statuses from this account.
        max_id: Return results older than this ID.
        min_id: Return results immediately newer than this ID.
        offset: Skip the first N results.

    Returns:
        A list of Status objects or an error dict.
    """
    params: dict = {
        "q": query,
        "type": "statuses",
        "limit": limit,
        "offset": offset,
    }
    if account_id:
        params["account_id"] = account_id
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    try:
        r = _session().get(f"{_base()}/search", params=params)
        r.raise_for_status()
        data = r.json()
        return data.get("statuses", data)
    except Exception as exc:
        return {"error": str(exc)}
