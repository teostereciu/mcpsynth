import os
from typing import Any, Dict, Optional

import requests

from .http_client import EbayHTTP


MEDIA_SCOPE_USER = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_url

    Doc: docs/api_commerce_media_resources_image_methods_createImageFromUrl.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.apim_base,
        "/commerce/media/v1_beta/image/create_image_from_url",
        scope=MEDIA_SCOPE_USER,
        user=True,
        json={"imageUrl": image_url},
        headers={"Content-Type": "application/json"},
    )


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/image/{image_id}

    Doc: docs/api_commerce_media_resources_image_methods_getImage.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.apim_base,
        f"/commerce/media/v1_beta/image/{image_id}",
        scope=MEDIA_SCOPE_USER,
        user=True,
    )


def create_image_from_file(file_path: str, *, content_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image

    Doc: docs/api_commerce_media_resources_image_methods_createImageFromFile.md

    Note: Uses multipart/form-data upload.
    """
    if not os.path.exists(file_path):
        return {"error": "file_not_found", "path": file_path}

    http = EbayHTTP()
    token, err = http.oauth.get_user_token(MEDIA_SCOPE_USER)
    if err:
        return err

    url = http.oauth.apim_base.rstrip("/") + "/commerce/media/v1_beta/image/create_image_from_file"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    ct = content_type
    if ct is None:
        # best-effort; requests will set multipart boundary
        ct = "application/octet-stream"

    try:
        with open(file_path, "rb") as f:
            files = {"image": (os.path.basename(file_path), f, ct)}
            resp = requests.post(url, headers=headers, files=files, timeout=120)
    except Exception as e:
        return {"error": "request_failed", "details": str(e), "url": url}

    try:
        payload = resp.json()
    except Exception:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        return {"error": "http_error", "status": resp.status_code, "url": url, "details": payload}
    return payload


def create_video(*, title: str, size: int, description: Optional[str] = None, classification: str = "ITEM") -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video

    Doc: docs/api_commerce_media_resources_video_methods_createVideo.md

    classification: currently only ITEM is supported by eBay.
    """
    http = EbayHTTP()
    body: Dict[str, Any] = {
        "title": title,
        "size": size,
        "classification": [{"name": classification}],
    }
    if description is not None:
        body["description"] = description

    return http.request(
        "POST",
        http.oauth.apim_base,
        "/commerce/media/v1_beta/video",
        scope=MEDIA_SCOPE_USER,
        user=True,
        json=body,
        headers={"Content-Type": "application/json"},
    )


def upload_video(video_id: str, file_path: str, *, content_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video/{video_id}/upload_video

    Doc: docs/api_commerce_media_resources_video_methods_uploadVideo.md
    """
    if not os.path.exists(file_path):
        return {"error": "file_not_found", "path": file_path}

    http = EbayHTTP()
    token, err = http.oauth.get_user_token(MEDIA_SCOPE_USER)
    if err:
        return err

    url = http.oauth.apim_base.rstrip("/") + f"/commerce/media/v1_beta/video/{video_id}/upload_video"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    ct = content_type or "application/octet-stream"
    try:
        with open(file_path, "rb") as f:
            files = {"video": (os.path.basename(file_path), f, ct)}
            resp = requests.post(url, headers=headers, files=files, timeout=300)
    except Exception as e:
        return {"error": "request_failed", "details": str(e), "url": url}

    try:
        payload = resp.json()
    except Exception:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        return {"error": "http_error", "status": resp.status_code, "url": url, "details": payload}
    return payload


def get_video(video_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/video/{video_id}

    Doc: docs/api_commerce_media_resources_video_methods_getVideo.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.apim_base,
        f"/commerce/media/v1_beta/video/{video_id}",
        scope=MEDIA_SCOPE_USER,
        user=True,
    )


def create_document(*, title: str, size: int, description: Optional[str] = None, classification: str = "ITEM") -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document

    Doc: docs/api_commerce_media_resources_document_methods_createDocument.md
    """
    http = EbayHTTP()
    body: Dict[str, Any] = {
        "title": title,
        "size": size,
        "classification": [{"name": classification}],
    }
    if description is not None:
        body["description"] = description

    return http.request(
        "POST",
        http.oauth.apim_base,
        "/commerce/media/v1_beta/document",
        scope=MEDIA_SCOPE_USER,
        user=True,
        json=body,
        headers={"Content-Type": "application/json"},
    )


def create_document_from_url(document_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/create_document_from_url

    Doc: docs/api_commerce_media_resources_document_methods_createDocumentFromUrl.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.apim_base,
        "/commerce/media/v1_beta/document/create_document_from_url",
        scope=MEDIA_SCOPE_USER,
        user=True,
        json={"documentUrl": document_url},
        headers={"Content-Type": "application/json"},
    )


def upload_document(document_id: str, file_path: str, *, content_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/{document_id}/upload_document

    Doc: docs/api_commerce_media_resources_document_methods_uploadDocument.md
    """
    if not os.path.exists(file_path):
        return {"error": "file_not_found", "path": file_path}

    http = EbayHTTP()
    token, err = http.oauth.get_user_token(MEDIA_SCOPE_USER)
    if err:
        return err

    url = http.oauth.apim_base.rstrip("/") + f"/commerce/media/v1_beta/document/{document_id}/upload_document"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    ct = content_type or "application/octet-stream"
    try:
        with open(file_path, "rb") as f:
            files = {"document": (os.path.basename(file_path), f, ct)}
            resp = requests.post(url, headers=headers, files=files, timeout=300)
    except Exception as e:
        return {"error": "request_failed", "details": str(e), "url": url}

    try:
        payload = resp.json()
    except Exception:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        return {"error": "http_error", "status": resp.status_code, "url": url, "details": payload}
    return payload


def get_document(document_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/document/{document_id}

    Doc: docs/api_commerce_media_resources_document_methods_getDocument.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.apim_base,
        f"/commerce/media/v1_beta/document/{document_id}",
        scope=MEDIA_SCOPE_USER,
        user=True,
    )
