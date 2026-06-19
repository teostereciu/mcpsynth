"""
Mastodon API — Search domain tools.
Covers: unified search, search accounts, search statuses, search hashtags.
"""

import requests
from config import BASE_URL, HEADERS


def search(
    query: str,
    type: str = None,
    resolve: bool = False,
    following: bool = False,
    account_id: str = None,
    max_id: str = None,
    min_id: str = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Perform a unified search across accounts, statuses, and hashtags.

    Args:
        query: The search query string.
        type: Restrict results to a specific type: 'accounts', 'statuses', or 'hashtags'.
        resolve: Attempt to resolve the query as a remote resource (WebFinger lookup).
        following: Only include accounts the authenticated user follows (for account search).
        account_id: Filter statuses by this account ID.
        max_id: Return results older than this ID (for statuses).
        min_id: Return results immediately newer than this ID (for statuses).
        limit: Maximum number of results per type (default 20, max 40).
        offset: Offset for pagination.

    Returns:
        A dict with keys 'accounts', 'statuses', and 'hashtags', or an error dict.
    """
    url = f"{BASE_URL}/search"
    params: dict = {
        "q": query,
        "resolve": resolve,
        "following": following,
        "limit": limit,
        "offset": offset,
    }
    if type:
        params["type"] = type
    if account_id:
        params["account_id"] = account_id
    if max_id:
        params["max_id"] = max_id
    if min_id:
        params["min_id"] = min_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def search_accounts(
    query: str,
    limit: int = 40,
    resolve: bool = False,
    following: bool = False,
) -> list:
    """
    Search for accounts matching a query string.

    Args:
        query: The search query (username, display name, or domain).
        limit: Maximum number of results (default 40, max 80).
        resolve: Attempt to resolve the query as a remote account via WebFinger.
        following: Only return accounts the authenticated user follows.

    Returns:
        A list of Account objects, or an error dict.
    """
    url = f"{BASE_URL}/accounts/search"
    params = {
        "q": query,
        "limit": limit,
        "resolve": resolve,
        "following": following,
    }
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def search_statuses(query: str, limit: int = 20, offset: int = 0) -> list:
    """
    Search for statuses matching a query string.

    Args:
        query: The search query.
        limit: Maximum number of results (default 20, max 40).
        offset: Offset for pagination.

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/search"
    params = {"q": query, "type": "statuses", "limit": limit, "offset": offset}
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data.get("statuses", data)
    except requests.RequestException as e:
        return {"error": str(e)}


def search_hashtags(query: str, limit: int = 20, offset: int = 0) -> list:
    """
    Search for hashtags matching a query string.

    Args:
        query: The search query (without the leading '#').
        limit: Maximum number of results (default 20, max 40).
        offset: Offset for pagination.

    Returns:
        A list of Tag objects, or an error dict.
    """
    url = f"{BASE_URL}/search"
    params = {"q": query, "type": "hashtags", "limit": limit, "offset": offset}
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data.get("hashtags", data)
    except requests.RequestException as e:
        return {"error": str(e)}
