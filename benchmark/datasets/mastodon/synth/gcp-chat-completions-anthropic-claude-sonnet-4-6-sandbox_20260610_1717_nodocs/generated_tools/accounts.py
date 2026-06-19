"""
Mastodon API — Accounts domain tools.
Covers: verify credentials, get account, follow, unfollow,
        followers, following, statuses by account, relationships, mute, block.
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
# Get authenticated account (verify credentials)
# ---------------------------------------------------------------------------
def get_authenticated_account() -> dict:
    """
    Return the account of the currently authenticated user.

    Returns:
        The CredentialAccount object or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/accounts/verify_credentials")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get account by ID
# ---------------------------------------------------------------------------
def get_account(account_id: str) -> dict:
    """
    Fetch a public account by its ID.

    Args:
        account_id: The ID of the account.

    Returns:
        The Account object or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/accounts/{account_id}")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Follow an account
# ---------------------------------------------------------------------------
def follow_account(account_id: str, reblogs: bool = True, notify: bool = False) -> dict:
    """
    Follow an account.

    Args:
        account_id: The ID of the account to follow.
        reblogs: Whether to show boosts from this account in the home timeline.
        notify: Whether to receive notifications when this account posts.

    Returns:
        A Relationship object or an error dict.
    """
    try:
        r = _session().post(
            f"{_base()}/accounts/{account_id}/follow",
            json={"reblogs": reblogs, "notify": notify},
        )
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Unfollow an account
# ---------------------------------------------------------------------------
def unfollow_account(account_id: str) -> dict:
    """
    Unfollow an account.

    Args:
        account_id: The ID of the account to unfollow.

    Returns:
        A Relationship object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/accounts/{account_id}/unfollow")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get followers of an account
# ---------------------------------------------------------------------------
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
        A list of Account objects or an error dict.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        r = _session().get(f"{_base()}/accounts/{account_id}/followers", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get accounts followed by an account
# ---------------------------------------------------------------------------
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
        A list of Account objects or an error dict.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        r = _session().get(f"{_base()}/accounts/{account_id}/following", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get statuses posted by an account
# ---------------------------------------------------------------------------
def get_account_statuses(
    account_id: str,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
    only_media: bool = False,
    exclude_replies: bool = False,
    exclude_reblogs: bool = False,
    pinned: bool = False,
    tagged: str = None,
) -> list:
    """
    List statuses posted by the given account.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
        only_media: Only return statuses with media attachments.
        exclude_replies: Skip statuses that are replies.
        exclude_reblogs: Skip statuses that are boosts.
        pinned: Only return pinned statuses.
        tagged: Only return statuses with this hashtag.

    Returns:
        A list of Status objects or an error dict.
    """
    params: dict = {
        "limit": limit,
        "only_media": only_media,
        "exclude_replies": exclude_replies,
        "exclude_reblogs": exclude_reblogs,
        "pinned": pinned,
    }
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    if min_id:
        params["min_id"] = min_id
    if tagged:
        params["tagged"] = tagged
    try:
        r = _session().get(f"{_base()}/accounts/{account_id}/statuses", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get relationships with accounts
# ---------------------------------------------------------------------------
def get_relationships(account_ids: list) -> list:
    """
    Return relationship info between the authenticated account and the given accounts.

    Args:
        account_ids: A list of account IDs to check.

    Returns:
        A list of Relationship objects or an error dict.
    """
    try:
        params = [("id[]", aid) for aid in account_ids]
        r = _session().get(f"{_base()}/accounts/relationships", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Mute an account
# ---------------------------------------------------------------------------
def mute_account(account_id: str, notifications: bool = True, duration: int = 0) -> dict:
    """
    Mute an account.

    Args:
        account_id: The ID of the account to mute.
        notifications: Whether to mute notifications from this account.
        duration: Duration of the mute in seconds (0 = indefinite).

    Returns:
        A Relationship object or an error dict.
    """
    try:
        r = _session().post(
            f"{_base()}/accounts/{account_id}/mute",
            json={"notifications": notifications, "duration": duration},
        )
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Unmute an account
# ---------------------------------------------------------------------------
def unmute_account(account_id: str) -> dict:
    """
    Unmute an account.

    Args:
        account_id: The ID of the account to unmute.

    Returns:
        A Relationship object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/accounts/{account_id}/unmute")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Block an account
# ---------------------------------------------------------------------------
def block_account(account_id: str) -> dict:
    """
    Block an account.

    Args:
        account_id: The ID of the account to block.

    Returns:
        A Relationship object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/accounts/{account_id}/block")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Unblock an account
# ---------------------------------------------------------------------------
def unblock_account(account_id: str) -> dict:
    """
    Unblock an account.

    Args:
        account_id: The ID of the account to unblock.

    Returns:
        A Relationship object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/accounts/{account_id}/unblock")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Update credentials
# ---------------------------------------------------------------------------
def update_credentials(
    display_name: str = None,
    note: str = None,
    avatar: str = None,
    header: str = None,
    locked: bool = None,
    bot: bool = None,
    discoverable: bool = None,
) -> dict:
    """
    Update the authenticated account's profile.

    Args:
        display_name: New display name.
        note: New bio / profile note.
        avatar: Base64-encoded avatar image (data URI).
        header: Base64-encoded header image (data URI).
        locked: Whether the account requires follow approval.
        bot: Whether the account is a bot.
        discoverable: Whether the account is listed in the directory.

    Returns:
        The updated CredentialAccount object or an error dict.
    """
    payload: dict = {}
    if display_name is not None:
        payload["display_name"] = display_name
    if note is not None:
        payload["note"] = note
    if avatar is not None:
        payload["avatar"] = avatar
    if header is not None:
        payload["header"] = header
    if locked is not None:
        payload["locked"] = locked
    if bot is not None:
        payload["bot"] = bot
    if discoverable is not None:
        payload["discoverable"] = discoverable
    try:
        r = _session().patch(f"{_base()}/accounts/update_credentials", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}
