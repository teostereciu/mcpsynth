"""Confluence v2 Content Properties API tools."""
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
    def get_page_properties(
        page_id: int,
        key: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all content properties for a specific page."""
        params = {"max_results": max_results}
        if key:
            params["key"] = key
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/pages/{page_id}/properties"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_page_property_by_id(page_id: int, property_id: int) -> dict:
        """Get a specific content property for a page by property ID."""
        try:
            r = requests.get(_v2(f"/pages/{page_id}/properties/{property_id}"), auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_page_property(page_id: int, key: str, value) -> dict:
        """Create a new content property on a page. value can be any JSON-serializable type."""
        payload = {"key": key, "value": value}
        try:
            r = requests.post(_v2(f"/pages/{page_id}/properties"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def update_page_property(
        page_id: int,
        property_id: int,
        key: str,
        value,
        version_number: int,
        version_message: str = "",
    ) -> dict:
        """Update an existing content property on a page."""
        payload = {
            "key": key,
            "value": value,
            "version": {"number": version_number, "message": version_message},
        }
        try:
            r = requests.put(
                _v2(f"/pages/{page_id}/properties/{property_id}"),
                json=payload,
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_page_property(page_id: int, property_id: int) -> dict:
        """Delete a content property from a page."""
        try:
            r = requests.delete(
                _v2(f"/pages/{page_id}/properties/{property_id}"),
                auth=_auth(),
            )
            r.raise_for_status()
            return {"status": "deleted", "page_id": page_id, "property_id": property_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_post_properties(
        blog_post_id: int,
        key: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all content properties for a specific blog post."""
        params = {"max_results": max_results}
        if key:
            params["key"] = key
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}/properties"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_blog_post_property(blog_post_id: int, key: str, value) -> dict:
        """Create a new content property on a blog post."""
        payload = {"key": key, "value": value}
        try:
            r = requests.post(_v2(f"/blogposts/{blog_post_id}/properties"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def update_blog_post_property(
        blog_post_id: int,
        property_id: int,
        key: str,
        value,
        version_number: int,
        version_message: str = "",
    ) -> dict:
        """Update an existing content property on a blog post."""
        payload = {
            "key": key,
            "value": value,
            "version": {"number": version_number, "message": version_message},
        }
        try:
            r = requests.put(
                _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"),
                json=payload,
                auth=_auth(),
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_blog_post_property(blog_post_id: int, property_id: int) -> dict:
        """Delete a content property from a blog post."""
        try:
            r = requests.delete(
                _v2(f"/blogposts/{blog_post_id}/properties/{property_id}"),
                auth=_auth(),
            )
            r.raise_for_status()
            return {"status": "deleted", "blog_post_id": blog_post_id, "property_id": property_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
