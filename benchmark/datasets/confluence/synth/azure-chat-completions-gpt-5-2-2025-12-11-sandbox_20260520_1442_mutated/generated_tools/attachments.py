from __future__ import annotations

import os
from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_attachments(*, cursor: Optional[str] = None, max_results: int = 25, filename: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/attachments"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    if filename:
        params["filename"] = filename
    status, body, headers = c.request("GET", "/api/v2/attachments", params=params)
    return ok_or_error(status, body, headers)


def list_page_attachments(page_id: int, *, cursor: Optional[str] = None, max_results: int = 25) -> Dict[str, Any]:
    """GET /api/v2/pages/{id}/attachments"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if cursor:
        params["cursor"] = cursor
    status, body, headers = c.request("GET", f"/api/v2/pages/{page_id}/attachments", params=params)
    return ok_or_error(status, body, headers)


def get_attachment(attachment_id: str) -> Dict[str, Any]:
    """GET /api/v2/attachments/{id}"""
    c = ConfluenceClient()
    status, body, headers = c.request("GET", f"/api/v2/attachments/{attachment_id}")
    return ok_or_error(status, body, headers)


def delete_attachment(attachment_id: int, *, purge: bool = False) -> Dict[str, Any]:
    """DELETE /api/v2/attachments/{id}"""
    c = ConfluenceClient()
    status, body, headers = c.request(
        "DELETE",
        f"/api/v2/attachments/{attachment_id}",
        params={"purge": str(purge).lower()},
    )
    return ok_or_error(status, body, headers)


def download_attachment_to_file(attachment_id: str, dest_path: str) -> Dict[str, Any]:
    """Downloads attachment binary using the attachment's downloadLink.

    Uses:
      - GET /api/v2/attachments/{id} to obtain downloadLink
      - then GET {downloadLink} (absolute or relative)

    Returns {"saved_to": dest_path, "bytes": n}
    """
    c = ConfluenceClient()
    meta = get_attachment(attachment_id)
    if meta.get("error"):
        return meta
    data = meta.get("data") or {}
    download_link = data.get("downloadLink") or (data.get("_links") or {}).get("download")
    if not download_link:
        return {"error": "attachment download link not found", "data": data}

    # downloadLink may be absolute or relative to /wiki
    if download_link.startswith("http://") or download_link.startswith("https://"):
        url = download_link
        path = None
    else:
        url = None
        path = download_link if download_link.startswith("/") else "/" + download_link

    # stream download
    import requests

    headers = {"Authorization": c._auth_header(), "Accept": "*/*"}
    try:
        if url:
            resp = requests.get(url, headers=headers, stream=True, timeout=c.timeout)
        else:
            resp = requests.get(c.base_url + path, headers=headers, stream=True, timeout=c.timeout)
    except requests.RequestException as e:
        return {"error": str(e)}

    if not (200 <= resp.status_code < 300):
        return {"error": "download failed", "status": resp.status_code, "data": resp.text}

    os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)
    n = 0
    with open(dest_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024 * 256):
            if chunk:
                f.write(chunk)
                n += len(chunk)
    return {"status": resp.status_code, "saved_to": dest_path, "bytes": n}
