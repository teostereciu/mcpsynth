"""Mastodon API — Media Attachments domain tools."""

import os
import requests

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/") + "/api/v1"
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def upload_media(
    file_path: str,
    description: str = None,
    focus: str = None,
) -> dict:
    """Upload a media file (image, video, audio, or gifv) to use in a status.

    Args:
        file_path: Local path to the media file to upload.
        description: Plain-text description of the media for accessibility (alt text).
        focus: Two floating points (x,y) between -1.0 and 1.0 for the focal point, e.g. '0.5,0.3'.
    """
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            r = requests.post(
                f"{BASE_URL}/media",
                headers=_headers(),
                files=files,
                data=data,
            )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_media(media_id: str) -> dict:
    """Get information about a media attachment.

    Args:
        media_id: The ID of the media attachment.
    """
    try:
        r = requests.get(f"{BASE_URL}/media/{media_id}", headers=_headers())
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def update_media(media_id: str, description: str = None, focus: str = None) -> dict:
    """Update the description or focal point of a media attachment.

    Args:
        media_id: The ID of the media attachment to update.
        description: New plain-text description (alt text) for the media.
        focus: New focal point as 'x,y' floats between -1.0 and 1.0.
    """
    payload = {}
    if description is not None:
        payload["description"] = description
    if focus is not None:
        payload["focus"] = focus
    try:
        r = requests.put(f"{BASE_URL}/media/{media_id}", headers=_headers(), json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}
