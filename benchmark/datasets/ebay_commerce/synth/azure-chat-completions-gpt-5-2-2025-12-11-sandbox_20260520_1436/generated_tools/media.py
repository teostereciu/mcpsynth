import os
from typing import Any, Dict, Optional

import requests

from .ebay_client import EbayClient, _base_url


SELL_INVENTORY_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def create_image_from_file(file_path: str) -> Any:
    """POST /commerce/media/v1_beta/image/create_image_from_file (multipart)

    Doc: docs/api_commerce_media_resources_image_methods_createImageFromFile.md

    Returns JSON payload plus captured Location header when available.
    """
    if not os.path.exists(file_path):
        return {"error": f"file not found: {file_path}"}

    client = EbayClient()
    token = client.get_user_token(SELL_INVENTORY_SCOPE)
    if isinstance(token, dict):
        return token

    url = _base_url(media=True) + "/commerce/media/v1_beta/image/create_image_from_file"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    with open(file_path, "rb") as f:
        files = {"image": (os.path.basename(file_path), f)}
        r = requests.post(url, headers=headers, files=files, timeout=300)

    if r.status_code >= 400:
        try:
            details = r.json()
        except Exception:
            details = {"message": r.text}
        return {"error": {"status": r.status_code, "reason": r.reason, "url": r.url, "details": details}}

    out: Dict[str, Any] = {}
    try:
        out.update(r.json())
    except Exception:
        out["text"] = r.text
    if r.headers.get("Location"):
        out["location"] = r.headers["Location"]
    out["status"] = r.status_code
    return out


def create_image_from_url(image_url: str) -> Any:
    """POST /commerce/media/v1_beta/image/create_image_from_url

    Doc: docs/api_commerce_media_resources_image_methods_createImageFromUrl.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def get_image(image_id: str) -> Any:
    """GET /commerce/media/v1_beta/image/{image_id}

    Doc: docs/api_commerce_media_resources_image_methods_getImage.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def create_document(metadata: Dict[str, Any]) -> Any:
    """POST /commerce/media/v1_beta/document

    Doc: docs/api_commerce_media_resources_document_methods_createDocument.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document",
        json_body=metadata,
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def create_document_from_url(url: str) -> Any:
    """POST /commerce/media/v1_beta/document/create_document_from_url

    Doc: docs/api_commerce_media_resources_document_methods_createDocumentFromUrl.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body={"documentUrl": url},
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def upload_document(document_id: str, file_path: str, content_type: Optional[str] = None) -> Any:
    """POST /commerce/media/v1_beta/document/{document_id}/upload_document (binary)

    Doc: docs/api_commerce_media_resources_document_methods_uploadDocument.md
    """
    if not os.path.exists(file_path):
        return {"error": f"file not found: {file_path}"}
    if content_type is None:
        content_type = "application/octet-stream"

    with open(file_path, "rb") as f:
        raw = f.read()

    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/media/v1_beta/document/{document_id}/upload_document",
        raw_body=raw,
        content_type=content_type,
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def get_document(document_id: str) -> Any:
    """GET /commerce/media/v1_beta/document/{document_id}

    Doc: docs/api_commerce_media_resources_document_methods_getDocument.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def create_video(metadata: Dict[str, Any]) -> Any:
    """POST /commerce/media/v1_beta/video

    Doc: docs/api_commerce_media_resources_video_methods_createVideo.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/video",
        json_body=metadata,
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def upload_video(video_id: str, file_path: str, content_type: Optional[str] = None) -> Any:
    """POST /commerce/media/v1_beta/video/{video_id}/upload_video (binary)

    Doc: docs/api_commerce_media_resources_video_methods_uploadVideo.md
    """
    if not os.path.exists(file_path):
        return {"error": f"file not found: {file_path}"}
    if content_type is None:
        content_type = "application/octet-stream"

    with open(file_path, "rb") as f:
        raw = f.read()

    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/media/v1_beta/video/{video_id}/upload_video",
        raw_body=raw,
        content_type=content_type,
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )


def get_video(video_id: str) -> Any:
    """GET /commerce/media/v1_beta/video/{video_id}

    Doc: docs/api_commerce_media_resources_video_methods_getVideo.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        media=True,
        user_scope=SELL_INVENTORY_SCOPE,
    )
