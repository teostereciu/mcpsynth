"""
Mastodon API — Media domain tools.
Covers: upload media attachment, get/update media attachment.
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
# Upload a media attachment
# ---------------------------------------------------------------------------
def upload_media(
    file_path: str,
    description: str = None,
    focus_x: float = None,
    focus_y: float = None,
) -> dict:
    """
    Upload a media file and return a media attachment object.
    The returned 'id' can be passed to post_status() as part of media_ids.

    Args:
        file_path: Local filesystem path to the file to upload.
        description: Plain-text description (alt text) for the media.
        focus_x: Horizontal focal point (-1.0 to 1.0).
        focus_y: Vertical focal point (-1.0 to 1.0).

    Returns:
        A MediaAttachment object or an error dict.
    """
    try:
        with open(file_path, "rb") as fh:
            mime_guess = _guess_mime(file_path)
            files = {"file": (os.path.basename(file_path), fh, mime_guess)}
            data: dict = {}
            if description:
                data["description"] = description
            if focus_x is not None and focus_y is not None:
                data["focus"] = f"{focus_x},{focus_y}"
            r = _session().post(f"{_base()}/media", files=files, data=data)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


def _guess_mime(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    mapping = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".mp4": "video/mp4",
        ".mov": "video/quicktime",
        ".webm": "video/webm",
        ".mp3": "audio/mpeg",
        ".ogg": "audio/ogg",
        ".wav": "audio/wav",
    }
    return mapping.get(ext, "application/octet-stream")


# ---------------------------------------------------------------------------
# Get a media attachment
# ---------------------------------------------------------------------------
def get_media(media_id: str) -> dict:
    """
    Fetch a media attachment by its ID (useful for checking async processing status).

    Args:
        media_id: The ID of the media attachment.

    Returns:
        A MediaAttachment object or an error dict.
    """
    try:
        r = _session().get(f"{_base()}/media/{media_id}")
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Update a media attachment
# ---------------------------------------------------------------------------
def update_media(
    media_id: str,
    description: str = None,
    focus_x: float = None,
    focus_y: float = None,
) -> dict:
    """
    Update the description or focal point of an existing media attachment.

    Args:
        media_id: The ID of the media attachment to update.
        description: New plain-text description (alt text).
        focus_x: New horizontal focal point (-1.0 to 1.0).
        focus_y: New vertical focal point (-1.0 to 1.0).

    Returns:
        The updated MediaAttachment object or an error dict.
    """
    payload: dict = {}
    if description is not None:
        payload["description"] = description
    if focus_x is not None and focus_y is not None:
        payload["focus"] = f"{focus_x},{focus_y}"
    try:
        r = _session().put(f"{_base()}/media/{media_id}", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        return {"error": str(exc)}
