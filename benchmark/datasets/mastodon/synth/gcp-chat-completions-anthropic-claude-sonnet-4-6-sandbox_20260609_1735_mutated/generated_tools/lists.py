"""Mastodon lists API tools."""
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
    def get_lists() -> list:
        """Get all lists owned by the authenticated user."""
        try:
            resp = requests.get(_api("/api/v1/lists"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_list(list_id: str) -> dict:
        """Get a single list by ID.

        Args:
            list_id: The ID of the list.
        """
        try:
            resp = requests.get(_api(f"/api/v1/lists/{list_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_list(
        title: str,
        replies_policy: Optional[str] = None,
        exclusive: Optional[bool] = None,
    ) -> dict:
        """Create a new list.

        Args:
            title: The title of the list.
            replies_policy: One of 'followed', 'list', or 'none'. Defaults to 'list'.
            exclusive: Whether list members are removed from the Home feed.
        """
        try:
            data = {"title": title}
            if replies_policy:
                data["replies_policy"] = replies_policy
            if exclusive is not None:
                data["exclusive"] = str(exclusive).lower()
            resp = requests.post(_api("/api/v1/lists"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_list(
        list_id: str,
        title: str,
        replies_policy: Optional[str] = None,
        exclusive: Optional[bool] = None,
    ) -> dict:
        """Update an existing list.

        Args:
            list_id: The ID of the list to update.
            title: The new title of the list.
            replies_policy: One of 'followed', 'list', or 'none'.
            exclusive: Whether list members are removed from the Home feed.
        """
        try:
            data = {"title": title}
            if replies_policy:
                data["replies_policy"] = replies_policy
            if exclusive is not None:
                data["exclusive"] = str(exclusive).lower()
            resp = requests.put(_api(f"/api/v1/lists/{list_id}"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_list(list_id: str) -> dict:
        """Delete a list.

        Args:
            list_id: The ID of the list to delete.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/lists/{list_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_list_accounts(list_id: str, limit: Optional[int] = None) -> list:
        """Get accounts in a list.

        Args:
            list_id: The ID of the list.
            limit: Maximum number of results (default 40, max 80; 0 = all).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api(f"/api/v1/lists/{list_id}/accounts"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
        """Add accounts to a list.

        Args:
            list_id: The ID of the list.
            account_ids: List of account IDs to add (must be following them).
        """
        try:
            data = [("account_ids[]", aid) for aid in account_ids]
            resp = requests.post(_api(f"/api/v1/lists/{list_id}/accounts"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
        """Remove accounts from a list.

        Args:
            list_id: The ID of the list.
            account_ids: List of account IDs to remove.
        """
        try:
            data = [("account_ids[]", aid) for aid in account_ids]
            resp = requests.delete(_api(f"/api/v1/lists/{list_id}/accounts"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
