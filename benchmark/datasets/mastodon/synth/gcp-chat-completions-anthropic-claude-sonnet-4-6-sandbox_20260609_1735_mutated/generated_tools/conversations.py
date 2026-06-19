"""Mastodon conversations API tools."""
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
    def get_conversations(limit: Optional[int] = None) -> list:
        """Get direct message conversations for the authenticated user.

        Args:
            limit: Maximum number of results (default 20, max 40).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/conversations"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def delete_conversation(conversation_id: str) -> dict:
        """Remove a conversation from your conversation list.

        Args:
            conversation_id: The ID of the conversation to remove.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/conversations/{conversation_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def mark_conversation_read(conversation_id: str) -> dict:
        """Mark a conversation as read.

        Args:
            conversation_id: The ID of the conversation to mark as read.
        """
        try:
            resp = requests.post(_api(f"/api/v1/conversations/{conversation_id}/read"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
