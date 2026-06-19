"""
Mastodon API — Accounts domain tools.
Covers: verify credentials, get account, follow, unfollow, followers, following,
        mute, unmute, block, unblock, account statuses.
"""

import requests
from config import BASE_URL, HEADERS


def get_authenticated_account() -> dict:
    """
    Retrieve the profile of the currently authenticated account.

    Returns:
        The CredentialAccount object as a dict, or an error dict.
    """
    url = f"{BASE_URL}/accounts/verify_credentials"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_account(account_id: str) -> dict:
    """
    Retrieve a public account by its ID.

    Args:
        account_id: The ID of the account.

    Returns:
        The Account object as a dict, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def follow_account(account_id: str, reblogs: bool = True, notify: bool = False) -> dict:
    """
    Follow an account.

    Args:
        account_id: The ID of the account to follow.
        reblogs: Whether to show reblogs from this account in the home timeline.
        notify: Whether to receive notifications when this account posts.

    Returns:
        A Relationship object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/follow"
    try:
        resp = requests.post(
            url, headers=HEADERS, json={"reblogs": reblogs, "notify": notify}
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def unfollow_account(account_id: str) -> dict:
    """
    Unfollow an account.

    Args:
        account_id: The ID of the account to unfollow.

    Returns:
        A Relationship object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/unfollow"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_account_followers(
    account_id: str, max_id: str = None, since_id: str = None, limit: int = 40
) -> list:
    """
    List accounts that follow the given account.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        limit: Maximum number of results (default 40, max 80).

    Returns:
        A list of Account objects, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/followers"
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_account_following(
    account_id: str, max_id: str = None, since_id: str = None, limit: int = 40
) -> list:
    """
    List accounts that the given account follows.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        limit: Maximum number of results (default 40, max 80).

    Returns:
        A list of Account objects, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/following"
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_account_statuses(
    account_id: str,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
    exclude_replies: bool = False,
    exclude_reblogs: bool = False,
    only_media: bool = False,
    pinned: bool = False,
) -> list:
    """
    List statuses posted by the given account.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
        exclude_replies: Skip statuses that are replies.
        exclude_reblogs: Skip statuses that are reblogs.
        only_media: Only return statuses with media attachments.
        pinned: Only return pinned statuses.

    Returns:
        A list of Status objects, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/statuses"
    params = {
        "limit": limit,
        "exclude_replies": exclude_replies,
        "exclude_reblogs": exclude_reblogs,
        "only_media": only_media,
        "pinned": pinned,
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


def get_account_relationships(account_ids: list) -> list:
    """
    Check relationships between the authenticated account and one or more accounts.

    Args:
        account_ids: List of account IDs to check relationships for.

    Returns:
        A list of Relationship objects, or an error dict.
    """
    url = f"{BASE_URL}/accounts/relationships"
    params = [("id[]", aid) for aid in account_ids]
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def mute_account(account_id: str, notifications: bool = True, duration: int = 0) -> dict:
    """
    Mute an account (hide their posts and/or notifications).

    Args:
        account_id: The ID of the account to mute.
        notifications: Whether to mute notifications from this account.
        duration: How long to mute (in seconds). 0 means indefinite.

    Returns:
        A Relationship object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/mute"
    try:
        resp = requests.post(
            url,
            headers=HEADERS,
            json={"notifications": notifications, "duration": duration},
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def unmute_account(account_id: str) -> dict:
    """
    Unmute an account.

    Args:
        account_id: The ID of the account to unmute.

    Returns:
        A Relationship object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/unmute"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def block_account(account_id: str) -> dict:
    """
    Block an account.

    Args:
        account_id: The ID of the account to block.

    Returns:
        A Relationship object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/block"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def unblock_account(account_id: str) -> dict:
    """
    Unblock an account.

    Args:
        account_id: The ID of the account to unblock.

    Returns:
        A Relationship object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/{account_id}/unblock"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def lookup_account(acct: str) -> dict:
    """
    Look up an account by its username (and optional domain).

    Args:
        acct: The username (e.g. 'user' or 'user@example.com').

    Returns:
        The Account object, or an error dict.
    """
    url = f"{BASE_URL}/accounts/lookup"
    try:
        resp = requests.get(url, headers=HEADERS, params={"acct": acct})
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}
