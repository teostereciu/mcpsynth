import os
from typing import Any, Dict, Optional

import requests

from .ebay_client import EbayClient, get_base_url


MEDIA_SCOPE_USER = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def create_image_from_file(file_path: str) -> Dict[str, Any]:
    """Upload an image file to EPS.

    POST /commerce/media/v1_beta/image/create_image_from_file (apim.* base)
    OAuth: user token with sell.inventory
    """
    if not os.path.isfile(file_path):
        return {"error": f"file not found: {file_path}"}

    client = EbayClient()
    token = client.oauth.get_user_token(MEDIA_SCOPE_USER)
    url = get_base_url(is_media=True) + "/commerce/media/v1_beta/image/create_image_from_file"

    with open(file_path, "rb") as f:
        files = {"image": (os.path.basename(file_path), f)}
        try:
            r = requests.post(
                url,
                headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
                files=files,
                timeout=120,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

    data: Any
    ct = r.headers.get("Content-Type", "")
    if "application/json" in ct:
        try:
            data = r.json()
        except Exception:
            data = {"raw": r.text}
    else:
        data = {"raw": r.text}

    if r.status_code >= 400:
        return {"error": "ebay_api_error", "status": r.status_code, "url": url, "response": data}

    # capture Location header if present
    loc = r.headers.get("Location")
    if loc:
        return {"location": loc, "response": data}
    return data


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Create an EPS image by downloading from a URL.

    POST /commerce/media/v1_beta/image/create_image_from_url
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )


def get_image(image_id: str) -> Dict[str, Any]:
    """Get EPS image details.

    GET /commerce/media/v1_beta/image/{image_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )


def create_document(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Create a document container (metadata) for later upload.

    POST /commerce/media/v1_beta/document
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document",
        json_body=metadata,
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )


def create_document_from_url(source_url: str, *, document_type: Optional[str] = None) -> Dict[str, Any]:
    """Create a document by downloading from a URL.

    POST /commerce/media/v1_beta/document/create_document_from_url
    """
    body: Dict[str, Any] = {"url": source_url}
    if document_type is not None:
        body["documentType"] = document_type
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body=body,
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )


def get_document(document_id: str) -> Dict[str, Any]:
    """Get document details.

    GET /commerce/media/v1_beta/document/{document_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )


def upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    """Upload document binary to an existing document container.

    POST /commerce/media/v1_beta/document/{document_id}/upload
    """
    if not os.path.isfile(file_path):
        return {"error": f"file not found: {file_path}"}

    client = EbayClient()
    token = client.oauth.get_user_token(MEDIA_SCOPE_USER)
    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/document/{document_id}/upload"

    with open(file_path, "rb") as f:
        try:
            r = requests.post(
                url,
                headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
                data=f,
                timeout=120,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

    ct = r.headers.get("Content-Type", "")
    if "application/json" in ct:
        try:
            data: Any = r.json()
        except Exception:
            data = {"raw": r.text}
    else:
        data = {"raw": r.text}

    if r.status_code >= 400:
        return {"error": "ebay_api_error", "status": r.status_code, "url": url, "response": data}

    loc = r.headers.get("Location")
    if loc:
        return {"location": loc, "response": data}
    return data


def create_video(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Create a video container (metadata) for later upload.

    POST /commerce/media/v1_beta/video
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/media/v1_beta/video",
        json_body=metadata,
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )


def upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    """Upload video binary to an existing video container.

    POST /commerce/media/v1_beta/video/{video_id}/upload
    """
    if not os.path.isfile(file_path):
        return {"error": f"file not found: {file_path}"}

    client = EbayClient()
    token = client.oauth.get_user_token(MEDIA_SCOPE_USER)
    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/video/{video_id}/upload"

    with open(file_path, "rb") as f:
        try:
            r = requests.post(
                url,
                headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
                data=f,
                timeout=300,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

    ct = r.headers.get("Content-Type", "")
    if "application/json" in ct:
        try:
            data: Any = r.json()
        except Exception:
            data = {"raw": r.text}
    else:
        data = {"raw": r.text}

    if r.status_code >= 400:
        return {"error": "ebay_api_error", "status": r.status_code, "url": url, "response": data}

    loc = r.headers.get("Location")
    if loc:
        return {"location": loc, "response": data}
    return data


def get_video(video_id: str) -> Dict[str, Any]:
    """Get video details.

    GET /commerce/media/v1_beta/video/{video_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        scope=MEDIA_SCOPE_USER,
        user=True,
        is_media=True,
    )
