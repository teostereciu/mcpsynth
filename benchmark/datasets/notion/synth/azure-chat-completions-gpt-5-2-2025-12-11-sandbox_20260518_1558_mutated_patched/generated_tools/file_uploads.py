import base64
from typing import Any, Dict, Optional

import requests

from .http_client import request_json, _headers


def file_uploads_create(*, mode: str = "single_part", filename: Optional[str] = None, content_type: Optional[str] = None,
                        number_of_parts: Optional[int] = None, external_url: Optional[str] = None) -> Dict[str, Any]:
    """POST /file_uploads"""
    body: Dict[str, Any] = {"mode": mode}
    if filename is not None:
        body["filename"] = filename
    if content_type is not None:
        body["content_type"] = content_type
    if number_of_parts is not None:
        body["number_of_parts"] = number_of_parts
    if external_url is not None:
        body["external_url"] = external_url
    return request_json("POST", "/file_uploads", json_body=body)


def file_uploads_send(file_upload_id: str, *, file_b64: str, filename: Optional[str] = None, content_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /file_uploads/{file_upload_id}/send

    This endpoint uploads binary data. To keep MCP JSON-serializable, accept base64.
    """
    # First retrieve upload_url
    meta = request_json("GET", f"/file_uploads/{file_upload_id}")
    if "error" in meta:
        return meta
    upload_url = meta.get("upload_url")
    if not upload_url:
        return {"error": "missing upload_url on file upload object"}

    try:
        data = base64.b64decode(file_b64)
    except Exception as e:
        return {"error": f"invalid_base64: {e}"}

    hdrs = _headers()
    # Notion upload_url is pre-signed; auth headers may be ignored but safe.
    if content_type:
        hdrs = dict(hdrs)
        hdrs["Content-Type"] = content_type

    files = {"file": (filename or meta.get("filename") or "upload.bin", data, content_type or meta.get("content_type") or "application/octet-stream")}

    try:
        resp = requests.post(upload_url, headers=hdrs, files=files, timeout=120)
    except requests.RequestException as e:
        return {"error": f"upload_failed: {e}"}

    if 200 <= resp.status_code < 300:
        # Some upload endpoints return empty body
        try:
            return resp.json()
        except ValueError:
            return {"status": resp.status_code, "ok": True}

    return {"error": {"status": resp.status_code, "message": resp.text}}


def file_uploads_complete(file_upload_id: str) -> Dict[str, Any]:
    """POST /file_uploads/{file_upload_id}/complete"""
    return request_json("POST", f"/file_uploads/{file_upload_id}/complete", json_body={})


def file_uploads_retrieve(file_upload_id: str) -> Dict[str, Any]:
    """GET /file_uploads/{file_upload_id}"""
    return request_json("GET", f"/file_uploads/{file_upload_id}")


def file_uploads_list(*, status: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /file_uploads"""
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/file_uploads", params=params or None)
