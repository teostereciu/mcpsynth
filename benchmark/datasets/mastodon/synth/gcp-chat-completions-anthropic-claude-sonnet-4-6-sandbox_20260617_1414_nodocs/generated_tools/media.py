"""
Mastodon API — Media domain tools.
Covers: upload media attachment, get media attachment, update media attachment.
"""

import requests
from config import BASE_URL, HEADERS


def upload_media(
    file_path: str,
    description: str = None,
    focus: str = None,
) -> dict:
    """
    Upload a media file to be attached to a future status.

    Args:
        file_path: Local filesystem path to the media file to upload.
        description: Plain-text description (alt text) for the media, for accessibility.
        focus: Two floating-point values (x,y) between -1.0 and 1.0, e.g. '0.5,-0.3'.

    Returns:
        A MediaAttachment object (including the media ID), or an error dict.
    """
    url = f"{BASE_URL}/media"
    # Build headers without Content-Type so requests sets multipart boundary
    upload_headers = {k: v for k, v in HEADERS.items() if k.lower() != "content-type"}
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
            resp = requests.post(url, headers=upload_headers, files=files, data=data)
        resp.raise_for_status()
        return resp.json()
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except requests.RequestException as e:
        return {"error": str(e)}


def get_media(media_id: str) -> dict:
    """
    Retrieve a media attachment by its ID (useful for checking async processing status).

    Args:
        media_id: The ID of the media attachment.

    Returns:
        A MediaAttachment object, or an error dict.
    """
    url = f"{BASE_URL}/media/{media_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def update_media(
    media_id: str,
    description: str = None,
    focus: str = None,
) -> dict:
    """
    Update the description or focus of an existing media attachment.

    Args:
        media_id: The ID of the media attachment to update.
        description: New plain-text description (alt text) for the media.
        focus: New focus point as 'x,y' floats between -1.0 and 1.0.

    Returns:
        The updated MediaAttachment object, or an error dict.
    """
    url = f"{BASE_URL}/media/{media_id}"
    payload = {}
    if description is not None:
        payload["description"] = description
    if focus is not None:
        payload["focus"] = focus
    try:
        resp = requests.put(url, headers=HEADERS, json=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}
