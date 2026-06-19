from typing import Any, Dict, Optional

from .ebay_auth import auth_header, get_media_base_url, request_json


# Media API (user token; different base domain)


def create_upload_session(file_name: str, file_size: int, content_type: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/upload_session"""
    url = get_media_base_url() + "/commerce/media/v1_beta/upload_session"
    body = {"fileName": file_name, "fileSize": file_size, "contentType": content_type}
    res, err = request_json("POST", url, headers={**auth_header(user=True), "Content-Type": "application/json"}, json=body)
    return err or res  # type: ignore


def get_upload_session(upload_session_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/upload_session/{uploadSessionId}"""
    url = get_media_base_url() + f"/commerce/media/v1_beta/upload_session/{upload_session_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore


def upload_part(upload_session_id: str, part_sequence: int, data_b64: str) -> Dict[str, Any]:
    """PUT /commerce/media/v1_beta/upload_session/{uploadSessionId} (part upload)

    Expects base64-encoded bytes for the part.
    """
    import base64

    url = get_media_base_url() + f"/commerce/media/v1_beta/upload_session/{upload_session_id}"
    headers = {
        **auth_header(user=True),
        "Content-Type": "application/octet-stream",
        "Content-Range": f"bytes {part_sequence}-*/*",
    }
    raw = base64.b64decode(data_b64)
    res, err = request_json("PUT", url, headers=headers, data=raw)
    return err or res  # type: ignore


def complete_upload_session(upload_session_id: str) -> Dict[str, Any]:
    """POST /commerce/media/v1_beta/upload_session/{uploadSessionId}/complete"""
    url = get_media_base_url() + f"/commerce/media/v1_beta/upload_session/{upload_session_id}/complete"
    res, err = request_json("POST", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore


def get_asset(asset_id: str) -> Dict[str, Any]:
    """GET /commerce/media/v1_beta/asset/{assetId}"""
    url = get_media_base_url() + f"/commerce/media/v1_beta/asset/{asset_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore


def delete_asset(asset_id: str) -> Dict[str, Any]:
    """DELETE /commerce/media/v1_beta/asset/{assetId}"""
    url = get_media_base_url() + f"/commerce/media/v1_beta/asset/{asset_id}"
    res, err = request_json("DELETE", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore
