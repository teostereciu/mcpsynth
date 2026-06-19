from typing import Any, Dict, Optional

from .notion_client import NotionClient


def file_uploads_send(
    file_upload_id: str,
    *,
    file_path: Optional[str] = None,
    file_bytes_b64: Optional[str] = None,
    part_number: Optional[int] = None,
    content_type: Optional[str] = None,
    filename: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/file_uploads/{file_upload_id}/send

    Doc: docs/send-a-file-upload.md

    Provide either file_path or file_bytes_b64.
    """
    import base64
    import os

    if (file_path is None) == (file_bytes_b64 is None):
        return {"error": "Provide exactly one of file_path or file_bytes_b64"}

    if file_path is not None:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
        except OSError as e:
            return {"error": str(e)}
        if filename is None:
            filename = os.path.basename(file_path)
    else:
        try:
            data = base64.b64decode(file_bytes_b64 or "", validate=True)
        except Exception as e:
            return {"error": f"Invalid base64: {e}"}
        if filename is None:
            filename = "upload.bin"

    # Notion's send endpoint expects raw binary body; however, our NotionClient always sends JSON.
    # Implement this call directly with requests.
    client = NotionClient()
    headers = client._headers()
    if "error" in headers:
        return headers  # type: ignore[return-value]

    # Override content-type for binary upload.
    if content_type:
        headers["Content-Type"] = content_type
    else:
        headers.pop("Content-Type", None)

    params: Dict[str, Any] = {}
    if part_number is not None:
        params["part_number"] = part_number

    import requests

    url = "https://api.notion.com/v1" + f"/file_uploads/{file_upload_id}/send"
    try:
        resp = requests.post(url, headers=headers, params=params or None, data=data, timeout=120)
    except requests.RequestException as e:
        return {"error": str(e)}

    try:
        out = resp.json()
    except ValueError:
        out = {"raw": resp.text}

    if resp.status_code >= 400:
        return {"error": "Notion API error", "status": resp.status_code, "data": out}
    return out if isinstance(out, dict) else {"data": out}



def file_uploads_complete(file_upload_id: str) -> Dict[str, Any]:
    """POST /v1/file_uploads/{file_upload_id}/complete

    Doc: docs/complete-a-file-upload.md
    """
    client = NotionClient()
    return client.request("POST", f"/file_uploads/{file_upload_id}/complete")



def file_uploads_retrieve(file_upload_id: str) -> Dict[str, Any]:
    """GET /v1/file_uploads/{file_upload_id}

    Doc: docs/retrieve-a-file-upload.md
    """
    client = NotionClient()
    return client.request("GET", f"/file_uploads/{file_upload_id}")



def file_uploads_list(
    *,
    status: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/file_uploads

    Doc: docs/list-file-uploads.md
    """
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient()
    return client.request("GET", "/file_uploads", params=params or None)



def file_uploads_create(
    *,
    mode: Optional[str] = None,
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    number_of_parts: Optional[int] = None,
    external_url: Optional[str] = None,
) -> Dict[str, Any]:
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

    client = NotionClient()
    return client.request("POST", "/file_uploads", json_body=body or None)
