"""Mastodon Lists API tools."""
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


def register_lists(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_lists() -> list:
        """Get all lists owned by the authenticated user."""
        try:
            r = requests.get(_api("/api/v1/lists"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_list(list_id: str) -> dict:
        """Get a single list by ID."""
        try:
            r = requests.get(_api(f"/api/v1/lists/{list_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_list(
        title: str,
        replies_policy: Optional[str] = None,
        exclusive: Optional[bool] = None,
    ) -> dict:
        """Create a new list. replies_policy: 'followed', 'list', or 'none'."""
        data: dict = {"title": title}
        if replies_policy:
            data["replies_policy"] = replies_policy
        if exclusive is not None:
            data["exclusive"] = str(exclusive).lower()
        try:
            r = requests.post(_api("/api/v1/lists"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_list(
        list_id: str,
        title: str,
        replies_policy: Optional[str] = None,
        exclusive: Optional[bool] = None,
    ) -> dict:
        """Update a list's title and/or replies_policy."""
        data: dict = {"title": title}
        if replies_policy:
            data["replies_policy"] = replies_policy
        if exclusive is not None:
            data["exclusive"] = str(exclusive).lower()
        try:
            r = requests.put(_api(f"/api/v1/lists/{list_id}"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_list(list_id: str) -> dict:
        """Delete a list by ID."""
        try:
            r = requests.delete(_api(f"/api/v1/lists/{list_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_list_accounts(list_id: str, limit: Optional[int] = None) -> list:
        """Get accounts in a list."""
        params: dict = {}
        if limit is not None:
            params["limit"] = limit
        try:
            r = requests.get(_api(f"/api/v1/lists/{list_id}/accounts"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def add_accounts_to_list(list_id: str, account_ids: list) -> dict:
        """Add accounts to a list. account_ids: list of account ID strings."""
        try:
            data = [("account_ids[]", aid) for aid in account_ids]
            r = requests.post(_api(f"/api/v1/lists/{list_id}/accounts"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
        """Remove accounts from a list. account_ids: list of account ID strings."""
        try:
            params = [("account_ids[]", aid) for aid in account_ids]
            r = requests.delete(_api(f"/api/v1/lists/{list_id}/accounts"), params=params, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
