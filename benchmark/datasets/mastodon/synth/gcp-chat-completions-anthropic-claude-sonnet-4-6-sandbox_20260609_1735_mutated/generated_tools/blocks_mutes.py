"""Mastodon blocks and mutes list API tools."""
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
    def get_blocks(limit: Optional[int] = None) -> list:
        """Get accounts blocked by the authenticated user.

        Args:
            limit: Maximum number of results (default 40, max 80).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/blocks"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_mutes(limit: Optional[int] = None) -> list:
        """Get accounts muted by the authenticated user.

        Args:
            limit: Maximum number of results (default 40, max 80).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/mutes"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]
