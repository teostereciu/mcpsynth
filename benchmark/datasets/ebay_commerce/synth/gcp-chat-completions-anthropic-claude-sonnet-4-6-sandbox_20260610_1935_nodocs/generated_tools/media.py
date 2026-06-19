"""
eBay Commerce Media API tools.
Base path: /commerce/media/v1_beta  (uses apim.* subdomain)
Auth: user token (refresh_token)
"""

from .auth import user_get, user_post, user_delete

_BASE = "/commerce/media/v1_beta"


# ---------------------------------------------------------------------------
# Video
# ---------------------------------------------------------------------------

def create_video(
    title: str,
    size: int,
    classification: list[str] | None = None,
    description: str | None = None,
) -> dict:
    """
    Create a new video resource on eBay (first step before uploading).

    Args:
        title: Title of the video (max 80 chars).
        size: File size in bytes of the video to be uploaded.
        classification: List of classification strings, e.g. ["ITEM_DESCRIPTION"].
        description: Optional description of the video.

    Returns:
        Dict with videoId and upload URL/instructions.
    """
    body: dict = {"title": title, "size": size}
    if classification:
        body["classification"] = classification
    if description:
        body["description"] = description
    return user_post(f"{_BASE}/video", json_body=body, media=True)


def get_video(video_id: str) -> dict:
    """
    Retrieve metadata and status for a video by its ID.

    Args:
        video_id: The eBay video ID returned from create_video.

    Returns:
        Dict with videoId, title, status, playList (streaming URLs), thumbnail, etc.
    """
    return user_get(f"{_BASE}/video/{video_id}", media=True)


def get_videos(
    q: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    List videos owned by the authenticated user.

    Args:
        q: Optional keyword filter on video title.
        limit: Number of results (max 100).
        offset: Pagination offset.

    Returns:
        Dict with videos list and pagination info.
    """
    params: dict = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    return user_get(f"{_BASE}/video", params=params, media=True)


def delete_video(video_id: str) -> dict:
    """
    Delete a video resource.

    Args:
        video_id: The eBay video ID to delete.

    Returns:
        Dict confirming deletion or error details.
    """
    return user_delete(f"{_BASE}/video/{video_id}", media=True)


# ---------------------------------------------------------------------------
# Image
# ---------------------------------------------------------------------------

def create_image(
    image_url: str,
    image_type: str = "JPEG",
) -> dict:
    """
    Upload an image to eBay by providing a publicly accessible URL.

    Args:
        image_url: Publicly accessible URL of the image to upload.
        image_type: Image format — JPEG, PNG, GIF, TIFF, BMP, WEBP (default JPEG).

    Returns:
        Dict with imageId and status.
    """
    body = {"imageUrl": image_url, "imageType": image_type}
    return user_post(f"{_BASE}/image", json_body=body, media=True)


def get_image(image_id: str) -> dict:
    """
    Retrieve metadata for an uploaded image.

    Args:
        image_id: The eBay image ID.

    Returns:
        Dict with imageId, imageUrl, status, etc.
    """
    return user_get(f"{_BASE}/image/{image_id}", media=True)


# ---------------------------------------------------------------------------
# Document
# ---------------------------------------------------------------------------

def create_document(
    document_type: str,
    languages: list[str],
    files: list[dict] | None = None,
) -> dict:
    """
    Create a document resource (e.g. regulatory compliance document).

    Args:
        document_type: Type of document, e.g. "REGULATORY_DOCUMENT".
        languages: List of language codes, e.g. ["en_US"].
        files: Optional list of file metadata dicts with keys: fileName, fileType, fileSize.

    Returns:
        Dict with documentId and upload instructions.
    """
    body: dict = {"documentType": document_type, "languages": languages}
    if files:
        body["files"] = files
    return user_post(f"{_BASE}/document", json_body=body, media=True)


def get_document(document_id: str) -> dict:
    """
    Retrieve metadata for a document resource.

    Args:
        document_id: The eBay document ID.

    Returns:
        Dict with documentId, documentType, status, files, etc.
    """
    return user_get(f"{_BASE}/document/{document_id}", media=True)
