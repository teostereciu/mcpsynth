"""Mastodon featured tags API tools."""
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
    def get_featured_tags() -> list:
        """Get hashtags featured on the authenticated user's profile."""
        try:
            resp = requests.get(_api("/api/v1/featured_tags"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]

    @mcp.tool()
    def feature_tag(name: str) -> dict:
        """Feature a hashtag on your profile.

        Args:
            name: The hashtag name to feature (without the # symbol).
        """
        try:
            data = {"name": name}
            resp = requests.post(_api("/api/v1/featured_tags"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfeature_tag(featured_tag_id: str) -> dict:
        """Remove a featured hashtag from your profile.

        Args:
            featured_tag_id: The ID of the FeaturedTag to remove.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/featured_tags/{featured_tag_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_featured_tag_suggestions() -> list:
        """Get up to 10 recently-used hashtags as suggestions to feature."""
        try:
            resp = requests.get(_api("/api/v1/featured_tags/suggestions"), headers=_headers())
            return resp.json()
        except Exception as e:
            return [{"error": str(e)}]
