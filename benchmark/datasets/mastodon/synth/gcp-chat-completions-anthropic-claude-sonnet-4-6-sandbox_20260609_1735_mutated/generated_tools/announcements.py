"""Mastodon announcements API tools."""
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
    def get_announcements() -> list:
        """Get all currently active announcements from the instance admins."""
        try:
            resp = requests.get(_api("/api/v1/announcements"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def dismiss_announcement(announcement_id: str) -> dict:
        """Mark an announcement as read/dismissed.

        Args:
            announcement_id: The ID of the announcement to dismiss.
        """
        try:
            resp = requests.post(_api(f"/api/v1/announcements/{announcement_id}/dismiss"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def add_announcement_reaction(announcement_id: str, emoji_name: str) -> dict:
        """React to an announcement with an emoji.

        Args:
            announcement_id: The ID of the announcement.
            emoji_name: Unicode emoji character or custom emoji shortcode.
        """
        try:
            resp = requests.put(
                _api(f"/api/v1/announcements/{announcement_id}/reactions/{emoji_name}"),
                headers=_headers(),
            )
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_announcement_reaction(announcement_id: str, emoji_name: str) -> dict:
        """Remove an emoji reaction from an announcement.

        Args:
            announcement_id: The ID of the announcement.
            emoji_name: Unicode emoji character or custom emoji shortcode.
        """
        try:
            resp = requests.delete(
                _api(f"/api/v1/announcements/{announcement_id}/reactions/{emoji_name}"),
                headers=_headers(),
            )
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
