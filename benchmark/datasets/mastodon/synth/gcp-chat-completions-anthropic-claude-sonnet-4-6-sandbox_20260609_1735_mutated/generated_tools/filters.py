"""Mastodon filters API tools (v2)."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register(mcp: FastMCP):

    @mcp.tool()
    def get_filters() -> list:
        """Get all content filters for the authenticated user (v2)."""
        try:
            resp = requests.get(_api("/api/v2/filters"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_filter(filter_id: str) -> dict:
        """Get a single content filter by ID.

        Args:
            filter_id: The ID of the filter.
        """
        try:
            resp = requests.get(_api(f"/api/v2/filters/{filter_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_filter(
        title: str,
        context: list,
        filter_action: Optional[str] = None,
        expires_in: Optional[int] = None,
        keywords: Optional[list] = None,
    ) -> dict:
        """Create a new content filter.

        Args:
            title: The name of the filter group.
            context: Where to apply the filter. List of: 'home', 'notifications', 'public', 'thread', 'account'.
            filter_action: Policy when matched: 'warn', 'hide', or 'blur'.
            expires_in: Seconds until filter expires (omit for never).
            keywords: List of dicts with 'keyword' and optional 'whole_word' keys.
        """
        try:
            data = [("title", title)]
            for ctx in context:
                data.append(("context[]", ctx))
            if filter_action:
                data.append(("filter_action", filter_action))
            if expires_in is not None:
                data.append(("expires_in", expires_in))
            if keywords:
                for kw in keywords:
                    data.append(("keywords_attributes[][keyword]", kw.get("keyword", "")))
                    data.append(("keywords_attributes[][whole_word]", str(kw.get("whole_word", False)).lower()))
            resp = requests.post(_api("/api/v2/filters"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_filter(
        filter_id: str,
        title: Optional[str] = None,
        context: Optional[list] = None,
        filter_action: Optional[str] = None,
        expires_in: Optional[int] = None,
    ) -> dict:
        """Update an existing content filter.

        Args:
            filter_id: The ID of the filter to update.
            title: New name for the filter group.
            context: New context list: 'home', 'notifications', 'public', 'thread', 'account'.
            filter_action: New policy: 'warn', 'hide', or 'blur'.
            expires_in: New expiry in seconds from now.
        """
        try:
            data = []
            if title:
                data.append(("title", title))
            if context:
                for ctx in context:
                    data.append(("context[]", ctx))
            if filter_action:
                data.append(("filter_action", filter_action))
            if expires_in is not None:
                data.append(("expires_in", expires_in))
            resp = requests.put(_api(f"/api/v2/filters/{filter_id}"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_filter(filter_id: str) -> dict:
        """Delete a content filter.

        Args:
            filter_id: The ID of the filter to delete.
        """
        try:
            resp = requests.delete(_api(f"/api/v2/filters/{filter_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_filter_keywords(filter_id: str) -> list:
        """Get all keywords in a filter group.

        Args:
            filter_id: The ID of the filter.
        """
        try:
            resp = requests.get(_api(f"/api/v2/filters/{filter_id}/keywords"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def add_filter_keyword(filter_id: str, keyword: str, whole_word: Optional[bool] = None) -> dict:
        """Add a keyword to a filter group.

        Args:
            filter_id: The ID of the filter.
            keyword: The keyword string to add.
            whole_word: Whether to match whole words only.
        """
        try:
            data = {"keyword": keyword}
            if whole_word is not None:
                data["whole_word"] = str(whole_word).lower()
            resp = requests.post(_api(f"/api/v2/filters/{filter_id}/keywords"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_filter_keyword(keyword_id: str) -> dict:
        """Remove a keyword from a filter.

        Args:
            keyword_id: The ID of the filter keyword to delete.
        """
        try:
            resp = requests.delete(_api(f"/api/v2/filters/keywords/{keyword_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
