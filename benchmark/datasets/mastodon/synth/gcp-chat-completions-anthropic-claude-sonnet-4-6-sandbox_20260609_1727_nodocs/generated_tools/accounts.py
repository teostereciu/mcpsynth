"""Mastodon API — Accounts domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_authenticated_account() -> dict:
    """Return the account information for the currently authenticated user."""
    try:
        r = requests.get(f"{BASE_URL}/accounts/verify_credentials", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_account(account_id: str) -> dict:
    """Fetch a Mastodon account by its ID.

    Args:
        account_id: The ID of the account to retrieve.
    """
    try:
        r = requests.get(f"{BASE_URL}/accounts/{account_id}", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def lookup_account(acct: str) -> dict:
    """Look up an account by its username (and optional domain).

    Args:
        acct: The username (e.g. 'user' or 'user@example.com') to look up.
    """
    try:
        r = requests.get(f"{BASE_URL}/accounts/lookup", headers=_headers(), params={"acct": acct})
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def follow_account(account_id: str, reblogs: bool = True, notify: bool = False) -> dict:
    """Follow an account.

    Args:
        account_id: The ID of the account to follow.
        reblogs: Whether to show reblogs from this account in the home timeline.
        notify: Whether to receive notifications when this account posts.
    """
    try:
        payload = {"reblogs": reblogs, "notify": notify}
        r = requests.post(
            f"{BASE_URL}/accounts/{account_id}/follow", headers=_headers(), json=payload
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unfollow_account(account_id: str) -> dict:
    """Unfollow an account.

    Args:
        account_id: The ID of the account to unfollow.
    """
    try:
        r = requests.post(f"{BASE_URL}/accounts/{account_id}/unfollow", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_account_followers(account_id: str, limit: int = 40, max_id: str = None, since_id: str = None) -> list:
    """Get the list of followers for an account.

    Args:
        account_id: The ID of the account.
        limit: Maximum number of results (default 40, max 80).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        r = requests.get(
            f"{BASE_URL}/accounts/{account_id}/followers", headers=_headers(), params=params
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_account_following(account_id: str, limit: int = 40, max_id: str = None, since_id: str = None) -> list:
    """Get the list of accounts that an account is following.

    Args:
        account_id: The ID of the account.
        limit: Maximum number of results (default 40, max 80).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
    """
    params = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        r = requests.get(
            f"{BASE_URL}/accounts/{account_id}/following", headers=_headers(), params=params
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_account_statuses(
    account_id: str,
    limit: int = 20,
    max_id: str = None,
    since_id: str = None,
    exclude_replies: bool = False,
    exclude_reblogs: bool = False,
    only_media: bool = False,
    pinned: bool = False,
) -> list:
    """Get statuses posted by an account.

    Args:
        account_id: The ID of the account.
        limit: Maximum number of results (default 20, max 40).
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        exclude_replies: Skip statuses that are replies.
        exclude_reblogs: Skip statuses that are reblogs.
        only_media: Only return statuses with media attachments.
        pinned: Only return pinned statuses.
    """
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
    try:
        r = requests.get(
            f"{BASE_URL}/accounts/{account_id}/statuses", headers=_headers(), params=params
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def block_account(account_id: str) -> dict:
    """Block an account.

    Args:
        account_id: The ID of the account to block.
    """
    try:
        r = requests.post(f"{BASE_URL}/accounts/{account_id}/block", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unblock_account(account_id: str) -> dict:
    """Unblock an account.

    Args:
        account_id: The ID of the account to unblock.
    """
    try:
        r = requests.post(f"{BASE_URL}/accounts/{account_id}/unblock", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def mute_account(account_id: str, notifications: bool = True, duration: int = 0) -> dict:
    """Mute an account.

    Args:
        account_id: The ID of the account to mute.
        notifications: Whether to mute notifications from this account.
        duration: Duration of the mute in seconds (0 = indefinite).
    """
    try:
        payload = {"notifications": notifications, "duration": duration}
        r = requests.post(
            f"{BASE_URL}/accounts/{account_id}/mute", headers=_headers(), json=payload
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unmute_account(account_id: str) -> dict:
    """Unmute an account.

    Args:
        account_id: The ID of the account to unmute.
    """
    try:
        r = requests.post(f"{BASE_URL}/accounts/{account_id}/unmute", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_relationships(account_ids: list) -> list:
    """Get relationship information between the authenticated account and a list of accounts.

    Args:
        account_ids: List of account IDs to check relationships for.
    """
    try:
        params = [("id[]", aid) for aid in account_ids]
        r = requests.get(f"{BASE_URL}/accounts/relationships", headers=_headers(), params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def update_credentials(
    display_name: str = None,
    note: str = None,
    avatar: str = None,
    header: str = None,
    locked: bool = None,
    bot: bool = None,
    discoverable: bool = None,
) -> dict:
    """Update the authenticated account's profile information.

    Args:
        display_name: The display name to use for the profile.
        note: The account bio / profile note.
        avatar: Path to a local image file to use as avatar.
        header: Path to a local image file to use as header.
        locked: Whether the account requires follow requests.
        bot: Whether the account is a bot.
        discoverable: Whether the account should appear in the profile directory.
    """
    try:
        data = {}
        files = {}
        if display_name is not None:
            data["display_name"] = display_name
        if note is not None:
            data["note"] = note
        if locked is not None:
            data["locked"] = str(locked).lower()
        if bot is not None:
            data["bot"] = str(bot).lower()
        if discoverable is not None:
            data["discoverable"] = str(discoverable).lower()
        if avatar:
            files["avatar"] = open(avatar, "rb")
        if header:
            files["header"] = open(header, "rb")
        r = requests.patch(
            f"{BASE_URL}/accounts/update_credentials",
            headers=_headers(),
            data=data,
            files=files if files else None,
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
