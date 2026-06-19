"""Confluence v2 Versions API tools."""
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
    def get_page_versions(
        page_id: int,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all versions of a specific page."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/pages/{page_id}/versions"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_page_version_details(page_id: int, version_number: int) -> dict:
        """Get detailed information about a specific version of a page."""
        try:
            r = requests.get(
                _v2(f"/pages/{page_id}/versions/{version_number}"),
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def restore_page_version(page_id: int, version_number: int, message: str = "") -> dict:
        """Restore a page to a specific historical version (uses v1 API).
        Creates a new version with the content of the specified historical version."""
        payload = {
            "operationKey": "restore",
            "params": {"versionNumber": version_number, "message": message, "restoreTitle": True},
        }
        try:
            r = requests.post(
                _v1(f"/content/{page_id}/version"),
                json=payload,
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_post_versions(
        blog_post_id: int,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all versions of a specific blog post."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}/versions"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_post_version_details(blog_post_id: int, version_number: int) -> dict:
        """Get detailed information about a specific version of a blog post."""
        try:
            r = requests.get(
                _v2(f"/blogposts/{blog_post_id}/versions/{version_number}"),
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_attachment_versions(
        attachment_id: str,
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all versions of a specific attachment."""
        params = {"max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/attachments/{attachment_id}/versions"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_attachment_version_details(attachment_id: str, version_number: int) -> dict:
        """Get detailed information about a specific version of an attachment."""
        try:
            r = requests.get(
                _v2(f"/attachments/{attachment_id}/versions/{version_number}"),
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
