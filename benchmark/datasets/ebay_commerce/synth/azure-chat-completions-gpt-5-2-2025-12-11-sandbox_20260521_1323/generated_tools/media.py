import os
from typing import Any, Dict, Optional

import requests

from .http_client import EbayClient, ebay_api_base_url


MEDIA_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_url

    Doc: docs/api_commerce_media_resources_image_methods_createImageFromUrl.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )


def create_image_from_file(file_path: str, form_field_name: str = "image") -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_file

    Doc: docs/api_commerce_media_resources_image_methods_createImageFromFile.md

    Note: Uses multipart/form-data upload.
    """
    client = EbayClient()
    try:
        token = client.oauth.get_user_token(MEDIA_SCOPE)
    except Exception as e:
        return {"error": str(e)}

    url = ebay_api_base_url(is_media=True) + "/commerce/media/v1_beta/image/create_image_from_file"
    if not os.path.exists(file_path):
        return {"error": f"file_not_found: {file_path}"}

    try:
        with open(file_path, "rb") as f:
            files = {form_field_name: (os.path.basename(file_path), f)}
            r = requests.post(url, headers={"Authorization": f"Bearer {token}"}, files=files, timeout=120)
    except Exception as e:
        return {"error": f"upload_failed: {e}", "url": url}

    # Media API returns JSON body and Location header
    try:
        body = r.json() if r.text else {}
    except Exception:
        body = {"raw": r.text}

    if r.status_code >= 400:
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return {
        **(body if isinstance(body, dict) else {"data": body}),
        "location": r.headers.get("Location"),
        "_http": {"status": r.status_code},
    }


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/image/{image_id}

    Doc: docs/api_commerce_media_resources_image_methods_getImage.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )


def create_video() -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video

    Doc: docs/api_commerce_media_resources_video_methods_createVideo.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/video",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )


def upload_video(video_id: str, file_path: str, content_type: str = "video/mp4") -> Dict[str, Any]:
    """PUT /commerce/media/v1_beta/video/{video_id}/upload

    Doc: docs/api_commerce_media_resources_video_methods_uploadVideo.md

    Note: Uploads raw bytes.
    """
    if not os.path.exists(file_path):
        return {"error": f"file_not_found: {file_path}"}
    with open(file_path, "rb") as f:
        data = f.read()

    client = EbayClient()
    return client.request(
        "PUT",
        f"/commerce/media/v1_beta/video/{video_id}/upload",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
        raw_body=data,
        content_type=content_type,
    )


def get_video(video_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/video/{video_id}

    Doc: docs/api_commerce_media_resources_video_methods_getVideo.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )


def create_document() -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document

    Doc: docs/api_commerce_media_resources_document_methods_createDocument.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )


def create_document_from_url(url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/create_document_from_url

    Doc: docs/api_commerce_media_resources_document_methods_createDocumentFromUrl.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body={"url": url},
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )


def upload_document(document_id: str, file_path: str, content_type: str = "application/pdf") -> Dict[str, Any]:
    """PUT /commerce/media/v1_beta/document/{document_id}/upload

    Doc: docs/api_commerce_media_resources_document_methods_uploadDocument.md
    """
    if not os.path.exists(file_path):
        return {"error": f"file_not_found: {file_path}"}
    with open(file_path, "rb") as f:
        data = f.read()

    client = EbayClient()
    return client.request(
        "PUT",
        f"/commerce/media/v1_beta/document/{document_id}/upload",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
        raw_body=data,
        content_type=content_type,
    )


def get_document(document_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/document/{document_id}

    Doc: docs/api_commerce_media_resources_document_methods_getDocument.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
        is_media=True,
        scope=MEDIA_SCOPE,
        user_token=True,
    )
