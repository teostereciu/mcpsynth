"""eBay Commerce Media API tools — user-token authenticated.

Note: Media API uses a different base domain: apim.sandbox.ebay.com / apim.ebay.com
"""
from __future__ import annotations
import os
from typing import List, Optional
import requests
from .auth import get_user_token

SANDBOX = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper() == "SANDBOX"
# Media API uses apim.* subdomain
BASE = "https://apim.sandbox.ebay.com" if SANDBOX else "https://apim.ebay.com"
# Document endpoints use api.* subdomain
DOC_BASE = "https://api.sandbox.ebay.com" if SANDBOX else "https://api.ebay.com"


def _headers(content_type: str = "application/json") -> dict:
    token = get_user_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": content_type,
    }


# ── Document methods ──────────────────────────────────────────────────────────

def create_document(document_type: str, languages: List[str]) -> dict:
    """Stage a document resource for upload. Returns a documentId.

    Args:
        document_type: Type of document e.g. 'USER_GUIDE_OR_MANUAL', 'SAFETY_DATA_SHEET'.
        languages: List of language codes used in the document e.g. ['en'].
    """
    url = f"{DOC_BASE}/commerce/media/v1_beta/document"
    payload = {"documentType": document_type, "languages": languages}
    try:
        resp = requests.post(url, headers=_headers(), json=payload, timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def create_document_from_url(document_type: str, document_url: str, languages: List[str]) -> dict:
    """Download a document from a URL and add it to the user's account.

    Args:
        document_type: Type of document e.g. 'USER_GUIDE_OR_MANUAL'.
        document_url: HTTPS URL of the document (.pdf, .png, .jpg, .jpeg; max 10 MB).
        languages: List of language codes used in the document e.g. ['en'].
    """
    url = f"{DOC_BASE}/commerce/media/v1_beta/document/create_document_from_url"
    payload = {
        "documentType": document_type,
        "documentUrl": document_url,
        "languages": languages,
    }
    try:
        resp = requests.post(url, headers=_headers(), json=payload, timeout=60)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_document(document_id: str) -> dict:
    """Retrieve the current status and metadata of a document.

    Args:
        document_id: The unique identifier of the document (from createDocument).
    """
    url = f"{DOC_BASE}/commerce/media/v1_beta/document/{document_id}"
    try:
        resp = requests.get(url, headers=_headers(), timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def upload_document(document_id: str, file_path: str) -> dict:
    """Upload a file to an existing document resource.

    Args:
        document_id: The unique identifier of the document (from createDocument).
        file_path: Local filesystem path to the file (.pdf, .jpeg, .jpg, .png; max 10 MB).
    """
    url = f"{DOC_BASE}/commerce/media/v1_beta/document/{document_id}/upload"
    token = get_user_token()
    headers = {"Authorization": f"Bearer {token}"}
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            resp = requests.post(url, headers=headers, files=files, timeout=120)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Image methods ─────────────────────────────────────────────────────────────

def create_image_from_url(image_url: str) -> dict:
    """Upload a picture to eBay Picture Services (EPS) from an HTTPS URL.

    Args:
        image_url: HTTPS URL of the image (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
    """
    url = f"{BASE}/commerce/media/v1_beta/image/create_image_from_url"
    payload = {"imageUrl": image_url}
    try:
        resp = requests.post(url, headers=_headers(), json=payload, timeout=60)
        if resp.ok:
            result = resp.json()
            # Capture Location header for convenience
            if "Location" in resp.headers:
                result["location"] = resp.headers["Location"]
            return result
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def create_image_from_file(file_path: str) -> dict:
    """Upload a picture file to eBay Picture Services (EPS) using multipart/form-data.

    Args:
        file_path: Local filesystem path to the image file (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
    """
    url = f"{BASE}/commerce/media/v1_beta/image/create_image_from_file"
    token = get_user_token()
    headers = {"Authorization": f"Bearer {token}"}
    try:
        with open(file_path, "rb") as f:
            files = {"image": f}
            resp = requests.post(url, headers=headers, files=files, timeout=120)
        if resp.ok:
            result = resp.json()
            if "Location" in resp.headers:
                result["location"] = resp.headers["Location"]
            return result
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_image(image_id: str) -> dict:
    """Retrieve an EPS image URL and expiration details by image ID.

    Args:
        image_id: The unique identifier of the image (from createImageFromFile/Url).
    """
    url = f"{BASE}/commerce/media/v1_beta/image/{image_id}"
    try:
        resp = requests.get(url, headers=_headers(), timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Video methods ─────────────────────────────────────────────────────────────

def create_video(
    title: str,
    size: int,
    classification: Optional[List[str]] = None,
    description: Optional[str] = None,
) -> dict:
    """Create a video resource (metadata only). Returns a video ID in the Location header.

    Args:
        title: Title of the video.
        size: Exact size in bytes of the video file (max 157,286,400 bytes).
        classification: List of classification values; currently only ['ITEM'] is supported.
        description: Optional description of the video.
    """
    url = f"{BASE}/commerce/media/v1_beta/video"
    payload: dict = {
        "title": title,
        "size": size,
        "classification": classification or ["ITEM"],
    }
    if description:
        payload["description"] = description
    try:
        resp = requests.post(url, headers=_headers(), json=payload, timeout=30)
        result: dict = {}
        if resp.ok:
            if resp.text:
                result = resp.json()
            if "Location" in resp.headers:
                result["location"] = resp.headers["Location"]
                # Extract video_id from location URL
                result["video_id"] = resp.headers["Location"].rstrip("/").split("/")[-1]
            result["status_code"] = resp.status_code
            return result
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_video(video_id: str) -> dict:
    """Retrieve a video's metadata, status, playlist URLs, and thumbnail.

    Args:
        video_id: The unique identifier of the video.
    """
    url = f"{BASE}/commerce/media/v1_beta/video/{video_id}"
    try:
        resp = requests.get(url, headers=_headers(), timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def upload_video(video_id: str, file_path: str) -> dict:
    """Upload a video file to an existing video resource.

    The file size must exactly match the size declared in createVideo.

    Args:
        video_id: The unique identifier of the video (from createVideo).
        file_path: Local filesystem path to the .mp4 video file (MPEG-4 AVC).
    """
    url = f"{BASE}/commerce/media/v1_beta/video/{video_id}/upload"
    token = get_user_token()
    file_size = os.path.getsize(file_path)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream",
        "Content-Length": str(file_size),
    }
    try:
        with open(file_path, "rb") as f:
            resp = requests.post(url, headers=headers, data=f, timeout=300)
        if resp.ok:
            return {"status_code": resp.status_code, "message": "Video uploaded successfully"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
