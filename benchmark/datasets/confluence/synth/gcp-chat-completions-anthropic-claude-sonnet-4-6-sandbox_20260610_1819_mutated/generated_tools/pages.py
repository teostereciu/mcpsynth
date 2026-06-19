"""Confluence v2 Pages API tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

def _auth():
    return (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])

def _base():
    return os.environ["CONFLUENCE_BASE_URL"].rstrip("/")

def _v2(path: str) -> str:
    return f"{_base()}/api/v2{path}"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_pages(
        space_id: str = None,
        title: str = None,
        content_status: str = None,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """List pages, optionally filtered by space, title, or status."""
        params = {"body-format": body_format, "max_results": max_results}
        if space_id:
            params["space-id"] = space_id
        if title:
            params["title"] = title
        if content_status:
            params["content_status"] = content_status
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2("/pages"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_page_by_id(
        page_id: int,
        body_format: str = "storage",
        include_labels: bool = False,
        include_properties: bool = False,
        include_versions: bool = False,
        version: int = None,
    ) -> dict:
        """Get a specific page by its ID."""
        params = {
            "body-format": body_format,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-versions": include_versions,
        }
        if version is not None:
            params["version"] = version
        try:
            r = requests.get(_v2(f"/pages/{page_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_page(
        space_id: str,
        title: str,
        body_value: str,
        body_representation: str = "storage",
        parent_id: str = None,
        content_status: str = "current",
    ) -> dict:
        """Create a new page in a space."""
        payload = {
            "spaceId": space_id,
            "title": title,
            "content_status": content_status,
            "body": {"representation": body_representation, "value": body_value},
        }
        if parent_id:
            payload["parentId"] = parent_id
        try:
            r = requests.post(_v2("/pages"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def update_page(
        page_id: int,
        title: str,
        body_value: str,
        version_number: int,
        body_representation: str = "storage",
        content_status: str = "current",
        version_message: str = "",
        parent_id: str = None,
    ) -> dict:
        """Update an existing page by ID. version_number must be current version + 1."""
        payload = {
            "id": str(page_id),
            "title": title,
            "content_status": content_status,
            "body": {"representation": body_representation, "value": body_value},
            "version": {"number": version_number, "message": version_message},
        }
        if parent_id:
            payload["parentId"] = parent_id
        try:
            r = requests.put(_v2(f"/pages/{page_id}"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_page(page_id: int, purge: bool = False, draft: bool = False) -> dict:
        """Delete a page by ID. Set purge=True to permanently delete a trashed page."""
        params = {}
        if purge:
            params["purge"] = "true"
        if draft:
            params["draft"] = "true"
        try:
            r = requests.delete(_v2(f"/pages/{page_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return {"status": "deleted", "page_id": page_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_pages_in_space(
        space_id: int,
        title: str = None,
        content_status: str = None,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all pages in a specific space."""
        params = {"body-format": body_format, "max_results": max_results}
        if title:
            params["title"] = title
        if content_status:
            params["content_status"] = content_status
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/spaces/{space_id}/pages"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def update_page_title(
        page_id: int,
        title: str,
        content_status: str = "current",
    ) -> dict:
        """Update only the title of a page."""
        payload = {"content_status": content_status, "title": title}
        try:
            r = requests.put(_v2(f"/pages/{page_id}/title"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_pages_for_label(
        label_id: int,
        space_id: str = None,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get pages associated with a specific label ID."""
        params = {"body-format": body_format, "max_results": max_results}
        if space_id:
            params["space-id"] = space_id
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/labels/{label_id}/pages"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
