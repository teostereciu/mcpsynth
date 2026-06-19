import os
from typing import Any, Dict, Optional

import requests

from .http import EbayAuth, get_base_url


AUTH = EbayAuth()


def _media_token() -> str:
    return AUTH.get_user_token("https://api.ebay.com/oauth/api_scope/sell.inventory")


def create_image_from_file(file_path: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_file (multipart/form-data)"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + "/commerce/media/v1_beta/image/create_image_from_file"
    if not os.path.exists(file_path):
        return {"error": "file_not_found", "file_path": file_path}

    try:
        with open(file_path, "rb") as f:
            files = {"image": (os.path.basename(file_path), f)}
            r = requests.post(url, headers={"Authorization": f"Bearer {token}"}, files=files, timeout=120)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    out: Dict[str, Any] = r.json() if r.text else {"ok": True}
    loc = r.headers.get("Location") or r.headers.get("location")
    if loc:
        out["location"] = loc
    return out


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/image/create_image_from_url"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + "/commerce/media/v1_beta/image/create_image_from_url"
    try:
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"},
            json={"imageUrl": image_url},
            timeout=60,
        )
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    out: Dict[str, Any] = r.json() if r.text else {"ok": True}
    loc = r.headers.get("Location") or r.headers.get("location")
    if loc:
        out["location"] = loc
    return out


def get_image(image_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/image/{image_id}"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/image/{image_id}"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"}, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return r.json()


def create_document(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + "/commerce/media/v1_beta/document"
    try:
        r = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"}, json=payload, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    out: Dict[str, Any] = r.json() if r.text else {"ok": True}
    loc = r.headers.get("Location") or r.headers.get("location")
    if loc:
        out["location"] = loc
    return out


def create_document_from_url(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/create_document_from_url"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + "/commerce/media/v1_beta/document/create_document_from_url"
    try:
        r = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"}, json=payload, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    out: Dict[str, Any] = r.json() if r.text else {"ok": True}
    loc = r.headers.get("Location") or r.headers.get("location")
    if loc:
        out["location"] = loc
    return out


def upload_document(document_id: str, file_path: str, content_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/document/{document_id}/upload_document (multipart/form-data)"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/document/{document_id}/upload_document"
    if not os.path.exists(file_path):
        return {"error": "file_not_found", "file_path": file_path}

    headers = {"Authorization": f"Bearer {token}"}
    try:
        with open(file_path, "rb") as f:
            files = {"document": (os.path.basename(file_path), f, content_type) if content_type else (os.path.basename(file_path), f)}
            r = requests.post(url, headers=headers, files=files, timeout=120)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return r.json() if r.text else {"ok": True}


def get_document(document_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/document/{document_id}"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/document/{document_id}"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"}, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return r.json()


def create_video(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + "/commerce/media/v1_beta/video"
    try:
        r = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"}, json=payload, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    out: Dict[str, Any] = r.json() if r.text else {"ok": True}
    loc = r.headers.get("Location") or r.headers.get("location")
    if loc:
        out["location"] = loc
    return out


def upload_video(video_id: str, file_path: str, content_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/video/{video_id}/upload_video (multipart/form-data)"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/video/{video_id}/upload_video"
    if not os.path.exists(file_path):
        return {"error": "file_not_found", "file_path": file_path}

    headers = {"Authorization": f"Bearer {token}"}
    try:
        with open(file_path, "rb") as f:
            files = {"video": (os.path.basename(file_path), f, content_type) if content_type else (os.path.basename(file_path), f)}
            r = requests.post(url, headers=headers, files=files, timeout=300)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return r.json() if r.text else {"ok": True}


def get_video(video_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/video/{video_id}"""
    token = _media_token()
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    url = get_base_url(is_media=True) + f"/commerce/media/v1_beta/video/{video_id}"
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"}, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return r.json()
