"""Confluence v2 Comments API tools (footer + inline)."""
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

    # ── Footer comments ──────────────────────────────────────────────────────

    @mcp.tool()
    def get_footer_comments(
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all footer comments across the site."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2("/footer-comments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_footer_comment(
        body_value: str,
        body_representation: str = "storage",
        page_id: str = None,
        blog_post_id: str = None,
        parent_comment_id: str = None,
    ) -> dict:
        """Create a footer comment on a page, blog post, or as a reply to another comment."""
        payload: dict = {
            "body": {"representation": body_representation, "value": body_value}
        }
        if page_id:
            payload["pageId"] = page_id
        if blog_post_id:
            payload["blogPostId"] = blog_post_id
        if parent_comment_id:
            payload["parentCommentId"] = parent_comment_id
        try:
            r = requests.post(_v2("/footer-comments"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_footer_comment_by_id(comment_id: str, body_format: str = "storage") -> dict:
        """Get a specific footer comment by its ID."""
        params = {"body-format": body_format}
        try:
            r = requests.get(_v2(f"/footer-comments/{comment_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def update_footer_comment(
        comment_id: str,
        body_value: str,
        version_number: int,
        body_representation: str = "storage",
        version_message: str = "",
    ) -> dict:
        """Update an existing footer comment."""
        payload = {
            "body": {"representation": body_representation, "value": body_value},
            "version": {"number": version_number, "message": version_message},
        }
        try:
            r = requests.put(_v2(f"/footer-comments/{comment_id}"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_footer_comment(comment_id: str) -> dict:
        """Delete a footer comment by its ID."""
        try:
            r = requests.delete(_v2(f"/footer-comments/{comment_id}"), auth=_auth())
            r.raise_for_status()
            return {"status": "deleted", "comment_id": comment_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_page_footer_comments(
        page_id: int,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all footer comments for a specific page."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/pages/{page_id}/footer-comments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_page_inline_comments(
        page_id: int,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all inline comments for a specific page."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/pages/{page_id}/inline-comments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_post_footer_comments(
        blog_post_id: int,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all footer comments for a specific blog post."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}/footer-comments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_blog_post_inline_comments(
        blog_post_id: int,
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all inline comments for a specific blog post."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2(f"/blogposts/{blog_post_id}/inline-comments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    # ── Inline comments ───────────────────────────────────────────────────────

    @mcp.tool()
    def get_inline_comments(
        body_format: str = "storage",
        cursor: str = None,
        max_results: int = 25,
        sort: str = None,
    ) -> dict:
        """Get all inline comments across the site."""
        params = {"body-format": body_format, "max_results": max_results}
        if cursor:
            params["cursor"] = cursor
        if sort:
            params["sort"] = sort
        try:
            r = requests.get(_v2("/inline-comments"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_inline_comment(
        body_value: str,
        body_representation: str = "storage",
        page_id: str = None,
        blog_post_id: str = None,
        inline_marker_ref: str = None,
        inline_original_selection: str = None,
    ) -> dict:
        """Create an inline comment on a page or blog post.
        Provide inline_marker_ref and inline_original_selection to anchor the comment."""
        payload: dict = {
            "body": {"representation": body_representation, "value": body_value}
        }
        if page_id:
            payload["pageId"] = page_id
        if blog_post_id:
            payload["blogPostId"] = blog_post_id
        if inline_marker_ref or inline_original_selection:
            payload["inlineCommentProperties"] = {}
            if inline_marker_ref:
                payload["inlineCommentProperties"]["textSelection"] = inline_marker_ref
            if inline_original_selection:
                payload["inlineCommentProperties"]["textSelectionMatchCount"] = inline_original_selection
        try:
            r = requests.post(_v2("/inline-comments"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_inline_comment_by_id(comment_id: str, body_format: str = "storage") -> dict:
        """Get a specific inline comment by its ID."""
        params = {"body-format": body_format}
        try:
            r = requests.get(_v2(f"/inline-comments/{comment_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_inline_comment(comment_id: str) -> dict:
        """Delete an inline comment by its ID."""
        try:
            r = requests.delete(_v2(f"/inline-comments/{comment_id}"), auth=_auth())
            r.raise_for_status()
            return {"status": "deleted", "comment_id": comment_id}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
