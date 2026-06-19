"""Mastodon polls API tools."""
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
    def get_poll(poll_id: str) -> dict:
        """Get a poll attached to a status.

        Args:
            poll_id: The ID of the poll.
        """
        try:
            resp = requests.get(_api(f"/api/v1/polls/{poll_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def vote_on_poll(poll_id: str, choices: list) -> dict:
        """Vote on a poll.

        Args:
            poll_id: The ID of the poll.
            choices: List of integer indices (0-based) of the options to vote for.
        """
        try:
            data = [("choices[]", c) for c in choices]
            resp = requests.post(_api(f"/api/v1/polls/{poll_id}/votes"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
