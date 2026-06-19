"""Mastodon suggestions API tools."""
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
    def get_follow_suggestions(limit: Optional[int] = None) -> list:
        """Get suggested accounts to follow (v2 — includes source reason).

        Args:
            limit: Maximum number of results (default 40, max 80).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v2/suggestions"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def remove_follow_suggestion(account_id: str) -> dict:
        """Remove an account from follow suggestions.

        Args:
            account_id: The ID of the account to remove from suggestions.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/suggestions/{account_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
