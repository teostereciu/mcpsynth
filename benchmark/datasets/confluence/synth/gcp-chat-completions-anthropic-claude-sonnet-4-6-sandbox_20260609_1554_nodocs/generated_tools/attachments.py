"""
Confluence Cloud REST API — Attachments (v2 preferred)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, API_TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def _handle(resp: requests.Response) -> dict:
    try:
        data = resp.json()
    except Exception:
        data = {"raw": resp.text}
    if not resp.ok:
        return {"error": data, "status_code": resp.status_code}
    return data


def list_page_attachments(
    page_id: str,
    limit: int = 25,
    cursor: str = "",
    filename: str = "",
    media_type: str = "",
) -> dict:
    """List attachments on a page (v2).

    Args:
        page_id: The page ID.
        limit: Maximum number of results.
        cursor: Pagination cursor.
        filename: Filter by filename.
        media_type: Filter by media type (e.g. 'image/png').
    """
    params: dict = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if filename:
        params["filename"] = filename
    if media_type:
        params["mediaType"] = media_type
    resp = requests.get(_v2(f"/pages/{page_id}/attachments"), params=params, auth=_auth())
    return _handle(resp)


def upload_attachment_to_page(
    page_id: str,
    file_path: str,
    comment: str = "",
) -> dict:
    """Upload a file as an attachment to a page (v1).

    Args:
        page_id: The page ID to attach the file to.
        file_path: Local filesystem path to the file to upload.
        comment: Optional comment for the attachment.
    """
    if not os.path.isfile(file_path):
        return {"error": f"File not found: {file_path}"}

    filename = os.path.basename(file_path)
    headers = {"X-Atlassian-Token": "no-check"}
    with open(file_path, "rb") as fh:
        files = {"file": (filename, fh)}
        data = {}
        if comment:
            data["comment"] = comment
        resp = requests.post(
            _v1(f"/content/{page_id}/child/attachment"),
            files=files,
            data=data,
            headers=headers,
            auth=_auth(),
        )
    return _handle(resp)


def get_attachment_by_id(attachment_id: str) -> dict:
    """Get metadata for a specific attachment (v2).

    Args:
        attachment_id: The attachment ID.
    """
    resp = requests.get(_v2(f"/attachments/{attachment_id}"), auth=_auth())
    return _handle(resp)


def download_attachment(attachment_id: str, save_path: str) -> dict:
    """Download an attachment and save it to a local path (v1).

    Args:
        attachment_id: The attachment ID.
        save_path: Local filesystem path where the file should be saved.
    """
    # First get attachment metadata to find the download URL
    meta_resp = requests.get(
        _v1(f"/content/{attachment_id}"),
        params={"expand": "body.download"},
        auth=_auth(),
    )
    if not meta_resp.ok:
        return _handle(meta_resp)

    meta = meta_resp.json()
    download_url = (
        meta.get("_links", {}).get("download")
        or meta.get("body", {}).get("download", {}).get("value", "")
    )
    if not download_url:
        return {"error": "Could not determine download URL from attachment metadata"}

    if not download_url.startswith("http"):
        download_url = BASE_URL + download_url

    dl_resp = requests.get(download_url, auth=_auth(), stream=True)
    if not dl_resp.ok:
        return {"error": f"Download failed with status {dl_resp.status_code}"}

    os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
    with open(save_path, "wb") as fh:
        for chunk in dl_resp.iter_content(chunk_size=8192):
            fh.write(chunk)
    return {"success": True, "saved_to": save_path}


def delete_attachment(attachment_id: str) -> dict:
    """Delete an attachment by ID (v1).

    Args:
        attachment_id: The attachment ID to delete.
    """
    resp = requests.delete(_v1(f"/content/{attachment_id}"), auth=_auth())
    if resp.status_code == 204:
        return {"success": True}
    return _handle(resp)
