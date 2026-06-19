from __future__ import annotations

import re
from typing import Any, Dict, Optional

import requests

from .http import media_base_url, request_json


SCOPE_INVENTORY = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def _extract_id_from_location(location: Optional[str]) -> Optional[str]:
    if not location:
        return None
    m = re.search(r"/commerce/media/v1_beta/(image|document|video)/([^/?#]+)", location)
    if not m:
        return None
    return m.group(2)


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_url (user token)."""
    # Need Location header for image_id; use requests directly.
    from .http import get_user_access_token

    token = get_user_access_token(scope=SCOPE_INVENTORY)
    url = media_base_url() + "/commerce/media/v1_beta/image/create_image_from_url"
    try:
        resp = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            json={"imageUrl": image_url},
            timeout=60,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if not resp.ok:
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {"error": {"status": resp.status_code, "reason": resp.reason, "details": err}, "url": url}

    location = resp.headers.get("Location")
    image_id = _extract_id_from_location(location)
    payload: Dict[str, Any] = {}
    try:
        payload = resp.json()
    except Exception:
        payload = {"raw": resp.text}

    if location:
        payload["location"] = location
    if image_id:
        payload["imageId"] = image_id
    return payload


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/image/{image_id} (user token)."""
    return request_json(
        "GET",
        media_base_url(),
        f"/commerce/media/v1_beta/image/{image_id}",
        user_auth=True,
        scope=SCOPE_INVENTORY,
    )


def create_document_from_url(document_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/create_document_from_url (user token)."""
    from .http import get_user_access_token

    token = get_user_access_token(scope=SCOPE_INVENTORY)
    url = media_base_url() + "/commerce/media/v1_beta/document/create_document_from_url"
    try:
        resp = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            json={"documentUrl": document_url},
            timeout=60,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if not resp.ok:
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {"error": {"status": resp.status_code, "reason": resp.reason, "details": err}, "url": url}

    location = resp.headers.get("Location")
    document_id = _extract_id_from_location(location)
    payload: Dict[str, Any] = {}
    try:
        payload = resp.json()
    except Exception:
        payload = {"raw": resp.text}

    if location:
        payload["location"] = location
    if document_id:
        payload["documentId"] = document_id
    return payload


def get_document(document_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/document/{document_id} (user token)."""
    return request_json(
        "GET",
        media_base_url(),
        f"/commerce/media/v1_beta/document/{document_id}",
        user_auth=True,
        scope=SCOPE_INVENTORY,
    )


def upload_video() -> Dict[str, Any]:
    """Placeholder for uploadVideo (multipart). Not implemented."""
    return {"error": "upload_video not implemented (multipart upload)"}


def create_video() -> Dict[str, Any]:
    """Placeholder for createVideo. Not implemented."""
    return {"error": "create_video not implemented"}


def get_video(video_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/video/{video_id} (user token)."""
    return request_json(
        "GET",
        media_base_url(),
        f"/commerce/media/v1_beta/video/{video_id}",
        user_auth=True,
        scope=SCOPE_INVENTORY,
    )
