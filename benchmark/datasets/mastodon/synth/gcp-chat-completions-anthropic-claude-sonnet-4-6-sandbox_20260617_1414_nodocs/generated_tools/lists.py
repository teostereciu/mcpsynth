"""
Mastodon API — Lists domain tools.
Covers: create, read, update, delete lists; add/remove accounts from lists;
        get accounts in a list.
"""

import requests
from config import BASE_URL, HEADERS


def get_lists() -> list:
    """
    Retrieve all lists created by the authenticated account.

    Returns:
        A list of List objects, or an error dict.
    """
    url = f"{BASE_URL}/lists"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_list(list_id: str) -> dict:
    """
    Retrieve a single list by its ID.

    Args:
        list_id: The ID of the list.

    Returns:
        A List object, or an error dict.
    """
    url = f"{BASE_URL}/lists/{list_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def create_list(title: str, replies_policy: str = "list", exclusive: bool = False) -> dict:
    """
    Create a new list.

    Args:
        title: The title of the list.
        replies_policy: Replies to show in the list — 'followed', 'list', or 'none'.
        exclusive: Whether members of this list will be removed from the home timeline.

    Returns:
        The newly created List object, or an error dict.
    """
    url = f"{BASE_URL}/lists"
    payload = {
        "title": title,
        "replies_policy": replies_policy,
        "exclusive": exclusive,
    }
    try:
        resp = requests.post(url, headers=HEADERS, json=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


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
        replies_policy: New replies policy — 'followed', 'list', or 'none'.
        exclusive: Whether members of this list will be removed from the home timeline.

    Returns:
        The updated List object, or an error dict.
    """
    url = f"{BASE_URL}/lists/{list_id}"
    payload = {}
    if title is not None:
        payload["title"] = title
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    try:
        resp = requests.put(url, headers=HEADERS, json=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def delete_list(list_id: str) -> dict:
    """
    Delete a list.

    Args:
        list_id: The ID of the list to delete.

    Returns:
        An empty dict on success, or an error dict.
    """
    url = f"{BASE_URL}/lists/{list_id}"
    try:
        resp = requests.delete(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json() if resp.text.strip() else {}
    except requests.RequestException as e:
        return {"error": str(e)}


def get_list_accounts(
    list_id: str,
    max_id: str = None,
    since_id: str = None,
    limit: int = 40,
) -> list:
    """
    Retrieve accounts that are members of a list.

    Args:
        list_id: The ID of the list.
        max_id: Return results older than this account ID.
        since_id: Return results newer than this account ID.
        limit: Maximum number of results (default 40, max 80).

    Returns:
        A list of Account objects, or an error dict.
    """
    url = f"{BASE_URL}/lists/{list_id}/accounts"
    params: dict = {"limit": limit}
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


def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
    """
    Add one or more accounts to a list.

    Args:
        list_id: The ID of the list.
        account_ids: List of account IDs to add.

    Returns:
        An empty dict on success, or an error dict.
    """
    url = f"{BASE_URL}/lists/{list_id}/accounts"
    # Mastodon expects account_ids[] as repeated form params
    data = [("account_ids[]", aid) for aid in account_ids]
    try:
        resp = requests.post(url, headers=HEADERS, data=data)
        resp.raise_for_status()
        return resp.json() if resp.text.strip() else {}
    except requests.RequestException as e:
        return {"error": str(e)}


def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
    """
    Remove one or more accounts from a list.

    Args:
        list_id: The ID of the list.
        account_ids: List of account IDs to remove.

    Returns:
        An empty dict on success, or an error dict.
    """
    url = f"{BASE_URL}/lists/{list_id}/accounts"
    data = [("account_ids[]", aid) for aid in account_ids]
    try:
        resp = requests.delete(url, headers=HEADERS, data=data)
        resp.raise_for_status()
        return resp.json() if resp.text.strip() else {}
    except requests.RequestException as e:
        return {"error": str(e)}
