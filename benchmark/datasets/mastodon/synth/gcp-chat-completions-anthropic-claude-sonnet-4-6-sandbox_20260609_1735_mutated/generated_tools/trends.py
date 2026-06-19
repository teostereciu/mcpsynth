"""Mastodon trends API tools."""
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
    def get_trending_tags(limit: Optional[int] = None, offset: Optional[int] = None) -> list:
        """Get hashtags that are trending on this instance.

        Args:
            limit: Maximum number of results (default 10, max 20).
            offset: Skip the first n results.
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            if offset is not None:
                params["offset"] = offset
            resp = requests.get(_api("/api/v1/trends/tags"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_trending_statuses(limit: Optional[int] = None, offset: Optional[int] = None) -> list:
        """Get statuses that are trending on this instance.

        Args:
            limit: Maximum number of results (default 20, max 40).
            offset: Skip the first n results.
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            if offset is not None:
                params["offset"] = offset
            resp = requests.get(_api("/api/v1/trends/statuses"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_trending_links(limit: Optional[int] = None, offset: Optional[int] = None) -> list:
        """Get links (articles) that are trending on this instance.

        Args:
            limit: Maximum number of results (default 10, max 20).
            offset: Skip the first n results.
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            if offset is not None:
                params["offset"] = offset
            resp = requests.get(_api("/api/v1/trends/links"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]
