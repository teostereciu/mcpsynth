from typing import Any, Dict, Optional

from .ebay_auth import request_json


# Media API (different base domain; user token typically required)


def upload_image(image_url: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/upload"""
    status, body = request_json(
        "POST",
        "/commerce/media/v1_beta/image/upload",
        json={"imageUrl": image_url},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        user=True,
        media=True,
    )
    return {"status": status, "data": body}


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/image/{imageId}"""
    status, body = request_json(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        user=True,
        media=True,
    )
    return {"status": status, "data": body}
