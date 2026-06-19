"""Mastodon markers API tools."""
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
    def get_markers(timelines: Optional[list] = None) -> dict:
        """Get saved timeline read positions (markers).

        Args:
            timelines: List of timelines to get markers for. Values: 'home', 'notifications'.
        """
        try:
            params = []
            if timelines:
                for t in timelines:
                    params.append(("timeline[]", t))
            resp = requests.get(_api("/api/v1/markers"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def save_markers(
        home_last_read_id: Optional[str] = None,
        notifications_last_read_id: Optional[str] = None,
    ) -> dict:
        """Save your current position in timelines.

        Args:
            home_last_read_id: ID of the last status read in the home timeline.
            notifications_last_read_id: ID of the last notification read.
        """
        try:
            data = {}
            if home_last_read_id:
                data["home[last_read_id]"] = home_last_read_id
            if notifications_last_read_id:
                data["notifications[last_read_id]"] = notifications_last_read_id
            resp = requests.post(_api("/api/v1/markers"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
