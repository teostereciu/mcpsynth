from typing import Any, Dict, Optional

import os
import requests

from .notion_client import DEFAULT_NOTION_VERSION, NOTION_BASE_URL, request_json


def file_uploads_create(*, mode: Optional[str] = None, filename: Optional[str] = None,
                        content_type: Optional[str] = None, number_of_parts: Optional[int] = None,
                        external_url: Optional[str] = None) -> Dict[str, Any]:
    """POST /v1/file_uploads

    Doc: docs/create-a-file-upload.md
    """
    body: Dict[str, Any] = {}
    if mode is not None:
        body["mode"] = mode
    if filename is not None:
        body["filename"] = filename
    if content_type is not None:
        body["content_type"] = content_type
    if number_of_parts is not None:
        body["number_of_parts"] = number_of_parts
    if external_url is not None:
        body["external_url"] = external_url
    return request_json("POST", "/file_uploads", json=body)


def file_uploads_send(file_upload_id: str, *, file_path: Optional[str] = None, data: Optional[bytes] = None,
                      filename: Optional[str] = None, content_type: Optional[str] = None,
                      part_number: Optional[int] = None) -> Dict[str, Any]:
    """POST /v1/file_uploads/{file_upload_id}/send

    Doc: docs/send-a-file-upload.md

    Provide either file_path or data.
    """
    if data is None and file_path is None:
        return {"error": "missing_file", "details": "Provide file_path or data"}

    if data is None:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
        except Exception as e:
            return {"error": "file_read_failed", "details": str(e)}

    if filename is None and file_path is not None:
        filename = os.path.basename(file_path)

    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"error": "missing_NOTION_API_KEY"}

    url = NOTION_BASE_URL + f"/file_uploads/{file_upload_id}/send"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": DEFAULT_NOTION_VERSION,
    }
    params: Dict[str, Any] = {}
    if part_number is not None:
        params["part_number"] = part_number

    files = {
        "file": (filename or "upload.bin", data, content_type or "application/octet-stream"),
    }

    try:
        resp = requests.post(url, headers=headers, params=params, files=files, timeout=120)
    except Exception as e:
        return {"error": "request_failed", "details": str(e)}

    try:
        payload = resp.json() if resp.content else {}
    except Exception:
        payload = {"raw": resp.text}

    if 200 <= resp.status_code < 300:
        return payload if isinstance(payload, dict) else {"result": payload}
    return {"error": "notion_api_error", "status": resp.status_code, "details": payload}


def file_uploads_complete(file_upload_id: str) -> Dict[str, Any]:
    """POST /v1/file_uploads/{file_upload_id}/complete

    Doc: docs/complete-a-file-upload.md
    """
    return request_json("POST", f"/file_uploads/{file_upload_id}/complete")


def file_uploads_retrieve(file_upload_id: str) -> Dict[str, Any]:
    """GET /v1/file_uploads/{file_upload_id}

    Doc: docs/retrieve-a-file-upload.md
    """
    return request_json("GET", f"/file_uploads/{file_upload_id}")


def file_uploads_list(*, status: Optional[str] = None, page_cursor: Optional[str] = None,
                      results_per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /v1/file_uploads

    Doc: docs/list-file-uploads.md
    """
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["results_per_page"] = results_per_page
    return request_json("GET", "/file_uploads", params=params)
