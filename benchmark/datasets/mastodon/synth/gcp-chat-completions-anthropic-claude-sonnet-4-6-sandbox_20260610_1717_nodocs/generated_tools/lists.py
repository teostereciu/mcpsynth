"""
Mastodon API — Lists domain tools.
Covers: create, read, update, delete lists; add/remove accounts from lists;
        get accounts in a list.
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
# List all lists
# ---------------------------------------------------------------------------
def get_lists() -> list:
    """
    Return all lists owned by the authenticated account.

    Returns:
        A list of List objects or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/lists")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get a single list
# ---------------------------------------------------------------------------
def get_list(list_id: str) -> dict:
    """
    Fetch a single list by its ID.

    Args:
        list_id: The ID of the list.

    Returns:
        A List object or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/lists/{list_id}")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Create a list
# ---------------------------------------------------------------------------
def create_list(
    title: str,
    replies_policy: str = "list",
    exclusive: bool = False,
) -> dict:
    """
    Create a new list.

    Args:
        title: The title of the list.
        replies_policy: How replies are handled: 'followed', 'list', or 'none'.
        exclusive: Whether members' posts are removed from the home timeline.

    Returns:
        The created List object or an error dict.
    """
    try:
        r = _session().post(
            f"{_base()}/lists",
            json={
                "title": title,
                "replies_policy": replies_policy,
                "exclusive": exclusive,
            },
        )
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Update a list
# ---------------------------------------------------------------------------
def update_list(
    list_id: str,
    title: str = None,
    replies_policy: str = None,
    exclusive: bool = None,
) -> dict:
    """
    Update an existing list.

    Args:
        list_id: The ID of the list to update.
        title: New title for the list.
        replies_policy: New replies policy: 'followed', 'list', or 'none'.
        exclusive: Whether members' posts are removed from the home timeline.

    Returns:
        The updated List object or an error dict.
    """
    payload: dict = {}
    if title is not None:
        payload["title"] = title
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    try:
        r = _session().put(f"{_base()}/lists/{list_id}", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Delete a list
# ---------------------------------------------------------------------------
def delete_list(list_id: str) -> dict:
    """
    Delete a list.

    Args:
        list_id: The ID of the list to delete.

    Returns:
        An empty dict on success, or an error dict.
    """
    try:
        r = _session().delete(f"{_base()}/lists/{list_id}")
        r.raise_for_status()
        return {} if not r.text.strip() else r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get accounts in a list
# ---------------------------------------------------------------------------
def get_list_accounts(
    list_id: str,
    max_id: str = None,
    since_id: str = None,
    limit: int = 40,
) -> list:
    """
    Return accounts that are members of the given list.

    Args:
        list_id: The ID of the list.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        limit: Maximum number of results (default 40, max 80).

    Returns:
        A list of Account objects or an error dict.
    """
    params: dict = {"limit": limit}
    if max_id:
        params["max_id"] = max_id
    if since_id:
        params["since_id"] = since_id
    try:
        r = _session().get(f"{_base()}/lists/{list_id}/accounts", params=params)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Add accounts to a list
# ---------------------------------------------------------------------------
def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
    """
    Add one or more accounts to a list.

    Args:
        list_id: The ID of the list.
        account_ids: A list of account IDs to add.

    Returns:
        An empty dict on success, or an error dict.
    """
    try:
        r = _session().post(
            f"{_base()}/lists/{list_id}/accounts",
            json={"account_ids": account_ids},
        )
        r.raise_for_status()
        return {} if not r.text.strip() else r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Remove accounts from a list
# ---------------------------------------------------------------------------
def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
    """
    Remove one or more accounts from a list.

    Args:
        list_id: The ID of the list.
        account_ids: A list of account IDs to remove.

    Returns:
        An empty dict on success, or an error dict.
    """
    try:
        r = _session().delete(
            f"{_base()}/lists/{list_id}/accounts",
            json={"account_ids": account_ids},
        )
        r.raise_for_status()
        return {} if not r.text.strip() else r.json()
    except Exception as exc:
        return {"error": str(exc)}
