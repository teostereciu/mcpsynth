"""
eBay Commerce Media API tools.
Uses user-token (refresh_token grant).
Base: https://apim.sandbox.ebay.com/commerce/media/v1  (different subdomain)
"""

from typing import Optional
import requests
from .auth import MEDIA_URL, user_headers, safe_json

_BASE = f"{MEDIA_URL}/commerce/media/v1"


# ── Video ─────────────────────────────────────────────────────────────────────

def create_video(
    title: str,
    size: int,
    classification: Optional[list] = None,
    description: Optional[str] = None,
) -> dict:
    """
    Create a video resource on eBay (first step before uploading the video file).

    Args:
        title: Title of the video (max 80 characters).
        size: Size of the video file in bytes.
        classification: List of classification strings (e.g. ['ITEM_DESCRIPTION']).
        description: Optional description of the video.
    """
    url = f"{_BASE}/video"
    body: dict = {"title": title, "size": size}
    if classification:
        body["classification"] = classification
    if description:
        body["description"] = description
    resp = requests.post(url, headers=user_headers(), json=body, timeout=15)
    return safe_json(resp)


def upload_video(video_id: str, video_data: bytes, content_type: str = "video/mp4") -> dict:
    """
    Upload the binary content of a video to eBay after creating the video resource.

    Args:
        video_id: The video ID returned by create_video.
        video_data: Raw bytes of the video file.
        content_type: MIME type of the video (default 'video/mp4').
    """
    url = f"{_BASE}/video/{video_id}/upload"
    headers = user_headers()
    headers["Content-Type"] = content_type
    resp = requests.post(url, headers=headers, data=video_data, timeout=120)
    return safe_json(resp)


def get_video(video_id: str) -> dict:
    """
    Retrieve metadata and status for a video resource.

    Args:
        video_id: The eBay video ID.
    """
    url = f"{_BASE}/video/{video_id}"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


# ── Image ─────────────────────────────────────────────────────────────────────

def create_image(
    image_data: bytes,
    content_type: str = "image/jpeg",
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Upload an image to the eBay media service.

    Args:
        image_data: Raw bytes of the image file.
        content_type: MIME type of the image (e.g. 'image/jpeg', 'image/png').
        marketplace_id: eBay marketplace ID (default 'EBAY_US').
    """
    url = f"{_BASE}/image"
    headers = user_headers()
    headers["Content-Type"] = content_type
    headers["marketplace_id"] = marketplace_id
    resp = requests.post(url, headers=headers, data=image_data, timeout=30)
    return safe_json(resp)


# ── Document ──────────────────────────────────────────────────────────────────

def create_document(
    document_type: str,
    files: list,
) -> dict:
    """
    Create a document resource (e.g. a regulatory document) on eBay.

    Args:
        document_type: Type of document (e.g. 'USER_GUIDE', 'SAFETY_DATA_SHEET').
        files: List of file metadata dicts, each with 'fileName' and 'fileType'.
    """
    url = f"{_BASE}/document"
    body = {"documentType": document_type, "files": files}
    resp = requests.post(url, headers=user_headers(), json=body, timeout=15)
    return safe_json(resp)


def upload_document_file(document_id: str, file_name: str, file_data: bytes, content_type: str = "application/pdf") -> dict:
    """
    Upload the binary content of a document file to eBay.

    Args:
        document_id: The document ID returned by create_document.
        file_name: The file name as declared in create_document.
        file_data: Raw bytes of the document file.
        content_type: MIME type of the document (default 'application/pdf').
    """
    url = f"{_BASE}/document/{document_id}/upload"
    headers = user_headers()
    headers["Content-Type"] = content_type
    headers["file_name"] = file_name
    resp = requests.post(url, headers=headers, data=file_data, timeout=60)
    return safe_json(resp)


def get_document(document_id: str) -> dict:
    """
    Retrieve metadata and status for a document resource.

    Args:
        document_id: The eBay document ID.
    """
    url = f"{_BASE}/document/{document_id}"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)
