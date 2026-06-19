"""Tools for eBay Commerce Media API (apim.* domain).

Includes image, document, and video helpers.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Optional

from .http import request_json


def _extract_id_from_location(location: Optional[str]) -> Optional[str]:
    if not location:
        return None
    m = re.search(r"/commerce/media/v1(?:_beta)?/(?:image|document|video)/([^/?#]+)", location)
    return m.group(1) if m else None


# -------------------- Images --------------------

def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Upload an image to EPS from a public HTTPS URL.

    Docs: POST /commerce/media/v1_beta/image/create_image_from_url
    Auth: User token (sell.inventory scope)

    Returns payload plus extracted imageId when possible.
    """

    status, data, headers = request_json(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        user_auth=True,
        media=True,
    )
    if status < 400:
        image_id = _extract_id_from_location(headers.get("Location") or headers.get("location"))
        if image_id:
            data = dict(data)
            data["imageId"] = image_id
    return data


def get_image(image_id: str) -> Dict[str, Any]:
    """Get EPS image metadata.

    Docs: GET /commerce/media/v1_beta/image/{image_id}
    Auth: User token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        user_auth=True,
        media=True,
    )
    return data


# -------------------- Documents --------------------

def create_document_from_url(document_url: str) -> Dict[str, Any]:
    """Upload a document from a public HTTPS URL.

    Docs: POST /commerce/media/v1_beta/document/create_document_from_url
    Auth: User token

    Returns payload plus extracted documentId when possible.
    """

    status, data, headers = request_json(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body={"documentUrl": document_url},
        user_auth=True,
        media=True,
    )
    if status < 400:
        doc_id = _extract_id_from_location(headers.get("Location") or headers.get("location"))
        if doc_id:
            data = dict(data)
            data["documentId"] = doc_id
    return data


def get_document(document_id: str) -> Dict[str, Any]:
    """Get document metadata.

    Docs: GET /commerce/media/v1_beta/document/{document_id}
    Auth: User token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
        user_auth=True,
        media=True,
    )
    return data


# -------------------- Videos --------------------

def create_video() -> Dict[str, Any]:
    """Create a video resource (upload session).

    Docs: POST /commerce/media/v1_beta/video
    Auth: User token
    """

    status, data, headers = request_json(
        "POST",
        "/commerce/media/v1_beta/video",
        json_body={},
        user_auth=True,
        media=True,
    )
    if status < 400:
        vid = _extract_id_from_location(headers.get("Location") or headers.get("location"))
        if vid:
            data = dict(data)
            data["videoId"] = vid
    return data


def get_video(video_id: str) -> Dict[str, Any]:
    """Get video metadata.

    Docs: GET /commerce/media/v1_beta/video/{video_id}
    Auth: User token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        user_auth=True,
        media=True,
    )
    return data
