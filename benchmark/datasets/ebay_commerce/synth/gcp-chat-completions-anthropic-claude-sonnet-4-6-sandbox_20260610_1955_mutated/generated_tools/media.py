"""
eBay Commerce Media API tools.
Uses user token (refresh_token grant).
Base: apim.sandbox.ebay.com / apim.ebay.com  (different subdomain!)
"""
import os
from typing import Optional
import requests
from .auth import MEDIA_BASE_URL, get_user_token, safe_json

MEDIA_BASE = f"{MEDIA_BASE_URL}/commerce/media/v1_beta"


def _media_headers() -> dict:
    return {
        "Authorization": f"Bearer {get_user_token()}",
        "Content-Type": "application/json",
    }


# ── Documents ──────────────────────────────────────────────────────────────

def create_document(document_type: str, languages: list) -> dict:
    """
    Stage a new document resource for upload. Returns a documentId needed
    for uploadDocument. The document starts in PENDING_UPLOAD status.

    Args:
        document_type: Type of document e.g. 'USER_GUIDE_OR_MANUAL', 'SAFETY_DATA_SHEET'.
        languages: List of language codes used in the document e.g. ['en_US'].
    """
    try:
        resp = requests.post(
            f"{MEDIA_BASE}/document",
            headers=_media_headers(),
            json={"documentType": document_type, "languages": languages},
            timeout=30,
        )
        result = safe_json(resp)
        # Also capture Location header if present
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
        return result
    except Exception as e:
        return {"error": str(e)}


def create_document_from_url(document_type: str, document_url: str, languages: list) -> dict:
    """
    Download a document from a URL and add it to the user's account.
    The document URL must be HTTPS and point to a .pdf, .png, .jpg, or .jpeg file (max 10 MB).

    Args:
        document_type: Type of document e.g. 'USER_GUIDE_OR_MANUAL'.
        document_url: HTTPS URL of the document to download.
        languages: List of language codes e.g. ['en_US'].
    """
    try:
        resp = requests.post(
            f"{MEDIA_BASE}/document/create_document_from_url",
            headers=_media_headers(),
            json={
                "documentType": document_type,
                "documentUrl": document_url,
                "languages": languages,
            },
            timeout=60,
        )
        result = safe_json(resp)
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
        return result
    except Exception as e:
        return {"error": str(e)}


def get_document(document_id: str) -> dict:
    """
    Retrieve the current status and metadata of a document by its ID.
    Returns documentStatus, documentType, languages, and documentMetadata (fileName, fileSize, fileType).

    Args:
        document_id: The unique identifier of the document (returned by createDocument).
    """
    try:
        resp = requests.get(
            f"{MEDIA_BASE}/document/{document_id}",
            headers=_media_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def upload_document(document_id: str, file_path: str) -> dict:
    """
    Upload a file to an existing document resource. Supported types: PDF, JPEG, JPG, PNG (max 10 MB).
    The document must have been created with createDocument first.

    Args:
        document_id: The document ID returned by createDocument.
        file_path: Local filesystem path to the file to upload.
    """
    try:
        token = get_user_token()
        with open(file_path, "rb") as f:
            resp = requests.post(
                f"{MEDIA_BASE}/document/{document_id}/upload",
                headers={"Authorization": f"Bearer {token}"},
                files={"file": f},
                timeout=120,
            )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


# ── Images ─────────────────────────────────────────────────────────────────

def create_image_from_url(image_url: str) -> dict:
    """
    Upload a picture to eBay Picture Services (EPS) from an HTTPS URL.
    Returns the EPS imageUrl and expirationDate. The Location header contains the image_id URI.

    Args:
        image_url: HTTPS URL of the image (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
    """
    try:
        resp = requests.post(
            f"{MEDIA_BASE}/image/create_image_from_url",
            headers=_media_headers(),
            json={"imageUrl": image_url},
            timeout=60,
        )
        result = safe_json(resp)
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
        return result
    except Exception as e:
        return {"error": str(e)}


def create_image_from_file(file_path: str) -> dict:
    """
    Upload a picture file to eBay Picture Services (EPS) using multipart/form-data.
    Returns the EPS imageUrl and expirationDate. The Location header contains the image_id URI.

    Args:
        file_path: Local filesystem path to the image file (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
    """
    try:
        token = get_user_token()
        with open(file_path, "rb") as f:
            resp = requests.post(
                f"{MEDIA_BASE}/image/create_image_from_file",
                headers={"Authorization": f"Bearer {token}"},
                files={"image": f},
                timeout=120,
            )
        result = safe_json(resp)
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
        return result
    except Exception as e:
        return {"error": str(e)}


def get_image(image_id: str) -> dict:
    """
    Retrieve an EPS image URL and its expiration details by image ID.
    Returns imageUrl and expirationDate.

    Args:
        image_id: The unique identifier of the image (from createImageFromFile/Url Location header).
    """
    try:
        resp = requests.get(
            f"{MEDIA_BASE}/image/{image_id}",
            headers=_media_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


# ── Videos ─────────────────────────────────────────────────────────────────

def create_video(
    title: str,
    size: int,
    classification: list,
    description: Optional[str] = None,
) -> dict:
    """
    Create a video resource (metadata only). Returns a video ID in the Location header.
    Use uploadVideo to upload the actual video file afterwards.

    Args:
        title: Title of the video.
        size: Size of the video file in bytes (max 157,286,400).
        classification: List of classification values — currently only ['ITEM'] is supported.
        description: Optional description of the video.
    """
    try:
        body: dict = {
            "title": title,
            "size": size,
            "classification": classification,
        }
        if description:
            body["description"] = description

        resp = requests.post(
            f"{MEDIA_BASE}/video",
            headers=_media_headers(),
            json=body,
            timeout=30,
        )
        result = {"status_code": resp.status_code}
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
            # Extract video_id from location URL
            result["video_id"] = location.rstrip("/").split("/")[-1]
        if resp.content:
            result.update(safe_json(resp))
        return result
    except Exception as e:
        return {"error": str(e)}


def get_video(video_id: str) -> dict:
    """
    Retrieve a video's metadata, status, playlist URLs, and thumbnail by video ID.
    Status values: PENDING_UPLOAD, PROCESSING, LIVE, BLOCKED, PROCESSING_FAILED.

    Args:
        video_id: The unique identifier of the video.
    """
    try:
        resp = requests.get(
            f"{MEDIA_BASE}/video/{video_id}",
            headers=_media_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def upload_video(video_id: str, file_path: str) -> dict:
    """
    Upload an MP4 video file to an existing video resource.
    The file size must exactly match the size declared in createVideo.

    Args:
        video_id: The video ID returned by createVideo.
        file_path: Local filesystem path to the .mp4 video file.
    """
    try:
        token = get_user_token()
        file_size = os.path.getsize(file_path)
        with open(file_path, "rb") as f:
            resp = requests.post(
                f"{MEDIA_BASE}/video/{video_id}/upload",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                    "Content-Length": str(file_size),
                },
                data=f,
                timeout=300,
            )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}
