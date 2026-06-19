"""Mastodon Media API tools."""
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


def register_media(mcp: FastMCP) -> None:

    @mcp.tool()
    def upload_media(
        file_path: str,
        description: Optional[str] = None,
        focus: Optional[str] = None,
    ) -> dict:
        """Upload a media attachment from a local file path. Returns a MediaAttachment with an ID to use in post_status.
        description: alt text for accessibility. focus: 'x,y' floats from -1.0 to 1.0."""
        h = _headers()
        # Remove Accept header for multipart; requests will set it
        data = {}
        if description:
            data["description"] = description
        if focus:
            data["focus"] = focus
        try:
            with open(file_path, "rb") as f:
                files = {"file": f}
                r = requests.post(_api("/api/v2/media"), data=data, files=files, headers=h)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_media(media_id: str) -> dict:
        """Get a media attachment by ID (to check processing status)."""
        try:
            r = requests.get(_api(f"/api/v1/media/{media_id}"), headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_media(
        media_id: str,
        description: Optional[str] = None,
        focus: Optional[str] = None,
    ) -> dict:
        """Update a media attachment's description or focus point before posting."""
        data = {}
        if description is not None:
            data["description"] = description
        if focus is not None:
            data["focus"] = focus
        try:
            r = requests.put(_api(f"/api/v1/media/{media_id}"), data=data, headers=_headers())
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_media(media_id: str) -> dict:
        """Delete a media attachment that is not yet attached to a status."""
        try:
            r = requests.delete(_api(f"/api/v1/media/{media_id}"), headers=_headers())
            if r.status_code == 200:
                try:
                    return r.json()
                except Exception:
                    return {"status": "deleted"}
            return {"error": f"HTTP {r.status_code}", "body": r.text}
        except Exception as e:
            return {"error": str(e)}
