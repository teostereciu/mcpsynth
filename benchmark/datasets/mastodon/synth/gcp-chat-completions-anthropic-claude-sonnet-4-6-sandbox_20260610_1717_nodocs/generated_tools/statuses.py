"""
Mastodon API — Statuses domain tools.
Covers: post, get, delete, boost, unboost, favourite, unfavourite, context.
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
# Post a new status
# ---------------------------------------------------------------------------
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
    Publish a new status (toot).

    Args:
        status: The text content of the status.
        in_reply_to_id: ID of the status being replied to.
        media_ids: List of media attachment IDs to attach (up to 4).
        sensitive: Mark the media as sensitive.
        spoiler_text: Content warning / subject text.
        visibility: 'public', 'unlisted', 'private', or 'direct'.
        language: ISO 639-1 language code for the status.

    Returns:
        The created status object as a dict, or an error dict.
    """
    payload = {"status": status, "visibility": visibility, "sensitive": sensitive}
    if in_reply_to_id:
        payload["in_reply_to_id"] = in_reply_to_id
    if media_ids:
        payload["media_ids[]"] = media_ids
    if spoiler_text:
        payload["spoiler_text"] = spoiler_text
    if language:
        payload["language"] = language

    try:
        r = _session().post(f"{_base()}/statuses", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get a single status
# ---------------------------------------------------------------------------
def get_status(status_id: str) -> dict:
    """
    Fetch a single status by its ID.

    Args:
        status_id: The ID of the status.

    Returns:
        The status object as a dict, or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/statuses/{status_id}")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Delete a status
# ---------------------------------------------------------------------------
def delete_status(status_id: str) -> dict:
    """
    Delete a status authored by the authenticated account.

    Args:
        status_id: The ID of the status to delete.

    Returns:
        The deleted status object (with source text) or an error dict.
    """
    try:
        r = _session().delete(f"{_base()}/statuses/{status_id}")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Boost (reblog) a status
# ---------------------------------------------------------------------------
def boost_status(status_id: str, visibility: str = "public") -> dict:
    """
    Boost (reblog) a status.

    Args:
        status_id: The ID of the status to boost.
        visibility: Visibility of the boost ('public', 'unlisted', 'private').

    Returns:
        The boost status object or an error dict.
    """
    try:
        r = _session().post(
            f"{_base()}/statuses/{status_id}/reblog",
            json={"visibility": visibility},
        )
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Unboost (unreblog) a status
# ---------------------------------------------------------------------------
def unboost_status(status_id: str) -> dict:
    """
    Undo a boost of a status.

    Args:
        status_id: The ID of the status to unboost.

    Returns:
        The original status object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/statuses/{status_id}/unreblog")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Favourite a status
# ---------------------------------------------------------------------------
def favourite_status(status_id: str) -> dict:
    """
    Favourite (like) a status.

    Args:
        status_id: The ID of the status to favourite.

    Returns:
        The status object with updated favourites_count, or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/statuses/{status_id}/favourite")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Unfavourite a status
# ---------------------------------------------------------------------------
def unfavourite_status(status_id: str) -> dict:
    """
    Remove a favourite from a status.

    Args:
        status_id: The ID of the status to unfavourite.

    Returns:
        The status object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/statuses/{status_id}/unfavourite")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get status context (thread)
# ---------------------------------------------------------------------------
def get_status_context(status_id: str) -> dict:
    """
    Retrieve the ancestors and descendants of a status (the thread).

    Args:
        status_id: The ID of the status.

    Returns:
        A dict with 'ancestors' and 'descendants' lists, or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/statuses/{status_id}/context")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get accounts that boosted a status
# ---------------------------------------------------------------------------
def get_status_reblogged_by(status_id: str) -> list:
    """
    List accounts that boosted a given status.

    Args:
        status_id: The ID of the status.

    Returns:
        A list of account objects, or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/statuses/{status_id}/reblogged_by")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get accounts that favourited a status
# ---------------------------------------------------------------------------
def get_status_favourited_by(status_id: str) -> list:
    """
    List accounts that favourited a given status.

    Args:
        status_id: The ID of the status.

    Returns:
        A list of account objects, or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/statuses/{status_id}/favourited_by")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Bookmark a status
# ---------------------------------------------------------------------------
def bookmark_status(status_id: str) -> dict:
    """
    Bookmark a status for the authenticated account.

    Args:
        status_id: The ID of the status to bookmark.

    Returns:
        The status object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/statuses/{status_id}/bookmark")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Unbookmark a status
# ---------------------------------------------------------------------------
def unbookmark_status(status_id: str) -> dict:
    """
    Remove a bookmark from a status.

    Args:
        status_id: The ID of the status to unbookmark.

    Returns:
        The status object or an error dict.
    """
    try:
        r = _session().post(f"{_base()}/statuses/{status_id}/unbookmark")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}
