"""Mastodon tags API tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register(mcp: FastMCP):

    @mcp.tool()
    def get_tag(tag_name: str) -> dict:
        """Get information about a hashtag.

        Args:
            tag_name: The name of the hashtag (case-insensitive, without #).
        """
        try:
            resp = requests.get(_api(f"/api/v1/tags/{tag_name}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def follow_tag(tag_name: str) -> dict:
        """Follow a hashtag so its posts appear in your home timeline.

        Args:
            tag_name: The name of the hashtag to follow (case-insensitive, without #).
        """
        try:
            resp = requests.post(_api(f"/api/v1/tags/{tag_name}/follow"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfollow_tag(tag_name: str) -> dict:
        """Unfollow a hashtag.

        Args:
            tag_name: The name of the hashtag to unfollow (case-insensitive, without #).
        """
        try:
            resp = requests.post(_api(f"/api/v1/tags/{tag_name}/unfollow"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_followed_tags() -> list:
        """Get all hashtags followed by the authenticated user."""
        try:
            resp = requests.get(_api("/api/v1/followed_tags"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]
