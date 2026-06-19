"""
Confluence Cloud v2 Attachments tools + v1 upload.
Endpoints: GET /api/v2/attachments, GET/DEL /api/v2/attachments/{id},
           GET /api/v2/pages/{id}/attachments, GET /api/v2/blogposts/{id}/attachments,
           POST /wiki/rest/api/content/{id}/child/attachment (v1 upload)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def get_attachments(
    media_type: str | None = None,
    filename: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return all attachments, optionally filtered by media type or filename."""
    params: dict = {"max_results": max_results}
    if media_type:
        params["mediaType"] = media_type
    if filename:
        params["filename"] = filename
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2("/attachments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_attachment_by_id(
    attachment_id: str,
    include_labels: bool = False,
    include_properties: bool = False,
    include_versions: bool = False,
) -> dict:
    """Return a specific attachment by its ID."""
    params: dict = {}
    if include_labels:
        params["include-labels"] = "true"
    if include_properties:
        params["include-properties"] = "true"
    if include_versions:
        params["include-versions"] = "true"
    try:
        r = requests.get(_v2(f"/attachments/{attachment_id}"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def delete_attachment(attachment_id: str, purge: bool = False) -> dict:
    """Delete an attachment by ID. Set purge=True to permanently delete a trashed attachment."""
    params = {}
    if purge:
        params["purge"] = "true"
    try:
        r = requests.delete(_v2(f"/attachments/{attachment_id}"), params=params, auth=_auth(), timeout=30)
        if r.status_code == 204:
            return {"success": True, "message": f"Attachment {attachment_id} deleted."}
        r.raise_for_status()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_attachments(
    page_id: str,
    filename: str | None = None,
    media_type: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return attachments for a specific page."""
    params: dict = {"max_results": max_results}
    if filename:
        params["filename"] = filename
    if media_type:
        params["mediaType"] = media_type
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/pages/{page_id}/attachments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_attachments(
    blog_post_id: str,
    filename: str | None = None,
    media_type: str | None = None,
    cursor: str | None = None,
    max_results: int = 25,
) -> dict:
    """Return attachments for a specific blog post."""
    params: dict = {"max_results": max_results}
    if filename:
        params["filename"] = filename
    if media_type:
        params["mediaType"] = media_type
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/attachments"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def upload_attachment(
    content_id: str,
    file_path: str,
    comment: str = "",
    minor_edit: bool = True,
) -> dict:
    """
    Upload a file as an attachment to a page or blog post (v1 API).
    content_id: the page or blog post ID.
    file_path: local filesystem path to the file to upload.
    """
    url = _v1(f"/content/{content_id}/child/attachment")
    headers = {"X-Atlassian-Token": "no-check"}
    try:
        with open(file_path, "rb") as f:
            filename = os.path.basename(file_path)
            files = {"file": (filename, f)}
            data = {"comment": comment, "minorEdit": str(minor_edit).lower()}
            r = requests.post(
                url,
                headers=headers,
                files=files,
                data=data,
                auth=_auth(),
                timeout=60,
            )
        r.raise_for_status()
        return r.json()
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def download_attachment(attachment_id: str, output_path: str) -> dict:
    """
    Download an attachment by ID to a local file.
    First fetches the attachment metadata to get the download link, then downloads.
    """
    meta = get_attachment_by_id(attachment_id)
    if "error" in meta:
        return meta
    download_link = meta.get("downloadLink") or (meta.get("_links", {}).get("download"))
    if not download_link:
        return {"error": "No download link found in attachment metadata."}
    # download_link may be relative
    if download_link.startswith("/"):
        download_url = BASE_URL.rstrip("/wiki") + download_link
    else:
        download_url = download_link
    try:
        r = requests.get(download_url, auth=_auth(), timeout=60, stream=True)
        r.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return {"success": True, "output_path": output_path, "attachment_id": attachment_id}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code}
    except Exception as e:
        return {"error": str(e)}
