from typing import Any, Dict, List, Optional

import requests

from generated_tools.catalog import client


MEDIA_BASE = "https://apim.sandbox.ebay.com" if client.base_url.endswith("sandbox.ebay.com") else "https://apim.ebay.com"
SELL_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def _media_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    data: Any = None,
) -> Dict[str, Any]:
    token_payload = client.get_user_token(SELL_SCOPE)
    if "error" in token_payload:
        return token_payload
    req_headers = {"Authorization": f"Bearer {token_payload['access_token']}"}
    if headers:
        req_headers.update(headers)
    try:
        response = requests.request(
            method,
            f"{MEDIA_BASE}{path}",
            params=params,
            json=json_body,
            data=data,
            headers=req_headers,
            timeout=300,
        )
        if response.content:
            try:
                payload: Any = response.json()
            except Exception:
                payload = {"text": response.text}
        else:
            payload = {}
        if response.status_code >= 400:
            return {"error": payload, "status_code": response.status_code}
        if isinstance(payload, dict):
            if response.headers.get("Location"):
                payload.setdefault("location", response.headers.get("Location"))
            return payload
        return {"data": payload}
    except Exception as exc:
        return {"error": str(exc)}


def create_document(document_type: str, languages: List[str]) -> Dict[str, Any]:
    return _media_request(
        "POST",
        "/commerce/media/v1_beta/document",
        json_body={"documentType": document_type, "languages": languages},
        headers={"Content-Type": "application/json"},
    )


def create_document_from_url(document_type: str, document_url: str, languages: List[str]) -> Dict[str, Any]:
    return _media_request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        json_body={"documentType": document_type, "documentUrl": document_url, "languages": languages},
        headers={"Content-Type": "application/json"},
    )


def get_document(document_id: str) -> Dict[str, Any]:
    return _media_request("GET", f"/commerce/media/v1_beta/document/{document_id}")


def upload_document(document_id: str, file_path: str, file_name: Optional[str] = None) -> Dict[str, Any]:
    token_payload = client.get_user_token(SELL_SCOPE)
    if "error" in token_payload:
        return token_payload
    try:
        with open(file_path, "rb") as fh:
            files = {"file": (file_name or file_path.split("/")[-1], fh)}
            response = requests.post(
                f"{MEDIA_BASE}/commerce/media/v1_beta/document/{document_id}/upload",
                headers={"Authorization": f"Bearer {token_payload['access_token']}"},
                files=files,
                timeout=300,
            )
            payload = response.json() if response.content else {}
            if response.status_code >= 400:
                return {"error": payload, "status_code": response.status_code}
            return payload
    except Exception as exc:
        return {"error": str(exc)}


def create_image_from_file(file_path: str, file_name: Optional[str] = None) -> Dict[str, Any]:
    token_payload = client.get_user_token(SELL_SCOPE)
    if "error" in token_payload:
        return token_payload
    try:
        with open(file_path, "rb") as fh:
            files = {"image": (file_name or file_path.split("/")[-1], fh)}
            response = requests.post(
                f"{MEDIA_BASE}/commerce/media/v1_beta/image/create_image_from_file",
                headers={"Authorization": f"Bearer {token_payload['access_token']}"},
                files=files,
                timeout=300,
            )
            payload = response.json() if response.content else {}
            if response.headers.get("Location") and isinstance(payload, dict):
                payload.setdefault("location", response.headers.get("Location"))
            if response.status_code >= 400:
                return {"error": payload, "status_code": response.status_code}
            return payload
    except Exception as exc:
        return {"error": str(exc)}


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    return _media_request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        json_body={"imageUrl": image_url},
        headers={"Content-Type": "application/json"},
    )


def get_image(image_id: str) -> Dict[str, Any]:
    return _media_request("GET", f"/commerce/media/v1_beta/image/{image_id}")


def create_video(title: str, size: int, classification: List[Dict[str, Any]], description: Optional[str] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"title": title, "size": size, "classification": classification}
    if description is not None:
        body["description"] = description
    return _media_request(
        "POST",
        "/commerce/media/v1_beta/video",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )


def get_video(video_id: str) -> Dict[str, Any]:
    return _media_request("GET", f"/commerce/media/v1_beta/video/{video_id}")


def upload_video(
    video_id: str,
    file_path: str,
    content_range: Optional[str] = None,
    content_length: Optional[int] = None,
) -> Dict[str, Any]:
    token_payload = client.get_user_token(SELL_SCOPE)
    if "error" in token_payload:
        return token_payload
    try:
        with open(file_path, "rb") as fh:
            headers = {
                "Authorization": f"Bearer {token_payload['access_token']}",
                "Content-Type": "application/octet-stream",
            }
            if content_range:
                headers["Content-Range"] = content_range
            if content_length is not None:
                headers["Content-Length"] = str(content_length)
            response = requests.post(
                f"{MEDIA_BASE}/commerce/media/v1_beta/video/{video_id}/upload",
                headers=headers,
                data=fh,
                timeout=1800,
            )
            payload = response.json() if response.content else {}
            if response.status_code >= 400:
                return {"error": payload, "status_code": response.status_code}
            return payload if isinstance(payload, dict) else {"data": payload, "status_code": response.status_code}
    except Exception as exc:
        return {"error": str(exc)}
