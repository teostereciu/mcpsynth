"""Mastodon domain blocks API tools."""
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
    def get_domain_blocks(limit: Optional[int] = None) -> list:
        """Get domains blocked by the authenticated user.

        Args:
            limit: Maximum number of results (default 100, max 200).
        """
        try:
            params = {}
            if limit is not None:
                params["limit"] = limit
            resp = requests.get(_api("/api/v1/domain_blocks"), headers=_headers(), params=params)
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def block_domain(domain: str) -> dict:
        """Block a domain to hide all its content and interactions.

        Args:
            domain: The domain name to block (e.g. 'example.social').
        """
        try:
            data = {"domain": domain}
            resp = requests.post(_api("/api/v1/domain_blocks"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unblock_domain(domain: str) -> dict:
        """Unblock a previously blocked domain.

        Args:
            domain: The domain name to unblock.
        """
        try:
            data = {"domain": domain}
            resp = requests.delete(_api("/api/v1/domain_blocks"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
