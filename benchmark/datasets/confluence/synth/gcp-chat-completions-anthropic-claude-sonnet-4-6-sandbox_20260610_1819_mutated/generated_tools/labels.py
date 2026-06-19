"""Confluence v1+v2 Labels API tools."""
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
    def get_labels(
        prefix: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """List all labels, optionally filtered by prefix."""
        params = {"max_results": max_results}
        if prefix:
            params["prefix"] = prefix
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2("/labels"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_labels_for_page(
        page_id: int,
        prefix: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all labels for a specific page."""
        params = {"max_results": max_results}
        if prefix:
            params["prefix"] = prefix
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/pages/{page_id}/labels"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def add_labels_to_page(page_id: int, labels: list) -> dict:
        """Add one or more labels to a page. labels is a list of label name strings.
        Uses v1 API: POST /rest/api/content/{id}/label"""
        payload = [{"prefix": "global", "name": lbl} for lbl in labels]
        try:
            r = requests.post(
                _v1(f"/content/{page_id}/label"),
                json=payload,
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def remove_label_from_page(page_id: int, label_name: str) -> dict:
        """Remove a label from a page by label name. Uses v1 API."""
        try:
            r = requests.delete(
                _v1(f"/content/{page_id}/label/{label_name}"),
                auth=_auth(),
            )
            r.raise_for_status()
            return {"status": "removed", "page_id": page_id, "label": label_name}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_labels_for_blog_post(
        blog_post_id: int,
        prefix: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all labels for a specific blog post."""
        params = {"max_results": max_results}
        if prefix:
            params["prefix"] = prefix
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}/labels"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_labels_for_space(
        space_id: int,
        prefix: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all labels for a specific space."""
        params = {"max_results": max_results}
        if prefix:
            params["prefix"] = prefix
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/spaces/{space_id}/labels"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_labels_for_attachment(
        attachment_id: int,
        prefix: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all labels for a specific attachment."""
        params = {"max_results": max_results}
        if prefix:
            params["prefix"] = prefix
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/attachments/{attachment_id}/labels"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
