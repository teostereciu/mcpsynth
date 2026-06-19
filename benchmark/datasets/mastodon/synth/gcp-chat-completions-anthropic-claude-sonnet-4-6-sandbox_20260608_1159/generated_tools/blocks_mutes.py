"""Mastodon Blocks, Mutes, Follow Requests, and Tags API tools."""
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


def register_blocks_mutes(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_blocks(limit: Optional[int] = None) -> list:
        """Get accounts blocked by the authenticated user."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api("/api/v1/blocks"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_mutes(limit: Optional[int] = None) -> list:
        """Get accounts muted by the authenticated user."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api("/api/v1/mutes"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_follow_requests(limit: Optional[int] = None) -> list:
        """Get pending follow requests for the authenticated user."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api("/api/v1/follow_requests"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def accept_follow_request(account_id: str) -> dict:
        """Accept a follow request from an account."""
        try:
            r = requests.post(_api(f"/api/v1/follow_requests/{account_id}/authorize"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def reject_follow_request(account_id: str) -> dict:
        """Reject a follow request from an account."""
        try:
            r = requests.post(_api(f"/api/v1/follow_requests/{account_id}/reject"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_tag(tag_name: str) -> dict:
        """Get information about a hashtag by name (without the # symbol)."""
        try:
            r = requests.get(_api(f"/api/v1/tags/{tag_name}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def follow_tag(tag_name: str) -> dict:
        """Follow a hashtag so posts with it appear in your home timeline."""
        try:
            r = requests.post(_api(f"/api/v1/tags/{tag_name}/follow"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfollow_tag(tag_name: str) -> dict:
        """Unfollow a hashtag."""
        try:
            r = requests.post(_api(f"/api/v1/tags/{tag_name}/unfollow"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
