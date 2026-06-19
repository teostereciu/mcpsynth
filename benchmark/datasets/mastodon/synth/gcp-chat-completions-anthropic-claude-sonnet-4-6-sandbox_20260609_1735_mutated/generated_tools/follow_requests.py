"""Mastodon follow requests API tools."""
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
    def get_follow_requests(limit: Optional[int] = None) -> list:
        """Get pending follow requests for the authenticated user.

        Args:
            limit: Maximum number of results (default 40, max 80).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/follow_requests"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def accept_follow_request(account_id: str) -> dict:
        """Accept a follow request from an account.

        Args:
            account_id: The ID of the account whose follow request to accept.
        """
        try:
            resp = requests.post(_api(f"/api/v1/follow_requests/{account_id}/authorize"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def reject_follow_request(account_id: str) -> dict:
        """Reject a follow request from an account.

        Args:
            account_id: The ID of the account whose follow request to reject.
        """
        try:
            resp = requests.post(_api(f"/api/v1/follow_requests/{account_id}/reject"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
