"""Mastodon API — Statuses domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def post_status(
    status: str,
    in_reply_to_id: str = None,
    media_ids: list = None,
    sensitive: bool = False,
    spoiler_text: str = None,
    visibility: str = "public",
    language: str = None,
) -> dict:
    """Post a new status (toot) to Mastodon.

    Args:
        status: The text content of the status.
        in_reply_to_id: ID of the status being replied to.
        media_ids: List of media attachment IDs to attach.
        sensitive: Mark status and attached media as sensitive.
        spoiler_text: Text to be shown as a warning before the actual content.
        visibility: Visibility of the post — public, unlisted, private, or direct.
        language: ISO 639 language code for the status.
    """
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
        r = requests.post(f"{BASE_URL}/statuses", headers=_headers(), json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_status(status_id: str) -> dict:
    """Fetch a single status by its ID.

    Args:
        status_id: The ID of the status to retrieve.
    """
    try:
        r = requests.get(f"{BASE_URL}/statuses/{status_id}", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def delete_status(status_id: str) -> dict:
    """Delete a status posted by the authenticated account.

    Args:
        status_id: The ID of the status to delete.
    """
    try:
        r = requests.delete(f"{BASE_URL}/statuses/{status_id}", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def boost_status(status_id: str) -> dict:
    """Reblog (boost) a status.

    Args:
        status_id: The ID of the status to boost.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/reblog", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unboost_status(status_id: str) -> dict:
    """Undo a reblog (boost) of a status.

    Args:
        status_id: The ID of the status to unboost.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/unreblog", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def favourite_status(status_id: str) -> dict:
    """Favourite (like) a status.

    Args:
        status_id: The ID of the status to favourite.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/favourite", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unfavourite_status(status_id: str) -> dict:
    """Remove a favourite from a status.

    Args:
        status_id: The ID of the status to unfavourite.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/unfavourite", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_status_context(status_id: str) -> dict:
    """Get the thread context (ancestors and descendants) of a status.

    Args:
        status_id: The ID of the status whose context to retrieve.
    """
    try:
        r = requests.get(f"{BASE_URL}/statuses/{status_id}/context", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_status_reblogged_by(status_id: str) -> list:
    """Get the list of accounts that reblogged a status.

    Args:
        status_id: The ID of the status.
    """
    try:
        r = requests.get(f"{BASE_URL}/statuses/{status_id}/reblogged_by", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_status_favourited_by(status_id: str) -> list:
    """Get the list of accounts that favourited a status.

    Args:
        status_id: The ID of the status.
    """
    try:
        r = requests.get(f"{BASE_URL}/statuses/{status_id}/favourited_by", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def bookmark_status(status_id: str) -> dict:
    """Bookmark a status.

    Args:
        status_id: The ID of the status to bookmark.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/bookmark", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unbookmark_status(status_id: str) -> dict:
    """Remove a bookmark from a status.

    Args:
        status_id: The ID of the status to unbookmark.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/unbookmark", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def pin_status(status_id: str) -> dict:
    """Pin a status to the authenticated account's profile.

    Args:
        status_id: The ID of the status to pin.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/pin", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def unpin_status(status_id: str) -> dict:
    """Unpin a status from the authenticated account's profile.

    Args:
        status_id: The ID of the status to unpin.
    """
    try:
        r = requests.post(f"{BASE_URL}/statuses/{status_id}/unpin", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
