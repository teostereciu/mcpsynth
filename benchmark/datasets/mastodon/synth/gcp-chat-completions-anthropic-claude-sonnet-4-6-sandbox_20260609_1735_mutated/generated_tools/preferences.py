"""Mastodon preferences API tools."""
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
    def get_preferences() -> dict:
        """Get the authenticated user's preferences (default post visibility, language, etc.)."""
        try:
            resp = requests.get(_api("/api/v1/preferences"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
