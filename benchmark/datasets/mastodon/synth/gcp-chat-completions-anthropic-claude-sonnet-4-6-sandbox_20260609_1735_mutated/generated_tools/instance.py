"""Mastodon instance API tools."""
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
    def get_instance() -> dict:
        """Get general information and statistics about the Mastodon server (v2)."""
        try:
            resp = requests.get(_api("/api/v2/instance"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_instance_peers() -> list:
        """Get list of domains that this instance is aware of."""
        try:
            resp = requests.get(_api("/api/v1/instance/peers"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_instance_activity() -> list:
        """Get weekly activity statistics for this instance (last 12 weeks)."""
        try:
            resp = requests.get(_api("/api/v1/instance/activity"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_instance_rules() -> list:
        """Get the rules of this Mastodon instance."""
        try:
            resp = requests.get(_api("/api/v1/instance/rules"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_instance_extended_description() -> dict:
        """Get the extended description of this Mastodon instance."""
        try:
            resp = requests.get(_api("/api/v1/instance/extended_description"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
