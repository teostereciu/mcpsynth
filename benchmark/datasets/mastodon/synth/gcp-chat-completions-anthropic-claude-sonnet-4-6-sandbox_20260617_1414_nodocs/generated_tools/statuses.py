"""
Mastodon API — Statuses domain tools.
Covers: post, get, delete, boost, unboost, favourite, unfavourite, context.
"""

import requests
from config import BASE_URL, HEADERS


def post_status(
    status: str,
    in_reply_to_id: str = None,
    media_ids: list = None,
    sensitive: bool = False,
    spoiler_text: str = None,
    visibility: str = "public",
    language: str = None,
) -> dict:
    """
    Publish a new status (post/toot).

    Args:
        status: The text content of the status.
        in_reply_to_id: ID of the status being replied to.
        media_ids: List of media attachment IDs to attach (up to 4).
        sensitive: Mark status and attached media as sensitive.
        spoiler_text: Text to be shown as a warning before the actual content.
        visibility: Visibility of the post — 'public', 'unlisted', 'private', or 'direct'.
        language: ISO 639-1 language code for the status.

    Returns:
        The newly created status object as a dict, or an error dict.
    """
    url = f"{BASE_URL}/statuses"
    payload = {"status": status, "sensitive": sensitive, "visibility": visibility}
    if in_reply_to_id:
        payload["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        payload["media_ids[]"] = media_ids
    if spoiler_text:
        payload["spoiler_text"] = spoiler_text
    if language:
        payload["language"] = language
    try:
        resp = requests.post(url, headers=HEADERS, data=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_status(status_id: str) -> dict:
    """
    Retrieve a single status by its ID.

    Args:
        status_id: The ID of the status.

    Returns:
        The status object as a dict, or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def delete_status(status_id: str) -> dict:
    """
    Delete a status that belongs to the authenticated account.

    Args:
        status_id: The ID of the status to delete.

    Returns:
        The deleted status object (with source text) or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}"
    try:
        resp = requests.delete(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def boost_status(status_id: str, visibility: str = "public") -> dict:
    """
    Reblog (boost) a status.

    Args:
        status_id: The ID of the status to boost.
        visibility: Visibility of the reblog — 'public', 'unlisted', or 'private'.

    Returns:
        The reblog status object or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/reblog"
    try:
        resp = requests.post(url, headers=HEADERS, json={"visibility": visibility})
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def unboost_status(status_id: str) -> dict:
    """
    Undo a reblog (boost) of a status.

    Args:
        status_id: The ID of the status to unboost.

    Returns:
        The original status object or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/unreblog"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def favourite_status(status_id: str) -> dict:
    """
    Favourite (like) a status.

    Args:
        status_id: The ID of the status to favourite.

    Returns:
        The status object with updated favourites_count, or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/favourite"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def unfavourite_status(status_id: str) -> dict:
    """
    Remove a favourite (like) from a status.

    Args:
        status_id: The ID of the status to unfavourite.

    Returns:
        The status object or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/unfavourite"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_status_context(status_id: str) -> dict:
    """
    Retrieve the thread/context of a status (ancestors and descendants).

    Args:
        status_id: The ID of the status.

    Returns:
        A dict with 'ancestors' and 'descendants' lists of status objects, or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/context"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_status_reblogged_by(status_id: str) -> list:
    """
    List accounts that have reblogged a status.

    Args:
        status_id: The ID of the status.

    Returns:
        A list of account objects, or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/reblogged_by"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_status_favourited_by(status_id: str) -> list:
    """
    List accounts that have favourited a status.

    Args:
        status_id: The ID of the status.

    Returns:
        A list of account objects, or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/favourited_by"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def bookmark_status(status_id: str) -> dict:
    """
    Bookmark a status.

    Args:
        status_id: The ID of the status to bookmark.

    Returns:
        The status object or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/bookmark"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def unbookmark_status(status_id: str) -> dict:
    """
    Remove a bookmark from a status.

    Args:
        status_id: The ID of the status to unbookmark.

    Returns:
        The status object or an error dict.
    """
    url = f"{BASE_URL}/statuses/{status_id}/unbookmark"
    try:
        resp = requests.post(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}
