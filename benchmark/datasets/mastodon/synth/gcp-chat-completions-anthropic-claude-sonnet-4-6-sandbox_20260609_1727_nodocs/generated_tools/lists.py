"""Mastodon API — Lists domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def get_lists() -> list:
    """Fetch all lists created by the authenticated account."""
    try:
        r = requests.get(f"{BASE_URL}/lists", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_list(list_id: str) -> dict:
    """Fetch a single list by its ID.

    Args:
        list_id: The ID of the list to retrieve.
    """
    try:
        r = requests.get(f"{BASE_URL}/lists/{list_id}", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def create_list(title: str, replies_policy: str = "list", exclusive: bool = False) -> dict:
    """Create a new list.

    Args:
        title: The title of the list.
        replies_policy: Which replies to show in the list: 'followed', 'list', or 'none'.
        exclusive: Whether accounts in this list should be removed from the home timeline.
    """
    payload = {"title": title, "replies_policy": replies_policy, "exclusive": exclusive}
    try:
        r = requests.post(f"{BASE_URL}/lists", headers=_headers(), json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def update_list(list_id: str, title: str = None, replies_policy: str = None, exclusive: bool = None) -> dict:
    """Update an existing list.

    Args:
        list_id: The ID of the list to update.
        title: New title for the list.
        replies_policy: Which replies to show: 'followed', 'list', or 'none'.
        exclusive: Whether accounts in this list should be removed from the home timeline.
    """
    payload = {}
    if title is not None:
        payload["title"] = title
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    try:
        r = requests.put(f"{BASE_URL}/lists/{list_id}", headers=_headers(), json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def delete_list(list_id: str) -> dict:
    """Delete a list.

    Args:
        list_id: The ID of the list to delete.
    """
    try:
        r = requests.delete(f"{BASE_URL}/lists/{list_id}", headers=_headers())
        r.raise_for_status()
        return {"status": "deleted"} if not r.content else r.json()
    except Exception as e:
        return {"error": str(e)}


def get_list_accounts(list_id: str, limit: int = 40, max_id: str = None, since_id: str = None) -> list:
    """Get the accounts in a list.

    Args:
        list_id: The ID of the list.
        limit: Maximum number of accounts to return (default 40, max 80).
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
            f"{BASE_URL}/lists/{list_id}/accounts", headers=_headers(), params=params
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
    """Add accounts to a list.

    Args:
        list_id: The ID of the list.
        account_ids: List of account IDs to add to the list.
    """
    try:
        payload = {"account_ids": account_ids}
        r = requests.post(
            f"{BASE_URL}/lists/{list_id}/accounts", headers=_headers(), json=payload
        )
        r.raise_for_status()
        return r.json() if r.content else {"status": "added"}
    except Exception as e:
        return {"error": str(e)}


def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
    """Remove accounts from a list.

    Args:
        list_id: The ID of the list.
        account_ids: List of account IDs to remove from the list.
    """
    try:
        payload = {"account_ids": account_ids}
        r = requests.delete(
            f"{BASE_URL}/lists/{list_id}/accounts", headers=_headers(), json=payload
        )
        r.raise_for_status()
        return r.json() if r.content else {"status": "removed"}
    except Exception as e:
        return {"error": str(e)}
