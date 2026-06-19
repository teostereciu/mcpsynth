"""Confluence v2 Attachments API tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

def _auth():
    return (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])

def _base():
    return os.environ["CONFLUENCE_BASE_URL"].rstrip("/")

def _v2(path: str) -> str:
    return f"{_base()}/api/v2{path}"

def _v1(path: str) -> str:
    return f"{_base()}/rest/api{path}"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_attachments(
        filename: str = None,
        media_type: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """List all attachments, optionally filtered by filename or media type."""
        params = {"max_results": max_results}
        if filename:
            params["filename"] = filename
        if media_type:
            params["mediaType"] = media_type
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2("/attachments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_attachment_by_id(
        attachment_id: str,
        include_labels: bool = False,
        include_properties: bool = False,
        include_versions: bool = False,
        version: int = None,
    ) -> dict:
        """Get a specific attachment by its ID."""
        params = {
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-versions": include_versions,
        }
        if version is not None:
            params["version"] = version
        try:
            r = requests.get(_v2(f"/attachments/{attachment_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_attachment(attachment_id: int, purge: bool = False) -> dict:
        """Delete an attachment by ID. Set purge=True to permanently delete a trashed attachment."""
        params = {}
        if purge:
            params["purge"] = "true"
        try:
            r = requests.delete(_v2(f"/attachments/{attachment_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return {"status": "deleted", "attachment_id": attachment_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_attachments_for_page(
        page_id: int,
        filename: str = None,
        media_type: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all attachments for a specific page."""
        params = {"max_results": max_results}
        if filename:
            params["filename"] = filename
        if media_type:
            params["mediaType"] = media_type
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/pages/{page_id}/attachments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_attachments_for_blog_post(
        blog_post_id: int,
        filename: str = None,
        media_type: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all attachments for a specific blog post."""
        params = {"max_results": max_results}
        if filename:
            params["filename"] = filename
        if media_type:
            params["mediaType"] = media_type
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}/attachments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def upload_attachment_to_page(
        page_id: int,
        file_path: str,
        comment: str = "",
    ) -> dict:
        """Upload a file as an attachment to a page (uses v1 API)."""
        try:
            with open(file_path, "rb") as f:
                filename = os.path.basename(file_path)
                files = {"file": (filename, f)}
                data = {"comment": comment} if comment else {}
                headers = {"X-Atlassian-Token": "no-check"}
                r = requests.post(
                    _v1(f"/content/{page_id}/child/attachment"),
                    files=files,
                    data=data,
                    headers=headers,
                    auth=_auth(),
                )
                r.raise_for_status()
                return r.json()
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def download_attachment(attachment_id: str, save_path: str) -> dict:
        """Download an attachment's binary content and save it to a local file path."""
        try:
            # First get the attachment metadata to find the download link
            meta_r = requests.get(_v2(f"/attachments/{attachment_id}"), auth=_auth())
            meta_r.raise_for_status()
            meta = meta_r.json()
            download_link = meta.get("downloadLink") or (meta.get("_links", {}).get("download"))
            if not download_link:
                return {"error": "No download link found in attachment metadata"}
            # download_link may be relative
            if download_link.startswith("/"):
                download_url = _base().rstrip("/wiki") + download_link
            else:
                download_url = download_link
            r = requests.get(download_url, auth=_auth(), stream=True)
            r.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return {"status": "downloaded", "save_path": save_path, "attachment_id": attachment_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
        except OSError as e:
            return {"error": str(e)}
