"""Mastodon Instance API tools."""
import os
import requests
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


def register_instance(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_instance() -> dict:
        """Get general information about the Mastodon server (v2: includes configuration, rules, etc.)."""
        try:
            r = requests.get(_api("/api/v2/instance"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_instance_rules() -> list:
        """Get the rules of the Mastodon instance."""
        try:
            r = requests.get(_api("/api/v1/instance/rules"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_instance_peers() -> list:
        """Get domains that this instance is aware of (federated peers)."""
        try:
            r = requests.get(_api("/api/v1/instance/peers"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_instance_activity() -> list:
        """Get weekly activity statistics for this instance."""
        try:
            r = requests.get(_api("/api/v1/instance/activity"), headers=_headers())
            return r.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def get_instance_extended_description() -> dict:
        """Get the extended description of the instance."""
        try:
            r = requests.get(_api("/api/v1/instance/extended_description"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}
