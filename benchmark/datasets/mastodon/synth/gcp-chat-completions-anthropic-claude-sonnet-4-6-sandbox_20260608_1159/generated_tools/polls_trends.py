"""Mastodon Polls, Trends, Followed Tags, and Preferences API tools."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers() -> dict:
    h = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        h["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    return h


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register_polls_trends(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_poll(poll_id: str) -> dict:
        """Get a poll attached to a status by poll ID."""
        try:
            r = requests.get(_api(f"/api/v1/polls/{poll_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def vote_on_poll(poll_id: str, choices: list) -> dict:
        """Vote on a poll. choices: list of integer indices (0-based) for the options to vote for."""
        try:
            data = [("choices[]", c) for c in choices]
            r = requests.post(_api(f"/api/v1/polls/{poll_id}/votes"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_trending_tags(limit: Optional[int] = None, offset: Optional[int] = None) -> list:
        """Get hashtags that are trending on the instance."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        try:
            r = requests.get(_api("/api/v1/trends/tags"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_trending_statuses(limit: Optional[int] = None, offset: Optional[int] = None) -> list:
        """Get statuses that are trending on the instance."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        try:
            r = requests.get(_api("/api/v1/trends/statuses"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_trending_links(limit: Optional[int] = None, offset: Optional[int] = None) -> list:
        """Get links (articles) that are trending on the instance."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        try:
            r = requests.get(_api("/api/v1/trends/links"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_followed_tags(limit: Optional[int] = None) -> list:
        """Get all hashtags followed by the authenticated user."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api("/api/v1/followed_tags"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_preferences() -> dict:
        """Get the authenticated user's preferences (default visibility, language, etc.)."""
        try:
            r = requests.get(_api("/api/v1/preferences"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
