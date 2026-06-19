from typing import Any, Dict, Optional

from generated_tools.pages import _request


def create_file_upload(mode: str = "single_part", filename: Optional[str] = None, content_type: Optional[str] = None, number_of_parts: Optional[int] = None, external_url: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"mode": mode}
    if filename is not None:
        body["filename"] = filename
    if content_type is not None:
        body["content_type"] = content_type
    if number_of_parts is not None:
        body["number_of_parts"] = number_of_parts
    if external_url is not None:
        body["external_url"] = external_url
    return _request("POST", "/file_uploads", json_body=body)


def complete_file_upload(file_upload_id: str) -> Any:
    return _request("POST", f"/file_uploads/{file_upload_id}/complete")


def retrieve_file_upload(file_upload_id: str) -> Any:
    return _request("GET", f"/file_uploads/{file_upload_id}")


def list_file_uploads(status: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", "/file_uploads", params=params or None)
