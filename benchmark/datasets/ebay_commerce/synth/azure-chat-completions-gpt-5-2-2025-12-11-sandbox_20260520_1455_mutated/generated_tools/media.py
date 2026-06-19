from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def create_image_from_file(file_path: str) -> Dict[str, Any]:
    """POST /image/create_image_from_file (multipart/form-data)

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    with open(file_path, "rb") as f:
        files = {"image": (file_path.split("/")[-1], f)}
        return client.request(
            "POST",
            "/commerce/media/v1_beta/image/create_image_from_file",
            files=files,
        )


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """POST /image/create_image_from_url

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    return client.request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json={"imageUrl": image_url},
    )


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /image/{image_id}

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    return client.request("GET", f"/commerce/media/v1_beta/image/{image_id}")


def create_document(type: str, languages: list[str]) -> Dict[str, Any]:
    """POST /document

    Stages a document resource; use upload_document to upload bytes.

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document",
        json={"type": type, "languages": languages},
    )


def create_document_from_url(type: str, languages: list[str], document_url: str) -> Dict[str, Any]:
    """POST /document/create_document_from_url

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json={"type": type, "languages": languages, "documentUrl": document_url},
    )


def upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    """POST /document/{document_id}/upload (multipart/form-data)

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    with open(file_path, "rb") as f:
        files = {"file": (file_path.split("/")[-1], f)}
        return client.request(
            "POST",
            f"/commerce/media/v1_beta/document/{document_id}/upload",
            files=files,
        )


def get_document(document_id: str) -> Dict[str, Any]:
    """GET /document/{document_id}

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    return client.request("GET", f"/commerce/media/v1_beta/document/{document_id}")


def create_video(title: str, size: int, classification: str, description: Optional[str] = None) -> Dict[str, Any]:
    """POST /video

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    payload: Dict[str, Any] = {"title": title, "size": size, "classification": classification}
    if description is not None:
        payload["description"] = description
    return client.request("POST", "/commerce/media/v1_beta/video", json=payload)


def upload_video(video_id: str, file_path: str) -> Dict[str, Any]:
    """POST /video/{video_id}/upload (multipart/form-data)

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    with open(file_path, "rb") as f:
        files = {"file": (file_path.split("/")[-1], f)}
        return client.request(
            "POST",
            f"/commerce/media/v1_beta/video/{video_id}/upload",
            files=files,
        )


def get_video(video_id: str) -> Dict[str, Any]:
    """GET /video/{video_id}

    OAuth scope: sell.inventory (user token)
    Base domain: apim.ebay.com
    """
    client = EbayClient.for_media_api(user_scoped=True)
    return client.request("GET", f"/commerce/media/v1_beta/video/{video_id}")
