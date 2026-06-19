"""Confluence v2 Blog Posts API tools."""
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
    def get_blog_posts(
        space_id: str = None,
        title: str = None,
        content_status: str = None,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """List all blog posts, optionally filtered by space, title, or status."""
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
            r = requests.get(_v2("/blogposts"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_post_by_id(
        blog_post_id: int,
        body_format: str = "storage",
        include_labels: bool = False,
        include_properties: bool = False,
        include_versions: bool = False,
    ) -> dict:
        """Get a specific blog post by its ID."""
        params = {
            "body-format": body_format,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-versions": include_versions,
        }
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_blog_post(
        space_id: str,
        title: str,
        body_value: str,
        body_representation: str = "storage",
        content_status: str = "current",
    ) -> dict:
        """Create a new blog post in a space."""
        payload = {
            "spaceId": space_id,
            "title": title,
            "content_status": content_status,
            "body": {"representation": body_representation, "value": body_value},
        }
        try:
            r = requests.post(_v2("/blogposts"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def update_blog_post(
        blog_post_id: int,
        title: str,
        body_value: str,
        version_number: int,
        body_representation: str = "storage",
        content_status: str = "current",
        version_message: str = "",
        space_id: str = None,
    ) -> dict:
        """Update an existing blog post. version_number must be current version + 1."""
        payload = {
            "id": str(blog_post_id),
            "title": title,
            "content_status": content_status,
            "body": {"representation": body_representation, "value": body_value},
            "version": {"number": version_number, "message": version_message},
        }
        if space_id:
            payload["spaceId"] = space_id
        try:
            r = requests.put(_v2(f"/blogposts/{blog_post_id}"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_blog_post(blog_post_id: int, purge: bool = False, draft: bool = False) -> dict:
        """Delete a blog post by ID. Set purge=True to permanently delete a trashed post."""
        params = {}
        if purge:
            params["purge"] = "true"
        if draft:
            params["draft"] = "true"
        try:
            r = requests.delete(_v2(f"/blogposts/{blog_post_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return {"status": "deleted", "blog_post_id": blog_post_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_posts_in_space(
        space_id: int,
        title: str = None,
        content_status: str = None,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """Get all blog posts in a specific space."""
        params = {"body-format": body_format, "max_results": max_results}
        if title:
            params["title"] = title
        if content_status:
            params["content_status"] = content_status
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2(f"/spaces/{space_id}/blogposts"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
