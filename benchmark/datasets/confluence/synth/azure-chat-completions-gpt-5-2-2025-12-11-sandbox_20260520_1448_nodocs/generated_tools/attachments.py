from typing import Any, Dict, Optional

from .http import confluence_request


def list_attachments(page_id: int, limit: int = 25, start: int = 0) -> Dict[str, Any]:
    params = {"limit": limit, "start": start}
    return confluence_request("GET", f"/rest/api/content/{page_id}/child/attachment", params=params)


def upload_attachment(page_id: int, filename: str, content_bytes_b64: str, comment: str = "") -> Dict[str, Any]:
    import base64
    data = base64.b64decode(content_bytes_b64.encode("utf-8"))
    files = {"file": (filename, data)}
    headers = {"X-Atlassian-Token": "no-check"}
    params = {"comment": comment} if comment else None
    return confluence_request(
        "POST",
        f"/rest/api/content/{page_id}/child/attachment",
        params=params,
        headers=headers,
        files=files,
    )


def download_attachment(download_url: str) -> Dict[str, Any]:
    # download_url is typically a relative URL like /wiki/download/attachments/... or absolute.
    # We return text for non-binary; for binary, caller should use the URL.
    if download_url.startswith("http"):
        # strip base if same site
        return {"url": download_url}
    return {"url": download_url}


def get_attachment(attachment_id: int) -> Dict[str, Any]:
    return confluence_request("GET", f"/rest/api/content/{attachment_id}", params={"expand": "version,metadata"})
