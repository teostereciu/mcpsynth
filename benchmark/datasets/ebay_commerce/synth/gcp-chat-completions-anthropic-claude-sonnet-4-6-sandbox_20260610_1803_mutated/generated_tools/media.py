"""
eBay Commerce Media API tools.
Base URL: https://apim.sandbox.ebay.com/commerce/media/v1_beta
Auth: User token (refresh_token)
Note: Media API uses a different subdomain (apim.* vs api.*)
"""

import requests
from .auth import get_user_token, _media_base_url


def _media_url(path: str) -> str:
    return f"{_media_base_url()}/commerce/media/v1_beta{path}"


def _user_auth_headers(content_type: str = "application/json") -> dict:
    return {
        "Authorization": f"Bearer {get_user_token()}",
        "Content-Type": content_type,
    }


# ── Document methods ──────────────────────────────────────────────────────────

def create_document(document_type: str, languages: list[str]) -> dict:
    """
    Stage a new document resource for upload.
    document_type: e.g. 'USER_GUIDE_OR_MANUAL', 'SAFETY_DATA_SHEET'
    languages: list of language codes, e.g. ['en_US']
    Returns documentId, documentStatus, documentType, languages.
    """
    try:
        resp = requests.post(
            _media_url("/document"),
            headers=_user_auth_headers(),
            json={"documentType": document_type, "languages": languages},
            timeout=30,
        )
        if resp.status_code in (200, 201):
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def create_document_from_url(document_type: str, document_url: str, languages: list[str]) -> dict:
    """
    Download a document from a URL and add it to the user's account.
    document_type: e.g. 'USER_GUIDE_OR_MANUAL', 'SAFETY_DATA_SHEET'
    document_url: HTTPS URL to a .pdf, .png, .jpg, or .jpeg file (max 10 MB)
    languages: list of language codes, e.g. ['en_US']
    Returns documentId, documentStatus, documentType, languages.
    """
    try:
        resp = requests.post(
            _media_url("/document/create_document_from_url"),
            headers=_user_auth_headers(),
            json={
                "documentType": document_type,
                "documentUrl": document_url,
                "languages": languages,
            },
            timeout=60,
        )
        if resp.status_code in (200, 201):
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_document(document_id: str) -> dict:
    """
    Retrieve the current status and metadata of a document by its ID.
    Returns documentId, documentMetadata, documentStatus, documentType, languages.
    """
    try:
        resp = requests.get(
            _media_url(f"/document/{document_id}"),
            headers={"Authorization": f"Bearer {get_user_token()}"},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def upload_document(document_id: str, file_path: str) -> dict:
    """
    Upload a file to an existing document resource.
    document_id: ID returned from create_document.
    file_path: local path to the file (.pdf, .jpeg, .jpg, .png — max 10 MB).
    Returns documentId, documentMetadata, documentStatus, documentType, languages.
    """
    try:
        with open(file_path, "rb") as f:
            resp = requests.post(
                _media_url(f"/document/{document_id}/upload"),
                headers={"Authorization": f"Bearer {get_user_token()}"},
                files={"file": f},
                timeout=120,
            )
        if resp.status_code in (200, 201):
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Image methods ─────────────────────────────────────────────────────────────

def create_image_from_url(image_url: str) -> dict:
    """
    Upload a picture to eBay Picture Services (EPS) from an HTTPS URL.
    image_url: HTTPS URL to the image (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
    Returns imageUrl (EPS URL) and expirationDate.
    """
    try:
        resp = requests.post(
            _media_url("/image/create_image_from_url"),
            headers=_user_auth_headers(),
            json={"imageUrl": image_url},
            timeout=60,
        )
        if resp.status_code in (200, 201):
            result = resp.json() if resp.text else {}
            location = resp.headers.get("Location", "")
            if location:
                result["location"] = location
            return result
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def create_image_from_file(file_path: str) -> dict:
    """
    Upload a picture file to eBay Picture Services (EPS) using multipart/form-data.
    file_path: local path to the image file (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
    Returns imageUrl (EPS URL) and expirationDate.
    """
    try:
        with open(file_path, "rb") as f:
            resp = requests.post(
                _media_url("/image/create_image_from_file"),
                headers={"Authorization": f"Bearer {get_user_token()}"},
                files={"image": f},
                timeout=120,
            )
        if resp.status_code in (200, 201):
            result = resp.json() if resp.text else {}
            location = resp.headers.get("Location", "")
            if location:
                result["location"] = location
            return result
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_image(image_id: str) -> dict:
    """
    Retrieve an EPS image URL and its expiration details by image ID.
    Returns imageUrl and expirationDate.
    """
    try:
        resp = requests.get(
            _media_url(f"/image/{image_id}"),
            headers={"Authorization": f"Bearer {get_user_token()}"},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Video methods ─────────────────────────────────────────────────────────────

def create_video(
    title: str,
    size: int,
    classification: list[str],
    description: str | None = None,
) -> dict:
    """
    Create a video resource (metadata only — use upload_video to upload the file).
    title: video title.
    size: exact size in bytes of the video file (max 157,286,400 bytes).
    classification: list of classification values, e.g. ['ITEM'].
    description: optional video description.
    Returns the Location header containing the video ID.
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
            _media_url("/video"),
            headers=_user_auth_headers(),
            json=body,
            timeout=30,
        )
        if resp.status_code in (200, 201):
            location = resp.headers.get("Location", "")
            return {"location": location, "status_code": resp.status_code}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_video(video_id: str) -> dict:
    """
    Retrieve a video's metadata and content by video ID.
    Returns title, size, classification, description, videoId, playLists,
    status, statusMessage, expirationDate, thumbnail, and moderation info.
    """
    try:
        resp = requests.get(
            _media_url(f"/video/{video_id}"),
            headers={"Authorization": f"Bearer {get_user_token()}"},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def upload_video(video_id: str, file_path: str) -> dict:
    """
    Upload a video file to an existing video resource.
    video_id: ID returned from create_video (extracted from Location header).
    file_path: local path to the .mp4 (MPEG-4 AVC) video file.
    Returns status_code 200 on success.
    """
    try:
        file_size = None
        import os
        file_size = os.path.getsize(file_path)
        with open(file_path, "rb") as f:
            headers = {
                "Authorization": f"Bearer {get_user_token()}",
                "Content-Type": "application/octet-stream",
                "Content-Length": str(file_size),
            }
            resp = requests.post(
                _media_url(f"/video/{video_id}/upload"),
                headers=headers,
                data=f,
                timeout=300,
            )
        if resp.status_code == 200:
            return {"status": "uploaded", "status_code": 200}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
