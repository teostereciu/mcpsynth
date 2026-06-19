import base64
from typing import Any, Dict, Optional

from ._client import request_json


def file_uploads_create(
    *,
    mode: str = "single_part",
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    number_of_parts: Optional[int] = None,
    external_url: Optional[str] = None,
) -> Any:
    body: Dict[str, Any] = {"mode": mode}
    if filename is not None:
        body["filename"] = filename
    if content_type is not None:
        body["content_type"] = content_type
    if number_of_parts is not None:
        body["number_of_parts"] = number_of_parts
    if external_url is not None:
        body["external_url"] = external_url
    return request_json("POST", "/file_uploads", json=body)


def file_uploads_send(
    file_upload_id: str,
    *,
    filename: str,
    data_base64: str,
    content_type: Optional[str] = None,
    part_number: Optional[int] = None,
) -> Any:
    # Notion's send endpoint expects multipart/binary; for MCP JSON transport we accept base64.
    # The API docs show SDK usage; we implement a JSON-friendly wrapper that uses raw bytes.
    raw = base64.b64decode(data_base64)
    headers: Dict[str, str] = {}
    if content_type:
        headers["Content-Type"] = content_type
    params: Dict[str, Any] = {"filename": filename}
    if part_number is not None:
        params["part_number"] = part_number
    return request_json(
        "POST",
        f"/file_uploads/{file_upload_id}/send",
        params=params,
        data=raw,
        headers=headers,
    )


def file_uploads_complete(file_upload_id: str) -> Any:
    return request_json("POST", f"/file_uploads/{file_upload_id}/complete", json={})


def file_uploads_retrieve(file_upload_id: str) -> Any:
    return request_json("GET", f"/file_uploads/{file_upload_id}")


def file_uploads_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/file_uploads", params=params or None)
