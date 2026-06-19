import os
from typing import Any, Dict, Optional

import requests

from .ebay_client import EbayClient


SELL_INVENTORY_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def _file_tuple(path: str) -> tuple:
    filename = os.path.basename(path)
    return (filename, open(path, "rb"), "application/octet-stream")


def create_image_from_file(file_path: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_file (multipart/form-data)"""
    client = EbayClient()
    try:
        token = client.get_user_token(scope=SELL_INVENTORY_SCOPE)
    except Exception as e:
        return {"error": str(e)}

    url = client.media_base.rstrip("/") + "/commerce/media/v1_beta/image/create_image_from_file"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    try:
        with open(file_path, "rb") as f:
            files = {"image": (os.path.basename(file_path), f, "application/octet-stream")}
            resp = requests.post(url, headers=headers, files=files, timeout=120)
    except Exception as e:
        return {"error": str(e)}

    if resp.status_code >= 400:
        try:
            return {"error": resp.json(), "status_code": resp.status_code}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}

    out: Dict[str, Any] = {}
    try:
        out.update(resp.json())
    except Exception:
        out["raw"] = resp.text
    loc = resp.headers.get("Location")
    if loc:
        out["location"] = loc
    out["status_code"] = resp.status_code
    return out


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_url"""
    client = EbayClient()
    return client.request(
        "POST",
        client.media_base,
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        headers={"Content-Type": "application/json"},
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
        timeout=120,
    )


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/image/{image_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.media_base,
        f"/commerce/media/v1_beta/image/{image_id}",
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
    )


def create_video(
    *,
    title: str,
    size: int,
    classification: Optional[list] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video"""
    client = EbayClient()
    body: Dict[str, Any] = {"title": title, "size": size}
    body["classification"] = classification if classification is not None else ["ITEM"]
    if description is not None:
        body["description"] = description
    return client.request(
        "POST",
        client.media_base,
        "/commerce/media/v1_beta/video",
        json_body=body,
        headers={"Content-Type": "application/json"},
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
        timeout=120,
    )


def upload_video(
    video_id: str,
    file_path: str,
    *,
    content_range: Optional[str] = None,
    content_length: Optional[int] = None,
) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video/{video_id}/upload (octet-stream)"""
    client = EbayClient()
    try:
        token = client.get_user_token(scope=SELL_INVENTORY_SCOPE)
    except Exception as e:
        return {"error": str(e)}

    url = client.media_base.rstrip("/") + f"/commerce/media/v1_beta/video/{video_id}/upload"
    headers: Dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream",
        "Accept": "application/json",
    }
    if content_range:
        headers["Content-Range"] = content_range
    if content_length is not None:
        headers["Content-Length"] = str(content_length)

    try:
        with open(file_path, "rb") as f:
            resp = requests.post(url, headers=headers, data=f, timeout=300)
    except Exception as e:
        return {"error": str(e)}

    if resp.status_code >= 400:
        try:
            return {"error": resp.json(), "status_code": resp.status_code}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}

    if resp.status_code == 204:
        return {"status_code": 204}
    try:
        return {"status_code": resp.status_code, **resp.json()}
    except Exception:
        return {"status_code": resp.status_code, "raw": resp.text}


def get_video(video_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/video/{video_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.media_base,
        f"/commerce/media/v1_beta/video/{video_id}",
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
    )


def create_document(document_type: str, languages: list[str]) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document"""
    client = EbayClient()
    return client.request(
        "POST",
        client.media_base,
        "/commerce/media/v1_beta/document",
        json_body={"documentType": document_type, "languages": languages},
        headers={"Content-Type": "application/json"},
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
        timeout=120,
    )


def upload_document(document_id: str, file_path: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/{document_id}/upload (multipart/form-data)"""
    client = EbayClient()
    try:
        token = client.get_user_token(scope=SELL_INVENTORY_SCOPE)
    except Exception as e:
        return {"error": str(e)}

    url = client.media_base.rstrip("/") + f"/commerce/media/v1_beta/document/{document_id}/upload"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f, "application/octet-stream")}
            resp = requests.post(url, headers=headers, files=files, timeout=300)
    except Exception as e:
        return {"error": str(e)}

    if resp.status_code >= 400:
        try:
            return {"error": resp.json(), "status_code": resp.status_code}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}

    try:
        return {"status_code": resp.status_code, **resp.json()}
    except Exception:
        return {"status_code": resp.status_code, "raw": resp.text}


def get_document(document_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/document/{document_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.media_base,
        f"/commerce/media/v1_beta/document/{document_id}",
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
    )


def create_document_from_url(document_type: str, languages: list[str], document_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/create_document_from_url"""
    client = EbayClient()
    return client.request(
        "POST",
        client.media_base,
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body={"documentType": document_type, "languages": languages, "documentUrl": document_url},
        headers={"Content-Type": "application/json"},
        auth="user",
        scope=SELL_INVENTORY_SCOPE,
        timeout=120,
    )
