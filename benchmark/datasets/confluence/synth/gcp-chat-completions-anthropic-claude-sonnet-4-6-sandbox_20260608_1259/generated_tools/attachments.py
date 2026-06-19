"""
Confluence Cloud v2 API — Attachments tools.
"""
import os
import requests
from typing import Optional

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def _auth():
    return (EMAIL, API_TOKEN)

def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"

def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"

def _handle(resp: requests.Response):
    if resp.status_code in (200, 201):
        try:
            return resp.json()
        except Exception:
            return {"status": resp.status_code}
    if resp.status_code == 204:
        return {"status": "deleted"}
    try:
        return {"error": resp.json()}
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}


def get_attachments(
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get all attachments (v2). Optionally filter by media_type or filename.
    """
    params: dict = {"limit": limit}
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2("/attachments"), params=params, auth=_auth())
    return _handle(resp)


def get_attachment_by_id(
    attachment_id: str,
    version: Optional[int] = None,
    include_labels: bool = False,
    include_properties: bool = False,
    include_versions: bool = False,
) -> dict:
    """
    Get a specific attachment by ID (v2).
    """
    params: dict = {}
    if version is not None:
        params["version"] = version
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_versions:
        params["include-versions"] = "true"
    resp = requests.get(_v2(f"/attachments/{attachment_id}"), params=params, auth=_auth())
    return _handle(resp)


def delete_attachment(attachment_id: str, purge: bool = False) -> dict:
    """
    Delete an attachment by ID (v2). Set purge=True to permanently delete a trashed attachment.
    """
    params: dict = {}
    if purge:
        params["purge"] = "true"
    resp = requests.delete(_v2(f"/attachments/{attachment_id}"), params=params, auth=_auth())
    return _handle(resp)


def get_page_attachments(
    page_id: str,
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get attachments for a specific page (v2).
    """
    params: dict = {"limit": limit}
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/pages/{page_id}/attachments"), params=params, auth=_auth())
    return _handle(resp)


def get_blog_post_attachments(
    blog_post_id: str,
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
) -> dict:
    """
    Get attachments for a specific blog post (v2).
    """
    params: dict = {"limit": limit}
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    if cursor:
        params["cursor"] = cursor
    resp = requests.get(_v2(f"/blogposts/{blog_post_id}/attachments"), params=params, auth=_auth())
    return _handle(resp)


def upload_attachment(
    page_id: str,
    file_path: str,
    comment: Optional[str] = None,
    minor_edit: bool = False,
) -> dict:
    """
    Upload an attachment to a page (v1).
    file_path: local filesystem path to the file to upload.
    comment: optional comment for the attachment.
    """
    url = _v1(f"/content/{page_id}/child/attachment")
    headers = {
        "X-Atlassian-Token": "no-check",
    }
    params: dict = {}
    if minor_edit:
        params["minorEdit"] = "true"
    try:
        with open(file_path, "rb") as f:
            filename = os.path.basename(file_path)
            files = {"file": (filename, f)}
            data = {}
            if comment:
                data["comment"] = comment
            resp = requests.post(
                url,
                headers=headers,
                files=files,
                data=data if data else None,
                params=params,
                auth=_auth(),
            )
        return _handle(resp)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}


def download_attachment(attachment_id: str, output_path: str) -> dict:
    """
    Download an attachment by ID and save to output_path.
    First fetches attachment metadata to get the download link, then downloads.
    """
    meta = get_attachment_by_id(attachment_id)
    if "error" in meta:
        return meta
    download_link = meta.get("downloadLink") or meta.get("_links", {}).get("download")
    if not download_link:
        return {"error": "No download link found in attachment metadata"}
    # download_link may be relative
    if download_link.startswith("/"):
        download_url = BASE_URL.rstrip("/wiki") + download_link
    else:
        download_url = download_link
    try:
        resp = requests.get(download_url, auth=_auth(), stream=True)
        if resp.status_code == 200:
            with open(output_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return {"status": "downloaded", "path": output_path}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
