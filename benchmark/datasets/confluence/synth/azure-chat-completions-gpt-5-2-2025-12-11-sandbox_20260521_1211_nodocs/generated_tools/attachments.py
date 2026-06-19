from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v1_list_attachments(content_id: str, *, limit: int = 25, start: int = 0, expand: str = "") -> Any:
    """GET /rest/api/content/{id}/child/attachment"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": limit, "start": start}
    if expand:
        params["expand"] = expand
    return c.request("GET", f"/rest/api/content/{content_id}/child/attachment", params=params)


def v1_upload_attachment(
    content_id: str,
    *,
    filename: str,
    file_bytes_b64: str,
    comment: str = "",
    minor_edit: bool = True,
) -> Any:
    """POST /rest/api/content/{id}/child/attachment"""
    import base64

    c = ConfluenceClient()
    file_bytes = base64.b64decode(file_bytes_b64.encode("ascii"))
    files = {"file": (filename, file_bytes)}
    headers = {"X-Atlassian-Token": "no-check"}
    data = {"comment": comment, "minorEdit": str(minor_edit).lower()}
    return c.request(
        "POST",
        f"/rest/api/content/{content_id}/child/attachment",
        headers=headers,
        files=files,
        data=data,
        expected=(200, 201),
    )


def v1_download_attachment(download_url: str) -> Any:
    """GET {downloadUrl} (absolute)"""
    # download_url is typically a relative URL like /wiki/download/attachments/... or absolute.
    c = ConfluenceClient()
    if download_url.startswith("http"):
        url = download_url
    else:
        url = c.base_url.rstrip("/") + (download_url if download_url.startswith("/") else "/" + download_url)
    try:
        resp = c.session.get(url, timeout=60)
    except Exception as e:
        return {"error": str(e)}
    if resp.status_code != 200:
        return {"error": f"HTTP {resp.status_code}", "details": resp.text}
    import base64

    return {
        "content_type": resp.headers.get("Content-Type"),
        "filename": resp.headers.get("Content-Disposition"),
        "bytes_b64": base64.b64encode(resp.content).decode("ascii"),
    }
